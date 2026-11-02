# Spread the five omissions and test six disjoint full radius2 covers

2026-11-01. The previous same-column mixed-copy/K6 rule is now closed by
its independently checked160>156 integer proof. This new experiment changes
the omission geometry and the integer formulation. No old factor/field,
source cube, sigma, R2 or Steiner verification is repeated.

## One actual selected rule

Reuse the already built complete source S8775/118300 and its accepted
synchronized A³/B³ proof. Reuse the saved sigma matching. From the old
eight groups in ../mixed_copy_cycle_sigma_31/INTEG_BLOCK_LOCAL_BINDING_RESULT.json,
take the smallest absolute label in groups1..5:73,138,204,269,334. For
a=0..4 omit the fourth original-neighborhood copy of class(a,b_a).
All other full original-S-neighborhood copies0..4 are present.

Add the present-representative4/5 cycles as before. Add same-copy sigma
matching edges only when both endpoints exist. The five omissions now
remove five matching edges, rather than lying over sigma's fixed column.
Predict base n10070, mandatory m151970, cycle edges1620, matching edges795,
total m154385. Predict F degrees28:30/29:1590, old-U degrees30:130/31:8320.
The unrestricted spare pool remains1750; this search deliberately uses
only the130 freed old U points, each of capacity one.

The routing prediction is that the120 freed U points with nonabsolute B
coordinate reach at least five of the old projection groups in their
two-step original-absolute target supports; the ten with absolute B
coordinate reach one. This contrasts with the old same-column model's
one-group U channels. Check the actual current graph rather than assuming
that different B labels automatically give complementary routes.

## Small exact coloring/cover model

Find six disjoint sets S_h of those130 vertices, each of size<=26, such
that the closed radius2 balls around S_h cover EVERY old G0 vertex.
Every U pin may be assigned at most once. Since130<6*26, any unused pins
can be assigned to a helper with spare budget without harming coverage;
therefore assigning every pin exactly one of six colors is without loss.

For every old target v collect the exact130-bit mask

    E_v = closedB2_G0(v) intersect freed_U.

Each mask must contain every color. Identical masks may be merged. A mask
containing a smaller retained mask is redundant; save a subset witness
for EACH old target so the reduced model remains a complete coverage
certificate. If a mask has fewer than six points, the U-only submodel is
immediately impossible. Do not turn that into a general cap31 exclusion.

Use binary x[h,u], at most780 such variables, each pin exactly one color,
each color class<=26, and one cover row per retained mask and color.
Helper colors are interchangeable. A restricted-growth first-occurrence
ordering on one chosen mask is valid symmetry breaking; do not additionally
impose unrelated pin-count or label orders that might remove solutions.
An optional single integer max-load variable z<=26 can provide a nonzero
balancing objective; any feasible point is enough, not an optimality claim.

If feasible append K6 on six new helpers and connect h only to S_h. The
final target is(31,3)10076/154530. All8450 old U points then have degree31.
Old-old routes inherit the fixed source/interior clone proof. Each helper
reaches G0 through its OWN radius2 cover and is adjacent to all other
helpers. Unlike the earlier joint-only model, this also supplies valid
individual helper prefixes when the edges to prior helpers are included.
Actual full graph and six new-root BFS still require fresh acceptance.

## Budget and result boundary

One base construction from the saved S and recipe<=15CPU, one worker.
One exact130-point model batch including masks/imports<=60CPU, solver<=45
seconds, one worker, one hole layout and no seed/timer restart. Return the
complete masks and subset-witness reduction, actual status and any pin
solution. If feasible save the complete graph and hand it to independent
acceptance. If UNKNOWN or infeasible, record only this U-only fixed-rule
scope; F-pin repairs and other layouts remain open.

The broader Goal is unchanged. The candidate would exceed only the
currently located10075 published guarantee by1; exact priority is UNKNOWN.
No graph/parameter/Lean increment before actual mathematical acceptance.
