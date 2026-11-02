# Proof obligations and dependency skeleton

All entries concern finite exact identities; there are no limiting,
probabilistic, integration, or asymptotic obligations.

## Typed objects and hypotheses

- `A`: the adjacency matrix of one fixed simple undirected 8-regular
  graph on 61 vertices, diameter at most two.
- `B=A^2+A-7I-J`: the defect matrix of that same graph. Connected positive
  support, nonnegative entries in `{0,1,2}`, zero diagonal and row sum four
  are explicit accepted imports. Commutation follows from `AJ=JA=8J`.
- `u,v,s,t,p,q`: vertices; only `u,v,s,t` are initially distinct. The
  location proof subsequently establishes `p in T`, `q in S`, hence all
  six are distinct.
- `U,V,S,T,Z`: disjoint actual vertex sets, respectively of sizes
  `5,5,6,6,35`, defined and proved to exhaust the vertices outside the core.
- `C=B[U,V]`: integral nonnegative 5-by-5 matrix with all margins two.
- `K=A[S,T]`: binary 6-by-6 matrix, degree two at row `q` and column `p`,
  degree one elsewhere; total seven edges.
- `P=B[S,T]`: 6-by-6 permutation matrix, variable relative to `K`.
- `L`: actual `Z` incidence counts between `S,T` classes; `L=J-K+P`.
- `E=N(p) intersect S`, `F=N(q) intersect T`: two-element sets.
- `epsilon=A_pq`, `eta=B_pq`: binary scalars; no choice is fixed.
- Cycle lemma only: `n>=3` odd, `H` a real `n`-by-`n` matrix commuting
  with `C_n` and having constant diagonal. Here `C_n` denotes cycle
  adjacency, not the 5-by-5 matrix `C` from the local note.

## Canonical statements

For every `A` as above, conditional on the accepted imports, and every
ordered adjacent pair `u,v` with `B_uv=2`, there exist labels and actual
sets of vertices satisfying local equations (1)–(17) and one of the seven
`C` types. The label choices do not assert an automorphism or impose
extra original edges. This is a necessary template only.

For every odd integer `n>=3` and every real matrix `H` indexed by
`Z/nZ`, if `HC_n=C_nH` and all diagonal entries are equal, then
`H_{i+1,j+1}=H_ij` for all indices. Symmetry is not a hypothesis.

For every actual `A` above, `B != 2A(C_61)` under every vertex labeling.
With accepted nonnegative row-four connected support, the graph of
entries `B_uv=2` is a disjoint union of paths and isolated vertices.

## Dependency DAG and discharged claims

`Actual A + imports -> core -> partition -> ports -> layer degrees`

`partition + commutation -> C margins/cells -> seven C types`

`ports + commutation -> four port bijections -> compatible S/T labels`

`core + layer degrees + commutation -> ST permutation + internal/remaining ports`

`odd n + commuting H + constant diagonal -> circulancy`

`actual A + all-double cycle -> circulancy -> radius-two bound -> contradiction`

`contradiction + connected row-four B -> double-support path forest`

No cycle in these dependencies is used; neither local normalization nor
the cycle obstruction relies on an adjacent-double exclusion.

| ID | Obligation and used assumptions | Disposition / evidence |
|---|---|---|
| L1 | Adjacent double pair forces two triangles and saturated u,v rows | Discharged: `mu=B` for an edge and row-four nonnegativity |
| L2 | st nonedge, B_st=1, external unit ports | Discharged: extra triangle contradiction and connected support |
| L3 | Ports not adjacent to their own parents; exact triangle counts | Discharged: neighbor-defect sum `2+A_sp` is even |
| L4 | Independent disjoint U,V,S,T and (4) | Discharged: exact common-neighbor/triangle counts; polynomial identity and commutation |
| L5 | Exact neighborhood blocks (5), unique U/V incidence | Discharged: actual additional-common-neighbor count, not support alone |
| L6 | Complete 61-point partition | Discharged: 35 distinct U endpoints, excluded S/T endpoints, size equality |
| L7 | p in T, q in S and all U/V external defect sums | Discharged: nonnegative (7), proved partition, own-parent nonadjacencies |
| L8 | Every layer degree and A[Z] four-regular | Discharged: (1) against core vertices and original degree eight |
| L9 | C margins two and actual cell size 1+C_ij | Discharged: Bg=-2g and actual shared Z-neighborhoods |
| L10 | P permutation and L=J-K+P | Discharged: both commutation margins and actual S/T shared neighborhoods |
| L11 | Internal defect edges (13), Z-port counts (14)–(16) | Discharged: exact N(s),N(t) blocks, commutation and full row budget |
| L12 | Two five-point transversals and overlap (17) | Discharged; parent corrected MINOR-1 and reviewer reread it |
| N1 | Exactly seven independent U/V types | Discharged: bipartite cycles and two alternating perfect matchings |
| N2 | All four ports are bijections | Discharged: (7) for S/T side, (s,u_i),(t,u_i) and symmetric equations for U/V side |
| N3 | S/T labeling compatible with C and cell labels | Discharged: independent S/T permutations; V maps and transversal remain variable |
| C1 | Odd-cycle constant-diagonal commutant lemma | Discharged: recurrence reaches the diagonal using invertibility of two |
| C2 | All-double 61-cycle impossible | Discharged: original A meets lemma hypotheses; two-step ball at most 41 |
| C3 | Double-support is a path forest | Discharged modulo imports: saturation, connectedness and C2 |
| M1 | Full graph model specification covers all actual adjacent-double graphs | Discharged: same 61 labels, all1830 pairs, row-seven H cell layout and independent S/T labels; implementation unreviewed |
| M2 | Between any two U groups in Z, and likewise V groups, A[Z] induces a perfect matching | Discharged: actual `mu(U_i,z)=d_Z_i(z)=1-A_U_i,z`, and the symmetric V identity |
| P1 | Exact S/T color-neighbor counts use the same A | Discharged: full original neighborhood of each S/T point and inherited unit port counts |
| P2 | K/P overlap only at (q,p) | Discharged: actual S/T/Z triangle forces both exceptional port columns |
| P3 | No edge inside any S/T parent class in Z | Discharged: putative edge forces epsilon0 eta1 and an exact closed eight-point B component |
| P4 | Ordinary S/T points triangle-free; q,p unique triangle exactly in epsilon1 eta1 | Discharged: all possible neighborhood edges accounted for using P2/P3 |
| P5 | Exactly 5-epsilon repeated S neighbor colors, and likewise T | Discharged: exact color formula, zero rows on ordinary E/F, and unique q/p port when epsilon1 |
| N4 | Revised binary port thresholds and selected-case coverage | Discharged: c=1+B on binary ST/SZ/TZ interfaces; one positive selector unit in the exactly-one seven-type model |
| N5 | Within-cell parent lex order preserves actual-graph representatives and uses1050 clauses/case | Discharged: permute all incident A edges within actual UV cells;105 clauses/comparison times35−25 comparisons |

The P1–P5 delta reuses the initial review context. Its dependency is
`L11/L12 -> P1 -> P2 -> P3 -> P4/P5`, with connected support additionally
used for P3. It introduces no dependency on a solver result, and retains
all seven C types and all four `(epsilon,eta)` cases.

## Open research, not missing proof of the claimed statements

The actual 35-vertex completion, a full original-graph encoding and its
coverage/evidence, exclusion of adjacent doubles, exclusion of nonadjacent
doubles, and general order61 nonexistence are not proved here. None is
needed to justify the stated necessary template or path-forest theorem.
