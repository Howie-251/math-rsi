# Exact eleven-bit lifting with two prescribed central triangles

This note defines a restricted family within the existing K4/Q64,
256-vertex, degree-eight construction. The two prescribed triangle
products guarantee that every vertex reaches its central mate in at
most three steps. They do not guarantee diameter three. The remaining
coverage and simplicity conditions below are exact for this family.

Only the saved 832-bad-pair source parameters were read, and two group
products and their dependent-edge coordinates were checked. No new
graph, projection enumeration, central enumeration, or BFS was run.

## 1. Group and prescribed triangles

Use

    (x,s)(y,t) = (x+(-1)^s*y+16*s*t mod32, s XOR t),
    c = (16,0),
    (x,0)^-1 = (-x mod32,0),
    (x,1)^-1 = (x+16 mod32,1).

The element c is central of order two. The quotient by <c> is D32,
with coordinates (a,s), a modulo 16.

Base edges have their existing IDs and canonical orientations:

    01: 0,1,2       02: 3,4,5       03: 6,7
    12: 8,9        13: 10,11,12    23: 13,14,15.

Tree edges 0,3,6 have voltage e. Impose

    h2 * h12 * h7^-1 = c,        triangle 0 -> 1 -> 3 -> 0,
    h9 * h15 * h11^-1 = c,       triangle 1 -> 2 -> 3 -> 1.

Equivalently, define the dependent voltages by

    h12 = h2^-1 * c * h7,
    h15 = h9^-1 * c * h11.

The independent edges, in bit order, are

    F = [1,2,4,5,7,8,9,10,11,13,14].

Any eleven Q64 voltages on F determine exactly one assignment satisfying
the tree and triangle conditions, before checking simplicity. Conversely,
every assignment satisfying those conditions is obtained this way.

## 2. All four orbits reach their central mates

If a closed triangle has edge product abc=c, changing its starting
vertex changes its product to a^-1*c*a=c, and reversing it gives
c^-1=c. Thus each cyclic start of either prescribed triangle also has
product c.

The first triangle visits base vertices 0,1,3, and the second visits
1,2,3. Their union visits all four base vertices. For every i and g in
Q64 there is consequently a length-three walk

    (i,g) -> ... -> (i,g*c).

The endpoints are distinct because c is nonidentity. This proves
d((i,g),(i,g*c))<=3 for all 256 vertices, whenever the parameters define
a legal graph. Left multiplication translates the four representative
walks to all vertices. This argument uses centrality; it does not assume
that arbitrary noncentral triangle products remain unchanged on rotation.

In particular, the four root-to-same-orbit quotient-identity slots each
contain both the empty-walk form 0 and a triangle form identically 1.
Those four slots are automatically fully covered for every center choice.
Other target slots remain unrestricted by this conclusion.

## 3. Projected voltages and the correct zero-bit baseline

Let q_e be the projection of h_e to D32. The dependent projections are

    q12 = q2^-1 * q7,
    q15 = q9^-1 * q11.

Fix arbitrary projected voltages on F. For an independent edge with
q_e=(a_e,p_e), take its baseline h_e^0=(a_e,p_e), using 0<=a_e<16.
Set the tree baselines to e and compute the other two baselines in Q64:

    h12^0 = (h2^0)^-1 * c * h7^0,
    h15^0 = (h9^0)^-1 * c * h11^0.

These dependent baselines need not be canonical representatives of
their quotient elements. Their central constants must be retained.
Replacing them afterwards by canonical representatives generally changes
the prescribed triangle products.

Let m_e be an eleven-bit vector. It is zero on tree edges, the appropriate
unit vector on independent edges, and

    m12 = m2 XOR m7,
    m15 = m9 XOR m11.

In the displayed free-edge order, their integer masks are 18 and 320.
For z in F2^11 every voltage is exactly

    h_e(z) = h_e^0 * c^(m_e dot z).

For example, centrality and c^-1=c give

    (h2^0*c^z2)^-1 * c * (h7^0*c^z7)
      = ((h2^0)^-1*c*h7^0) * c^(z2 XOR z7).

This proves the dependent masks, with no assumption that the canonical
section D32 -> Q64 is a homomorphism. Fixed independent projections have
exactly 2^11 center assignments satisfying the triangle constraints,
before imposing legality. No additional central coordinate is free.

## 4. Exact eleven-bit coverage condition

Enumerate the named-edge, nonbacktracking base walks of lengths 0 to 3.
Only an immediately reversed dart of the same named edge is cancelled;
different projected-parallel edges remain different. There are
1+8+56+392=457 such walks from each base root.

For a walk w, multiply the actual zero-bit Q64 baselines, using their
true inverses in reverse directions. If its projected endpoint is
(a_w,p_w), write the resulting product as

    value_w(0) = (a_w+16*beta_w,p_w),    0<=a_w<16.

Its center coefficient is the XOR of m_e over all edge occurrences.
Reverse traversal has the same coefficient, since
(h_e^0*c^t)^-1=(h_e^0)^-1*c^t. Thus

    ell_w(z) = beta_w XOR (M_w dot z),
    M_w = XOR_{edge occurrences in w} m_e.

There are 4*4*32=512 slots alpha=(source orbit,target orbit,a,p).
For each slot keep the distinct pairs (M_w,beta_w); call this set
F_alpha. Two identical affine forms are redundant; equal masks with
opposite constants must both be retained.

For a legal z, diameter at most three is equivalent to every slot's
evaluated values containing both bits. The exact four-root missing count
is

    M(z) = 2*N_empty
           + sum_{alpha: F_alpha nonempty}
               1[all forms in F_alpha evaluate equally at z].

The number of bad unordered vertex pairs is exactly 32*M(z), by the
simultaneous left Q64 action. This remains valid if the graph is
disconnected, counting unreachable targets as bad.

Choosing one form (M_0,beta_0) in a nonempty slot, its bad center choices
are the solutions of the affine GF2 system

    (M_w XOR M_0) dot z = beta_w XOR beta_0    for all other forms.

Consequently the full constrained problem is: find a legal z outside
the union of these bad affine solution sets, with no empty slot.
For a two-form slot its good condition is the complementary equation

    (M_1 XOR M_0) dot z = 1 XOR beta_1 XOR beta_0.

Larger slots generally require a disjunction, not an arbitrary selected
two-form equation. The prescribed triangles eliminate four specific
bad sets; they do not eliminate these other joint constraints.

## 5. Simplicity and the baseline-dependent legality equations

The base is loop-free. Its lift is simple and eight-regular precisely
when matchings in each endpoint class have distinct actual voltages.
Different projected voltages cannot coincide after lifting.

For each baseline write

    h_e^0 = (a_e+16*b_e,p_e),    0<=a_e<16, b_e in F2.

If two same-class projected voltages agree, equality of their actual
voltages is equality of their center bits. Distinctness is therefore
exactly

    (m_e XOR m_f) dot z = 1 XOR b_e XOR b_f.

The b_e terms are essential for dependent edges. This formula also
handles a tree edge, whose mask and baseline center bit are both zero.
Three matchings with the same projection cannot have three distinct
lifts; such a projected assignment is illegal for this family.

Unlike the unconstrained thirteen-bit model, the pair equations here
can share variables through m12 and m15. They need not be independent,
and absence of a triple collision alone does not prove consistency.
Combine all equations as E*z=f. If inconsistent, there is no legal lift.
If consistent of rank r, the legal space has dimension 11-r. Restrict
the coverage forms to this affine space for the exact legality-aware
coverage test. Repeated projected matchings are allowed when these
conditions hold; pre-excluding them would remove valid parameters.

## 6. Read-only membership check of the saved 832-bad-pair source

The input was [the saved source parameters](../nonabelian4_256_search/best.json),
using its encoding x+32*s. The relevant values are

    h2=(26,0), h12=(22,1), h7=(0,1),
    h9=(16,1), h15=(15,1), h11=(1,0).

Direct actual group multiplication gives

    h2*h12 = (16,1),     h7^-1 = (16,1),
    h2*h12*h7^-1 = (16,0),

    h9*h15 = (17,0),     h11^-1 = (31,0),
    h9*h15*h11^-1 = (16,0).

Thus this source belongs to the constrained family. Its independent
center bits in order F are

    [0,1,1,0,0,0,1,1,0,0,0],     integer mask 198.

Computing the dependent zero-bit baselines as above gives

    h12^0=(6,1),       h15^0=(31,1).

Both dependent masks evaluate to one at z=198, restoring h12=(22,1)
and h15=(15,1). In particular b15=1 in this baseline. Canonicalizing
h15^0 to (15,1) would flip the second triangle product and is incorrect.
The stored diameter-four and 832-bad-pair results were not recomputed.

## 7. Scope and boundary

The parameterization is complete for this fixed base, these edge IDs,
the identity tree gauge, and these two prescribed central triangles.
It is a subfamily of the full thirteen-free-voltage Q64 construction.
There is no proof that every D3 graph in the larger family must satisfy
these specific triangle equations: a central mate could be reached
through a different triangle or a two-edge route.

Tree gauge does not introduce an additional restriction within this
subfamily. Under h_ij -> k_i^-1*h_ij*k_j, a closed triangle product is
conjugated at its start; c is unchanged. The tree can therefore be
normalized to the identity while preserving both constraints.

The old source's membership supplies an actual starting point, not a
D3 construction. Any subsequent incomplete search concerns only its
explicit explored range; even exhaustive rejection of this constrained
family would not exclude all Q64 voltages or arbitrary 256-vertex graphs.
