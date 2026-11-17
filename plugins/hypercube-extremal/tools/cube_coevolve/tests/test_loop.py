import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from cube_coevolve.loop import run, counterexample_view, training_view
from cube_coevolve.inequalities import normalize, evaluate
from cube_coevolve.metrics import Registry
from cube_coevolve.reward import freeze
from cube_coevolve.runtime import execute


ROOT = Path(__file__).resolve().parents[1]


class LoopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_root = ROOT / "runs" / "test-tmp"
        cls.temp_root.mkdir(parents=True, exist_ok=True)

    def test_round_feedback_and_resume(self):
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            out = Path(tmp) / "run"
            first = run(ROOT / "configs/smoke.json", out, 1)
            self.assertEqual(first["completed_rounds"], 1)
            self.assertGreater(first["inequality_statuses"]["exhaustive_verified"], 0)
            lower_receipt = (out / "rounds/0000/lower/receipt.json").read_bytes()
            second = run(None, out, 1, resume=True)
            self.assertEqual(second["completed_rounds"], 2)
            self.assertEqual(lower_receipt, (out / "rounds/0000/lower/receipt.json").read_bytes())
            after = json.loads((out / "rounds/0000/reward_after.json").read_text())
            before = json.loads((out / "rounds/0001/reward_before.json").read_text())
            self.assertEqual(after, before)
            prompt = json.loads((out / "rounds/0001/lower/prompt.txt").read_text().split("ACTUAL INPUT:\n")[1])
            self.assertTrue(prompt["parent_programs"])
            self.assertTrue(all(i["status"] != "refuted" for i in before["inequalities"]))
            self.assertFalse(second["goal_reached"])
            with self.assertRaises(ValueError):
                run(ROOT / "configs/smoke.json", out, 1)

    def test_program_failure_is_not_a_graph(self):
        registry = Registry(2)
        context = {"n": 2, "metric_definitions": [], "focus": "objective", "max_graphs": 2,
                   "reward_snapshot": freeze([], [], {"metric": "edges", "target": 4})}
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            out = execute("import os\ndef generate(context): return []", context, Path(tmp) / "bad")
            self.assertEqual(out["status"], "rejected_source")
            out = execute("def generate(context):\n    while True: pass", context, Path(tmp) / "loop", timeout=1)
            self.assertNotEqual(out["status"], "ok")
            self.assertEqual(out["graphs"], [])
            out = execute("def generate(context): return [{'edges': [[0,1],[0,2],[1,3]]}]", context, Path(tmp) / "good")
            self.assertEqual(out["status"], "ok")
            self.assertEqual(len(out["graphs"]), 1)
            out = execute("def generate(context): return 1/0", context, Path(tmp) / "crash")
            self.assertIn("ZeroDivisionError", out["stderr_tail"])

    def test_heldout_refutation_is_visible_to_upper(self):
        registry = Registry(2)
        empty = {"id": "empty01", "n": 2, "edges": [], "metrics": registry.compute([])}
        witness = {"id": "witness00", "n": 2, "edges": [[0, 1], [0, 2], [1, 3]], "metrics": registry.compute([(0, 1), (0, 2), (1, 3)])}
        graphs = [empty, witness]
        view, _ = training_view(graphs, registry)
        self.assertEqual(view["challenge_ids_not_shown"], [witness["id"]])
        inequality = evaluate(normalize({"coefficients": {"edges": 1}, "rhs": 0}, registry), graphs)
        actual = counterexample_view({"graphs": graphs, "inequalities": [inequality]})
        self.assertEqual(actual[0]["edges"], witness["edges"])
        self.assertEqual(actual[0]["metrics"]["edges"], 3)

    def test_new_metric_is_recomputed_and_fed_back(self):
        from cube_coevolve import loop
        original = loop.propose
        calls = []
        def proposer(role, context, config, directory, registry=None, graphs=None):
            if role == "lower":
                calls.append(context)
                return original(role, context, config, directory, registry, graphs)
            return {"metrics": [{"name": "q2_edges_min_new", "kind": "face_aggregate", "dimension": 2, "metric": "edges", "aggregate": "min"}] if len(calls) == 1 else [],
                    "inequalities": [{"name": "new_metric_bound", "coefficients": {"q2_edges_min_new": 1}, "rhs": 3, "conditions": []}]}, {"status": "ok", "backend": "test"}
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp, patch.object(loop, "propose", proposer):
            output = Path(tmp) / "run"
            run(ROOT / "configs/smoke.json", output, 2)
            self.assertIn("q2_edges_min_new", calls[1]["registry"]["definitions"][-1]["name"])
            self.assertTrue(all("q2_edges_min_new" in row["metrics"] for row in calls[1]["parents"]))
            self.assertTrue(any("q2_edges_min_new" in i["coefficients"] for i in calls[1]["reward_snapshot"]["inequalities"]))

    def test_failed_model_is_not_retried_or_replaced(self):
        from cube_coevolve import providers
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            directory = Path(tmp) / "model"
            config = {"backend": "codex", "model": "gpt-6.1-sol"}
            with patch.object(providers.shutil, "which", return_value="/test/codex"), patch.object(providers, "run_process", return_value={"status": "failed", "returncode": 1}) as caller:
                for _ in range(2):
                    with self.assertRaises(RuntimeError):
                        providers.propose("lower", {}, config, directory)
                self.assertEqual(caller.call_count, 1)
                receipt = json.loads((directory / "receipt.json").read_text())
                self.assertEqual(receipt["backend"], "codex")
                self.assertEqual(receipt["status"], "failed")


if __name__ == "__main__":
    unittest.main()
