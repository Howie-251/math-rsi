import hashlib
import json
import re
import subprocess
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from lib.cadical_sc2025 import CadicalSc2025Solver

try:
    from pysat.solvers import Solver
except ImportError:
    Solver = None

class Clauses:
    """
    A Boolean formula represented by:
      - one representative literal self._lit
      - a list of definitional CNF clauses self._defs
    The formula is asserted true when SATInstance.add(...) adds:
      self._defs + [[self._lit]]
    """

    def __init__(self, instance, name, lit, defs=None):
        self._instance = instance
        self._name = name
        self._lit = lit
        self._defs = [] if defs is None else defs

    def __len__(self):
        # "assert this formula true" would contribute len(defs) + 1 clauses
        return len(self._defs) + 1

    def __iter__(self):
        # Keep backward compatibility:
        # iterating over a formula means iterating over its asserted CNF.
        yield from self._defs
        yield [self._lit]

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self._name}@{self._lit} with {len(self._defs)} def-clauses"

    def __and__(self, other):
        assert self._instance is other._instance
        z = self._instance._fresh_var()
        name = f"({self._name})&({other._name})"

        # z <-> (self._lit & other._lit)
        defs = self._defs + other._defs + [
            [-z, self._lit],
            [-z, other._lit],
            [z, -self._lit, -other._lit],
        ]
        return Clauses(self._instance, name, z, defs)

    def __or__(self, other):
        assert self._instance is other._instance
        z = self._instance._fresh_var()
        name = f"({self._name})|({other._name})"

        # z <-> (self._lit | other._lit)
        defs = self._defs + other._defs + [
            [-self._lit, z],
            [-other._lit, z],
            [-z, self._lit, other._lit],
        ]
        return Clauses(self._instance, name, z, defs)

    def __invert__(self):
        # Negation is just flipping the representative literal.
        return Clauses(self._instance, f"~({self._name})", -self._lit, self._defs)

    def implies(self, other):
        # Keep API compatibility.
        return (~self) | other

    def solution(self):
        assert self._instance._solution is not None
        return self._instance._solution[abs(self._lit)] == self._lit


class SATInstance:
    def __init__(self):
        self._num_vars = 0
        self._clauses = []
        self._solution = None
        self._var_names = {}
        self._name_to_var = {}
        self._var_roles = {}
        self._current_clause_group = "other"
        self._clause_groups = []
        self._group_clause_counts = {}
        self._metadata = {}
        self._last_solver_result = None

    def _fresh_var(self):
        self._num_vars += 1
        return self._num_vars

    def _infer_var_role(self, name):
        triple_match = re.fullmatch(r"x_(\d+)_(\d+)_(\d+)", name)
        if triple_match:
            i, j, k = (int(part) for part in triple_match.groups())
            return {"role": "triple", "i": i, "j": j, "k": k}

        orient_match = re.fullmatch(r"v\((\d+),(\d+),(\d+)\)", name)
        if orient_match:
            i, j, k = (int(part) + 1 for part in orient_match.groups())
            return {"role": "triple", "i": i, "j": j, "k": k}

        cap_match = re.fullmatch(r"cap\((\d+),(\d+),(\d+)\)", name)
        if cap_match:
            i = int(cap_match.group(1)) + 1
            j = int(cap_match.group(2)) + 1
            d = int(cap_match.group(3))
            return {"role": "cap", "i": i, "j": j, "d": d}

        cap_state_match = re.fullmatch(r"cap\((\d+),(\d+),(\d+),(\d+)\)", name)
        if cap_state_match:
            i, j, k = (int(cap_state_match.group(idx)) + 1 for idx in range(1, 4))
            d = int(cap_state_match.group(4))
            return {"role": "cap_state", "i": i, "j": j, "k": k, "d": d}

        cup_match = re.fullmatch(r"cup\((\d+),(\d+),(\d+)\)", name)
        if cup_match:
            i = int(cup_match.group(1)) + 1
            j = int(cup_match.group(2)) + 1
            d = int(cup_match.group(3))
            return {"role": "cup", "i": i, "j": j, "d": d}

        cup_state_match = re.fullmatch(r"cup\((\d+),(\d+),(\d+),(\d+)\)", name)
        if cup_state_match:
            i, j, k = (int(cup_state_match.group(idx)) + 1 for idx in range(1, 4))
            d = int(cup_state_match.group(4))
            return {"role": "cup_state", "i": i, "j": j, "k": k, "d": d}

        split_cap_match = re.fullmatch(r"split_cap_exists\((\d+),(\d+)\)", name)
        if split_cap_match:
            return {
                "role": "split_cap_exists",
                "right_endpoint": int(split_cap_match.group(1)) + 1,
                "cap_size": int(split_cap_match.group(2)),
            }

        split_cup_match = re.fullmatch(r"split_cup_exists\((\d+),(\d+)\)", name)
        if split_cup_match:
            return {
                "role": "split_cup_exists",
                "right_endpoint": int(split_cup_match.group(1)) + 1,
                "cup_size": int(split_cup_match.group(2)),
            }

        split_pair_match = re.fullmatch(r"split_pair\((\d+),(\d+),(\d+)\)", name)
        if split_pair_match:
            return {
                "role": "split_pair",
                "right_endpoint": int(split_pair_match.group(1)) + 1,
                "cap_size": int(split_pair_match.group(2)),
                "cup_size": int(split_pair_match.group(3)),
            }

        split_end_match = re.fullmatch(r"split_end\((\d+)\)", name)
        if split_end_match:
            return {
                "role": "split_end",
                "right_endpoint": int(split_end_match.group(1)) + 1,
            }

        return {"role": "aux"}

    def new_var(self, name, role=None, **metadata):
        """Generate a new SAT variable."""
        lit = self._fresh_var()
        inferred = self._infer_var_role(name)
        record = {"var": lit, "name": name}
        record.update(inferred)
        if role is not None:
            record["role"] = role
        record.update(metadata)
        self._var_names[lit] = name
        self._name_to_var[name] = lit
        self._var_roles[lit] = record
        return Clauses(self, name, lit)

    def set_metadata(self, **metadata):
        self._metadata.update(metadata)

    def set_clause_group(self, group):
        self._current_clause_group = group

    @contextmanager
    def clause_group(self, group):
        previous = self._current_clause_group
        self._current_clause_group = group
        try:
            yield
        finally:
            self._current_clause_group = previous

    def _record_group_clauses(self, group, count):
        if count <= 0:
            return
        start_clause = len(self._clauses) - count
        end_clause = len(self._clauses) - 1
        self._clause_groups.append(
            {
                "group": group,
                "start_clause": start_clause,
                "end_clause": end_clause,
                "count": count,
            }
        )
        self._group_clause_counts[group] = self._group_clause_counts.get(group, 0) + count

    def add(self, clauses, group=None):
        """
        Assert a formula true, or add raw CNF clauses.

        Supported:
          - add(Clauses): add definitional clauses + unit clause on root literal
          - add(list_of_clauses): directly append raw clauses
        """
        if group is None:
            group = self._current_clause_group

        before = len(self._clauses)
        if isinstance(clauses, Clauses):
            self._clauses.extend(clauses._defs)
            self._clauses.append([clauses._lit])
        else:
            self._clauses.extend(clauses)
        self._record_group_clauses(group, len(self._clauses) - before)

    def add_clause(self, clause, group=None):
        """Add one raw clause, e.g. [-x, y, z] or [] for contradiction."""
        if group is None:
            group = self._current_clause_group
        self._clauses.append(clause)
        self._record_group_clauses(group, 1)

    def clauses(self):
        return self._clauses

    def add_implies(self, c0, c1, group=None):
        """
        Directly encode c0 -> c1 as (~root(c0) v root(c1)),
        plus the definitional clauses of c0 and c1.
        This is smaller than building (~c0) | c1 as a fresh OR-gate.
        """
        assert isinstance(c0, Clauses) and isinstance(c1, Clauses)
        assert c0._instance is self and c1._instance is self

        if group is None:
            group = self._current_clause_group

        before = len(self._clauses)
        self._clauses.extend(c0._defs)
        self._clauses.extend(c1._defs)
        self._clauses.append([-c0._lit, c1._lit])
        self._record_group_clauses(group, len(self._clauses) - before)

    def write(self, filename):
        with open(filename, "w") as f:
            head = f"p cnf {self._num_vars} {len(self._clauses)}"
            f.write(head + "\n")
            f.writelines(" ".join(map(str, c)) + " 0\n" for c in self._clauses)

    def _file_sha256(self, filename):
        digest = hashlib.sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def metadata_dict(self, cnf_path=None, extra=None):
        payload = {
            "num_vars": self._num_vars,
            "num_clauses": len(self._clauses),
            "var_names": self._var_names,
            "name_to_var": self._name_to_var,
            "var_roles": self._var_roles,
            "clause_groups": self._clause_groups,
            "group_clause_counts": self._group_clause_counts,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        payload.update(self._metadata)
        if cnf_path is not None:
            payload["cnf_path"] = str(cnf_path)
            if Path(cnf_path).exists():
                payload["cnf_sha256"] = self._file_sha256(cnf_path)
        if extra:
            payload.update(extra)
        return payload

    def write_metadata(self, meta_path, cnf_path=None, extra=None):
        payload = self.metadata_dict(cnf_path=cnf_path, extra=extra)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True)
            f.write("\n")
        return payload

    def load(self, filename):
        self._solution = [None]
        with open(filename, "r") as file:
            for line in file:
                if line[:2] != "v ":
                    continue
                self._solution.extend(map(int, line[2:].split()))

    def load_model(self, model):
        self._solution = [None] * (self._num_vars + 1)
        if model is None:
            return

        for lit in model:
            v = abs(lit)
            if v <= self._num_vars:
                self._solution[v] = lit

        for v in range(1, self._num_vars + 1):
            if self._solution[v] is None:
                self._solution[v] = -v

    def new_incremental_solver(self, solver_name="cadical-sc2025"):
        if solver_name == "cadical-sc2025":
            solver = CadicalSc2025Solver(self._num_vars)
            for clause in self._clauses:
                solver.add_clause(clause)
            return solver

        if Solver is None:
            raise ImportError(
                "python-sat is required for incremental solving. "
                "Install it with: pip install python-sat"
            )

        solver = Solver(name=solver_name)
        for clause in self._clauses:
            solver.add_clause(clause)
        return solver

    def solve_incremental(self, solver, assumptions=None):
        if assumptions is None:
            assumptions = []

        successful = solver.solve(assumptions=assumptions)
        if successful:
            self.load_model(solver.get_model())
        return successful

    def last_solver_result(self):
        """Return a copy of the most recent external-solver result, if any."""
        if self._last_solver_result is None:
            return None
        return dict(self._last_solver_result)

    def solve(self, filename="tmp", solver="kissat"):
        cnf_path = Path(f"{filename}.cnf")
        out_path = Path(f"{filename}.out")
        sat_path = Path(f"{filename}.sat")
        unsat_path = Path(f"{filename}.unsat")
        color_path = Path(f"{filename}.color")
        for stale_path in (sat_path, unsat_path, color_path):
            if stale_path.exists():
                stale_path.unlink()
        self.write(str(cnf_path))
        if solver == "kissat":
            command = [
                "/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat",
                str(cnf_path),
                str(unsat_path),
            ]
        elif solver == "cadical":
            command = [
                "/data/ktqiu_hdd/math_agent/cadical-sc2025/build/cadical",
                str(cnf_path),
            ]
        else:
            raise ValueError(f"Unknown solver: {solver}")

        started = time.perf_counter()
        try:
            with open(out_path, "w", encoding="utf-8") as stdout_f:
                completed = subprocess.run(
                    command,
                    stdout=stdout_f,
                    stderr=subprocess.STDOUT,
                    check=False,
                )
        except OSError as exc:
            elapsed = time.perf_counter() - started
            self._last_solver_result = {
                "schema": "solver_status_v1",
                "status": "ERROR",
                "solver": solver,
                "command": command,
                "returncode": None,
                "elapsed_sec": elapsed,
                "error": f"{type(exc).__name__}: {exc}",
            }
            return False

        elapsed = time.perf_counter() - started
        returncode = completed.returncode
        if returncode == 10:
            if unsat_path.exists():
                unsat_path.unlink()
            if sat_path.exists():
                sat_path.unlink()
            out_path.replace(sat_path)
            self.load(str(sat_path))
            status = "SAT"
        elif returncode == 20:
            # CaDiCaL does not receive a proof-output path.  Retain the legacy
            # `.unsat` completion marker for both supported solvers.
            unsat_path.touch(exist_ok=True)
            status = "UNSAT"
        else:
            status = "ERROR"

        self._last_solver_result = {
            "schema": "solver_status_v1",
            "status": status,
            "solver": solver,
            "command": command,
            "returncode": returncode,
            "elapsed_sec": elapsed,
            "output": str(sat_path if status == "SAT" else out_path),
            "proof": str(unsat_path) if unsat_path.exists() else None,
        }
        if status == "SAT":
            return True
        return False
