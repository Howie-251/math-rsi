<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Ordinary N(8,5,8)≤63: physical-input bridge and retained-proof recovery

Status on2026-11-20: **independent complete CNF reconstruction passed; the one
recovery DRAT and an authorized distinct parallel GRAT route are running.** This document is a prepared proof entry, not an
announcement that the bound has already passed its checker. No external review.
Only $m=8$appears here.

## 1. Exact statement, imports, and dependency boundary

The intended conclusion is that every finite complete ordered rank-3signotope
with no blue5-point path, no red8-point path and no same-end weak8has at most
63points. Paths count vertices; a weak8uses the same two actual outer vertices
and blue/red path lengths summing10. General-position planar inputs form a
subclass; abstract examples are not asserted geometrically realizable.

The following are mathematical imports to this finite formula. DRAT checks the
formula; it does not check these imported general lemmas.

| Import | Full hypotheses used here | Supplied conclusion/source |
|---|---|---|
| State injection/admissible chart | One actual ordered complete signotope; incoming pair ranks in $[a]\times[b]$; colored triple increases the corresponding coordinate | Ideals label physical points injectively; actual pair labels lie in target ideal minus source ideal. Base construction in [the existing bridge](../evidence/n8-d122-common-bridges-20261119/NEAR65_SEMANTIC_BRIDGE.md) §§2–3. |
| Coordinate deletion | Same actual physical subset selected by fixed included/avoided natural word coordinates; inherited labels satisfy the common-color growth rules | Actual colors and weak prohibition survive compression; one included coordinate in $3\times6$gives $2\times6$, one avoided coordinate gives $3\times5$. [Original proof](../../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md), not a claim that inherited labels are canonical true ranks. |
| Short-cap22 | Complete ordered signotope, no blue4, no red8, no weak8 | $N(8,4,8)\le22$. Existing Baek v2Theorem2.7import and adopted abstract-domain scope are recorded in [the source audit](../../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md). |
| Three-column50 | Complete ordered signotope, no blue5, no red7, no weak8 | $N(8,5,7)\le50$from [the full paper proof](../N857_SHARED_ROWS_NEXT.md). This is an existing same-session paper import; it has not become an independent theorem audit by inclusion here. |
| Native boundary traces | A valid ideal-chart difference with every column/row present and weakly decreasing heights across columns; its row/column joining chains are ideals | Every actual occupied subset is covered by opposite-color same-end paths. A trace of $a+b$states in the current weak8domain contains at most7physical points. [Complete argument](../../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-MOVE.md) §2, including missing extreme states and degenerate arms. |
| Horizontal compression | Each six-row map has its ordered thresholds monotone, with the explicit adjacent-row cross inequalities verified in the independent generator | Each28-state image is an actual $2\times6$chart and contains at most22points. General source-width proof is recorded in [C188](../N8_C188_311_20261119.md) §3; all24maps here are separately regenerated. |

The preliminary ordinary858≤66used among the rows follows directly by summing
the nine22-point coordinate faces: every3-word occurs in three faces, so
$3|X|\le9\cdot22$. It does not import the desired63bound. The50import is
likewise upstream of this formula. Neither ordinary866≤56nor aC8bound is used
to prove ordinary858≤63.

## 2. A hypothetical64-point physical input gives84states and20holes

Restrict any hypothetical larger input to64actual points. For an ordered
actual pair $x<y$, let $l_B(x,y),l_R(x,y)$be the maximum same-color path edge
counts ending with that pair. The path caps give

$$l(x,y)=(l_B,l_R)\in[3]\times[6].$$

Define the actual incoming ideal

$$P(y)=\downarrow\{l(x,y):x<y\}.$$

For every actual pair, $l(x,y)\in P(y)\setminus P(x)$. To see the exclusion
from $P(x)$, any earlier incoming pair whose label dominated $l(x,y)$would,
in the color of its joining triple, extend beyond that corresponding maximum.
Thus the64physical points have64distinct ideals among
$\binom93=84$possible3-by6ideals, leaving exactly20holes.

Comparable ideals must occur in their inclusion order. The CNF's total order
on all84states can extend the real physical order by inserting the holes.
Colors and path flags on comparable chains take their actual physical values;
constraints on these chains are only necessary restrictions of the complete
physical input. No converse realization of a satisfying necessary assignment
is assumed.

The true first two ideals are the empty ideal and the singleton. A label11can
leave only the first physical point: with an earlier point the joining triple
increases one coordinate. For the second physical point, outgoing pair labels
are12or21according to their shared triple with the first point. All such source
extent and first-pair restrictions in the formula follow from these actual
ranks, with holes deactivating physical clauses.

## 3. Exact incoming corners and shared missing outgoing corners

Every maximal cell of $P(y)$is attained by at least one actual incoming pair.
For every possible predecessor state $a$, target state $b$and permitted cell
$g\in I_b\setminus I_a$, a corner flag allows that actual order and exact pair
label. Incomparable source/target ideals are included. On a true input set
precisely its actual attaining flags true; pair uniqueness and all incoming
corner disjunctions then hold together.

For each physical point $x$and each minimal outside cell $g$of $P(x)$, define
`missing(x,g)`exactly when no actual outgoing pair has label $g$. Set missing
flags false at holes. This uses the same actual $l$labels throughout.

Let

$$Q_l(x)=G\setminus\uparrow\{l(x,z):z>x\}.$$

If $g$is a missing minimal outside cell, then $g\in Q_l(x)$: if some outgoing
$l\le g$, its exclusion from $P(x)$and the minimality of $g$force $l=g$.
For all physical points one may simultaneously replace $P(x)$by any ideal in
$[P(x),Q_l(x)]$. Every fixed outgoing label stays outside its source; every
incoming label stays inside its target. Therefore the same actual colors still
satisfy their strict growth rules and the modified chart remains injective.
This is a common actual-label chart operation, not a simultaneous choice of
independent extremal models. It does not assume actual forward $u=l$or a frozen
66-point chart.

## 4. Every missing-angle and entry charge lifts to the original input

Write each ideal as a three-subset word of $[9]$. Adding a minimal cell replaces
one natural coordinate $j-1$by $j$, with $j$previously absent from that word;
distinct addable cells of the same point introduce distinct $j$.

Fix$j$. Simultaneously add all missing cells introducing$j$at their physical
points. The preceding interval argument makes this one legal common chart.
The coordinate-$j$face has28possible states, compresses to an actual2-by6input,
and has at most22physical points by the short-cap import. Consequently

$$h(F_j)\ge6+\#\{\text{missing cells introducing }j\}.$$

Summing over the nine coordinates, each of20holes is counted three times, so
the total missing-angle count is at most$60-54=6$. The CNF encodes each stronger
individual coordinate inequality; no full-freezing inference is made from this
six-angle total.

For every valid pure-hole support$S$with demand$d$, let$Entry_S(x)$mean that
$P(x)\notin S$but at least one missing minimal cell would move$x$into$S$.
Choose one such cell per entry point and move all of them in the same fixed-label
chart; leave already occupied$S$states alone. Injectivity gives precisely
one new occupant per entry point. Therefore

$$h(S)\ge d+\sum_x Entry_S(x).$$

One Boolean ORper physical point prevents counting multiple usable angles
twice on the same row. Across different rows these are separate universally
valid inequalities on one shared hole/missing vector, not claims that different
chosen modifications must be performed together.

The563supports comprise all native mother/single-coordinate traces, coordinate
capacity faces3-by6(cap66),3-by5(cap50),2-by6(cap22), and the24ordered horizontal
2-by6images(cap22). The independent source regenerates every support and demand
using the complete formulas, rather than trusting a source-provided list hash.

## 5. Prefix/color/path constraints cover all actual64-point inputs

The first six actual points produce one of the$2^{20}$triple-color masks.
Exactly908masks have legal four-packets;843also avoid blue5. The independent
enumerator recomputes incoming pair ranks for all of them, their six actual
ideals and colors. A genuine64-point input selects its own one of these843
records. Its first six points really are first, so the prefix-shadow exclusions
are valid. No reverse prefix, last-point rank or future saturation is imported.

Every active physical packet uses one actual four-point packet. One-way blue3,
blue4and red-path flags take the truth values of actual path existence in the
encoded comparable domain. Red7with blue3at the same ends, and red6with blue4at
the same ends, are excluded because their lengths sum10. The blue5/red8caps
already follow from the actual pair ranks. Thus these are all relevant weak8
splits; auxiliary one-way flags do not need to prove spurious existence.

The special incoming corner with red coordinate1and blue coordinate greater
than1also forces a true blue3from the physical first point: its source cannot
be first, and the joining triple from any earlier point must be blue since a
red triple would raise the red incoming coordinate. The encoded implication
is therefore valid for the same actual corner witness.

All cardinality counters encode the inequalities just proved and admit their
usual auxiliary assignments. Hence every hypothetical64-point original input
lifts to this exact necessary CNF. UNSAT of that CNF would exclude every such
input; SAT of this relaxation would not establish an actual input.

## 6. Actual finite bindings and completed independent reconstruction

Original input directory:
`<private-artifact-root>`.

| Artifact | Binding |
|---|---|
| Exact CNF |298511variables,5187264clauses,170803254bytes; SHA`3754079cd7a76f18d12bfce74d00fa6fdb39ba145c91308337a9356c83e737a6`|
| Original source |SHA`07116610434f2be0efcdfe0da26cc2e5099ccd38f5ea2f268644c11402f5c15f`|
| Complete original proof |9327117152bytes; SHA`15bf2b1ee800eab71daba8916a53c21cf022102c6712022df56829dc9eafdbde`|
| Original solver/checker |Solver20; original old checker−11. Original receipt remains unchanged and incomplete. |
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
| Independent result |[Complete receipt](../../SOURCE_MAP.md#excluded-sources): all215369semantic IDs and all clauses regenerated; exact CNF SHA matches,13.405851654seconds. No second checker in this program. |
| Exhaustive prefix library |1048576masks→908packet legal→843no-blue5; SHA`966b628d3e00ae1ff5c4edc5de76c44bc3fce4237a41c190c76f02dcc452e783`|
| Independently regenerated row source |563supports/24maps; SHA`09cf47edcfd71e04095033b152c3e39eaa87e8bbcc65a66749aebec5631f620d`|

## 7. Recovered checker and distinct GRAT route: terminal acceptance pending

The old source's32-bit `RATset`cannot safely address all large proof-database
offsets; the project already has a validated September14repair. This run copies
that existing source and binary into a new directory; it does not replace any
sealed checker or modify the original CNF/proof.

Fresh run directory:
`<private-artifact-root>`.

Fixed binary SHA`0e0b9f7e0aa78ce2f4f970676407d95eae6908dff2b48af212f885d137374787`;
source SHA`ada55215f76b5ffe3af03be7e7259c75c855a3ee61603e80c260df4144b032de`.
Both match the retained[18-test validation](../../SOURCE_MAP.md#excluded-sources),
including actual high-offset/ASan and invalid-proof regressions. The actual
[launch binding](../../SOURCE_MAP.md#excluded-sources) records checker PID/PGID3833744,
started2026-11-20 03:18:39.869091UTC. Exactly one recovered checker is running.

The controller will accept only actual exit0, exactly one`s VERIFIED`and
unchanged before/after hashes of CNF, proof, fixed binary and source. On current
evidence those terminal conditions have **not** yet occurred. Its original
proof is complete and has been entirely parsed; parsing is not proof acceptance.
No solver rerun or external review has been invoked.

Upon actual success, attach the exact terminal result/log/hash receipt here;
then §§1–5plus this finite replay yield ordinary858≤63. That is one actual
successful replay over an independently reconstructed formula, not two proof
checker runs or an independent mathematical audit of the imported lemmas.

## 8. Caller connection after genuine completion

Only after §7succeeds, combine this63bound with the caller's separately bound
ordinary866≤56and C8≤187. In every real R7residual$D$, let$U$be its red6endpoints
and$A=D\setminus U$. The real residual junction excludes blue5from$U$in the
whole residual, so$U$is an ordinary858input;$A$has no red6and is ordinary866.
Therefore$|D|\le63+56=119$. The actual R7partition gives

$$Q_8\le187+119=306,\qquad F_8=Q_8+1\le307,\qquad ES(8)\le F_8+1\le308.$$

The last equality/+1and geometric containment are the caller's existing R20
transport imports. No geometric realization of the finite necessary formula
is needed for this upper-bound direction. Until the real recovered checker
succeeds (or the independently checked GRAT route below succeeds), this last
display remains conditional, not an achieved theorem.

## 9. Authorized distinct parallel GRAT route

After reading the installed trusted toolchain and its actual past pilot
comparison, the caller explicitly authorized this genuinely distinct route;
the existing fixed DRAT continues. No second drat-trim was launched.
The already installed GRATgen/GRATchk binaries match their October23validated
hashes. The historical10.8GBASCII pilot completed generator+checker in1410.685s
with8threads, versus its historical9677.519sDRATbaseline; this is observed
comparative evidence with stated cache/concurrency limitations, not a timing
promise for this different9.33GBbinary proof.

Actual strict binary census found111167998addition records,114347895deletions,
2285896831addition-literal occurrences, maximum variable301660, maximum clause
length852and a final empty addition. Including the5187264CNFclauses gives
116355262monotonic IDs, safely within signed32. The raw database upper bound
is2551505255four-byte words,10206021020bytes; it exceeds the old32-bit database
offset boundary and fits the installed GRATsource's64-bit position type.

The scanner passed actual valid/malformed/truncated/negative-zero/overflow
fixtures. A separate genuine small binary-DRAT inference was converted by the
installed generator and independently checked by installedGRATchk; an invalid
binary proof was rejected. This supplements the existing18-test process/tool
engineering gate, including exact semantic-error status rejection.

The conservative16-thread model is261802760384bytes, below the320GiBaddress
limit. The measured admission had506763329536bytesavailable memory and
2480302366720bytesfree disk, with64GiBmemory and256GiBdisk reserves. The pipeline
uses16generator threads, a254gMLton heap cap, resource monitoring, real executable
identities, process-group/PDEATHSIGhandling and no wall-time limit. Its process
execution function is reused unchanged from the previously18-test-validated
October23controller. All new artifacts are in a fresh directory.

Actual detached controller PID3848781; output root:
`<private-artifact-root>`.

The generator command uses the **original** bound CNF and binary DRAT with`-b`,
split lemma/proof outputs and`-j16`. Only normal generator exit0with exact unique
`s VERIFIED`, unchanged tool/input hashes and nonempty sealed outputs dispatches
the distinct independent checker. Only normal checker exit0with exact unique
`s VERIFIED UNSAT`, all input/output/tool hashes unchanged and the completed
independent CNF reconstruction matching can publish the final result.
Generator success alone grants no theorem credit. This terminal result is
currently pending.

Actual admission and smoke command receipts are
[the census gate](../../SOURCE_MAP.md#excluded-sources),
[binary inference/rejection gate](../../SOURCE_MAP.md#excluded-sources), and
[detached launch](../../SOURCE_MAP.md#excluded-sources). The controller source is
[run_grat.py](../../SOURCE_MAP.md#excluded-sources). Upon combined success this route independently
certifies the same CNFand §8conclusion; it need not wait for the older slow DRAT
process to finish, and its different checker semantics must be reported accurately.

## 10. Resumed caller: F8≤306 and ES8≤307

The new user target resumes both existing routes to completion; it does not
authorize duplicate solves/checkers or external review. At2026-11-20
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
forward pass. No terminal verdict had occurred.

Once one full route proves ordinary858≤63, combine it with the completed
ordinary866≤56import to obtain real residual$D_8\le119$. The caller's newer
[actual macro theorem](../N8_F307_ES308_20261120.md) §§3–6proves, for the real
R7partition of **every**Q8input, that$|H|=187$implies$|D|\le104$.
Together with C8≤187this gives the sharper case split

$$|H|\le186\Longrightarrow|X|\le186+119=305,$$
$$|H|=187\Longrightarrow|X|\le187+104=291.$$

Therefore the completed ordinary63certificate plus that paper macro would yield

$$Q_8\le305,\qquad F_8\le306,\qquad ES(8)\le307.$$

This consumes the macro exactly on its R7-definedH; it does not claim an
unconditional C8≤186bound. The macro remains the caller's unreviewed paper
import, and the pending finite checker has not yet supplied ordinary63.

## 11. Later caller release

The caller's stronger common-budget paper proof now yieldsF8≤300/ES8≤301without
ordinary63. Both already launched proof routes remain unchanged as separate
ordinary-capacity work. At04:15:41UTCfixed DRATwas5.48%and GRATwas in16-thread
backward checking; neither had a terminal verdict. This entry remains pending
until its own actual terminal evidence is collected, regardless of the separate
global numerical proof.
