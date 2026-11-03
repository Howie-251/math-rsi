# Route-overlap cuts are valid for arbitrary two perfect matchings

Verdict: **VALID**. The3120 proposed linear cuts preserve every integer solution of the original unrestricted W(3,3) plus two-perfect-matchings model. This review is paper-only: no solver, BFS, geometry generation, matching enumeration, or candidate graph is run here.

The inherited geometry and original exact model are in [the earlier report](../../breadth_20261027_wave11/gq80_paired_matchings/REPORT.md), [constraint schema](../../breadth_20261027_wave11/gq80_paired_matchings/constraint_schema.json), and [geometry](../../breadth_20261027_wave11/gq80_paired_matchings/geometry.json). The old15-second MILP returned UNKNOWN with no incumbent. It did not exclude arbitrary pairs of perfect matchings. The present cuts are a new consequence of route overlap, rather than a fixed matching, symmetry assumption, or resumption with unchanged constraints.

## Notation and geometry counts

There are40 points and40 lines, with four incidences per vertex. Retain all160 incidence edges. Let P be any perfect matching of the point side and Q any perfect matching of the line side. The resulting target would be80 vertices,200 edges, and degree5.

For a point x, let Cx consist of x and every point collinear with x in the original quadrangle. Then |Cx|=1+4*3=13, and its complement consists of27 same-side far points. For every distinct x,y,

    |Cx intersect Cy| = 4.

This is a pointwise identity, not an average. If x,y are collinear, the intersection is the four points on their unique line, including x,y. If they are not collinear, each of the four lines through x supplies its unique point collinear with y, giving four common points. Equivalently, on the point side the symplectic polar hyperplanes are distinct projective planes intersecting in a four-point projective line.

Consequently, for every distinct x,y,

    |Cy minus Cx| = 9,
    Zxy = points minus (Cx union Cy),
    |Zxy| = 18.

These counts hold whether the prospective matching edge xy is collinear or noncollinear. The line side has the dual identities by the generalized-quadrangle axioms; no point-line self-duality assumption or special matching is needed.

## All possible routes of length at most3

Assume Pxy=1, so the matched neighbor of x is y. A path from x to another point has an even number of incidence edges. The same-side vertices reached within three steps are therefore contained in the union of:

* Cx, from zero or two incidence steps;
* Cy, from the matching first and then up to two incidence steps;
* P(Cx), from up to two incidence steps and the point matching last;
* the points on Q(L), for the four lines L incident with x, from incidence–line matching–incidence.

A path having no incidence edge stays within the single P edge at x; repeated matching steps add no new endpoint beyond x and y. With two incidence edges and one matching step, the matching can only be first, last, or middle, exactly as listed. Thus no same-side path type has been omitted.

The first two sets miss Zxy by definition. For each of the four incident lines L, put M=Q(L). If x is incident with M, all four points on M are in Cx. If x is not incident with M, the unique-collinear-point axiom gives exactly one point on M in Cx. In either case M contains at most three points outside Cx, and hence at most three in Zxy. The entire opposite-matching relay therefore contributes at most12 distinct points of Zxy. Overlap between relays only decreases that bound.

For full D3 coverage, all18 points of Zxy must be covered. It follows that

    |P(Cx) intersect Zxy| >= 18-12 = 6.

This is also the direct accounting of27 far points: the own-first contribution is pointwise at most9, the opposite relay is at most12, so at least6 must be supplied by own-last. The Zxy argument makes the required overlap exclusion explicit.

## Exact linear inequality and its scope

Cx and Zxy are disjoint, and P is a matching. Therefore

    |P(Cx) intersect Zxy|
       = sum P_uv over u in Cx and v in Zxy.

The234 unordered cross edges are distinct because the two sets are disjoint. When Pxy=1 the sum must be at least6; when Pxy=0 its nonnegativity suffices. Combining the two cases gives the valid linear cut

    sum_{u in Cx, v in Zxy} P_uv - 6*P_xy >= 0.

The selected edge xy is not among the234 cross edges, since x,y are outside Zxy. It is a separate235th nonzero coefficient. The reverse-root inequality uses Cy in place of Cx, with the same Zxy. Apply both orientations to each of780 possible point matching edges, and then apply the dual argument to all780 line matching edges. This gives2*780*2=3120 cuts. All possible internal edges remain available; none is preselected or forbidden by an extra geometric hypothesis.

Adding the cuts to the original80 degree equations and1080 exact cover rows gives4280 rows and47400+3120*235=780600 nonzeros, consistent with the producer's [MODEL_STATS.json](MODEL_STATS.json). This review does not rebuild that matrix or launch the prepared model.

## LP interpretation and limits

Every integer solution of the original exact D3 matching model satisfies the new inequalities. Thus the feasible graphs are unchanged. The inequalities also hold on the convex hull of all such integer solutions. They can strengthen an LP relaxation by carrying the whole conditional counting argument for a selected edge into a fractional model before that edge is fixed.

Strict LP improvement, an improved lower bound, solver performance, or infeasibility is not established by this proof. In particular, the original model's exactness on binary matchings does not mean its fractional relaxation already includes every valid integer inequality. Whether any new row is redundant for that relaxation has not been tested here. A new bounded solver run may use these valid cuts; UNKNOWN or no incumbent would still not exclude this family.

The scope remains arbitrary perfect matchings on both40-vertex sides, retaining the complete original incidence graph. No source or graph other than this exact80-vertex template is implicated. There is no new actual target graph, diameter, or ordinary bad-pair count from this review.
