# Refined polarity73 necessary screen

This separate input extends the baseline variable deletion screen without
changing its saved inputs, models, or results. All 73 deletion decisions and
all deletion sets at retained orders 58/59 remain available. The baseline
CNF is built in memory through its definitions and forms the initial variable
and clause ranges. The parent variable map is copied into the refined map;
the exact inherited ranges, source, counters, and new maps are recorded.

`one[x]` is equivalent in both directions to retention and exactly
`degree_H(x)-7` deleted old neighbors. Thus it means retained degree 7.
For every directed old nonedge, `C[x,y]` implies `one[x]`, retention of y,
and failure of `sat[y]`. Every unit-deficit vertex chooses exactly one y.
If y also has unit deficit, a selected x-to-y edge forces the reverse choice.

For each old nonedge x,s with unique ambient common neighbor m, require

    not one[x] or not sat[s] or not D[m]
        or OR(C[x,y] for y in N_H(s) with xy an old nonedge).

In any monotone degree-eight diameter-two completion, choose the actual
unique new neighbor of each unit-deficit vertex. These choices satisfy the
guards and reciprocity. When all three cover guards hold, the surviving
saturated vertex s keeps all old neighbors, and the lost pair x,s must be
repaired through x's unique new neighbor. That neighbor belongs to N_H(s).
Consequently every actual completion maps to a model of these necessary
conditions, subject to the inherited baseline reduction. No aggregate
linear bound or unproved restriction is added.

Incoming capacity at vertices with larger deficits is deliberately not
constrained. Other old bad pairs and final diameter are not required to be
repaired. A SAT assignment is only a partial neighbor-choice candidate;
neither its original induced graph nor its partial added edges are a target.

The CLI is `screen.py prepare --n 58|59`, `decode --n 58|59`, or bounded
explicit-assignment `sanity --n 58|59`. Preparation saves separate `n58/`
and `n59/` inputs, maps, encoding metadata and semantic sanity. It never
overwrites existing case inputs. No solver is launched by this source.
Root controls preparation and any later bounded solver run after review.

Decode reads the case's `solver.log` unless `--log` is supplied. It checks
the full assignment against every saved CNF clause and recomputes the
baseline, one indicators, choice guards, exact choices, reciprocity and
coverage directly from the preserved H. Failure exits nonzero.
`deletion_candidate.json` records the deletion set, all original bad pairs,
degrees, deficits, saturated/unit sets, directed choices, partial undirected
added edges, and any unconstrained incoming-capacity overflow. The separate
`retained_H.edges` still contains only the old induced graph.

Sanity uses nine explicit D/choice assignments, including both orientations
of a chosen unit pair, two outgoing choices from one source, and deliberately false source, retained-target and
unsaturated-target guards. It compares all sat/one indicators, all constraint
groups and every cover clause with direct predicates. This is not a deletion
search, solver call, completion witness, or runtime guarantee.

2026-10-18 resumed discovery execution: each order receives one no-proof
CaDiCaL run with 30 CPU / 45 wall seconds (soft28), 4 GiB address-space cap.
Any UNSAT returned in this mode is RAW_UNSAT_UNCERTIFIED, not an exclusion.
This supersedes any assumption that discovery automatically emits a proof.
