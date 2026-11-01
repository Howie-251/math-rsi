# Round01 cross-family review record

Updated 2026-10-13. These are scoped mathematical reviews, not a completed
T34 proof or a claim that either model executed Lean.

| Raw response | Valid scope and disposition |
|---|---|
| `gemini_multi_bad_lp.json` | Fixed actual bad-count vector, linearized minimum over finitely many layouts, exact weak dual. The claim that the optimal auxiliary y is unique was too strong and is not used; choosing all upper bounds suffices. Proposed cross-center quotas were not assumed. |
| `grok_seven_low.json` | 24-point at-least-seven-low candidate, actual selection and fixed-vector layout mixture; no table regeneration. |
| `grok_twenty_two_and_six.json`, `gemini_twenty_two_and_six.json` | 22-point minimum-degree-seven coverage chain and exact repaired dual; 21-point unique-six/no-seven selection. Gemini quoted 24231/24310 as the maximum of five rows; the actual maximum is 12152/12155. All five remain strict. Neither regenerated the large domains. |
| `grok_twentyfive.json` | Full 25-point paper map: actual q=5/8/9 selection, clique decomposition and extension coverage, singleton/empty restoration and actual tenth lock. Did not recompute the 11692/840/147 tables or run Lean. |
| `grok_20_21_24_selection.json` | 20-point degree-eight graph/capacity contradiction; 21-point degree-eight graph reduction; 24-point weighted three-class selection of eight matching locks. No specific mathematical defect found in the read scope; local tables and numerical witnesses treated as dependencies, not regenerated. |
| `gemini_twenty_two_full_new.json` | New successful session: 22-point one-/two-low actual selection, degree split and universal residual-profile quantifiers; verifies U≥14 in the two-low/two-seven case and the weighted-overlap coefficient inequality. No large JSON replay or Lean execution. |

All valid Grok entries report `grok-4.7-build/xhigh`, `stopReason=end_turn`.
All valid Gemini entries report CLI-selected `gemini-3.8-flash-high/high`,
`status=SUCCESS`; this is the CLI selection record, not independent server-side
model identification.

## Failed calls retained without acceptance

- `grok_six_low_and_six_degree.json`: `max_turn_requests`, `isError=true`;
  the requested 24-six-low/21-full-six review did not finish. No automatic
  retry of that unchanged paid request.
- `gemini_six_seven_low.json` and `gemini_six_seven_low_retry1.json`:
  interrupted streams, no completed mathematical verdict.
- `gemini_six_seven_low_retry2_fresh.json`: new conversation returned ERROR
  (`HTTP response to HTTPS client`). The two immediate extra attempts allowed
  by the user were then exhausted; no further immediate retry was made.
- After roughly 25 minutes, a new session on the newly completed 22-point
  scope succeeded (`gemini_twenty_two_full_new.json`). It does not turn the
  earlier incomplete scopes into accepted reviews or establish the old
  connection failure's root cause.

## Remaining final review

The scoped 23- and 24-point requests listed below have now returned valid
responses. Complete paper review R1 is saved in `../paper-audit/`; its only
MINOR dependency-description issue was corrected without changing any
mathematics. The final exported Lean statement, transitive axioms, final
cross-family C review and reproducible handoff remain unfinished.

## Subsequent valid scope and reconciliations

- `gemini_24_complete_23_fourfive.json`: SUCCESS; actual 24-point selection,
  eighth-low projection, and 23-point r4/5 selection/universal residual
  quantifiers. No large-table arithmetic or Lean execution.
- `grok_23_selection_24_complete.json`: end_turn; six-point exchange and W=6
  two-K7 structure, and the 24-point actual extension dispatcher. Its wording
  about all-seven restoration must be read for the six-lock base only. Seven
  locks can temporarily have negative empty count; actual code preserves
  those until lowering degrees. The 56 temporary-negative promotions yield
  207 necessary mixed orbits, all actually retained. Updated §3 makes this
  order explicit; the original data and mathematical scope did not change.
- Fresh proof-checker identified an outdated dependency description: the
  weighted-overlap lemma is valid but unused by the final strict certificates.
  Root confirmed all 22 four-low entries are ordinary direct/joint; the only
  root weighted entries are eight non-strict 23-point diagnostics. High-math
  separately checked 75 JSON / 1049 certificates and found zero weighted
  quotas. The unused extra formalization was stopped before any Lean source
  was created, and the mandatory dependency map was corrected.

- `gemini_23_onetwothree.json`: valid SUCCESS on the new 23-point r1/2/3
  selections, common-unit degree counts, sorted-high coverage, and cluster
  graph contradiction. No table replay or Lean execution. One wording issue
  in the response needs correction: a strict deletion *of a lock profile*
  colors the same original H through its conditional probability lemma.
  This is not an appeal to colorability of an induced subhypergraph implying
  colorability of the whole graph (which would be invalid). All 34 edges
  remain in the projected trace counts. The proof texts already use the
  former, correct meaning. Strong adjectives in model output are not an
  additional mathematical guarantee.

- `grok_23_minseven_onetwo.json`: valid end_turn, actual `grok-4.7-build/xhigh`.
  Checks full 23-point no-low selection/extension and r1/r2 common-unit
  counts and cluster contradiction. Explicitly confirms the corrected
  temporary-negative seven-lock handling. Did not regenerate 66/725/78/209/
  1125/26 profile counts or the strong-codegree certificate package, and
  did not independently derive the saved probability fractions. No Lean run.

## Actual Lean B interface and the shorter 23-point selection

- `grok_mixed_lean_B.json`: valid end_turn, grok-4.7-build/xhigh. Full four-file
  MixedLayout core, actual type/bad-pair dependencies and one concrete caller
  checked statically; ordered capacities, half penalties, same-H binding and
  original coloring interface accepted in scope. Read existing logs, no Lean
  execution.
- `gemini_mixed_lean_B.json`: ERROR, HTTP response to HTTPS client, no verdict.
  Authorized fresh retry1 in `gemini_mixed_lean_B_retry1.json` returned SUCCESS,
  CLI-selected gemini-3.8-flash-high/high. Same four-file actual interface,
  relevant dependency sources, caller0 and the five-caller audit logs read;
  no substantive issue found, no Lean execution. Its endorsement of all five
  callers is limited to this source/log scope, not five separate reruns.
- `grok_23_selection_simplification.json`: valid mathematical review of the
  energy/parity replacement for subset averaging and selected-vertex
  saturation replacing the global two-K7 step. Directly checks the existing
  equality generator only needs the actual degree-eight/unit-codegree input;
  209 old certificates not recomputed.
- `gemini_23_selection_simplification.json`: valid SUCCESS, CLI-selected
  gemini-3.8-flash-high/high. Checks both mathematical simplifications, the
  three selection source modules, the equality generator and existing logs;
  confirms the generator needs only an actual degree-eight vertex with unit
  codegrees to the six selected locks. No generator or Lean execution. Its
  build-status paragraph cites the older failing r6 log: this is superseded by
  `../twentyone-lean/build-twenty-three-r7.log` (910 jobs successful) and
  `../twentythree-seven-math/selection-audit.log` (eight standard-three-axiom
  queries, exit 0). Thus no source repair remains at that cited location.
  Both models' endorsements concern these selection obligations, not the
  still-unassembled full 23-point coloring theorem or T34.


## Completed scoped source review of the 24-point actual selection

The compiled `WeightedThreePartition`, `TwentyFourMatchingSelection` and
`LockRelabel` modules were sent to new Grok and Gemini B sessions with
`MATCHING_LEAN_B_PACKET.md`. Grok has returned valid end_turn, actual
grok-4.7-build/xhigh, in `grok_matching_lean_B.json`. It read the three
modules, actual defining dependencies, a live 21-point relabel caller and
existing build logs; no missing actual-input connection or counterexample
found in scope. It ran no commands. Its sentence about equality being
realizable is used only as an algebraic equality condition on the degree
budget, not a proof that some hypergraph realizes the bound sharply.

Gemini returned valid SUCCESS, CLI-selected gemini-3.8-flash-high/high,
in `gemini_matching_lean_B.json`, thread 6566c476-bb18-4b9c-9d7a-e2d8b08e3d9b.
It read all three sources and defining dependencies, an actual relabel caller
and existing build logs, and found no substantive issue. No commands were
executed. Both reviews concern actual selection and type-count transport,
not the complete 24-point branch or T34.


## Sparse promotion completeness and actual reconstruction B

- `gemini_promotion_lean_B.json`: valid SUCCESS, CLI-selected
  gemini-3.8-flash-high/high, thread b89de7aa-2f7c-44cd-8588-a28fbc88f667.
  Read the general allocation/split/reconstruction sources, initial triples,
  new four-lock data/kernel/caller, generator, downstream dispatch and graph
  context. No mathematical or actual-input issue found in scope; no commands
  or table regeneration. Phrases such as “as proved” in this static review
  do not establish that the new four-lock coverage/classifier compiled. At
  readback, shared interfaces and base triples have passed; four-lock full
  kernel/caller/classifier still await their actual builds. T34 remains open.
- `grok_promotion_lean_B.json`: valid end_turn, actual grok-4.7-build/xhigh,
  thread 4ab98820-131f-4cc5-8c6b-9215467a3753. Read the seven attacked bindings
  and actual source dependencies, including enumeration, omitted-type
  readback, subtraction, reconstruction and permutation direction. Found
  no defect in scope; explicitly retained the three-lock inventory and
  codegree-cap premises of the four-lock caller. It did not run Lean or
  recompute tables and did not claim the 23-point branch or T34 is proved.
  New 21-point Many/Unique assembly is outside this review packet.
