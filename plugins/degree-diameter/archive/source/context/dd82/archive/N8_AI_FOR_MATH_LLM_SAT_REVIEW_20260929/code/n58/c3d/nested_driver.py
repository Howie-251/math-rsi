#!/usr/bin/env python3
"""Coverage-preserving nested enumeration for one live 3D parity root.

The driver deliberately separates three finite searches:

``phase primary bits -> anonymous block multiplicities -> H_R``.

A SAT child is never interpreted as closing its parent.  Completed or exactly
pruned child states are excluded from the parent formula by a clause over that
layer's primary variables only.  Auxiliary cardinality, conjunction, and
connectivity variables never occur in a blocking clause.
"""

from __future__ import annotations

import argparse
import fcntl
import filecmp
import json
import os
import shlex
import shutil
import subprocess
import sys
import time
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

from sat58.v3.c3d.audits import TheoryPrune
from sat58.v3.c3d.coverage import audit_state_document
from sat58.v3.c3d.block_cover import (
    decode_block_cover_model,
    generate as generate_block_cover,
)
from sat58.v3.c3d.hr_encoder import generate as generate_hr
from sat58.v3.c3d.phase import decode_phase_model, generate as generate_phase
from sat58.v3.c3d.tables import DEFAULT_TABLES_PATH, root_by_index
from sat58.v3.c3d.verify_hr_model import verify_model as verify_hr_model
from sat59.solver_output import SatAssignment, load_sat_solver_output


STATE_FORMAT = "n58-v3-3d-nested-state-v1"
TERMINAL_ROOT = {"RAW_CLOSED", "SAT_VERIFIED", "ERROR"}
BLOCKED_CHILD = {"EXACT_PRUNE", "RAW_CLOSED"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _write_json_atomic(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def _read_header(path: Path) -> tuple[int, int]:
    with path.open("r", encoding="ascii") as handle:
        line = handle.readline().strip()
    fields = line.split()
    if len(fields) != 4 or fields[:2] != ["p", "cnf"]:
        raise ValueError(f"{path} does not begin with a DIMACS header")
    return int(fields[2]), int(fields[3])


def materialize_with_blockers(
    base_path: Path,
    target_path: Path,
    blockers: Sequence[Sequence[int]],
) -> dict:
    """Copy ``base_path`` and append exact primary-state blocking clauses."""

    variables, clauses = _read_header(base_path)
    normalized = [tuple(map(int, clause)) for clause in blockers]
    if any(not clause for clause in normalized):
        raise ValueError("a nested-enumeration blocker may not be empty")
    if any(literal == 0 or abs(literal) > variables for row in normalized for literal in row):
        raise ValueError("a blocker contains an invalid DIMACS literal")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = target_path.with_name(f".{target_path.name}.tmp-{os.getpid()}")
    with base_path.open("r", encoding="ascii") as source, temporary.open(
        "w", encoding="ascii"
    ) as target:
        source.readline()
        target.write(f"p cnf {variables} {clauses + len(normalized)}\n")
        for line in source:
            target.write(line)
        for clause in normalized:
            target.write(" ".join(map(str, clause)) + " 0\n")
    os.replace(temporary, target_path)
    return {
        "variables": variables,
        "base_clauses": clauses,
        "blocking_clauses": len(normalized),
        "clauses": clauses + len(normalized),
        "bytes": target_path.stat().st_size,
    }


def _solver_status(path: Path) -> str:
    statuses: set[str] = set()
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        fields = raw.strip().upper().split()
        if len(fields) < 2 or fields[0] != "S":
            continue
        if fields[1] == "SATISFIABLE":
            statuses.add("SAT")
        elif fields[1] == "UNSATISFIABLE":
            statuses.add("UNSAT")
        elif fields[1] == "UNKNOWN":
            statuses.add("UNKNOWN")
    if len(statuses) > 1:
        return "CONFLICTING"
    return next(iter(statuses), "UNKNOWN")


def _primary_state(
    assignment: SatAssignment, variables: Sequence[int], label: str
) -> tuple[int, ...]:
    normalized = tuple(map(int, variables))
    if len(normalized) != len(set(normalized)) or any(variable <= 0 for variable in normalized):
        raise ValueError(f"{label} variables must be distinct and positive")
    assignment.require_assigned(normalized, label)
    return tuple(
        variable if variable in assignment.positive_variables else -variable
        for variable in normalized
    )


def _phase_primary_variables(map_path: Path) -> tuple[int, ...]:
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    if mapping.get("schema_version") != "sat58-v3-3d-phase-map-v1":
        raise ValueError("not a V3 3D phase map")
    return tuple(int(row["variable"]) for row in mapping["phase_high_bits"])


def _block_primary_variables(map_path: Path) -> tuple[int, ...]:
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    if mapping.get("schema_version") != "sat58-v3-3d-block-cover-map-v1":
        raise ValueError("not a V3 3D block-cover map")
    return tuple(
        int(variable)
        for row in mapping["allowed_blocks"]
        for variable in row["count_ge_variables"]
    )


def _hr_primary_variables(map_path: Path) -> tuple[int, ...]:
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    if mapping.get("encoding") != "sat58-v3-3d-hr-realization-v1":
        raise ValueError("not a V3 3D H_R map")
    return tuple(int(row["var"]) for row in mapping["edge_variables"])


class NestedParityDriver:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.run_dir = args.run_dir.resolve()
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self._lock_handle = (self.run_dir / ".nested-driver.lock").open("a+")
        try:
            fcntl.flock(self._lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            self._lock_handle.close()
            raise ValueError("another nested driver already owns this run directory") from error
        self.tables_source = Path(args.tables).resolve()
        self.tables_snapshot = self.run_dir / "inputs" / "n58_v3_frontend_tables.json"
        self.state_path = self.run_dir / "state.json"
        self.summary_path = self.run_dir / "summary.json"
        self.phase_dir = self.run_dir / "phase_root"
        self.phase_cnf = self.phase_dir / "base.cnf"
        self.phase_map = self.phase_dir / "base.map.json"
        self.phase_stats = self.phase_dir / "base.stats.json"
        self.session_started = time.monotonic()
        self.deadline = self.session_started + args.session_seconds
        self.session_calls = 0
        if self.state_path.exists():
            if not args.resume:
                raise ValueError("state.json already exists; pass --resume")
            self.state = json.loads(self.state_path.read_text(encoding="utf-8"))
            self._validate_resume()
        else:
            if args.resume:
                raise ValueError("--resume requested but state.json does not exist")
            self.state = self._initialize()
        self.state.setdefault("sessions", []).append(
            {
                "session": len(self.state.get("sessions", ())) + 1,
                "started_at_utc": utc_now(),
                "solver": str(args.solver),
                "solver_args": list(args.solver_arg),
                "timeout_seconds": args.timeout_seconds,
                "session_seconds": args.session_seconds,
                "max_solver_calls": args.max_solver_calls,
                "resume": bool(args.resume),
            }
        )
        self._save()

    def _initialize(self) -> dict:
        self.tables_snapshot.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(self.tables_source, self.tables_snapshot)
        root = root_by_index(self.args.root_index, self.tables_snapshot, require_live=True)
        generated = generate_phase(
            root_index=self.args.root_index,
            tables_path=self.tables_snapshot,
            cnf_path=self.phase_cnf,
            map_path=self.phase_map,
            stats_path=self.phase_stats,
        )
        root_node = {
            "node_id": root.branch_id,
            "kind": "PARITY_ROOT",
            "parent_id": None,
            "children": [],
            "status": "OPEN",
            "enumeration_attempts": [],
            "phase_primary_variables": list(_phase_primary_variables(self.phase_map)),
            "base_cnf": str(self.phase_cnf),
            "map": str(self.phase_map),
            "stats": str(self.phase_stats),
        }
        return {
            "format": STATE_FORMAT,
            "created_at_utc": utc_now(),
            "updated_at_utc": utc_now(),
            "root_index": self.args.root_index,
            "root_id": root.branch_id,
            "tables_source": str(self.tables_source),
            "tables_snapshot": str(self.tables_snapshot),
            "tables_bytes": self.tables_snapshot.stat().st_size,
            "status": "OPEN",
            "solver_calls": 0,
            "next_phase_number": 1,
            "next_block_number": 1,
            "next_hr_number": 1,
            "phase_formula": generated,
            "nodes": {root.branch_id: root_node},
            "sessions": [],
        }

    def _validate_resume(self) -> None:
        if self.state.get("format") != STATE_FORMAT:
            raise ValueError("unsupported nested-driver state format")
        if int(self.state.get("root_index", -1)) != self.args.root_index:
            raise ValueError("resume root index differs from state.json")
        if not self.tables_source.is_file() or not self.tables_snapshot.is_file():
            raise ValueError("resume table source or frozen snapshot is missing")
        if self.tables_snapshot.stat().st_size != int(self.state.get("tables_bytes", -1)):
            raise ValueError("frozen table snapshot byte count differs from state.json")
        if not filecmp.cmp(self.tables_source, self.tables_snapshot, shallow=False):
            raise ValueError("current table differs byte-for-byte from the frozen run snapshot")
        root = root_by_index(self.args.root_index, self.tables_snapshot, require_live=True)
        if self.state.get("root_id") != root.branch_id:
            raise ValueError("resume root id differs from current frozen table")
        for required in (self.phase_cnf, self.phase_map, self.phase_stats):
            if not required.is_file():
                raise ValueError(f"resume artifact is missing: {required}")
        if len(_phase_primary_variables(self.phase_map)) != 36:
            raise ValueError("resume phase map no longer has 36 primary bits")
        with tempfile.TemporaryDirectory(prefix="resume-audit-", dir=self.run_dir) as directory:
            temporary = Path(directory)
            generate_phase(
                root_index=self.args.root_index,
                tables_path=self.tables_snapshot,
                cnf_path=temporary / "base.cnf",
                map_path=temporary / "base.map.json",
            )
            if not filecmp.cmp(self.phase_cnf, temporary / "base.cnf", shallow=False):
                raise ValueError("phase base CNF differs from deterministic regeneration")
            if not filecmp.cmp(self.phase_map, temporary / "base.map.json", shallow=False):
                raise ValueError("phase map differs from deterministic regeneration")
        audit_state_document(self.state)

    def close(self) -> None:
        handle = getattr(self, "_lock_handle", None)
        if handle is not None and not handle.closed:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
            handle.close()

    @property
    def nodes(self) -> dict[str, dict]:
        return self.state["nodes"]

    @property
    def root(self) -> dict:
        return self.nodes[self.state["root_id"]]

    def _save(self) -> None:
        self.state["updated_at_utc"] = utc_now()
        self.state["status"] = self.root["status"]
        _write_json_atomic(self.state_path, self.state)
        _write_json_atomic(self.summary_path, self.summary())

    def summary(self) -> dict:
        counts: dict[str, int] = {}
        kinds: dict[str, int] = {}
        for node in self.nodes.values():
            counts[node["status"]] = counts.get(node["status"], 0) + 1
            kinds[node["kind"]] = kinds.get(node["kind"], 0) + 1
        return {
            "format": "n58-v3-3d-nested-summary-v1",
            "root_id": self.state["root_id"],
            "root_index": self.state["root_index"],
            "status": self.root["status"],
            "solver_calls": self.state["solver_calls"],
            "node_kinds": dict(sorted(kinds.items())),
            "node_statuses": dict(sorted(counts.items())),
            "phase_states_seen": len(self.root["children"]),
            "active_path": self._active_path(),
            "coverage_audit": audit_state_document(self.state),
            "updated_at_utc": self.state.get("updated_at_utc"),
        }

    def _active_path(self) -> list[str]:
        path = [self.root["node_id"]]
        phases = [self.nodes[node_id] for node_id in self.root["children"] if self.nodes[node_id]["status"] == "OPEN"]
        if not phases:
            return path
        if len(phases) != 1:
            raise ValueError("state has more than one active phase")
        phase = phases[0]
        path.append(phase["node_id"])
        blocks = [self.nodes[node_id] for node_id in phase["children"] if self.nodes[node_id]["status"] == "OPEN"]
        if not blocks:
            return path
        if len(blocks) != 1:
            raise ValueError("state has more than one active block state")
        block = blocks[0]
        path.append(block["node_id"])
        hrs = [self.nodes[node_id] for node_id in block["children"] if self.nodes[node_id]["status"] == "OPEN"]
        if hrs:
            if len(hrs) != 1:
                raise ValueError("block state has more than one active H_R child")
            path.append(hrs[0]["node_id"])
        return path

    def _phase_blockers(self) -> list[list[int]]:
        return [
            self.nodes[node_id]["blocking_clause"]
            for node_id in self.root["children"]
            if self.nodes[node_id]["status"] in BLOCKED_CHILD
        ]

    def _block_blockers(self, phase: dict) -> list[list[int]]:
        return [
            self.nodes[node_id]["blocking_clause"]
            for node_id in phase["children"]
            if self.nodes[node_id]["status"] in BLOCKED_CHILD
        ]

    def _hr_blockers(self, hr: dict) -> list[list[int]]:
        return [
            self.nodes[node_id]["blocking_clause"]
            for node_id in hr["children"]
            if self.nodes[node_id]["status"] == "EXACT_PRUNE"
        ]

    def _blocked_child_ids(self, stage: str, node: dict) -> list[str]:
        if stage in {"PHASE", "BLOCK"}:
            accepted = BLOCKED_CHILD
        elif stage == "H_R":
            accepted = {"EXACT_PRUNE"}
        else:
            raise ValueError(f"unknown nested solver stage {stage!r}")
        return [
            node_id
            for node_id in node["children"]
            if self.nodes[node_id]["status"] in accepted
        ]

    def _can_call_solver(self) -> bool:
        return (
            self.session_calls < self.args.max_solver_calls
            and time.monotonic() < self.deadline
        )

    def _solve(
        self,
        *,
        stage: str,
        node: dict,
        base_cnf: Path,
        working_cnf: Path,
        blockers: Sequence[Sequence[int]],
    ) -> tuple[str, Path]:
        if not self._can_call_solver():
            return "SESSION_LIMIT", working_cnf
        blocked_child_ids = self._blocked_child_ids(stage, node)
        if len(blocked_child_ids) != len(blockers):
            raise ValueError(
                f"{stage} blocker count does not match the closed-child ledger"
            )
        for child_id, blocker in zip(blocked_child_ids, blockers, strict=True):
            if list(blocker) != list(self.nodes[child_id]["blocking_clause"]):
                raise ValueError(
                    f"{stage} blocker order differs from child ledger at {child_id}"
                )
        dimensions = materialize_with_blockers(base_cnf, working_cnf, blockers)
        call_id = int(self.state["solver_calls"]) + 1
        attempt_dir = self.run_dir / "attempts" / f"{call_id:08d}_{stage.lower()}"
        attempt_dir.mkdir(parents=True, exist_ok=True)
        solver_log = attempt_dir / "solver.log"
        command = [str(self.args.solver), *self.args.solver_arg, str(working_cnf)]
        attempt = {
            "call_id": call_id,
            "stage": stage,
            "node_id": node["node_id"],
            "started_at_utc": utc_now(),
            "command": command,
            "command_text": shlex.join(command),
            "base_cnf": str(base_cnf),
            "working_cnf": str(working_cnf),
            "blocker_count": len(blockers),
            "residual_revision": len(blockers),
            "blocked_child_ids": blocked_child_ids,
            "dimensions": dimensions,
            "solver_log": str(solver_log),
            "timeout_seconds": min(
                self.args.timeout_seconds,
                max(0.0, self.deadline - time.monotonic()),
            ),
        }
        started = time.monotonic()
        try:
            completed = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=attempt["timeout_seconds"],
                check=False,
                env={
                    **os.environ,
                    "OMP_NUM_THREADS": "1",
                    "OPENBLAS_NUM_THREADS": "1",
                    "MKL_NUM_THREADS": "1",
                },
            )
            solver_log.write_text(completed.stdout, encoding="utf-8")
            status = _solver_status(solver_log)
            attempt["return_code"] = completed.returncode
            if (status == "SAT" and completed.returncode not in (0, 10)) or (
                status == "UNSAT" and completed.returncode not in (0, 20)
            ):
                status = "BAD_EXIT"
        except subprocess.TimeoutExpired as error:
            output = error.stdout or ""
            if isinstance(output, bytes):
                output = output.decode("utf-8", errors="replace")
            solver_log.write_text(output, encoding="utf-8")
            status = "TIMEOUT"
            attempt["return_code"] = None
        attempt["status"] = status
        attempt["wall_seconds"] = round(time.monotonic() - started, 6)
        attempt["finished_at_utc"] = utc_now()
        node.setdefault("enumeration_attempts", []).append(attempt)
        self.state["solver_calls"] = call_id
        self.session_calls += 1
        self._save()
        return status, solver_log

    def _new_phase(self, primary_state: Sequence[int], model: Path) -> dict:
        number = int(self.state["next_phase_number"])
        self.state["next_phase_number"] = number + 1
        node_id = f"{self.root['node_id']}::phase-{number:06d}"
        directory = self.run_dir / "phases" / f"{number:06d}"
        directory.mkdir(parents=True, exist_ok=True)
        node = {
            "node_id": node_id,
            "kind": "PHASE_STATE",
            "parent_id": self.root["node_id"],
            "children": [],
            "status": "OPEN",
            "primary_state": list(primary_state),
            "blocking_clause": [-literal for literal in primary_state],
            "source_model": str(model),
            "directory": str(directory),
            "enumeration_attempts": [],
        }
        self.nodes[node_id] = node
        self.root["children"].append(node_id)
        return node

    def _new_block(self, phase: dict, primary_state: Sequence[int], model: Path) -> dict:
        number = int(self.state["next_block_number"])
        self.state["next_block_number"] = number + 1
        node_id = f"{phase['node_id']}::block-{number:06d}"
        directory = Path(phase["directory"]) / "blocks" / f"{number:06d}"
        directory.mkdir(parents=True, exist_ok=True)
        node = {
            "node_id": node_id,
            "kind": "BLOCK_STATE",
            "parent_id": phase["node_id"],
            "children": [],
            "status": "OPEN",
            "primary_state": list(primary_state),
            "blocking_clause": [-literal for literal in primary_state],
            "source_model": str(model),
            "directory": str(directory),
        }
        self.nodes[node_id] = node
        phase["children"].append(node_id)
        return node

    def _new_hr(self, block: dict) -> dict:
        number = int(self.state["next_hr_number"])
        self.state["next_hr_number"] = number + 1
        node_id = f"{block['node_id']}::hr-{number:06d}"
        directory = Path(block["directory"]) / "hr"
        directory.mkdir(parents=True, exist_ok=True)
        node = {
            "node_id": node_id,
            "kind": "H_R_REALIZATION",
            "parent_id": block["node_id"],
            "children": [],
            "status": "OPEN",
            "directory": str(directory),
            "enumeration_attempts": [],
        }
        self.nodes[node_id] = node
        block["children"].append(node_id)
        return node

    def _new_hr_state(self, hr: dict, primary_state: Sequence[int], model: Path) -> dict:
        number = len(hr["children"]) + 1
        node_id = f"{hr['node_id']}::state-{number:06d}"
        node = {
            "node_id": node_id,
            "kind": "H_R_STATE",
            "parent_id": hr["node_id"],
            "children": [],
            "status": "OPEN",
            "primary_state": list(primary_state),
            "blocking_clause": [-literal for literal in primary_state],
            "source_model": str(model),
        }
        self.nodes[node_id] = node
        hr["children"].append(node_id)
        return node

    # These narrow wrappers make the state machine testable without replacing
    # any production encoding logic.
    def _decode_phase(self, model: Path, output: Path) -> dict:
        return decode_phase_model(
            model_path=model,
            map_path=self.phase_map,
            output_path=output,
            tables_path=self.tables_snapshot,
        )

    def _generate_block(self, phase_solution: Path, directory: Path) -> dict:
        return generate_block_cover(
            phase_path=phase_solution,
            tables_path=self.tables_snapshot,
            cnf_path=directory / "block.base.cnf",
            map_path=directory / "block.base.map.json",
            stats_path=directory / "block.base.stats.json",
        )

    def _decode_block(self, model: Path, map_path: Path, output: Path) -> dict:
        return decode_block_cover_model(
            model_path=model,
            map_path=map_path,
            output_path=output,
            tables_path=self.tables_snapshot,
        )

    def _generate_hr(self, cover: Path, directory: Path) -> dict:
        return generate_hr(
            cover_path=cover,
            tables_path=self.tables_snapshot,
            cnf_path=directory / "hr.base.cnf",
            map_path=directory / "hr.base.map.json",
            stats_path=directory / "hr.base.stats.json",
        )

    def _verify_hr(self, model: Path, map_path: Path) -> dict:
        return verify_hr_model(model, map_path, tables_path=self.tables_snapshot)

    def _solve_phase(self) -> str:
        status, model = self._solve(
            stage="PHASE",
            node=self.root,
            base_cnf=self.phase_cnf,
            working_cnf=self.phase_dir / "working.cnf",
            blockers=self._phase_blockers(),
        )
        if status == "UNSAT":
            self.root["status"] = "RAW_CLOSED"
            self.root["closure"] = {
                "kind": "EXHAUSTIVE_PHASE_ENUMERATION",
                "solver_call": self.state["solver_calls"],
                "blocked_phase_states": len(self._phase_blockers()),
            }
            self._save()
            return "PROGRESS"
        if status != "SAT":
            return status
        assignment = load_sat_solver_output(model)
        primary = _primary_state(
            assignment, self.root["phase_primary_variables"], "phase-primary"
        )
        if any(
            tuple(self.nodes[node_id].get("primary_state", ())) == primary
            for node_id in self.root["children"]
        ):
            raise ValueError("solver repeated an already recorded phase state")
        phase = self._new_phase(primary, model)
        solution = Path(phase["directory"]) / "phase.solution.json"
        try:
            document = self._decode_phase(model, solution)
        except TheoryPrune as error:
            phase["status"] = "EXACT_PRUNE"
            phase["exact_prune"] = str(error)
        except ValueError as error:
            phase["status"] = "DECODER_ERROR"
            phase["decoder_error"] = str(error)
            self.root["status"] = "ERROR"
            self._save()
            return "ERROR"
        else:
            phase["solution"] = str(solution)
            phase["audit"] = document.get("audit")
            generated = self._generate_block(solution, Path(phase["directory"]))
            phase["block_cnf"] = str(Path(phase["directory"]) / "block.base.cnf")
            phase["block_map"] = str(Path(phase["directory"]) / "block.base.map.json")
            phase["block_stats"] = str(Path(phase["directory"]) / "block.base.stats.json")
            phase["block_formula"] = generated
            phase["block_primary_variables"] = list(
                _block_primary_variables(Path(phase["block_map"]))
            )
        self._save()
        return "PROGRESS"

    def _solve_block(self, phase: dict) -> str:
        status, model = self._solve(
            stage="BLOCK",
            node=phase,
            base_cnf=Path(phase["block_cnf"]),
            working_cnf=Path(phase["directory"]) / "block.working.cnf",
            blockers=self._block_blockers(phase),
        )
        if status == "UNSAT":
            phase["status"] = "RAW_CLOSED"
            phase["closure"] = {
                "kind": "EXHAUSTIVE_BLOCK_ENUMERATION",
                "solver_call": self.state["solver_calls"],
                "blocked_block_states": len(self._block_blockers(phase)),
            }
            self._save()
            return "PROGRESS"
        if status != "SAT":
            return status
        assignment = load_sat_solver_output(model)
        primary = _primary_state(
            assignment, phase["block_primary_variables"], "block-multiplicity-primary"
        )
        if any(
            tuple(self.nodes[node_id].get("primary_state", ())) == primary
            for node_id in phase["children"]
        ):
            raise ValueError("solver repeated an already recorded block state")
        block = self._new_block(phase, primary, model)
        cover = Path(block["directory"]) / "block.solution.json"
        try:
            document = self._decode_block(model, Path(phase["block_map"]), cover)
        except TheoryPrune as error:
            block["status"] = "EXACT_PRUNE"
            block["exact_prune"] = str(error)
        except ValueError as error:
            block["status"] = "DECODER_ERROR"
            block["decoder_error"] = str(error)
            phase["status"] = "ERROR"
            self.root["status"] = "ERROR"
            self._save()
            return "ERROR"
        else:
            block["solution"] = str(cover)
            block["audit"] = document.get("audit")
            hr = self._new_hr(block)
            generated = self._generate_hr(cover, Path(hr["directory"]))
            hr["base_cnf"] = str(Path(hr["directory"]) / "hr.base.cnf")
            hr["map"] = str(Path(hr["directory"]) / "hr.base.map.json")
            hr["stats"] = str(Path(hr["directory"]) / "hr.base.stats.json")
            hr["formula"] = generated
            hr["primary_variables"] = list(
                _hr_primary_variables(Path(hr["map"]))
            )
        self._save()
        return "PROGRESS"

    def _solve_hr(self, phase: dict, block: dict, hr: dict) -> str:
        status, model = self._solve(
            stage="H_R",
            node=hr,
            base_cnf=Path(hr["base_cnf"]),
            working_cnf=Path(hr["directory"]) / "hr.working.cnf",
            blockers=self._hr_blockers(hr),
        )
        if status == "UNSAT":
            hr["status"] = "RAW_CLOSED"
            hr["closure"] = {
                "kind": "EXHAUSTIVE_HR_ENUMERATION",
                "solver_call": self.state["solver_calls"],
                "blocked_hr_states": len(self._hr_blockers(hr)),
            }
            block["status"] = "RAW_CLOSED"
            self._save()
            return "PROGRESS"
        if status != "SAT":
            return status
        assignment = load_sat_solver_output(model)
        primary = _primary_state(
            assignment, hr["primary_variables"], "H_R-edge-primary"
        )
        if any(
            tuple(self.nodes[node_id].get("primary_state", ())) == primary
            for node_id in hr["children"]
        ):
            raise ValueError("solver repeated an already recorded H_R state")
        hr_state = self._new_hr_state(hr, primary, model)
        try:
            report = self._verify_hr(model, Path(hr["map"]))
        except TheoryPrune as error:
            hr_state["status"] = "EXACT_PRUNE"
            hr_state["exact_prune"] = str(error)
            self._save()
            return "PROGRESS"
        except ValueError as error:
            hr_state["status"] = "VERIFIER_ERROR"
            hr_state["verification_error"] = str(error)
            hr["status"] = "ERROR"
            block["status"] = "ERROR"
            phase["status"] = "ERROR"
            self.root["status"] = "ERROR"
            self._save()
            return "ERROR"
        report_path = Path(hr["directory"]) / "verification.json"
        _write_json_atomic(report_path, report)
        hr_state["status"] = "SAT_VERIFIED"
        hr_state["verification"] = str(report_path)
        hr["status"] = "SAT_VERIFIED"
        hr["verification"] = str(report_path)
        block["status"] = "SAT_VERIFIED"
        phase["status"] = "SAT_VERIFIED"
        self.root["status"] = "SAT_VERIFIED"
        self._save()
        return "SAT_VERIFIED"

    def step(self) -> str:
        if self.root["status"] in TERMINAL_ROOT:
            return self.root["status"]
        active = self._active_path()
        if len(active) == 1:
            return self._solve_phase()
        phase = self.nodes[active[1]]
        if len(active) == 2:
            return self._solve_block(phase)
        block = self.nodes[active[2]]
        if len(active) != 4:
            raise ValueError("open block state has no active H_R child")
        return self._solve_hr(phase, block, self.nodes[active[3]])

    def run(self) -> dict:
        try:
            stop_reason = "DRY_RUN" if self.args.dry_run else None
            while stop_reason is None and self.root["status"] not in TERMINAL_ROOT:
                if not self._can_call_solver():
                    stop_reason = "SESSION_LIMIT"
                    break
                outcome = self.step()
                if outcome in {
                    "TIMEOUT",
                    "UNKNOWN",
                    "CONFLICTING",
                    "BAD_EXIT",
                    "ERROR",
                }:
                    stop_reason = outcome
                elif outcome == "SESSION_LIMIT":
                    stop_reason = outcome
            session = self.state["sessions"][-1]
            session["finished_at_utc"] = utc_now()
            session["solver_calls_used"] = self.session_calls
            session["stop_reason"] = stop_reason or self.root["status"]
            self._save()
            return self.summary()
        finally:
            self.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-index", type=int, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--tables", type=Path, default=DEFAULT_TABLES_PATH)
    parser.add_argument("--solver", type=Path, required=True)
    parser.add_argument("--solver-arg", action="append", default=[])
    parser.add_argument("--timeout-seconds", type=float, default=3600.0)
    parser.add_argument("--session-seconds", type=float, default=43200.0)
    parser.add_argument("--max-solver-calls", type=int, default=1000000)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.timeout_seconds <= 0 or args.session_seconds <= 0:
        raise SystemExit("timeouts must be positive")
    if args.max_solver_calls <= 0:
        raise SystemExit("--max-solver-calls must be positive")
    try:
        summary = NestedParityDriver(args).run()
    except (OSError, KeyError, TypeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
