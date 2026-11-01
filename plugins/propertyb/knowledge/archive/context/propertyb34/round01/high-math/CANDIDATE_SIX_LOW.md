# Exactly six degree-six vertices at 24 vertices

## Claim

Let $H$ be a simple five-uniform hypergraph on $24$ vertices, with exactly $34$
edges, covering every vertex pair. If exactly six vertices have degree six,
then $H$ has Property B.

## Status and assumptions

**PROVABLE AS STATED**, as a complete paper candidate with exact finite local
certificates. No new Lean theorem is asserted. The existing probability bound,
the earlier complete six-unit trace catalogue, and the finite shared-vector dual
inequality are used with their actual-input hypotheses below.

Write $L$ for the six low vertices, $d(x)$ for degree, and $\lambda(x,y)$ for
codegree. The failure-probability estimate is the same locked random-permutation
estimate used previously. Its three contributions at a position are $A,B,C$;
actual impossible ordered edge pairs are removed from $C$ before taking the
minimum.

## Strategy and dependency map

1. Nonunit pairs in $L$ are already covered by the six-low matching catalogue.
2. For unit $L$, five of its nine local trace types are already strict.
3. A degree count supplies at least four degree-seven vertices unit with $L$.
4. Adding one such high lock leaves only five local orbits; adding any second
   leaves only four orbits, all with the two highs unit.
5. None of those pair restrictions can hold simultaneously for three highs.

## Proof

### 1. Existing six-low cases

For every degree-six vertex $x$,
$$\sum_{y\ne x}(\lambda(x,y)-1)=4\cdot6-23=1.$$
It has exactly one exceptional partner, of codegree two, and exactly one
unordered bad pair of incident edges. If two vertices of $L$ are exceptional
partners, the previously verified $181$-orbit matching catalogue applies.
Hence assume all pairs in $L$ are unit.

Their multi-point traces partition the pairs of $L$. The earlier complete
$352$-label / nine-orbit catalogue leaves four cases after applying the existing
strict certificates:

| Six-low catalogue ID | Large traces |
|---:|---|
| 1 | one triple |
| 3 | two triples intersecting in one point |
| 5 | two disjoint triples |
| 8 | a Pasch family of four triples |

Every remaining pair is itself a trace. A low vertex in $t_i$ listed triples has
singleton multiplicity $1+t_i$.

### 2. At least four usable seven-degree vertices

Let $t$ count degree-seven vertices. All other $18-t$ non-low vertices have
degree at least eight, so
$$170\ge6\cdot6+7t+8(18-t)=180-t,$$
and $t\ge10$. Delete the at most six exceptional partners of the low vertices.
At least four seven-degree vertices remain. Call their set $Q$. Every vertex in
$Q$ has unit codegree with all of $L$.

Each $x\in Q$ has total codegree excess $4\cdot7-23=5$. The proof will show that
every pair of vertices in $Q$ must also be unit in a counterexample, and then use
three distinct vertices of $Q$.

### 3. Complete addition of a first high lock

Fix $x\in Q$. Its incident edges that meet $L$ have old $L$-traces partitioning
$L$, because $\lambda(x,i)=1$ for every $i\in L$. Every partition block must
be a positive old trace of size at most four. Conversely this describes an
exhaustive local relaxation: promote each chosen trace $T$ to $T\cup\{x\}$,
decrease its old multiplicity by one, give singleton $\{x\}$ multiplicity
$7-$number of partition blocks, and subtract this from the old empty count.
Retain exactly the nonnegative inputs.

`SIX_LOW_EXTENSION.json` records the resulting $50,32,37,12$ labelled inputs for
the four rows, respectively: $131$ total. Exact position certificates and the
shared actual bad-vector certificates leave these five orbits:

| Six-low type | Remaining behavior of $x$ |
|---|---|
| one triple | A: $x$ occurs only on six singleton low traces |
| one triple | B: $x$ promotes one pair among the three low vertices outside the triple; all other low incidences use singleton traces |
| two intersecting triples | A only |
| two disjoint triples | A only |
| Pasch | A only |

The $22$ initially unresolved colored orbits, their exact duals, and the five
non-strict residues are in `SIX_EXTENSION_JOINT.json`. All $17$ strict dual
certificates independently replay in `SIX_EXTENSION_JOINT_INDEPENDENT.json`.

For clarity, a type A high lies in one distinct edge for each of the six
singleton low traces, plus one edge avoiding $L$. A type B high lies in the
promoted pair edge, four singleton low edges, and two edges avoiding $L$.

### 4. Complete addition of a second high lock

Take distinct $x,y\in Q$ and put $c=\lambda(x,y)$. The second-high generator
partitions the six low labels among positive seven-lock traces, allowing the
old high $x$ to occur in several of them. If it occurs $b$ times, choose a
further $c-b$ old singleton-$x$ traces for promotion. Add singleton $y$ edges to
bring its degree to seven. Again discard exactly the negative-count cases.
This covers every actual input: the unit low incidences determine the partition,
while the specified codegree determines the additional singleton-$x$ promotions.

If the separate $L\cup\{y\}$ projection is already good in Step 3, stop there.
For the remaining inputs:

- Every case with $c=2,3,4$ has a strict exact position certificate.
- For $c\ge5$, the two degree-seven locks alone suffice. Their counts are
  $\mu_\varnothing=20+c$, $\mu_x=\mu_y=7-c$, $\mu_{xy}=c$. The bounds for
  $c=5,6,7$ are respectively $47167/49742$, $88271/99484$, and
  $20574/24871$, all strict. (The excess identity already excludes $c=7$ in the
  present actual setting; retaining it in this small table is harmless.)

Thus in a counterexample every pair in $Q$ is unit. For $c=1$, the complete
second-high table leaves $12$ labelled inputs, exactly four orbits:

| Low type | Necessary remaining behavior of every high pair |
|---|---|
| one triple | one high is A and the other B |
| two intersecting triples | both are A |
| two disjoint triples | both are A; their common edge is either a singleton-low edge or an edge avoiding $L$ |
| Pasch | no residue |

The second-high files are `SIX_LOW_TWO_HIGH.json` ($c=1,2$) and
`SIX_LOW_HIGHER_CODEGREE.json` ($c=3,4$). Each stored position certificate was
replayed with the original Fraction formulas and independent labelled injection
counts. `STRONG_SEVEN_PAIR.json` stores the direct high-codegree certificates.
`SIX_LOW_THREE_HIGH.json` records the four residual orbits explicitly; it also
independently enumerates $32,52,43,45$ third-high extensions, all excluded by
another two-high projection. The next step supplies a shorter analytic argument.

### 5. Three highs contradict the residual restrictions

Choose distinct $x,y,z\in Q$, which are pairwise unit by Step 4.

**One low triple.** Every pair of highs must contain exactly one A and one B.
Among three highs, two have the same letter, contradicting this restriction.

**Two intersecting low triples.** There is a low vertex $a$ outside the two
triples, with exactly one singleton-low edge. All three type A highs lie in
that edge. A low vertex $b$ belonging to exactly one triple has only two
singleton-low edges. The three highs must use three different such edges:
otherwise two highs share both the edge at $a$ and an edge at $b$, violating
unit codegree. Three distinct required edges cannot fit into two.

**Two disjoint low triples.** Every low vertex has exactly two singleton-low
edges. At each of the six lows, three type A highs choose among two edges, so
at least one high pair shares an edge there. This gives at least six incidences
of a high pair sharing a singleton-low edge. Each of the three high pairs can
contribute at most one incidence, since its codegree is one, giving at most
three. The inequalities $6\le3$ contradict each other. Edges assigned to
different singleton-low traces are distinct, so no incidence is counted twice
as the same actual edge.

All residual cases are impossible. Therefore $H$ has Property B. $\square$

## Exact dual evidence and remaining implementation

The shared-vector certificates fix the actual bad-pair count vector before
varying layouts. Low vertices have a unique actual bad pair: a positive avoided
quota forces that pair to belong to the corresponding avoided slot set. This
justifies the low-slot restrictions in the certificate inventory. For unit
locks, two actual bad edges cannot share any other selected lock. High-center
bad counts use capacity bounds and all stated avoided quotas.

The LP proposes a dual; saved nonnegative rational layout weights, clamped
coefficients, avoided-quota multipliers, and explicit capacity penalties verify
the inequality exactly. `verify_joint.py` independently reconstructs the slot
domain, quotas, every A/B/C row, both ordered weights, and the dual bound.

The proof is now a candidate for cross-family review and Lean implementation.
The root agent owns those steps. Combined with `CANDIDATE_SEVEN_LOW.md`, the new
paper range covers all 24-vertex inputs with at least six degree-six vertices;
the one-through-five-low cases remain open.
