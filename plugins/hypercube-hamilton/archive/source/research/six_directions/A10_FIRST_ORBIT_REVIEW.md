# A10 first marked orbit: independent proof review

Date: 2026-11-01. Reviewer: `/root/a10_first_orbit_audit`.
User-requested setting: GPT-6.1-sol, high; ARIS proof-checker.
`review_independence: same-family`; `acceptance_status: provisional`.

## Verdict and exact scope

**PASS, relative to the declared certified Q4 inputs.** No missing mathematical
assumption or open proof obligation was found in the stated first-orbit theorem.
For every matching of the complete graph on Q5 with holes exactly
`{0,3,5,6,8,15,16,23,25,26}`, a simple cycle on exactly Q5 minus 0 contains
the matching and uses only short additional edges. Required edges may be long
or join vertices of the same parity. Coordinate permutations prove exactly
the stated orbit of 30 marked normalized geometries.

This review proves neither full A10 nor Q6 P6. No full Q5 A8 theorem is an
input. Its contemporaneous audit is unnecessary here. No production source,
producer output, or main progress state was changed. Provisional denotes the
same-family assurance level, not an unclosed branch of this scoped argument.

## Assumptions and dependency ledger

The acyclic dependency graph is:
Q4 GQ4-avoid + Q4 T15 exact classification -> the two-bridge sufficient rule
-> failure constraints for six choices -> two closed eight-sets -> impossible
odd covered intersection -> first marked orbit, then coordinate transport.

The Q4 statements were read directly in `Q4_GENERAL_AUGMENTATION.md` and
`Q4_T15_CLASSIFICATION.md`. Their audited bridge use and prior certification
were inspected in `A8_BRIDGE_INPUTS_REVIEW.md/.json` and
`Q4_T15_CLASSIFICATION_REVIEW.md/.json`. This is a relative review of these
imports, not a rerun of all transitive Q4 certificates. No A8 global closure,
Q5 A10 theorem, or P6 conclusion occurs in the dependency graph.

The complete quantified claim is: for every matching F with precisely H as
its uncovered set, there exists a simple 31-cycle K with vertex set V-H0,
where H0={0}, F subset E(K), and every edge of E(K)-F has Hamming distance
one. For each coordinate permutation the same quantifiers hold with the
transported H and unchanged forbidden vertex 0. There is no restriction on
the crossing count, on the parity of required-edge endpoints, or on whether
a selected bridge mirror is a crossing port.

Symbols are consistent: F_A,F_B,C partition F; X_A,X_B are endpoint sets of
C; T is a set of A vertices; P,J,D,Q are matchings on T with D perfect;
L is the compressed matching on B. Here Q is the endpoint matching called S
in earlier bridge material. A terminal means the B endpoint of a component
meeting T, with its unique T root; unrelated F_B endpoints are not such
terminals. All contracted cycle statements use labelled multigraph edges.

| Obligation | Discharge |
|---|---|
| Exact input, arbitrary required edges | Claim and hypothesis use only matching and exact H; no later step tests required-edge length |
| Bridge legality | A endpoints t,s are distinct original holes; tw,sz are new short mirror edges, not presumed original C edges |
| Crossing count and T | 2|F_A|+c=10, so c even, 0<=c<=10; T has c+2 distinct vertices and 1<=d<=6 |
| G is a path forest | Every T vertex has degree one; only selected mirrors can have degree two in B, and each leads to an A leaf |
| Unique roots and endpoint pairing | Each T--T component contributes a disjoint P edge; each other T component has one distinct B terminal/root |
| Root prescription is a matching | Roots of p,q, when both exist, are distinct and unused by P |
| Strict J subset D | With r=2d-2|P| even, an outside terminal gives r>=2 for e=0 and r>=4 for e=1, hence d>|P|+e |
| GQ4-avoid hypotheses | F_A+D has exactly three majority holes and one minority hole; 0 remains an uncovered majority vertex |
| Removing D leaves paths | D is a nonempty matching in the 15-cycle; endpoint set is exactly T, giving Q and a single alternating Q+D cycle |
| No premature cycle | Any proper subset J of labelled D breaks that alternating cycle; Q+J and Q+P are forests |
| Compression produces a matching | All A minus 0 and selected mirrors are path interiors; endpoints are precisely covered B nonmirrors |
| Compressed obstruction excluded | Single-edge F_B components excluded by pq notin F_B; two rooted terminals excluded by adding their root edge to J |
| T15 hypotheses | L holes are original singleton a and five opposite-parity holes; avoided mirrors are two neighbors and remaining neighbors p,q are not paired in L |
| Expansion | Disjoint interiors restored once; all F_A,F_B,C survive, D disappears, all other added edges are short |
| Six-choice quantifiers | At least four nonfixed choices; each candidate lies in at least two of them, including the two-disjoint-fixed-edge case |
| Closure and contradiction | Both covered eight-sets are invariant under the original mate involution; their five-point covered intersection must have even size, contradiction |
| Orbit transfer | All 120 coordinate permutations yield exactly 30 marked images, fixing 0 and preserving required edges, shortness, and simplicity |

There are no asymptotic constants, analytic interchanges, probability-mode
changes, or limit orders in this finite proof.

## Independent reconstruction of the decisive steps

At lines 94--108, let r be the number of rooted terminals. Their count is
even because r=|T|-2|P|. If p,q are both rooted terminals and there is
another terminal, r>=3 and hence r>=4. Otherwise the one outside terminal
already forces r>=2. Thus in both cases r>2e, where e records whether the
extra root edge was prescribed. Consequently J extends to D with at least
one D edge outside J. Equality |J|=d is never used as a successful case.

Deleting D from K produces paths, including any length-one paths. Their
endpoint matching Q and D make a single alternating multigraph cycle.
Restoring a proper subset of the D edges cannot form a cycle. This includes
d=1: coincident Q and D endpoint pairs are two labelled parallel edges;
retaining both would be a two-edge cycle. This convention also handles a
root prescription whose endpoints are already joined by a Q edge.

In the attached graph, a closed component would contract to a cycle of
Q+P, excluded by Q+J being a forest. Original B--B components not meeting
T are single original F_B edges: any longer path would need an internal
selected mirror, whose bridge leads to an A leaf. Thus p,q can become a
compressed pair only through their original edge, explicitly excluded, or
through their distinct rooted components. The second alternative would
join their roots in Q+P and form a cycle upon adding the prescribed root
edge in J. This excludes precisely the T15 obstruction, including long
compressed edges. Expansion preserves every original crossing edge even
when its A endpoint is unrelated to a mirror endpoint.

At lines 138--175 the global no-cycle hypothesis applies to *every* bridge
pair. For a nonfixed pair, a crossing port outside M is a rooted terminal
outside {p,q}; an internal partner outside M of a selected mirror is also
such a terminal. Therefore the port restriction follows from any one
nonfixed pair and the internal-partner restriction follows separately for
each candidate selected in a nonfixed pair. For a fixed candidate x, the
three complementary obstruction edges lie on the other three candidates,
so at most one belongs to F_B. At least two nonfixed choices select x.
This proves the needed coverage even if F_B contains two disjoint edges
inside M; it never assumes at most one fixed obstruction overall.

Every covered vertex of B outside M consequently has its mate in that
same set: it cannot cross, and cannot pair to M. Apply this to both cuts:

| Cut | Candidate neighbors M | Closed covered set |
|---|---|---|
| b=8, singleton 15 | 11,13,14,31 | 9,10,12,24,27,28,29,30 |
| b=16, singleton 23 | 19,21,22,31 | 17,18,20,24,27,28,29,30 |

Their intersection is {24,27,28,29,30}. It contains no hole. If both sets
are closed under the original matching, so is the intersection. The mate
map on it is a fixed-point-free involution, which partitions it into pairs.
Five vertices cannot admit that partition. This is an analytic contradiction
for every original F, not an inference from unsuccessful Hamilton search.

## Independent finite checks and adversarial pass

`A10_FIRST_ORBIT_REVIEW_check.py` is a separate implementation that does not
import or run the producer checker. It reads the frozen JSON only for
comparison and verifies that the producer's recorded checker hash matches
the actual source. It checks both cuts, hole parities, all six bridge/OB
complements, the eight-sets, their five-point covered intersection, and the
30-element marked orbit. A separate leave-unmatched-or-pair recursion
generates all ten partial matchings on four candidates; all satisfy the
nonfixed-choice coverage bound. No full Q5 matching is enumerated.

As a finite supplement to the analytic forest argument, it fixes canonical
D and generates every perfect Q on 2d labelled vertices for 1<=d<=6,
retaining all single alternating Q+D cycles. It checks every proper subset
J of D with a union-find forest test that detects parallel-edge cycles.

| d | Single alternating cycles | Proper-subset forest checks |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 6 |
| 3 | 8 | 56 |
| 4 | 48 | 720 |
| 5 | 384 | 11904 |
| 6 | 3840 | 241920 |

Adversarial cases checked in the proof: c=0; d=1; both mirrors internally
paired to each other; one or both mirrors crossing ports; arbitrary long
crossings; both obstruction endpoints rooted; one endpoint in a separate
F_B edge; Q/root-edge parallelism; |J|=d outside the sufficient hypothesis;
and zero, one, or two disjoint fixed obstruction edges. None gives a
counterexample to the stated sufficient rule or closure argument.

Execution: `D:\anaconda\python.exe research\six_directions\A10_FIRST_ORBIT_REVIEW_check.py`,
exit code 0, status PASS. The checker hashes all nine declared input files
before and after verification and confirms unchanged bytes. Its evidence is
`A10_FIRST_ORBIT_REVIEW_check.json`. The original producer was deliberately
not executed because it overwrites a frozen production JSON. The review
JSON pins the exact audited inputs and independent evidence.

## Final accounting

Open FATAL: 0. Open CRITICAL: 0. Open MAJOR: 0. Open MINOR: 0.
No proof edits required. The scoped first A10 orbit passes relative to its
Q4 imports. Full A10 and P6 remain OPEN; no main-state promotion is made.
