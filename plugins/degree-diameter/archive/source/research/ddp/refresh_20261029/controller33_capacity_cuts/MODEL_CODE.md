# Code review entry

`run_once.py --prepare-only` copies the inherited canonical model's literal construction, asserts its31845-variable/109466-clause baseline, appends only the stated necessary capacity cuts, and writes `model.cnf`, `MODEL.json`, `EDGE_VARIABLES.json`, and `CAPACITY_TERMS.json`. It exits before solver code.

`run_once.py --solve` requires those saved inputs. It never regenerates CNF and rejects any existing HANDLE or TERMINAL, so repeated invocations cannot silently restart a run. It uses the saved preparation CPU when reporting the aggregate budget. Root must approve this mode separately after review.

The project root is `HERE.parents[3]` for this new directory depth. The old nested `canonical_labeling/solve/` path used `parents[4]`; copying that expression unchanged would be incorrect.

The weighted input list retains multiplicity. A contribution2 inserts the same exact pair-conjunction literal twice. The sequential counter sees occurrences, not a set, and forbids a fourth true occurrence. The flag and pair gates are exact iff definitions; no one-way positive witness is substituted for a full condition.

SAT decoding independently rebuilds adjacency from the495 edge variables plus fixed triangles, checks four-regularity and every ordered adjacent/NB3 route, and derives inverse ports by orienting each designated triangle and each external2-factor cycle. This is a controller-only acceptance step. Large-graph generation remains with root.

Preparation completed after reading `../controller33_route_capacity/PROOF.md`:65890 total variables,194694 clauses,0 solver calls, encoding CPU0.288120746 seconds. The original canonical prefix matched exactly. `MODEL.json` has status `CNF_READY_NOT_SOLVED`; there is no solver HANDLE or TERMINAL. The separately saved old-best statistics pass these new necessary cuts, so no claim of eliminating that object or improving solver performance is made.
