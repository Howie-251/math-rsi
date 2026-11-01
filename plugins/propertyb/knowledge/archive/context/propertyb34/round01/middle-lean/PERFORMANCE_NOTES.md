# T34 Lean performance and reusable actual-input interfaces

Recorded 2026-10-14 Beijing. This is a continuation aid, not a theorem audit.

The 21-point seven-degree quad coverage first ended with system exit 137.
Splitting into 64 pair-vector declarations still exceeded 15 minutes; RSS
was observed near 8 GB before the owner terminated that exact process.
The retained logs are `../twentyone-lean/build-queue-TwentyOneSevenQuads-r18.log`
and `...-r19.log`. Both are incomplete runs, not accepted coverage evidence.

The suspected bottleneck is reduction of a sparse large-Nat pattern matcher.
An attempted explicit array on 15,552 encodings itself failed during data
elaboration after about 84 seconds with stack overflow (exit 134), before
mathematical coverage. The successful replacement uses `List.lookup` with
673 nondefault keys; the complete coverage domain remains 674 actual keys
and 70 representatives. Data r23 passed in 4.22 seconds total (Lean 3.1 s,
max RSS 1,855,127,552 bytes). The complete kernel r24 passed in 87.75 seconds
wall time (83.93 user seconds, max RSS 8,123,957,248 bytes), retaining all 64
chunks. See `../twentyone-lean/build-quad-kernel-r24.log`. The corresponding
actual four-lock residual theorem passed in r26. The old interrupted run
exceeded 15 minutes; it does not supply an exact baseline runtime or speedup.
The 23-point catalogue also uses a sparse association list with equality tests.

Separate Data, Numeric/Kernel and actual-caller modules. Changes to a binder,
API application or actual bridge should not recheck unchanged heavy formulas.
Lake still rebuilds genuinely affected dependencies; reuse is not a reason
to skip changed mathematics. One owner executes official heavy builds, while
other agents develop independent mathematics and source modules.

The root's four-lock extension now has six small coverage declarations per
family, rather than one giant Cartesian statement. The exact Python replay
`FOUR_PROMOTION_COVERAGE_REPLAY.json` records 460/167 capacity allocations,
246/66 positive-pair inputs and 73/48 orbits, with all transported counts
checked. These numbers name different domains. The complete Lean Numeric passed in r37 (46 s), and actual coverage plus
strict/residual classification passed in r39 (1.4 s and 10 s). All six
exported interfaces have only the standard three axioms. The 22+19 residual
profiles remain; no full 23-point coloring conclusion follows yet.

Reuse the following connections by actual need:

| Module | Mathematical responsibility | Evidence at this snapshot |
|---|---|---|
| LockProjection | Counts of every retained-lock trace sum all same-H fibers | r18 PASS |
| LockExtension | Actual old fiber splits by the new vertex; degree sum and singleton recovery | r19 PASS |
| LockRelabel | Exact same-H type counts under lock permutation | r8 PASS |
| BoundedAllocations | Every bounded, capacity-feasible vector occurs in recursive enumeration; list readback | r22 PASS |
| ActualAllocations | Actual high-trace counts satisfy containment capacities | r22 PASS, standard three axioms |
| PromotionCatalog | Actual promotions satisfy degree/codegree capacities and enter the sparse list | r22 PASS, standard three axioms |
| PromotionReconstruction | Complete new inventory, including empty and singleton, equals actual counts | r22 PASS, standard three axioms |
| LockLiftRelabel | Normalize the old locks while fixing the new last lock | r22 PASS |
| TwentyThreeFewLowBase | Actual one-/two-low triple has one of six inventories | r20 PASS, standard three axioms |

The first pure four-lock caller and Joint17 passed in r20. Their interface
was then expanded to 75 pure and 5 joint strict representatives, each exactly
replayed before export. The full Lean batch passed in r21 (Joint17 reused its r20 build); see
`FEW_LOW_FOUR_ALL_EXPORT.json`. This avoids generating a large batch against
an untested actual-input interface.

The unique-seven catalogue's 925 allocations also passed their complete
certificate module in 152 seconds (max RSS 10,737,713,152 bytes). Splitting
the expensive declarations from the small dispatcher meant that correcting
the append dispatcher did not repeat that computation. In the actual caller,
Lean next spent its heartbeats reducing `Matched values` with a symbolic
allocation. Giving the intermediate proof an explicit `Matched values` type
and setting `attribute [local irreducible] Matched` stopped this unwanted
unfolding; the proof later unfolds the predicate explicitly at the selected
branch. This is an elaboration optimization, not a changed theorem or axiom.
The actual caller then needed the dispatch extracted into a helper whose
`values : List Nat` is an abstract parameter; applying that helper to the
actual inventory prevents kernel deep recursion on the symbolic catalogue.
The complete unique-seven actual branch passed in r35: actual caller 1.7 s,
wrapper 1.5 s, only the standard three axioms. It is now incorporated in
Assembly and the independent `OneAudit.lean` (both PASS). A higher heartbeat limit or another copy of the same
build is not itself a reduction in proof work.

Grok and Gemini have both returned valid scoped source reviews for the new
promotion interface; neither executed Lean. They found no actual-input or
permutation-direction issue in the specified scope. See
`../reviews/PROMOTION_B_PACKET.md` and `REVIEW_DISPOSITION.md`. These reviews
do not imply the final T34 review or acceptance.

The user's final 30-minute work window runs from 17:36:37 to 18:06:37 UTC
on 2026-10-13. Existing branch assembly and builds take priority during it;
no new broad search, table expansion or review loop is scheduled. At the
deadline, stop and preserve actual acceptance status and exact remaining work.

The nine four-seven residual families were promoted through 3,618 complete
capacity allocations. Their separate certificate module passed in 357 s
(360.32 s for the full invocation, max RSS 8,989,097,984 bytes). Dispatcher
normalization, the actual core and the final two wrappers then passed in
1.5/1.0/1.3/1.3 s, without rerunning those certificates. `ManyAudit.lean`
and the updated Assembly both pass; the actual branch needs at least five
seven-degree vertices and no user-supplied profile or certificate.
