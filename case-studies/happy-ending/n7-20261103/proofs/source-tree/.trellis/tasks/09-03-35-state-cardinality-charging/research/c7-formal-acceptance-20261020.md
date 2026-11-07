# C7 formal human acceptance with same-family/provisional review, 2026-10-20

C7 is formally accepted by the user's explicit decision. The current upper
bound is **N<=28 in the complete ordered rank-3 signotope / blue-path-5 /
red-path-6 / no-weak-7-gon model domain**. Accepted C1..C6 and four retained
checked C7 cases establish `e(X)>=7 => m(X)>=7` at every finite order in this
domain. This is not a geometric Erdős–Szekeres upper bound.

The exact user authorization is: “接受这次 GPT 审查结果，正式验收 C7，将限定模型域内的上限更新为 28，保留 same-family/provisional 说明，C8、C9、C10 的证明检查继续运行。”
Authority is `human_user`; favorable review alone was not treated as acceptance.

## Row and numerical inference

Endpoint injection into the 25 ordinary and 10 exceptional state catalog gives
`N=25+e-m`. A C7 counterexample has e>=7 and m<=6; accepted C6 forces m>=6,
so m=6 and N=19+e. Since e<=10, these retained exact cells are exhaustive:

| Cell | Missing ordinary states | N | Historical encoding | Reused qualification |
| --- | ---: | ---: | --- | --- |
| A[7,7] | 6 | 26 | legacy_exact_with_state_path_bridges_v1 | VERIFIED_UNSAT |
| A[7,8] | 6 | 27 | legacy_exact_with_state_path_bridges_v1 | VERIFIED_UNSAT |
| A[7,9] | 6 | 28 | legacy_exact_with_state_path_bridges_v1 | VERIFIED_UNSAT |
| A[7,10] | 6 | 29 | legacy_exact_with_state_path_bridges_v1 | VERIFIED_UNSAT |

Their emptiness proves C7. For e<=6, accepted C1..C6 give m>=e (e=0 uses
m>=0), hence N<=25. For e>=7, C7 and e<=10 give N<=25+10-7=28.
No complete m>=e or N<=25 theorem is asserted.

## Exact publication evidence

Server root:
`/data/ktqiu_hdd/math_agent/res/state_charging/20261020_c7_row_acceptance_v1`.
Local raw originals: [accepted evidence](evidence/c7-accepted-20261020/README.md).

- [Formal certificate](evidence/c7-accepted-20261020/cardinality_c7_accepted_certificate.json),
  SHA256 `bac5a4c242bd224cb2307acf0a255dde2a082d66cdea85fd4c2730e2ec964e60`.
- [Acceptance receipt](evidence/c7-accepted-20261020/campaign_acceptance_audit.json),
  SHA256 `347bcf377f53102316c091ebdf9cd415acbaa33ffbe1f52f47061531f791ec96`.
- [Current status](evidence/c7-accepted-20261020/current_status.json),
  SHA256 `568775f511b047f0414df3be68f9594a423a259402369314eff19b1b495b8d9a`.
- [Human authority](evidence/c7-accepted-20261020/human_acceptance_20261020_v1/human_authorization.json),
  [publication validation](evidence/c7-accepted-20261020/human_acceptance_20261020_v1/publication_validation.json),
  [output manifest](evidence/c7-accepted-20261020/human_acceptance_20261020_v1/output_manifest.json).

Certificate and receipt set c7_proved/theorem_credit=true and certified_upper_bound=28
only in the specified domain. Original pending SHA256 remains
`ea26adb07a4e17ca87bb6600a19c4fdb704911aacd773c8b38cca4a29dc78ee2`,
with false credit and null bound. Historical C6 remains accepted with its
original bound29, authority/provisional fields and certificate/receipt hashes.
Old campaign source/status/seal pending flags retain their historical meaning;
future row audits can resolve the predecessor through this new C7 receipt.

## Review assurance and limits

The fresh-context GPT verdict is `SUPPORTED_UNDER_STATED_REUSE_ASSUMPTIONS`,
assurance `SAME_FAMILY_PROVISIONAL`, with zero confirmed blockers or required
repairs. [Verbatim response](evidence/c7-accepted-20261020/human_acceptance_20261020_v1/001-c7-row-review.response.md)
SHA256 is `384dfe06dce3cda2caa779fe8a6679720574fab669cf866c69a2c399dd5266df`.
Exact request, root run metadata and original receipt are retained unchanged.
User authority accepts the disclosed limits but does not upgrade assurance.

Four existing C7 checks and accepted C1..C6 are reused premises. The review
checked local mathematics, sealed source, small bindings and complete checker
logs; it did not rerun solvers, checkers, tests or formula replay, or inspect
CNF/proof bodies. The 164 historical external Linux runtime dependencies were
not exported locally or independently revalidated, so original sealing and
replay records remain relied upon. Exact reviewer model/backend and actual
effort remain unknown/unverifiable; no cross-family independence is claimed.

## Engineering validation and preserved work

The publisher passed **19/19 focused Linux tests** in forktqiu3, zero failures,
errors or skips. Tests cover authority/quote/bound/domain/assurance/backend
mismatch, incomplete review, rejected C6 dependency, missing/duplicate or
mislabelled cases, binding drift, create-only behavior, no proof/CNF reads,
publication-last refusal and cross-file binding. All 21 manifested downloaded
publication files match server hashes. The 22-file archive SHA256 is
`6acc47fd9983d0a904191e57328293bec6b443208d3f57c684a46e7eaf4da712`.
Original row files are unchanged before/after publication.

Fresh checker replay0, formula replay0, formula/proof content reads0, fresh
proof hashes0, solver/checker invocations0; four checked cases reused. No new
review was called. No production encoding or existing run was modified.

C8/C9/C10 controller PID2438636, PPID2438548, start_ticks338655522,
boot34c2d313-2938-4220-ad0b-8a0018d3c7e8 remains live with identical argv and
seal SHA256 `1afccc3c827fff253c79d86e161a435a98dabd60eb51707cc2db2cfc32aef103`.
Post-publication read-only observation recorded prehash phase r08_e09,
42,379,247,616 of 66,340,299,391 bytes for that case, no pipeline error/exit and
no checker launched yet. The owned pipeline continues its authorized work;
no signals/restarts were sent. These observations are dated records, not live
claims. C8/C9/C10 row acceptance remains pending. No commit, push or task archive.

The [final wrap-up observation](evidence/c7-accepted-20261020/pipeline_wrapup_20261020.json)
at unix1792501924.2357383 records the same live controller identity, three
completed prehash receipts and active prehash r09_e09 at 8,858,370,048 of
109,692,548,932 bytes. No checker has started yet; pipeline error and exit
remain null. The process is waiting on I/O in that snapshot. This separate
dated observation does not change the sealed acceptance bundle or its manifest.
