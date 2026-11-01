# T34 first-hour low-vertex research report

2026-10-13. Work began at approximately 09:14 UTC. This report records the completed mathematical candidates and the exact arithmetic already run in this subtask. All paths below are within the Property B project. Existing T32/T33 artifacts and Lean files were not modified by this agent.

## Main result

**The 20-vertex branch now has a complete paper candidate, and the entire minimum-degree-five branch on 21 vertices also has a complete paper candidate.** These are statements about simple, pair-covering five-uniform hypergraphs with exactly 34 edges. They are internal branches of the proposed T34 proof, not a proof of all T34 and not new Lean completion.

The candidates combine actual degree/codegree selection, exact local trace classification, existing locked-permutation inequalities, independently recomputed rational witnesses, and general incidence contradictions that eliminate the remaining local types. The work did not enumerate hypergraphs on 20 or 21 vertices.

## Candidate map and actual scope

|Branch|Mathematical candidate entry|Numerical verification|
|---|---|---|
|20 points, minimum degree 5 or 6|[LOW_DEGREE_SIX.md](LOW_DEGREE_SIX.md)|`LOW_DEGREE_SIX_VERIFIED.json`: 17 strict witnesses|
|20 points, minimum degree 7, at least three sevens|[SEVEN_MANY.md](SEVEN_MANY.md)|`SEVEN_MANY_VERIFIED.json`: 136 strict witnesses|
|20 points, minimum degree 7, exactly two sevens|[SEVEN_TWO.md](SEVEN_TWO.md)|`SEVEN_TWO_VERIFIED.json`: 222 strict witnesses and one residual profile eliminated by actual edge capacity|
|20 points, minimum degree 7, exactly one seven|[SEVEN_ONE.md](SEVEN_ONE.md)|`SEVEN_ONE_VERIFIED.json`: 674 local profiles, 445 retained strict witnesses, six residual orbits eliminated by a partition/incidence argument|
|20 points, minimum degree 8|[EIGHT.md](EIGHT.md)|`EIGHT_VERIFIED.json`: 12,103 local profiles, 976 after triple elimination, 95 four-lock orbits, 98 strict witnesses including doubles/triples, sixteen residual orbits eliminated by a general graph/incidence argument|
|21 points, minimum degree 5|[TWENTYONE_FIVE_COMPLETE.md](TWENTYONE_FIVE_COMPLETE.md)|`TWENTYONE_FIVE_VERIFIED.json`: 169 strict witnesses; the remaining explicitly listed local profiles are eliminated by actual incidence counting|
|21 points, unique six/no sevens: partial reduction|[TWENTYONE_SIX_REDUCTION.md](TWENTYONE_SIX_REDUCTION.md)|`TWENTYONE_SIX_REDUCTION_VERIFIED.json`: exact witnesses reduce this subbranch to a specific equality structure; it remains open|

These witness counts belong to different verification lists and overlap. They should not be summed into a count of distinct mathematical cases or percentage progress. Pair covering and degree sum 170 give 5≤δ≤8 on 20 points, so the first five entries cover that complete internal branch.

## What changed relative to the feasibility pilot

The pilot's six failed unit-double inputs on 20 points were a limitation of that selection rule. The new proof does not need to make each of those bounds strict. For minimum degree six, stronger selection avoids the problematic (6,9) input. For minimum degree seven, three/four locks and actual-H incidence constraints eliminate the stubborn local types. For minimum degree eight, an exact residual unit graph is rigid enough to yield a contradiction without enumerating all unit graphs.

The old 21-point (5,8,8) unit triple was checked at all 3,990 distinct placements after identifying the interchangeable eight-degree labels. Its best bound is still `44215/43758>1`; the entire old placement-only route is exhausted for the specified nested pure/total bound. Adding an actual fourth low-degree lock succeeds by forcing residual capacities, rather than by searching still more positions for the same triple.

## Mathematical mechanism worth reusing

The most productive pattern was:

1. Compute a small exact table only for inputs that actual degree/codegree arguments can produce.
2. Keep every type whose bound remains ≥1; do not attempt to hide or average it away.
3. Ask what it would mean if **every selectable lock set** of the relevant kind had one of these residual types.
4. Transfer those local restrictions back to actual edges, then double-count degrees/pairs or use a small forbidden-induced-graph argument.

This universal use of the residual table was decisive. On 20 points with one seven-degree point, it forced a partition of at least eight eight-degree points into two impossible incidence patterns. With all degrees at least eight, it forced a triangle-free unit graph excluding 2K2 and P3+P1. The exceptional C4 had an actual common edge, and unit-codegree uniqueness linked two such C4 witnesses; the induced-claw zero-trace condition then excluded three common neighbors. The final contradiction is a general graph/counting proof, not a scan of r-vertex graphs.

The equality case in the star argument is essential. Nine leaves with pair codegree two saturate `sum C(j,2)≤sum j`; every nonempty leaf trace must then have exactly three points, contradicting the zero four-trace for the center plus three leaves. This is written explicitly in EIGHT.md.

## Verification actually performed

Every file ending in `_VERIFIED.json` was generated by an executed `verify_*.py` script. Retained A/B/C rows are compared with the separate labelled-injection implementation in `computations/independent_structure_bounds.py`. Bounds and margins use Python `Fraction`.

Pure/total deductions use the already established nested quota allocation. For the new avoided-lock refinements, the verifier independently recomputes each subfamily quota, nonnegative rational multiplier, actual pair-type capacity, two-direction weight, and capacity penalty. The numerical LP only proposes multipliers. Neither floating optimality nor solver success is used as a mathematical premise.

The local classification coverage is checked from exact trace-recovery formulas, and the largest degree-eight domain is bound back to all stored permutation orbits. These checks do not reprove the original probability lemmas, nor replace the eventual Lean input-to-certificate connection. `PROFILE_BINDING_CHECK.json` separately confirms that the first six retained verification lists contain 34 total edges per profile, the advertised degree vector and distinct lock positions, and a strict exact row-sum bound.

## Reproduction

From the project root, run each of:

```text
python3 context/propertyb34-hour1-20261013/low-math/verify_low.py
python3 context/propertyb34-hour1-20261013/low-math/verify_seven_many.py
python3 context/propertyb34-hour1-20261013/low-math/verify_seven_two.py
python3 context/propertyb34-hour1-20261013/low-math/verify_seven_one.py
python3 context/propertyb34-hour1-20261013/low-math/verify_eight.py
python3 context/propertyb34-hour1-20261013/low-math/verify_twentyone_five.py
```

These verification scripts do not require SciPy: they check saved rational multipliers and formulas directly. Generating new dual proposals uses the already installed `.tools/math-python/bin/python`, which has SciPy. No new package was installed. Individual verification runtimes observed in this run were approximately 0.3–4.3 seconds; this says nothing about future Lean compile time.

## Failed routes and their exact boundaries

|Diagnostic|What was checked|Result and reuse condition|
|---|---|---|
|Old (5,8,8) on 21 points|All 3,990 distinct placements, fixed nested pure/total bound|Best `44215/43758`; no more placement search under that same bound. Reuse only with stronger actual information or a different probability estimate.|
|Five locks (7,7,8,8,8) on 20 points|41 profiles under the proposed restricted pair-codegree pattern; four contiguous windows and all labels|Some pure/dual bounds remained ≥1. Superseded by the shorter four-lock residual-to-incidence proof in SEVEN_TWO.md; no need to formalize this failed route.|
|Four-lock preliminary unique-seven scan|674 profiles with pair codegrees 1/2|Initial pure bounds left more failures; avoided-lock duals and a few different positions reduced them to six residual orbits. The intermediate nine-orbit file is superseded by SEVEN_ONE_VERIFIED.json.|
|Five eight-degree locks around a four-trace|Seven small graph types; four windows and all labels|Empty-graph type still `718/715`; superseded because the corresponding four-lock common-edge case became strict under the dual. No need to add the fifth lock here.|
|21 minimum degree 6,7,8|A final short unique-six/no-seven diagnostic reduces that subbranch to degree sequence 6^1,8^16,9^4 with twelve unit eight-degree neighbors pairwise at codegree two|Still open, including this equality case. Do not extrapolate the degree-five result to the entire 21-point branch.|

## Remaining work

The new paper candidates need the designated Grok/Gemini reviews and full Lean actual-input connections. The root agent owns review scheduling and formal assembly; this report does not claim either review completed just because a file was sent.

Within this subtask, 21-point minimum degrees six, seven, and eight remain the next mathematical obligations. The final partial reduction `TWENTYONE_SIX_REDUCTION.md` supplies a concrete equality case for the unique-six/no-seven subbranch; it is deliberately not included among the completed candidates. A natural next step is to repeat the successful residual-domain method, beginning from the minimum-degree-six actual link budgets and a few low-degree locks. It should be guided by real selected profiles and short exact diagnostics, not a blind increase in the number of locks.

The whole T34 theorem additionally has other vertex branches and its original-input reduction/assembly. Their state is maintained by the root agent. No completed T32/T33 theorem has been changed, and this report does not claim m(5)≥35.
