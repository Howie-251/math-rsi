import random
import unittest
from cube_coevolve.graphs import validate, geometry, greedy
from cube_coevolve.metrics import Registry
from cube_coevolve.inequalities import normalize, evaluate, exhaustive_oracle
from cube_coevolve.reward import freeze, score


class CoreTests(unittest.TestCase):
    def test_literal_validation(self):
        for invalid in ([[0, 1], [1, 0]], [[0, 3]], [[False, 1]], list(geometry(2)[0])):
            with self.assertRaises(ValueError):
                validate(2, invalid)
        edges, report = validate(2, [[0, 1], [0, 2], [1, 3]])
        self.assertTrue(report["valid"])
        self.assertEqual(Registry(2).compute(edges)["edges"], 3)

    def test_actual_q8_seed(self):
        from pathlib import Path
        from cube_coevolve.graphs import read_edges
        path = Path(__file__).resolve().parents[3] / "archive/q8-683/research/ex_qn_c4/proofs/q8_seed_isometries_cycle011/seed1.edges"
        edges, _ = validate(8, read_edges(path))
        metrics = Registry(8).compute(edges)
        self.assertEqual((metrics["edges"], metrics["even_squares"]), (682, 0))
        self.assertEqual([metrics[f"degree_{d}"] for d in (4, 5, 6)], [2, 168, 86])

    def test_face_metric_and_exact_counts(self):
        registry = Registry(3, [{"name": "q2_edge_sum", "kind": "face_aggregate", "dimension": 2, "metric": "edges", "aggregate": "sum"}])
        edges, _ = validate(3, greedy(3, random.Random(7)))
        m = registry.compute(edges)
        self.assertEqual(m["q2_edge_sum"], 2 * len(edges))
        self.assertEqual(m["p0_holes"] + m["p1_holes"], 2 - m["stars3"])
        q8 = Registry(8, [{"name": "Jmin", "kind": "face_aggregate", "dimension": 7, "metric": "q7_J", "aggregate": "min"}])
        self.assertIn("38448 - 126*edges", q8.describe()["face_base_definitions"]["7"]["q7_J"])

    def test_conditions_counterexample_and_exhaustive_domain(self):
        registry = Registry(2)
        good = normalize({"coefficients": {"edges": 1}, "rhs": 3}, registry)
        bad = normalize({"coefficients": {"edges": 1}, "rhs": 2}, registry)
        impossible = normalize({"coefficients": {"edges": 1}, "rhs": -1,
                                "conditions": [{"metric": "min_degree", "op": ">=", "value": 3}]}, registry)
        report, witnesses = exhaustive_oracle(registry, [good, bad, impossible])
        self.assertEqual(report["all_edge_subsets"], 16)
        self.assertEqual(report["valid_graphs"], 15)
        self.assertEqual(report["inequalities"][good["id"]]["max_residual"], 0)
        self.assertEqual(report["inequalities"][impossible["id"]]["applicable"], 0)
        self.assertEqual(len(witnesses), 1)
        graph = {"id": "literal", "metrics": registry.compute(witnesses[0])}
        self.assertEqual(evaluate(bad, [graph])["status"], "refuted")
        self.assertEqual(evaluate(impossible, [graph])["status"], "untested")
        self.assertEqual(exhaustive_oracle(Registry(8), [])[0]["status"], "not_run")

    def test_reward_scope_and_scale_invariance(self):
        registry = Registry(2)
        graph = {"id": "a", "metrics": registry.compute([(0, 1)])}
        rows = [normalize({"coefficients": {"edges": c}, "rhs": 3*c}, registry) for c in (1, 7)]
        goal = {"metric": "edges", "target": 2, "conditions": [{"metric": "min_degree", "op": ">=", "value": 1}]}
        scores = [score(graph["metrics"], freeze([evaluate(i, [graph])], [graph], goal)) for i in rows]
        self.assertEqual(scores[0], scores[1])
        self.assertFalse(scores[0]["eligible"])
        self.assertFalse(scores[0]["goal_reached"])
        self.assertLess(scores[0]["challenge"], 0)

    def test_edge_bound_cannot_mask_correlation_reward(self):
        registry = Registry(2)
        graph = {"id": "a", "metrics": registry.compute([(0, 1), (0, 2), (1, 3)])}
        edge = normalize({"coefficients": {"edges": 1}, "rhs": 3}, registry)
        correlation = normalize({"coefficients": {"edges": 1, "min_degree": 1}, "rhs": 5}, registry)
        snapshot = freeze([evaluate(edge, [graph]), evaluate(correlation, [graph])], [graph], {"metric": "edges", "target": 4})
        result = score(graph["metrics"], snapshot)
        self.assertEqual(snapshot["challenge_id"], correlation["id"])
        self.assertEqual(result["max_violation"], 0)
        self.assertLess(result["challenge"], 0)

    def test_duplicate_candidate_gets_zero_novelty(self):
        registry = Registry(2)
        graph = {"id": "a", "metrics": registry.compute([(0, 1), (0, 2), (1, 3)])}
        empty = {"id": "empty", "metrics": registry.compute([])}
        snapshot = freeze([], [graph, empty], {"metric": "edges", "target": 4})
        self.assertEqual(score(graph["metrics"], snapshot, "a")["novelty"], 0)
        self.assertGreater(score(graph["metrics"], snapshot, "a", exclude_self=True)["novelty"], 0)

    def test_challenge_schedule_covers_four_candidates(self):
        from cube_coevolve.loop import challenge_turn_index
        registry = Registry(2)
        graph = {"id": "a", "metrics": registry.compute([(0, 1)])}
        rows = [evaluate(normalize({"coefficients": {"edges": 1, "degree_sq_sum": k}, "rhs": 20}, registry), [graph]) for k in range(1, 5)]
        targets = [freeze(rows, [graph], {"metric": "edges", "target": 4}, challenge_turn_index({}, i))["challenge_id"] for i in (1, 5, 9, 13)]
        self.assertEqual(len(set(targets)), 4)


if __name__ == "__main__":
    unittest.main()
