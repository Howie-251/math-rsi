# Read-only implementation review

No blocking issue was found in prepare_model.py, decode_model.py and run_preparation.py. This is a static review against ANALYSIS_MATCHING_ROUTES.md, not a solver or candidate result.

Each selector contains7 disjoint edges between two distinct odd7-orbits. E1 on each of18 source orbits forces9 selectors and a perfect matching. For girth, fixing the first edge and testing the other6 translates catches every self-conflict; the negative unit forbids such a selector. For two selectors, fixing one edge and testing all7 translates of the other, in both endpoint pairings, catches all relevant4/5cycles. Shared-endpoint selector combinations are separately impossible by E1.

The unordered-pair canonicalization uses the minimum simultaneous+18 translate. Y2 uses closed oldB1, including the centre and therefore direct matching edges. OldB2 is True, the diagonal is True, and unsupported Y2 is False. The720 canonical oldfar pairs each consider all126 middle vertices. No whole-source vertex-transitivity is assumed.

Two concrete matching edges may have one selector. No code excludes this: conjunctions are keyed by their Y2 inputs, with an identical-input conjunction reduced to that input. Positive Y2 and AND witness implications suffice existentially, as in the paper proof.

The future decoder checks the complete CNF model, decodes only matching-selector atoms, verifies63 new matching edges and the252-edge simple4-regular graph, and checks actualC7 invariance before using18 representative roots. These future checks have not been rerun by this reviewer.

This reviewer ran zero preparations, graph constructions, BFS or solver calls. Static correctness of the frozen model does not settle its feasibility and does not exclude matching families outside the declaredC7/girth/domain restrictions.
