# Complete paper-candidate dispatcher for 23 vertices and 34 edges

Let H be a finite simple five-uniform hypergraph on exactly23 vertices, with34 edges, covering every pair. Every vertex has degree at least6: its incident five-edges must cover22 other vertices and each covers at most4. Let r be the number of degree-six vertices. The following mutually exclusive branches cover every r.

| r | Actual selection and decisive argument | Complete candidate source |
|---:|---|---|
|0|At least14 sevens. Select six minimizing internal codegree excess. Exchange gives (r7-7)d_S+2W<=30. The max-degree3/W<=4 domain is strict. For max-degree2, W6 forces two K7 components and a unit eight-degree extension; W2/3/4 admit an average-controlled seventh seven-degree extension. All local alternatives strict.|`N23_MIN_SEVEN.md`|
|1|At least10 common-unit sevens relative to the sole low. Every five has residual graph2K2+I, K3+2I, or K3+K2. Thus the whole graph has at most3 clique components of size at most3, contradicting10 vertices.|`../middle-math/CANDIDATE_ONE_TWO_LOW_23.md`|
|2|At least6 common-unit sevens relative to both lows. Choose5; the complete seven-lock promotion/projection domain has one final type, with bound1741/2002.|`../middle-math/CANDIDATE_ONE_TWO_LOW_23.md`|
|3|At least8 common-unit vertices of degree7/8, including at least2 sevens. Choose4 including2 sevens. Complete seven-lock domain has10 final types, all strict, maximum11381/11440.|`../high-math/CANDIDATE_THREE_LOW_23.md`|
|4|A fixed four-low set has at least5 common-unit7/8 vertices. Every residual triple must have degrees(7,8,8). Four members would force3k=4, contradiction.|`../middle-math/CANDIDATE_FOUR_FIVE_LOW_23.md`|
|5|Every low-low pair is forced unit. Select4 lows and3 common-unit7/8 vertices, then append the actual fifth low. All63 final profiles are strict, maximum4707/5005.|`../middle-math/CANDIDATE_FOUR_FIVE_LOW_23.md`|
|6|The only six-low residual is the two-triple trace type. Among at least10 external degree7/8 vertices, one consumes at most1 unit of total low-codegree excess. All36 corresponding mixed profiles are strict.|`../middle-math/CANDIDATE_LOW_BRANCHES.md`|
|>=7|Every six-low subset would have the unique residual. The complete seven-low promotion has no input with all six-projections residual, contradiction.|`../middle-math/CANDIDATE_LOW_BRANCHES.md`|

Each branch is now a complete paper candidate with local exact certificates and an explicit actual-vertex selection argument. The r=0 branch's2668 pure and176 joint retained certificates have independent exact replay. The r=3 branch has complete promotion/projection regeneration and original-profile binding audit in `../high-math/V23_THREE_LOW_COVERAGE_AUDIT.json`. Root owns the corresponding current audits for the other rows and the cross-family review records.

The checked selection/coverage reasoning of the other rows is recorded in `MIDDLE_SELECTION_REVIEW.md` (same-family/provisional). This dispatcher does not assert a23-point Lean theorem, completion of the overall T34 Goal, or independent human/machine reproduction.

For formalization, the root caller should accept only the actual23-point pair-covering H with34 edges, derive degree>=6, define the actual six-degree set, and branch on its cardinality. A caller that instead receives a local profile or probability certificate as an extra premise would leave the intended theorem incomplete. The global reduction from arbitrary original H with at most34 edges remains the existing T34 assembly obligation; it is distinct from the complete23-point structural dispatcher above.
