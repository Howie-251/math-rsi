# Common attachments are impossible at an internal double vertex

## Statement and status

For an actual simple order61 degree8 diameter-two graph A, use the inherited actual defect matrix B=A^2+A-7I-J and its double-support path forest D. For every consecutive D-path triple u,v,w,
N_A(u) intersect N_A(w) is a subset of N_A(v).

Equivalently the local common-attachment number h is zero. Thus only (r,h,beta)=(1,0,0) and (2,0,1) remain. This is a computation-assisted structural claim, root-checked, accepted by the explicitly reused local integration check and actual Gemini round3; it is not an internal-D or order61 exclusion and is not formalized in Lean.

## Complete reduction and actual checked contradiction

The inherited actual61 baseline and D-path forest are CONNECTED_TRIPLE_EXCLUSION.md and DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md, with their previously reviewed finite and checked-CNF dependencies. No old computation is rerun.

INTERNAL_DOUBLE_PATH_LOCAL.md partitions any selected triple into u,v,w, T=N_A(v), and Z, with P=N_A(u) intersect Z and Q=N_A(w) intersect Z. INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md proves epsilon=0, rh=0 and h<=1, leaving exactly the three types listed in INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md. If h>0, the only remaining type is (r,h,beta)=(0,1,0).

Sections1–3 of that design map EVERY such actual graph to the specified labels, using unused neutral-parent permutations and within-class attachment labels. The h1 case uses no reference matching normalization. Its complete original adjacency has1086 free bits and74 fixed edges; the full61 original vertex set is retained. There is no seed, group, edit radius or arbitrary matching restriction.

The stable implementation computations/dd82/n61/internal_double_full61_run/encode.py encodes every original degree and all1830 original pair coverages, using actual-A common-neighbor paths, exact short defect counts and the proved shared-attachment row conditions. For this h1 input, the optional r2 endpoint-domain constraints are not invoked. Every hypothetical graph in this case gives satisfying values to the actual edge and exact auxiliary bits.

Mathematical representation and labels passed DELTA_PORT_MODEL_AUDIT.md and actual Gemini round2. A separate fresh static source check found no blocking issue in SOURCE_REVIEW.md, both under reviews/dd82/proof-checker-n61-internal-path-20261013/. Root executed the new short-counter Boolean sanity and the preparation's emitted-CNF semantic comparison; these checks support implementation semantics and are not themselves impossibility proofs.

The actual r0_h1_b0 input has53046 variables and163721 clauses. CaDiCaL returned exit20 after4.012334 CPU seconds, producing a complete11623492-byte LRAT proof. The existing independent lrat-trim0.2.0 checked THAT saved input and proof, returned exit20 with the exact line s VERIFIED, and used0.113276 CPU seconds. Evidence:
- computations/dd82/n61/internal_double_full61_run/r0_h1_b0/input.cnf
- the same directory's proof.lrat, result.json, certificate_check.json and certificate_check.log.

Therefore this exact CNF is contradictory. The coverage implication above excludes every actual graph/triple in the h1 type. Combining with the pure reductions yields h=0.

## Direct consequences and limits

Every common neighbor of u,w lies in T or Z because their pair and the two consecutive D edges are original nonedges. There is no common neighbor in Z when h=0, proving the statement.

The remaining intersection size is r=1+beta. On any D component with at least four vertices, each consecutive triple has at least one endpoint internal to D; that endpoint's double-neighbor row already spends its four defect units, so beta=B_uw=0. Consequently each such triple has exactly one common original neighbor, and it is adjacent to all three vertices. On a three-vertex D component, r may be1 or2.

For any original vertex x, the binary sequence A[x,v_i] along a D path cannot contain the consecutive pattern101: the two ones would make x a common neighbor of v_i,v_{i+2}, hence also adjacent to v_{i+1}. This is a short consequence, not an assumed graph automorphism or a full path classification.

The two other actual inputs r1_h0_b0 and r2_h0_b1 returned UNKNOWN after56.298772 and57.767905 CPU seconds respectively. Their partial LRAT traces are not certificates. No complete graph was found. Both remaining types, the entire internal-D branch and general58–61 remain open;57<=N(8,2)<=61 is unchanged.

