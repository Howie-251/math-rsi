# Exact exterior-moment inequalities for a twelve-vertex D1 heavy component

## Statement and status

This new finite-inequality derivation is awaiting independent review. Assume an
actual legal order62 graph, a D1 heavy component H with |H|=12, and its generated
triangle component K. Use the proved component quotient and the moment lemmas
in `D1_COMPONENT_MINIMUM_SIZES.md`. Write k=|K|, a=r_HK, b=r_KH,
s=r_HH and t=r_KK. Then the following necessary list remains after the exact
separating inequalities below:

| k | a,b | Remaining (s,t) |
|---|---|---|
| 12 | 4,4 | (0,1), (1,0) |
| 16 | 4,3 | (0,0), (0,1), (0,2), (1,1), (1,2), (2,0), (2,1) |
| 20 | 5,3 | (0,2), (1,2) |
| 24 | 6,3 | (0,2) |
| 28 | 7,3 | none |

This list does not assert realizability. The separate component-size argument
may further remove entries; it is not assumed in this finite check. In particular
this result alone does not exclude |H|=12 or the whole D1 branch.

## Actual graph to finite inequalities

The preceding paper proves H≠K and the exact five possibilities for (k,a,b).
For each exterior vertex v put x=|N(v)∩H| and y=|N(v)∩K|. Both are nonnegative
integers and satisfy

    x+y≤8,   (s+1)x+b y≤12,   a x+(t+1)y≤k.

Let φ(x,y)=(1,x,y,x(x−1),y(y−1),xy). The sum over all exterior vertices is the
following exact integer vector:

    M = (50−k,
         12(8−s−a),
         k(8−t−b),
         12(14−s²−a(b−1)),
         k(k+2−t²−b(a−1)),
         12(k−a(s+t+1))).

These identities use actual degree and common-neighbor counting, not an LP
model assumption. All six entries must be nonnegative. Internal degrees also
satisfy 0≤s≤8−a and 0≤t≤8−b. The exact enumeration of these elementary bounds
has 33 cases. All other choices are already contradicted by a negative entry
or an invalid degree.

For each row of the table below, z is an integer coefficient vector satisfying
z·φ(x,y)≥0 at every integer point in the displayed domain. Nevertheless z·M
is the negative integer in the last column. Summing the pointwise inequality
over the actual exterior vertices gives the contradiction 0≤z·M<0.

| k | s | t | z in the order (1,x,y,x(x−1),y(y−1),xy) | z·M |
|---|---|---|---|---|
| 12 | 0 | 0 | 0, 0, 1, 1, 0, -1 | -24 |
| 12 | 1 | 1 | 2, -2, -2, 1, 1, 2 | -44 |
| 16 | 0 | 3 | 6, -4, -6, 1, 6, 6 | -108 |
| 16 | 1 | 0 | 0, 6, 0, -1, 0, -2 | -36 |
| 20 | 0 | 0 | 3, 3, 3, 3, -1, -3 | -98 |
| 20 | 0 | 1 | 0, 18, 18, -6, -6, -7 | -120 |
| 20 | 0 | 3 | 6, -4, -6, 1, 3, 6 | -96 |
| 20 | 1 | 0 | 36, 36, 36, -1, -15, -30 | -1092 |
| 20 | 1 | 1 | 0, 6, 0, -1, 0, -2 | -12 |
| 20 | 2 | 0 | 6, 6, -4, 6, 1, -2 | -68 |
| 20 | 2 | 1 | 12, -12, -6, 12, 1, 12 | -84 |
| 24 | 0 | 0 | 3, 3, 3, 3, -1, -3 | -330 |
| 24 | 0 | 1 | 12, 12, 12, 9, -5, -10 | -672 |
| 24 | 0 | 3 | 6, -4, -4, 1, 1, 6 | -60 |
| 24 | 1 | 0 | 9, 9, 9, 1, -3, -9 | -654 |
| 24 | 1 | 1 | 36, 36, 36, -1, -15, -30 | -948 |
| 24 | 1 | 2 | 12, -8, -6, 2, 1, 12 | -24 |
| 28 | 0 | 0 | 3, 3, 3, 3, -1, -3 | -570 |
| 28 | 0 | 1 | 3, 3, 3, 3, -1, -3 | -374 |
| 28 | 0 | 2 | 12, 12, 12, 12, -5, -10 | -544 |
| 28 | 0 | 3 | 6, -6, -4, 6, 1, 6 | -80 |

## Exact check and reproducibility

The table contains 21 excluded moment cases. The remaining 12 cases are exactly
those in the necessary list above. The standard-library checker
`computations/dd82/n62/check_component_exterior_separators.py` regenerates the
33-case domain, reconstructs every admissible integer (x,y), and checks each
separator and its negative target with integer arithmetic. Its completed output
is `computations/dd82/n62/component_exterior_separators_check.json`: 21 integer
separators, 334 pointwise evaluations, and exact coverage of all 33 cases.

The integer coefficient data are stored in
`computations/dd82/n62/component_exterior_moments.json`. The discovery driver
`component_exterior_moments.py` first used floating LP to find candidate
separators, then reconstructed and checked integer coefficients. Its 0.46-second
run used one pinned CPU. The proof's inequality check does not use LP feasibility,
floating tolerances, or a numerical infeasibility status. No claim is made that
a floating feasible vector lifts to even component sizes or to an original graph.

The finite checker is an ordinary exact computation, not a Lean theorem.
The original-graph moment derivation and its hypotheses remain explicit
mathematical dependencies; no certificate-to-Lean or complete order62 claim is
made here. No solver jobs remain running from this calculation.
