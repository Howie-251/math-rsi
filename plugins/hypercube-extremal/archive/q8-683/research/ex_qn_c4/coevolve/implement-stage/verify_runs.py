"""Read-only artifact checks, separate from generated search programs."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from cube_coevolve.graphs import validate, graph_id
from cube_coevolve.metrics import Registry
from cube_coevolve.inequalities import evaluate


def check(name):
    run = ROOT / "runs" / name
    state = json.loads((run / "state.json").read_text())
    registry = Registry(state["config"]["n"], state["metric_definitions"])
    for graph in state["graphs"]:
        edges, verification = validate(registry.n, graph["edges"])
        assert graph["id"] == graph_id(registry.n, edges)
        assert graph["metrics"] == registry.compute(edges)
        assert graph["verification"] == json.loads(json.dumps(verification))
        saved = json.loads((run / "graphs" / (graph["id"] + ".json")).read_text())
        assert saved == graph
    for inequality in state["inequalities"]:
        assert evaluate(inequality, state["graphs"]) == inequality
        if registry.n > 3:
            assert inequality["status"] != "exhaustive_verified"
    calls = []
    valid_outputs = 0
    for row in state["rounds"]:
        directory = run / "rounds" / f"{row['round']:04d}"
        for side in ("lower", "upper"):
            receipt = json.loads((directory / side / "receipt.json").read_text())
            assert receipt["status"] == "ok"
            calls.append({"round": row["round"], "side": side, "backend": receipt["backend"], "requested_model": receipt.get("requested_model"), "reported_model": receipt.get("reported_model")})
        before = json.loads((directory / "reward_before.json").read_text())
        for pid in row["program_ids"]:
            runtime_input = json.loads((directory / pid / "input.json").read_text())
            assert runtime_input["reward_snapshot"] == before
            assessment = json.loads((directory / pid / "evaluation.json").read_text())
            valid_outputs += sum(g["status"] == "accepted" for g in assessment["outputs"])
        if row["round"]:
            prior = run / "rounds" / f"{row['round']-1:04d}" / "reward_after.json"
            # Earlier development runs can predate reward fixes. The final Q8 run must be continuous.
            if name == "q8_live":
                assert json.loads(prior.read_text()) == before
                prompt = json.loads((directory / "lower" / "prompt.txt").read_text().split("ACTUAL INPUT:\n")[1])
                assert prompt["parent_programs"]
    summary = json.loads((run / "summary.json").read_text())
    assert summary["completed_rounds"] == state["completed_rounds"]
    return {"run": name, "status": "PASS", "n": registry.n, "rounds": state["completed_rounds"],
            "graphs_rechecked": len(state["graphs"]), "accepted_program_outputs": valid_outputs,
            "best_objective": summary["best_objective"], "goal_reached": summary["goal_reached"],
            "inequality_statuses": summary["inequality_statuses"], "calls": calls}


if __name__ == "__main__":
    print(json.dumps([check(name) for name in sys.argv[1:]], ensure_ascii=False, indent=2))
