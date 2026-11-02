# One saved controller: first-contact triangle labeling

Input only `research/ddp/breadth_20261027_wave2/triangle_factor33_controller/best.edges`, with its designated triangle factor {3i,3i+1,3i+2}, i=0..10. No other controller, random graph, search, SAT, distance calculation or NB3 calculation is included.

Algorithm: choose the smallest old vertex whose two external neighbors lie in different designated triangles. Give it new label 0, and give its two triangle mates labels 1,2 in old-label order. Scan assigned vertices in increasing new-label order. When an external edge first touches an unassigned triangle, give that triangle the next three-label block, placing the touched endpoint at 3b and its mates in old-label order. At each scanned vertex, inspect its external neighbors in old-label order.

Prediction: this object's relabeling preserves every edge, makes the external neighbors of new vertex 0 equal to 3 and 6, and for each nonroot triangle b=1..10 its smallest external neighbor label m_b satisfies m_b<3b, the sequence of m_b is nondecreasing, and edge (m_b,3b) exists. Block 0 is excluded from the m_b<3b statement; its external neighbors necessarily have positive labels.

Save the literal old/new permutation, all first-contact events, the relabeled edge list and direct checks. This is one implementation sample, not a proof that every graph admits the labeling. The general preservation argument is assigned separately by the parent. One worker, at most 2 CPU seconds.
