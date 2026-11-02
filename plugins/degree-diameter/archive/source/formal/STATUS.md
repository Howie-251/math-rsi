# Formalization status

Original target: determine exact N(8,2), following ../N8/DEGREE_DIAMETER_8_2_ARIS_GOAL.md. Exact N(8,2) remains OPEN.

The current certified global baseline is **57 ≤ N(8,2) ≤ 63**. `original_baseline63` in ReviewAudit.lean combines the actual 57-point witness with `∀ n, Exists82 n → n ≤ 63`. The upper bound also has a universe-polymorphic original-graph statement. Orders 64 and 65 are universally excluded from the original degree/path hypotheses; orders 58–63 remain unresolved in this Lean project.

A separate n=59 theorem excludes only the stated triangle-free/all-2211-matching-row subcase. It is not a universal n=59 exclusion or a proof of the entire H5 branch.

## Pinned environment

- Lean 4.24.0 is installed in ../.tools/lean-4.24.0-linux; Lean and Lake executables were actually checked.
- Mathlib v4.24.0 and all eight upstream dependencies are fixed by lake-manifest.json; the upstream Mathlib checkout is unmodified.
- Official compiled dependencies for the imported graph and matrix modules were downloaded with Mathlib cache. The initial missing ProofWidgets release tag was resolved by fetching the pinned v0.0.74 tag. No further dependency installation is required for the present entry point.
- Environment entry: `source ../.tools/lean-env.sh`. It sets local Lean/Git paths and an eight-thread limit.

## Actual compiled modules

- DegreeDiameter/Definitions.lean: original maximum-degree bound, explicit actual edge-or-two-edge-path diameter condition, Exists82, and IsExact82. Gemini checkpoint A found no mathematical mismatch according to the parent review record. Exists82 uses a Type 0 existential carrier, and the compiled Relabel module now proves that every finite original graph in any universe has an actual Fin n copy satisfying the same degree/path predicates.
- DegreeDiameter/Relabel.lean: transports the actual degree/path predicates across graph isomorphisms, constructs the Fin n copy, proves exists82_of_original_graph for arbitrary universes, and proves exists82_iff_fin.
- DegreeDiameter/Moore.lean: root bound n ≤ 1 + 8 degree(r), Moore n ≤ 65, and n > 57 implies degree-eight regularity, all from one actual original graph.
- DegreeDiameter/Brown57Verified.lean: the explicit Fin 57 projective-coordinate graph with exact dot product modulo 7 and inequality excluding self-loops. Pure-kernel `decide` checks all 57 degree bounds and all 57 × 57 ordered vertex-pair path conditions. The whole adjacency rule is checked, not an assumed certificate. It compiled in 88 seconds during the initial 120-second profiling invocation.
- DegreeDiameter/Brown57.lean: bridges the computable and classical neighbor enumerations and proves `exists82_57` with that actual graph.
- DegreeDiameter/Defect.lean: constructs integer A and B=A*A+A−7I−J from the original graph. Proves common-neighbor counts, zero diagonal under regularity, symmetry, the exact off-diagonal formula, nonnegativity from actual diameter, row sum 65−card(V), and AB=BA. The original-graph caller derives regularity from Moore. Integer subtraction is used throughout.
- DegreeDiameter/TraceFive.lean: reduction modulo 5 proves that trace(A^5) is divisible by 5; the exact n=59 matrix and trace identities then give a contradiction from explicit trace(A^3)=0 and trace(B^2)=trace(AB^2)=590.
- DegreeDiameter/MatchingZero.lean: matchingRow is defined using four distinct actual vertices, B row 2δa+2δb+δc+δd, two same-weight actual edges, and four cross nonedges. It contains no trace assumptions. Row squares and row quadratic forms are proved equal to 10, both global moments are proved equal to 10 card(V), and actual triangle absence gives trace(A^3)=0. `no_n59_triangle_free_matching_rows` thus has only the original degree/path/order hypotheses plus genuine triangle absence and matching-row semantics.
- DegreeDiameter/Moore65.lean: at order 65, actual B≥0 and zero row sums force B=0. Over ZMod 29, M=2A+I obeys M²=4J and MJ=17J, hence M^(k+2)=4*17^k J. Frobenius at k=27 contradicts a pure-kernel finite-field calculation. This excludes order 65 and gives the original-graph and Exists82 upper bound 64.
- DegreeDiameter/Moore64Structure.lean: at order 64, nonnegative integer row sums of one force B entries to be 0/1 and B²=I. A genuine triangle would force two positive entries in one row, so the original graph is triangle-free. This also proves trace(AB)=0, using actual adjacency and common neighbors.
- DegreeDiameter/Moore64.lean: uses the above derived structure, with D=A(I+B)+I and the integer E0=6(I−B), reduced modulo 11. The identities D²=E+4J, DE=E, DJ=17J give D^(k+2)=E+4*17^k J. Frobenius at k=9 contradicts a pure-kernel finite-field calculation. `no_original_graph_card_64` assumes no additional matching, triangle, trace or spectral property. `original_graph_card_le_63` and `exists82_le_63` supply the current global upper bound.
- DegreeDiameter.lean imports all completed modules. ReviewAudit.lean independently imports that entry point and prints specifications, theorem types, raw original-domain callers, the successive baselines, and transitive axioms.

## Actual verification

The latest integrated `lake build DegreeDiameter` and independent `lake env lean ReviewAudit.lean` both completed with exit status 0 on 2026-10-11:

- logs/build-moore64-integrated.log
- logs/review-moore64-audit.log

All newly exported n=64 structure, exclusion, global-bound theorems and `original_baseline63` depend only on `propext`, `Classical.choice`, and `Quot.sound`. Earlier audited Brown, Moore, Defect, TraceFive, MatchingZero and Moore65 chains have the same allowed scope (the finite path checker needs only propext and Quot.sound). No sorry, new mathematical axiom, or native_decide occurs in the theorem sources or exported dependency chains.

Earlier successful build/audit logs are retained as actual milestones: baseline, defect, trace5, matching-zero, and moore65. Failed initial compiler attempts are also retained and are not represented as verification evidence.

## Remaining mathematical scope

No theorem determines exact N(8,2). No universal exclusion of orders 58–63 exists here. The n59 conditional theorem still needs a genuine structural caller proving the relevant branch supplies its matching rows, and cases with actual triangles require further arguments. No root-budget identities or structural classifications are silently assumed. Cross-family Gemini A/B/C reviews and their source scopes are tracked in the parent workflow and are not implied merely by Lean compilation.

## Reproduce

```bash
cd /inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal
source ../.tools/lean-env.sh
lake build DegreeDiameter
lake env lean ReviewAudit.lean
```

This is an incremental project build using official precompiled Mathlib dependencies, not a separately provisioned clean reproduction.

The finite relabeling bridge passed integrated build (logs/build-relabel-integrated.log) and independent audit (logs/review-relabel-audit.log), both exit 0. All five new theorems use only propext, Classical.choice, and Quot.sound. The Type 0 representation obligation is closed. The proposed n63 rational-polynomial route is described in N63_ALGEBRAIC_ROUTE.md; its 63 Chebyshev factor identities and composition leading coefficients passed exact Python checks (logs/n63-chebyshev-check.log), but no n63 original-graph Lean exclusion is claimed.

N63Norm and N63Lift passed the integrated build (`logs/build-n63-algebra-integrated.log`) and independent axiom audit (`logs/review-n63-algebra-audit.log`), both exit 0. The compiled results include the exact norm formula for 29+4 times an actual power-basis generator, multiplicativity and doubled degree of the ordinary-polynomial lift, and rational irreducibility transferred from an actual cyclotomic lift identity. Their transitive axioms are only propext, Classical.choice, and Quot.sound. Finite table instantiation and the original n63 graph caller are unfinished and paused; these generic bridges do not improve the certified upper bound 63.

## User-directed pause of known n63–65 formalization, 2026-10-11

The user explicitly directed work toward new orders 58–62, and stopped further proofs/formalization of the known exclusions 63–65 unless directly needed by those new proofs. The classical research baseline ≤62 is literature-backed in the parent workflow; it is not added here as an axiom or represented as a Lean theorem. The existing independently audited Lean baseline remains 57–63. No n63 original-graph exclusion is claimed, and completion of the n63 route is no longer an active obligation.

Checkpoint only was performed after that instruction, without further theorem development or an integrated rebuild:

- The active `lake build DegreeDiameter.N63Table` profiling attempt was interrupted (exit 130). `logs/n63-table-profile61.log` preserves that unfinished attempt. No compiler from this attempt is intentionally left running.
- `N63Norm` and `N63Lift` remain the latest integrated/audited additions, with the successful build and audit logs named above. The default `DegreeDiameter.lean` and `ReviewAudit.lean` were restored to this last integrated state.
- `DegreeDiameter/N63Compose.lean` compiled successfully in `logs/n63-table-small-compose-second.log` (overall exit 0). It proves the concrete quadratic discriminant criterion and actual simple-extension norm-to-composition irreducibility bridge. It was not subsequently added to the default entrypoint or independently axiom-audited.
- The previous six-row table sample (orders 1–6) also compiled in that log: actual cyclotomic coefficient identities, degrees, monicity, lift identities and irreducibility for orders ≥3, exact norms, and nonsquare rational norms where applicable. The current `DegreeDiameter/N63Table.lean` and `gen_n63_table.py` include an extension to order 61 and additional endpoint/composition statements; this current extended source has no completed validation. No complete 63-row Lean table or Chebyshev factor table was produced. The current table is not imported by the default entrypoint.
- The separate agent's `DegreeDiameter/N63Defect.lean` compiled in `logs/n63-defect-build-verified.log` and has its own `logs/n63-defect-type-axiom-audit.log`. Its real original-graph theorem proves the finite Chebyshev product annihilates the actual defect matrix. This proves no n63 exclusion. Its new default-import/audit additions were moved to the optional `ReviewN63Checkpoint.lean`, which was not run after the pause.
- The small official dependency-cache request finished successfully in `logs/n63-support-cache.log`. No `N63Support.lean` or `N63Restriction.lean` was started by this agent, and no characteristic-factor-support proof, restriction proof, or final n63 caller was completed.

Potentially reusable completed algebra consists of the actual power-basis norm identity, the polynomial lift irreducibility transfer, and the nonsquare-discriminant quadratic-composition criterion. Reuse is justified only if directly needed for a new 58–62 argument; no further general-library development is scheduled. All completed and unfinished sources and actual logs are preserved. No new axiom, sorry, native_decide, or artifact hash was introduced.

## New n59 zero-core capacity inputs, 2026-10-11

`DegreeDiameter/N59ZeroCore.lean` is compiled and its dedicated type/transitive-axiom audit succeeded. This work concerns a new n59 capacity argument, not the paused known-bound project. Actual commands were `lake build DegreeDiameter.N59ZeroCore` and `lake env lean ReviewN59ZeroCore.lean`, both exit 0, with at most three threads:

- logs/n59-zero-core-heavy-build.log
- logs/n59-zero-core-type-axiom-audit.log

`zeroTriangleVertex G z` means the actual neighborhood of z is independent. `commonZeroNeighbors G u v` filters genuine common neighbors by that predicate. No matrix certificate, moment assumption, or triangle count is part of either definition.

The compiled chain proves positive matching-row entries are 1 or 2; distinct equal-weight endpoints are adjacent in the original graph; hence three independent vertices with matching rows cannot form a positive triangle in the actual defect matrix. `common_zero_neighbors_card_le_two` assumes only that every zero-triangle vertex satisfies the existing actual `matchingRow`, plus distinctness of the queried pair. It proves the cardinality of that pair's actual common zero-neighbor set is at most two for any finite graph. It does not require matching rows at nonzero vertices.

`zero_heavy_has_nonzero_common_neighbor` then proves every distinct actual defect pair of weight 2 with a zero endpoint has a genuine common graph neighbor which is not zero. `n59_zero_heavy_has_nonzero_common_neighbor` calls this from the original degree bound, actual two-step diameter, card(V)=59, the explicit zero-only matching-row hypothesis, a zero endpoint, and the actual defect entry 2; it derives distinctness from Moore regularity and the actual zero defect diagonal.

All seven exported local/core/caller theorems checked in the dedicated audit use only propext, Classical.choice, and Quot.sound. No sorry, native_decide, new axiom, or hash was introduced. Only the successful module was added to the default entrypoint and the corresponding names to ReviewAudit; no whole-project rebuild or known-bound regression was run.

The remaining bridge to the paper's global capacity inequality is actual finite double counting: unordered zero-neighbor light/heavy pairs, nonedge second-neighbor counts and their local budget, heavy ZZ edge coverage by nonzero common neighbors, and triangle-incidence sums. This module does not prove 59≤4m−3T, m≥20, T≥7, N15 for all legal original graphs, or a universal n59 exclusion. Those conclusions must not be inferred from this local checkpoint alone.

## New n59 global nonzero-vertex bound completed, 2026-10-11

`DegreeDiameter/N59Capacity.lean` now closes the actual finite-counting chain to
`n59_nonzero_triangle_vertices_at_least_twenty`:

```lean
(G : SimpleGraph V)
(hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
(hcard : Fintype.card V = 59)
(hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
⊢ 20 ≤ (nonzeroTriangleVertices G).card
```

Every counted object is constructed from that same actual graph and its existing defect matrix. `nonzeroTriangleVertices` is the finite set of vertices whose actual neighborhood is not independent, equivalently vertices in at least one actual triangle. Only zero vertices are assumed to have matching rows. No local capacity or global incidence condition is supplied as an extra hypothesis.

The compiled chain proves the original nonzero-root nonedge budget ≤4, each ordered heavy pair of zero neighbors has exactly two root-outside common neighbors, the common-zero cap bounds each reverse fiber by two, and hence the actual local ordered-heavy-pair count plus heavy-zero-endpoint count is ≤4. The exact global heavy-degree identity gives 2|Z|; every ZZ heavy pair is covered by a genuine nonzero root using N59ZeroCore. Finite summation gives 2|Z|≤4|N|, and |Z|+|N|=59 yields |N|≥20.

Actual successful commands were `lake build DegreeDiameter.N59Capacity` and `lake env lean ReviewN59Capacity.lean`, each exit 0, with at most three threads:

- logs/n59-capacity-global-second.log
- logs/n59-capacity-type-axiom-audit.log

The dedicated audit prints the real definitions and exact caller types. All seven audited capacity/global results, including the final theorem, depend only on propext, Classical.choice, and Quot.sound. The successful module and theorem names were added to the default entrypoint/audit; no known-63–65 proof, full-project rebuild, or known-bound regression was run. Sources contain no sorry, native_decide, or new axiom.

Remaining scope: this closes the requested m≥20 finite-count bridge under explicit zero-only matchingRow semantics. It does not prove N15 for every legal original graph, the stronger triangle-count expression 59≤4m−3T, a formal triangle-count lower bound T≥7, any T=7 equality classification, or a universal order-59 exclusion. Those are distinct obligations. The original exact N(8,2) goal remains open.

## New order62 S_TOUCH exclusion, 2026-10-11

DegreeDiameter/N62STouch.lean and ReviewN62STouch.lean compiled with exit0 using at most3threads. Logs: logs/n62-stouch-complete-second.log and logs/n62-stouch-type-axiom-audit.log. The final no_n62_stouch_template takes the original graph degree/diameter/order62 hypotheses plus STouchTemplate, a predicate containing only actual Adj facts and parent uniqueness. It derives all needed B rows; there is no supplied defect-row certificate, no Bsimple premise and no new axiom. The audited transitive axioms are only propext, Classical.choice, Quot.sound.

This excludes the whole actual S_TOUCH template. It does not construct the seven-template coverage theorem in Lean, exclude other templates, or prove arbitrary order62 nonexistence. Entry/audit imports now include this module. Gemini B15 accepted the actual source backtranslation, with zero reviewer commands. N62TriangleMate is a separate active module for the original-graph triangle pairing bridge, not yet part of this checkpoint. No known63–65 work was resumed.

## Actual order62 triangle mates, 2026-10-11

N62TriangleMate.lean and ReviewN62TriangleMate.lean compile/audit exit0 (logs/n62-triangle-mate-build.log and n62-triangle-mate-type-axiom-audit.log). Final n62_triangle_has_paired_triangle takes only original graph hypotheses and three genuine triangle edges, constructing a disjoint paired triangle, no edges between the triangles, and reciprocal actual repeat rows. All six exported theorem audits have standard axioms only. No global Bsimple or supplied template is required. The source uses a shorter AB-entry proof of mate adjacency than the reviewed indicator paper. Global finite triangle involution/evenness is the next active module; simple-B parity/exclusion not yet Lean. No63–65 work.

## Actual order62 parity theorems, 2026-10-11 10:20 UTC

N62TriangleParity and N62OppositeParity compiled and passed their dedicated actual type/axiom audits, all exit0. The first proves Even (G.cliqueFinset 3).card for every original legal order62 graph, using its constructed reciprocal triangleMateSet. The second proves Even (unitNonedgePairs G).card with the explicit additional actual-defect premise B≤1, using oppositePair as the actual common-neighbor set. All five exported results use only propext, Classical.choice, Quot.sound. Dedicated logs and precise definitions are in N62_TRIANGLE_PARITY_HANDOFF.md. Imports/checks now integrated; no whole-project or known63–65 rebuild was run. Gemini B16 source review is in flight.

The active remaining formal bridge is 2·unitNonedgePairs.card+6·cliqueFinset3.card=186 from actual incidence counts, then simple-B contradiction. The full order62 exclusion remains open; no supplied counting certificate or abstract involution is an extra original-graph premise.

## Simple-defect order62 exclusion completed, 2026-10-11 10:29 UTC

N62SimpleExclusion.lean now proves the actual incidence identity 2·unitNonedgePairs.card+6·cliqueFinset3.card=186 and connects it to both actual evenness results. Final no_n62_simple_defect_graph takes only original graph degree/diameter/card62 plus the explicit actual B≤1 premise, and concludes False. There is no count certificate or supplied pairing. Dedicated build n62-simple-exclusion-build-second.log and actual definitions/types/axioms/raw caller audit n62-simple-exclusion-type-axiom-audit.log both exit0, standard three axioms only. Integrated source imports and audit declarations are updated; B17 cross-family review pending. Universal62 remains open in the heavy-repeat region. D2 actual-parent formalization is active; no63–65 work.

## D2_MATCH actual-parent exclusion completed, 2026-10-11

N62D2.lean and ReviewN62D2.lean compile/audit exit0 (logs/n62-d2-full-second.log; n62-d2-type-axiom-audit.log). All16 exported results use only standard three axioms. Final no_n62_d2_match_template derives the full saturated-row, 5/5/6 class counting, support and commutation contradiction from originalG and a template containing only actual vertex/Adj/parent facts. No count certificate, B row, N15, simpleB or triple-elimination premise. See N62_D2_HANDOFF.md for exact scope. Integrated imports/audit updated; cross-family finalsource review is next batch. N62D0Bin actual parent/BIN-witness implementation now active, no63–65 work.

## D0_EDGE_BIN actual-parent exclusion completed, 2026-10-11 10:51 UTC

N62D0Bin.lean and ReviewN62D0Bin.lean compiled and passed the actual caller/type/axiom audit (logs/n62-d0-bin-full-build.log and n62-d0-bin-type-axiom-audit.log). The final no_n62_d0_edge_bin_template takes the original degree, diameter and order hypotheses and an actual adjacency/parent template. Its BIN witness is an actual additional common neighbor of w,b; bin_common_neighbor_of_unit_repeat derives this witness from the branch's actual unit-repeat condition. All five audited exports use only propext, Classical.choice, Quot.sound. No matrix-row certificate or counting identity is an extra caller premise. The validated module is now imported by the default entrypoint; no full-project or known63–65 rebuild was run. Cross-family final-source review is pending. D0 closed-component formalization is active; the full order62 and exact-value goals remain open.

## Actual D0 closed components completed, 2026-10-11 10:54 UTC

N62D0Components.lean completes both MATCH and BOUT original-graph callers. It constructs four distinct vertices, all four actual repeat rows, and the full induced original graph (empty in MATCH; exactly two opposite edges in BOUT). An explicit theorem zeros all repeat entries from the four vertices to outside. The BOUT template contains actual adjacency and common-neighbor data; a public bridge constructs it from the actual unit-repeat branch condition. All seven exports passed the dedicated caller/type/transitive-axiom audit with the standard three axioms only. Final logs: n62-d0-components-final-build.log and n62-d0-components-type-axiom-audit.log. Imported after those successes; no full-project rebuild. This does not yet formalize global odd-double parity, template coverage, or D1-root existence. The shorter source proof relative to the paper is documented in N62_D0_COMPONENTS_HANDOFF.md; final-source Gemini review remains to be sent.

## Actual odd double-repeat count completed, 2026-10-11 11:03 UTC

N62DoubleParity.lean derives Odd (doubleRepeatPairs G).card from the original graph assumptions and explicit actual B≤2. The counted set consists of all unordered actual B=2 pairs; nonadjacency is proved, not baked into that final set. The chain constructs actual opposite-pair flags, proves their fixed-point-free swap, counts them as P1+3d, and derives actual repeat incidence 2P1+4d+6T=186. Triangle evenness closes the odd-d conclusion. No supplied count or cycle certificate appears in the caller. All six exports passed the dedicated original caller/type/transitive-axiom audit with only the standard three axioms; final logs n62-double-parity-full-third.log and n62-double-parity-type-axiom-audit.log. The module is imported after these successes. Triple-repeat exclusion and global template coverage are not formalized here; no universal62 result follows yet. Finalsource cross-family review is next batch.

## Actual double-root coverage and D1 outlet, 2026-10-11 11:17 UTC

N62DoubleRoot.lean now constructs actual parent data directly from any B[r,w]=2. The final local theorem n62_double_root_d1_or_closed_component takes only the original graph conditions and that double entry, and constructs either a D1MatchParentTemplate or a ClosedDoubleFour containing the chosen pair. It derives ordinary-parent uniqueness and actual parent cardinalities, constructs and excludes D2 and BIN cases, and connects actual MATCH/BOUT callers. No global B≤2 premise is needed locally. Twelve exports and both raw callers passed the dedicated standard-axiom audit. Logs: n62-double-root-closure-first.log and n62-double-root-type-axiom-audit.log.

N62D1Outlet.lean then defines the other double pair canonically as the actual unit-repeat neighbors of the first pair. Under absence of D1, the local theorem makes this a fixed-point-free involution on actual doubleRepeatPairs; hence their count is even. Contradicting N62DoubleParity yields n62_exists_d1_match_parent from original graph conditions and the explicit actual B≤2 premise. The four exports and raw caller passed the dedicated standard-axiom audit. Logs: n62-d1-outlet-first.log and n62-d1-outlet-type-axiom-audit.log. Both modules are integrated after their completed checks; no full-project or known63–65 rebuild was run. The paper's separate triple-repeat exclusion is not formalized in this caller. D1 exclusion and arbitrary order62 nonexistence remain open. Final-source Gemini review is a subsequent batch, not B19.

11:52 source-review update: Gemini B18 accepted final D2/BIN sources, B19 accepted D0Components/DoubleParity, and B20 accepted DoubleRoot/D1Outlet within their actual caller scopes, with zero reviewer executions. B20's summary incorrectly says every double edge is D1; the actual theorem proves existence of at least one D1 root, and D0 components may coexist. Its separate component-size paper review contains incorrect moment substitutions and is not accepted. B21 subsequently accepted the corrected moment and component-size proofs. No Lean source or build result changed. New three-component exclusions remain paper/external exact-check results and are not formalized here.

## Actual repeat-component equitability completed, 2026-10-11 12:18 UTC

N62RepeatComponents.lean constructs the positive support of the actual defect matrix and proves n62_repeat_components_equitable using only original degree, diameter and order62 conditions. Actual component indicators are B-harmonic; AB=BA makes their original-neighbor count vectors harmonic, and a finite integer Dirichlet argument makes those counts constant on actual support components. Concrete repeatComponentDegree and repeatQuotientMatrix are constructed, and every actual source vertex realizes its entry. No B<=2, D1, component-size or supplied quotient premise is required.

The dedicated module build and ten-result type/transitive-axiom/rawcaller audit both exited0: logs/n62-repeat-components-fourth.log and logs/n62-repeat-components-type-axiom-audit-final.log. All results use only propext, Classical.choice and Quot.sound. Source and successful evidence have been inspected, and the module and main theorem names are integrated in DegreeDiameter.lean and ReviewAudit.lean. No whole-project or known63–65 rebuild was needed. Gemini B23 final-source overlay is in flight.

The new paper connectedness theorem passed local integration PASS15 and Gemini B22, including the external exact quotient search coverage. This is not a Lean connectedness theorem: quotient quadratic/balance/row identities, spectral trace/count facts, component-size results and the exact finite classifications remain later formal obligations. No arbitrary order62 exclusion or new global numerical bound is claimed.

## Actual quotient identities and component bounds completed, 2026-10-11

N62RepeatQuotient.lean constructs actual component sizes and membership S on the actual finite support-component type. It proves AS=SR, BS=3S and JS=Ssize, then derives R²+R=10I+1nT from the actual defect definition. Row sums8, size-weighted edge balance, actual sizes sum62, positive sizes and nonnegative entries are proved from original graph inputs. No B<=2 or supplied quotient premise. Eleven public results and original quadratic/row/balance callers passed targeted build and standard-axiom audit: logs/n62-repeat-quotient-second.log and n62-repeat-quotient-type-axiom-audit.log, exit0. GeminiB24 accepted the final source and exact scope with zero reviewer execution. N62RepeatComponents final-source review passed B23.

N62RepeatComponentBounds.lean proves actual restricted rows sum3, each actual component has even size, and under explicit actual B<=2 each component has at least4 vertices. Evenness and the exact nonnegative quotient budget do not need that bound. The budget is sum_D R_CD(R_DC-1)=size(C)+2-R_CC, and its diagonal term yields R_CC²-2<=size(C). Seven exports and three original callers passed targeted build and standard-axiom audit: logs/n62-repeat-component-bounds-second.log and n62-repeat-component-bounds-type-axiom-audit.log. The private generic parity helper has one harmless unused Fintype-variable warning. GeminiB25 source review is in flight.

Both modules and main audit names were integrated only after those successful checks. No whole-project or known63–65 regression was run. Component-count trace17, D1 minimum sizes, connectedness and finite quotient classifications remain outside these formalized scopes. A directly relevant actual quotient trace proof is the next bounded formal task.

The connectedness paper now uses SHORT_COMPONENT_COUNT_BOUND.md with only earlier H,K>=12, bypassing the longer chain reaching14. Local deltaPASS6 and GeminiB24 accept that dependency reduction. It changes no global numerical bound and is not yet a Lean connectedness theorem.


## 2026-10-11 13:04 UTC: actual trace and triple geometry

N62RepeatQuotientTrace.lean is compiled (third build exit0, no warnings) and independently invoked in ReviewN62RepeatQuotientTrace.lean (audit exit0). Eight exported theorems use only propext, Classical.choice, Quot.sound. The original finite G, degree<=8, diameter<=2 and order62 hypotheses directly give c+2traceR=17 and c odd, with actual repeat components and quotient. The integer centered matrix P=62(2R+I)-17N satisfies P^3=157604P; exact F1063 trace divisibility and integer interval bounds replace a longer spectral implementation. No B<=2 or supplied spectral/trace certificate. B26 source review accepted, with review-only prose corrections recorded in its disposition. Shared import/audit entries added.

N62TripleRepeat.lean is compiled (second build exit0, only replayed predecessor linter warnings). Dedicated ReviewN62TripleRepeat audit exit0; twelve exported theorems including membership API and three actual callers, only the standard three axioms. Original G plus actual Buv=3 yields saturated rows, distinct nonadjacent zero-triangle endpoints, actual four-common-neighbor set S, its complete closed unit defect rows, CN(s,t)={u,v}, outside-neighbor uniqueness, and actual repeat components of sizes2 and4. Shared import/audit entries added. Full five-cell construction, finite classification and actual triple exclusion B<=2 are still outstanding. B27 source review in flight.

ComponentBounds B25 source review accepted within its explicit hypotheses. No formal connectedness, whole62 exclusion, exact N8 theorem, or renewed63–65 work. Overall compiled bound57..63 unchanged; cited baseline57..62 unchanged. New task N62TripleMatching is active, limited to actual two four-point exclusive-neighbor sets and their perfect original matching.


## 2026-10-11 13:33 UTC: analytic triple replacement and next actual bridges

N62TripleMatching.lean and N62RepeatComponentBudget.lean are integrated and compiled. Matching has19 audited declarations/four original callers; final audit log is n62-triple-matching-type-axiom-audit-final.log. Budget has3 theorems/two actual or conditional callers; its six-component/three-diagonal hypotheses remain explicit. Both use only propext, Classical.choice, Quot.sound. B28 source review accepted.

N62TripleCells.lean is integrated: actual E8 cross-repeat support and row3, four disjoint six-point original-neighbor fibers giving U24, actual inner14 and remainderV24, and E/U/V repeat closure. 23 public theorems/four raw graph callers passed dedicated audit; second target build exit0,27s with two unnecessarySimpa suggestions. Full original-neighbor quotient is separate.

N62TripleFourBlock.lean is integrated: an explicitly supplied symmetric nonnegative integer Fin4 matrix with diagonal0 and row3 is classified under an actual four-label permutation fixing0 into300/210/111, specifying all six upper entries. Three theorem audits and matrix caller passed; third build exit0,9.6s,no warnings. Actual graph construction remains separate. B29 source review of Cells/FourBlock running in MCP cell374.

TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md replaces recovered finite-table Steps4--5 by three actual eight-point repeat components of internal original degree2; c>=6 and traceR>=6 contradict17. Recovered originalgraph Steps1--3 retained. Fresh full-chain provisional PASS and B28 accepted; trace identity has no B<=2 or connectedness premise. No full Lean triple exclusion yet.

Active individual files N62TripleCellDegrees.lean and N62TripleActualBlock.lean are unfinished and not imported. Dedicated63--65 work remains stopped. Overall compiled57..63 and cited57..62 unchanged.
