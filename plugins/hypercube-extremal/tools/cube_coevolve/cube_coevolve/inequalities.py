"""Integer conjectures, explicit domains, and a genuinely exhaustive tiny oracle."""
import hashlib
import json
import math
import operator
from .graphs import geometry

OPS = {"<=": operator.le, ">=": operator.ge, "==": operator.eq,
       "!=": operator.ne, "<": operator.lt, ">": operator.gt}


def check_conditions(conditions, names):
    if not isinstance(conditions, list):
        raise ValueError("conditions must be a list")
    for c in conditions:
        if not isinstance(c, dict) or set(c) != {"metric", "op", "value"}:
            raise ValueError("conditions require metric/op/value")
        if c["metric"] not in names or c["op"] not in OPS or type(c["value"]) is not int:
            raise ValueError("invalid condition metric/op/integer")


def applicable(metrics, conditions):
    return all(OPS[c["op"]](metrics[c["metric"]], c["value"]) for c in conditions)


def condition_distance(metrics, conditions):
    distance = 0
    for c in conditions:
        x, value, op = metrics[c["metric"]], c["value"], c["op"]
        if OPS[op](x, value):
            continue
        distance += 1 if op == "!=" else abs(x - value) + (op in ("<", ">"))
    return distance


def normalize(raw, registry):
    if not isinstance(raw, dict):
        raise ValueError("inequality must be an object")
    coefficients = raw.get("coefficients", {})
    if not isinstance(coefficients, dict) or not coefficients:
        raise ValueError("inequality needs coefficients")
    if any(k not in registry.names or type(v) is not int for k, v in coefficients.items()):
        raise ValueError("unknown metric or noninteger coefficient")
    coefficients = {k: v for k, v in sorted(coefficients.items()) if v}
    rhs = raw.get("rhs")
    if not coefficients or type(rhs) is not int:
        raise ValueError("nonzero coefficients and integer rhs required")
    conditions = raw.get("conditions", [])
    check_conditions(conditions, registry.names)
    conditions = sorted(conditions, key=lambda c: (c["metric"], c["op"], c["value"]))
    divisor = math.gcd(*coefficients.values(), rhs)
    coefficients = {k: v // divisor for k, v in coefficients.items()}
    rhs //= divisor
    identity = {"n": registry.n, "coefficients": coefficients, "rhs": rhs, "conditions": conditions}
    identifier = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:16]
    return {**identity, "id": identifier, "name": str(raw.get("name", identifier))[:160],
            "rationale": str(raw.get("rationale", ""))[:8000], "status": "untested", "origin": raw.get("origin", "model")}


def residual(inequality, metrics):
    return sum(value * metrics[key] for key, value in inequality["coefficients"].items()) - inequality["rhs"]


def evaluate(inequality, graphs):
    samples = [(g["id"], residual(inequality, g["metrics"])) for g in graphs
               if applicable(g["metrics"], inequality["conditions"])]
    counterexamples = [gid for gid, value in samples if value > 0]
    result = dict(inequality)
    # Evidence from an exhaustive same-domain run is preserved; samples never upgrade it.
    result.update(support_count=len(samples), counterexample_ids=counterexamples,
                  max_residual=max((v for _, v in samples), default=None))
    if counterexamples:
        result["status"] = "refuted"
    elif inequality["status"] not in ("refuted", "exhaustive_verified"):
        result["status"] = "empirical" if samples else "untested"
    return result


def exhaustive_oracle(registry, inequalities):
    n = registry.n
    if n > 3:
        return {"status": "not_run", "reason": "complete enumeration implemented only for n<=3"}, []
    edges, _, squares, _ = geometry(n)
    forbidden = [sum(1 << e for e in s) for s in squares]
    checked = {i["id"]: {"applicable": 0, "max_residual": None, "counterexample": None} for i in inequalities}
    valid_count = 0
    for mask in range(1 << len(edges)):
        if any(mask & s == s for s in forbidden):
            continue
        valid_count += 1
        graph = [e for j, e in enumerate(edges) if mask >> j & 1]
        metrics = registry.compute(graph)
        for inequality in inequalities:
            if not applicable(metrics, inequality["conditions"]):
                continue
            row = checked[inequality["id"]]
            value = residual(inequality, metrics)
            row["applicable"] += 1
            if row["max_residual"] is None or value > row["max_residual"]:
                row["max_residual"] = value
            if value > 0 and row["counterexample"] is None:
                row["counterexample"] = graph
    for row in checked.values():
        row["vacuous"] = row["applicable"] == 0
    report = {"status": "complete", "domain": {"n": n, "simple_cube_subgraphs": True, "C4_free": True},
              "all_edge_subsets": 1 << len(edges), "valid_graphs": valid_count, "inequalities": checked}
    witnesses = [row["counterexample"] for row in checked.values() if row["counterexample"] is not None]
    return report, witnesses


def fit_directions(graphs, registry):
    """Offline fallback selected explicitly, never masquerading as a model."""
    directions = [{"edges": 1}, {"edges": 1, "even_squares": -1},
                  {"edges": 2, "degree_sq_sum": -1}, {"edges": 1, "holes_max_side": 1}]
    output = []
    for co in directions:
        rhs = max(sum(v * g["metrics"][k] for k, v in co.items()) for g in graphs)
        output.append({"name": "sample_support_" + str(len(output)), "coefficients": co,
                       "rhs": rhs, "conditions": [], "origin": "offline_direction_fit",
                       "rationale": "Empirical support plane over the current finite archive, not a theorem."})
    return output
