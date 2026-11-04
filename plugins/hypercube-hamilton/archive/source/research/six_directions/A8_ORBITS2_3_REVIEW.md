# A8 residual orbits 2 and 3: independent analytic proof audit

2026-11-01. ARIS proof-checker; reviewer `/root/higher_hole_transfer_audit`,
user-requested `gpt-6.1-sol / high`. Assurance: **same-family / provisional**.

**PASS relative to the declared accepted Q4 inputs.** The proof works for
every arbitrary complete-graph matching with either specified hole set,
omits the prescribed vertex0, preserves every required edge, and introduces
only short edges. Its coordinate images cover exactly20+30 marked geometries
in residual orbits2 and3. These do not overlap the first60-element orbit,
the fourth30-element orbit, or the last20-element orbit.

No complete A8 or P6 verdict follows from this package. The last orbit and
the eventual whole-proof assembly remain outside this review. No production
proof, producer checker/output or main state was changed.

## Submitted inputs and imports

The three fixed submitted inputs are:

| File | SHA256 |
|---|---|
| A8_ORBITS2_3_ANALYTIC_CLOSURE.md |c273b767a2ee10303c768b48d5d35a23da330cd4128af62b08547d51bc542764|
| A8_orbits2_3_geometry_check.py |766baf576b87865d49458c24f4e1f60731b415c13eb979c5c591a377bd7ee241|
| A8_orbits2_3_geometry_check.json |6be0beb1392c836934615d17735fa3ce97853e78845e9d661024ef5312f8fe9b|

The exact statements of GQ4-avoid, Q4 T15 classification and Q4 T63
classification were read. They all permit arbitrary required edges,
including long and same-parity edges. The latter two classify all their
marked inputs, rather than promising universal positive extension.

For T15 with singleton hole a and specified same-parity omissions Y,
when Y consists of two neighbors of a, the only possible obstruction is
the required edge on the remaining two neighbors. For T63, the obstruction
is a covered opposite-parity vertex a with only one neighbor b outside the
three omissions and with ab required. These are precisely the statements
needed after compression; merely excluding the edge in F_B would be
insufficient without the additional argument in Step1.

The accepted `A8_BRIDGE_INPUTS_REVIEW.md/.json` supplies the exact T63
classification and previously reviewed bridge-forest reasoning. The new
delta-five application is checked here directly, using the reproduced
terminal-excess proof. It is not inferred by substituting into the older
delta-minus-one three-bridge statement. Four relevant reports are PASS;
six relevant recorded source hashes match current sources. Prior large
positive matching certificates are accepted inputs, not rerun in this audit.

## Typed notation, quantifiers and dependency graph

F is any simple matching covering exactly Q5 minus H2 or H3; no shortness
or bipartiteness condition is imposed. Its mate map on the24 covered
vertices is a fixed-point-free involution. v=0 is the forbidden majority
hole. A,B are the zero/one faces of the selected bit b; C is the original
crossing matching, X_A,X_B its ports. T consists of A ports and selected
hole sources. Y is their covered B mirror set. P pairs T--T components
of G, J is P plus at most one terminal-root pair, D completes J on T,
and Q pairs the components obtained from the A cycle after deleting D.
These matchings must retain edge labels in a multigraph when endpoints
coincide.

Dependencies are accepted Q4 classifications/GQ4-avoid -> common sufficient
bridge construction -> nonfixed-choice restrictions -> closed sets ->
remaining-vertex contradiction. Independent bit geometry supplies only the
particular sets and obstruction identities. The final permutation step
transports the universal theorem. No A8 orbit closure, full A8, or Q6
theorem is used upstream.

## Micro-obligation ledger

| ID | Obligation and discharge | Result |
|---|---|---|
| O01 | Sources are distinct original A holes other than0; all mirrors Y are distinct originally covered B vertices. Hence bridges are new short edges, not original matching edges. In each application consuming the selected holes leaves A excess2 and keeps0 free. | PASS |
| O02 | In G=F_B union C union bridges every T vertex has degree1. Each Y has degree2 but has an adjacent T leaf. Every other covered B vertex has degree1. A cycle would have to traverse Y and its adjacent leaf, impossible. Thus G is a path forest, including internal Y--Y required edges and port mirrors. | PASS |
| O03 | Components are T--T paths (giving disjoint pairs P), T--B terminal paths with distinct roots outside P, or isolated original F_B edges. A longer B--B path cannot occur because reaching Y exposes its T leaf. Original B holes stay isolated. | PASS |
| O04 | Potential obstruction endpoints p,q are originally covered and outside Y. If both are rooted terminals, their two roots are distinct and outside P, so adding their pair creates a matching J. Otherwise J=P. The fixed edge pq is explicitly excluded in F_B. | PASS |
| O05 | Terminal roots number2d-2|P|. If a terminal outside{p,q} exists, this even number exceeds2e, where e=|J|-|P|. Thus d>|J| and J is a proper subset of a completion D. This includes d=1,e=0; the failure when only p,q are terminals is correctly not accepted as a sufficient case. | PASS |
| O06 | D is disjoint from F_A, because all T vertices were free for F_A. GQ4-avoid applies after the checked source consumption. D is nonempty since k>=2. Deleting it from the15-cycle leaves paths whose pairing Q satisfies that Q union D is one labeled alternating cycle. | PASS |
| O07 | Removing at least one D edge from this single alternating cycle leaves Q union J acyclic. This remains true for the d=1 two-parallel-edge multigraph boundary. Since P is a submatching of J, attaching G cannot close a component through Q union P. | PASS |
| O08 | Compressing all attached paths yields a matching L on B with holes exactly H_B union Y. Its path interiors are all A−0 and Y, each once. Isolated F_B edges are retained, not lost during compression. | PASS |
| O09 | If p or q is not a rooted terminal, an L edge pq would have to be an unchanged F_B edge, excluded already. If both are rooted, a new compressed pq edge would join their roots in Q union P; adjoining the prescribed J pair would close a cycle in Q union J. Thus pq is also absent from L. | PASS |
| O10 | The exact local classification therefore supplies the B cycle avoiding exactly Y. Expanding the disjoint recorded paths restores all31 global nonforbidden vertices and every original F_A,F_B,C edge. D disappears; new surviving edges come only from the two local short extensions and short bridges. | PASS |
| O11 | Contraposition is legitimate: if the global cycle fails and pq is not fixed in F_B, no terminal outside{p,q} exists. Ports outside S=Y union{p,q} are such terminals; an internally matched y∈Y whose mate is outside S also gives one. Conversely these exhaust impermissible terminals. This proves precisely restriction(R). | PASS |
| O12 | For all four principal cut rows, S=M union{r} is independent of the chosen Y. Every possible obstruction is r-u with u the unique unselected candidate. All choices share r, so at most one can be fixed in a matching. Removing any single choice still leaves selected sets covering every member of M. | PASS |
| O13 | Applying(R) to every nonfixed choice puts all B ports in S and keeps every internally matched member of M within S. Only r could escape. Since c has the parity of16−|H_A| and |S|−c is even, an external mate for r would leave an odd number of other internal S vertices requiring internal pairing. This contradiction forces all of S closed except its ports, and consequently all covered B vertices outside S form a global closed matching set. | PASS |
| O14 | In the three two-bridge rows A has4 majority/0 minority holes; consume2 to leave2/0. B after compression has the singleton hole and5 opposite-parity holes. The two omitted mirrors neighbor that singleton, giving exactly the r-u T15 obstruction in the table. | PASS |
| O15 | In H2,bit16, A has all5 majority holes and no minority. Choose3 of the4 nonzero majority holes, leaving0 and one other majority hole. B after compression has6 same-parity holes. The selected mirror triple has the unique common opposite-parity neighbor23, whose sole nonavoided neighbor is the unselected candidate. T63 therefore has exactly one possible obstruction23-u. All Step1 hypotheses hold despite original delta5. | PASS |
| O16 | The derived C8,C16 are the claimed eight-sets. Intersections and differences of closed mate-involution sets are closed, giving disjoint I,D8,D16. Their complement in the covered support is the stated twelve-set R_j and is also closed. | PASS |
| O17 | Each specified delta-zero cut consumes its two minority A holes, leaving two majority holes including0. Its exact T15 obstruction joins D8 to D16 and is therefore absent from F. Restriction(R) forces all B ports into S⊆U. Thus any R_j matching edge preserves that cut bit. | PASS |
| O18 | H2 preserves all three low bits on R2, and vertex1 is the unique member with its low-bit pattern. H3 preserves bits2,4 on R3, again leaving vertex1 alone in that pattern. Since R_j is closed and the matching has no loops, its covered vertex1 has no possible mate. This contradicts existence of F under the assumed absence of a global cycle. | PASS |
| O19 | Adjacent coordinate transpositions independently generate the complete stabilizer of0. The respective orbits have20 and30 members, equal exactly to the second and third accepted residual member sets. They are disjoint from the other three residual orbits. Automorphisms transport arbitrary required edges and short new edges without changing the marked forbidden vertex. | PASS |

All19 obligations are discharged. No proof repair was required. The proof
uses no probability, asymptotic limit, analytic interchange or untracked
uniformity assertion.

## Independent finite geometry and edge-quantifier verification

`A8_ORBITS2_3_REVIEW_check.py` imports and runs neither the producer nor any
prior checker. From the two hole sets it derives each zero-face, the required
bridge count delta−2, all available majority-source mirrors, and every choice
of2-of3 or3-of4 mirrors. For every choice it derives the obstruction from
the exact classification by pairwise Hamming adjacency, rather than accepting
the producer's declared obstruction edge. All13 choices agree with the
producer's sets and endpoints. In particular the delta-five cut's unique
T63 obstruction is independently identified for all four triples.

The checker then verifies all17 possibilities of retaining every choice or
discarding one possible fixed-obstruction choice; the usable source choices
always cover every candidate. It verifies40 possible special-set port subsets
with the correct crossing parity, and49 terminal-excess populations up to
the maximum seven D edges. These are endpoint/set arithmetic checks, not
enumeration of original matching instances.

All principal closed-set identities, local post-consumption hole counts,
delta-zero mirror sets, exact obstruction edges, preserved bits and isolated
vertex1 classes are recomputed. The producer's reported geometry fields
match. The independent group traversal reconstructs all five residual
orbits of sizes60,20,30,30,20 and compares their complete marked member sets;
all are disjoint. Hence the new50 cases cannot recount the old first60 or
the separately studied fourth30. No original matching instance is enumerated.

Counterexample attempts targeted paired internal mirrors, all-port mirrors,
no crossings, one alternating gap, both obstruction endpoints as terminals,
an original fixed obstruction, a new obstruction edge created by compression,
an external mate only for the distinguished r, and a hidden second T63
obstruction in the delta-five cut. The path-leaf invariant, strict terminal
excess, fixed-choice discard, prescribed root-pair and parity argument
discharge these cases. The d=1 multigraph boundary and the exact-three-of-four
neighbor condition are included. No counterexample or open gap was found.

## Verdict and remaining scope

The two stated representative theorems and all their20+30 coordinate images
are accepted relative to the explicitly audited Q4 imports, with provisional
semantic assurance. This proof alone does not establish any other residual
orbit, full A8, any complete higher-hole Q6 layer or full P6. Those claims
require their own final proof and complete assembly review.
