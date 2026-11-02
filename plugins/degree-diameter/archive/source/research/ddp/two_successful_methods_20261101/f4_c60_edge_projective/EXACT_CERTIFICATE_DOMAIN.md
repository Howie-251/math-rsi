# Exact rank/pencil criterion for the literal C60/F4 linear chart domain

## Statement and scope

Use the saved simple5regular C60, the five-conic directions over polynomial F4, full four-point line fibers, invertible edge-dependent linear charts, and exact reverse matrices with direction transport. No affine offsets are included. Then the resulting graph has diameter at most3 **if and only if**:

1. Every directed controller edge has a complete five-plane backtrack pencil.
2. Every ordered nonadjacent/equal controller pair has a rank-three nonbacktracking3-word.

Sufficiency is the already accepted actual3840 route proof. The point here is necessity on triangle edges, where an extra two-step route exists. The generated graph, SAT answer and compiled Lean proof are unchanged. This is a paper characterization, not an additional Lean theorem or a classification of all degree20 graphs.

## Controller facts actually needed

The existing required-pair capacity file proves that if all NB3 words at any nonadjacent/equal pair have rank at most2, the union of all <=3 zero-source route images has at most61 of64 points. That argument uses only homogeneous linearity and literal route counts; it does not require globally equal charts. Thus condition2 is necessary even for edge-dependent charts.

The new adjacent trace is saved in EXACT_CERTIFICATE_CONTROLLER_TRACE.json. Each controller vertex has exactly two oriented NB3 words returning to itself, the two orientations of its unique triangle. External edges have no additional NB2 or NB3 route; triangle edges have exactly one NB2 route and no NB3 route. Backtracking routes are accounted separately in the pencil.

## Why a four-plane triangle pencil cannot be repaired

Fix triangle edge u-v. Its two four-point subsets in the five-point quotient PG(1,4) give either four or five distinct backtrack planes through the direct noise line L. Five planes cover all64 points. Four planes cover only

    4 + 4(16-4) = 52.

The only extra route is the triangle's two-step image plane K. If K does not contain L, its intersections with the four pencil planes are four distinct lines in K, containing13 of its16 points. It adds only3 points, giving at most55. If K contains L and is already in the pencil, it adds none. The only way K could repair the missing12 points is to be the fifth pencil plane, in particular K contains L.

But then append the reverse of the direct edge to this two-step triangle route. Its three-step closed-word noise span still has dimension2: the appended noise line lies in the transported K. Reversing a full-line path preserves its noise rank (the reversed relation is the original relation inverted by its invertible center matrix), so the other orientation of the same triangle also has rank at most2.

Now consider source coordinate0 in fiber u. By the literal controller trace, its only three-step closed routes are those two triangle orientations. Its two-step backtracks contribute five lines. Even allowing all these linear subspaces to add their maximum independent nonzero points gives

    1 + 5(4-1) + 2(16-1) = 46 < 64.

Thus some same-fiber target cannot be reached within3, contradicting diameter3. Therefore triangle pencils must also have all five planes. External pencils were already necessary because no extra route exists. This establishes condition1.

## What this changes

For this exact C60, fixed-conic, homogeneous edge-chart domain, the original7200-selector SAT certificate is complete for diameter3, rather than just a sufficient search subdomain. The previous cautious statement remains the correct historical description before this argument. No prior RAW_UNSAT is upgraded, no new exhaustive matrix classification is claimed, and affine offsets, changed frames/controllers, or collective coverage on other controllers remain outside the conclusion.
