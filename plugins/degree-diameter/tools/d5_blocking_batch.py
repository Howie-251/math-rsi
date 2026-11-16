"""Bounded continuation of the accepted D12/754-plane construction.

--plan-only reads the current checkpoint and source header; it does not search.
Real execution requires an ACTIVE project state and explicit batch/CPU/wall limits.
Output is author evidence, awaiting independent validation and parent consumption.
"""
import argparse
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "base/tools"))
from current_context import read_state, require_consumed_results, resolve_path


def execution_progress(output, native_attempted, native_result=None):
    """Read flushed author diagnostics, without accepting or verifying a graph.

    A native invocation alone does not prove its candidate search was entered.
    Partial JSON lines are uncounted; their presence is reported explicitly.
    """
    def rows(name):
        records, complete = [], True
        path = output / name
        if path.exists():
            for line in path.read_text().splitlines():
                if not line.strip():
                    continue
                try:
                    value = json.loads(line)
                except ValueError:
                    complete = False
                    continue
                if isinstance(value, dict):
                    records.append(value)
                else:
                    complete = False
        return records, complete

    additions, complete = rows("ADDITIONS.jsonl")
    prefixes = sum("new_vertex" in row and isinstance(row.get("pins"), list)
                   for row in additions)
    steps, _ = rows("STEP_RESULTS.jsonl")
    checked_steps = steps + ([native_result] if native_result else [])
    search_evidence = bool(prefixes) or any(
        row.get("P_tail_checks", 0) > 0 or row.get("reached_planes", 0) > 0
        for row in checked_steps)
    if search_evidence:
        started = True
    elif not native_attempted:
        started = False
    elif native_result is not None and "P_tail_checks" in native_result:
        started = False
    else:
        started = None
    return dict(native_invocation_attempted=native_attempted, search_started=started,
                author_prefixes_written=prefixes, author_prefix_log_complete=complete,
                author_prefixes_status="UNVERIFIED_AUTHOR_OUTPUT_NOT_ACCEPTANCE")


def build_plan(state_path, planes, output, max_new, cpu_limit, wall_limit):
    if max_new < 1 or not math.isfinite(cpu_limit) or cpu_limit <= 0 or not math.isfinite(wall_limit) or wall_limit <= 0:
        raise ValueError("positive finite batch, CPU and wall limits required")
    state = json.loads(Path(state_path).read_text())
    family = state["current_context"]["families"]["12,5"]
    if family["generator_domain"] != "d12_754_planes_core41356":
        raise ValueError("this driver is only for the bound D12 plane family")
    graph = family["latest_graph"]
    source = resolve_path(graph["edge_file"], Path(state_path).parent)
    with source.open() as f:
        n, m = map(int, f.readline().split())
    if (n, m) != (graph["n"], graph["m"]):
        raise ValueError("source header does not match the accepted checkpoint")
    if not family["accepted_orders"] or n != max(family["accepted_orders"]):
        raise ValueError("source prefix is not the latest accepted order")
    with Path(planes).open() as f:
        if f.readline().strip() != "754":
            raise ValueError("requires the original 754 actual-ID plane rows")
    return dict(state_path=str(Path(state_path).resolve()),
                goal_status=state["status"], source=str(source.resolve()), source_n=n, source_m=m,
                source_evidence=graph["evidence"], planes=str(Path(planes).resolve()),
                output=str(Path(output).resolve()), max_new=max_new, cpu_limit=cpu_limit,
                wall_limit=wall_limit, generated_by_this_plan=0,
                source_D5="inherited accepted premise; concrete Lean gap remains",
                stop_reasons=["BATCH_LIMIT_REACHED", "UNKNOWN_PROVIDER_PREPARATION_LIMIT",
                    "UNKNOWN_PROVIDER_PREPARATION_LIMIT_AFTER_ACCEPTED_GRAPH",
                    "UNKNOWN_WHOLE_CPU_LIMIT", "UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH",
                    "COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN", "PROCESS_LIMIT_OR_ERROR"],
                followup="No automatic continuation; parent consumes results and decides next batch.")


def execute(plan):
    # A plan is a reading artifact. Re-read the original state at the actual
    # execution boundary, including results returned since the plan was made.
    state_path = Path(plan["state_path"])
    state = read_state(state_path)
    if state["status"].upper() != "ACTIVE":
        raise ValueError("mathematical Goal is not ACTIVE; plan-only is available")
    require_consumed_results(state, state_dir=state_path.parent)
    family = state["current_context"]["families"]["12,5"]
    latest = family["latest_graph"]
    if (family["generator_domain"] != "d12_754_planes_core41356"
            or not family["accepted_orders"]
            or max(family["accepted_orders"]) != plan["source_n"]
            or (latest["n"], latest["m"]) != (plan["source_n"], plan["source_m"])
            or resolve_path(latest["edge_file"], state_path.parent) != Path(plan["source"]).resolve()):
        raise ValueError("planned source is no longer the latest accepted checkpoint; rebuild the plan")
    out = Path(plan["output"])
    out.mkdir(parents=True, exist_ok=False)
    (out / "BATCH.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    start = time.monotonic()
    parent0 = time.process_time()
    def children_cpu():
        r = resource.getrusage(resource.RUSAGE_CHILDREN)
        return r.ru_utime + r.ru_stime
    child0 = children_cpu()
    def used():
        return children_cpu() - child0 + time.process_time() - parent0
    def run(command, log):
        remaining = plan["cpu_limit"] - used()
        wall = plan["wall_limit"] - (time.monotonic() - start)
        if remaining <= 0 or wall <= 0:
            raise TimeoutError("batch budget exhausted before next process")
        def limit():
            seconds = max(1, math.ceil(remaining))
            resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
            resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
            resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        with (out / log).open("w") as f:
            subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, check=True,
                           timeout=wall, preexec_fn=limit,
                           env={**os.environ, "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1"})
    (out / "RUN_HANDLE.json").write_text(json.dumps(dict(running=True, pid=os.getpid())) + "\n")
    error = None
    stage = "compile"
    native_attempted = False
    native_result = None
    try:
        binary = str(out / "continue")
        run(["g++", "-O3", "-std=c++17", str(Path(__file__).with_suffix(".cpp")), "-o", binary], "COMPILE.log")
        stage = "control"
        run([binary, "--control"], "CONTROL.log")
        # Leave serialization/accounting time inside the original total cap.
        remaining = plan["cpu_limit"] - used() - 1.0
        if remaining <= 0:
            raise TimeoutError("no native budget after compilation/control")
        stage = "native"
        native_attempted = True
        run([binary, str(out), plan["planes"], plan["source"], str(remaining),
             str(plan["max_new"]), str(plan["source_n"]), str(plan["source_m"])], "NATIVE.log")
        stage = "native_result"
        native_result = json.loads((out / "NATIVE_RESULT.json").read_text())
        result = native_result
        stage = "finished"
    except (OSError, TimeoutError, ValueError, subprocess.SubprocessError) as exc:
        error = str(exc)
        result = dict(status="PROCESS_LIMIT_OR_ERROR", running=False, error=error,
                      source_n=plan["source_n"],
                      accepted_new_graphs=None,
                      recovery="Inspect flushed ADDITIONS/STEP_RESULTS; no automatic acceptance or restart.")
    result.update(stage=stage, **execution_progress(out, native_attempted, native_result))
    result.update(whole_CPU=used(), whole_wall=time.monotonic() - start,
                  whole_CPU_cap=plan["cpu_limit"], running=False,
                  further_continuation_authorized=False, independent_validation="PENDING")
    result["cpu_budget_exceeded"] = result["whole_CPU"] > plan["cpu_limit"]
    (out / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    (out / "RUN_HANDLE.json").write_text(json.dumps(dict(running=False, status=result["status"])) + "\n")
    return result, error


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--state", type=Path, required=True)
    p.add_argument("--planes", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--max-new", type=int, required=True)
    p.add_argument("--cpu-limit", type=float, required=True)
    p.add_argument("--wall-limit", type=float, required=True)
    p.add_argument("--plan-only", action="store_true")
    a = p.parse_args()
    plan = build_plan(a.state, a.planes, a.output, a.max_new, a.cpu_limit, a.wall_limit)
    if a.plan_only:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
    else:
        result, error = execute(plan)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if error:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
