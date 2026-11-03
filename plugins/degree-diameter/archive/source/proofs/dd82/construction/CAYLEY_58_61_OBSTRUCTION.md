# Cayley graph obstruction at orders 58 through 61

Date: 2026-10-11.

The existing cyclic-action obstructions and the saved exhaustive calculation on $A_5$ together exclude every simple undirected Cayley graph of maximum degree at most eight and diameter at most two on $58$, $59$, $60$, or $61$ vertices. Moreover, there is no vertex-transitive graph with these degree and diameter bounds on $58$, $59$, or $61$ vertices.

The order-$60$ conclusion is **computer-assisted**: it uses the existing small quotient-capacity screen for four cyclic orbits and the existing exhaustive $A_5$ calculation. This note supplies the group-theoretic reduction and inspects those saved dependencies; it does not rerun either enumeration. There is no Lean certificate here. No exclusion of arbitrary vertex-transitive graphs on $60$ vertices, or arbitrary graphs of any of these four orders, is asserted.

## Regularity and the action supplied by a Cayley graph

In a graph of maximum degree at most eight, the radius-two ball at a vertex of degree $d$ has at most

$$1+d+7d=1+8d$$

vertices. Thus a graph of diameter at most two and order greater than $57$ must be eight-regular.

Use the convention that $\operatorname{Cay}(G,S)$ has edges $g\sim gs$, where $e\notin S=S^{-1}$. Hence $|S|=8$ in every case at issue. Left multiplication by any element of $G$ preserves every edge. If $h\in G$ has order $m$, then $\langle h\rangle$ acts freely: $h^k g=g$ implies $h^k=e$. Its orbits therefore all have length $m$. Normality of $\langle h\rangle$ is not needed.

## Order 58

Cauchy's theorem gives an element of order $29$ in every group of order $58$. Its left multiplication action has exactly two orbits of length $29$. The complete analytic obstruction in [Cyclic lift constructions, two-orbit proof](CYCLIC_LIFT_CONSTRUCTION.md) excludes precisely this action.

For clarity, its final step does not rely on a parity contradiction. The only surviving degree pattern has two internal neighbors and six cross neighbors. Exact cross coverage forces the six-element cross set $C$ to be inverse-closed after translation. Then $|C-C|\leq19$, and the remaining internal offsets contribute at most four new residues. At most $23$ of the required $29$ same-orbit offsets are covered.

## Orders 59 and 61

A group of prime order $p$ is cyclic. Since $p$ is odd and $S$ is inverse-closed of size eight, write

$$S=\{\pm a_1,\pm a_2,\pm a_3,\pm a_4\}\subseteq\mathbb Z_p.$$

Every offset reached in at most two steps lies among

$$0,\qquad \pm a_i,\qquad \pm2a_i,\qquad \pm a_i\pm a_j\quad(i<j).$$

Consequently the radius-two ball has size at most

$$1+8+8+4\binom42=41.$$

This is less than both $59$ and $61$.

## Order 60: reduce all groups to two cases

Every group of order less than $60$ is solvable, and every simple group of order $60$ is isomorphic to $A_5$. If a group $G$ of order $60$ is not simple, choose $1\ne N\lhd G$, $N\ne G$. Both $N$ and $G/N$ have order less than $60$, so both are solvable. A solvable extension is solvable. Thus every group of order $60$ is either solvable or isomorphic to $A_5$. These standard facts and their elementary proofs are in [J. S. Milne, *Group Theory*, §5.18–5.19, pp. 84–85, and §6, Proposition 6.6](https://www.jmilne.org/math/CourseNotes/GT.pdf). This uses no classification of general finite simple groups.

### Solvable case: a cyclic subgroup of order 15

Hall's theorem supplies a subgroup $H$ of order $15$, since $15$ and $4$ are coprime. The existence statement is [Hall's theorem, Theorem 23.8(1), p. 125, UCLA-hosted algebra text](https://www.math.ucla.edu/~rse/algebra_book.pdf); see also [D. A. Craven, *Finite Group Theory*, §2.2, Proposition 2.9](https://web.mat.bham.ac.uk/D.A.Craven/docs/lectures/finitegroups2012.pdf).

In a group of order $15$, Sylow's theorem gives

$$n_5\mid3,\quad n_5\equiv1\pmod5;\qquad n_3\mid5,\quad n_3\equiv1\pmod3.$$

Therefore both Sylow subgroups are normal. Their intersection is trivial, so they commute and $H\cong C_3\times C_5\cong C_{15}$. Left multiplication by a generator gives four free cyclic orbits of length $15$.

All such four-orbit targets have already been excluded. The complete [quotient screen](../../../computations/dd82/construction/cyclic_lift15_quotient_screen.py), with its [saved result](../../../computations/dd82/construction/cyclic_lift15_quotient_screen.json), considers every nonnegative integer cross-size matrix after sorting the four even internal degrees. It leaves seven labeled matrices among $395$ degree-feasible matrices, comprising these three types up to orbit relabeling:

| Internal degrees | Cross-size pattern | Closing argument |
| --- | --- | --- |
| $(0,0,0,0)$ | Each orbit has cross sizes $3,3,2$; the size-two pairs form a matching | [332 obstruction](CYCLIC_LIFT_FOUR_ORBIT_332.md) |
| $(0,0,2,2)$ | $c_{01}=2$, $c_{23}=0$, and the other four sizes equal three | [0022 obstruction and full screen derivation](CYCLIC_LIFT15_0022_OBSTRUCTION.md) |
| $(2,2,2,2)$ | Two opposite pairs have size zero; the other four sizes equal three | [2222 obstruction](CYCLIC_LIFT_FOUR_ORBIT_2222.md) |

Each closing argument is analytic. The finite screen is essential to the assertion that these three types exhaust the four-orbit family. Together they exclude the solvable case.

### Nonsolvable case: the recorded exhaustive calculation on $A_5$

The remaining group is $A_5$. Its $59$ nonidentity elements split under inversion into $15$ involutions and $22$ two-element inverse pairs. Every inverse-closed set of size eight is obtained uniquely by choosing $j$ inverse pairs and $8-2j$ involutions, for some $0\leq j\leq4$. Hence the complete input count is

$$\sum_{j=0}^{4}\binom{22}{j}\binom{15}{8-2j}=600875.$$

The existing [C++ program](../../../computations/dd82/construction/a5_cayley60.cpp) constructs all even permutations on five letters, composes them exactly, groups the nonidentity elements into their inverse orbits, and traverses every selection of inverse orbits of total size eight. For each resulting set $S$ it counts the bitset

$$\{e\}\cup S\cup\{st:s,t\in S\}.$$

This is exactly the radius-two ball at the identity. The enumeration includes sets that do not generate $A_5$; including them preserves completeness. Cayley transitivity makes checking the identity sufficient.

The [saved output](../../../computations/dd82/construction/a5_cayley60.json) records all $600875$ inputs and a maximum radius-two ball size of **53**, so none has diameter at most two. The histogram counts sum to $600875$, agreeing with the independent binomial count above. Source inspection confirms that the increasing-index recursion selects each inverse-closed set once and that the ball computation uses the group multiplication table. No new graph enumeration was performed for this note.

The saved best graph also has an [independent BFS verification](../../../computations/dd82/construction/a5_cayley60_best.verification.json): $60$ vertices, $240$ edges, degree eight throughout, and $210$ unordered pairs at distance three. This agrees with seven missing vertices per radius-two ball, since $60\cdot7/2=210$. That BFS checks the saved best graph only; it is not an independent repetition or certificate of the entire exhaustive enumeration. The full $A_5$ exclusion retains the evidence level of the saved exact C++ computation.

This closes the order-$60$ Cayley case.

## Vertex-transitive corollary at 58, 59, and 61

If a finite graph is vertex-transitive on $n$ vertices, orbit-stabilizer gives $n\mid|\operatorname{Aut}(\Gamma)|$.

For $n=58$, Cauchy's theorem therefore supplies an automorphism of order $29$. Its permutation action has either one or two $29$-cycles. In the one-cycle case, every other vertex is fixed. An edge from a fixed vertex to the cycle would give that vertex all $29$ cycle vertices as neighbors, violating the degree bound. Thus the cycle and the fixed set are disconnected, contradicting diameter at most two. The two-cycle case is the excluded free cyclic action above.

For $n=p\in\{59,61\}$, Cauchy's theorem supplies an automorphism of order $p$. On $p$ vertices it is a single $p$-cycle, hence generates a regular cyclic group of graph automorphisms. Labeling vertices along this cycle identifies the graph with a Cayley graph on $\mathbb Z_p$. The radius-two bound $41$ then excludes it.

This argument gives no regular subgroup, cyclic element of order $15$, or four-orbit action for an arbitrary vertex-transitive graph of order $60$. The order-$60$ statement remains restricted to Cayley graphs.

## Evidence boundary

The group-theoretic reduction, the prime-order bound, the order-$58$ argument, and the vertex-transitive corollaries are mathematical deductions. The order-$60$ conclusion additionally depends on the existing $395$-quotient screen and $600875$-set $A_5$ calculation. Their source and saved results are linked above; neither was rerun or upgraded to formal certification here. This note introduces no new construction search.

## External construction discussion C5

The final bounded C5 discussion read this proof and accepted its substantive implications. Raw response: `reviews/dd82/20261011_C5_hs59_cayley.json`; requested and CLI-selected model gemini-3.8-flash-high/high, using the existing Antigravity thread. Root also checked the argument and exact evidence boundaries. This is provisional corroboration, not Lean or independent backend attestation.

The response's concluding description of all results as pure mathematics is not adopted: the order-60 Cayley exclusion remains computer-assisted, depending on the saved quotient screen and A5 enumeration. The A5 source was inspected locally; C5 listed the proof notes and A5 result JSON as its actual reads.
