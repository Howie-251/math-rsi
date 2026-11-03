# Proof obligations and assumptions

All statements quantify over the actual finite simple undirected graph with maximum degree at most eight and the explicit edge-or-two-edge-path property. Matrices are derived from that same graph. No separately chosen defect matrix is admitted.

## Typed symbols

| Symbol | Type and role |
|---|---|
| A | Integer adjacency matrix, also viewed over Q when needed |
| B | Integer matrix A²+A−7I−J, symmetric, nonnegative, zero diagonal |
| t(v), T | Nonnegative integer local and global triangle counts |
| N15 | At every zero vertex, exact 2211 defect row; full induced equal-weight matching where transport is used |
| P,H,Y,S (endpoint proof) | Root-neighbor set, its induced graph, outside vertices, three parents of z |
| C,I,E (Brown proof) | Disjoint fixed Brown vertex classes of sizes 8,21,28; I here is not an identity matrix |
| d_v,j,e,sigma,k | Nonnegative integer deletion/incidence counts |
| R,Z,m | Repeated internal points, a six-point set, uncovered internal point |
| P (n63) | Permutation matrix representing defect components; not assumed an automorphism of G |
| R_r,H,C_ell,F_ell | Polynomials over Q, with explicitly integer coefficients |
| K,alpha | Degree-d quotient field Q[X]/(C_ell) and canonical root |
| W,T,U (n63) | Rational sum-zero space and restrictions of A,B; T here is not a triangle count |
| p,q,e_ell | Nonnegative integer characteristic-factor exponents |

The symbol reuse is confined to explicitly separated proofs. No inference transfers a symbol with a different type between them.

## Dependency DAG

`actual graph -> root bound -> regularity -> defect/nonnegative/repeat/commutation identities`.

`identities + zero N15 -> isolated parent -> parent is zero -> forced light pair -> no zero-to-t2 heavy entry`.

`Brown edge facts + n58 regularity -> deficits + triangle destruction -> 20/21 coverage -> checked family properties -> incidence bounds -> eight-III-plus-EE contradiction`.

`n63 actual row-two defect -> cycle/doubled-edge permutation -> orbit-bounded annihilator`.

`cyclotomic irreducibility + finite Laurent lifts -> C_ell irreducibility -> norm identity + finite residues -> quadratic/composition irreducibility`.

`annihilator + composition factors + rational W -> characteristic-factor support -> degree/trace identities -> 46=5(p−q)`.

`full zero N15 + commutation -> transport -> weighted-triangle obstruction`.

`T=2 shared edge + heavy-endpoint exclusion + transport -> tip B=1 -> fourth-trace congruence -> both tip residuals 21 -> weighted-triangle contradiction`.

The graph is acyclic. In particular, the heavy-endpoint lemma does not use the shared-edge exclusion; the norm argument does not establish the cyclotomic irreducibility used to define its field; the present Brown branch does not need a prior exclusion of all smaller deletion counts.

## Assumption ledger

| Result | Hypotheses actually needed and discharge |
|---|---|
| Heavy-endpoint exclusion | Order59 legality supplies regularity, defect identities and budget6. Global zero-row 2211 and light-pair adjacency are explicit. The proof establishes t(p)=0 before applying them at p. |
| Brown branch exclusion | Order58 legality supplies regularity and triangle cap3. Exactly eight distinct III single-edge deletions plus one EE deletion is the branch hypothesis. Fixed graph facts and all 14+84 family facts are independently checked. |
| n63 rational exclusion | Order63 legality supplies regularity and row-two defect. Cycle classification proves the permutation representation. Exact finite identities and standard characteristic-zero field algebra supply all arithmetic steps. |
| Transport | Full induced-matching N15 at the particular zero vertex x and positive B[r,x]; both are explicit at each use. Symmetry and commutation are universal defect identities. |
| Weighted triangle support | Entire support, exact weights111/2/1, actual triangle, two zero endpoints. Each is part of the local statement and verified in the final tip-row application. |
| Shared-edge exclusion | Order59 legality, exactly two distinct triangles sharing an edge, full N15 at every zero. Endpoint lemma applies with no H5 qualification. Fourth-cycle trace identity is universal. |

## Canonical quantified conclusions

- For every legal order59 graph satisfying the stated zero-row assumption, for every zero z and every v, B[z,v]=2 implies t(v)≤1.
- For every legal order58 graph on Brown57's labeled vertices plus one new vertex, its deleted Brown-edge set cannot have the specified eight-III-plus-one-EE form.
- There is no legal order63 graph, at the paper-proof level of the checked rational route.
- For every legal order59 graph satisfying full zero-row N15, its complete triangle set cannot consist of exactly two triangles with a shared edge.
- For every row of such a defect matrix, full support111 on an actual triangle plus21 on two zero vertices is impossible, independent of the graph's total triangle count.

There are no asymptotic estimates, probability claims, or analytic interchanges. All sums, products, spaces and enumerations are finite. The detailed machine-readable micro-claim ledger is `obligations.json`; formal implementation obligations are separated from paper obligations.
