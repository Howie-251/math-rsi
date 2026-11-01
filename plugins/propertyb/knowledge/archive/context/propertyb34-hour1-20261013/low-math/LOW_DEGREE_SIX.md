# T34 on 20 vertices: minimum degree five or six

2026-10-13, first-hour sprint. This is a complete paper candidate for these two degree branches, using the existing locked-permutation probability and nested bad-link quota lemmas. It is not a Lean result or all of the 20-vertex branch.

## Target and invariant object

Let H be a simple pair-covering 5-uniform hypergraph on 20 vertices, with exactly 34 edges. Prove Property B when its minimum degree δ is 5 or 6. The controlled quantity is the usual upper bound `U = sum_k min(A_k,B_k,C_k-D_k)` on greedy-coloring failure, conditional on the selected lock positions.

## Assumptions and notation

Degree is d(x); codegree is λ(x,y). Pair covering gives λ≥1 and total degree is 170. At a vertex x,

`sum_(y≠x) (λ(x,y)-1) = 4d(x)-19`.

A unit neighbor has λ=1. Its complement has size at most this codegree excess, so there are at least `38-4d(x)` unit neighbors.

## Derivation map

1. Use actual degree and codegree budgets to select one of 17 explicitly listed double-lock profiles.
2. Recover exact edge-trace counts from the two degrees and their codegree.
3. Apply existing probability/link lemmas and the exact rational witness for that profile.
4. The strict bound below one supplies a valid coloring.

## Main derivation

### δ=5

Choose a five-degree vertex x. It has at least 18 unit neighbors. If all those vertices had degree at least 9, the degree sum would be at least `5 + 18*9 + 5 = 172`, since every remaining vertex has degree at least 5. This contradicts 170. Thus x has a unit neighbor y of degree 5, 6, 7, or 8.

At lock positions (10,11), the four respective bounds are

|Degrees|Codegree|Bound|
|---|---|---|
|(5,5)|1|4457/4862|
|(5,6)|1|22557/24310|
|(5,7)|1|23081/24310|
|(5,8)|1|4721/4862|

All are strictly below one.

### δ=6

Choose a six-degree vertex x. If another vertex y has degree 6 or 7, use this pair, with arbitrary actual codegree `1≤λ≤6`. All twelve possible profiles have strict witnesses in the table below.

Otherwise x is the unique six-degree vertex and all other 19 vertices have degree at least 8. Their total degree is 164, whereas the baseline is `19*8=152`. At most 12 of them can have degree at least 9; hence at least 7 have degree exactly 8. The codegree excess at x is `24-19=5`, so at most 5 other vertices can be nonunit neighbors. At least one of the seven eight-degree points therefore has codegree one with x. This gives the additional profile (6,8,λ=1), with bound `23877/24310<1`.

|Degrees|Codegree|Positions assigned in degree order|Bound|
|---|---|---|---|
|(6,6)|1|(10,11)|22829/24310|
|(6,6)|2|(10,11)|11709/12155|
|(6,6)|3|(10,11)|277/286|
|(6,6)|4|(1,11)|67583/72930|
|(6,6)|5|(1,11)|380381/437580|
|(6,6)|6|(1,11)|88879/109395|
|(6,7)|1|(10,11)|2123/2210|
|(6,7)|2|(10,11)|23921/24310|
|(6,7)|3|(11,1)|16483/16830|
|(6,7)|4|(11,1)|406213/437580|
|(6,7)|5|(11,1)|10586/12155|
|(6,7)|6|(11,1)|356231/437580|
|(6,8)|1|(10,11)|23877/24310|

For arbitrary degrees a,b and codegree c the exact trace counts are `l_empty=34-a-b+c`, `l_x=a-c`, `l_y=b-c`, `l_xy=c`. Thus every actual input selected above maps into the recorded domain.

## Numerical verification and scope

`verify_low.py` reruns all 17 retained witnesses and independently compares every A/B/C row to the labelled-injection implementation. The output is `LOW_DEGREE_SIX_VERIFIED.json`; every independent comparison passed. Deductions use the existing `pure_quota.certificate` nested pure/total allocation and the established counting lemmas. This second calculation verifies the probability-formula arithmetic, not a new independent proof of those lemmas.

The unit (6,9) residual from the first feasibility round has been eliminated by stronger selection, without improving its failing bound. Minimum degrees 7 and 8 remain separate obligations. The full T34 theorem and Lean assembly remain open.

## Status

COHERENT AS STATED at paper-candidate level. The mathematical selection is complete for δ=5,6 and the numerical witnesses are exact and independently checked for A/B/C. New formalization, actual-H assembly, and final cross-model review are not claimed here.
