# Actual (5,6) 2836 source: no free attachment interface

The actual source was obtained once from
[Nishant Bhakar's primary repository](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg5/dia6).
The fresh main table lists 2836 at (5,6), without optimality markup.
The saved author files are README.author.md, source2836.author.edges.txt,
construction.author.json and verification.author.txt. The source's
diameter-6 assertion is inherited from the author's supplied verification;
no source BFS or independent diameter sweep was repeated.

PREDICTION.json was written before parsing the actual edges. Its
prediction was that the recipe leaves no degree slack, so the successful
edge-preserving star/free-proxy mechanism has no attachment interface
here. The literal confirms this: 2836 vertices, 7090 distinct edges,
no loops, no duplicates, and every vertex has degree exactly 5.
There are zero free vertices and zero free slots. Every prototype has
five saturated neighbors, so minSatN=5 and no free-neighborhood proxy
or complete spare star is available.

The author's point/line/layer ranges agree with actual adjacency:
0..1364 are points, 1365..2729 are lines, and 2730..2835 are the 106
inserted vertices. There are 6719 retained point–line edges, 212
base–layer edges and 159 layer edges. Every inserted vertex has exactly
one point neighbor, one line neighbor and three layer neighbors.
Thus the cubic layer really uses the entire remaining degree budget;
it is not a source of unfilled ports.

The resulting obstruction is uniform and stronger than absence of a
particular star. Retain all edges of this source and impose maximum
degree 5. Every old vertex remains saturated, so no edge can connect
any old vertex to a new vertex. Any positive number of new vertices
therefore makes the enlarged graph disconnected. No connected proper
edge-preserving enlargement at this degree exists, regardless of how
the new vertices connect to one another.

This closes only that fixed-source, degree-preserving, old-edge-retaining
mechanism. It does not exclude deleting source edges, rewiring, another
source, or general (5,6) graphs of order 2837. No absorption experiment,
anchor search, lower-missing-score search or new template was launched.
The one literal profile used 0.014543 CPU seconds and zero BFS runs.
RESULT.json and terminal.json have no pending work. The shared Wiki,
HTML and recovery entrance were not modified.
