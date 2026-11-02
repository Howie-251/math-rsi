# Current (13,4)6804 source: no spare vertices

2026-10-27. The source and degree profile are complete; the proposed spare-fiber prediction is refuted. No candidate graph, BFS, or coverage search was started.

The fresh [official main table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) lists 6804 for (13,4), without bold optimality marking. Its exact cell HTML and retrieval time are saved in SOURCE_FACTS.json. The current [primary recipe](https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg13/dia4/README.md), construction.json, and complete literal edge list were downloaded. Source diameter four is inherited from that published construction; it was not rechecked here.

## Prediction and actual rule

The frozen prediction was that the thirteenth neighbor arose from a reflection matching inside each odd 81-point fiber, leaving at least one degree-12 vertex per fiber. In the actual recipe the reflection crosses **different** controller fibers:

    (g,x) -- (gz, -x+c),  z=y^6,  c=(0,0,1,0).

The controller is Z7 semidirect_2 Z12, with a=xy, b=y^4, their inverses, and z. In the author's numbering g=i+7j, multiplication by z sends g to g+42 modulo84. Thus z has no fixed controller vertex. Even when -x+c=x in the fiber coordinates, the two graph vertices remain distinct. Odd fiber size causes no unmatched graph vertex.

## One literal profile

Parsing the source once gave n=6804, m=44226, no loops or repeated edge rows, and degree histogram {13:6804}. All 84 fibers are independent. There are 168 unordered line-linked fiber pairs with 243 edges each and 42 plain-matched fiber pairs with 81 edges each. The 3402 plain edges were checked against the displayed reflection rule. Every vertex has exactly one plain neighbor and twelve line neighbors; the quotient has degree five at every controller vertex.

There are zero degree-spare vertices, and every vertex has thirteen saturated neighbors. Profile CPU was 0.132923931 seconds, below the two-second limit. The conditional allfree-R3 test was not run because its spare set is empty.

Consequently, no connected enlargement preserving every source edge and maximum degree thirteen can add any number of new vertices: all old vertices are saturated, so no new-old edge is possible. This is an obstruction to edge-preserving extensions of this fixed literal source. It does not exclude constructions that delete or redirect old edges, change the controller/chart, or use another source.

## Prior scope and disposition

The relevant prior Wiki row is `ddp-wave5-cayley84-nb4`: a fixed F7 semidirect_3 C12 quartic Cayley controller and the exact-NB4 requirement. It is not this source's mixed four-line-plus-one-plain operator; its closed range was not rerun or re-labelled. The odd-fiber observation previously suggested for the unavailable 972-point source was conditional and is not evidence for this actual 6804 graph.

This source-preparation task now stops. Evidence is PREDICTION.json, SOURCE_DIRECTORY.json, SOURCE_RECEIPTS.json, SOURCE_FACTS.json, construction.json, AUTHOR_README.md, source6804.edges, profile.py, RESULT.json, and terminal.json. No global Wiki, HTML, or delivery file was changed.
