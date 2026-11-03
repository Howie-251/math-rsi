# Independent paper check: the one mixed-copy/cycle/sigma model at cap 31

2026-11-01. **The stated joint six-helper interface is sound and exact for this fixed G0 and fixed K6. No paper obstruction or missing short-route class was found. Final feasibility remains unknown here.** This is a same-family, paper-only mechanism review, not fresh acceptance of a 10076-vertex graph, a solver result, a Lean result, or an external review.

Inputs read: `PREDICTION_AND_SCOPE.md`, `solver_once.py`, `run_milp_once.py`, the head of the saved sigma metadata, and the producer's actual `RESULT.json`, `NEW_B_CUBE_CHECK.json`, and `TERMINAL.json`. No graph, CSR/NPZ, old field, old geometry, old B-radius/Steiner table, BFS, solver, or Lean module was read or executed. The project proof-checker discipline was restricted to the explicitly requested paper interface; its broader review/render/wiki/hash workflow was not run.

## 1. The old-old D3 inheritance needs synchronized walks, and has the right interface

It would be insufficient merely to know that each factor has diameter at most three: product routes require the same length in both coordinates. Here the inherited looped relation A satisfies A^3=4A+J, and the newly produced receipt reports the actual saved looped relation B^3=16B+J, all 342225 ordered entries checked with zero mismatches. I did not repeat either check.

Consequently every entry of (A tensor B)^3=A^3 tensor B^3 is positive. Thus any two original product vertices have a relation-walk of length three. Removing a self-loop step from that walk leaves a genuine walk of length at most three in the simple source S. This supplies the original 8775 old vertices' D3 property without a product-parity gap. The new B-cube check is a necessary discharged input to this particular proof, rather than another old source BFS.

Each new class representative has the complete **open neighborhood in S** of its based source center. This is degree 26; the looped Cartesian relation row has size 27 and must not be substituted for it. For a clone and an original source vertex other than its center, replace the first endpoint of a source shortest path by the clone. To its own center use any of the 26 common neighbors, giving length two. Two clones of the same center also share those neighbors. For distinct centers at source distance two or three, replace both endpoints of a source shortest path. If two centers were adjacent, the general replacement route is clone(c)-d-c-clone(d), of length three. In the present absolute-product code the distinct centers are independent, but that stronger fact is not needed for the general full-N inheritance.

These paths have only original S vertices as interior vertices. Omitting five copies creates no missing internal route: copies were never needed as interiors. Arbitrary nonuniform copy multiplicities, and every prefix of those **copy additions**, preserve old-old D3. The later cycle/sigma edges can only add routes. This statement is different from a prefix claim about the six helpers.

## 2. Cycles, sigma, and the actual degree ledger are consistent

There are 325 based classes. The five classes over the fixed absolute column b0 have four present representatives each (original plus three clones); the other 320 have five each (original plus four clones). Thus there are 1295 new clones and 1620 representatives F. The mandatory graph has

    n = 8775 + 1295 = 10070,
    m = 118300 + 1295*26 = 151970.

The 4/5-cycles are simple cycles inside individual classes, so contribute one edge per representative, 1620 edges, and degree two at every representative. The saved sigma fixes b0 and pairs the other 64 absolute columns. Its matching preserves the representative index; those 64 columns all have the full index range, so the five omissions do not produce unmatched endpoints. At b0 no sigma edge is added. Away from b0 the 1600 representatives are paired, giving 800 edges and degree one. Cycle edges are within classes, matching edges are between different classes, and all are F-F while mandatory edges are F-U, so these edge families do not overlap. Sigma's old order-two/edge-preservation checks are inherited; this review did not recompute them.

The resulting ledger is exactly

| vertex kind | count | degree in G0 | spare to 31 |
| --- | ---: | ---: | ---: |
| representatives over b0 | 20 | 28 | 3 |
| other representatives | 1600 | 29 | 2 |
| old U in the five omitted classes' disjoint N sets | 130 | 30 | 1 |
| remaining old U | 8320 | 31 | 0 |

The 130 freed vertices are distinct because the five mandatory N sets are disjoint and each has size 26. Therefore P has exactly 1750 vertices, and G0 has 154390 edges. These numerical quantities also agree with the producer's actual closed receipts; agreement is not a new independent literal graph check. In particular, the 8320 saturated old U vertices cannot be added to the pin pool while retaining all G0 edges at cap 31. The newly freed 130 old U vertices are precisely the interface change that invalidates the earlier uniform-saturation exclusions.

## 3. The stated coverage constraint is both sufficient and necessary

Let K be the final graph formed by retaining G0, adding helpers H=K6, and adding only the selected helper-to-P pin edges. Write closed balls in the **complete actual G0**, including the prescribed cycles and sigma matching. For an old target v and helper h,

    dist_K(h,v) <= 3

is equivalent to

    [some own pin lies in closed B2_G0(v)]
    OR [some other helper's pin lies in closed B1_G0(v)].

Sufficiency is immediate from h-u-(at most two G0 edges)-v and h-g-u-(at most one G0 edge)-v. Closed balls are essential: v itself may be a pin, and routes shorter than the maximum must count.

For necessity take a shortest path of length at most three. If h is its only helper, its first edge reaches an own pin and the remaining suffix uses at most two G0 edges. If its first step is another helper g, there is at most one G0 edge after g's pin, unless there is yet another helper; because H is a clique, h can then jump directly to the last helper and shorten that route. The remaining apparent mixed type h-u-g-v, with an old pin u followed by another helper g, similarly shortens to h-g-v. If g=h the repeated-vertex walk shortens further. Thus interleaving old pins and helpers introduces no uncovered three-step case. This reduction uses the fixed complete helper graph; it must not be transferred unchanged to a nonclique controller.

The binary inequality in the prediction is exactly this disjunction. The old endpoint constraints sum_h x[h,u] <= 31-deg_G0(u), and each helper has fixed degree 5 plus at most 26 pins. They are exactly the cap constraints for the permitted new edge types. Shared pin vertices are permitted up to their actual spare degree; no unjustified global pin-disjointness restriction is imposed.

The read-only solver inspection agrees with this interface: it makes one coverage row for every (v,h), v=0,...,10069, not just original S vertices or based classes. In particular all 1620 representatives, including all 1295 clones, really occur as individual old targets; so do the 130 newly freed U targets. Its `one` set contains eligible neighbors and the eligible target itself. Its `two` set adds eligible endpoints of every actual two-edge G0 walk. It includes all other five helpers' `one` sets. I did not run or load the prepared CSR to verify its literal binding; that remains a separate input/acceptance obligation.

The five weighted pin-sum ordering rows in the solver are harmless symmetry breaking: the six helpers have identical budgets, clique adjacency and target constraints. Every feasible solution can be relabeled to order those six scalar sums. The ordering neither fixes a particular pin nor imposes equal pin counts.

## 4. What a feasible solution would, and would not, prove

If the literal G0 binding and an actual binary pin assignment pass, the final graph has 10076 vertices and

    m_final = 154390 + 15 + total_pins = 154405 + total_pins,
    0 <= total_pins <= 156.

There is no single predetermined final edge count. Simplicity follows from binary old-to-distinct-new-helper pins, the simple retained G0 and the simple K6. The cap is at most 31, and is attained by the 8320 already saturated old U vertices regardless of pin choices. Old-old pairs use the retained source-interior proof; helper-helper pairs are adjacent; all new-old pairs are exactly the model rows above. Diameter at most three is therefore a full-pair conclusion, not a sample-BFS extrapolation. Diameter cannot be at most two because a degree-at-most-31 diameter-two graph has at most 1+31+31*30=962 vertices, below 10076. An actual distance-three pair from the planned new-helper BFS would be an additional concrete witness.

No claim follows for an ordering that adds the helpers singly while demanding D3 at every intermediate graph: a root h may need a pin owned by a helper g not yet present. The exact model is for the joint six-helper graph, as the prediction already states. It is appropriate to require final joint D3 and final degrees, and inappropriate to add a single-helper-prefix requirement that was not part of this rule.

The solver is only one bounded experiment. A numerical infeasible return applies only to this exact G0, hole set, cycle/sigma rule, pin pool and K6; UNKNOWN proves no exclusion. A feasible model assignment still requires a complete literal final graph and fresh mathematical acceptance, including ordinary BFS from the six new helpers and exact pin/degree/binding checks. The scoped published 10075 comparison and exact global priority UNKNOWN remain unchanged. No other omission pattern, peer rule, helper controller or parameter has been tested or excluded by this note.

## Disposition

Proceed with the already authorized single bounded exact joint model. No change of the connection rule, extra run, extra validation or graph count is warranted by this paper review. Producer receipts have discharged the newly needed synchronized B-three-walk input; feasibility itself is left to the actual one-shot solver and, if successful, fresh graph acceptance.
