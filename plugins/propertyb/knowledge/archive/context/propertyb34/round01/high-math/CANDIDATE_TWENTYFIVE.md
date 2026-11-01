# The complete 25-vertex branch for T34

## Claim

Every simple five-uniform hypergraph on $25$ vertices with exactly $34$ edges
and covering every vertex pair has Property B.

## Status

**PROVABLE AS STATED**, as a complete paper candidate. All local domains below
have been fully generated, every retained bound is an exact rational strictly
below one, and every witness has an independent labelled-injection A/B/C
replay. Cross-family review and Lean implementation remain separate root-owned
obligations; this document does not assert a completed T34 theorem.

## Notation, assumptions, and strategy

Write $d(x)$ for degree, $\lambda(x,y)$ for codegree, and $r$ for the number of
degree-six vertices. All intermediate hypotheses in this document describe the
existing 25-vertex reduced branch; they are not new assumptions in the original
T34 target. The edge count gives $\sum_xd(x)=170$, and pair covering gives
$$4d(x)\ge24,\qquad
 \sum_{y\ne x}(\lambda(x,y)-1)=4d(x)-24.$$
Thus $d(x)\ge6$, and every degree-six vertex is unit with every other vertex.

The proof uses nine unit locks with degrees $6^q7^{9-q}$. Only $q=5,8,9$ is
needed. Complete local clique decomposition gives the actual trace counts;
strict locked-permutation bounds handle all but five profiles. In those five,
an actual tenth lock has a complete strict extension catalogue.

## Dependency map

1. Degree/excess counting and greedy independent-set selection give the actual
   nine locks.
2. The complete local clique-decomposition catalogue and degree equations give
   one of the stated profiles.
3. Exact direct certificates, or an actual tenth-lock extension, give a failure
   bound below one.
4. The existing probability lemmas return a proper two-coloring of the original
   $H$.

## 1. Universal selection of the nine locks

Since every non-low vertex has degree at least seven,
$$170\ge6r+7(25-r)=175-r,$$
so $r\ge5$. Let $t$ count degree-seven vertices. Then
$$170\ge6r+7t+8(25-r-t)=200-2r-t,$$
and $t\ge30-2r$.

On the degree-seven vertices, join two vertices when their codegree exceeds
one. Every vertex in this graph has degree at most four, since its total
codegree excess is $4\cdot7-24=4$. A greedy independent-set algorithm selects
one vertex and removes it and at most four neighbors at each step; hence it
finds at least $\lceil t/5\rceil$ independent vertices.

- If $r=5,6,7$, then $t\ge20,18,16$ respectively, so choose four pairwise-unit
  degree-seven vertices and any five low vertices. These nine locks have
  $q=5$. Their low-high pairs are automatically unit.
- If $r=8$, choose all eight low vertices and one of the at least fourteen
  degree-seven vertices. This gives $q=8$.
- If $r\ge9$, choose nine low vertices, giving $q=9$.

This covers every possible degree sequence. There is no need to classify the
much larger $q=6,7$ colored domains.

## 2. Complete nine-lock local classification

For unit locks $S$, every multi-point edge trace occurs once and the multi-point
traces partition the pairs of $S$ into cliques of sizes two through five. If
$\mathcal B$ is this decomposition and lock $i$ has specified degree $d_i$,
then
$$\mu_{\{i\}}=d_i-|\{B\in\mathcal B:i\in B\}|,\qquad
 \mu_\varnothing=34-|\mathcal B|-\sum_i\mu_{\{i\}}.$$
Negative counts are impossible. These equations exactly recover the actual
singleton and empty counts; no unproved geometric realizability condition is
introduced.

The exhaustive vertex-extension construction and its proof are given in
`CANDIDATE_25_MANY_LOW.md`, §1. Starting with the established nine six-point
types, it produces $22$, $65$, and $374$ uncolored types on seven, eight, and
nine points. To extend a decomposition by a new point, promote any family of
pairwise-disjoint old blocks of size at most four; every unused old vertex forms
its pair with the new point. Restricting an actual decomposition proves that
every actual type arises this way.

For each degree pattern, all assignments of the low labels are generated,
negative counts are discarded, and only actual bijective relabelings identify
profiles. The complete domains are:

| $q$ | Feasible color assignments to the 374 uncolored representatives | Colored profile orbits |
|---:|---:|---:|
| 5 | 23,507 | 11,692 |
| 8 | 1,397 | 840 |
| 9 | 147 | 147 |

Sources are `UNIT_CATALOGUE_9.json` and `V25_NINE_Q{5,8,9}_CATALOGUE.json`.
The scripts use incidence invariants only to narrow which permutations must be
tested; each chosen representative is still an actual renamed input. A second
first-unused-vertex extension recursion replays the eight/nine-point catalogues,
and the older first-uncovered-pair recursion independently checks all $8382$
seven-point labelled inputs. The final actual-profile audit is
`FULL25_COVERAGE_AUDIT.json`.

## 3. Direct strict bounds

The existing conditional-permutation formulas are evaluated with the actual
trace counts. Bare layouts require no bad-pair deduction. When needed, a
center of degree $d$ uses the established total link quota
$$q_{\mathrm{total}}=\left\lceil\frac{4d-24}{3}\right\rceil$$
and the nested pure-trace quota on the sixteen unlocked vertices. The pure quota
is deducted first, then only the remaining total quota is assigned to residual
capacities. This avoids counting one bad pair twice. Actual ordered weights are
summed in both directions before an unordered bad pair is deducted.

| $q$ | Profiles | Direct strict profiles | Maximum of direct strict bounds | Residues |
|---:|---:|---:|---|---:|
| 5 | 11,692 | 11,692 | $12869/12870$ | 0 |
| 8 | 840 | 838 | $2285/2288$ | 2 |
| 9 | 147 | 144 | $1429/1430$ | 3 |

For $q=5$, five fixed bare layouts handle $11,334$ profiles. Only the remaining
$358$ require the exact position search. The full checked run took about $170$
seconds. All $11,692$ actual certificates, including every A/B/C row, were
independently replayed. The $q=8$ and $q=9$ complete runs took about $260$ and
$41$ seconds respectively. These are local formula evaluations, not enumeration
of whole 25-vertex hypergraphs.

The search uses states `(position, placed-lock subset)` to examine all lock
orders and positions, with integer coefficients scaled by $(25-|S|)!$. Search
optimality is not needed in the proof: the saved concrete positions and exact
strict bounds suffice. Files `V25_NINE_Q{5,8,9}_BOUNDS.json` preserve those
witnesses and the exact residues.

## 4. Actual tenth lock when $r=8$

The two $q=8$ residues have catalogue IDs $0,10$. Let $h$ be the old degree-seven
lock. There are at least fourteen degree-seven vertices; at most four are
nonunit with $h$. Excluding $h$ and these neighbors leaves at least nine choices
for a new degree-seven lock $x$. It is unit with $h$ and automatically unit with
the eight old lows.

The old traces of $x$-incident edges meeting $S$ partition the nine old locks.
Each part must be a positive old trace of size at most four. Promote those
traces; if there are $a$ parts, add singleton $x$ multiplicity $7-a$ and decrease
the old empty multiplicity by the same amount. This recovers every actual
extension and discards only negative-count inputs.

The two complete extension domains have $24$ and $101$ labelled inputs, or $4$
and $16$ orbits fixing the two high roles. Every orbit is strict; their maxima
are $4618/5005$ and $925/1001$. Counts, layouts and independent A/B/C replays are
stored in `V25_Q8_TENTH_BOUNDS.json`.

## 5. Actual tenth lock when $r\ge9$

For $r\ge10$, choose another low vertex, of degree six. For $r=9$, the inequality
$t\ge30-2r$ gives at least twelve degree-seven vertices, so choose any of them.
In both cases the new vertex is unit with the nine old lows.

The same promotion construction, with new degree $d=6$ or $7$, covers all actual
extensions of the three $q=9$ residues with IDs $0,3,6$. Their labelled counts
for $d=6,7$ are respectively $(16,28)$, $(102,138)$, and $(14,14)$; after fixing
the new role there are $(2,3)$, $(7,9)$, and $(2,2)$ orbits. All $25$ orbits have
strict exact bounds. See `V25_TENTH_BOUNDS.json` and the more detailed proof in
`CANDIDATE_25_MANY_LOW.md`.

## 6. Conclusion

Every actual $H$ supplies one of the three selected degree patterns. Every
resulting actual trace input belongs to its complete catalogue. A direct strict
bound exists, or an actual tenth-lock extension has one. Thus the conditional
random-permutation failure probability is below one in a finite nonempty
sample space. Some permutation succeeds, giving a proper two-coloring of $H$.
$\square$

## Remaining verification work

The mathematical target has not been weakened. New Lean work must connect the
actual selection, vertex-extension coverage, relabelings, precise trace counts,
bad-pair quotas and strict tables to the original coloring conclusion. The
largest local table is $11,692$ profiles; a smaller symbolic certificate or
shared computation may reduce kernel cost without changing coverage. The
independent arithmetic and cross-model opinions do not replace those formal
connections. The original T34 problem still has other vertex-count branches.
