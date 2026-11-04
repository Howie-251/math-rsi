# Complete Q5 A8: independent assembly review

2026-11-01. ARIS proof-checker; reviewer `/root/higher_hole_transfer_audit`,
user-specified `gpt-6.1-sol / high`. Assurance: **same-family / provisional**.

**PASS relative to the explicitly accepted inputs.** Full Q5 A8 is proved:
for every arbitrary matching F with3 holes of one parity and5 of the other,
and every specified majority hole v, a simple cycle on exactly Q5−v contains
F and has only short edges outside F. No restriction to short or bipartite
required matching edges is imposed.

The fifth-orbit gate was checked only after its independent full-domain and
all-positive-certificate review became final PASS. There is no pending orbit
input in this acceptance. Full Q6 P6, A10, all-hole Q5 endpoint statements
and complete remaining Q6 layers are not established by this assembly.
Production proofs and the main state were not modified.

## Exact submission, acceptance gate and import boundary

The theorem-bearing submission is `Q5_A8_FULL_CLOSURE.md`; its fixed SHA256
is in the JSON sidecar. Imported theorem/review/evidence hashes are recorded
separately. Historical pending-review wording in frozen source drafts is
resolved by the following final accepted reviews, not by editing their bytes.

| Input | Accepted exact scope |
|---|---|
| A6_CLOSURE_REVIEW | Every arbitrary K(Q5) matching with2+4 holes; every specified majority hole omitted |
| A8_PARTIAL_REVIEW | Short augmentation avoiding the marked hole; every remaining delta1/2/3 cut, all crossing cases |
| A8_DELTA4_FIRST_ORBIT_REVIEW | Full arbitrary-matching theorem for the first60-member residual orbit |
| A8_ORBITS2_3_REVIEW | Full arbitrary-matching theorems for residual orbits2 and3, of sizes20 and30 |
| A8_ORBIT4_FULL_REVIEW | Full fourth30-member orbit: analytic cut cover plus complete200475-input finite remainder and all positive cycles |
| A8_ORBIT5_FULL_REVIEW | Full fifth20-member orbit: analytic cut cover plus complete2732625-input finite remainder and all positive cycles |

All six reports are PASS. Their theorem sources match their recorded audited
hashes. In particular `A8_ORBIT5_FULL_REVIEW.json` is fixed at SHA256
`7465ec62e8cc1907992dd26a52af1259bb92a5444225ddb877085bace9b4febb`.
Its exact scope is arbitrary twelve-edge matchings on the complement of
{0,2,4,8,15,23,27,29}, omitted vertex0, including long and same-parity edges.
Its final report directly checks all2,732,625 matching inputs and positive
31-cycles, not a partial run or success count from a search.

The standard last-orbit certificate has150,294,375 bytes, exactly
2,732,625 records of55 bytes, and SHA256
`4faabf92ae61845e9a12b36a754998b03f14bf143e263999a6c6e731ac397f22`.
This assembly checker independently rehashes it and all files listed as
audited inputs in the final fourth/fifth-orbit reviews; every hash matches.
The fourth-orbit certificate has200,475 records with its own accepted hash.
The preceding independent reviewers' complete domain/cycle checks are
imported here. This review does not claim to rerun those matching checks
or any large earlier core certificate.

## Canonical theorem and dependency graph

For every F⊆E(K(Q5)) that is a matching with hole parity counts3:5, for
every v in its five-element majority-hole set, there exists a simple cycle C
such that V(C)=V(Q5)\{v} and F⊆E(C)⊆F∪E(Q5).

The dependency graph has two initial branches: A6 -> short augmentation;
and independently accepted Q4 inputs/bridge criteria/finite positive
certificates -> the partial A8 and five orbit theorems. Their exact
geometry partition -> full A8. The accepted K8 theorem is absent from this
graph. Its dependence on partial A8 is therefore harmless: K8 is not used
in either this assembly or any of its six theorem-bearing proof sources.
Those sources likewise do not invoke the present whole-A8 assembly.

## Proof-obligation ledger

| ID | Obligation and verification | Result |
|---|---|---|
| A01 | If a minority hole has a short edge to a majority hole other than v, add that edge. Its endpoints were free, v stays free, and hole counts become2:4. The arbitrary-matching A6 theorem supplies exactly the required31-cycle. The added requirement was short relative to original F. | PASS |
| A02 | In every other input no nonforbidden majority hole is adjacent to a minority hole. Translating by v fixes the prescribed omission at0 and makes majority holes numerically even regardless of their original parity. It preserves shortness and transports every arbitrary required edge bijectively. | PASS |
| A03 | The normalized domain is exactly four distinct nonzero even holes Z and three distinct odd holes W with no Z--W adjacency. Adjacency from0 to W is allowed and is never silently excluded. No short-matching realizability condition applies to this arbitrary-K(Q5) theorem. | PASS |
| A04 | A fresh complete odd-first enumeration yields exactly2700 geometries. Exactly2540 admit a target-containing face with majority-minus-minority count1,2,3. All160 others are retained for orbit coverage. | PASS |
| A05 | Each of the2540 good geometries has an actual cut/imbalance witness. The accepted partial theorem applies to every arbitrary matching on its complement and the marked omission0, including all original crossing counts and arbitrary long crossing partners. | PASS |
| A06 | The first representative is precisely Z={3,5,6,15}, W={8,25,26}; its60 images are covered by the accepted first-orbit delta-four theorem. The marked omission is0. | PASS |
| A07 | The second and third representatives have respectively Z={3,5,6,15} or{3,5,15,23}, both with W={25,26,28}. The accepted analytic theorems quantify over all original matchings and omit0; their20 and30 images match the partition exactly. | PASS |
| A08 | The fourth representative is Z={15,23,27,29}, W={1,2,4}. Its accepted analytic cover reaches every matching outside an exhaustive necessary finite family; all200475 members of that family have verified positive cycles. These are not asserted to be all possible arbitrary matchings on24 vertices. Their union with the analytic cases proves the universal representative theorem and its30 images. | PASS |
| A09 | The fifth representative is Z={15,23,27,29}, W={2,4,8}. The final accepted proof has the same analytic-complement/complete-finite-family structure, with2732625 inputs. Every finite input and every positive31-cycle passed independent checking. Its final PASS and certificate pins were checked before this verdict. | PASS |
| A10 | Each orbit is generated by coordinate permutations fixing0. For any original F in an orbit, invert the corresponding permutation, apply the representative theorem to that arbitrary transformed matching, then transform its cycle back. Every required edge, short new edge and specified omission is preserved. | PASS |
| A11 | The five complete marked orbit sets are pairwise disjoint, of sizes60,20,30,30,20. Their union is exactly the160 residual geometries, disjoint from all2540 partial cases. No family is recounted. | PASS |
| A12 | Augmentation and the no-augmentation normalized domain partition every original F,v. The independently verified partial/orbit cover exhausts that normalized domain. Translating back yields the exact original majority hole v, not just one favorably chosen hole. | PASS |
| A13 | No proof uses K8, unrestricted T15, A10, a higher Q6 layer or full A8 as a hidden hypothesis. Published/Q4 base results remain the explicit transitive import boundary. The dependency DAG is acyclic. | PASS |
| A14 | Every branch concludes one simple31-cycle, containing all original required edges, with every other edge short. Augmentation adds only a short required edge; automorphisms preserve shortness. No auxiliary long edge or compressed edge is left unexplained at assembly level. | PASS |
| A15 | Every necessary import gate is final PASS and source-bound. Prior orbit-only reports correctly left full A8 open within their own scope; the new exact union and gate check supplies the separate whole-A8 acceptance. No full P6 conclusion is inferred. | PASS |

All fifteen obligations are discharged, with no open FATAL, CRITICAL, MAJOR
or MINOR issue. No proof correction was needed. There are no asymptotic,
probabilistic, analytic-interchange or limit-order claims in the assembly.

## Independent complete geometry cover

New `Q5_A8_FULL_REVIEW_check.py` calls no producer or prior checker.
For each odd triple W it forms every nonzero even quadruple in the common
nonneighbor set. This enumerates exactly the normalized domain, with
neither omissions nor duplicate choices. Actual target-containing faces
are tested directly using their global majority/minority hole counts.

The checker separately generates all coordinate permutations of each fixed
representative, verifies orbit sizes and pairwise disjointness, and retains
an actual permutation witness for each residual geometry. Its complete
sets also agree with the previously accepted residual member lists, whose
source hash is checked against the partial review. Those old lists are a
comparison, not an enumeration oracle for the new domain.

| Disjoint branch | Geometries |
|---|---:|
| Partial delta1/2/3 |2540|
| First residual orbit |60|
| Second residual orbit |20|
| Third residual orbit |30|
| Fourth residual orbit |30|
| Fifth residual orbit |20|
| Total |2700|

`Q5_A8_FULL_REVIEW_witness.tsv` records every geometry and its actual
cut/imbalance or representative/orbit permutation. The independent geometry
result, final fixed-import checks, theorem/evidence hashes and witness hash
are in the new geometry/check JSON files and final review sidecar. No
original matching instance is reenumerated in this assembly audit.

## Counterexample pass and limits

The adversarial pass examined minority holes adjacent to0, a majority
forbidden vertex of either numerical parity, a required long or same-parity
edge, arbitrary original crossing partners, an incorrectly marked orbit,
double counting of the newly proved20+30 cases, a finite-family count
mistaken for the complete arbitrary matching domain, an incomplete final
certificate, and a K8 reverse dependency. The exact preprocessing domain,
source quantifiers, permutation witnesses, disjoint set equality,
analytic-complement coverage and final gate/hashes exclude these failures.
No counterexample or unresolved obligation was found in the exact A8 claim.

The final fifth-orbit review was PENDING during preparation; only geometry
evidence was produced then. This final report was emitted after its complete
positive-certificate PASS was frozen and independently source-bound.
Semantic assurance remains same-family/provisional relative to the declared
imports. Full A8 is accepted at that assurance level. A10, complete arbitrary-
hole balanced endpoint/cycle conclusions, complete remaining Q6 layers and
full P6 require separate proofs and audits.
