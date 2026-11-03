# Why the joint CEG reduction is exact for its stated domain

For line L, define its point-cover set as the union of the cached radius-(D-1) balls of its three actual pins. A selected line covers t iff at least one pin of L covers t. Taking the OR of the incident-line masks of all pin coverers of t therefore produces the exact selector clause for that target. No complete-fiber condition is involved.

A union of at most five three-point free lines has at most15 distinct free pins. Retain all source edges and join the new vertex exactly to that union. Its distance to old t is one plus the distance from the union to t, so full point coverage plus actual degree legality proves the new diameter bound. SAT is accepted only after the full n-point cache OR and eventual actual-degree/edge checks.

Every initial test point is a necessary target. If a SAT assignment misses t in the authoritative full point OR, its current selectors have no intersection with t's exact support clause. Adding that clause excludes the assignment while preserving every possible complete cover. The negative point is another ordinary valid target clause. Monotone additions change constraints rather than select an improved-score candidate or retry a seed.

Consequently a completed UNSAT result at any round rules out the complete stated five-line domain even though only a subset of all targets was present. A SAT result at a partial round is only a candidate. UNKNOWN, time budget or the fixed round bound leaves the family unresolved. In this run both initial formulas returned rawUNSAT; no CEG candidate or extra clause was generated. This note does not certify the solver's UNSAT proof and does not exclude unrestricted15-pin sets.
