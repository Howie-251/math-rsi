"""Bounded V6 campaign: shared bases, exact structural splits and resume."""

import argparse
import concurrent.futures as futures
import copy
import fcntl
import json
import os
from pathlib import Path
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
from collections import Counter, defaultdict, deque

from sat59.jobs.run_c1_queue import atomic_json, append_jsonl, dimacs_header, terminate_process, utc_now
from sat59.jobs.run_extremal_v5 import DynamicTaskTree
from sat59.jobs.extremal_v5_timeout_splitter import CLOSED_STATES, SemanticPivot, split_timeout_task
from sat59.theory.structural_v6_specs import MODES, campaign_spec, base_templates
from sat59.verify.verify_structural_v6 import decode, verify

REPO = Path(__file__).resolve().parents[2]


def load(path):
    return json.loads(Path(path).read_text())


def coverage_status(manifest, tasks):
    owners = manifest["representative_owners"]
    closed = [rep for rep, roots in owners.items() if all(tasks[r]["state"] in CLOSED_STATES for r in roots)]
    return {"logical_representatives": len(owners), "closed_representatives": len(closed),
            "open_representatives": len(owners) - len(closed), "closed_ids": closed}


def task_units(task, variable_map):
    units = list(task.get("cube_units", []))
    q = task["case"].get("exact_q2")
    if q is not None:
        term = variable_map["q2_selectors"][str(q)]
        if term is False:
            return None
        if term is not True:
            units.append(term)
    if any(-u in units for u in units):
        return None
    return list(dict.fromkeys(units))


def materialize(base, destination, units):
    """Copy the cached formula with an adjusted header and exact cube units."""
    variables, clauses = dimacs_header(base)
    with Path(base).open("rb") as src, Path(destination).open("wb") as dst:
        for line in src:
            if line.startswith(b"p cnf "):
                dst.write(f"p cnf {variables} {clauses + len(units)}\n".encode())
                break
            dst.write(line)
        else:
            raise ValueError("base DIMACS header missing")
        shutil.copyfileobj(src, dst, 1024 * 1024)
        dst.write(b"\n")
        for literal in units:
            dst.write(f"{literal} 0\n".encode())
    return variables, clauses + len(units)


def split_structural(tree, task_id, variable_map, child_timeout):
    task = tree.tasks[task_id]
    used = {abs(t) for t in task.get("cube_units", [])}
    candidates = [p for p in variable_map["structural_pivots"] if p["exact"] and abs(p["literal"]) not in used]
    if not candidates:
        return []
    choice = min(candidates, key=lambda p: p["priority"])
    selected = SemanticPivot(choice["literal"], choice["name"], choice["definition"]["kind"], choice["priority"])
    parent, children = split_timeout_task(task, selected, child_timeout_seconds=child_timeout)
    parent["split_rule"]["definition"] = choice["definition"]
    tree.tasks[task_id] = parent
    for child, truth in zip(children, (True, False)):
        predicates = copy.deepcopy(task.get("semantic_predicates", []))
        predicates.append({"name": choice["name"], "definition": choice["definition"], "value": truth,
                           "literal": choice["literal"]})
        child["semantic_predicates"] = predicates
        child["case"] = copy.deepcopy(task["case"])
        child["case"]["case_id"] = child["task_id"]
        child["index"] = tree.value["next_index"]
        tree.value["next_index"] += 1
        tree.tasks[child["task_id"]] = child
    tree.save()
    return [c["task_id"] for c in children]


def memory_available_mb():
    info = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, value, *_ = line.split()
        info[key.rstrip(":")] = int(value) / 1024
    available = info["MemAvailable"]
    # Cluster containers may have a much smaller limit than host MemTotal.
    for limit_path, usage_path in (
        ("/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory.current"),
        ("/sys/fs/cgroup/memory/memory.limit_in_bytes", "/sys/fs/cgroup/memory/memory.usage_in_bytes"),
    ):
        if Path(limit_path).is_file():
            limit = Path(limit_path).read_text().strip()
            if limit.isdigit():
                used = int(Path(usage_path).read_text())
                available = min(available, (int(limit) - used) / 1048576)
    return max(0, available)


def process_stats(pid):
    try:
        fields = Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()
        cpu = (int(fields[11]) + int(fields[12])) / os.sysconf("SC_CLK_TCK")
        rss = int(fields[21]) * os.sysconf("SC_PAGE_SIZE") / 1048576
        return cpu, rss
    except (FileNotFoundError, ProcessLookupError):
        return 0.0, 0.0


class StructuralQueue:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        args.run_dir.mkdir(parents=True, exist_ok=True)
        self.manifest_path = args.run_dir / "campaign.json"
        if self.manifest_path.exists():
            self.manifest = load(self.manifest_path)
            if self.manifest["evidence_mode"] != args.mode:
                raise ValueError("resume must use the original evidence mode")
            if getattr(args, "manual_round", None) and self.manifest.get("research_round") != "N59_MANUAL12_ACTIVE":
                raise ValueError("manual12 needs its own run; do not attach it to an old V6 campaign")
            if getattr(args, "manual_round", None) and Path(self.manifest['round_directory']).resolve() != args.manual_round.resolve():
                raise ValueError('resume must use its original package directory; r2 needs a new run')
        else:
            if getattr(args, "manual_round", None):
                from sat59.theory.manual12_specs import campaign_spec as manual_campaign
                self.manifest = manual_campaign(args.manual_round)
            else:
                self.manifest = campaign_spec(args.mode)
            atomic_json(self.manifest_path, self.manifest)
        self.build_repo = REPO
        if self.manifest.get("research_round") == "N59_MANUAL12_ACTIVE":
            from sat59.jobs.manual12_inputs import freeze_inputs
            self.build_repo = freeze_inputs(self.manifest["round_directory"], args.run_dir, self.manifest)
        self.templates = base_templates(self.manifest)
        self.tree = DynamicTaskTree(args.run_dir / "task_tree.json", self.manifest_path, self.manifest)
        self.tree.recover_running()
        # Exhausted wall budgets are resumable, but completed exclusions stay closed.
        for task in self.tree.tasks.values():
            if not task["children"] and task["state"] in {"TIMEOUT", "MEMORY_LIMIT"}:
                task["state"] = "PENDING"
        self.tree.save()
        self.deadline = self.started + args.wall_timeout - args.final_reserve
        self.stop = threading.Event()
        self.lock = threading.Lock()
        self.live = {}
        self.build_slots = threading.Semaphore(args.build_workers)
        self.base_locks = {t: threading.Lock() for t in self.templates}
        self.cache = args.run_dir / "templates"
        self.cache.mkdir(exist_ok=True)
        self.peak_solver_rss = 0.0
        self.solver_observed = False
        self.last_group = None
        run_path = args.run_dir / "run.json"
        self.run_record = load(run_path) if run_path.exists() else {"created_utc": utc_now(), "sessions": []}
        self.run_record["sessions"].append({"started_utc": utc_now(), "hostname": socket.gethostname(),
            "workers": args.workers, "build_workers": args.build_workers, "mode": args.mode,
            "wall_timeout": args.wall_timeout, "first_task_timeout": args.first_task_timeout,
            "child_timeout": args.child_timeout, "max_split_depth": args.max_split_depth,
            "final_reserve": args.final_reserve, "proof_requested": args.proof,
            "scratch_directory": str(args.scratch_dir) if args.scratch_dir else tempfile.gettempdir(),
            "run_directory": str(args.run_dir), "python": sys.version,
            "execution_command": [sys.executable, *sys.argv],
            "solver": str(args.solver), "solver_args": args.solver_arg,
            "research_round": self.manifest.get("research_round"),
            "package_revision": self.manifest.get("package_revision"),
            "build_source": str(self.build_repo),
            "computation_question": self.manifest.get("computation_question"),
            "scheduling_policy": self.manifest.get("scheduling_policy", "LEGACY"),
            "initial_available_memory_mb": round(memory_available_mb(), 1),
            "solver_log_limit_mb": 128 if self.manifest.get("research_round") else None})
        atomic_json(run_path, self.run_record)

    def base_directory(self, task):
        return self.cache / task["template_id"]

    def monitor(self, task_id, process, kind, seconds, output_path=None):
        started = time.monotonic()
        deadline = min(self.deadline, started + seconds)
        peak_cpu, peak_rss = 0.0, 0.0
        reason = None
        with self.lock:
            self.live[task_id] = {"pid": process.pid, "kind": kind, "started": started}
        try:
            while process.poll() is None:
                cpu, rss = process_stats(process.pid)
                peak_cpu, peak_rss = max(peak_cpu, cpu), max(peak_rss, rss)
                with self.lock:
                    self.live[task_id].update(cpu_seconds=cpu, rss_mb=rss, peak_rss_mb=peak_rss)
                    if kind == "solver":
                        self.peak_solver_rss = max(self.peak_solver_rss, peak_rss)
                        self.solver_observed |= time.monotonic() - started >= 30
                if output_path is not None and output_path.stat().st_size > 128 * 1024 * 1024:
                    reason = "output_limit"
                    terminate_process(process)
                    break
                if self.stop.is_set() or time.monotonic() >= deadline:
                    reason = "stopped" if self.stop.is_set() else ("campaign_deadline" if deadline == self.deadline else "task_timeout")
                    terminate_process(process)
                    break
                time.sleep(0.25)
            process.wait()
        finally:
            with self.lock:
                self.live.pop(task_id, None)
        return {"return_code": process.returncode, "reason": reason,
                "seconds": round(time.monotonic() - started, 3),
                "cpu_seconds_sampled": round(peak_cpu, 3), "peak_rss_mb": round(peak_rss, 1)}

    def ensure_base(self, task):
        directory = self.base_directory(task)
        with self.base_locks[task["template_id"]]:
            if self.stop.is_set() or time.monotonic() >= self.deadline:
                raise InterruptedError("campaign stopped before base access")
            if (directory / "ready.json").is_file():
                return directory
            while not self.build_slots.acquire(timeout=0.2):
                if self.stop.is_set() or time.monotonic() >= self.deadline:
                    raise InterruptedError("campaign stopped before base build")
            try:
                if self.stop.is_set() or time.monotonic() >= self.deadline:
                    raise InterruptedError("campaign stopped before base build")
                directory.mkdir(exist_ok=True)
                atomic_json(directory / "case.json", task["base_case"])
                with (directory / "build.log").open("w") as log:
                    proc = subprocess.Popen([sys.executable, "-m", "sat59.jobs.build_structural_v6",
                        "--case", str(directory / "case.json"), "--output", str(directory)],
                        cwd=self.build_repo, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                    outcome = self.monitor(task["task_id"], proc, "builder", 1800)
                if outcome["reason"]:
                    raise InterruptedError("base build interrupted: " + outcome["reason"])
                if outcome["return_code"] != 0:
                    raise RuntimeError(f"base build failed; see {directory / 'build.log'}")
                atomic_json(directory / "ready.json", outcome)
            finally:
                self.build_slots.release()
        return directory

    def execute(self, task, attempt):
        started = time.monotonic()
        directory = self.args.run_dir / "tasks" / task["task_id"]
        directory.mkdir(parents=True, exist_ok=True)
        atomic_json(directory / "task.json", task)
        scratch = None
        try:
            base = self.ensure_base(task)
            if self.stop.is_set() or time.monotonic() >= self.deadline:
                raise InterruptedError("campaign deadline before solver")
            vm = load(base / "base.map.json")
            units = task_units(task, vm)
            if units is None:
                return {"state": "STATIC_UNSAT", "reason": "false selector or complementary cube units"}
            scratch = Path(tempfile.mkdtemp(prefix="n59-v6-", dir=self.args.scratch_dir))
            cnf = scratch / "instance.cnf"
            variables, clauses = materialize(base / "base.cnf", cnf, units)
            log_path = directory / f"attempt-{attempt['number']:03d}.solver.log"
            atomic_json(directory / f"attempt-{attempt['number']:03d}.cube.json", {"units": units})
            build_seconds = time.monotonic() - started
            timeout = self.attempt_timeout(task)
            command = [str(self.args.solver), *self.args.solver_arg, str(cnf)]
            if self.args.proof:
                command.append(str(directory / f"attempt-{attempt['number']:03d}.proof"))
            with log_path.open("w") as log:
                proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                if self.manifest.get("research_round"):
                    result = self.monitor(task["task_id"], proc, "solver", timeout, output_path=log_path)
                else:
                    result = self.monitor(task["task_id"], proc, "solver", timeout)
            outcome = {"finished_utc": utc_now(), "solver": result,
                "build_seconds": round(build_seconds, 3), "wall_seconds": round(time.monotonic() - started, 3),
                "variables": variables, "clauses": clauses, "solver_log": str(log_path),
                "base_map": str(base / "base.map.json"), "cube_units": units,
                "proof_requested": self.args.proof, "command": command,
                "solver_timeout_seconds": timeout,
                "constraint_sets": task["case"].get("constraint_sets", [])}
            if result["reason"]:
                outcome.update(state="INTERRUPTED" if result["reason"] == "stopped" else "TIMEOUT", reason=result["reason"])
                if result["reason"] == "output_limit":
                    outcome["state"] = "OUTPUT_LIMIT"
            elif result["return_code"] == 20:
                outcome["state"] = "RAW_UNSAT_NEW"
            elif result["return_code"] == 10:
                matrix = decode(log_path, vm)
                verdict = verify(matrix, vm, task)
                if task["case"].get("manual_revision"):
                    from sat59.verify.verify_manual12 import enrich_verification
                    verdict = enrich_verification(matrix, vm, task, verdict)
                if task['case'].get('manual_revision') == 'r2_20260928':
                    from sat59.verify.verify_manual12_r2 import enrich_verification as enrich_r2
                    verdict = enrich_r2(matrix, vm, task, verdict)
                atomic_json(directory / f"attempt-{attempt['number']:03d}.verification.json", verdict)
                outcome["state"] = verdict["status"]
                if verdict["base_graph_valid"]:
                    self.stop.set()
            else:
                outcome.update(state="SOLVER_ERROR", reason=f"return code {result['return_code']}")
            return outcome
        except InterruptedError as error:
            return {"state": "INTERRUPTED", "reason": str(error), "wall_seconds": round(time.monotonic() - started, 3)}
        except Exception as error:
            return {"state": "BUILD_OR_SOLVER_ERROR", "reason": repr(error), "wall_seconds": round(time.monotonic() - started, 3)}
        finally:
            # Only this attempt's mkdtemp directory; maps, logs and cubes stay.
            if scratch is not None:
                shutil.rmtree(scratch)

    def attempt_timeout(self, task):
        timeout = self.args.first_task_timeout if task['depth'] == 0 else self.args.child_timeout
        # r2 respects the explicit per-attempt bound at every depth. A
        # timed-out leaf is not requeued in this session just to fill cores.
        if self.manifest.get('scheduling_policy') != 'BOUNDED_ATTEMPTS_UNTRIED_FIRST' and task['depth'] >= self.args.max_split_depth:
            timeout = max(1, self.deadline - time.monotonic())
        return timeout

    def pick(self, pending):
        if self.manifest.get('scheduling_policy') == 'BOUNDED_ATTEMPTS_UNTRIED_FIRST':
            # Never-run ranges precede old timeouts, regardless of class,
            # priority or depth. Within that tier retain class round-robin.
            least = min(len(self.tree.tasks[t].get('attempts', [])) for t in pending)
            pending = [t for t in pending if len(self.tree.tasks[t].get('attempts', [])) == least]
        # Round-robin structural groups; spare capacity is borrowed freely.
        groups = defaultdict(list)
        for task_id in pending:
            task = self.tree.tasks[task_id]
            group = task.get("service_group") or task["case"].get("family") or ("m0" if task["case"]["m"] == 0 else f"m1_K{task['case']['K']}")
            groups[group].append(task_id)
        order = sorted(groups)
        if self.last_group in order:
            i = order.index(self.last_group) + 1
            order = order[i:] + order[:i]
        self.last_group = order[0]
        return groups[order[0]][0]

    def worker_cap(self, active_count):
        with self.lock:
            peak = self.peak_solver_rss
            observed = self.solver_observed
        if not observed:
            return min(self.args.workers, 4)
        extra = int(max(0, memory_available_mb() - 3072 * self.args.build_workers) / max(512, peak * 1.4))
        return min(self.args.workers, max(1, active_count + extra))

    def progress(self):
        with self.lock:
            live = copy.deepcopy(self.live)
        for item in live.values():
            item["elapsed_seconds"] = round(time.monotonic() - item.pop("started"), 1)
        roots = {r: self.tree.tasks[r]["state"] for r in self.tree.roots}
        coverage = coverage_status(self.manifest, self.tree.tasks)
        coarse = defaultdict(list)
        for rep_id, rep in self.manifest["representatives"].items():
            coarse[rep["partition_id"]].append(rep_id)
        closed_set = set(coverage["closed_ids"])
        coarse_status = {k: {"closed": sum(r in closed_set for r in reps), "total": len(reps),
                             "fully_closed": all(r in closed_set for r in reps)} for k, reps in coarse.items()}
        attempts = [a for t in self.tree.tasks.values() for a in t["attempts"] if a.get("state") != "RUNNING"]
        closed = coverage["open_representatives"] == 0
        graph = any(t["state"] in {"SAT_VERIFIED", "BASE_GRAPH_VALID_PRIOR_OR_BRANCH_CONFLICT"} for t in self.tree.tasks.values())
        result = {"updated_utc": utc_now(), "hostname": socket.gethostname(), "evidence_mode": self.args.mode,
            "global_result": "GRAPH_FOUND" if graph else ("CONDITIONAL_RAW_C1_CLOSED" if closed else "UNRESOLVED"),
            "session_elapsed_hours": round((time.monotonic() - self.started) / 3600, 3),
            "session_remaining_hours": round(max(0, self.deadline - time.monotonic()) / 3600, 3),
            "runtime_roots": len(roots), "root_states": roots, "runtime_nodes": len(self.tree.tasks),
            "leaf_states": dict(Counter(self.tree.tasks[t]["state"] for t in self.tree.current_leaf_ids())),
            "untried_leaf_ids": [t for t in self.tree.current_leaf_ids() if not self.tree.tasks[t]['attempts']],
            "solver_cpu_hours_sampled": round((sum(a.get("solver", {}).get("cpu_seconds_sampled", 0) for a in attempts)
                + sum(p.get("cpu_seconds", 0) for p in live.values() if p["kind"] == "solver")) / 3600, 3),
            "live_processes": live, "requested_workers": self.args.workers,
            "live_solvers": sum(p["kind"] == "solver" for p in live.values()),
            "live_builders": sum(p["kind"] == "builder" for p in live.values()),
            "coarse_classes": coarse_status,
            "inherited_migration_counts": dict(Counter(r["state"] for r in self.manifest["migration"])),
            "scope": "surviving c1 representatives only; not the entire n=59 problem",
            "research_round": self.manifest.get("research_round"),
            "package_revision": self.manifest.get("package_revision"), **coverage}
        atomic_json(self.args.run_dir / "progress.json", result)
        append_jsonl(self.args.run_dir / "progress.jsonl", result)
        return result

    def run(self):
        active = {}
        last_progress = 0
        with futures.ThreadPoolExecutor(max_workers=self.args.workers) as pool:
            while True:
                pending = self.tree.pending_ids()
                cap = self.worker_cap(len(active))
                while pending and len(active) < cap and not self.stop.is_set() and time.monotonic() < self.deadline:
                    task_id = self.pick(pending)
                    pending.remove(task_id)
                    attempt = self.tree.begin_attempt(task_id)
                    active[pool.submit(self.execute, copy.deepcopy(self.tree.tasks[task_id]), attempt)] = task_id
                if time.monotonic() - last_progress >= 15:
                    result = self.progress()
                    print(f"{utc_now()} closed={result['closed_representatives']}/{result['logical_representatives']} "
                          f"solvers={result['live_solvers']} builders={result['live_builders']} "
                          f"leaves={result['leaf_states']}", flush=True)
                    last_progress = time.monotonic()
                if not active:
                    break
                done, _ = futures.wait(active, timeout=1, return_when=futures.FIRST_COMPLETED)
                for future in done:
                    task_id = active.pop(future)
                    outcome = future.result()
                    self.tree.finish_attempt(task_id, outcome)
                    task = self.tree.tasks[task_id]
                    if outcome["state"] == "TIMEOUT" and outcome.get("reason") == "task_timeout" and task["depth"] < self.args.max_split_depth:
                        split_structural(self.tree, task_id, load(self.base_directory(task) / "base.map.json"), self.args.child_timeout)
                    self.tree.aggregate_from(task_id)
                    self.tree.save()
        result = self.progress()
        self.run_record["sessions"][-1].update(finished_utc=utc_now(), result=result["global_result"])
        atomic_json(self.args.run_dir / "run.json", self.run_record)
        print(json.dumps({k: result[k] for k in ("global_result", "closed_representatives", "open_representatives", "leaf_states")}, indent=2))
        return result


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run-dir", type=Path, required=True)
    p.add_argument("--mode", choices=MODES, default=MODES[0])
    p.add_argument("--manual-round", type=Path, help="N59_MANUAL12_ACTIVE package directory; manual execution only")
    p.add_argument("--workers", type=int, default=54)
    p.add_argument("--build-workers", type=int, default=2)
    p.add_argument("--wall-timeout", type=int, default=43200)
    p.add_argument("--first-task-timeout", type=int, default=21600)
    p.add_argument("--child-timeout", type=int, default=7200)
    p.add_argument("--max-split-depth", type=int, default=2)
    p.add_argument("--final-reserve", type=int, default=900)
    p.add_argument("--solver", type=Path, default=REPO / "solvers/satcomp2025/AE_kissat2025_MAB/kissat")
    p.add_argument("--solver-arg", action="append", default=[])
    p.add_argument("--scratch-dir", type=Path)
    p.add_argument("--proof", action="store_true", help="request a Kissat proof log; remains raw until checked")
    return p


def main():
    args = parser().parse_args()
    args.run_dir = args.run_dir.resolve()
    args.solver = args.solver.resolve()
    prior_campaign = args.run_dir / "campaign.json"
    if prior_campaign.is_file() and load(prior_campaign).get("research_round") == "N59_MANUAL12_ACTIVE" and not args.manual_round:
        raise SystemExit("resume manual12 with --manual-round and the remaining authorized time budget")
    if args.manual_round:
        args.manual_round = args.manual_round.resolve()
        if args.mode != "LATEST_CONDITIONAL":
            raise SystemExit("manual12 requires explicit --mode LATEST_CONDITIONAL")
        if args.max_split_depth > 1 or args.wall_timeout > 64800:
            raise SystemExit("manual12: at most one inherited complementary split and 18h per session")
    if not 1 <= args.workers <= 54 or not 1 <= args.build_workers <= min(2, args.workers):
        raise SystemExit("use 1..54 workers, 1..2 builders (builders occupy worker slots)")
    if args.wall_timeout <= args.final_reserve or args.first_task_timeout < 1 or args.child_timeout < 1 or args.max_split_depth < 0:
        raise SystemExit("invalid time/split limits")
    if not os.access(args.solver, os.X_OK):
        raise SystemExit(f"solver not executable: {args.solver}")
    args.run_dir.mkdir(parents=True, exist_ok=True)
    with (args.run_dir / "launcher.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        (args.run_dir / "launcher.pid").write_text(str(os.getpid()) + "\n")
        (args.run_dir / "launcher.host").write_text(socket.gethostname() + "\n")
        queue = StructuralQueue(args)
        signal.signal(signal.SIGTERM, lambda *_: queue.stop.set())
        signal.signal(signal.SIGINT, lambda *_: queue.stop.set())
        queue.run()


if __name__ == "__main__":
    main()
