# One or two degree-six vertices at 23 points

## Claim and status

Let $H$ be a simple five-uniform hypergraph on 23 vertices, with exactly 34
edges and covering every pair. If exactly one or two vertices have degree
six, then $H$ has Property B. This is a complete paper candidate; actual-H
Lean implementation and cross-family review are still required.

## Actual selection

Let $r\in\{1,2\}$ count the six-degree vertices, and let $t$ count the
seven-degree vertices. The other vertices have degree at least eight, giving

$$170\ge6r+7t+8(23-r-t),\qquad t+2r\ge14.$$

Every low vertex has total codegree excess $4\cdot6-22=2$. Let $U$ be the
seven-degree vertices unit with every low. Removing the at most $2r$
exceptional neighbors gives

$$|U|\ge t-2r\ge14-4r.$$

Thus $|U|\ge10$ for $r=1$, and $|U|\ge6$ for $r=2$.

The existing 23-point strong-codegree certificates apply to seven-degree
vertices regardless of the minimum degree elsewhere. A pair of sevens with
codegree at least five already has a strict double-lock bound. Otherwise,
if a pair has codegree four, choose any third seven. The complete nonnegative
triple domain with maximum codegree four is strict. Such a third point exists
because $t\ge10$. In a counterexample, therefore, every seven-seven pair has
codegree at most three. This uses the actual 49-entry threshold package
`context/propertyb34-hour1-20261013/MIDDLE_THRESHOLDS_VERIFIED.json`;
its explicit 23-point portion is described in `MIDDLE_PROGRESS.md` §23.

## Local domains and extension completeness

For three locks, write their degrees $d_i$ and codegrees $\lambda_{ij}$.
The common triple count $a$ ranges from zero to the smallest pair codegree.
The exact pair counts are $\lambda_{ij}-a$; singleton and empty counts are
then forced by $d_i$ and 34 total edges. Retain nonnegative values.
The initial domains use one low plus two sevens, or two lows plus one seven.
All low-high codegrees are one. For two lows their mutual codegree may be
one, two or three. These are complete necessary local conditions.

To add another actual member of $U$, promote $p_T$ copies of each old trace
$T$ of size at most four, with $0\le p_T\le n_T$. The remaining
$7-\sum_Tp_T$ new incidences become its singleton and are subtracted from the
empty count. Enforce codegree one to each low, codegrees one through three
to old sevens, and the actual remaining excess budgets at each old and new
point. These are literal necessary conditions on an actual extension.
Require every deletion of a selected high point to remain a non-strict old
profile; a strict deletion already proves Property B. Canonicalization uses
all degree-preserving permutations and transports the positions accordingly.

The complete tables from `few_low23.py` are:

| Lows | Sevens | Labelled promotions | Retained labels | Orbits | Residual orbits |
|---:|---:|---:|---:|---:|---:|
|1|2|6|6|6|6|
|1|3|246|246|73|22|
|1|4|7571|1669|311|40|
|1|5|94965|1113|160|26|
|2|1|6|6|6|6|
|2|2|66|66|48|19|
|2|3|1638|554|160|19|
|2|4|13878|172|42|2|
|2|5|2733|1|1|0|

Each file is `FEW_LOW23_<lows>_<sevens>.json`. The strict bounds were
independently checked during generation: labelled-injection A/B/C for direct
bounds and complete exact rational weak-dual, quotas, slot capacities and
both directed weights for mixed-layout bounds. The floating LP supplies a
proposal only. The application uses the same actual bad-count vector in all
layouts, so a strict weighted average yields at least one strict layout.

## Exactly two lows

There are at least six members of $U$; select five of them. Iterating the
complete extension/projection classification gives only one residual input
to check at the final seven-lock level. Its bound is
$1741/2002<1$. Every actual selected input therefore has a strict certificate
on itself or on one of its smaller lock projections. Each such probability
certificate still concerns all 34 edges of the same H; it is not a coloring
of an induced subhypergraph. This proves $r=2$.

## Exactly one low

For every five selected members of $U$, a strict profile suffices. Otherwise
their nonunit graph, with edges where codegree equals two, has one of exactly
three shapes:

$$2K_2+K_1,\qquad K_3+2K_1,\qquad K_3+K_2.$$

Every residual has only codegrees one and two; the 26 residual inventories
split into 20, 4 and 2 of these graph shapes. This is checked directly in
`ONE_LOW_23_RESIDUAL_GRAPHS.json`.

Let $G$ be the nonunit graph on all of $U$. Every pair extends to a five-set,
so no pair has codegree three. Every five-set induces one of the displayed
graphs. In particular:

1. $G$ has no induced three-vertex path. Such a path could be extended by
   two other vertices to a forbidden five-set. Therefore each connected
   component of $G$ is a clique: a shortest path between nonadjacent
   connected vertices would contain an induced three-vertex path.
2. No component has four vertices. A four-clique and any fifth vertex
   cannot induce one of the displayed graphs. Thus every component has
   at most three vertices.
3. There are at most three components. If there were four, choose one
   representative from each and any fifth distinct vertex. The induced
   five-set would have at least four components, whereas every displayed
   graph has at most three.

All extensions used above exist because $|U|\ge10$. The three statements
give $|U|\le3\cdot3=9$, a contradiction. Hence some selected input has a
strict certificate, proving $r=1$.

## Scope

The graph contradiction holds for arbitrarily large $U$ and is an analytic
argument. The finite domains classify only traces on at most seven selected
locks. They do not enumerate whole hypergraphs. The general probability
lemmas connect each strict certificate to an actual proper coloring; these
new local-domain coverage and selection connections remain to be implemented
in Lean.

Saved-certificate readback: `NEW23_CERTIFICATES_VERIFIED.json` independently
replays this branch and the four-/five-low branch together, checking 1382
direct and 153 joint strict certificates with their actual input bindings.
The unneeded six-high diagnostic was stopped once the analytic graph
contradiction closed the one-low branch; it supplies no proof evidence.
