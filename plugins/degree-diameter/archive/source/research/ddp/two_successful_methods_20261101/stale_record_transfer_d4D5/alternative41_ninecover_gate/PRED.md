# Three new41-point sources: arbitrary nine-sheet cover capacity

Recorded before the new adjacency/route computation. The target is a
degree-preserving ordinary nine-sheet cover of a41-point4-regular source,
giving369 points, which would improve the current(4,5)=364 only if its
diameter were at most5.

Inherited exclusions, not rerun:

* breadth_20261027_wave6/cyclic_cover369 fixes Allwright Graph1(a) and
  excludes its ordinary cyclic C9 covers by five signed voltage forms in
  the0-to0 slot. It is not an all-source or arbitrary-cover classification.
* refresh_20261029/controller41_transfer_gate fixes that same Graph1(a)
  and excludes a different affine-line transfer by a triangle-free vertex.

The new source change is limited to Michel de Messieres' N1,N2,N3, listed
as three additional nonisomorphic41-point,82-edge,degree4,D3 graphs in
the actual official desc_g3 page, October2026. That page says N1/N2 have
girth5 and N3 has one triangle. No new isomorphism or source-distance
verification is proposed.

Specific prediction: at least one new source may have at least nine
length-at-most-five nonbacktracking walks for every ordered source pair,
permitting an actual nine-cover voltage question. The triangle-free new
sources change the short-cycle route structure of Graph1(a), but this
does not by itself establish return capacity; the prediction is falsifiable
by a concrete pair with fewer than nine walks.

For each new source, count all nonbacktracking walks of lengths0..5, and
save the minimum count and a lex-first tight pair. A shortest path in any
ordinary graph cover projects to a nonbacktracking source walk: the unique
lift of an immediately reversed base edge would itself immediately reverse.
Each source walk has one lift endpoint from a fixed lifted root. Therefore
fewer than nine such walks to one base target prevents reaching all nine
vertices of that target fiber within5, independent of voltage values, deck
group, regularity of the covering action, or a C9 presentation.

Only three small inputs, one process, total at most10CPU including imports,
preparation, any download failure and route counting, with a separately
identified conservative preparation charge0.1. No369-point graph, solver,
source all-root validity/BFS, field/rank/Lean or review. A passed capacity
gate is necessary only, not a cover or record. Root decides any later
voltage generation. A failed source excludes only its ordinary nine-sheet
cover rule, not modified source edges or another graph family.

The actual official hrefs end in41_Messieres_N1/N2/N3.adjlistt and returned
404. Make only one obvious suffix correction to.adjlist for each, saving
the exact fetched URL and bytes. If unavailable, stop that source UNKNOWN
without guessing more filenames or changing sources. Do not touch the old
Allwright inputs, results, root documents or Wiki.

Implementation note before any new-source route count: the corrected N1 URL
is readable, but its three metadata lines are not prefixed by#. The first
attempt stopped parsing that observed format with no route calculations;
its actual receipts are retained as INITIAL_PARSE_FAILURE_*. The minimal
parser correction recognizes only the observed'(4,3)=41 N*;' prefix and
reuses the actual local N1 download. That attempt's charged0.147974707CPU
seconds remains in the same original10CPU budget; no source or timer changes.
