# Uniform obstruction for every nonzero antipodal shift

Status: **VALID paper exclusion of the expanded stated family**. No new graph, matching assignment, BFS, solver call or endpoint enumeration was performed for this analysis. The existing 4096-case execution remains exactly 4096 tested reciprocal assignments; the larger exclusion below is algebraic.

## Fixed family and witness

All arithmetic is in F5. Retain the loop-deleted polynomial source G on the original coordinates (a,b,c), with neighbours

    (s,a*s-b,a^2*s+a*s^2-c).

Use the established coordinate change

    y=b-a^2/2,  h=c-a^3-4*a*y,
    b=y+3*a^2,  c=h+a^3+4*a*y.

Let H be G plus the step-one C5 on its five absolute vertices (a,y,h)=(a,0,0). For every nonzero v=(y,h), choose a nonzero shift tau(v), independent of a, subject only to tau(-v)=-tau(v). Add the matching

    M: (a,v) <-> (a+tau(v),-v).

There are twelve antipodal pairs among the 24 nonzero v, so this family has 4^12 shift assignments. The previously tested six-direction reciprocal family is a subfamily of 4096 assignments. As already proved in `ANALYSIS_ROUTES.md`, every such matching is simple and avoids old edges, and the resulting graph has 125 vertices, 375 edges and degree six.

Take p=(0,0,0) and Q=(0,2,0), both written here in original coordinates. Q also has gauge coordinates (a,y,h)=(0,2,0), saved vertex ID2. The claim is that Q is outside the closed radius-three ball of p for every allowed tau.

## Complete path classification

p is absolute and therefore has no M edge. A shortest path cannot use two consecutive M edges, since M is a matching. Thus a path of length at most three can have:

* no M edge, entirely in H;
* one M edge in the middle, H-M-H (including a shorter H-M path);
* one M edge last, H-at-most-two-M.

One M first is impossible at p. The only reduced three-step type with two M edges is M-H-M, also impossible at p. This classification includes all shorter paths; there is no omitted extra-matching route.

## No path entirely in H

A source walk of length at most three from p can be padded by its formal self-loop to length three. Its endpoint is

    (d,e,f),  e=v*(d-u),  f=e*(v+d+u).

For Q, d=0, e=2 and f=0. Since e is nonzero, f=0 gives u=-v, whence e=v^2=2, impossible because 2 is a nonsquare in F5.

If an H path of length at most three ending at Q uses a C5 edge, its first edge must be a C5 edge. An old neighbour (u,0,0) of p, u!=0, is nonabsolute, so an old first step cannot immediately be followed by a C5 step. A final C5 step would end at an absolute. Therefore the only additional cases are C5-G-at-most-two and C5-C5-G; three C5 steps end at an absolute.

After one C5 step the starting absolute is (s,3*s^2,s^3), s=+1 or -1. For its formal two-source-step endpoint to have first coordinate zero and second coordinate two, the two-step formula forces u=s. Its third coordinate is then -s, not zero. This also covers shorter old walks because an absolute has a formal source self-loop. Thus C5-G-at-most-two cannot reach Q.

After two nonbacktracking C5 steps the absolute parameter is s=+2 or -2. Its second coordinate is 3*s^2=2, so an old edge to Q would require the sum of second coordinates to be 2+2=0; it is instead 4. A backtracking C5-C5 pair returns to p and gives no new possibility. Hence Q is not in B3_H(p).

## No middle matching path

In p-H-M-H-Q, the first H edge must be an old edge to (u,0,0), u!=0; a C5 neighbour is absolute and has no M edge. The gauge vector of (u,0,0) is

    (y,h)=(2*u^2,u^3).

After its matching edge, write the new first coordinate as r*u. Its gauge vector is (-2*u^2,-u^3), so its original third coordinate is

    c'=u^3*(r^3+2*r-1).

For r=0,1,2,3,4, the coefficient is respectively 4,2,1,2,1. It is always nonzero. This matching endpoint is nonabsolute, so its final H edge, if present, must be an old edge. An old edge to Q, whose first and third coordinates are zero, requires c'=0. Contradiction. It cannot already equal Q after the matching step either, for the same reason.

## No last matching path

The mate of Q has gauge coordinates (d,3,0), where d=tau(2,0)!=0. In original coordinates it is

    X=(d,b,c),  b=3+3*d^2,  c=d^3+2*d.

It suffices to show that X is outside B2_H(p). It is nonabsolute, so the only possibilities are an old walk of length at most two or C5-G. The other two-step orders either cannot start a C5 step after an old edge, or end at an absolute.

For an old two-walk from p to (d,b,c), d!=0, the source formula gives the necessary identity

    c*d=b*(b+d^2).

For X, use d^4=1. The left hand side is 1+2*d^2, whereas the right hand side is 1+d^2. Their difference is d^2!=0. Shorter old walks are included by the formal loop at p.

For C5-G, its intermediate absolute has s=+1 or -1. The old third-coordinate adjacency equation to X implies

    d^3+d+s*(1-d^2)=0.

If d^2=1, the left hand side is 2*d!=0. If d^2=4, it is 2*s!=0. These exhaust nonzero d in F5. Thus X cannot be reached in two H steps, and a last matching edge cannot reach Q in three steps.

## Disposition and exact stopping scope

All path types are excluded, so d_(H union M)(p,Q)>3 for **every** a-independent, nonzero antipodal shift assignment tau(-v)=-tau(v). This excludes the full 4^12 family, not just the tested reciprocal subfamily.

The saved `SAVED_FIRST_WITNESS_SUMMARY.json` reports ID2 as the first missing target in all 4096 existing cases. That observation motivated the uniform proof; it is not substituted for the proof or relabelled as an enumeration of 4^12 cases. The four repaired vertical targets from `ANALYSIS_ROUTES.md` remain genuine local successes and do not contradict this distinct universal missing target.

The conclusion does not cover a different absolute cycle, matchings with arbitrary a-dependent fibre permutations, pairings that do not send v to -v, other extra edges, deletions or rewiring, or arbitrary 125-vertex graphs. Exact global diameters and ordinary unordered bad-pair totals were not calculated. No further parameter, field or matching search follows from this analysis.

Evidence: `PREDICTION.json`, `RESULT.json`, `PRED_CONTROL.json`, `SAVED_FIRST_WITNESS_SUMMARY.json`, `ANALYSIS_ROUTES.md`, and `SCOUT_SCOPE_ANALYSIS.md`. The last file records the earlier preparation-stage scope; the present post-experiment proof supplies the stronger stopping scope without changing that chronology.
