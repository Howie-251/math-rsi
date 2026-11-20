# N(m,r,s) incremental research handoff — 20 November 2026

This archive freezes the 18–20 November increment after the 17 November
archive integrated by PR #44. It delivers complete working manuscripts and
selected finite evidence, not a new acceptance of the mathematical results.
The latest two entry manuscripts are the [macro portfolio](research/NMRS_MACRO_PORTFOLIO_20261120.md)
and the [sector-deficit proof and corollaries](research/NMRS_SECTOR_DEFICIT_COROLLARIES_20261120.md).
Both state that the new analytic chains remain **unreviewed and unaccepted**.
The source snapshots, byte identities and publication transformations are in
[INVENTORY.json](INVENTORY.json); [SOURCE_MAP.md](SOURCE_MAP.md) locates imported
and omitted dependencies. Scientific execution belongs to Linux. Packaging
and checking file identities do not create new solver or proof-checker runs.

## Object and current working bounds

An input is a complete ordered rank-3 signotope: each increasing triple has
one of two colors, and each increasing four-point packet changes color at
most once. Paths count vertices. The capacity N(m,r,s) is the largest
population avoiding a blue r-path, a red s-path and weak m. A weak m consists
of two opposite-color paths with the same actual first and last vertices,
whose vertex counts sum to at least m+2. No extra disjointness assumption is
added to that definition. Let Q_m=N(m,m−1,m), F_m=N(m,m,m).
The imported R20 chart/extension proof gives F_m=Q_m+1; geometric inclusion
then gives ES(m)≤F_m+1. These are separate mathematical bridges.

| m | Q_m | F_m | ES(m) working consequence | Status and readable proof |
|---:|---:|---:|---:|---|
|7|≤75|≤76|≤77|Unchanged from #44; [common-root/lock replacement proof](../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md). No new universal 74-point exclusion.|
|8|≤292|≤293|≤294|[Complete same-lock and common-budget proof](research/N8_F298_ES299_20261120.md), §§2–7. The filename retains the earlier F8≤298 target.|
|9|≤1098|≤1099|≤1100|[Sector-deficit manuscript](research/NMRS_SECTOR_DEFICIT_COROLLARIES_20261120.md), §4; imports ordinary 977≤222 and 978≤380 from #44.|
|10|≤3978|≤3979|≤3980|[Same manuscript](research/NMRS_SECTOR_DEFICIT_COROLLARIES_20261120.md), §7, including the 420-point equality exclusion and ordinary imports 773/1372.|

These are conditional-on-import working proof chains, with no claim of
sharpness, literature priority, geometric realization of abstract witnesses,
Lean verification or independent mathematical acceptance. Older included
snapshots retain their historical numbers; this table identifies the active
assembled bounds. In particular, the older 307/308/309 and 1146/1147/1148
assemblies are not the current best working chains in this source project.

## The reusable structural result

For 6≤m≤10, fix one actual Q_m input. Let S be its red (m−1)-sources,
B its blue (m−2)-sources, O the complement of S∪B, and let b=|S∩B|,
p=|O|. Use proved upper bounds u≥N(m,m−2,m−2),
t≥N(m,m−2,m−1) for the **same m**. A mixed owner in
K=S∩B∩End_R(m−2) has a unique actual lock: every long red path ends
there and every long blue path uses it as second vertex. Different owners
may share a lock.

For every distinct lock q, choose the last owner in all of K and retain
**all** possible penultimate vertices V_q of its long red paths. The
actual induced sets I=(S∩B)\K and Y=(O∪K∪⋃V_q)\L satisfy

\[
\delta=u+t-b-p
=(u-|I|)+(t-|Y|)+\sum_q(|V_q|-1)+|L\setminus O|\ge0.
\]

The four sectors of the same actual outgoing-state diagram have exact
ordinary-row multiplicities m−2, m−3, 1, 1. If ρ is total ordinary-row
slack and ε=t−|B\S|, the resulting exact budget is

\[
(m-2)n+\rho+\epsilon+(m-3)\delta
=(m-1)\binom{2m-7}{m-4}+(m-3)u+(m-2)t.
\]

The [full proof](research/NMRS_SECTOR_DEFICIT_COROLLARIES_20261120.md),
§§1–3, includes empty K, all-path quantifiers and population identities.
For m=8, u=56,t=100, this alone gives Q8≤293; the separate common
exchange argument excludes 293 and gives 292. For m=9, u=222,t=380,
the right side is 7688 and floor(7688/7)=1098. For m=10, the
same-parameter imported pair u=773,t=1372 gives 31831 and
floor(31831/8)=3978. Arithmetic checks cannot replace these actual-set
proofs or their imports.

## What the finite evidence supports

The [replay instructions](REPLAY.md) and [verification report](VERIFICATION.md)
state the commands actually run for this delivery and the exact finite
predicates checked. The finite data are selected inputs, not the complete
multi-gigabyte solver archive. The [publication projection register](evidence/PUBLIC_PROJECTIONS.json)
separates original receipt hashes from redacted export hashes. Those JSON
projections retain scientific numbers, hash bindings and historical solver
process metadata; they are not byte-original receipts.
Five inspection source snapshots also replace private paths with neutral
placeholders; their original and exported identities are recorded separately.
They do not form a self-contained runnable historical builder runtime.

| Evidence | Historical guarantee retained | Delivery limitation |
|---|---|---|
|Ordinary 866≤56|One full DRAT success; an independently generated complete CNF has the same bytes. The [frontier manuscript](research/N8_FRONTIER_ADVANCE_20261120.md), §§1–2, connects every hypothetical 57-point input to that CNF.|Large CNF and DRAT omitted. Receipt consistency in this delivery is not another DRAT run or an independent proof of the original-input encoding bridge.|
|Ordinary 858≤64|Two actual DRAT processes using the same checker implementation; independent complete CNF rebuild. [Original-input bridge](research/evidence/n8-d122-common-bridges-20261119/NEAR65_SEMANTIC_BRIDGE.md) and [proof entry](research/evidence/n8-d122-common-bridges-20261119/ORDINARY858_64_VERIFIED.md).|Large CNF and DRAT omitted. The two historical checker runs are not two distinct checker implementations.|
|17-point common-lock input|Complete original triple coloring; two genuine owners share a lock. [Actual fan and separation proof](research/n8-same-lock-298-20261120/ADVANCE.md).|An abstract example, not a 292-point input, geometric realization or upper-bound proof.|
|Five-column window certificates|Exact all-face inequalities for retained heights 44,45,48,56,64, with a repaired rational denominator at 64; same-input subset transport and integer lift.|Finite certificate replay verifies the stated inequalities. The original endpoint/face bridge remains mathematical, and capacity optimality is unproved.|

The 866 CNF has 543459 variables, 41049536 clauses, 1920462700 bytes and
SHA256 `0db0b5dee1bc578115b448cc841d8b57d5671d9eff53e42d7fdc0fec707b36bc`.
Its 2608906477-byte DRAT has SHA256
`8f3f6750b5c67d005605339a077cedbe0432122e6743e23ab0ce65a83940e087`.
These hashes identify omitted originals; they do not permit a standalone
DRAT replay without obtaining those bytes. The archive has no public
download service for those large files.

## General windows and the honest comparison

The [final window manuscript](research/NMRS_WINDOW_ADVANCE_20261120.md), §6,
transports the same actual marked four-faces through all height subsets.
It defines A44=62044 and uses
Ah=max(ceil(h A(h−1)/(h−4)),ceil(Wh)) at the retained seed heights.
For every v≥1024 this proves the working coefficient

\[
p\ge\left\lceil
\frac{20966536167}{227725146880}\binom v4
\right\rceil.
\]

The same p,q enter the original ordinary-row inequality. After giving the
old 44-height seed the **same integer lift**, the new H gains at
v=64,100,128,256,1024 are respectively 127,1411,4508,93573,28259503.
This is improvement over that named old envelope, not an optimum over all
known inequalities or a direct improvement of the small-m diagonal bounds.
The finite v=44 union result N(50,7,47)≤2103267 remains separate: its
red-hole union saving cannot be transported at unchanged cost. The
[integer-lift source manuscript](research/NMRS_WINDOW_INTEGER_LIFT_20261119.md),
§§9.2–9.4, proves the necessary mixture correction.

## Failed routes and the next mathematical obligations

The active next question is whether shared locks, few penultimate choices
and almost-full ordinary rows can coexist in one actual high-population
input. The [portfolio](research/NMRS_MACRO_PORTFOLIO_20261120.md), §§4–5,
orders the directions and states their remaining quantifiers.

1. At the eight-parameter 292 layer, the older scalar system leaves 6126
   types. It forces simultaneous 56/100 subdomains, singleton V_q, at least
   five full faces and at least 68 frozen **point ideals**. The [scalar proof](research/n8-penultimate292-20261120/PROOF.md)
   is a relaxation, not a signotope construction. Later interval separation
   gives 5|L|≤|B\S| and removes its 19-lock types; it does not exhaust 292.
   At nine-parameter 1098, ρ+ε+6δ=2, so δ=0 and at most two rows are
   unsaturated. A proof of δ8≥6 on every actual 289-point Q8 input would
   yield Q8≤288; δ9≥11 on every 1089-point Q9 input would yield Q9≤1088.
   **Both are open.** Roles must be recomputed after restriction.
2. An improved ordinary 866 bound can be used on every relevant face.
   The [Horn extension manuscript](research/NMRS_RIGHT_EXTENSION_HORN_20261120.md),
   §§8–11, retains two real 50-point calibrations: a long cut jumps from
   zero to twenty permanent holes, while all two-end boundaries of length
   at most twelve still only bound population by 70. Complete seven-point
   templates produce no weak8 catalogue gain; the old all-rejected claim
   was corrected to four compatible cases. Template proliferation lacks
   the universal anchor/coverage argument.
3. For seven parameters, a universal ≤24-point transversal of **all** red
   six-path supports in every 74-point input would yield Q7≤73. The
   [component proof](research/N7_74_CRITICAL_COMPONENT_DELETION_20261118.md)
   and [critical-product return](research/N7_CRITICAL_PRODUCT_RETURN_20261118.md)
   preserve the unresolved 6×12+1 and 5×12+13 shared-choice cases.
   Individually possible marked extensions do not give a common extension.
4. The [old D9 trace certificate result](../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)
   contains a feasible exact fractional point for all 47635 rows; merely
   reweighting that LP cannot improve its integer-rounded hole bound of
   124. New path support, an integer cut or a new same-lock constraint
   must also be compared with the active Q9≤1098 chain.

## Freeze, exclusions and recovery

The manuscript freeze is recorded file by file in [INVENTORY.json](INVENTORY.json).
It includes the two final 20 November syntheses, full 8/9/10 working
proofs, their imported #44 manuscripts, the final window chain, and the
selected local failures above. Included historical dependencies are reading
material, not an instruction to resume their searches.

No success for ordinary 858≤63 was locally received by the source
portfolio's last 13:40 Singapore-time query. A generator had finished and a
checker was last observed running; connection failure yielded no newer
terminal evidence. Thus this freeze uses **858≤64**. Any copied 63 proof
draft/runbook remains preparatory and carries no extra bound credit. No
later external-job state has been inferred. Historical reviewer requests
failed before mathematical feedback; session data are excluded, and no
independent mathematical review has been started by this packaging task.

This is a publication excerpt package: links are relocated, machine roots
and connection identities are redacted, manuscript process-control lines
are omitted, and every transformed
manuscript is labeled. Original SHA256 identities are retained; exported
bytes are not claimed identical to private originals. No credentials,
private endpoints, session transcripts or compressed archives belong in
the committed increment. Old dependencies continue to use the unchanged
17 November archive. Start a new review from the complete original-input
bridges, row/compression imports, same-lock proof and R20 outlet before
accepting any assembled numerical theorem. No Goal is created or resumed.
