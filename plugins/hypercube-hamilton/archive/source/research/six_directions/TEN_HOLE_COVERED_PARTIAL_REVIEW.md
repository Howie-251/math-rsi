# Covered ten-hole partial A8 transfer: independent audit

2026-11-01. ARIS proof-checker; reviewer `/root/higher_hole_transfer_audit`,
user-selected `gpt-6.1-sol / high`. Assurance: **same-family / provisional**.

**PASS for the six sufficient transfer rules and the complete stated-domain
coverage accounting, relative to the accepted imports.** The independent
census reconstructs all145,248,180 covered-target geometries. The previous
rules leave121,690; the six additions cover30,465 of these and leave exactly
**91,225 OPEN geometries**, split26,880 /29,955 /34,390 at v=1 /7 /31.
This is not a proof of complete ten-hole covered-target P6 or full P6.

No production proof, producer data or main claim state was modified. The
new reviewer files have the prefix `TEN_HOLE_COVERED_PARTIAL_REVIEW`.

## Accepted imports and fixed input boundary

The proof-bearing input is `TEN_HOLE_COVERED_PARTIAL_A8_TRANSFER.md`.
The JSON sidecar fixes its SHA256 separately from imported theorem/report
hashes, independent checker artifacts and compared producer files.

The accepted uniform transfer supplies its eight original ten-hole rows,
the conditional marked-T15 transfer and the forest/tag/suppression argument.
The complete eight-hole endpoint theorem includes covered targets and
therefore justifies the short augmentation before this census. K8 supplies
the arbitrary-K(Q5)-matching balanced-eight-hole cycle extension.

Only the accepted partial A8 claims are imported: delta1/2/3 cuts with the
marked majority forbidden hole, and the separately reviewed cut having all
five majority holes and exactly one minority hole on the forbidden side.
Both allow arbitrary long and same-parity required edges. The latter
requires no minority adjacency to a nonforbidden majority hole; that
hypothesis is verified explicitly in every application below. Neither full
A8 nor A10 is used.

For marked T15, the fixed previously accepted core registry specifies IDs
0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44,
with exact holes, omitted pair and whole-core PASS reports. The only other
accepted T15 family is the full split theorem: after translating the
minority to0, one coordinate has exactly two of the five majority holes in
its one-face and separates the two marked omissions. Both crossing counts
zero and positive are included. No unrestricted same-face shortcut is used.

The33 frozen theorem/review hashes from the accepted ten-free import
manifest were all rechecked; each referenced complete-core report is PASS.
The new accepted uniform/K8/partial-A8/delta-four reports were checked for
PASS and bound to current source/report hashes. Their large matching
certificates are imports, not claimed as rerun here. The producer programs
were read diagnostically but never called or imported by the reviewer.

## Quantified statement and mathematical ledger

For every short27-edge matching M on Q6, free root u and covered
opposite-parity target v, normalize u=0 and assume its nonroot even holes
Z and odd holes W are independent. Each of the six stated cut conditions
is sufficient for a Hamilton u--v path through M. The independent census
then gives the exact subset of this marked-hole domain accepted by the
union of old and new conditions. It makes no assertion on the other91,225
geometries' matching instances.

| ID | Obligation and discharge | Result |
|---|---|---|
| C01 | A Z--W short hole edge can be added without covering u. Full eight-hole P6 applies to the same root and covered target. Translation and target-preserving coordinate permutations normalize covered v to1,7,31. Root--W adjacency is allowed in the residual domain. | PASS |
| C02 | The no-crossing case uses the declared five-direction theorem on the original short matching. For positive crossings, parity counts and distinct ports are exactly those of the uniform transfer. | PASS |
| C03 | Local endpoint conversion: r,y,h are distinct since r is free and y covered. F-yh+hr is a matching with3+5 holes, omitted y. Its31-cycle minus hr is an r--h path; appending original hy gives a Hamilton r--y path. Only the artificial hr is removed, and all new edges relative to F are short. | PASS |
| C04 | In row(0,1), A has balanced2 completed holes. The no-bridge transfer yields B holes4+4, with its root consumed if it lies in B. K8 needs a cycle, not prescribed local endpoints, so its exact conclusion suffices. | PASS |
| C05 | In row(1,1), bridge the sole z in Z∩A. Its mirror y is internally B-covered by independence and a free mirror. The final B holes are precisely Z∩B (three minority) and (W∩B) union{y} (five majority), with y omitted. This is independent of root face and D. | PASS |
| C06 | In row(0,2), two W∩A sources exist and at most one has mirror u. The covered target is not a hole and excludes no source. A legal source leaves B minority W∩B of size3 and majority (Z∩B) union{y} of size5. The root is consumed separately, not included in this geometry. | PASS |
| C07 | Row(3,4): no bridge; completed A has4+4 holes. For u∈A take r=u. Otherwise the original port imbalance is1, giving an even port r. Removing r and adding v gives exactly minority Z∩A and majority (W∩A) union{v}. B is balanced1+1. | PASS |
| C08 | Row(4,4): choose even bridge source z. With u∈A take r=u and pair ports plus z; otherwise take r=z and pair all ports. Completed A has4+4 holes; after removing r, its minority holes are (Z∩A) minus{z} in both cases. Its majority holes after adding v are (W∩A) union{v}. B holes are0+2 and the marked omitted bridge mirror is one of them, so N14 applies. | PASS |
| C09 | Row(3,5): choose an odd bridge source with mirror different from u; five candidates and at most one exclusion suffice. With u∈B the even-port surplus is2, so a free even root port exists. Completed A holes are4+4. After root removal and v insertion, minority holes are Z∩A and majority holes ((W∩A) minus source) union{v}. B has2+0 holes and N14 omits the bridge mirror. | PASS |
| C10 | In the last three rows, v remains covered by the completed A matching: either its internal original edge or its D edge at an odd crossing port covers it. v is neither the even root nor any hole source. This verifies the covered-target hypothesis even if its temporary mate is itself a port or source. | PASS |
| C11 | In every displayed marked A8 geometry, minority and nonforbidden majority vertices are original Z/W vertices. Their nonadjacency is exactly the original independence hypothesis. The prescribed omitted vertex is y on B or v on A. The auxiliary admissibility cut ranges only over the five coordinates other than the outer cut. Both global majority parities are supported. | PASS |
| C12 | The last three rows repeat the completion and forest proof rather than invoking the old bound b≤3 as a theorem premise. That bound was only needed for the previous A endpoint import; the new4+4 endpoint conversion replaces it. All forest hypotheses survive. For u∈A, D is nonempty; for u∈B, possible D-empty boundaries are already included in the accepted tagged argument. | PASS |
| C13 | After the A path is supplied, deleting D and attaching crossings/one bridge leaves distinct B endpoints. A crossing target may temporarily be isolated and is then reattached. The artificial global tag joins separate terminal segments or extends to the B root. The sole bridge conflict has an original mate outside all transferred endpoints. Suppression, the exact B cycle, expansion and tag deletion preserve every original edge and the specified endpoints. | PASS |
| C14 | Each new rule's source and marked auxiliary cut depend only on holes and v; arbitrary D and the actual target mate need not be known geometrically. Imported arbitrary-matching quantifiers cover every realizing original M. The finite result therefore proves sufficient classes rather than sampled matching instances. | PASS |
| C15 | The accepted old T15 cases use exactly two actual bridge mirrors as omissions. Translating the actual B minority and deleting the outer coordinate gives the correct minority0 normalization. All permitted source pairs are tried; root-mirror sources are excluded. The lookup is rebuilt from fixed representatives under coordinate permutations plus the exact split condition. | PASS |
| C16 | The independent enumeration covers every nonzero even Z quadruple and every odd W quintuple with v∉W and no Z--W adjacency. It tests the full union of old and new sufficient rules, excludes no unrealizable matching geometry, and records every failure as OPEN. Exact residual sets, not merely cardinalities, match the supplied files. | PASS |

The dependency graph is accepted Q4/Q5 inputs -> partial A8/K8 and uniform
forest transfer -> these six rules -> finite marked-hole coverage. The
complete eight-hole theorem supplies only preprocessing. No ten-hole
covered theorem, full A8, A10 or higher P6 claim is fed into this graph.
There are no analytic interchange, limiting, probabilistic or asymptotic
obligations in this finite combinatorial argument.

## Independent exhaustive accounting

The new Python checker reconstructs coordinate-permutation orbits using
adjacent coordinate swaps from the fixed24 accepted marked core
representatives. Their union has1600 marked geometries. It independently
enumerates the full split condition on all marked five-subsets, obtaining
31,640 geometries. The union has33,240 entries. No producer lookup file,
residual input, dynamic core ledger or cached producer census is used.

The new C++ checker reverses the producer's parity order: for each v choose
every W quintuple from the31 odd vertices other than v, then every Z
quadruple from all nonzero even common nonneighbors. There is no test
excluding adjacency to root0. Its nested combination bounds enumerate each
set exactly once. It performs no matching-feasibility test.

| v | Complete domain | Eight basic rows | Old marked T15 | After old rules | Newly covered | OPEN |
|---:|---:|---:|---:|---:|---:|---:|
|1|47,316,060|46,657,325|621,485|37,250|10,370|26,880|
|7|48,840,660|48,127,161|674,349|39,150|9,195|29,955|
|31|49,091,460|48,332,075|714,095|45,290|10,900|34,390|
|Total|145,248,180|143,116,561|2,009,929|121,690|30,465|91,225|

All counts are a disjoint accounting in the stated order of rule tests;
multiple sufficient witnesses can exist for one geometry. The new coverage
by first successful rule is:

| Cut rule | v=1 | v=7 | v=31 |
|---|---:|---:|---:|
|(0,1), K8|370|318|410|
|(1,1), marked B A8|6990|5850|7170|
|(0,2), marked B A8|750|648|750|
|(3,4), marked A endpoint conversion|2100|2196|2340|
|(4,4), marked A endpoint conversion|100|102|140|
|(3,5), marked A endpoint conversion|60|81|90|

The C++ checker retains a concrete outer cut, source when applicable,
inner admissibility coordinate and imbalance for each of the30,465 new
geometries. A separate Python pass replays every witness from original
labels, checks the six actual local hole formulas, role distinctness,
nonforbidden nonadjacency, and the marked-face predicate. All pass. Of
these,1098 use K8; the remaining29,367 use selected A8 witnesses with
imbalance1:231, imbalance3:14,970 and exact5-majority/1-minority
imbalance4:14,166. These are witness-choice counts, not new A8 theorems.

The independently generated OPEN files use a different enumeration order.
For each v the checker checks nine-byte record alignment, no duplicates,
the exact expected count, and equality of the complete sorted record lists
against `ten_covered_after_partial_a8_v{v}.bin`. All three sets agree exactly.
The report JSON binds both raw file hashes and canonical sorted-record hashes.
Producer residual files serve only as post-computation comparison targets.
No feasibility exclusion was used anywhere in the independent census.

## Adversarial boundaries and decision

Counterexample candidates tested analytically were a bridge into root0,
an A target that is a crossing port, a D mate used by the endpoint swap,
a root represented by the consumed source in row(4,4), no even port in
row(3,5), an auxiliary admissibility test accidentally using the removed
outer coordinate, an unmarked or wrong-parity A8 theorem, D empty, and a
same-face T15 shortcut. The explicit source exclusions, exact port surplus,
completed-hole identities and accepted tagged forest proof resolve them.
The complete-domain and witness checks independently catch the coordinate
and marking errors. No counterexample or open issue was found in the
claimed sufficient scope.

All16 obligations pass. The91,225 remaining marked geometries are open
obligations for every realizing original matching, not counterexamples or
automatically realizable cases. Full ten-hole covered-target P6, full A8,
A10, all higher Q6 layers and full P6 remain outside this verdict.
