import unittest
from cube_coevolve.metrics import Registry
from cube_coevolve.reward import freeze, score, select_parents
from cube_coevolve.runtime import SearchAPI
from cube_coevolve.inequalities import normalize, evaluate
from cube_coevolve.loop import training_view


class QualityBandTests(unittest.TestCase):
    def setUp(self):
        self.registry = Registry(2)
        self.path = [[0, 1], [0, 2], [1, 3]]
        self.graphs = [{"id": "dense01", "edges": self.path, "metrics": self.registry.compute(self.path)},
                       {"id": "sparse02", "edges": [[0, 1]], "metrics": self.registry.compute([[0, 1]])},
                       {"id": "empty03", "edges": [], "metrics": self.registry.compute([])}]

    def test_novelty_cannot_trade_away_quality_band(self):
        snapshot = freeze([], self.graphs, {"metric": "edges", "target": 4}, quality_band={"min_edges": 3})
        api = SearchAPI({"n": 2, "metric_definitions": [], "reward_snapshot": snapshot, "focus": "novelty"})
        self.assertGreater(api.reward(self.path), api.reward([]))
        self.assertGreater(api.reward(self.path), api.reward([[0, 1], [0, 2]]))
        parents = select_parents(self.graphs, snapshot)
        self.assertLessEqual(sum(g["metrics"]["edges"] < 3 for g in parents), 1)

    def test_discovery_prefers_dense_but_validation_checks_sparse(self):
        view, train = training_view(self.graphs, self.registry, {"min_edges": 3})
        self.assertEqual([g["id"] for g in train], ["dense01"])
        candidate = normalize({"coefficients": {"edges": -1}, "rhs": -3}, self.registry)
        self.assertEqual(evaluate(candidate, train)["status"], "empirical")
        self.assertEqual(evaluate(candidate, self.graphs)["status"], "refuted")

    def test_real_counterexample_outside_band_retains_reward(self):
        candidate = evaluate(normalize({"coefficients": {"edges": 1}, "rhs": 1}, self.registry), [self.graphs[2]])
        snapshot = freeze([candidate], [self.graphs[2]], {"metric": "edges", "target": 4}, quality_band={"min_edges": 3})
        api = SearchAPI({"n": 2, "metric_definitions": [], "reward_snapshot": snapshot, "focus": "challenge"})
        edges = [[0, 1], [0, 2]]
        self.assertFalse(api.score(edges)["in_quality_band"])
        self.assertGreater(api.reward(edges), 2)


if __name__ == "__main__":
    unittest.main()
