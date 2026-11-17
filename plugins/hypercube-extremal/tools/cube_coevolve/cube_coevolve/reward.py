"""Frozen-round residual scales and distinct selection channels."""
from .inequalities import applicable, residual, condition_distance


def freeze(inequalities, graphs, goal, challenge_index=0, quality_band=None):
    active = []
    for inequality in inequalities:
        if inequality["status"] not in ("empirical", "exhaustive_verified"):
            continue
        values = sorted(residual(inequality, g["metrics"]) for g in graphs
                        if applicable(g["metrics"], inequality["conditions"]))
        spread = values[3 * (len(values) - 1) // 4] - values[(len(values) - 1) // 4] if values else 0
        scale = max(sum(abs(v) for v in inequality["coefficients"].values()), spread)
        active.append({**inequality, "scale": scale})
    names = [k for k in ("edges", "even_squares", "degree_3", "degree_4", "degree_5", "degree_6", "holes_max_side")
             if graphs and k in graphs[0]["metrics"]]
    feature_scales = {k: max(1, max(g["metrics"][k] for g in graphs) - min(g["metrics"][k] for g in graphs)) for k in names}
    # A tight edge-only bound would otherwise mask every negative correlation residual.
    targets = [i for i in active if any(k != "edges" for k in i["coefficients"])] or active
    challenge_id = targets[challenge_index % len(targets)]["id"] if targets else None
    return {"goal": goal, "inequalities": active, "challenge_id": challenge_id, "challenge_index": challenge_index, "feature_scales": feature_scales,
            "quality_band": quality_band,
            "reference": [{"id": g["id"], "metrics": {k: g["metrics"][k] for k in names}} for g in graphs]}


def score(metrics, snapshot, identifier=None, exclude_self=False):
    goal = snapshot["goal"]
    eligible = applicable(metrics, goal.get("conditions", []))
    margins = {i["id"]: residual(i, metrics) / i["scale"] for i in snapshot["inequalities"]
               if applicable(metrics, i["conditions"])}
    distances = [sum(abs(metrics[k] - g["metrics"][k]) / scale for k, scale in snapshot["feature_scales"].items())
                 / max(1, len(snapshot["feature_scales"]))
                 for g in snapshot["reference"] if not exclude_self or g["id"] != identifier]
    objective = metrics[goal.get("metric", "edges")]
    direction = 1 if goal.get("sense", "max") == "max" else -1
    target = goal["target"]
    floor = (snapshot.get("quality_band") or {}).get("min_edges", 0)
    return {"eligible": eligible, "objective": objective,
            "in_quality_band": metrics["edges"] >= floor, "quality_deficit": max(0, floor - metrics["edges"]),
            "objective_utility": direction * objective,
            "goal_gap": max(0, direction * (target - objective)),
            "goal_reached": eligible and direction * (objective - target) >= 0,
            "condition_distance": condition_distance(metrics, goal.get("conditions", [])),
            "challenge": margins.get(snapshot.get("challenge_id")), "margins": margins,
            "max_violation": max(margins.values(), default=None),
            "tightness": 1 / (1 + abs(margins[snapshot["challenge_id"]])) if snapshot.get("challenge_id") in margins else 0,
            "novelty": min(distances, default=1.0)}


def select_parents(graphs, snapshot, limit=6, round_index=0):
    scored = [(g, score(g["metrics"], snapshot, g["id"], exclude_self=True)) for g in graphs]
    outside = []
    if snapshot.get("quality_band"):
        dense = [(g, s) for g, s in scored if s["in_quality_band"]]
        if dense:
            outside = [(g, s) for g, s in scored if not s["in_quality_band"]]
            scored = dense
    main_limit = limit - 1 if outside and limit > 1 else limit
    channels = {
        "objective": lambda s: (s["eligible"], s["objective_utility"], s["novelty"]),
        "challenge": lambda s: (s["challenge"] is not None, s["challenge"] if s["challenge"] is not None else 0, s["objective_utility"]),
        "novelty": lambda s: (s["novelty"], s["objective_utility"]),
        "condition": lambda s: (-s["condition_distance"], s["objective_utility"], s["novelty"]),
    }
    selected = []
    names = list(channels)
    names = names[round_index % 4:] + names[:round_index % 4]
    for name in names:
        for g, s in sorted(scored, key=lambda row: channels[name](row[1]), reverse=True):
            if g["id"] not in {row["id"] for row in selected}:
                selected.append({**g, "selection_channel": name, "reward": s})
                break
    # Separate champions per empirical metric cell preserve alternative populations.
    cells = set()
    for g, s in sorted(scored, key=lambda row: row[1]["objective_utility"], reverse=True):
        cell = (g["metrics"]["edges"] // 4, g["metrics"]["even_squares"] // 8, g["metrics"]["min_degree"])
        if cell not in cells and g["id"] not in {row["id"] for row in selected}:
            selected.append({**g, "selection_channel": "cell", "reward": s})
            cells.add(cell)
        if len(selected) >= main_limit:
            break
    selected = selected[:main_limit]
    if outside and limit > 1:
        g, s = max(outside, key=lambda row: (row[1]["objective_utility"], row[1]["novelty"]))
        selected.append({**g, "selection_channel": "exploration", "reward": s})
    return selected[:limit]
