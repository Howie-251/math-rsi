# Current (14,3) 1141 source is bound and fully saturated

The actual current primary literal is
[deg14D3_1141_.edges](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/deg14D3_1141_.edges).
One small profile confirms1141vertices,7987distinct edges, no loops,
and degree exactly14 at every vertex. There are zero free vertices
and slots, and minSatN=14 throughout. Source D3 is inherited from the
official publication; no source BFS or candidate was run. Profile CPU
was0.016167seconds. The normalized copy source1141.header.edges has
header1141 7987.

The initial7×163Frobenius/Cayley guess is paper-refuted, rather than
silently retained. Since7 does not divide162, there is no nontrivial
C7 action on C163. Both Sylow subgroups of a group of order7*163 are
normal: their possible nontrivial Sylow counts7 and163 fail the
required congruences. The group is therefore C7×C163, hence cyclic.
For an undirected abelian Cayley graph with at most seven inverse
generator pairs, its radius-3 ball has at most

    1 + 2*7*3 + 4*C(7,2)*3 + 8*C(7,3) = 575

points. Thus no Cayley graph of order1141 has degree at most14 and
diameter at most3. The table's asterisk may refer to a former Cayley
entry; the description indeed lists an older1053Cayley graph. It does
not make the current1141graph Cayley. No F163 action, generators,
phase cover or transfer search was attempted.

The official current entry credits Francesc Comellas, October23,
2026, with GPT6Astra assistance. It describes vertex/edge insertion,
edge pruning and attachment exchanges based on a previous1118graph
credited to the handle mizopl. This is a non-Cayley augmentation
source, not a recovered group-generator recipe. The description's
statement that six vertices were added to1118 is arithmetically
inconsistent with1141. The current literal is bound, but the exact
old-to-new label/edit sequence is not. No individual author's
identity or construction is inferred from the handle or filename.

PROVENANCE_URLS.json preserves all seven links in the current1141
and former1118sections: both official literals, both Sage scripts,
both online script links, and the author primary pull request457.
FORMER1118_PRIMARY_FILES.json records that pull request's relevant
file metadata URLs without executing or downloading its source files.
It locates an explicit1118edge file, adjacency text, mathematical
construction notes and search code. These URLs are available for a
separately authorized actual1118header/recipe recovery; this task did
not fetch or profile that different graph.

The fixed current1141source has no edge-preserving star/proxy growth
window. Keeping all old edges and maximumdegree14 forbids every
old-to-new edge, because every old vertex is already saturated.
Any nonempty new-vertex set would therefore disconnect from the old
source. This closes only its connected edge-preserving enlargement
mechanism. It does not exclude deleting or rewiring old edges, other
sources, or general (14,3) graphs above1141.

PREDICTION.json preserves the initial guess and its explicit paper
refutation; RESULT.json and terminal.json are complete. No new graph,
world-record claim, original all-source verification, additional
parameter source, dependency, or shared Wiki/HTML change resulted.
