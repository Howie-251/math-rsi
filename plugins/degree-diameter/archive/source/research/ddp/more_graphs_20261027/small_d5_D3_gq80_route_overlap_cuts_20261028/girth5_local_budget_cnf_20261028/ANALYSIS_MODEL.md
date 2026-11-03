# Local route budgets as sequential-unary CNF

The original girth5 model, model.cnf and VARIABLE_MAP.json are read only. Its first1080variables and35720clauses are unchanged. For each of80roots, the cached old C(x)\{x} has12vertices and54allowed own-side matching edges. The inherited route proof gives a_x<=3: of26far targets other than the matched mate, own-first contributes8, own-last exactly12−2a_x, and opposite relays at most12, hence26<=32−2a_x. This is necessary for D3 in the complete girth5 model, so the added budget preserves that integer graph family. It does not guarantee D3.

For inputs x1..x54, allocate distinct unary threshold variables s[i,j], i1..54,j1..3. The clauses are: x_i⇒s[i,1]; s[i−1,j]⇒s[i,j]; (x_i and s[i−1,j−1])⇒s[i,j] for j2,3; not(x_i and s[i−1,3]); and boundary not s[i,j] where j>i. The first carry/overflow row begins at i2.

If at least j inputs in the first i positions are true, induction forces s[i,j]. A fourth true input therefore conflicts with the overflow clause. Conversely, any input assignment of weight<=3 extends by s[i,j] iff the actual prefix weight is at least j; all clauses then hold. Thus existential auxiliary assignment is equivalent to the intended at-most-three constraint. The auxiliaries need not be unique.

Each54-input counter has162auxiliaries and375clauses (54input,159carry,106increment,53overflow,3boundary). All80give12960auxiliaries/30000newclauses, for14040total variables and65720clauses. EdgeIDs1..1080 are preserved; auxiliaries1081..14040 occupy disjoint per-root ranges. COUNTERS.json saves each54original-edge and DIMACS-input list, aux range, and exact full-CNF clause range; COUNTER_CLAUSES.json saves all clauses.

COUNTER_CALIBRATION.json records every input assignment for n1..8 (510patterns) and7n54boundary controls, using canonical prefix extensions for valid weights and unit-propagation contradictions for overflow. These are encoding checks, not graph-model solver calls. Calibration runs before the single CaDiCaL invocation and failure would stop without that call.

SAT witness decoding uses only the inherited1080edge records and never auxiliary IDs. All65720clauses, original matching/cover rows, girth restrictions, overlap inequalities and all80a_x counts are checked before exporting80/200edges. Full graph BFS remains with the parent after an actual candidate. The one-t30/35CPU/45wall bounded call has no automatic continuation, seed, encoding switch or additional cut loop.
