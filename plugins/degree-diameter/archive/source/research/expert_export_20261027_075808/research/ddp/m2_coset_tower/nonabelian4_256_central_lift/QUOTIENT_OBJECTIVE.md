# A projection objective that detects unavoidable central deficits

This is a proposed next search objective for the existing four-orbit Q64
construction. It derives a lower bound from the exact central forms and
the recorded 403-projection experiment. No projection search, center-bit
enumeration, graph generation, or BFS was performed for this note.

The group, tree gauge, thirteen free-edge variables, and named-edge walk
convention are those in [CENTRAL_LIFT_MATH.md](CENTRAL_LIFT_MATH.md).
The observed results below are from [summary.json](summary.json).

## Definition and exact lower bound

Fix a projected D32 voltage assignment P, with the three tree voltages
equal to the identity. Let z range over the thirteen free central bits.
For each slot

    alpha = (source orbit i, target orbit j, projected endpoint (a,p)),

collect all length-at-most-three nonbacktracking named-edge walks. There
are 4*4*32 = 512 slots. Correct Q64 multiplication gives an affine form

    ell_w(z) = beta_w XOR parity(mask_w & z)

for each walk. Let F_alpha be the set of distinct pairs (mask_w,beta_w),
not the multiset of walks and not just the set of masks. In particular,
equal masks with opposite constants give two forms that always cover
both lifts; repeated identical pairs give only one form.

Define

    N_empty(P)     = #{alpha : |F_alpha| = 0},
    N_singleton(P) = #{alpha : |F_alpha| = 1},
    L(P) = 2*N_empty(P) + N_singleton(P).

Each slot represents two actual Q64 targets. An empty slot misses both
targets. A nonempty slot misses one target precisely when all its forms
evaluate to the same bit. Consequently the exact four-root deficit is

    M_P(z) = 2*N_empty(P)
             + sum_{alpha: F_alpha nonempty}
                 1[all ell in F_alpha have the same value at z].

A singleton contributes one for every z, even if its unique form is a
nonconstant function of z. Every other summand is nonnegative. Thus

    M_P(z) >= L(P)

for every legal central assignment. The coefficients 2 and 1 count
missing actual vertices; they are not chosen heuristic weights. By the
simultaneous left Q64 action, the full number of bad unordered vertex
pairs is 32*M_P(z), and therefore is at least 32*L(P).

N_empty is exactly the sum of the four quotient-root radius-three
deficits. Optimizing it alone cannot distinguish quotient-D3 projections
whose central forms can or cannot reach both lifts.

## What the completed 403 projections show

Of the 403 projections, 395 have an empty slot. The remaining eight have
N_empty=0, but their N_singleton values, in recorded cursor order, are

    21, 35, 20, 27, 31, 23, 33, 21.

The recorded `constant_bad_slots` equal these singleton counts: a
nonempty slot has a globally constant bad event exactly when all its
affine forms are identical, hence its deduplicated set has size one.

These eight projections therefore have immutable four-root deficits of
at least 20–35, or at least 640–1120 bad unordered pairs respectively.
These are lower bounds, not attained minima. For example, cursor 185
has L=20, while its already completed exact central minimization has
minimum M=36. All eight are excluded from D3 by the singleton condition
alone. This explains the observed failure without extrapolating to
unexamined projections.

## Legal projected parallel matchings

Legality must be checked separately from L. In one endpoint class,
orient all matchings in the same direction and compare projected
voltages (a,p).

- Different projections always give different Q64 voltages.
- Two equal projections are allowed, with the necessary and sufficient
  condition z_e XOR z_f = 1. A tree bit is fixed at zero.
- Three equal projections have no legal lift to three distinct
  matchings, because a quotient element has only two preimages.

In the current tree, the duplicate-pair equations use disjoint free-bit
supports. If no triple occurs, they define a nonempty affine legal
space z=z_*+Tt. There is no reason to reject a projection merely because
two of its parallel matchings coincide. Their distinct central lifts
also give a genuine two-step route to the central element. All named
edges must be retained during form construction.

An optional stronger bound is obtained by substituting z=z_*+Tt into
every form and deduplicating again. Its mask and constant become

    mask' = T^T mask,
    beta' = beta XOR (mask dot z_*).

Empty slots are unchanged, and singleton counts can only increase.
Thus the resulting L_legal is at least L and remains a lower bound for
every legal lift. This is a possible simplification of the same
objective, not an additional experiment performed here.

## L=0 does not establish a feasible lift

For a slot with two distinct forms (m_0,beta_0) and (m_1,beta_1), covering
both targets requires the forced equation

    (m_0 XOR m_1) dot z = 1 XOR beta_0 XOR beta_1.

These equations must be jointly consistent with parallel-edge legality.
For example, the abstract slots {0,z_1} and {0,1 XOR z_1} have neither
empty nor singleton form sets, but require z_1=1 and z_1=0 respectively.
This is an illustration of the Boolean interface, not a newly observed
Q64 graph example.

Restriction to forced equations may collapse other slots to singletons
or produce new forced equations. Even if this process is consistent,
larger form sets still impose disjunctions that need not be jointly
satisfiable. The complete condition remains that a legal z lie outside
every affine bad set, as proved in
[CENTRAL_LIFT_MATH.md](CENTRAL_LIFT_MATH.md). The small-slot consequences
are developed in [PARITY_OBSTRUCTION.md](PARITY_OBSTRUCTION.md).

## Suggested use in a future coordinate search

Use L, or its legality-restricted version, as the projection score
within the explicitly chosen coordinate neighborhood. Discard
projections with no legal distinct-matching lift first. This gives
credit for removing a singleton obstruction as well as an empty slot;
it also permits an improvement that temporarily introduces an empty
slot but removes more than two singleton slots. A rule that first
minimizes N_empty lexicographically would prevent that trade and retain
the failure mode observed above.

For the D3 decision, L>0 safely avoids center enumeration. At L=0,
combine the forced GF2 equations with legality and then use the exact
central-coverage test for survivors. Do not stop at quotient D3 or at
L=0. A strict-descent search on L can itself stop at an unliftable
plateau; this lower bound supplies useful feedback but does not promise
access to a lift-feasible projection.

If a later authorized search instead minimizes the actual lifted
deficit, write mu(P)=min_{legal z} M_P(z). An incumbent exact value B
allows any neighbor with L(P)>=B to be skipped when seeking a strict
improvement. Remaining neighbors require exact central scoring before
claiming an improvement in mu. Lower L alone does not imply lower mu.

This note specifies only the next usable objective and its limits. It
does not authorize or report additional starts, coordinate moves, or
center-bit trials. A positive local minimum would concern only the
completed neighborhood, not the full Q64 construction family.
