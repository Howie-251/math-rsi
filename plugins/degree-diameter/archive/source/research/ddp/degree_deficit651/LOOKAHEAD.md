# Two selected low-cost exits from the 651-vertex source

The source has59 actual bad pairs. Its complete3230 one-step degree-deficit neighborhood has minimum61, attained at exactly two moves: add650–47/delete47–292 and add650–279/delete279–34.

This follow-up checked all3230 legal moves from each of those two61-defect graphs, using an exact closed-radius2/radius3 bitset distance criterion. Each neighborhood has exactly one improvement, returning to the original59-defect edge set. Every other neighbor is worse than61; neither graph has a61-defect neutral neighbor. Costs were3.84189 and3.83682CPU seconds. This is only the two specifically selected neighborhoods, not the entire two-step neighborhood of the original source.

The bitset scorer was checked against independent full BFS on the known650 positive control, the651 source, and two actual degree-deficit moves. Its radius criterion and apply/undo degree bookkeeping were independently reviewed. A simulated-annealing implementation exists in computations/ddp/deficit651/search.cpp, but no annealing profile was run. The fixed-source repair route is paused after these actual measurements; no claim of general651 nonexistence follows.
