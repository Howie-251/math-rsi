# A missing NB3 controller route obstructs actual diameter three

This is a counting proof, with no new graph generation or computation. It strengthens the combined controller result for the specified no-intrafiber, full-F9-line lift model.

## Distinct nonadjacent controller vertices

Let C be a simple graph of maximum degree r, and replace each controller vertex by a fiber of size q^3. Suppose there are no edges inside a fiber, and a lifted vertex has at most q neighbors in each adjacent controller fiber. The actual Fq^3 affine-line construction has exactly q such neighbors; the argument does not require any matrix rank hypothesis or restriction on affine offsets.

Suppose distinct nonadjacent controller vertices u,v have no nonbacktracking length-three walk. Then they have no length-three walk at all. Indeed, if a length-three walk has an immediate reversal in its first two edges, its form is u,a,u,v, which requires the edge uv. If the reversal is in its last two edges, its form is u,v,a,v, again requiring uv. Both contradict nonadjacency. Every remaining length-three walk would be nonbacktracking.

Fix any point x over u. A lifted walk projects to a controller walk of the same length because there are no intrafiber edges. No walk of length0 or1 reaches the fiber over v, and no walk of length3 reaches it by the preceding paragraph. Thus every point over v within distance at most3 of x must be reached in exactly two steps, through a common controller neighbor of u,v. There are at most r such common neighbors. Each two-step controller route gives at most q choices on its first edge and q on its second, hence at most q^2 target points. The union therefore has at most r*q^2 points.

When q>r, r*q^2<q^3. At least one target point over v has distance greater than3 from x, so the lifted graph cannot have diameter at most3. For the present r=6, q=9, the bound is6*81=486<729, leaving at least243 target points uncovered for every fixed x over u. This holds for arbitrary compatible true-inverse affine charts and offsets, and indeed for any edge relations with the stated per-fiber degree bound.

## Equal controller vertices

For completeness, in the specific true-inverse affine-line model, if u has no nonbacktracking length-three closed walk, it has no triangle. A three-step closed walk in a simple graph is necessarily a triangle, so no length-three route returns to its fiber. There are no one-step intrafiber routes. A two-step route returns through one controller edge and its reverse. True-inverse affine charts, with the port line carried to its reverse line and the compatible reverse offset, make the possible endpoints exactly a line x+L_p through x in the source fiber. Each of at most r such lines contains q points and all contain x. Including the zero-step route gives at most

`1+r*(q-1)`

reachable points over u. At r=6,q=9 this is49<729. Affine offsets cancel in the compatible inverse relation. This equal-controller-vertex case is not needed for the present family, because every deck's zero K4 supplies a triangle at every controller vertex.

## Application to the complete K4 / Z20 family

Each controller in this family has a zero K4 in each deck. Therefore every equal-vertex class already has a nonbacktracking length-three closed route. Every missing required class detected by the exact search is consequently a pair of distinct nonadjacent controller vertices; if the source and target have the same base index, the missing residue is necessarily nonzero. The complete symmetry reduction and two exhausted searches show that every shift assignment has such a missing class, unless the controller is disconnected, which already obstructs a connected finite-diameter lift.

The first counting argument thus applies to every member of the fixed six-nonzero-shift K4 / Z20 family. **No controller in this family can support a diameter-at-most-three lift on F9^3 fibers with no intrafiber edges and nine neighbors per incident controller edge.** In particular, arbitrary compatible true-inverse affine charts and offsets cannot repair the obstruction. The family exclusion is stronger than failure of the full-rank-plus-pencil certificate.

This does not exclude other 80-vertex controllers, models with intrafiber edges, different per-edge neighbor counts, or unrelated graphs. No fiber graph was generated or assigned a measured diameter.
