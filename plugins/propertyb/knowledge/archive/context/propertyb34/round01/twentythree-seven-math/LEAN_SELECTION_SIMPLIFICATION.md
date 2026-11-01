# Shorter actual six-lock selection for Lean

2026-10-13. This replaces two unnecessarily strong steps in the implementation plan, without changing the selected local domains or any probability certificate. New source: `formal/Aris4Math/ThirtyFour/WeightedSubsetSelection.lean` and `TwentyThreeSevenSelection.lean`. Build status is recorded separately; source existence is not verification.

Let L be the actual degree-seven vertices of a 23-point, 34-edge pair-covering five-uniform H with minimum degree seven. Then |L|=r≥14. Put w(x,x)=0 and w(x,y)=λ(x,y)−1 off the diagonal. Every x∈L has total weight six on all vertices. For S⊆L, |S|=6, define d_S(x)=Σ(y∈S)w(x,y) and E(S)=Σ(x∈S)d_S(x)=2W(S). Choose S of minimum E.

## The averaging identity can be omitted

The exact swap argument gives, for x∈S,

    (r−7)d_S(x)+E(S)≤30.

Symmetry gives E(S)≥2d_S(x). Since r−7≥7, d_S(x)≥4 is impossible. If some d_S(x)=3, then E≤9; E is even, so E≤8. Otherwise all six internal degrees are≤2 and E≤12. These are precisely the two domains used by the saved local classifications. There is no need to formalize averaging over all six-subsets.

## Only selected-vertex saturation is needed at W=6

Assume E=12. The same pointwise bound gives all d_S(x)≤2, hence all equal two. For y∈L\S, minimality gives

    d_S(y)≥2+w(x,y)   for every x∈S.

It first implies d_S(y)≥2. Equality at two would force every w(x,y)=0 and hence d_S(y)=0, a contradiction. Therefore every outside seven-degree point has d_S(y)≥3.

The cut weight C satisfies

    3(r−6) ≤ C ≤ 6·6−E = 24.

Together with r≥14 this forces r=14 and C=24. Thus Σ(x∈S)d_L(x)=E+C=36; since each of the six terms is≤6, each is exactly six. The full weight of x on all23 vertices is also six, so every selected x has weight zero to every vertex outside L.

The nine vertices outside L all have degree eight: each has degree≥8, and their total degree is 170−14·7=72. Choose any one y. It is distinct from S, has degree eight, and λ(x,y)=1 for every x∈S. This is exactly the actual seventh-lock input needed by `EQUALITY_SEVEN.json`.

It is unnecessary to prove that the entire weighted graph on L is two K7s. The saved local residual classification already identifies the 17 weight-six profiles on S; `equality_seven.py` appends a degree-eight vertex with unit codegrees, and assumes no other global graph condition. Its `partitions` routine splits old trace edges so each of the six old locks occurs exactly once with the new lock, using empty old traces for the remaining degree. Therefore the original 209 seven-lock profiles and strict certificates apply unchanged.

This simplification removes a global structural proof from the formal critical path. It does not remove local classification coverage, actual trace binding, or the original coloring conclusion.
