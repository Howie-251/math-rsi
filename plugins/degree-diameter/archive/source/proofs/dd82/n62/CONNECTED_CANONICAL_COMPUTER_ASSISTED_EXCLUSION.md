# Order-62 exclusion through two connected canonical inputs

## Claim and current status

Completed computer-assisted mathematical integration. The one bounded full-chain
review and Gemini final review on2026-10-11 found no remaining coverage or
candidate-preservation gap; see [the review record](../../../context/dd82/N62_EXISTING_PROOF_CHECK.md).
The theorem is: no finite simple graph on 62 vertices has maximum
degree at most eight and diameter at most two. The argument combines the
retained paper reductions, the external finite component-quotient
classification, and two independently checked LRAT proofs. It is not a
completed Lean theorem.

The two particular CNFs below are certificate-checked UNSAT. The complete
coverage and satisfiability-preservation argument in Sections1–4 transfers
that result to arbitrary original graphs; the review checked this mathematical
connection separately from the solver and checker exit codes. Current mathematical
range is57≤N(8,2)≤61. n62 has exited the active construction-first research queue.

## 1. Every original candidate supplies a D1 root and the global cuts

Let G be an arbitrary graph with the stated original hypotheses.
Regularity gives degree eight at every vertex. Define its actual matrix
B=A²+A−7I−J, with nonnegative integer entries and every row sum three.

Use CONNECTED_REPEAT_REDUCTION.md with its explicit dependencies. The
triple-repeat import is now TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md,
which retains the recovered analytic original-graph Steps 1–3 and uses
the unconditional actual quotient trace identity. It no longer uses
the former finite triple-repeat matrix table. The separate finite
component-quotient classifications for c=3,5,7,9 remain external
computer-assisted dependencies, with their coverage proofs and independent
implementations retained.

The connected-support reduction proves that G is triangle-free, all
double-repeat pairs are D1, and their unordered count d is one of
1,3,5,7,9. In particular there is a D1 pair, and d≤9. Neither
triangle-freeness nor connectedness is assumed in the original theorem.

Select any D1 pair. The D1 existence/outlet reduction and local parent
classification give a D1_MATCH root with the actual archived parent
template. The hard-branch and C4 transport papers then derive the
distinguished neighborhoods and repeat rows. They do not require
independent original/repeat matrices, an automorphism of G, or an
unproved identification of their matchings.

## 2. Exactly two canonical representatives cover the survivors

Apply D1_MATCH_CANONICAL_DIAGNOSTIC_COVERAGE.md. First normalize the
root-neighbor labels, then the classes of c and b, and finally the
distinguished points inside each class. These operations give one
graph isomorphism preserving all the derived data and the D1 template.

The possible representatives are b=28,34,41. The b=34 case is excluded
by the actual common-neighbor equation with root-neighbor label 5:
r=16 has exactly one original neighbor in C5, whereas distinct b and
c=35 would both lie there. Thus G has a relabeling with b=28 or b=41.

No historical symmetry breaker is combined with these labels. The
unassigned endpoints s,t,f,g retain their stated domains. Complete rows
have all omitted entries zero; partial rows impose only their explicit
fixed entries, support and exactly-one group constraints. Consequently
the two representatives provide coverage up to relabeling, not an
assertion that two unlabeled graphs or two unique labelings exhaust G.

## 3. Every relabeled graph extends to a satisfying assignment

For the concrete D1_MATCH template, use the forward witness construction
in CNF_BRIDGE_OBLIGATIONS.md. Assign each primary edge its actual adjacency,
each dynamic B1/B2 selector the truth of B_uv=1/2, and each tau its actual
triangle membership. Assign all AND/XOR and truncated unary auxiliaries
their indicated Boolean functions and prefix counts.

That paper checks every base clause family and the necessary depth
premise for guarded exact counters. The concrete parent-map metadata
satisfy the remaining-degree and singleton-class requirements; this
does not quantify over arbitrary schema-valid JSON.

The old d1_hard_diagnostic.py adds the reviewed canonical rows, fixed
entries, partial-row group counts and structural zero blocks. The
hard-branch and C4 proofs justify all those additions. In particular
B(C1,outside C2∪C3∪C4)=0, B[C2]=0 and B(C3,C4)=0; the original
independence of C1,C2,C3,C4 follows from their triangle-free parents.
The previously distinguished tau-false units also follow from those
proofs. No absent JSON field automatically becomes a constraint.

The new d1_connected_diagnostic.py preserves the old clause order and
appends only these two global consequences from Section 1:

1. All 62 tau variables are false.
2. The unordered number of double-repeat pairs is at most nine.

For the second condition, the 1,891 unordered pairs divide into 89
template-fixed pairs and 1,802 dynamic pairs. The only fixed double is
(0,9). Each dynamic pair has exactly one B2 selector, counted once.
Therefore d=1+sum(dynamic B2), so the required bound is sum(B2)≤8.

The added counter uses fresh variables and thresholds through level nine.
Its recurrence is s(i,j) iff s(i−1,j) OR (x_i AND s(i−1,j−1)), with
the first-level and boundary specializations. Assigning thresholds by
actual prefix counts satisfies every defining clause, and forbidding
the final ninth threshold is valid because d≤9. Thus every actual
candidate has a satisfying extension to one of the two exact new CNFs.

The complete emitted-clause agreement, mapping and resource records
live beside the inputs in computations/dd82/n62/d1_connected_diagnostic/.
Exact regeneration from the full archived base encoder, old canonical
driver and new connected driver reproduced all seven saved CNF files
byte-for-byte, including headers and clause order, and reproduced the
complete variable map. The record is regeneration_verification.json;
verify_d1_connected_regeneration.py is the reproducer. This took 5.24
seconds on one CPU, without a solver or checker rerun. Temporary outputs
were removed. It establishes the concrete emitted-file correspondence,
beyond map equality or numerical clause counts alone.

## 4. The two exact formulas are certificate-checked UNSAT

All paths here are below
computations/dd82/n62/d1_connected_diagnostic/.

| Case | CNF file | Variables | Clauses | Complete LRAT file |
|---|---|---:|---:|---|
| b=28 | D1_HARD_b_28.cnf | 444839 | 1633418 | D1_HARD_b_28.bounded120.lrat |
| b=41 | D1_HARD_b_41.cnf | 444839 | 1633419 | D1_HARD_b_41.bounded120.lrat |

The original solver runs returned UNSAT in about 43.5 and 60.0 wall
seconds. Their RAW records remain historical execution evidence.
The complete binary LRAT traces were then independently checked by
the official arminbiere/lrat-trim release0.2.0 with --no-trim, against
the respective exact saved CNF paths. Both checks returned exit20 and
s VERIFIED, in about 1.1 and 1.5 wall seconds.

Checker source/build metadata, exact invocations, complete logs and
the separate certificate outcomes are in .tools/dd82-lrat-check/ and
certificate_checks/results.json. These checks ran on one CPU without
rerunning the solver. They establish UNSAT for those concrete formulas
under the external checker, not Lean kernel evaluation.

Section 3 gives a satisfying assignment to one formula if G exists.
The checked UNSAT results contradict it. Subject to the retained
paper and finite-quotient imports and the reviewed exact compiler
correspondence, no such G exists.

## 5. Scope of the resulting bound

Once the integration is accepted, it supplies a computer-assisted
order-62 exclusion in this project. Combined with the cited classical
63–65 exclusions and Moore counting, it gives the mathematical bound
N(8,2)≤61. The verified 57-vertex construction supplies the lower bound.

It does not determine which of 57,58,59,60,61 is optimal. The complete
Lean arbitrary-graph chain remains unfinished: connectedness and the
finite component classification, the canonical graph-to-CNF bridge,
and kernel-checked evaluation of the two contradiction certificates
are not supplied by lrat-trim. No new axioms, sorry, or native_decide
are introduced. Dedicated reproving of known63–65 remains stopped.
