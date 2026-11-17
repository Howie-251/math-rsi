"""Explicit offline and actual Codex CLI providers; never silently substitute."""
import json
from pathlib import Path
import shutil
from .inequalities import fit_directions
from .runtime import run_process


OFFLINE_PROGRAM = '''import random

def generate(context):
    rng = random.Random(context["seed"])
    parents = context["parents"]
    pool = []
    for step in range(context["search_steps"]):
        parent = parents[step % len(parents)]["edges"] if parents and step % 4 else []
        delete = (3 + step % 10) if parent else 0
        edges = api.greedy(parent, delete=delete, seed=rng.randrange(1000000000))
        pool.append((api.reward(edges), edges))
    pool.sort(key=lambda item: item[0], reverse=True)
    return [{"edges": edges, "label": "offline_baseline"} for value, edges in pool[:context["max_graphs"]]]
'''


def schema_for(role):
    def obj(properties):
        return {"type": "object", "properties": properties, "required": list(properties), "additionalProperties": False}
    string = {"type": "string"}
    if role == "lower":
        return obj({"programs": {"type": "array", "items": obj({"name": string, "rationale": string, "source": string})}})
    # Coefficients are an array in the model transport to keep the JSON schema closed.
    condition = obj({"metric": string, "op": {"type": "string", "enum": ["<=", ">=", "==", "!=", "<", ">"]}, "value": {"type": "integer"}})
    inequality = obj({"name": string, "coefficients": {"type": "array", "items": obj({"metric": string, "coefficient": {"type": "integer"}})},
                      "rhs": {"type": "integer"}, "conditions": {"type": "array", "items": condition}, "rationale": string})
    metric = obj({"name": string, "kind": {"type": "string", "enum": ["face_aggregate"]}, "dimension": {"type": "integer"},
                  "metric": string, "aggregate": {"type": "string", "enum": ["min", "max", "sum"]}})
    return obj({"inequalities": {"type": "array", "items": inequality}, "metrics": {"type": "array", "items": metric}})


LOWER_INSTRUCTIONS = """Generate one improved Python construction/search PROGRAM, not an edge list.
Define generate(context), return 1..context['max_graphs'] objects {'edges': [[u,v],...], 'label': str}.
context contains n, seed, search_steps, parents (actual edge lists), goal and frozen reward_snapshot.
The injected api offers cube_edges(), greedy(edges=(),delete=0,seed=0,weights=None), valid(edges),
metrics(edges), score(edges) returning all reward components, and reward(edges) for this round's focus.
Use api.reward DURING search to select/rank moves, but host validation recomputes every result.
All vertices are integers 0..2**n-1; unique edges have xor a power of two. Graphs must be C4-free.
Programs run with a short CPU budget. Only math/random/itertools/collections/functools/heapq/bisect/statistics imports;
no file/network/process access, print, getattr, private attributes, dunder names, or external packages.
Allowed ordinary builtins include list/dict/set/tuple, sum/min/max, sorted, range, enumerate, zip.
Use actual parent programs and their measured failures to evolve a different useful search, not repeat blindly.
You may cross temporary edge losses and explore nonodd structures; archived local obstructions do not exclude all graphs.
Return JSON matching the schema. Do not invoke tools or edit files. Model-written scores are never trusted.
"""

UPPER_INSTRUCTIONS = """Propose 1..4 integer linear inequality CONJECTURES: sum(coefficient*metric)<=rhs.
Read the actual graph-cluster statistics, previous conjectures/counterexamples, and the exact indicator registry.
Each conjecture quantifies over all C4-free cube subgraphs in the stated dimension satisfying its OWN conditions.
Task conditions are NOT implicit inequality conditions. Use empty conditions for an unconditional conjecture.
Aim for nontrivial correlations that constrain the objective and give construction a useful residual gradient.
Do not only repeat the edge maximum. Prefer short integer coefficients and informative close-to-tight examples.
Sample support is not proof; include the intended mathematical meaning and missing proof obligation in rationale.
You may request at most TWO new declarative face_aggregate metrics over existing base metric names (min/max/sum).
Only use registered metrics or newly requested metrics; no generated evaluator code.
Existing refuted conjectures stay refuted. A changed bound is a new conjecture.
Return JSON matching the schema. Do not invoke tools or edit files. No purported proof status field is accepted.
"""


def propose(role, context, config, directory, registry=None, graphs=None):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    response_path = directory / "response.json"
    receipt_path = directory / "receipt.json"
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text())
        if receipt["status"] != "ok":
            raise RuntimeError(f"saved {role} model failure; inspect {receipt_path}; no automatic retry")
        return json.loads(response_path.read_text()), receipt
    if (directory / "dispatched.json").exists():
        raise RuntimeError(f"ambiguous interrupted model call in {directory}; inspect before explicitly retrying")
    instructions = LOWER_INSTRUCTIONS if role == "lower" else UPPER_INSTRUCTIONS
    prompt = instructions + "\nACTUAL INPUT:\n" + json.dumps(context, ensure_ascii=False, indent=2)
    (directory / "prompt.txt").write_text(prompt)
    if config["backend"] == "offline":
        response = {"programs": [{"name": "offline_greedy_repair", "rationale": "Explicit deterministic baseline, not an LLM call.", "source": OFFLINE_PROGRAM}]} if role == "lower" else {"inequalities": fit_directions(graphs, registry), "metrics": []}
        receipt = {"status": "ok", "backend": "offline", "requested_model": None, "reported_model": None, "role": role}
    elif config["backend"] == "codex":
        executable = shutil.which(config.get("executable", "codex"))
        if not executable:
            raise RuntimeError("codex executable not found; select/install an actual provider explicitly")
        schema = directory / "schema.json"
        schema.write_text(json.dumps(schema_for(role), indent=2))
        model = config.get("model", "gpt-6.1-sol")
        argv = [executable, "exec", "--skip-git-repo-check", "--ephemeral", "--sandbox", "read-only", "--json",
                "--model", model, "-c", 'model_reasoning_effort=' + json.dumps(config.get("effort", "medium")),
                "--output-schema", str(schema.resolve()), "--output-last-message", str(response_path.resolve()),
                "--cd", str(directory.resolve()), "-"]
        (directory / "dispatched.json").write_text(json.dumps({"argv": argv, "role": role}, indent=2))
        receipt = run_process(argv, cwd=directory, stdin=prompt, timeout=config.get("timeout_seconds", 180),
                              stdout_path=directory / "events.jsonl", stderr_path=directory / "stderr.txt")
        receipt.update(backend="codex", requested_model=model, reported_model=None, role=role)
        # A requested model is not independently observed provider identity.
        if receipt["status"] == "ok":
            try:
                response = json.loads(response_path.read_text())
            except (ValueError, OSError) as exc:
                receipt.update(status="invalid_output", error=str(exc))
        if receipt["status"] != "ok":
            receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
            raise RuntimeError(f"{role} model call {receipt['status']}; see {directory}")
    else:
        raise ValueError("backend must be offline or codex")
    response_path.write_text(json.dumps(response, ensure_ascii=False, indent=2) + "\n")
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    return response, receipt
