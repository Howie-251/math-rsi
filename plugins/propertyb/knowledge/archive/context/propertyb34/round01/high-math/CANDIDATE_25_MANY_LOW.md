# At least nine degree-six vertices suffice at 25 vertices

## Claim and status

Let $H$ be a simple five-uniform hypergraph on $25$ vertices, with exactly $34$
edges, covering every vertex pair. If at least nine vertices have degree six,
then $H$ has Property B.

**PROVABLE AS STATED:** complete paper candidate with actual selection and finite
local coverage, exact probability certificates, and independent injection
replay. Lean implementation and root-managed cross-family review remain.

## Assumptions, notation, and strategy

Write $r$ for the number of degree-six vertices. For such a vertex $x$,
$$\sum_{y\ne x}(\lambda(x,y)-1)=4\cdot6-24=0.$$
Every pair involving $x$ therefore has codegree one. Choose nine low vertices
$S$. Their multi-point edge traces form a partition of all pairs of $S$ into
cliques of sizes two through five. Each such trace occurs once. Singleton and
empty trace counts are determined by the nine degrees and the total $34$ edges.

The proof classifies these small local clique decompositions, uses direct strict
bounds for $144$ feasible types, and adds an actual tenth lock for three residues.
This is not enumeration of whole hypergraphs or evidence from random examples.

## 1. Complete local catalogue by vertex extension

Start with the already established nine isomorphism types of six-point clique
decompositions. To add a new point to a decomposition on $n$ points, choose a
set of pairwise vertex-disjoint existing blocks of sizes at most four and
adjoin the new point to each chosen block. For every old point not in a chosen
block, add its pair with the new point. Retain all unchosen old blocks.

This construction is exhaustive. In any decomposition on $n+1$ points, deleting
the new point leaves a decomposition on the old $n$ points after singleton
traces are ignored and missing pairs are restored. Blocks containing the new
point have pairwise-disjoint old traces, because each pair involving the new
point occurs exactly once. Old traces of size at least two are blocks of the
restricted decomposition, while singleton old traces produce the added pairs.
No original block has size above five, so only old blocks of size at most four
can be promoted.

`unit_catalogue.py` implements this exact extension. Canonicalization first
partitions vertices by isomorphism-invariant incidence signatures, then tests
every bijection within those classes; it never identifies objects without an
actual bijective relabeling. The complete orbit counts on seven, eight, and nine
points are $22,65,374$. Their extension counts are $272,1476,10271$.

As a separate check, the old first-uncovered-pair recursion produces all $8382$
labelled seven-point decompositions and exactly the same $22$ orbits:
`UNIT_CATALOGUE_7_INDEPENDENT.json`. Higher-level completeness rests on the
extension argument, not on that check alone.

## 2. Actual degree and edge-count binding

For each nine-point decomposition $\mathcal B$, let $b_i$ be the number of its
blocks containing $i$. The actual singleton and empty counts must be
$$\mu_{\{i\}}=6-b_i,\qquad
  \mu_\varnothing=34-|\mathcal B|-\sum_i\mu_{\{i\}}.$$
Negative counts are impossible. Applying exactly these inequalities to the
$374$-orbit catalogue leaves $147$ profiles, recorded in
`V25_NINE_Q9_CATALOGUE.json`. Every actual $H,S$ has one of these profiles after
a bijective relabeling; no extension-realizability assumption is imposed.

The exact all-order position search gives strict bounds for $144$ profiles.
Every retained input, position, and row is independently replayed with labelled
stub injections in `V25_NINE_Q9_BOUNDS.json`. The other three profiles have
$12,9,6$ triples respectively, grouped into $4,3,2$ parallel classes, with every
point lying in $4,3,2$ triples respectively. Their catalogue IDs are $0,3,6$;
the stored raw bounds are $6476/6435$, $1$, and $11497/11440$.

## 3. An actual tenth lock for every residual case

If $r\ge10$, choose another degree-six vertex $x$. It is unit with all nine old
locks. If $r=9$, let $t$ count degree-seven vertices. The degree sum gives
$$170\ge6\cdot9+7t+8(16-t)=182-t,$$
so $t\ge12$. Choose any such degree-seven vertex; it is again unit with every
old lock. Thus the new degree is $d=6$ or $d=7$ and every new-old codegree is one.

The old traces of edges containing $x$ and meeting $S$ partition $S$ into
positive old traces of size at most four. Promote those traces, decreasing
their old multiplicities by one. If there are $a$ chosen parts, the new singleton
count is $d-a$ and the old empty count decreases by $d-a$. These equations
recover every actual extension, and nonnegative counts are the only filter.

The complete domains and exact strict witnesses are in `V25_TENTH_BOUNDS.json`:

| Nine-lock ID | New degree | Labelled extensions | Colored orbits |
|---:|---:|---:|---:|
| 0 | 6 | 16 | 2 |
| 0 | 7 | 28 | 3 |
| 3 | 6 | 102 | 7 |
| 3 | 7 | 138 | 9 |
| 6 | 6 | 14 | 2 |
| 6 | 7 | 14 | 2 |

Every one of the $25$ colored orbits has a strict exact position certificate.
Canonicalization allows arbitrary old-lock relabelings while fixing the new
lock, so it cannot merge different new-degree roles. Each witness was replayed
through the original Fraction formula and independent $34$-stub injection rows.

## 4. Return to the original coloring

For every actual nine-lock input, either a direct bound is strictly below one
or its actual tenth-lock extension has one of the strict bounds above. The
conditional random-permutation space is finite and nonempty. A failure bound
strictly below one supplies a successful permutation and therefore a proper
two-coloring of $H$. This proves the claim. $\square$

## Implementation obligations

The existing probability lemmas supply the actual-event domination. The new
Lean work must implement the vertex-extension coverage, transport of real trace
counts, the three residual cases, tenth-lock selection and all exact witnesses.
The local numerical checks and model opinions are not a substitute for those
connections. The remaining 25-point cases have exactly five through eight low
vertices and are not covered by this claim.
