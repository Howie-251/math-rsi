# Independent ARIS review: actual Q6 application of 111 new marked local inputs

2026-11-01. Reviewer `/root/higher_forced_cherry_review`, user-directed GPT-6.1-sol/high, ARIS proof-checker. The reviewer did not produce this application. **Verdict: PASS modulo the explicit accepted inputs and transfer imports.** Review independence is **same-family**; acceptance is **provisional**. No open mathematical gap remains in the sufficient application or exact new residual. No producer or production-state file was edited.

## Accepted statement and exact result

From the three accepted upstream files totaling **215243 covered-target** twelve-hole geometries, the selected **111 independently accepted marked Q5 local inputs** give a Hamilton root–target extension for every original short matching realizing each of **177838** sufficient source records. Exactly **37405** original-label records remain as obligations. There is no matching-realizability exclusion and no favorable-matching choice.

| Covered target | Accepted input | Sufficient records | Exact remaining |
|---|---:|---:|---:|
| 1 | 59684 | 51652 | 8032 |
| 7 | 68385 | 56724 | 11661 |
| 31 | 87174 | 69462 | 17712 |
| Total | 215243 | 177838 | 37405 |

The three `TWELVE_NEW_TYPES_positive_remaining_v{1,7,31}.bin` files are the byte-for-byte source-order complements of the sufficient records. All records in this scope have covered targets. This review does not assert full twelve-hole Q6, any subsequent complete higher layer, or full P6. The 37405 records are open obligations, not counterexamples.

## Frozen inputs and dependency gates

Proof SHA256 `f34d54935c9d88ab87cdc2c961b083dbfb0da1ec43e57f0d107eb78b36dc3159` and manifest SHA256 `8c6893cd3499e99d7ece3f0c06c196c338a1eeb98fa2f8e43da31b561bc6c3f0` match the requested frozen inputs. All **21** manifest file hashes and sizes were checked and remain unchanged after review.

The final local acceptance is `TWELVE_NEW_TYPES_LOCAL_REVIEW.json`, SHA256 `660364dc26183230bc5421c6aaaf73df5000c2a42477a7eda03ee4ebae3ece88`, accepting exactly the ordered 111 indices and their actual marked geometries. The final source-domain acceptance is `HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json`, SHA256 `36a07f7fc4b6c5c37551ed30208beaddf46aa871efd1ca5e85552d5c0905b590`. Its three output hashes agree with the exact source files here. Both final reviews, their direct proofs, and the accepted uniform-transfer/endpoint gates are pinned in this review JSON. Frozen producer fields saying that local acceptance was pending are provenance from before that independent acceptance, not the current gate status.

The mathematical DAG is: accepted source domain + exact 111 accepted universal marked local theorems + accepted uniform cut transfer/allowed balanced endpoint inputs -> legal actual cut/source sufficient witnesses -> exact sufficient source subset -> raw residual complement. There is no backward dependency on a desired twelve-hole theorem. Large local rank certificates and earlier domain censuses are explicit accepted imports and were not rerun in this application audit.

## Independent geometric registry reconstruction

The source registry/summary geometry is checked against the final local review for every selected index, including type, minority, majority and marked omissions. Selected index order is exactly that accepted by the local review. No extra local theorem is silently inferred from a producer full_rank flag.

For synchronous marked lookup, independently generate all coordinate permutations and translations taking a source anchor to 0. Use each minority vertex as a possible anchor when the minority is nonempty; otherwise use each marked omission. Apply the **same** map to minority, majority and omissions. For a runtime actual geometry, translate its smallest minority vertex to 0, or its smallest omission if minority is empty. Including every allowable source anchor before coordinate permutations makes this normalization complete for the listed common cube images. Empty-minority T84/T105 inputs are therefore handled without referring to a nonexistent minority vertex or moving U independently.

The 111 accepted inputs generate **24930** normalized marked lookup keys. As a supplementary finite set comparison, the 232 producer-labeled full-rank geometries generate **59860** keys. The latter is only a registry of explicitly listed geometries; this review does not accept the other 121 local theorems or any negative rank classification. Their finite projection hit sets can nevertheless be compared with those of the accepted 111 inputs. Lookup collisions were checked for identical source index/type. No exhaustive classification of all Q5 geometries or proof of greedy optimality is needed.

## Independent full-domain checker

`TWELVE_NEW_TYPES_APPLICATION_REVIEW_check.cpp` was freshly written for this application. It reads the reviewer-generated marked lookup and the original eleven-byte source records; it does not execute or include the producer coverage/profile/search programs. It also reads the frozen witnesses and residuals for independent comparison, not as sources of membership decisions. Reproduction in this directory:

```
g++ -std=c++17 -O3 TWELVE_NEW_TYPES_APPLICATION_REVIEW_check.cpp -o TWELVE_NEW_TYPES_APPLICATION_REVIEW_check.exe
./TWELVE_NEW_TYPES_APPLICATION_REVIEW_check.exe
```

The checker verifies source alignment, sorted Z5/W6 labels, correct parities, distinct vertices, free root 0, covered odd target and nonroot independence. Duplicate source records within each file are rejected. It independently tries every target-facing coordinate cut and every legal source subset in the four stated shapes, deletes only the outer cut coordinate, and builds the actual minority/majority/omission masks. The selected and supplementary registry predicates are both derived from those actual masks.

Results:

- **888571** legal source projections were checked, split T28/T19/T84/T105 as **295285 / 228605 / 299450 / 65231**.
- All **177838** selected 28-byte witnesses were replayed against their actual source records. Headers, target/index/cut/source mask, selected accepted index, type and all three stored actual projected masks agree. Exactly one selected witness is present for each covered source record, and none is out of range or duplicated.
- Chosen-witness counts by T28/T19/T84/T105 are **101959 / 39756 / 26193 / 9930**. These are counts of the frozen chosen witnesses, not claims that the sufficient type subsets are disjoint.
- Independently reconstructed all per-record sets of hits among the 232 listed geometric predicates and compared them with **541463** supplied record/orbit hit witnesses. Every witness has a legal actual source/cut and matching marked masks; no orbit occurs twice for one source record. Every reconstructed record/orbit set agrees exactly. All 232 per-orbit cardinalities also agree with both the coverage JSON and source-profile actual-record counts.
- For every individual source record, a hit among the 232 listed geometries exists **iff** a hit among the selected 111 accepted geometries exists. Thus the claimed equal union was checked as actual record sets, not inferred from equal total counts. This does not validate rank certificates of the 121 unselected geometries; they are unnecessary to the accepted sufficient conclusion.
- For every record, selected witness membership equals the independently exhausted selected-111 predicate. All selected witnesses and all supplementary hit witnesses are consumed, so stray target/index records cannot survive.
- The checker rebuilds each residual by copying precisely the original eleven bytes of each source index with no selected hit, in original order. All **three complete residual byte sequences** equal the frozen outputs. Per-file input/covered/remaining counts match the application table and coverage JSON exactly.

The complete deterministic result is `TWELVE_NEW_TYPES_APPLICATION_REVIEW_check.json`; reviewer lookup/precheck/source files are preserved and hash-bound. The exact current raw residual SHA256 values are:

| Target | Remaining | Raw residual SHA256 |
|---|---:|---|
| 1 | 8032 | `c080c2cc696f25954578f08ea546d2b512a5331c993530c3603927ecab57e2ac` |
| 7 | 11661 | `c60c5e13697f0de6713384b105cc1af953d7823e44d8c983cba837150063ae7b` |
| 31 | 17712 | `fac1baa6e7b54631a61bafec663a6ccf3726099ea2182386e72aac308569a2fe` |

## Mathematical transfer and hypothesis ledger

**MC1 — exact four type rows.** In even consumption use s=a+1-b A even holes. Final B minority is Z intersect B, and majority is W intersect B plus the s mirrors. In odd consumption use s=b-a-1 A odd holes; minority is W intersect B, majority is Z intersect B plus mirrors. In either case the actual omitted set is exactly the mirrors. The root is removed from the B hole set if it lies in B, and is not counted in Z. Substituting the eight source rows gives:

| Type | Even (a,b); s | Odd (a,b); s | Actual final holes; omissions | Completed A holes per parity |
|---|---|---|---|---:|
| T28 | (3,1); 3 | (0,4); 3 | 2:8; 3 majority | 1 |
| T19 | (4,1); 4 | (0,5); 4 | 1:9; 4 majority | 1 |
| T84 | (5,2); 4 | (1,6); 4 | 0:8; 4 majority | 2 |
| T105 | (5,1); 5 | (0,6); 5 | 0:10; 5 majority | 1 |

These counts agree with the accepted local terminal/rank/forest/cycle interfaces: N22/R1024/E18/cycle29, N22/R1024/E17/cycle28, N24/R2048/E16/cycle28, and N22/R1024/E16/cycle27, respectively. They are never inferred just from an unmarked type name.

**MC2 — source and root legality.** Even sources are distinct originally free even Z vertices in A, so cannot equal the covered odd target or root. Odd sources are originally free W vertices in A and explicitly exclude the possible root mirror. A covered target is outside W, hence cannot be consumed. At most one A W vertex is the root mirror, and b-s=a+1>=1, so enough legal sources exist in every relevant odd row. Source masks are independently checked against the exact actual pool. No free-target branch is asserted by this application.

**MC3 — original B mirror coverage.** Each selected mirror is distinct. Its A source was free, so the mirror cannot be an original crossing port. Nonroot independence excludes any other original opposite-parity hole there; the source exclusion forbids root 0. The checker explicitly rejects a source whose mirror is any original hole/root. Therefore the mirror is internally B-covered for every realizing original short matching. Its original mate is distinct and has the opposite parity, outside source mirrors, ports and the free root.

**MC4 — endpoint theorem application.** All eight rows lie within the accepted original uniform-transfer ranges: b=1 or2 in even consumption and a=0 or1 in odd consumption. Completed A matching has exactly b:b or (a+1):(a+1) holes. Thus only balanced two-hole or four-hole arbitrary-matching endpoint inputs are used. The local root is free and even; v remains the prescribed odd covered target, including when it is a crossing port. Artificial completion edges can be long or same-parity, which the import allows. With zero original crossings the declared five-direction endpoint theorem applies.

**MC5 — forest and target-port boundaries.** For positive crossings, if root is in A it is the A path root; if root is in B, take the standard source root in even consumption or an even port root in odd consumption. The odd-port surplus is s+1, ensuring the latter exists and lies outside the completion pairing. Port parity makes the completion set even. All s>=3, so D is nonempty in the tagged A-cycle case. Removing D and attaching distinct B leaves yields a forest after tagging. A covered target port can lose its sole A path edge, but its original crossing and tag restore degree two; no assumption that deleted A components lack isolated vertices is used.

**MC6 — actual compressed matching.** Compression produces a matching of transferred A paths with B endpoints. Its only conflicts with original internal M_B occur at the same-parity mirrors Y. Their opposite-parity original mates are distinct pendant endpoints outside the transferred endpoints; conflict components cannot close a cycle, including a transferred Y-to-Y path. Simultaneous suppression yields the actual arbitrary matching L on exactly B minus its declared H_*, with Y omitted. It need not be short or bipartite. The local theorem applies to L, not merely to the original M_B.

**MC7 — actual accepted marked theorem.** Minority, majority and Y are projected and transformed simultaneously, so each selected lookup identifies one of the exact 111 accepted marked pairs and its common cube image. The local result quantifies over **every** perfect matching of the corresponding complete graph, including every L that any realizing original M can produce. It gives one simple cycle on B minus Y and only short new edges outside L. Empty minority is handled by an omission anchor solely for lookup; no root exclusion other than legal source mirrors is needed for these unconditional local inputs.

**MC8 — expansion and every-M quantifier.** Expand the recorded disjoint suppressed conflict paths and A paths in that local cycle, then delete the tagged root–target edge. The omitted Y vertices and every A vertex are restored once. All original matching edges survive, completion placeholders disappear, and every new surviving edge is short. The endpoints are the fixed original root 0 and target v. The cut/source witness depends only on geometry; completion/path choices may depend on the actual original matching. Since MC2–MC7 hold for every realizing short matching and the local theorem is universal in L, the sufficient conclusion has the claimed every-M quantifier.

**MC9 — exact sufficient subset and complement.** Record identity is (target,original source index); different successful orbits for the same record do not create extra source coverage. Independent full selected-predicate enumeration agrees exactly with one valid selected witness per accepted record. The complementary original records are copied unchanged in order and compared as complete byte strings. This proves the exact partition 177838+37405=215243 and the per-target complements without overlap subtraction or matching-realizability filtering.

## Adversarial checks and remaining scope

The audit explicitly addresses root mirrors selected as odd sources, a covered target mistaken for a hole, deleting the wrong coordinate, unmarked-only lookup, independently moved omission sets, empty-minority normalization, incorrect same-parity assumptions on L, target-port isolation, favorable original-matching choices and duplicate source/orbit counting. They are excluded by the stated predicates, direct witness replay and transfer argument. Failed lookup remains a route failure, not a nonexistence certificate.

The independent equal-union comparison concerns all listed 232 **geometric predicates**, while mathematical local acceptance remains restricted to the 111 already certified inputs. Greedy minimum-cardinality/optimality and the completeness of the 380-row geometry domain are not accepted or required. Nonfull ranks and unselected certificate files are not negative or additional positive mathematical conclusions. No asymptotic, probabilistic or limit/interchange claim occurs. Full twelve-hole Q6, 14–18-hole layers and full P6 remain OPEN; no state promotion is part of this audit.
