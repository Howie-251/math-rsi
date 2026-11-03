# Uniform lexicographic products: optimistic screen

This is another standard graph-product operation, not an independent new research mechanism. All27 saved degree/diameter cases were screened. No graph was generated and no BFS ran.

## Object and exact formulas

Let G have at least two vertices and be connected, and let H be any simple undirected graph on m>=2 vertices; H may be an independent set. G[H] has vertices (u,x). Vertices in different fibers are adjacent exactly when their G-coordinates are adjacent, with every pair of H-coordinates allowed; vertices in the same fiber follow H. Thus n=m*|G| and maximum degree=m*Delta(G)+Delta(H). Maximum degrees can be attained simultaneously by independently selecting the two coordinates.

For distinct base vertices, product distance equals G-distance: every product edge changes the G-coordinate along a G-edge or stays inside its fiber, and a shortest G-path can be lifted using arbitrary H-coordinates. Any two vertices of one fiber have distance at most two through any neighboring G-fiber. Consequently, for target D>=3, diameter(G[H])<=D holds exactly when diameter(G)<=D, regardless of connectivity or diameter of H.

## Complete numerical bound

Write d=Delta(G)>=1. The degree budget implies m*d<=Delta because Delta(H)>=0. Relaxing H to an independent set is optimistic for order at fixed m and d. For d>=2, Moore gives |G|<=1+d*sum((d-1)^j, j=0..D-1). For d=1, connected G is exactly K2, so |G|=2. Enumerate every m=2..Delta and d=1..floor(Delta/m), maximize m times this base-order upper bound. This includes arbitrary base graphs, and does not assume the Moore bound is attainable.

|Delta|D|Saved baseline|Optimistic product upper|Maximizing m,d|Result|
|---:|---:|---:|---:|---|---|
|4|3|41|14|2,2|cannot improve|
|4|4|104|18|2,2|cannot improve|
|4|5|364|22|2,2|cannot improve|
|5|3|72|14|2,2|cannot improve|
|5|4|252|18|2,2|cannot improve|
|5|5|650|22|2,2|cannot improve|
|6|3|120|44|2,3|cannot improve|
|6|4|441|92|2,3|cannot improve|
|6|5|1518|188|2,3|cannot improve|
|7|3|170|44|2,3|cannot improve|
|7|4|684|92|2,3|cannot improve|
|7|5|2810|188|2,3|cannot improve|
|8|3|253|106|2,4|cannot improve|
|8|4|1100|322|2,4|cannot improve|
|8|5|5334|970|2,4|cannot improve|
|9|3|585|106|2,4|cannot improve|
|9|4|1768|322|2,4|cannot improve|
|9|5|9020|970|2,4|cannot improve|
|10|3|650|212|2,5|cannot improve|
|10|4|2485|852|2,5|cannot improve|
|10|5|33397|3412|2,5|cannot improve|
|11|3|715|212|2,5|cannot improve|
|11|4|3444|852|2,5|cannot improve|
|11|5|37628|3412|2,5|cannot improve|
|12|3|810|374|2,6|cannot improve|
|12|4|5832|1874|2,6|cannot improve|
|12|5|42342|9374|2,6|cannot improve|

## Decision and boundaries

Numerical surviving cases: 0.
Every optimistic upper is at most a saved valid construction lower bound. Therefore unchanged uniform lexicographic products, including uniform independent-set blowups, cannot improve any of these27 bounds. Stop this operation without generating candidates. The conclusion remains valid if public lower bounds later increase.

Nonuniform blowups, fiber sizes depending on the base vertex, partial cross-fiber matchings, added or rewired edges, and arbitrary vertex replacement are not covered. No claim is made about general graphs or a new general degree/diameter upper bound.

## Actual work

330 parameter pairs across27 cases; one worker; 0.000917165 CPU seconds for the input/bound calculation, below5 seconds. RESULTS.json gives all maxima and witnesses. The only computation is finite integer arithmetic; 0 graphs, 0 BFS.
