# Compress the newly found24 automorphisms

Use only the saved24 complete permutations, without rerunning their discovery
or960-arc checks. Try each single generator, then generator pairs, stopping
at the first set generating all24. If pairs fail, retain a greedy generating
set; do not enlarge the controller group or numerical domain. Predict that
two generators suffice. Return actual generators/inverses, multiplication
table, short evaluation words and192 bindings of (orbit representative,
generator word) to the original controller label. Maximum2CPU seconds.

Finite kernel commutation then needs only those generators (192*5 identities
each), plus a generic composition theorem and192 reachability bindings,
instead of checking all24 permutations independently. This is proof-data
compression only, with no graph, rank, BFS, solver or Lean run.
