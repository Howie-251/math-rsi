# Coset-tower review: accepted content and rejected deductions

Two actual Antigravity calls completed in thread `a5a1aacb-40a0-4918-8858-8c2831630fa8`. Both receipts report `status=SUCCESS`, `model=gemini-3.8-flash-high`, `effort=high`, selected label `Gemini 3.8 Flash (High)`, effort source `cli_selected_model_variant`. This records the returned service metadata, not independent backend attestation. There is no running review call, no third call, no Grok review and no new Lean result.

Prompts and complete responses are retained as `m2_coset_tower_review_prompt_20261026.txt`, `m2_coset_tower_review_raw_20261026.json`, `m2_coset_tower_review_correction_prompt_20261026.txt`, and `m2_coset_tower_review_correction_raw_20261026.json`. Neither response is accepted as a whole.

## Accepted within the stated scope

The first response correctly checked the right-Cayley/left-action convention, transitivity on the three vertex layers, exact weighted three-root count, HH necessary condition, fixed-H/K scaling normalization, and the supplied all-involution branch exclusions. The second correctly accepted the exact head-root formulas already proved in `research/ddp/m2_coset_tower/HEAD_ROUTE_CRITERIA.md`. Independent existing-graph comparisons are in `HEAD_ROUTE_CHECK.md` and `.json`.

These opinions support review of the submitted derivations; the mathematical evidence is the derivation and actual independent checks. They do not certify later q98 or F64 results that were not part of the submitted material.

## First response: false ordinary-Cayley capacity bound, retracted

The first response claimed that targets unreachable through a head within five steps must lie in the ordinary leaf Cayley ball of radius five. It then asserted `(q−1)(d−1)^2 ≤ Moore_(d−1)(5)` and numerical bounds q≤11 for d4 and q≤31 for d5. The premise omits two-step within-block jumps. Its target count also fails to account for groups directly contacted by a source leaf, and its uniform group-pair edge bound fails over rings. Root rejected the proposed theorem and did not use it to select or exclude a search range.

A concrete counterexample already existed in the saved q41 graph. Leaf0→leaf2 has full distance5, leaf-only distance6 and shortest head-visiting distance6. The complete shortest path is

`0 → 247 → 516 → 207 → 822 → 2`,

with coordinates `(0,0) → (1,6) → (24,12) → (2,5) → block(2,0) → (2,0)`. Vertex516 is **(24,12)**; the second response's `(24,19)` is a transcription error. Of751 leaves at full distance≤5,172 have a five-step head shortcut and579 do not;235 of those579 are outside the pure leaf radius5 ball. “579” is not asserted to be the total number reachable by some head-avoiding path. The state-BFS head shortcut set exactly equals `K ∪ KS ∪ SK`.

See `research/ddp/m2_coset_tower/REVIEW_COUNTEREXAMPLE.md/.json`. The second response explicitly retracted the false inequality and its numerical exclusions. No q≤11/q≤31 theorem is retained. Its additional unproved mod6 sum condition is also not adopted. The d6/q61 batch had already been selected and started independently of these invalid arguments.

## Second response: block-to-block formula omitted the target-head branch

The second response proposed

`Tbad(b) = U R1 ∪ U rho({w∈W3 : j_w ≡ b mod d})`

as an exact BB criterion, where the target block `(x,b)` is tested at `x r^(−b)`. This lists the source-head branch and direct leaf branch but omits paths through the target head. Such a route has length five:

`source block → source leaf → target-group leaf → its block → target head → target block`.

Its normalized targets contribute `r^(−b) U S_x`. The correct union includes that term. Equivalently, the exact group-set criterion is

`T_BB = H W3 H ∪ K W1 H ∪ H W1 K`.

The last term is the omitted direction. The word “commute” in the response is unnecessary and not generally valid: a single cost2 H jump in the direct branch's remaining budget3 must lie before or after its at-most-one S step, so it can be absorbed into the endpoint H factors without commuting it past S.

The root derived this correction and the independent math agent checked the full path classification. `research/ddp/m2_coset_tower/FULL_ROUTE_CRITERIA.md` proves exact BB, BL and LL criteria, together with the existing head criteria, for arbitrary finite G and H≤K. The saved-graph check in `BLOCK_ROUTE_CHECK.md/.json` found an actual counterexample in q41best: block820=(0,0) reaches block914=(12,2) in five steps via `820 → 205 → 750 → 955 → 1037 → 914` (B,L,L,B,target H,B). The target normalized coordinate3 is absent from Tbad(2) and present in the missing target-head term. In this graph Tbad omits16 reachable block targets and has no false positives; Tgood agrees pointwise with the complete BFS target set. The first checked source650 happened to have no omissions. The check stopped after the q41 counterexample, used0.00373CPU seconds and did not search new candidates. The reviewer's incomplete BB equality is not used as a filter or a proof.

## Effect on research

All production scores came from actual graph BFS; neither rejected reviewer formula was inserted into those scorers. The q98 paper exclusion explicitly counts cost2 H jumps and cost4 K jumps, so it does not repeat the false ordinary-Cayley argument. Zero new records remain. This is a partially useful review with explicit mathematical corrections, not a blanket accepted review or a completed final-results certification.
