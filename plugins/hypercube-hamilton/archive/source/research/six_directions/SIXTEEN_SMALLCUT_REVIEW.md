# Independent review of the sixteen-hole small-cut package

Verdict: **PASS for precisely the local forced-edge/avoid-pair theorem and
the 118 specified actual geometries, modulo the explicitly listed imports.**
The complete sixteen-hole domain reduction is still conditional on complete
fourteen-hole extension. The exact unhandled source complement is 30 covered
target31 root-star records. Complete fourteen holes, complete sixteen holes,
and full P6 are not proved by this review.

Reviewer: `/root/sixteen_smallcut_audit`; user-selected GPT-6.1-sol, high.
This is an independent fresh-context review of another author's package,
with `review_independence: same-family`, `acceptance_status: provisional`.
It is not a Lean verification or a cross-family semantic acceptance.
The ARIS proof-checker instructions were read; the user's specific model,
output naming, review-only scope and artifact requirements take precedence
over the skill's default model and optional report-format workflow.

## Frozen inputs and independent execution

The manifest SHA256 is
`944a4a0f22448c318e2306e5d53e9e0747d29b81f959a575f809527cd952325a`.
The source review SHA256 is
`762ec4f5555a255e0182c0a6c9f0d235e4255a917dbf73651a74c5c121e07060`.
All 12 manifest input hashes, all 20 output hashes and every declared output
size were verified. The three source streams were also rebound directly to
the accepted source review's own hash entries.

`SIXTEEN_SMALLCUT_REVIEW_check.py` was written for this review from the
mathematical obligations. It imports no producer or earlier checker code.
The producer files were read for serialization conventions; their sanity
outputs were not accepted as verification. The checker was executed with
`D:/anaconda/python.exe`; exit code 0. Its own result is
`SIXTEEN_SMALLCUT_REVIEW_check.json`.

## Explicit imports and dependency ledger

1. The generic matching-connectivity theorem on all perfect matchings of
   a complete graph: over GF(2), rank H_t = 2^(t/2-1) for every even t>=2.
   The supplied primary-source note states this theorem for every even t;
   this package uses t=18, not the old deficient local K22 rank. Its cited
   Cygan--Kratsch--Nederlof result is an explicit mathematical import.
2. The already accepted balanced-hole Q5 endpoint theorem for arbitrary
   matching edges, a free root and either free or covered opposite target,
   with only short added edges. `Q5_A10_FULL_REVIEW.json` is hash-bound and
   its full consequence statement was checked against
   `Q5_A10_FULL_CLOSURE.md`. The actual use has exactly three free holes of
   each parity. Earlier large certificates are not rerun here.
3. The accepted source reduction and its three remaining actual streams,
   with the complete-fourteen-hole hypothesis retained. This review does
   not reconstruct or strengthen that earlier reduction.

The older s>=3 forced-cherry theorem is not an imported justification for
the new s=2 transfer. Its manifest hash is checked for provenance only.

Dependencies are acyclic: generic rank -> new finite local implication;
balanced Q5 endpoint theorem + local implication -> new s=2 transfer;
transfer + actual leaf/map witnesses -> 118 actual sufficient geometries.
The source's global domain reduction separately requires complete14.

## Local finite gate

The typed domains are Q5 vertices 0..31; hole sets HE={0,3,5},
HO={1,2,14,22,25,26,28}; omissions U={1,2}; K has 22 vertices;
e={30,31}; R={13,21}; reduced labels K minus e minus R have size 18.

For all 256 supplied 38-byte physical forests, the independent checker
verified each edge is short, endpoints are valid, all edges are distinct,
the graph is acyclic by DSU, and the degrees are 0 on U, 2 on H minus U,
and 1 on K. Every nonomitted vertex belongs to one path component with
exactly two K endpoints. Those endpoint matchings agree with the indicated
raw source rows; every selected physical block also agrees bytewise with
its recorded raw-source index. Neither e itself nor its endpoint pair is
already a forest component. Joining the endpoint graph with e and deleting
the two internal endpoints yields a perfect matching on 20 labels which
contains R. Deleting R gives exactly the supplied 18-label row.

Each of the 256 column blocks is a genuine perfect matching on exactly
the same 18 labels. All 65,536 connectivity entries were independently
recomputed by union-find on the union of two perfect matchings. Every bit
agrees with its little-bit-first matrix position. Integer-XOR elimination
of the recomputed rows gives rank **256**.

For clarity, the algebraic step is also checked semantically. These rows
are restrictions of full H18 rows. Their restricted rank 256 proves their
full-row independence. The imported upper bound rank(H18)<=256 therefore
makes them a basis of the whole full row space. For every arbitrary
matching G, its full column is nonzero: join its nine matched pairs in a
cyclic order using an opposite matching. Some selected row must evaluate
to 1 on that column. This is a universal statement over all G, not merely
over the 256 supplied columns.

Given any F on K with e in F and R not in F, remove e. The partners a,b of
13,21 are distinct vertices outside {13,21,30,31}. Replace 13a and 21b by
ab, producing an arbitrary perfect matching G on the 18 labels. In the
alternating multigraph, suppress the e path and then the a--13--21--b
path. This preserves connectedness in both directions. Hence the selected
connected row against G gives connected P+F. Expansion of the independently
checked physical forest gives a connected 2-regular graph on all 30
nonomitted vertices. A physical edge common to F and the forest would be
an isolated doubled-edge component, contradicting connectedness on 30
vertices. Thus it is an ordinary spanning cycle with all newly added
edges short. This closes the exact stated local implication.

## New s=2 transfer: hypothesis and boundary audit

Fix an arbitrary realizing original short matching M. A is the halfcube
containing covered target v; B contains free even root u=0. There are four
even and three odd holes in A. Internal M_A edges use one of each parity,
so |X_A even|-|X_A odd|=-1, giving positive odd crossing count c.
The two selected source holes S are even. Choose any r in S. The gap
domain X_A union (S minus r) has c+1 vertices, is disjoint from M_A,
and has even cardinality. Completing it by any perfect matching D leaves
three free holes of each parity. The imported Q5 theorem applies with r
free even and v opposite odd; if v is a crossing port then D covers it.
Long or same-parity artificial pairs are allowed by the imported theorem.

Delete D from that simple A Hamilton r--v path. Every nonroot source
gap and every original port gets its corresponding distinct B leaf;
r gets its source bridge; v gets the tagged edge to u. All A vertices
have degree two after attachment. The components are paths, because
deleting edges of a path creates no cycle, and attaching distinct new
leaves creates none. In particular the tag attaches a new B leaf and
does not close the A path. If v is a port and its sole A edge is in D,
the isolated A vertex gets its crossing leaf and distinct root leaf.
Thus T is an actual perfect endpoint pairing on X_B union Y union {u}.

Each y in Y is internally B-covered: its only potential original crossing
mate is its selected source hole; independence excludes another original
B hole at y; its odd parity excludes the even root. Its internal short
mate h_y has opposite parity and is outside all attachments and Y.
Combining T and M_B therefore has only degree-two concatenations at Y,
with distinct pendant mates h_y. Suppressing Y preserves paths, creates
no cycle (including a T pair joining both Y vertices), and gives an
arbitrary perfect matching F_B on exactly 22 vertices. Its marked holes
are (Z intersect B) union (W intersect B) union Y, with counts 3 and 7;
the two omitted vertices are exactly Y. The root is covered by its
tagged represented path. The surviving required original internal edge
e_B is unchanged, since it is disjoint from Y and from original ports.

For R_B={p,q}, both vertices lie outside marked holes and root, and share
Y's parity. If one is not a port, its internal opposite-parity mate is
outside Y, so its edge survives and is not pq. Suppression of Y moves
an endpoint only to an opposite-parity h_y; it cannot produce p or q.
Thus pq can appear in F_B only if both vertices are original ports and
T pairs them directly. In this case their A partners alpha,beta belong
to X_A and differ from r. Prescribing alpha-beta in D is legal; pair
the remaining even-sized gap domain arbitrarily. Every A completion
contains this D edge. Removing it from a simple path separates its
endpoints, and subsequent deletion and distinct-leaf attachment cannot
reconnect them. Consequently T does not pair p,q. If v equals one of
alpha,beta, its potentially isolated piece pairs that port with the
distinct root u, which was explicitly excluded from R_B. This boundary
does not need a second D deletion or an s>=3 hypothesis.

The prescribed D may depend on the actual M and its ports; this is the
correct quantifier order for proving existence of an extension for
every M. No favorable original M is chosen. The local theorem now applies
to the actual compressed F_B containing e_B and avoiding R_B. Its cycle
expands through all represented A paths and through both suppressed Y
vertices to a tagged spanning 64-cycle retaining M. Removing the tag
gives the required u--v path. Artificial D edges were already removed;
every remaining added physical edge is short.

These steps discharge every application hypothesis. The proof has no
asymptotic constants, probabilistic modes or analytic interchanges.

## Actual source records and exact complement

For each actual record, the checker verifies 7 even Z vertices, 8 odd W
vertices, independence, covered legal target and free root. Every one of
the 118 witnesses is checked against its exact source stream index and
15-byte record. The recorded cut contains v and has A counts (4,3); S is
two distinct original A holes. The complete single translation/permutation
map is independently reconstructed using the saved coordinate permutation.
The image of HE, HO, U, e and R simultaneously equals the actual minority,
majority, omission, required edge and forbidden pair. Thus no separately
chosen edge symmetry is being combined with a geometry map.

Every recorded leaf chain is checked directly in the residual six-cube
graph after all original holes and previous forced endpoints are removed.
At each step the named leaf has exactly one surviving cube neighbor.
Any perfect matching on that graph must use the edge; induction makes
the entire chain universally forced. The mapped e occurs in that chain,
is short, lies internally in B and is disjoint from Y. The mapped R has
Y parity, lies outside original holes, and excludes root and Y. These
checks establish the transfer prerequisites for every realizing M.

| Target | Source | Positive | Complement |
|---|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 7 | 18 | 18 | 0 |
| 31 | 130 | 100 | 30 |
| Total | 148 | 118 | 30 |

The six output streams equal the exact witness/nonwitness subsequences
of the frozen source, preserving source order, with no duplicate source
records. All 30 complements have W containing the six neighbors of root0.
Their set is exactly one orbit of its first record under coordinate
permutations fixing target31, independently enumerated, with size 30.
No assertion that other sufficient methods cannot handle these records
is made.

## Counterexample pass and final scope

The new critical prescribed-gap claim was also checked on all applicable
abstract simple A paths for (n,c)=(6,3),(8,3),(8,5), with target either a
prescribed port endpoint or a different endpoint. All residual gap
matchings containing the prescribed pair were considered. In 372 valid
path/gap configurations, deleting D and attaching all distinct leaves
gave paths with exactly two B leaves each and never paired the forbidden
ports. This supplements the symbolic path argument; it does not replace
it. Other degenerate cases checked in the proof are c=1 (two forbidden
ports cannot occur), a Y--Y transfer edge, v as a port, an isolated v
segment, a hypothetical doubled physical edge, and R containing root
(excluded and independently checked in all actual witnesses).

No fatal, critical, major or minor issue remains in the declared scope.
The new local theorem is sufficient only for matchings containing e and
avoiding R. The application proves the specified 118 geometries for all
realizing original short matchings. The source reduction's complete14
condition remains explicit. This package does not itself close full14,
full16, full18 or full P6. Producer artifacts and production/main ledgers
were not modified.
