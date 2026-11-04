# T15 core5 complete closure: independent proof review

Verdict: **PASS**, with **same-family / provisional** semantic acceptance.
No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue remains in the
displayed marked core5 claim. This does not prove all T15 geometries, the
full eight-hole layer, or P6.

Actual reviewer configuration: gpt-6.1-sol, reasoning high,
fork_turns=none, agent /root/t15_core5_complete_audit.
The assignment explicitly requests this configuration; the proof-checker
skill's nominal Astra/ultra configuration was not used. No cross-family
review is claimed. Instruction source:
F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md.
Only this audit's new files were written; no main proof status was changed.

## Exact quantified statement

For every matching F covering exactly the 26 vertices outside
{0,1,2,7,13,14} of K(Q5), there exists a simple cycle with vertex set
Q5 minus {1,2}, containing every edge of F and having cube distance one
for every edge outside F. Original edges may have arbitrary length or
parity. Transporting the entire construction gives every cube-automorphic
image of this marked configuration, including opposite parity orientation.

The label maps v_A -> 2v+1 and v_B -> 2v are cube isomorphisms on the
faces, with equal labels joined by a short edge across the cut. The
holes become exactly A:{0,3,6} and B:{0,7,1}, with omissions 0_A and 1_B.
The retained original free vertices are globally {0,7,13,14}.
Each face has thirteen originally covered vertices, so the crossing count
is exactly one of 1,3,5,7,9,11,13.

The only retained foundation imports are the arbitrary-matching Q4 N14
theorem and the exact balanced Q4 tables already audited in
T15_BALANCED_BRIDGE_REVIEW.md/.json. I read that audit and the precise N14
statement in Q4_CORE_AND_A4_SPLIT.md. The six relevant source identities
(two N14 binaries, the N14 statement, two balanced binaries, and the
prior audit Markdown) match their hashes in the prior review. I did not
rerun the foundations and do not claim to have done so. The author's
small-crossing counts and new combined verification JSON were not accepted
as proof by themselves: the core5 finite obligations were recomputed.

## Dependency and proof-obligation ledger

There is no circular dependency. The graph is
N14 -> connected A boundary pairings; exact balanced tables -> positive
compressed B matchings and at most two negatives; elementary pairing
obstruction / new B kernels / positive residual certificates -> a valid
compressed cycle; disjoint path expansion -> the claimed thirty-cycle.
Neither full T15 nor an eight-hole/P6 assertion is an input.

| Obligation | Independent judgment and discharge |
|---|---|
| Step 1: artificial matching | X_A is disjoint from the original A holes and from internal F_A. Adding z and any perfect matching D yields seven required edges and exactly the two same-parity holes 0 and the other retained A hole (3 or 6). Thus N14 applies for every deliberately selected D. |
| Step 1: connectedness | D is nonempty and is contained in one simple N14 cycle. Removing it gives paths spanning A minus 0; their endpoints are exactly E=X_A union {z}. Compression of the original cycle proves D union R connected as a multigraph. Parallel copies of a shared edge must be retained in this argument. |
| Step 2: internal mirror | B mirror z is internally covered. Its mate k is not a port; the transported partner q of z is a port. Thus k differs from q, and suppressing z gives a genuine six-edge matching L with holes {0,7,1,z}. |
| Step 2: injectivity | In L the edge incident to k identifies q. Undo kq -> kz,zq, remove the other fixed internal edges, and pull ports back through C. Hence at most the two negative bridge6 matchings can produce bad boundary R. |
| Step 3: occupied mirror | d=C inverse(z) is an originally covered A port and differs from A hole z. Prescribe zd in D, replace it by z_A,z_B,d_A, then delete the nonempty D' when c>=3. This is deletion of matching edges from a simple expanded cycle, so no closed forest component survives. |
| Step 3: quotient | The endpoints are the other B ports; internal F_B has disjoint support. Compression gives a perfect matching Q on c-1 endpoints and D' union Q connected. The map Q -> F_B union C(Q) is injective for fixed F_B,C. |
| Step 4: exclusion lemma | On N>=6 vertices an edge of the first forbidden matching is disjoint from some edge of the second: at most two of its at least three edges meet the first edge. Extend these two disjoint edges to D. Each shared edge is an isolated doubled-edge component in D union R_i. All such unions are disconnected because N>2. The zero- and one-forbidden cases also hold. |
| Step 5: large crossings | Internal mirror c>=5 gives N=c+1>=6; occupied mirror c>=7 gives N=c-1>=6. Select D or D' after determining the forbidden pairings. The subsequent N14 output must be connected with the selected artificial matching, so cannot be forbidden. Existential quantifiers are in the correct order. |
| Step 6: occupied c5 | Four internal B edges remain. Every bad L is one of exactly two negatives and decomposes by selecting two of its six edges as Q. Fresh enumeration gives 30 distinct four-edge F_B inputs; each has exactly one bad quotient among its three possible Q. Arbitrary C merely relabels this four-element boundary. Set D'=Q_bad, whose union with itself has two components; N14 then realizes another Q. |
| Step 7: c3 | All 270270 B partial matchings and all six crossing permutations were independently checked. Every one of 1621620 inputs has a bridge permitting at least two of its three pairings. N14 supplies at least two realizable A pairings: a singleton R0 would contradict connectedness on choosing D=R0. Two subsets of size at least two in a three-element set intersect. Occupied-mirror loops are excluded by the B checker. |
| Step 8: c1 | Fresh enumeration covers 13 ports times 10395 internal B matchings. Exactly five inputs have neither bridge admissible, and their complete edges/ports equal the producer's input list. For each remaining input the unique two-endpoint pairing is realized by N14. |
| Step 9: residual coverage | For each of the thirteen possible A ports, pair its other twelve covered vertices exhaustively by taking the least remaining vertex and each possible partner. This is a disjoint exhaustive recursion, giving 10395 matchings per port. Times five B inputs gives exactly 675675 residual original matchings. |
| Step 9: positive cycles | A fresh checker reconstructs every expected required edge, checks exact byte equality with its record, verifies thirty distinct vertices with support exactly Q5 minus {1,2}, removes all thirteen required edges from the cycle-edge set, and checks cube distance one on the remaining seventeen edges. Exact record count and absence of trailing bytes pass. |
| Final expansion | Replace every required compressed matching edge in the balanced fourteen-cycle by its corresponding path. The interiors consist of A minus 0 and B mirror z and are pairwise disjoint, outside the other B vertices. The result is one simple cycle of 14+15+1=30 vertices. Every original edge is retained. |
| Automorphic orbit | A cube automorphism preserves incidence, distinct vertices, holes, omissions, and Hamming distance one. Apply it to both the arbitrary matching and the entire constructed cycle; the exact marked-orbit conclusion follows. |

## Independent computation

New source: T15_CORE5_FULL_independent_check.cpp.
It does not import any producer/checker code, generated negative-list text,
or the author's verification JSON. It reads the two audited raw balanced
table binaries. Bridge3 uses (3,1) directly; bridge6 is the coordinate image
of (3,4) under bit map [1,2,0,3].

The B checker chooses the port subset first and independently pairs the
complement. For every crossing permutation and endpoint pairing it builds
the compressed multigraph and uses a disjoint-set union structure to find
its connected components. The mirror must have degree two and all other
active vertices degree one. Each accepted component must have exactly two
non-mirror endpoints; components with no such endpoints, including an
occupied-mirror loop, are rejected. Compressing these components gives the
B matching looked up in the imported exact negative table. This
component-based algorithm differs from both the producer's explicit
suppression and the supplied verifier's path-tracing implementation.

The residual checker performs no search; it directly verifies the saved
positive witness for every independently reconstructed original input.
Its checks use explicit failure exits, so they remain active regardless
of whether C++ assertions are enabled.

| Independent obligation | Result |
|---|---:|
| c1 B partial inputs | 135135 |
| c1 zero B inputs | 5 |
| c1 positive residual cycles | 675675 |
| c1 certificate bytes, no trailing data | 37837800 |
| c3 B partial matchings | 270270 |
| c3 crossing bijection inputs | 1621620 |
| c3 inputs lacking a bridge with at least two good pairings | 0 |
| bridge6 negative L | 2 |
| c5 distinct nonempty inverse F_B cases | 30 |
| negative quotient count in each c5 inverse case | 1 |

The complete freshly computed B histograms match both author histograms as
a secondary consistency check. In particular c1 spectrum counts are
0:5, 1:10414, 2:10426, 3:114290. No author histogram was used to accept
or reject an individual B input.

The supplemental Python checker independently reconstructs all thirty c5
inverse rows and checks consistency of every raw-table coordinate image
reaching (6,1). It finds exactly two such images, both from (3,4), with
coordinate permutations [1,2,0,3] and [2,1,0,3]. The complete negative L
lists and inverse rows are saved in
T15_CORE5_FULL_independent_supplement.json.

The positive residual binary has SHA-256
929204e08c9337ff76f778b6edd3586e42ecdcba2cf5734e56d03c8b3869b1b8.
Input hashes, actual configuration, scope, and all independent result
counts are in T15_CORE5_FULL_REVIEW.json.

Reproduction from this directory:

~~~powershell
g++ -O3 -std=c++17 T15_CORE5_FULL_independent_check.cpp -o T15_CORE5_FULL_independent_check.exe
./T15_CORE5_FULL_independent_check.exe | Out-File -Encoding utf8 T15_CORE5_FULL_independent_check.json
python T15_CORE5_FULL_independent_supplement.py
~~~

## Original long edges and boundary cases

An original F_A edge is retained in the N14 cycle and never deleted with
D, since F_A and D have disjoint vertex supports. Original crossings are
attached exactly as prescribed by the arbitrary bijection C. In the
occupied branch the crossing d_A z_B is explicitly restored when replacing
artificial zd; it is not replaced by a short-edge requirement. In the
internal branch, the original possibly long kz edge is restored upon
expanding the suppressed kq edge. Every other original F_B edge is
required in the balanced matching and remains in its cycle. Artificial
D edges and compressed L edges may be long but are removed or expanded;
only genuine added cube edges remain in the final graph.

The new bridge z_A z_B cannot equal an original crossing because z_A is
an original hole. Other new edges come from N14 and the positive balanced
table cycle and are short by the imported guarantees. The certificate
branch checks the final statement directly, including same-parity and
long original edges.

Counterexample attempts targeted the exceptional boundaries where the
generic obstruction fails: on N=2 the union of a pairing with itself is
connected, so c1 is handled separately; on N=4 two bad matchings might
defeat the shared-edge construction, so occupied c5 uses the exact
one-bad-quotient result. At c13 the internal matchings are empty but the
occupied construction and N14 hypotheses still hold. At occupied c3,
a boundary pairing joining z to its crossing preimage forms a closed
component and is correctly rejected. All other possible loops or
degenerate compressed components are rejected by the same degree and
component test. None yields an omitted case or a counterexample.

There are no analytic limits, big-O terms, probabilistic mode changes, or
measure-theoretic interchange obligations in this finite graph proof.
The odd crossing counts partition the original matching domain exactly.
All original matching-edge, omission, and arbitrary-crossing quantifiers
match the final statement.

