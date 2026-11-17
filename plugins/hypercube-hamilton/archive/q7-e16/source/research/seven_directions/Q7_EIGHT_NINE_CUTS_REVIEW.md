# Q7 eight-hole nine-cut theorem: independent audit

Verdict: **PASS**, `sound-modulo-imports`, `review_independence: same-family`,
`acceptance_status: provisional`. Reviewer configuration: user-requested
`gpt-6.1-sol`, `high`; served backend identity is not independently attested.
Reviewer agent: `/root/q7_eight_nine_cuts_audit`. Date: 2026-11-02.

The reviewed theorem is exactly `Q7_EIGHT_NINE_CUTS.md`: every short eight-hole
matching in Q7, every free root, and every opposite-parity target, free or
covered, subject to at least one of the three preprocessing conditions or one
of the nine good cut rows. There are no open in-scope issues. This does **not**
close either remaining eight-hole residual domain or P7.

The ARIS proof-checker skill was read at
`F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`.
The caller's explicit scope/model/output restrictions govern this independent
review: no source fixes, no RUN_STATE changes, no frozen six_directions writes,
and no additional reviewer fan-out. Hashes are recorded in the JSON sidecar.

## Inputs and dependency boundary

Imported universal statements were checked against their source statements:
Q7 six-hole paths (free or covered opposite-parity targets), Z7 (any short
matching with an empty direction), Q6 A4/B2/C2, Q6 A6 (both parity orientations,
any designated majority hole), and the literature-derived N10/N14/perfect
matching circle results recorded in PROOF_PACKAGE. Local dimension is six,
which satisfies the literature lower bound five. Long prescribed matching
edges are allowed in every local complete-graph input; only newly added edges
must be short. The original Q7 matching remains short throughout uses of Z7
and the Q7 six-hole theorem.

`Q7_EIGHT_NINE_CUTS_REVIEW_check.py` independently verified the four imported
PASS verdicts and 56 declared source/dependency hashes. Large imported
certificate suites and literature proofs were not rerun/reproved here.
This is explicitly a proof modulo those accepted imports, not an upgraded
cross-family or formal acceptance of their internals.

The dependency order is

    literature, earlier Q5 inputs -> Q6 A4 -> Q6 A6
    literature, P6, earlier four-hole layer -> Z7 -> Q7 six-hole theorem
    Q6 A4/A6, N10/N14 -> local endpoint lemma -> nine-cut transfer
    Q7 six-hole theorem and Z7 -> preprocessing

There is no edge back from any imported statement to this eight-hole theorem.
In particular, C3 in Section 1 follows from A6 and C2, rather than being used
to establish the same A6 input. Historical status prose in dependency source
files does not enlarge or invalidate their precise statements and current
hash-bound PASS artifacts. Old Q6 free-target geometric exhaustion is not an
input. No Q7 global cut census is needed for this sufficient-condition theorem.

## Local lemma and universal forest argument

For a local matching F with 2t holes and imbalance h, a free target insertion
removes epsilon(r)+epsilon(y)=h from the hole imbalance and leaves 2t-2
balanced holes. The three required circle inputs are therefore exactly
perfect/C1/C2 for t=1/2/3. For a covered target y with partner k, replacing
yk by kr removes the old free root and adds free y, giving

    h' = h - epsilon(r) + epsilon(y) = 2 epsilon(y).

The new matching still has 2t holes and y is a majority hole. N14/A4/A6
therefore applies with the designated omission y. The auxiliary kr is
present on the resulting circle, can be deleted, and original ky can be
restored. Distinctness follows from r being free and y covered. This proves
the endpoint lemma for every allowed target state and h, including
same-parity endpoints where prescribed long edges carry the imbalance.
Closing a local path at a short-neighbor target cannot duplicate an edge:
a Hamilton path on 64 vertices cannot already contain its endpoint edge.

Deleting a matching D from a path leaves path components, with isolated
target v possible when v is a crossport. Attaching each distinct B port once
cannot join two components or create a cycle. D avoids the free path root
(u or p); if delta=1 its nonemptiness separates u and v into distinct
terminal components. If delta=0 there is one actual v-terminal component;
p receives its crossedge and ceases to be an A endpoint. A bridge source
x is internal to the A path, has exactly one D edge removed, and receives
exactly one bridge. Thus its mirror y is one exposed B endpoint, either
terminal or on exactly one nonterminal segment. All other exposed B vertices
are distinct crossports, disjoint from internal M_B coverage.

When y is nonterminal, k=M_B(y) is internally covered and d=R(y) is a
crossport. Hence k,d,y are distinct, k is not in R and d is not in M_B.
Replacing yk and yd by kd produces a genuine matching, with y a free
majority hole. Expanding kd restores k-y followed by the y-d segment,
using y exactly once. When y is terminal no such compression is made:
y remains covered in M_B and is used as the covered target of a local
Hamilton path. This explicitly handles the terminal-bridge conflict rather
than silently treating y as free.

These arguments are universal in c and in all possible A-path orders.
The independent finite checker supplements them with all disjoint deletion
patterns on abstract paths of sizes 3 through 14 (6564 labeled bridge-choice
cases, including 2616 cases where the covered A target was isolated before
its crossedge was attached). This finite check is not used as a proof of
universal path orders or as an enumeration of Q7 matchings.

## Obligation ledger

All entries below are CLOSED, with imported theorem applications understood
as CLOSED_MODULO_IMPORTS.

| ID | Obligation and discharge |
|---|---|
| O01 | Short eight-hole input has four even/four odd holes; translate root to 0, preserving cube geometry and both endpoint states. |
| O02 | Nonroot-hole adjacency adds a short edge, keeps u free, yields six holes; v may become covered, which the six-hole theorem allows. |
| O03 | Free adjacent target: add uv, retain six holes with a remaining free root, obtain and close a six-hole path, delete uv to get endpoints u,v. |
| O04 | Empty direction invokes Z7 on the original short matching, for either target state/root side. |
| O05 | Local endpoint lemma: free insertion balance and total counts verified above. |
| O06 | Covered-target replacement balance, matching legality, majority omission and restoration verified above. |
| O07 | Circle corollaries use free roots and short-neighbor targets; closures are new short edges. |
| O08 | Every artificial D uses free local ports/selected original hole; it avoids u,p and any free v. Covered crossport v is permitted. |
| O09 | Port difference is E(X_A)-O(X_A)=b-a-delta, using shortness of original internal edges. |
| O10 | Zero bridge, delta=1: c positive even, hence D nonempty; A holes (a+1,a+1), B closure holes (3-a,3-a). |
| O11 | Zero bridge, delta=0: port difference 1 gives even p; c=1 and empty D are legal; B closure consumes free u and terminal r. |
| O12 | Zero-bridge a=0,1,2 keeps all circle/path inputs between two and six holes; rs or ur joins distinct free vertices. |
| O13 | Even source x in Z∩A exists for a>=1; its odd mirror y cannot be u or W and cannot be a crossport because x is free. Thus y is internally covered. |
| O14 | Even-source delta=1: c positive odd and D nonempty, including c=1. A holes (a,a). |
| O15 | Even-source delta=0: equal port classes plus c>0 gives c>=2 and an even p; D still nonempty at c=2. |
| O16 | Even-source nonterminal y: conflict plus rs/ur gives (3-a,5-a), y majority; A6/A4/N14 applies at a=1/2/3. |
| O17 | Even-source terminal delta=1: holes (3-a,4-a)+q, total 8-2a; imbalance 0/-2 matches epsilon(q)+epsilon(y). q is free, y covered. |
| O18 | Even-source terminal delta=0: holes (4-a,4-a), root u free and y odd covered; at most six holes. |
| O19 | Odd source: exclude free v and mirror u. Covered target leaves >=2 candidates; free target with a>=1 leaves >=2. At most one mirrors u. |
| O20 | Odd-source mirror y is even, not Z or u and not a crossport; internally covered. |
| O21 | Odd-source delta=1: c positive odd, D nonempty even at c=1. A holes (a+1,a+1). |
| O22 | Odd-source delta=0: port difference 2, c>=2, even p exists, D nonempty even at c=2. |
| O23 | Odd-source nonterminal y: holes (4-a,2-a), y majority; A6/A4/N14 applies at a=0/1/2. |
| O24 | Odd-source terminal delta=1: holes (3-a,2-a)+q, total 6-2a; imbalance 2/0 equals epsilon(q)+epsilon(y). |
| O25 | Odd-source terminal delta=0: holes (4-a,2-a), imbalance 2 matches even u and even covered y; six/four/two holes. |
| O26 | Terminal positions exhaust y's possibilities because y is an exposed forest endpoint, never an interior forest vertex. |
| O27 | Exceptional free target requires a=0,b=2,delta=0 with the sole other odd candidate x mirroring u; no other bridge-choice failure exists. |
| O28 | Exception: all-port pairing leaves exactly odd holes x,v in A; N10 permits same-parity free endpoints. Port difference 2 ensures c>=2 and D nonempty. |
| O29 | Exception: deleting D separates x,v before attaching ux; r,s are distinct crossports. L_B=M_B+R+rs is a matching with four even/two odd holes, including free u. |
| O30 | Exception: A6 omits u, deleting rs gives a B-u path, terminal u-r segment restores u exactly once. |
| O31 | All auxiliary endpoint edges are deleted, all R edges expanded, and kd expands through original ky plus transfer; no artificial long edge survives. |
| O32 | Connectedness comes from one local B path joined to the disjoint terminal forest and expansion of its edges; no hidden second circle survives. |
| O33 | Nine good rows and eleven bad rows are disjoint and cover the 4×5 possible (a,b) values. |
| O34 | Residual statement is a logical complement only; neither free nor covered residual is asserted empty/solved. |
| O35 | DAG has no dependence on the eight-hole target; no Q6 bad=0 geometric conclusion is imported. |

The independent arithmetic checker covers the nine rows for both delta
values and every positive c compatible with the face's 32+32 parity capacity.
It also checks all 12 applicable (t,h,epsilon(r),epsilon(y)) endpoint parity
tuples. Its output is `Q7_EIGHT_NINE_CUTS_REVIEW_check.json`.

## Adversarial checks and boundary decisions

The attempted failure modes were: c=1 with root same/opposite side;
c=2 with only one D edge; empty D in the legal zero-bridge opposite-root
branch; covered v itself a crossport and isolated by deleting D; bridge
at either terminal rather than in R; terminal endpoint parity both choices;
covered y with free local root; a=0 odd bridge-choice failure; and a=3
two-hole N14 boundary. None gives a counterexample. The universal arguments
and ledger above discharge them; the lack of a numeric counterexample is
not the basis for acceptance. No exhaustive eight-hole geometry or matching
search was executed. The bad-row complement has 11 entries and the text
explicitly retains its realizable free residual, so no scope overclaim occurs.

## Separately requested endpoint-swap preprocessing

This is **valid modulo the full Q7 six-hole theorem**, but is not part of
the hash-bound source theorem in this review. Suppose both u and v are free,
and u is short-adjacent to an odd hole w different from v. The enlarged
matching M+uw is short with six holes. Its root v is still free; its target
u is now covered and has opposite parity to v. The accepted six-hole theorem
gives a Hamilton v-u path containing M+uw. Reverse its order to obtain the
required u-v path containing M. The new edge uw is short and may remain in
the path. No deletion, circle or extra induction assumption is needed.

This strengthens the preprocessing for free targets and would also resolve
the exceptional root-bridge configuration of Section 6 directly. Section 6
remains a correct independent construction in the current source. Adding
the preprocessing later requires a new source hash and review-sidecar update;
this supplementary comment does not silently alter the theorem or its
residual domain definition.

No main proof, RUN_STATE, or frozen six_directions file was modified by this
review. All open in-scope issue counts are zero. Full eight-hole and P7
obligations remain outside the accepted scope.
