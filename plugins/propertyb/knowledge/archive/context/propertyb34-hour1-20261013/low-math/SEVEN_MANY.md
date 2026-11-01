# T34 on 20 vertices: at least three degree-seven vertices

2026-10-13 first-hour sprint. Complete paper candidate for the stated subbranch; no new Lean result.

## Target, assumptions, and invariant object

H is simple, pair-covering, 5-uniform, with 20 vertices and exactly 34 edges. Assume minimum degree seven and let r be the number of degree-seven vertices. This note proves a candidate Property B argument when r≥3, using the same `sum min(A,B,C-D)<1` invariant and existing locked-permutation lemmas.

## Derivation strategy and map

First use a good double or triple if it exists. If none exists, the codegrees on the remaining low vertices become highly constrained; a short four-lock classification then suffices.

1. A unit pair of seven-degree vertices already passes.
2. A pair of degrees (7,7) or (7,8) with codegree at least four passes.
3. Three degree-seven points, all pair codegrees in {2,3}, pass whenever at least one codegree is three.
4. The residual seven-degree set has every codegree exactly two. Four such points pass all actual trace profiles. If there are exactly three seven-degree points, one suitably constrained eight-degree point supplies the fourth lock.

## Main derivation

### r≥4

If some pair of seven-degree points has codegree one, use bound `23877/24310`. If some such pair has codegree at least four, the strong double rows in `SEVEN_MANY_VERIFIED.json` pass. Otherwise every codegree on the seven-degree set is two or three.

If any pair has codegree three, choose a third seven-degree point. The sorted pair-codegree triples are (2,2,3), (2,3,3), or (3,3,3); for each possible triple multiplicity `0≤t≤min(λ12,λ13,λ23)`, the recorded three-lock bound is strict. Thus the remaining case has every pair codegree exactly two.

Choose any four degree-seven points. Let q be the four-point trace multiplicity and let t_123,t_124,t_134,t_234 be their exact three-point trace multiplicities. Necessarily `0≤q≤2`; for each pair ij the residual exact pair trace is

`l_ij = 2-q-sum_(T contains ij) t_T ≥ 0`.

Each singleton trace is `7-sum_(S contains i, |S|≥2) l_S`, and the empty trace is 34 minus all nonempty counts. These formulas recover every actual input. The nonnegative domain has 26 labelled profiles: 20 with q=0, five with q=1, one with q=2. All have strict probability witnesses; the largest reported bound is `63/65`.

### r=3

The same good-pair/three-lock alternatives reduce to all three seven-degree points having mutual codegree two. The other 17 vertices have degree at least eight. The degree sum baseline is `3*7+17*8=157`, leaving 13 extra incidences. Hence at least `17-13=4` points have degree exactly eight.

Choose any degree-eight point z. A codegree of at least four between z and a seven-degree point is already a strict double case. Thus all three codegrees from z to the seven-degree set lie in {1,2,3}.

If any of these codegrees is three, choose a second seven-degree point: all (7,7,8) triple profiles with seven-seven codegree two and at least one of the other two codegrees three have strict witnesses. If two of the three codegrees differ as one and two, choosing those two seven-degree points likewise gives a strict (7,7,8) triple for every admissible triple multiplicity.

Therefore, in the residual case, z has either codegree one with all three seven-degree points or codegree two with all three. Take the three sevens and z as four locks. The same inclusion-exclusion recovery of exact traces gives eleven labelled profiles in the first case and 26 in the second. Every one passes a strict bound in `QUAD_MIXED.json`, independently recomputed in `SEVEN_MANY_VERIFIED.json`.

## Verification and interpretation

`verify_seven_many.py` re-evaluated the 136 retained double/triple/four-lock witnesses used by this derivation (including a few harmless supersets of required triple cases). Every A/B/C row matched the independent labelled-injection implementation. Every bound was strict; the maximum over this retained verification list is `12107/12155`.

The four-lock classification is an exact local trace domain from actual degrees and codegrees, not enumeration of 20-vertex hypergraphs. Its coverage argument is given above. Negative counts are excluded because actual trace counts cannot be negative. No assumption is made that every retained local profile extends to H.

## Boundaries and non-claims

Minimum degree seven with r=1 or r=2 remains open here. Minimum degree eight is also open. The newly derived local domain and the actual input connections are not yet formalized; paper coverage plus exact arithmetic is not reported as a Lean theorem or completion of T34.

## Status and open risks

COHERENT AS STATED for this paper candidate. The remaining work on this subbranch is formalization and review of the stated selection/classification/deduction connections. Its restricted r≥3 hypothesis is essential to this note and has not been dropped.
