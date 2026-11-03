# Exact three-control model and two-orbit coverage principle

The known source construction is read from research/ddp/m1_sources/684_recovered_construction.json. Its group is C38 semidirect_23 C9, with multiplication

    (a,b)*(c,d)=(a+23^b*c mod38,b+d mod9),

and inverse(a,b)^-1=(-23^(-b)*a mod38,-b mod9). Coordinates use vertex_id=side*342+normal*9+phase. The group action is well-defined because23 is a unit modulo38 and23^9=1. Source degree7/D4 and the earlier exact source-edge binding are inherited; recover_684.py was not imported or executed and no old-source BFS was run.

Each side has four internal neighbors from two true inverse pairs. The three0-to1 cross voltages are(2,2),(2,6),(24,3); each is a perfect matching between the two342-element sides. Its reverse arcs use the actual group inverse. Even when two cross group elements are inverses of one another, they are separate0-to1 matchings: reversing an arc changes its side. They must not be merged as a single internal inverse pair.

This experiment deletes one whole original cross matching at a time, with no changed phase, normal coordinate, modulus, action or internal edge. Its three controls remove respectively(2,2),(2,6),(24,3), and the matching's reverse arcs. Every candidate retains4 internal plus2cross neighbors per vertex, hence is simple6regular with684 vertices and2052 edges. The producer actually checked all degrees, no loops/duplicates, reverse adjacency and edge count. All three complete edge lists are saved.

For every retained voltage, left multiplication g->hg on both sides sends the edge g->g*s to hg->hg*s. It is therefore an automorphism. The action is transitive within each side; it need not exchange the two sides or guarantee connectivity. Thus two identity representative roots, IDs0 and342, would suffice to prove whole-graph D<=4. Since the degree6 radius3 Moore bound187<684, a complete positive would have exactD4. A failure at either one root is enough to reject its control, without the second root or a global distance computation.

All three controls fail at root0. Their missing counts103,147,114 count states outside that root's radius4, not ordinary unordered vertex pairs. Negative exact global diameter and connectivity remain null. The minimum side/phase image sizes27,26,26 are actual finite endpoint coverage, not a formal-route capacity estimate. Each phase slot needs38 normals. The root files preserve every18-slot distribution and literal missing IDs.

The result closes exactly these three matching deletions. It does not classify all degree6 graphs on684 vertices, every source surgery, another voltage/action/phase family, or generalN(6,4). The earlier p43 free-translation transfer scope has different parameters and was not continued. No candidate score optimization or additional deletion was started.
