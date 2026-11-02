# Existing11-degree D2 source for local edge repair

The user explicitly requests modifying existing small D2 graphs using edge
completion, rather than only fixed-old-edge cloning. Select the current
published106-vertex11-degree graph, not the previously bounded91-vertex
Brown source. The primary description itself reports a successful104->106
edge-rewiring construction.

Download its linked raw adjacency file once, with15-second network timeout
and no retry. Parse the leading vertex identifier in each row, save the
unchanged original, and bind its simple undirected adjacency. Prediction:
n106,m582,degree10:2/11:104, with the two spare vertices34 and54. Check its
two-step common-neighbor coverage once as a newly acquired source; do not
rebuild/recheck an old D2 source or restore N(8,2)/n61.

For any prospective107-point max11/D2 graph, each vertex has degree>=10,
since1+9*11=100<107. The first minimal editing rule is: delete4 disjoint
old edges away from the two spare vertices and attach one new degree10
vertex to the resulting10 spare endpoints. It would leave all old vertices
degree11. This is a concrete rule to test, not a claimed graph. A second
nearby degree11-newpoint rule requires at least5 old-edge deletions.

Prepare, for each source edge u-v, the old pairs whose unique two-step route
uses that edge. These explain which additional new adjacencies are forced;
do not merely count final bad pairs. Source preparation budget5CPU seconds;
no search/solver, graph candidate, field generation or Lean in this batch.
