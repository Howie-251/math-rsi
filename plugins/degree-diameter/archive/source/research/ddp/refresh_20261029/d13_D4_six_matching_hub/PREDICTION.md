# One frozen six-matching-edge hub candidate

Use only the saved source `research/ddp/more_graphs_20261027/d13_D4_current6804/source6804.edges` and its construction.json. The source is the 6,804-vertex 13-regular diameter-4 graph with controller C7 semidirect_2 C12. Multiplication is (i,j)(k,l) = (i + 2^j k mod7, j+l mod12), a=(1,1), and z=(0,6)=a^6. A vertex has label 81(i+7j) + x0+3x1+9x2+27x3.

Fix x*=(0,0,2,0), fiber code 18. It is fixed by gamma(x)=-x+(0,0,1,0). The twelve endpoints are `(a^k,x*)`, k=0..11, with literal labels

`T = [18,666,1395,1719,2367,3096,3420,4068,4797,5121,5769,6498]`.

Freeze exactly six original central-matching edges:

`M = [(18,3420),(666,4068),(1395,4797),(1719,5121),(2367,5769),(3096,6498)]`.

The candidate deletes M and adds vertex w=6804 adjacent to every vertex of T. If generated, it has 6,805 vertices and 44,232 edges; every old degree stays 13 and w has degree 12. No other matching, fiber coordinate, source, or seed is authorized.

Predictions to test: (1) t(x)=d_G(x,T) has maximum at most 3, so w reaches every old vertex in at most 4 steps; (2) all old-old distances in the changed graph remain at most 4. Both are conjectures for this one candidate, not inherited source facts.

First bind the six edges to the recipe and require that they are present in the literal edge list and pairwise disjoint. Run one multi-source BFS on the original graph from T. Because every removed edge has both endpoints in T, a shortest path to its first T vertex never uses M, hence d_(G-M)(x,T)=d_G(x,T). If any t(x)>3, save a witness and stop before constructing the candidate or running any candidate BFS.

Only on passing that gate, construct the actual changed graph and check radius 4 from root 0 onward, stopping at the first failure. Complete all roots if none fails. A positive graph is saved for the parent's separate independent verification and current public comparison. The equivalent exact old-pair condition is: for every pair with d_(G-M)(x,y)>4, t(x)+t(y)<=2.

Budget: one worker, at most 30 CPU seconds including preparation; no restart, parameter change, source all-root revalidation, or Lean work.

Targeted prior-scope query: the source directory and its corresponding d13-D4 ledger experiment files contain the two whole-matching controls (remove every z edge / replace every affine offset by zero), central packet analysis, fixed C8 obstruction, and one C9 transfer. No record of this six-edge common-hub candidate or a 6,805-vertex graph was found. The query was confined to this source's records.
