import json
from pathlib import Path
import tempfile
import unittest

from cube_coevolve.loop import add_graph, initialize, load_config, report
from cube_coevolve.metrics import Registry


ROOT = Path(__file__).resolve().parents[1]


class ProofGoalTests(unittest.TestCase):
    def test_missing_counterexample_never_proves_bound_and_auxiliary_conditions_do_not_hide_one(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "runs" / "test-tmp") as tmp:
            root = Path(tmp)
            config = json.loads((ROOT / "configs/smoke.json").read_text())
            config.update(n=2, seed_files=[], metrics=[], bootstrap_random=0,
                          primary_proof_goal={"statement": "Every C4-free Q2 has at most 2 edges (deliberately false test claim)", "upper_bound": 2})
            # The adversary's extra condition must not suppress a genuine refutation.
            config["goal"] = {"metric": "edges", "sense": "max", "target": 3,
                              "conditions": [{"metric": "min_degree", "op": ">=", "value": 2}]}
            path = root / "config.json"
            path.write_text(json.dumps(config))
            config = load_config(path)
            state = initialize(config, root / "out")
            first = report(state, root / "out")
            self.assertEqual(first["primary_proof_status"], "open")
            add_graph(state, Registry(2), [[0, 1], [0, 2], [1, 3]], {"kind": "test"}, root / "out")
            second = report(state, root / "out")
            self.assertFalse(second["adversarial_target_reached"])
            self.assertEqual(second["primary_proof_status"], "counterexample_pending_independent_verification")
            self.assertEqual(len(second["primary_counterexample_ids"]), 1)

    def test_proof_bound_and_adversarial_threshold_must_agree(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "runs" / "test-tmp") as tmp:
            path = Path(tmp) / "config.json"
            config = json.loads((ROOT / "configs/smoke.json").read_text())
            config["primary_proof_goal"] = {"statement": "test", "upper_bound": 10}
            path.write_text(json.dumps(config))
            with self.assertRaises(ValueError):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
