# Twenty-one vertices with a unique degree-seven point

2026-10-13. Complete paper candidate, not yet Lean. H is simple, pair-covering and five-uniform on 21 vertices, has 34 edges, and has minimum degree seven attained only at x. This note proves Property B for this branch.

The degree sum is 170. The baseline $7+20\cdot8=167$ leaves only three extra degrees, so at least seventeen points have degree eight. Let U be those with unit codegree to x. The total codegree excess at x is eight, hence at most eight points are nonunit neighbors, and |U|≥9.

The degree-seven unit-set lemma (Section 1 of `TWO_SEVENS.md`) applies: either a strict (7,8,8) or (7,8,8,8) witness supplies a coloring, or every U-pair has codegree two and each x-edge contains at most two U points. From now on assume the latter actual structure.

## 1. Two disjoint actual pairs

Each U point occurs in exactly one of the seven x-edges. If t of those edges contain two U points and s contain one, then $|U|=2t+s$ and $t+s\leq7$. Therefore $t\geq|U|-7\geq2$.

Choose two distinct x-edges containing two U points each, naming these pairs u1,u2 and u3,u4. The four points are distinct because every U point is unit to x. Choose a fifth point u5∈U outside the pairs. The x-edge containing u5 is distinct from the previous two, because those already contain the maximum two U points.

For the six locks (x,u1,u2,u3,u4,u5), degrees are (7,8,8,8,8,8). All x-to-U codegrees are one and all U-pair codegrees are two. The seven x-edges have the following exact traces on the five selected U points:

- one trace {u1,u2};
- one trace {u3,u4};
- one trace {u5};
- four empty traces.

This statement is forced by the actual x-edges and unit codegrees; it is not an assumed local certificate.

## 2. Five-lock projection constraints

Consider x and any four of the selected U points. At least one chosen x-pair remains complete. Up to permuting the four U labels, this is the domain where x,u1,u2 have common-edge multiplicity one, x-to-U codegrees are one, all U-pair codegrees are two, and no x-edge contains three selected U points.

The complete domain has 27 profiles. Four have strict mixed-layout certificates, using one common actual bad-pair count vector across layouts. Thus if no such witness has already supplied a coloring, every five-lock projection lies among the other 23 labelled profiles, considered up to permutation of the U labels. No failed numerical profile is claimed to exist globally.

## 3. The six-lock classification and strict bounds

Enumerate the exact traces on the five U locks with degrees eight, pair codegrees two, and 34 edges. Lift them to six locks by splitting off precisely the four x-trace classes in Section 1. In particular the old exact-pair counts for {u1,u2} and {u3,u4} must each be at least one, the old singleton count for u5 at least one, and the old empty count at least four. Exactly 316 five-U profiles admit this split.

Require each of the five projections containing x and four U locks to be among the 23 retained profiles from Section 2. This leaves 205 local profiles. Of these, 203 have strict single-layout witnesses. The other two have exact rational mixed-layout certificates with common bound

$$12812301167/12870000000<1.$$

For each actual input, either an earlier projection is already strict or its six-lock profile is in this complete 205-profile domain. A weighted average of layout-specific upper bounds below one guarantees some layout with its own failure probability below one. Hence H has a proper two-coloring.

## 4. Evidence

- `SEVEN_UNIT_FIVE.json` stores the 27 five-lock profiles and `SEVEN_UNIT_FIVE_STRICT_JOINT.json` the four strict certificates. The retained projection set consists precisely of the other 23 labels and their U-label permutations.
- `unique_seven_six.py` implements the exact split and all five projection constraints. `UNIQUE_SEVEN_SIX.json` records all 205 profiles and the 316-profile prefilter count.
- `UNIQUE_SEVEN_WITNESSES_VERIFIED.json` records independent A/B/C injection-count, quota/capacity, degree and edge-total checks for all 203 strict single-layout witnesses.
- `SEVEN_UNIT_FIVE_STRICT_JOINT_VERIFIED.json` and `UNIQUE_SEVEN_SIX_JOINT_VERIFIED.json` independently replay all six mixed-layout certificates, including pair weights, rational layout masses, shared avoided quotas and repaired dual capacities. `verify_unique_seven.log` records the actual runs.

The proof requires formal local-classification coverage and actual-profile transport in Lean. Together with `AT_LEAST_THREE_SEVENS.md` and `TWO_SEVENS.md`, this completes the paper candidate for minimum degree seven on 21 vertices. Minimum degree eight remains open.
