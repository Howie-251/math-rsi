# Fixed-root joint obstruction: exterior matchings cannot all exchange the two layers

## Claim

In the fixed-$A$, root-normalized six-Petersen model of
[PETERSEN_FIXED_ROOT_CONSTRAINTS.md](PETERSEN_FIXED_ROOT_CONSTRAINTS.md), a
valid diameter-two graph must have at least one exterior matching edge
whose endpoints lie in the same coordinate layer. Consequently it has at
least two such edges, and their total number is even and at most $24$.

This is a **joint** obstruction. It excludes all choices of the ten exterior
matchings that exchange the two layers, including choices beyond the old
three-shift or $C_5$-symmetric families. The local matching catalog contains
$244$ layer-exchanging permutations, but no simultaneous choice of ten of
them can solve the fixed-root problem.

## Status and assumptions

**PROVABLE AS STATED.** The proof is elementary and does not depend on a
new search or SAT result.

The root fiber has internal graph $P$. Every exterior fiber has the same
internal graph $Q$, on $(e,x)$ with $e\in\{0,1\}$ and $x\in\mathbb F_5$:

- layer $0$ has cycle steps $\pm2$;
- layer $1$ has cycle steps $\pm1$;
- its spokes are $(0,x)\sim(1,x+3)$.

All five root matchings are identity. The missing root labels form the
cubic bipartite graph $T$, whose neighbors of $(0,x)$ have coordinates
$(1,x+t)$ for $t\in\{1,2,4\}$. Assume all ten exterior matchings exchange
layers, and derive a contradiction.

## Proof strategy and dependency map

1. Exactly five cross-layer path slots force each five-point half-matching
   to be a translation or reflection.
2. Root coverage bounds reflections to at most one in each row and column
   of a five-by-five array of affine maps.
3. Same-layer coverage then permits at most one reflection globally.
4. A row-sum and equal-entry count excludes zero reflections.
5. Row and column coverage together exclude the single-reflection case.

## 1. Half-matchings are affine

For distinct exterior fibers $i,j$, write

$$f_{ij}:\mathbb F_5\longrightarrow\mathbb F_5$$

for the bijection taking $(0,x)$ in fiber $i$ to $(1,f_{ij}(x))$ in fiber
$j$. The same undirected matching takes $(1,x)$ in fiber $i$ to
$(0,f_{ji}^{-1}(x))$ in fiber $j$. Thus the twenty directed maps $f_{ij}$
encode all ten matchings without imposing any extra symmetry.

For a source $(0,x)$ in fiber $i$ and layer-$1$ targets in fiber $j$, exactly
five direct-or-two-step routes are available:

$$f_{ij}(x),\quad f_{ij}(x)+1,\quad f_{ij}(x)-1,
\quad f_{ij}(x+2),\quad f_{ij}(x-2).$$

The root route and the three other exterior intermediate-fiber routes end
in layer $0$, as do the routes involving an internal spoke. Therefore the
five displayed values must be all of $\mathbb F_5$. It follows that

$$\{f_{ij}(x+2),f_{ij}(x-2)\}
=\{f_{ij}(x)+2,f_{ij}(x)-2\}.$$

Hence $f_{ij}$ is an automorphism of the five-cycle with steps $\pm2$.
Following the cycle from $0,2,4,1,3$ proves directly that

$$f_{ij}(x)=s_{ij}x+a_{ij},\qquad s_{ij}\in\{1,-1\}.$$

Call sign $1$ a translation and sign $-1$ a reflection.

## 2. Root coverage bounds reflections in each row and column

For a fixed exterior fiber $i$, the four maps $f_{ij}$ must collectively
cover all three mandatory values $x+1,x+2,x+4$, for every source $x$.
After subtracting $x$, a translation supplies its fixed offset $a_{ij}$,
whereas a reflection supplies $a_{ij}-2x$.

If one of the three mandatory offsets were absent among the translations,
each reflection could supply it for only one of the five possible $x$.
There are only four maps, so reflections cannot supply it for all five
sources. Thus all three offsets $1,2,4$ occur as translations in every row.
Each row therefore has at most one reflection. If it has one, its other
three maps are precisely translations with offsets $1,2,4$.

Apply the same argument to layer-$1$ sources, using the inverse maps
$f_{ji}^{-1}$ and the mandatory offsets $-1,-2,-4$. It gives the same
statement for every column: at most one reflection, and if one occurs,
the other three off-diagonal maps have translation offsets $1,2,4$.

## 3. Same-layer coverage permits at most one reflection in total

Define diagonal maps $f_{ii}(x)=x+3$. For layer-$0$ sources in fiber $i$
and layer-$0$ targets in a different fiber $j$, the six path slots are

$$\{x\}\ \cup\ \{f_{jk}^{-1}(f_{ik}(x)):k=0,1,2,3,4\}.$$

The term $x$ is the root route. The terms $k=i,j$ are the two spoke routes;
the remaining three use the other exterior fibers. Coverage requires this
set to equal $\mathbb F_5$ for every $x$.

We use the following elementary observation. Suppose five affine maps
$g_k(x)=\epsilon_kx+b_k$, together with $x$, cover $\mathbb F_5$ for every
$x$. If there are $r<5$ reflections among the five maps, every nonzero
field element must already occur among the offsets of the translations:
a missing nonzero value could be supplied by at most $r$ of the five
source values $x$. Therefore $5-r\ge4$, so $r\le1$. When $r=1$, the other
four translation offsets are exactly $1,2,3,4$.

Two different rows of $(f_{ij})$ have reflections in different columns,
because each column has at most one reflection. In their five quotient
maps $f_{jk}^{-1}f_{ik}$, the number of reflections is consequently the
sum of their row reflection counts. If both rows contained a reflection,
this number would be two, contradicting the observation. Thus there is
at most one reflection in the entire array.

## 4. Zero reflections are impossible

Suppose all maps are translations and let $a_{ii}=3$. Every row and every
column of the array $(a_{ij})$ consists, as a multiset, of

$$\{3,1,2,4,e\},$$

where $e$ is its one extra offset. The row sum equals its extra offset
modulo five because $3+1+2+4=0$ in $\mathbb F_5$. Let $e_i$ be row $i$'s
extra offset and let $m_z$ count rows with $e_i=z$. The multisets of row
extras and column extras agree: count occurrences of each label in the
whole array and subtract the same five copies of the baseline
$\{3,1,2,4\}$.

For different rows $i,j$, same-layer coverage says their five coordinate
differences contain all four nonzero elements. Thus the difference
multiset is

$$\{1,2,3,4,e_i-e_j\}.$$

It has one zero exactly when $e_i=e_j$, and no zero otherwise. Consequently
the total number of equal-entry row pairs, summed over the five columns,
is

$$\sum_{z\in\mathbb F_5}\binom{m_z}{2}.$$

On the other hand, a column whose extra offset is zero has five distinct
entries. Every other column has exactly one equal-entry pair. The same
total is therefore $5-m_0$. We obtain

$$\sum_z m_z=5,\qquad \sum_z\binom{m_z}{2}=5-m_0.$$

These integer equations have no solution. For $m_0=0$, partitioning five
among the other four labels cannot give collision count five. For
$m_0=1$, partitioning the other four cannot give collision count four.
For $m_0=2$, the zero label contributes one and partitioning the other
three contributes only zero, one or three, never the required two.
For $m_0\ge3$, already $\binom{m_0}{2}>5-m_0$.
This excludes the zero-reflection case.

## 5. A single reflection is impossible

Suppose the unique reflection is at row $r$, column $c$, with $r\ne c$.
The four translation entries in row $r$ have offsets $3,1,2,4$ and sum
zero. The four translation entries in column $c$ are also precisely
$3,1,2,4$.

For any other row $i\ne r$, the quotient maps comparing rows $r,i$ have
one reflection. By Section 3, their four translation offsets are exactly
$1,2,3,4$ and sum zero. Thus

$$0=\sum_{k\ne c}(a_{rk}-a_{ik})
=0-(e_i-a_{ic}),$$

where $e_i$ is the extra offset in the entirely translational row $i$.
Hence $e_i=a_{ic}$. Since column $c$'s four translation offsets are
$1,2,3,4$, this value is nonzero. In row $i$, it therefore repeats one of
the baseline entries $3,1,2,4$: the entry in column $c$ is not unique in
its row.

Now use layer-$1$ coverage. For source fiber $j$ and target fiber $\ell$,
its five non-root route maps are

$$f_{k\ell}f_{kj}^{-1},\qquad k=0,1,2,3,4.$$

Compare column $c$ with any other column. These five maps have exactly one
reflection, so their four translation offsets are all nonzero. For each
$i\ne r$, this forces $a_{ic}$ to differ from the entry in every other
column of row $i$. That says the same entry is unique, contradicting the
previous paragraph. The one-reflection case is excluded.

Sections 3--5 exhaust the possibilities. Therefore the exterior matchings
cannot all exchange layers. $\square$

## Consequences for joint matching selection

This result gives a direct necessary clause for the fixed-root table
problem: **at least one selected external matching has a same-layer
entry**. It is not enough to choose only from the $244$ zero-same-layer
entries of the existing $18624$-permutation catalog.

In any permutation on two equal five-point layers, the number of
layer-$0$ to layer-$0$ entries equals the number of layer-$1$ to layer-$1$
entries. Thus one same-layer edge forces at least two in the complete
undirected graph, and the total same-layer edge count is even.

The root identity

$$\sum_{j\ne i}M_{ij}=T+S_i$$

also shows that every exterior vertex has at most one same-layer exterior
neighbor, since $T$ has only cross-layer edges and $S_i$ has one entry per
row. The same-layer edges therefore form a matching on each of the two
$25$-vertex layers, with at most $12$ edges in each. The necessary joint
range is consequently

$$2\le E_{\mathrm{same}}\le24,\qquad E_{\mathrm{same}}\equiv0\pmod2.$$

All these edges are off-$T$, so this consumes part of the existing total
off-$T$ budget of $25$; no stronger numerical lower bound is claimed here.

## Boundaries and outstanding obligation

The root matching choice, its normalized common $Q$, and the common
coordinate-layer partition are essential. Releasing the five root
matchings need not preserve this setup. The theorem does not exclude
fixed-root choices that include same-layer edges, and it does not resolve
the full six-fiber or arbitrary order-$60$ problem.

No new SAT input, annealing run, radius-two search, or numerical graph
search was used to obtain this obstruction.

## External discussion C6

Gemini read this proof and found no mathematical gap, via the existing
Antigravity conversation with requested/CLI-selected gemini-3.8-flash-high/high.
Root independently read the substantive argument. Raw response:
`reviews/dd82/20261011_C6_hs59_layer_capacity.json`; response wording and the
rejected unrelated C5 construction suggestion are recorded in
`reviews/dd82/20261011_C6_root_notes.md`. This is corroborating discussion,
not a Lean proof or independent backend model attestation.
