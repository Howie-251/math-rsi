# Q6 partial T15: independent D4/D5/D3 proof review

**PASS, sound modulo explicit frozen imports.** No open scoped issues. The new proofs establish the three named sufficient domains for arbitrary prescribed K(Q6) matchings, including long and same-parity prescribed edges. They do not establish full Q6 T15.

Reviewer `/root/q7_covered_domain_audit`, user-requested GPT-6.1-sol / high; backend identity not independently attested. Semantic assurance remains same-family / provisional. The reviewed SHA-256 bindings are in the companion JSON.

## Imports and dependency scope

The complete Q5 T44 theorem is read directly from the frozen `../six_directions/T44_Q5_CLOSURE_DRAFT.md`: four same-parity holes, any prescribed two omitted, arbitrary complete-graph matching, 30-cycle, only new short edges. Its existing PASS review and all eleven declared audited inputs were rehashed successfully. General dimension-five A2 (two same-parity holes, omit a specified one), free-root two-hole paths with the stated target parity, and balanced two-hole spanning circles are imported at exactly the interfaces in `PROOF_PACKAGE.md` section 3. That source has the same hash as the accepted (2,1) transfer context. Their literature derivation is an explicit import, not re-proved here. Neither full Q5 T15, full Q6 T15, nor full Q6 T44 is used in either new proof.

The DAG is Q5 T44 plus general two-hole results → D4/D5 and D3 single-cut transfer → D3 shared-outside-hole contradiction. The application to Q7 additionally imports the previously accepted precise (2,1) transfer. There is no reverse use of that Q7 conclusion.

## D4

A has four majority holes, including both omitted holes, and B has exactly the minority hole a and the fifth majority hole b. Since 32 minus the A hole count minus the number c of cross ports is internally matched, c is even; this argument uses vertex counts and allows arbitrary prescribed edges.

If c>0, any pairing D of the A ports is disjoint from F_A and leaves exactly the four original same-parity holes. Q5 T44 supplies a 30-cycle containing D. Nonempty D cuts the cycle into paths, and original crossings attach at distinct B ports, so compression gives a matching on all B ports. Its union with F_B has exactly the opposite-parity holes a,b; the balanced two-hole circle theorem yields a 32-cycle. Expanding the transfer paths restores all 30 included A vertices and all required original crossing edges, producing 62 vertices in one cycle.

If c=0, the B hole b has mirror bar(b) of minority global parity in A. All A holes are majority, so bar(b) is covered by F_A and occurs in the 30-cycle. At that vertex one cycle edge is prescribed and the other is unprescribed, hence short. Call the latter bar(b)t. Its B mirror is the short edge b bar(t), with bar(t) opposite parity to the free root b. The general two-hole theorem therefore gives a spanning B path from b to bar(t), even when bar(t)=a; closing by that short edge gives a spanning B cycle. The closing edge is not prescribed because b is free. Deleting the two optional mirror edges and adding the two short mirror bridges joins the two cycles. Neither omission is restored, and no prescribed edge is deleted. This discharges the zero-crossing case without a gluing assumption.

## D5: choice, suppression, and occupied-port separation

A has five holes, so c is odd and positive. Each included majority hole t has B mirror w of the minority hole's parity. Since a is not adjacent to t, w is not the sole B hole a; thus w is covered. The three candidate mirrors are different. At c=1, at most one is the sole B cross port, leaving a safe choice; no occupied-port c=1 transfer is claimed.

For the chosen t, pair X_A union {t}. If w is a cross port with actual prescribed partner d in A, require the pairing to contain td. This is valid because t is an original hole, while d is an occupied port distinct from t; all remaining ports pair freely in the complete graph. The resulting F_A union D has exactly the other four majority holes, including x,y. Every D edge therefore belongs to the Q5 T44 30-cycle.

If w is internally covered, deleting D and attaching the original crossings plus tw gives a path forest with endpoints X_B union {w}. The B attachments are distinct, so no cycle is introduced. Compression yields a matching R. Its only common covered vertex with F_B is w: all X_B vertices have their original partners across the cut. The internal partner k=F_B(w) is outside all R endpoints, so replacing kw and wq, q=R(w), by kq cannot create a loop, duplicate endpoint, or closed component. The resulting complete-graph matching has precisely holes a,w, of the same parity. A2 omits w. Expanding the suppressed two-edge path restores w and all original matching edges.

If w is a cross port, c≥3 and D has (c+1)/2≥2 edges. It is essential that D contains td. Remove td from the T44 cycle: t,d are the ends of the complementary path. Removing any second D edge on that path separates these two ends. Thus t and d lie in different components after all D edges are deleted. The actual prescribed edge dw attaches w to the d component, and the new short bridge tw joins it to the distinct t component. It cannot close a cycle. Other crossings attach at distinct degree-one B ports. The final forest has endpoints X_B minus {w} and interiors exactly the 30 included A vertices plus w. Compression again leaves precisely a,w as holes in F_B union R. A2 omits w; expansion restores it as a path interior.

In both branches the A2 circle has 31 B vertices. Adding back the 30 included A vertices and w gives 62. The four other original holes are incorporated as appropriate by the local circles. Every artificial pairing edge was deleted, every compression is expanded, and only original prescribed edges may be long.

## D3 and the odd intersection, including long edges

For a D3 cut, A contains a and four majority holes including x,y. B contains exactly the remaining included majority hole b. The mirror w of a differs from b because a is not adjacent to any included majority hole. Hence w is covered and c is positive odd. The safe branch repeats the D5 construction with special A hole a, B hole b, and auxiliary set X_A union {a}. Its suppressed B matching has holes b,w, both majority. The occupied branch c≥3 requires D to contain ad, where dw is the actual crossing edge; the same two-deleted-edges argument separates a,d. All hypotheses of Q5 T44 and A2 are met. A sole crossing with B endpoint w is the unique case the single-cut construction does not settle: with D={ad}, the bridge would close a separate A-side component.

Suppose distinct D3 cuts j,k have the same unique outside hole b and both are exceptional. Their intersection S=B_j intersection B_k fixes two independent coordinates, so has 16 vertices. Its only original hole is b, since B_j has just that hole and b belongs to B_k. Thus precisely 15 vertices of S are covered by F.

Any F edge with one endpoint s in S and another endpoint outside S must cross coordinate j or k. If it crosses j, its B_j endpoint is s. The assumed unique cross-j edge, however, has B_j endpoint w_j=a xor e_j. That point still has a's k coordinate, so is in A_k and outside S. Thus s cannot be w_j, a contradiction. Crossing k is symmetric. A long edge crossing both coordinates is subject to both arguments; shortness is never used. Consequently no prescribed edge leaves S. Matching all its 15 covered vertices internally is impossible, because an internal matching covers an even number of vertices. The two cuts therefore cannot both be exceptional, for every matching realizing the marked holes. This is the universal local property required by the Q7 transfer, rather than a successful sample matching.

## Adversarial and deterministic checks

Reviewed boundaries include c=0, c=1 safe/occupied, c=3 occupied, a chosen mirror at a B port, long crossing partners with unrelated local labels, a suppressed partner sharing a parity, and the two exceptional cross edges being potentially the same long edge. The proofs use no port-label equality, bipartiteness of arbitrary prescribed edges, or assumption that cross edges change only one coordinate.

The independent topology script enumerates cycle lengths 6 through 14 and disjoint removed cycle-edge sets up to four edges. It checks degrees, endpoint sets, absence of closed components, and all interior vertices. Results: 1767 D4 forests; 10896 safe mirror/suppression forests; 10716 forced-pair c≥3 occupied forests. All pass. The 180 c=1 occupied cases all form the correctly excluded closed component. A separate exhaustive Q6 incidence check covers all 737280 possible edges leaving the two-coordinate intersection, including long edges; every such exit violates a required sole-crossing mirror endpoint. These checks supplement the universal analytical arguments above and do not replace them.

The companion JSON contains the closed obligation ledger, exact source/import hashes, and deterministic artifact hashes. No source theorem, producer, state, or frozen file was changed.
