# T34: complete paper candidate for 21 vertices

2026-10-13. For an arbitrary simple pair-covering five-uniform H with 21 vertices and 34 edges, the minimum degree is at least five by pair coverage and at most eight by total degree 170. All four cases now have complete paper candidates:

| Minimum degree | Mathematical entrance |
|---|---|
|5|Frozen `context/propertyb34-hour1-20261013/low-math/TWENTYONE_FIVE_COMPLETE.md`|
|6, multiple six-degree points|`MULTIPLE_SIX.md`|
|6, unique six and no seven|`UNIQUE_SIX_NO_SEVEN.md`, including its frozen equality reduction|
|6, unique six and at least one seven|`SIX_WITH_SEVENS.md`|
|7, at least three sevens|`AT_LEAST_THREE_SEVENS.md`|
|7, exactly two sevens|`TWO_SEVENS.md`|
|7, exactly one seven|`UNIQUE_SEVEN.md`|
|8|`EIGHT.md`|

The reusable six-degree unit-set lemma is `SIX_UNIT_SET_LEMMA.md`; the seven-degree unit-set lemma is Section 1 of `TWO_SEVENS.md`. Actual-input connections are spelled out in each note. No branch assumes a profile certificate as an extra hypothesis: the paper argument selects real vertices and either obtains a strict earlier witness or proves the needed structural residue.

All retained new numerical witnesses have independent exact replays, using `verify_exact.py` for single layouts and `verify_joint.py` for common-actual-bad-vector mixtures. See `REPORT.md` for source maps and the branch-specific `_VERIFIED.json` files. Floating-point optimization only proposes rational certificates; finite formula checks and final inequalities use exact arithmetic.

This is a complete **paper candidate for the 21-point branch**, not a Lean theorem, not a full T34 theorem and not a claim that model reviewers have certified the material. Root owns cross-model review, wiki integration and future formalization. Required remaining work includes complete finite classification/actual trace transport, the mixed-layout inequality interface in Lean, assembly with the other point-count branches, and final audits.

The next mathematical assignment for this agent is 23 points with minimum degree at least seven, following the parent's updated priority.
