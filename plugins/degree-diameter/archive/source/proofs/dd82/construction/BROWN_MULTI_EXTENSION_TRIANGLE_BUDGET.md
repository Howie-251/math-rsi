# Brown57 extensions to 59, 60, and 61: necessary edit budgets

Date: 2026-10-11. This is a new-target consequence of the already established
Brown57 triangle data, not a new verification of the 57-point lower bound.
It excludes deletion-only extensions, not arbitrary target graphs.

Use the fixed graph and vertex classes in
[BROWN_EIGHT_DELETE_OBSTRUCTION.md](BROWN_EIGHT_DELETE_OBSTRUCTION.md).
It has 57 vertices and 224 edges. Its 21 internal vertices each belong to
four triangles. Every old edge belongs to at most one triangle. These exact
finite facts are existing dependencies, not re-enumerated here.

Suppose k new vertices are added, t old edges deleted, a old–old nonedges
added, and h edges placed between new vertices. The final graph has order
n=57+k, maximum degree eight and diameter at most two. Since n>57 it is
eight-regular.

For any final vertex v, the radius-two route budget gives

    2*number_of_triangles_through(v) ≤65−n.

Indeed edges among the eight neighbors of v each consume two repeated
length-two routes. Thus the triangle bound is three at n=59 and two at
n=60,61. Each of the 21 old internal vertices must lose at least one,
respectively two, of its four old triangles. An old triangle survives if
all its edges survive, regardless of any new edges. Each deleted edge can
destroy at most one old triangle, accounting for at most three of these
required internal-vertex/triangle incidences. Consequently

    t≥7 for n=59;       t≥14 for n=60 or61.

Let b count old–new edges. Summing final old degrees gives

    b=8+2t−2a.

Summing degrees at the k new vertices gives 8k=b+2h. Eliminating b yields

    a=t−4k+4+h.

In particular:

| Final order | Necessary old deletions | Necessary old–old additions |
|---|---:|---:|
|59|t≥7|a≥3+h|
|60|t≥14|a≥6+h|
|61|t≥14|a≥2+h|

So no extension to any of these orders can merely delete old Brown edges
and add new vertices. Actual construction must replace old adjacencies as
well. The much stronger existing 58-point bound t≥10,a=t is retained from
[BROWN_NINE_DELETE_OBSTRUCTION.md](BROWN_NINE_DELETE_OBSTRUCTION.md), and
was not re-proved here.

The displayed lower bounds are necessary only; they do not assert that
any edit pattern attaining them can be completed. No new search, finite
check, or Lean work was performed for this corollary. It is a root-derived
planning constraint, with no additional cross-model review at this point.
