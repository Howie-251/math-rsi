# Paper check: six own-radius-two covers on the dispersed freed-U130 pool

2026-11-01. **The reduction and individual-helper-prefix claim are valid in their stated own-cover scope.** No paper obstruction to the authorized one-shot model was found. This does not predict a feasible coloring. It is a paper-only same-family interface check, not a graph/CSR validation, numerical result, Lean proof or external review.

I read `PREDICTION_AND_SCOPE.md` and the producer's actual `RESULT.json`, `TERMINAL.json`, and `PROOF.md`. I did not read the source/G0 edge tables, NPZ/CSR, old B adjacency or R2/Steiner data, or run a source/cube/field/geometry/BFS/solver/Lean/review experiment. The prior exact same-column rule remains closed by its separate integer proof; its numerical UNKNOWN, LP witness and refuted initial prediction are unchanged.

## 1. The changed base and degree ledger

The selected holes are exactly copy4 at (a,b_a), a=0,...,4, with b_a=73,138,204,269,334. The base retains the original source S and all complete open-S-neighborhood copies other than those five. Nonuniform omission does not remove any source-interior walk: old-old D3 still follows from the inherited synchronized factor-three-walk proof and the full-neighborhood-clone endpoint replacement argument. Copy cycles and sigma peers add edges and preserve those walks.

All five missing representatives are away from sigma's fixed absolute column zero. Each removes one occurrence of the same-copy sigma matching. The present copy cycles contribute 1620 edges, and the matching contributes 800-5=795. Thus the paper counts are n=10070, mandatory m=151970 and complete G0 m=154385. The actual producer receipts report these counts and all source edges retained, without repeating the source cube or geometry checks.

There are 25 present representatives over the fixed column zero, all without a sigma match. Five other present representatives are the unmatched copy4 partners of the five omitted representatives. These 30 F vertices have degree 28; the other 1590 F vertices have degree 29. The five disjoint omitted mandatory neighborhoods free 130 old U points, now degree 30, while the other 8320 old U points have degree 31. This matches the producer's actual degree histogram.

The unrestricted eligible pool has 1750 vertices. The input to this particular model intentionally contains only the 130 freed original U points, each of spare degree one. The other 1620 eligible F points are excluded. A future model or receipt must preserve this distinction; `pool130` is a deliberate restriction rather than the whole eligible set.

Producer `TERMINAL.json` reports the base closed in 0.380094 CPU seconds, within its 15-second budget. It reports no new group-reach check. The prediction that the 120 nonabsolute-column U pins reach at least five old projection groups, and the other ten reach one, is therefore **not yet tested by that receipt**. Root's once-only actual mask preparation is the proper place to test it. That routing prediction is not a premise needed for validity of the exact mask formulation.

## 2. Exactly-one-color is without loss for six disjoint own covers

Let P be the 130-point restricted pool. Suppose six mutually disjoint own-cover sets S_h subset P already exist, with |S_h|<=26. Write q=sum_h |S_h|. There are 130-q unused pins and aggregate free helper pin capacity 156-q. Since 130-q<=156-q, assign each unused pin to any helper still below 26 until all are assigned. Such a helper always exists while an unused pin remains: otherwise the assigned total would already be 156, greater than 130. Adding pins preserves every cover and does not violate old endpoint degrees, because each point still belongs to exactly one helper and its spare degree is one.

Thus every feasible partial assignment of six disjoint own covers extends to an assignment in which every pin has exactly one color. Conversely an exactly-one-color assignment with each color class of size at most 26 and the required covers is plainly a feasible disjoint own-cover assignment. This argument depends on both endpoint capacity one and monotone coverage. It does not replace a general full-pool model that permits shared F endpoints.

The equivalence is for **own** covers. It does not assert that every U-only joint K6 completion has six own covers; a joint completion may instead use h-g-u-v through another helper's pin.

## 3. Target masks and safe reduction

For each of the 10070 old G0 vertices v use the exact closed mask

    E_v = P intersect closedB2_G0(v).

Undirectedness gives the precise equivalence

    v is within two G0 steps of S_h  iff  E_v intersects S_h.

Therefore requiring every E_v to contain every color is necessary and sufficient for six own-radius-two covers of **all** G0 vertices. This must include the original source vertices, every surviving clone and representative, and every freed U point. No orbit or based-class representative reduction is being presumed. Closed balls count an eligible target itself and all shorter routes.

Identical masks impose identical constraints and may be merged. If a retained mask E is a subset of E_v, a coloring that contains every color on E also does so on E_v. Removing supersets is consequently safe, provided every old target is linked to an actual retained mask E subset E_v. A chain ending at a retained minimal mask is sufficient, but the saved per-target witness should make that endpoint and its subset relation explicit. Because retained masks are actual target masks, the converse implication also holds: covering every original mask covers every retained one. Thus this antichain reduction is exact, not merely a necessary relaxation.

A mask of size less than six immediately refutes this own-cover coloring: disjoint color classes cannot supply six colors on fewer than six pins. It is not an exclusion for the full F-enabled pin model, nor necessarily for U-only joint completions.

## 4. Color symmetry and optional max-load objective

In any feasible coloring every target mask, including a fixed chosen mask, contains all six colors. Scan that chosen mask in a fixed pin order and relabel colors by their first occurrence. The resulting restricted-growth order has labels 0, then 1 when first new, and so on through 5. A simultaneous permutation of helper colors preserves every coverage constraint, endpoint assignment and equal color budget. Therefore this symmetry restriction selects at least one representative of every feasible helper-permutation orbit.

This justifies one consistent first-occurrence rule on that chosen mask. It does not justify combining it with an unrelated pin-count sort, independent color-label fixing on another mask, or another order that might select a different incompatible permutation. If a max-load variable z is used, constraints |S_h|<=z<=26 and minimization of z do not change feasibility: any feasible assignment can take z=26. An incumbent suffices for construction; a timed-out optimization does not justify an optimality or infeasibility claim.

## 5. The complete candidate and every helper prefix

Given an actual validated coloring, add six helpers forming K6 and connect h to S_h. All 130 freed U points are used exactly once. Therefore

    n_final = 10070+6 = 10076,
    m_final = 154385+15+130 = 154530.

Every one of the 8450 old U vertices then has degree 31. F degrees stay 28 or 29. Helper h has degree 5+|S_h|<=31, so the cap is attained and not merely bounded.

For old-old pairs keep the inherited G0 source-interior walks. For helper h and old v choose an own pin u in S_h intersect E_v; the path h-u followed by at most two G0 edges reaches v within three. Helper-helper pairs are adjacent. These are full-pair statements from actual masks and pins; they are not inferred from selected BFS roots.

For a prefix containing any first t complete helpers, retain G0 and include each present helper's entire S_h pin set and all edges between present helpers. The same own-pin paths remain available because all their interior vertices belong to the fixed G0. Old endpoint loads are still at most one. A present helper has degree |S_h|+(t-1)<=26+5=31. Thus every such complete-helper prefix has diameter at most three and respects the cap. The claim does not require the graph to satisfy D3 in the middle of adding that helper's individual pin edges. It is stronger than the earlier joint-only interface precisely because the selected own covers never need a future helper.

A final simple graph of order 10076 and maximum degree 31 cannot have diameter at most two, whose Moore bound is 1+31+31*30=962. Fresh acceptance should nevertheless retain the planned actual new-helper BFS distance-three witness and exact pin/degree/literal-graph checks. No full candidate or new-root BFS has been produced or accepted by this paper note.

## Scope and disposition

Proceed with the already authorized single exact coloring test on this actual dispersed base. This is not a continuation of the closed same-column integer model: the five omission neighborhoods and useful U transport changed. The older block argument cannot be imported merely from its numerical counts without deriving its premises for the new layout.

If this model is infeasible, the excluded scope is **this fixed layout, U130-only, six disjoint own-radius-two covers of size at most 26**. F-pin repairs remain open; so do U-only joint K6 completions that rely on other-helper B1 routes rather than own covers, other layouts and other helper rules. UNKNOWN excludes none of them. The located public comparison remains 10075 and exact priority UNKNOWN. This note changes no graph, parameter, Lean, root-state, Wiki, progress or frozen-packet count and starts no additional run. Paper task terminal.
