"""Bounded generated-program execution and the search API available to programs."""
import ast
import json
import os
from pathlib import Path
import random
import signal
import subprocess
import sys
import time
from .graphs import geometry, graph_id, greedy, validate
from .metrics import Registry
from .reward import score

ALLOWED_IMPORTS = {"math", "random", "itertools", "collections", "functools", "heapq", "bisect", "statistics"}


def vet_source(source):
    if not isinstance(source, str) or len(source.encode()) > 100_000:
        raise ValueError("program must be Python source <=100 KB")
    tree = ast.parse(source)
    if not any(isinstance(node, ast.FunctionDef) and node.name == "generate" for node in tree.body):
        raise ValueError("program must define generate(context)")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or ""]
            if any(name not in ALLOWED_IMPORTS for name in names) or getattr(node, "level", 0):
                raise ValueError("unsupported import")
        if isinstance(node, ast.Attribute) and node.attr.startswith("_"):
            raise ValueError("private/dunder attribute access unavailable")
        if isinstance(node, ast.Name) and node.id.startswith("__"):
            raise ValueError("dunder names unavailable")
    return tree


class SearchAPI:
    def __init__(self, context):
        self.n = context["n"]
        self.registry = Registry(self.n, context["metric_definitions"])
        self.snapshot = context["reward_snapshot"]
        self.focus = context["focus"]

    def cube_edges(self):
        return [list(e) for e in geometry(self.n)[0]]

    def greedy(self, edges=(), delete=0, seed=0, weights=None):
        return greedy(self.n, random.Random(seed), edges, deletion_count=delete, weights=weights)

    def valid(self, edges):
        try:
            validate(self.n, edges)
            return True
        except (ValueError, TypeError):
            return False

    def metrics(self, edges):
        es, _ = validate(self.n, edges)
        return self.registry.compute(es)

    def score(self, edges):
        es, _ = validate(self.n, edges)
        return score(self.registry.compute(es), self.snapshot, graph_id(self.n, es))

    def reward(self, edges):
        s = self.score(edges)
        progress = s["objective_utility"] / (abs(self.snapshot["goal"]["target"]) + 1)
        if self.snapshot.get("quality_band") and self.focus in ("challenge", "novelty"):
            if self.focus == "challenge" and s["max_violation"] is not None and s["max_violation"] > 0:
                z = s["max_violation"]
                return 2 + z / (1 + abs(z)) + 0.01 * progress
            if not s["in_quality_band"]:
                return -2 - s["quality_deficit"] + 0.01 * progress
            if self.focus == "novelty":
                return s["novelty"] / (1 + s["novelty"]) + 0.05 * progress
            z = s["challenge"]
            return (z / (1 + abs(z)) if z is not None else -1) + 0.01 * progress
        if self.focus == "challenge":
            return (s["challenge"] if s["challenge"] is not None else -1e6) + 0.01 * progress + 0.01 * s["novelty"]
        if self.focus == "novelty":
            return s["novelty"] + 0.05 * progress
        if self.focus == "condition":
            return -s["condition_distance"] + 0.001 * progress
        return s["objective_utility"] - (abs(self.snapshot["goal"]["target"]) + 1) * s["condition_distance"] + 0.01 * s["novelty"]


def run_process(argv, *, cwd, stdin, timeout, stdout_path, stderr_path, env=None):
    """No shell; process-group cancellation prevents orphan solver children."""
    started = time.monotonic()
    with open(stdout_path, "wb") as out, open(stderr_path, "wb") as err:
        process = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.PIPE, stdout=out, stderr=err,
                                   start_new_session=True, env=env)
        try:
            process.communicate(stdin.encode(), timeout=timeout)
            status = "ok" if process.returncode == 0 else "failed"
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
            status = "timeout"
        except BaseException:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
            raise
    return {"status": status, "returncode": process.returncode, "elapsed_seconds": time.monotonic() - started}


def execute(source, context, directory, timeout=15, memory_mb=512):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    source_path = directory / "program.py"
    source_path.write_text(source)
    (directory / "input.json").write_text(json.dumps(context, indent=2) + "\n")
    try:
        vet_source(source)
    except (ValueError, SyntaxError) as exc:
        result = {"status": "rejected_source", "error": str(exc), "graphs": []}
        (directory / "execution.json").write_text(json.dumps(result, indent=2) + "\n")
        return result
    # No model credentials or unrelated environment variables enter generated Python.
    env = {"PATH": os.defpath, "LANG": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1"}
    argv = [sys.executable, "-I", "-S", str(Path(__file__).with_name("worker.py")),
            str(source_path.resolve()), str(directory.resolve() / "input.json"), str(timeout), str(memory_mb)]
    result = run_process(argv, cwd=directory, stdin="", timeout=timeout + 2,
                         stdout_path=directory / "stdout.json", stderr_path=directory / "stderr.txt", env=env)
    result["graphs"] = []
    result["stderr_tail"] = (directory / "stderr.txt").read_text(errors="replace")[-6000:]
    if result["status"] == "ok":
        try:
            data = (directory / "stdout.json").read_text()
            if len(data) > 4_000_000:
                raise ValueError("program output exceeds 4 MB")
            graphs = json.loads(data)
            if not isinstance(graphs, list) or not 1 <= len(graphs) <= context["max_graphs"]:
                raise ValueError("generate must return 1..max_graphs graph objects")
            result["graphs"] = graphs
        except (ValueError, UnicodeError) as exc:
            result.update(status="invalid_output", error=str(exc))
    (directory / "execution.json").write_text(json.dumps(result, indent=2) + "\n")
    return result
