# R4 two-bridge proof review

**Verdict: PASS_WITH_SCOPE_LIMITS for the revised restricted lemma.**
`review_independence: same-family`; `acceptance_status: provisional`.
Review date: 2026-11-01. Fresh reviewer requested as GPT-6.1-sol / high.
This is a semantic review with fresh deterministic reruns, not cross-family
acceptance. The imported Q4 N14 theorem is assumed as previously audited.

The accepted input is `R4_DOUBLE_BRIDGE_BLOCKING.md` **after** its explicit
addition that r,s,t are nonzero. The exact SHA-256 and all other audited inputs
are recorded in `R4_DOUBLE_BRIDGE_REVIEW.json` under `audited_input_hashes`.
No production source or main proof ledger was edited by this reviewer.

## Accepted and excluded scope

For any original complete-graph matching F with the stated face restrictions,
arbitrary internal edges and crossing bijection C, c even and 4<=c<=12,
and any selected bridge pair a,b among the nonzero even retained A holes:

* Identify the unique applicable mode from the statuses of a_B,b_B in F_B.
* Let Bad(F_B) be **all** negative-table boundary outputs in that mode.
* If Bad(F_B) is empty, or there exists a boundary perfect pairing D0 such
  that every Q in Bad(F_B) has disconnected edge-labelled union with D0,
  then a 30-cycle retaining every original edge, omitting precisely x_A,y_B,
  and using only short new edges exists.

Here D0 may depend on F_B and the selected pair; it does not have to work
simultaneously for different F_B. The boundary existence implication is uniform
over **every** F_A and C. N14 is applied after D0 is chosen. Its outcome is
existential, and every such outcome has the required connected union. No
selection of a favorable N14 outcome is assumed.

This certifies every c=10,12 input for the three displayed geometries. It also
certifies every c=4,6,8 input outside the listed joint B residual supersets.
It does **not** certify complete cores 1,4,24, the residual supersets themselves,
c=0 or c=2, bridges at free B0, or an eight-hole theorem. The last sentence
claiming that some residuals have no two-bridge forest solution is a separate
diagnostic assertion, not established by these blocker tables and not included
in this verdict. A null blocker is not treated as an impossibility certificate.

## Gap found and repaired in the reviewed revision

**R4-01 — CASE_INCOMPLETE / HIDDEN_ASSUMPTION.** The original general statement
allowed 0 among r,s,t and said to choose any pair. For example A holes
{0,3,5,9} with x=3 permit a=0,b=5. Then a_B is the free B hole, neither a
port nor an internally matched vertex. The five modes do not apply, and
{0,y,a,b} is not a four-element hole set. This is a verified missing case,
not a counterexample to existence of the desired cycle.

The writer added the explicit hypothesis r,s,t!=0 (current lines 16-19).
All three applications satisfy it: bridge triples (3,5,9), (3,5,15),
(6,10,15). This repairs the obligation for the restricted lemma and propagates
the assumption to its statement. It does not prove the originally unrestricted
lemma. A weaker alternative would restrict only the selected pair to avoid 0;
that extension is not needed or claimed here. No open fatal or critical issue
remains within the accepted restricted scope.

## Boundary proof obligations

Write d_a=C^{-1}(a), d_b=C^{-1}(b) when the corresponding B vertex is a port.
Every initial D is a perfect matching on X_A union {a,b}, disjoint from F_A.
Thus F_A union D leaves exactly x and the fourth A hole unmatched, both even.
N14 applies with omission x, yielding a simple 15-cycle containing D.
Removing a nonempty matching from that cycle gives disjoint spanning paths.
Contracting them proves connectedness of the endpoint pairing with D.

| Mode | Prescribed edges in D | Remaining boundary in B | Number of deleted edges |
|---|---|---|---|
| Distinct internal mates | none | X_B union {a,b} | (c+2)/2 |
| Internally paired bridges | ab | X_B | c/2 |
| Only a_B a port | a d_a | (X_B-{a}) union {b} | c/2 |
| Only b_B a port | b d_b | (X_B-{b}) union {a} | c/2 |
| Both ports | a d_a, b d_b | X_B-{a,b} | (c-2)/2 |

All prescribed endpoints are distinct because a,b are A holes, the d's are
distinct A ports, and C is bijective. Any perfect D0 on the displayed boundary
pulls back through C and the unchanged bridge labels, and adjoining the
prescribed edges gives a legal D. Therefore there is no hidden restriction on
the blocker search domain. The last column is strictly positive for c>=4.

In the last four modes replace prescribed edges in the N14 cycle before
deleting the remaining D'. The replacement is a simple circle with two extra
B vertices; deleting nonempty D' prevents a closed inaccessible component.
In the distinct-mates mode, the two matched B mates are distinct and outside
X_B union {a,b}; attaching their incident F_B edges to the path endpoints
cannot create a cycle. The analogous single mate is outside the boundary
in the one-port modes. Untouched F_B edges remain separate matching edges.

Suppressing the internal paths leaves a genuine six-edge matching L on
B-{0,y,a,b}. All 17 suppressed vertices are exactly (A-x) union {a_B,b_B}.
The positive table cycle has the complementary 13 B vertices. Expanding each
of its quotient edges therefore yields one simple 30-cycle; disjoint interiors
prevent vertex repetitions. Paired bridge edge ab is restored in its replaced
path. Original crossings occur either in a prescribed replacement or an
attached remaining crossing. Every artificial D edge is deleted or replaced;
every quotient edge is expanded. All other added edges come from N14, the
positive table, or the two coordinate bridges, hence are short.

The connectedness criterion uses edge-labelled unions, so a doubled D/Q edge
on a two-vertex boundary is allowed. Ordinary BFS forgets multiplicities but
preserves connectivity, which is all the blocker verifier needs. In particular,
the both-port c=4 boundary of size two is not silently discarded.

## Inverse completeness and table audit

An output L splits into untouched F_B edges J and compressed path edges.
Inserting one missing bridge vertex into an oriented Q edge creates its
internal F_B mate and the remaining boundary edge. Inserting both vertices
sequentially accounts for both distinct modified edges and a single modified
edge whose expanded boundary pairs a with b. Insertion that creates F_B=ab
is excluded from this mode and handled separately as the paired mode.
Every inverse has the correct support, mode and number (14-c)/2 of F_B edges;
conversely suppression returns L. This checks all five displayed inverse
formulas, including all oriented assignments, without assuming shortness or
bipartiteness of matching edges.

The fresh run executed the independently written sequential-insertion checker
against all four saved families (3,5,1), (3,15,1), (6,10,1), (6,15,1).
Every saved output set equals the regenerated set, and each positive blocker
is checked against every bad output by undirected traversal. An additional
review harness asserts all 25 c/mode rows occur exactly once per family,
all actual output sets are nonempty, and all F_B statuses agree with their
claimed mode. These checks also avoid relying on accidental extra empty keys
from the checker's defaultdict lookup.

The fresh Q4 run checked all 124,740 records in 12 canonical tables, with
10,395 distinct matchings per table, and all 168 marked coordinate images.
For a positive entry it checks the full simple 13-cycle, F containment and
shortness of new edges. For a negative entry, free0 needs two distinct short
neighbors; the remaining vertices need one new edge each. The verifier
exhausts these neighbor choices and every complementary short matching
disjoint from F. Each resulting degree-two union is disconnected. Thus the
negative classification is an exhaustive degree-completion argument, not a
failed Hamiltonian search. Coordinate permutations fix free0 and transport
the two marked even omissions and the marked odd omission. The orbit sets
are disjoint and exhaust all 168 possibilities.

## Joint coverage

For each actual bridge pair the unresolved set is the union of its five mode
null lists. All coordinate permutations mapping that pair into any saved
canonical pair, with y=1 fixed, were checked to give the same transported
unresolved set. The three pairs within each core were then intersected, and
the result was compared matching by matching with the saved joint JSON.
All 15 rows are present; no core, c value or bridge pair was silently skipped.

| Core | c=4 | c=6 | c=8 | c=10 | c=12 |
|---|---:|---:|---:|---:|---:|
| 1 | 210 | 28 | 1 | 0 | 0 |
| 4 | 272 | 32 | 1 | 0 | 0 |
| 24 | 312 | 34 | 1 | 0 | 0 |

The c=8 singleton for cores 1 and 4 is {(6,7),(10,11),(12,13)}; for core 24
it is {(5,7),(9,11),(12,14)}. These are B supersets of unresolved full inputs;
no assertion is made that every F_A,C over these B inputs is obstructed.

Reproduce with `python research/six_directions/R4_DOUBLE_BRIDGE_REVIEW_check.py`.
It writes only review-prefixed outputs. `R4_DOUBLE_BRIDGE_REVIEW_check.json`
contains the deterministic PASS, exact residual counts and hash manifest;
the Q4 and four inverse rerun reports have the same review prefix.
Optional four-bridge 21+36 tables were not audited and are not dependencies.
