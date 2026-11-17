# Q6 S2 transfer audit — proposition one only

PASS modulo the named accepted imports. This is a same-family, provisional semantic audit, not a formal proof or cross-family acceptance. The user-authorized reviewer route is GPT-6.1-sol high, relayed by the parent; service identity is not independently attested. No S2 pilot certificate is used.

## Exact accepted statement

For every matching F in K(Q6), with holes a (minority) and five majority vertices, and designated majority omissions f,g, suppose a is nonadjacent to the three included majority holes. A coordinate face A contains a and exactly two majority holes b,f, with b included, while B contains the other three majority holes including g. Suppose also a is nonadjacent to g. If F does not have exactly one crossing whose B endpoint is w=a xor e_j, then F extends to a simple 62-cycle omitting exactly f,g, adding only short edges. Prescribed edges may be long or join equal parity vertices.

The claim is a sufficient construction with one untreated branch. It does not claim that the exceptional matchings lack the required cycle. The later lemma, proposition two, root enumeration, core385 transport, rank inputs, and pilot closure in the producer document are outside this acceptance.

## Imports and dependency accounting

1. Dimension-five A2: any complete-graph matching with two distinct same-parity holes extends to the 31-cycle omitting the designated one, with only new short edges. This is the precise interface in PROOF_PACKAGE.md section 3, imported as an already accepted literature consequence.
2. Complete dimension-five T44: any complete-graph matching with four distinct same-parity holes extends to the 30-cycle omitting any prescribed two of them, with only new short edges. The source is ../six_directions/T44_Q5_CLOSURE_DRAFT.md and its PASS review. This audit imports that accepted theorem at its stated quantifiers.

The dependency graph is A2,T44 -> S2 proposition one. The fiber review additionally imports the already accepted D3 single-cut transfer. Neither dependency uses this S2 pilot or a full six-dimensional T15 theorem. Hashes and live import checks are in the companion JSON.

## Proof obligations

S2-01, hole and port accounting. A has 32 vertices and three original holes, so 29-c vertices are matched internally. Thus c is positive odd and at most 29; no bipartiteness of F is needed. Neither a nor b,f is a port. The mirror w is a majority vertex in B. It cannot be an included hole by the nonadjacency hypothesis, nor g by the additional S2 hypothesis. Those exhaust B's original holes, so w is covered.

S2-02, auxiliary matching. If w is covered internally choose any A port d. If w is a port and c>=3, choose its actual F partner d in A. On X_A minus {d} choose any perfect matching D; the set has even cardinality c-1. Its endpoints are disjoint from F_A and from a,d. Consequently F_A union D union {ad} is a matching, with exactly holes b,f and no others. Artificial ad is a legitimate complete-graph edge even if long or same parity. A2 applies to these same-parity holes and omits f. Removing the included edge ad from the resulting 31-cycle gives a simple spanning d-to-a path P on A minus {f}, retaining F_A and D.

S2-03, internally covered w. Delete D from P; this creates |D|+1 path components, with ends X_A union {a}. Every A port receives its original crossing to a different B port; a receives the short bridge aw. All B attachments X_B union {w} are distinct. They are fresh degree-one attachments, so no cycle or identification is introduced. All A vertices in P now have degree two, and compression gives a matching R on X_B union {w}.

S2-04, suppression. F_B and R intersect in exactly the covered vertex w. Write t=F_B(w) and q=R(w). Vertex t is internally matched in B, hence outside X_B union {w}, so t is not an endpoint of R and t!=q. Replacing tw,wq by tq gives a matching without a loop, repeated endpoint, or closed component. The original three B holes and the now suppressed w are precisely its four holes. All four have the same parity. T44 may therefore omit g,w. Every compressed edge is prescribed in that cycle and can be expanded uniquely. Expansion recovers w and all 31 vertices of A minus {f}. The count is 30+1+31=62, exactly Q6 minus {f,g}.

S2-05, port w and c>=3. Here D has at least one edge. Since P is a simple path with ends d,a, deleting any D edge separates d and a; deleting further edges cannot reconnect them. Attach the original crossings at distinct B ports. The crossing dw has attached w to the d component. The new short bridge aw joins that component to the distinct a component; it cannot close a cycle. Other crossing attachments cannot identify components. The result is a path forest whose endpoints are exactly X_B minus {w}, and whose internal vertices are (A minus {f}) union {w}. Its compression R is a matching disjoint from F_B. The union has exactly the three original B holes and w, all same parity. T44 omitting g,w applies, and expansion gives the same 62 vertices and a single cycle.

S2-06, edge preservation. Every F_A edge is in P and survives; every F crossing is explicitly attached; every F_B edge is either retained directly or recovered by the suppression expansion. All D edges and ad were deleted. The only extra bridge is the short aw; all remaining added edges come from the local A2/T44 short extensions. Expansions are along internally disjoint paths, so the final graph is simple as a cycle even when artificial compressed edges were long. No parity restriction is imposed on the prescribed edges at any step.

S2-07, completeness and boundary checks. w covered gives exactly the internal or port branches. The only omitted branch is c=1 with port w. Then D is empty and dw plus aw would close P into an isolated component; the present construction does not settle it. The c=1 internally covered branch remains valid. At c=3 the single D edge suffices to separate d,a. The candidate c=0 is impossible by vertex count. The candidate suppression loop t=q is impossible because t lies outside R's endpoint set. These checks discharge the hidden degeneracies without assuming a short crossing edge or equal coordinate labels at its endpoints.

## Acceptance boundary

There are no open fatal, critical, or major issues within proposition one. This acceptance supplies exactly the nonexceptional S2 transfer needed by the anchored-fiber contradiction. It accepts no finite rank certificate and establishes neither complete S2 exceptional closure, full Q6 T15, the full Q7 eight-hole layer, nor P7.
