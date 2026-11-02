# Complete coverage check of the order-58 f=9 C7 branch

The saved normalized domain of 10,080 ordered triples has been checked
completely. None constructs a diameter-two graph. Its minimum is 105
unordered pairs at distance greater than two, attained by 288 triples.
The best complete graph has 58 vertices, 232 edges and degree eight.
This result concerns the **f=9 branch of an order-seven automorphism**;
it does not exclude arbitrary order-58 graphs or the general false-twin
construction with 28 independent matching interfaces.

Status: exact finite calculation completed, with a complete domain proof
below. Independent BFS of the best graph agrees with all 105 predicted
bad pairs. Gemini review is pending. No solver was invoked.

Parent mechanism run: `dd82-v3-f9-c7-20261013-0749`.

## 1. Assumptions and dependencies

A target is a simple graph of order 58, maximum degree at most eight and
diameter at most two. It must be eight-regular, since a vertex of degree
at most seven reaches at most 1+7+7·7=57 vertices in two steps.

The structural dependency is
[FALSE_TWINS58_EIGHT_SIX_FIBERS.md](FALSE_TWINS58_EIGHT_SIX_FIBERS.md),
Sections 1–5. Its exact false-twin representation and the f=9 fixed-set
reduction are used here. In particular, the f=9 branch has fixed induced
graph K1,8 and two fixed leaves with the same nonfixed seven-orbit of
neighbours. These leaves are false twins. The general false-twin theorem
then gives eight independent six-vertex fibres joined pairwise by perfect
matchings.

The f=9 action fixes one of these fibres pointwise and cycles the other
seven. Coordinates given by the matching to the fixed fibre make all
seven such matchings identity. Thus the 21 remaining interfaces are
specified by three permutations A,B,C in S6, at cyclic distances 1,2,3.
Reverse directions use their inverses. This is a coordinate normalization,
not a restriction on the target.

## 2. The finite domain preserves every candidate

Use row-source permutation matrices and write

\[
P_1=A,\quad P_2=B,\quad P_3=C,\quad
P_4=C^T,\quad P_5=B^T,\quad P_6=A^T.
\]

Coverage from the fixed fibre to an outer fibre requires

\[
K_\infty=I+\sum_{e=1}^6P_e\ge J_6.
\]

The matrix K_∞ has row and column sums seven, so K_∞−J is a symmetric
permutation matrix. Its diagonal entry at x is twice the number of
A,B,C fixing x. Hence all three permutations are derangements and this
residual permutation has no fixed points. Simultaneously relabelling the
six coordinates in all fibres normalizes it to

\[
F=(01)(23)(45),\qquad
A+A^T+B+B^T+C+C^T=J-I+F.\tag{1}
\]

The existing preparation enumerated all 265² ordered derangement pairs
A,B. For a nonnegative residual

\[
L=J-I+F-A-A^T-B-B^T,
\]

L is a symmetric loopless degree-two multigraph. A doubled edge forces
the corresponding transposition of C, and each simple cycle allows its
two orientations. This lists every C with C+C^T=L. The preparation has
4,568 admissible A,B pairs and exactly 10,080 distinct ordered triples:

| Components of L | A,B pairs | C orientations per pair |
| --- | ---: | ---: |
| 2+2+2 | 112 | 1 |
| 2+4 | 840 | 2 |
| 3+3 | 528 | 4 |
| 6 | 3,088 | 2 |

The actual input is
[triples.txt](../../../computations/dd82/construction/false_twins58_f9_domain_run/triples.txt),
produced by
[false_twins58_f9_domain_prepare.py](../../../computations/dd82/construction/false_twins58_f9_domain_prepare.py).
The new experiment reads this saved input, checks its length, distinctness,
permutation and derangement properties, and rechecks (1) for every triple.
It does not claim that the resulting graphs are pairwise nonisomorphic.

## 3. A triple determines one complete graph and four exact conditions

The concrete vertex labels are

- false twins u=0 and v=1;
- fixed parent h=2 and outer parents s_t=3+t, for t∈Z7;
- fixed fibre vertices ℓ_a=10+a, for a=0,…,5;
- outer fibre vertices x_(t,a)=16+6t+a.

Join each twin to all eight parents; join h to all ℓ_a; join s_t to its
six x_(t,a); join ℓ_a to x_(t,a) for every t; and join
x_(t,a) to x_(t+d,P_d(a)) for d=1,2,3 and every t,a.
These prescriptions give exactly

\[
16+6+42+42+126=232
\]

distinct edges. All 58 vertices have degree eight. This uniquely specifies
the labelled complete graph for each triple. The permutation that rotates
t and fixes the other labels is an automorphism of cycle type 1^9 7^7.

All pairs outside different fibres have distance at most two by the
false-twin representation. The fixed-fibre/outer-fibre pairs are covered
by K_∞. For two outer fibres at difference d, the **complete** route-count
matrix is

\[
K_d=I+P_d+
\sum_{e\in\mathbb Z_7\setminus\{0,d\}}P_eP_{d-e}.\tag{2}
\]

Here I counts the route through the fixed fibre, P_d the direct matching,
and the five summands the routes through the other outer fibres. Parents
and twins provide no additional path of length at most two for such a
pair. With row-source permutations, the product sends x to
P_(d−e)(P_e(x)); this is the order used by the implementation.

Every K_d has row and column sums seven. The six possible differences
occur in transpose pairs, so the graph is a target if and only if all
four matrices K_∞,K_1,K_2,K_3 are entrywise at least J. Equivalently, each
difference K−J is a permutation matrix. Thus no further coverage condition
is omitted and none has been imposed beyond actual diameter two.

For d=1,2,3 let z_d be the number of zero entries of K_d. The seven
unordered fibre pairs at each cyclic distance are distinct, and the
three distances partition all 21 unordered outer-fibre pairs. Therefore
the exact number of unordered graph pairs at distance greater than two is

\[
\operatorname{bad}(A,B,C)=7(z_1+z_2+z_3).\tag{3}
\]

The saved list of failing vertex pairs is obtained by translating those
zero entries to all seven outer positions. This is an exact formula,
but is not described as an independent BFS.

## 4. Completed run and actual failed candidate

The new evaluator is
[false_twins58_f9_coverage.py](../../../computations/dd82/construction/false_twins58_f9_coverage.py).
The first 64 triples were also expanded into actual adjacency sets. For
every unordered pair, a direct-edge/common-neighbour check agreed with
(3) and the full predicted failing-pair list. This was a prefix sanity
check inside the same episode. The prefix was not repeated.

The first-64 CPU measurement was 0.050239952 seconds, projecting
7.912792440 seconds for the complete domain, below the 60 CPU second cap.
The same run then completed all 10,080 triples:

| Quantity | Result |
| --- | ---: |
| Input triples / evaluated triples | 10,080 / 10,080 |
| Hub equations verified | 10,080 |
| Passing K_1 alone | 0 |
| Passing K_2 alone | 0 |
| Passing K_3 alone | 0 |
| Passing all four conditions | 0 |
| Minimum bad pairs | 105 |
| Triples attaining the minimum | 288 |
| CPU seconds, complete experiment | 0.571976676 |
| Wall seconds, complete experiment | 0.606043994 |
| Reported peak RSS, KiB | 432,020 |
| Solver calls | 0 |

The completion flag is true, with stop reason `full_domain_exhausted`.
Every triple's three zero counts and total bad count are saved in
[scores.csv](../../../computations/dd82/construction/false_twins58_f9_coverage_run/scores.csv).
The full histogram, all 288 minimizing input positions, prefix profile
and resource measurements are in
[result.json](../../../computations/dd82/construction/false_twins58_f9_coverage_run/result.json).

The saved first minimum is input line 704, with image lists

\[
\begin{aligned}
A&=[1,2,0,4,5,3],\\
B&=[3,5,4,2,1,0],\\
C&=[4,0,3,1,5,2].
\end{aligned}
\]

It has (z_1,z_2,z_3)=(3,7,5), hence 105 bad pairs. The complete graph is
[candidate.best.edges](../../../computations/dd82/construction/false_twins58_f9_coverage_run/candidate.best.edges)
and
[candidate.best.json](../../../computations/dd82/construction/false_twins58_f9_coverage_run/candidate.best.json).
The matrices, all 105 predicted bad pairs, parameters, vertex labels and
the explicit automorphism are in
[candidate.best.parameters.json](../../../computations/dd82/construction/false_twins58_f9_coverage_run/candidate.best.parameters.json).
All 232 edges were directly checked under the saved automorphism.
This is a complete failed graph, not a target or a construction claim.

## 5. Consequence and scope

Every target in the f=9 C7 branch has a normalized representative in the
saved domain by Section 2. Every triple uniquely determines its complete
graph, and Section 3 proves that the tested conditions are necessary and
sufficient. The completed finite check finds no passing triple. Subject
to the cited structural reduction and this finite computation, **there
is no target in the order-58 f=9 C7 branch**.

The general eight-by-six matching-cover family still has 28 independently
chosen matchings. The other possible fixed-set branches of an order-seven
automorphism and graphs without that automorphism are outside this
experiment. No continuation, alternative seed, SAT instance or additional
family search was launched.

## 6. V3 workflow and review boundary

This task followed
[DD82_V3_ARIS_GEMINI_PLAN_20261013.md](../../../context/dd82/DD82_V3_ARIS_GEMINI_PLAN_20261013.md).
The complete local
[proof-writer skill](../../../.agents/skills/proof-writer/SKILL.md) and
[experiment-bridge skill](../../../.agents/skills/experiment-bridge/SKILL.md)
were read before implementation. The experiment bridge was adapted to
an exact local finite graph calculation: fixed input/domain, one budgeted
episode, prefix sanity/profile, complete run, saved full candidate, and
a separate BFS handoff. GPU training, paper scoring, automatic ablation,
hashes and additional artifact manifests were inapplicable or disabled by
the current project instructions. Local source/route checks are not
substitutes for external review.

The parent agent owns the same-mechanism Gemini direction/result review
and overall project synchronization. At initial report creation,
**Gemini review of this result is pending**. The separate agent
`cyclic_lift58_60` completed independent all-source BFS, reading only the
final edge table and using adjacency sets plus a deque. Its
[standalone source](../../../computations/dd82/construction/false_twins58_f9_independent_bfs.py)
does not import this evaluator's matrix or distance routines. The
[independent result](../../../computations/dd82/construction/false_twins58_f9_coverage_run/independent_bfs.json)
confirms simplicity, 58 vertices, 232 edges, all degrees eight, connectivity,
diameter three and exactly 105 bad pairs. The unordered distance histogram
is 232 at distance one, 1,316 at distance two and 105 at distance three.
All 105 independently found bad pairs agree with the predicted list.
This check used 0.002198166 CPU seconds and 0.002198257 wall seconds,
separate from the experiment resources above. The original run JSON
intentionally retains its handoff-time BFS status as pending; this
independent artifact and this report record the subsequent completed check.
