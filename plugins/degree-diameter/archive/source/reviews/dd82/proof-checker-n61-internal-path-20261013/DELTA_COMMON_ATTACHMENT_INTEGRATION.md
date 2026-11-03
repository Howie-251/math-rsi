# Reused integration delta: common-attachment exclusion

Date: 2026-10-13. **PASS within the stated structural scope**, modulo
the explicitly inherited reductions, reviewed implementation semantics
and saved exact-input certificate verification. Reviewer:
`/root/internal_path_proof_check`; **reused, same-family, provisional**.
This receipt is not a fresh source audit, new certificate check, Gemini
acceptance or Lean result. The original reviews retain their scopes.

Read the complete 37-line primary manuscript
`proofs/dd82/n61/INTERNAL_DOUBLE_COMMON_ATTACHMENT_EXCLUSION.md`.
For this integration only, read the fresh `SOURCE_REVIEW.md` receipt,
the `r0_h1_b0/encoding.json`, `result.json`, `certificate_check.json`
and `certificate_check.log`, and the two other case result summaries
under `computations/dd82/n61/internal_double_full61_run/`.
No source code, solver or certificate was rerun or re-audited.

## Seven integration obligations

1. **Complete reduction to the checked type.** The earlier reviewed
   pure deductions give epsilon zero, `rh=0`, `h<=1`, and exactly
   `(r,h,beta)=(0,1,0),(1,0,0),(2,0,1)`. Therefore any positive h
   requires the first type. This uses the existing reduction, not an
   assumption that the other two computations succeeded.
2. **Every target reaches this actual input.** The prior model audit
   proved complete neutral-parent/attachment labeling for the h1 case,
   without reference matching or additional structural restriction.
   The separately fresh source receipt covers the stable implementation,
   all original degree and pair semantics, exact auxiliaries and the
   shared-attachment conditions. The actual encoding record identifies
   `r0_h1_b0`, epsilon zero, 1086 primary edge variables, 74 fixed
   edges, all1830 original pairs, 49 shared-attachment exact pairs,
   and zero r2 endpoint-domain additions. Its 53046 variables and
   163721 clauses match the actual result and checker log. Thus the
   previously proved coverage implication connects to this input;
   the optional r2 refinement is not a hidden h1 restriction.
3. **Actual checked contradiction.** The saved solver command names
   this case's `input.cnf` and `proof.lrat`; exit20, CPU4.012334 and
   proof size11623492 bytes are recorded. The saved `lrat-trim0.2.0
   --no-trim` command names the same two paths. Its log reads the
   `p cnf 53046 163721` input, checks73206 proof clauses and reports
   `s VERIFIED`; its result is exit20 with `verified=true` and
   CPU0.113276. These are inspected prior execution receipts, not a
   verification performed by this reviewer. They supply the exact
   input contradiction required by obligation2.
4. **Global local conclusion.** A hypothetical positive h for any
   selected consecutive D triple would satisfy the contradictory input.
   Hence h is zero for every such triple. Every common neighbor of
   u,w lies in T or Z: neither endpoint can be its own neighbor, and
   v is adjacent to neither endpoint. The Z intersection is empty,
   so `N(u) intersect N(w)` is contained in `T=N(v)`.
5. **The at-least-four-vertex consequence.** In any D component with
   at least four vertices, the two outer vertices of a consecutive
   triple cannot both be component endpoints. An internal outer
   endpoint already spends its complete defect row on its two D
   neighbors. The other outer endpoint is at path distance two, so
   their beta is zero. With epsilon=h=0, `r=1+beta=1`. The one
   common neighbor of the outer pair lies in T, hence is adjacent
   to all three vertices. It is the unique common neighbor of the
   whole triple. On a three-vertex component, r=1 or2 remains.
6. **No consecutive101 pattern.** Fix any original vertex x and any
   valid three-position window along any D path. If its first and
   last adjacency bits are one, x is a common neighbor of those
   outer vertices; obligation4 forces its middle bit to be one.
   This also applies when x itself lies on the path. No automorphism,
   global Toeplitz extension or unproved path classification is used.
7. **Residual status.** The actual other results are UNKNOWN, exit0,
   CPU56.298772 and57.767905, both with `proof_checked=false`.
   Their partial traces supply no contradiction. The two h0 types,
   all internal-double existence questions beyond this exclusion,
   and order61 remain unresolved.

All seven obligations are discharged, with zero issues. In particular,
the shortest relevant four-vertex component has an internal outer
endpoint in both of its triple windows; the three-vertex exception is
retained. A potential101 window is ruled out by an exact set inclusion,
not by a search that found no examples. The two surviving cases were
not inferred impossible from their time limits.

The delivered result is the computation-assisted structural theorem
`h=0`, the associated neighborhood inclusion, and the two stated path
consequences. No internal-double or whole-order61 exclusion, graph above57,
or changed range `57<=N(8,2)<=61` follows. Root-managed Gemini round3
remains a separate external review; it is not claimed by this receipt.

## Subsequent reused delta: direct endpoint-port clauses

Read in full `proofs/dd82/n61/INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md`
(27 lines). **PASS**, explicitly reused, same-family, provisional.
This new scope is a pure consequence of the universal h=0 result and
the separately reviewed r2 port classification. Root has since reported
actual Gemini round3 acceptance of the h=0 integration; no external
review or old calculation was repeated for this delta.

If `B_uz=2`, the distinct vertices v,u,z form a consecutive D triple:
u's two double entries at v,z exhaust its row. The universal inclusion
for this new triple gives `N(v) intersect N(z) subset N(u)`. Because
z has exactly one neighbor t(z) in `T=N(v)`, it follows that
`t(z) in U`. The w argument is identical. This uses universal h=0;
h=0 for only the originally selected triple would not justify it.

For r1, the three U parent classes have sizes5,6,6, totaling17.
Exactly `50-17=33` Z vertices lie over parents outside U. W has
the same count. Thus there are66 necessary negative second-threshold
conditions before simplification. These are33 Z positions per endpoint,
not33 distinct parents. A fixed-false threshold contributes a tautology.
In r2 each endpoint has only one residual defect unit, so a second-
threshold condition is already automatic.

For r2 the proved endpoint domains are
`{q0} union O_c union O_d` and `{p0} union O_c union O_d`, each
of size11. The allowed ordered pairs are three disjoint sets of
sizes1,25,25, hence51. Exactly `11*11-51=70` pairs are forbidden.
For every forbidden pair, the clause `not X_x or not Y_y` removes
precisely the simultaneous actual unit-port choice. Existing exact
thresholds and endpoint budgets already ensure one chosen port per
side. All three allowed configurations remain represented, without a
selected attachment matching or additional variable.

The two local deductions and both presimplification counts are sound.
No issue was found. The result authorizes these necessary mathematical
constraints; it does not certify a refined emitted input or a solver
outcome. The original integration receipt and both UNKNOWN results
retain their prior scope; no h1 rerun is needed by this deduction.
