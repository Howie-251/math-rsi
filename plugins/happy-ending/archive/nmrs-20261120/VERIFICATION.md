# Verification scope — N(m,r,s) update

## 2026-11-21 macOS portable replay

The corrected standard-library entry completed with exit 0 and
`status=PASS_BOUNDED_EXACT_REPLAY` on macOS 26.5.2 arm64 / Python 3.14.6.
The rejected height-64 seed exited 1 with `ValueError: infeasible face`.
This executes all advertised finite checks, including the 981 recurrence
heights 44–1024, five named-envelope examples, both actual finite colorings,
6,126 supplied scalar types and saved-receipt consistency. It does not establish
scalar-list completeness, geometric realizability, mathematical bridges or new
DRAT checks. Linux execution remains pending.

The first actual run exposed a checker implementation error: it used the
maximum private-face service `P=44` where the transported red-hole cost requires
`a*max E`. The source manuscript
[integer lift, §§9.2–9.4](research/NMRS_WINDOW_INTEGER_LIFT_20261119.md)
specifies `a=5`, `max E=8.205564`, hence `a*max E=41.02782`.
The checker now reconstructs `E`, asserts its exact maximum and retains the
exact `41.02782` assertion. A separate forward-incidence implementation,
accumulating each weight onto every served endpoint face, independently found
maximum numerator 8,205,564 at endpoint `(8,8)`, denominator 1,000,000.
The correction changes the evaluator, not the supplied weights or manuscript
claims. The complete run then passed without further evaluator corrections.

Repository checks on the PR head also completed on macOS: 148 documents and
2,277 local links, zero missing; public staging build 81 files, 24,536,841 bytes,
exact allowlist and no broken local references. These checks do not publish.

## Original preparation record (2026-11-20)

2026-11-20. **New portable checks and final site checks remain unexecuted on
Linux.** This is an accurate preparation record, not an acceptance certificate.
The supplied program, representative inputs and exact commands are in
[REPLAY.md](REPLAY.md). Existing historical calculations keep their original
scope; no Windows scientific execution substituted for the unavailable server.

| Obligation | Material actually available | This preparation |
|---|---|---|
| New normalized-window certificate predicates and integer lift | Five final public seeds, historical seed/row/union weights, exact portable checker | source/input assembly complete; Linux replay pending |
| m=9 and m=10 numerical consequences | Exact combinatorial arithmetic in portable checker; source mathematical manuscripts | arithmetic checker pending; input-to-inequality mathematical bridges remain paper arguments |
| Actual finite coloring checks | Complete 36-point and 17-point color tables | full packet/path/shared-lock replay implemented; execution pending |
| Q8 common scalar envelope | All 6126 scalar records decompressed without mathematical modification; historical result | listed-type validation and all-h envelope implemented; execution pending; no 292-point construction |
| Ordinary 866<=56 | Successful original result/log, CNF/DRAT/source seal, byte-identical independent reconstruction, frozen sources | historical evidence retained; no new DRAT or reconstruction |
| Ordinary 858<=64 | Two actual successful checker processes, saved complete short logs, complete independent reconstruction, original formula/proof identities | historical evidence retained; no new DRAT or reconstruction |
| Ordinary 858<=63 | Preparation manuscript and last retained in-progress/failed-check evidence | no new successful checker retrieved; <=63 is not claimed here |
| Final repository links and public-site allowlist | Repository scripts and final prepared source | Linux checks pending |
| Independent mathematical review | Fresh requested read-only Claude review | REVIEW_UNAVAILABLE: CLI exited 1; no mathematical opinion or acceptance |

The review failure is a technical failure, not an adverse mathematical verdict.
No automatic retry, alternate reviewer, or acceptance upgrade occurred. The
private raw review trace is not included in this public archive.

The new portable program deliberately distinguishes receipt consistency from a
fresh proof replay, finite examples from universal upper bounds, and numeric
consequences from their structural mathematical hypotheses. Pending execution
also means its own implementation has not yet been validated by a successful
run. Its expected outputs in REPLAY are targets for the first replay, not a
fabricated run receipt.

Authoritative Linux access failed before any package upload or scientific
execution. Both the configured domain route and the previously recorded private
route were tested with unchanged strict host-key checking; sandbox escalation
did not restore connectivity. No global proxy, host trust, running solve, sealed
runtime or original proof was changed. Network/account details are excluded
from public materials. A compact public status is retained in
[checks/preparation-status.json](checks/preparation-status.json).

Historical successful DRAT records support their fixed formulas; their
application to arbitrary original signotopes additionally depends on the
supplied semantic bridges. The new general same-lock and sector-deficit
manuscripts and their downstream Q9/Q10 consequences remain working mathematical
results pending independent review. This delivery neither certifies optimality
nor geometric realizability of the abstract examples.
