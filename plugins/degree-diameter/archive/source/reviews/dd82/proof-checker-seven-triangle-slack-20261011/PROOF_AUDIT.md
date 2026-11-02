# Audit of the seven-triangle exclusion and heavy cross-slack charging

**Verdict: PASS — same-family, provisional.** All 37 recorded obligations are discharged in this paper-proof review. No FATAL, CRITICAL, MAJOR or MINOR defect was found. No source edit or strengthened hypothesis is needed for the three stated conditional claims.

The requested reviewer route was `gpt-6-astra` with reasoning `ultra`, in a fresh context, task `/root/proof_review_seven_triangle_slack`. The backend did not independently attest the actual model or effort. This report records the requested route rather than claiming such attestation. A bounded trace-obligation shard supplied additional derivations, not a separate acceptance decision.

The primary files reviewed in full are:

- `proofs/dd82/n59/seven_triangles_twenty_core_exclusion_20261011.md` (**S**).
- `proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md` (**H**).

The full global-capacity proof (**G**), arbitrary-root support-transport proof (**P**), and matching-zero fourth/fifth-trace proof (**F**) listed in `PROOF_SKELETON.md` were read and their load-bearing arguments rederived. Prior review verdicts and the papers' own status labels were not evidence for acceptance. No web source, computation, formalization, or order-63–65 exclusion was used.

## Claims supported by this review

Under the explicit hypothesis that every zero-triangle vertex of the original legal order-59 graph has an actual exact N15 row:

1. The entire T=7,m=20 case is impossible. Hence a seven-triangle graph has m=21 and its triangles are vertex-disjoint.
2. The number K of heavy cross defect pairs satisfies K≤R_NZ≤2(4m−3T−59).
3. If T=7,m=21, the additional condition that every N–N nonedge has zero defect is impossible.

The positive-N–N-nonedge branch at T=7,m=21 remains open. These proofs do not establish N15 for arbitrary legal graphs, exclude all seven-triangle graphs, close H5, or exclude arbitrary order-59 graphs.

## Actual graph foundations and global capacity

**F01–F03.** A vertex of degree at most seven reaches at most 1+7+7·7=57 vertices in two steps. Thus every degree is eight. With the actual adjacency matrix,

\[
B=A^2+A-7I-J
\]

has zero diagonal, nonnegative integer off-diagonal entries, row sum 64+8−7−59=6, and commutes with A because the graph is regular. At distinct vertices B_xy equals c(x,y) on edges and c(x,y)−1 on nonedges. The neighbor and nonedge row budgets are respectively 2t(x) and 6−2t(x). A genuine edge incident to a zero vertex has defect zero. These facts discharge the actual-graph hypotheses everywhere they are used.

**G01–G02.** On an independent set U⊆Z, no zero row can have both its equal-weight defect endpoints in U, because N15 makes those two endpoints adjacent. Consequently each of the two positive-weight classes is a matching on U; a positive-defect triangle is impossible. If r,s had three common zero neighbors, those neighbors would form an independent set and every pair would have positive defect, yielding precisely such a triangle. This proves the common-zero-neighbor bound for every pair, without assuming N15 at a nonzero root.

**G03–G05.** For U_n=N_G(n)∩Z, a common neighbor of z,w∈U_n other than n cannot lie in N_G(n), because that would create a triangle at z. Therefore

\[
\ell_n+2h_n=\sum_{y\notin N_G[n]}\binom{q_y}{2}.
\]

For every such y, binom(q_y,2)≤B_ny. For a zero heavy endpoint this improves by one. Each pointwise residual is nonnegative, and the exact row budget gives

\[
6-2t(n)=\ell_n+2h_n+k_n+R_n.
\]

N15 gives 2|Z|=2H_ZZ+K. Every heavy ZZ pair has three common neighbors and at most two zero common neighbors, so it has at least one nonzero common neighbor. Thus D=Σh_n−H_ZZ≥0. Summation proves the exact identity

\[
2(4m-3T-59)=\sum_n\ell_n+2D+\sum_nR_n.
\]

There is no dropped negative term or multiplicity error. Each heavy cross pair is counted once at its N endpoint, and each heavy ZZ pair twice in zero heavy degree.

**G06–G07.** The incidence inequality m≤3T yields m≥20,T≥7. If T=7,m=20, the entire nonnegative right side above vanishes. Each light ZZ pair has no common neighbor in N; each heavy ZZ pair has exactly one; every pointwise residual is zero. These are exactly the equality facts used in S.

## Transport is valid at nonzero roots

**P01–P02.** If x∈Z and B_vx>0, the row of x satisfies exact N15, so v has exactly one neighbor in that row's positive support, its equal-weight partner. Therefore (BA)_xv=B_xv. Symmetry and AB=BA imply

\[
\sum_{w\sim x}B_{vw}=B_{vx}.
\]

The assumption is at x; v may be any vertex. No nonzero row is assigned N15 without proof. If zero support vertices x,y are adjacent in row v, the two transport equations give B_vx≥B_vy and B_vy≥B_vx. Equality forces both endpoints to have no other positive support neighbor. If x has no zero support neighbor, its nonzero support neighbors have total row weight B_vx; they are independent because x lies in no triangle.

**X03.** If v∈N has two zero nonedge repeats of weight two, their weight four forces 6−2t(v)≥4 and hence t(v)=1. They exhaust the nonedge budget. The only other positive entries are its two unit triangle partners a,b. At one heavy zero x, transport gives 2=2A_xy+A_xa+A_xb. Since a∼b and x is zero, the last two terms sum to at most one, so x∼y. This argument uses no triangle-core classification, so its use in the general charging lemma is valid.

## Entire T=7,m=20 exclusion

**X01.** A positive N–N nonedge has, by the pointwise equality, defect one and exactly two zero common neighbors z,w. The pair z,w is a nonedge with positive defect and has two nonzero common neighbors. Its defect is either one or two by N15. Both contradict the corresponding equality multiplicity above. Thus every N–N nonedge has zero defect.

**X02.** There are 21 triangle incidences on 20 vertices with positive incidence. Exactly one vertex occurs twice; the other nineteen occur once. The two overlapping triangles share only this vertex, and the five other triangles are disjoint. In particular no edge belongs to two triangles, and every positive defect on a true edge in N is one.

**X04.** A heavy cross pair u,z has two zero common neighbors x,y and exactly one nonzero common neighbor v. Each of v,x and v,y is a nonedge with common neighbors u,z. A light value would contradict the equality rule because u is nonzero. Their zero endpoints bound their defect values by two, so both are heavy. X03 then forces x∼y, contrary to x,y having the common neighbor u and being zero vertices. This rules out every heavy cross pair, without a row-count branch split.

**X05–X06.** Every nonzero row now has only unit entries and row square sum six. Every zero row has row square sum ten. Hence s=20·6+39·10=510. The fourth trace gives

\[
8C_4=6\cdot59+510-12\cdot7=780\equiv4\pmod8,
\]

which is impossible. Finally 20≤m≤21 under T=7, so m=21 and all triangles are vertex-disjoint. This establishes the entire stated equality-case exclusion.

## General charging: exhaustive cases and injectivity

**C01.** At a cross nonedge the complete pointwise possibilities are:

| B_nz | Possible q | r(n,z) |
|---:|---|---|
| 0 | 0 or 1 | 0 |
| 1 | 0 or 1 | 1 |
| 1 | 2 | 0 |
| 2 | 0 or 1 | 1 |
| 2 | 2 | 0 |

The exclusion of q=2 in the first row follows from c(n,z)=B_nz+1. This table accounts for q=0,1,2 and proves r∈{0,1}; adjacent cross pairs cannot have positive defect.

**C02–C04.** A heavy source with q≤1 charges its own r=1 term. A heavy source n,z with q=2 has common neighbors x,y∈Z and v∈N. Each v,x and v,y is a cross nonedge with at least the common neighbors n,z, and N15 bounds each positive defect by two. They cannot both be heavy: X03 would force x∼y, creating a triangle at a zero vertex through n. At least one is light. A selected light pair v,x has exactly two common neighbors, namely n∈N and z∈Z; therefore q(v,x)=1 and its r term is one.

**C05.** A fixed ordering of vertices can select the first available light target if one wants an explicit function; the proof's arbitrary selection works equally well. From any selected light target v,x, its unique nonzero and unique zero common neighbors recover the source n,z. Two distinct heavy sources cannot have the same light target. Self-heavy targets are distinct for distinct sources and are disjoint from light targets by their defect weights. Thus the map is injective into the unit terms counted by R_NZ. There is no assumption that source and target roots are the same, and no double counting of unordered cross pairs.

**C06.** R_NZ is a subset of the pointwise nonnegative terms in ΣR_n. The exact global identity therefore gives K≤R_NZ≤2(4m−3T−59). No equality-case or trace argument enters this general lemma.

## The isolated-light correction in the repeat-free core

Assume only for this part T=7,m=21 and B_uv=0 on N–N nonedges.

**B01–B02.** Triangle incidence forces t(n)=1 at every nonzero root. Its nonzero positive support is precisely the unit edge formed by its triangle partners. Its zero nonedge support has total weight four, so the only partitions are 22,211,1111. A heavy vertex in 211 cannot have a zero support neighbor of equal weight; its possible nonzero support neighbors form an independent subset of a unit edge and cannot supply weight two. Thus 211 is impossible. In 22 the two zero support vertices must be adjacent and form an isolated full-support edge. In 1111 there are p_n=0,1,2 matching edges and 4−2p_n isolated vertices.

**B03.** Each isolated light x has, by transport, one unit neighbor among its root n's triangle partners. This is a nonzero common neighbor of n,x. Since B_nx=1, the pair has exactly two common neighbors, hence q(n,x)≤1 and r(n,x)=1. Summing gives exactly 2b distinct isolated-light cross terms. The proof does not discard the p_n=0 or p_n=1 cases.

**B04.** Consider any light target v,x selected from a q=2 heavy source n,z. Root n is of type 22. The zero support edge containing z is isolated in the full support, so z is adjacent to neither triangle partner of n. Its nonzero common neighbor v with n is therefore not a triangle partner of n. Equivalently n is not a triangle partner of v.

The only common neighbors of the target v,x are n and z. Every positive nonzero support vertex of row v is a triangle partner of v, hence a true neighbor of v. If such a vertex were adjacent to x, it would have to be n or z. It cannot be z because z∈Z; it cannot be n because n is not a triangle partner of v. Thus x has no positive nonzero support neighbor at root v. Transport forces x to have a zero support neighbor, so this charged target is paired. In particular it is not among the isolated-light terms. The repeat-free-core hypothesis is used exactly here and was not imported into the general charging lemma.

**B05.** There are K=2a heavy cross pairs. Their injective targets and the 2b isolated-light terms are pairwise disjoint, yielding 2a+2b≤R_NZ. The available slack is 2(4·21−3·7−59)=8; hence a+b≤4.

## Trace identities and the final integer obstruction

**T01.** Set s=tr(B²). From the actual defect identity, tr(AB)=6T and tr(A²B)=s−6T+6n. Direct expansion of the latter gives tr(A⁴)+6T−120n, hence tr(A⁴)=126n+s−12T. Four-step closed walks comprise the simple four-cycles and backtracking walks, with tr(A⁴)=8C_4+n·8(2·8−1)=8C_4+120n. Thus 8C_4=6n+s−12T. This count permits chords in C_4.

**T02–T03.** Let w=tr(AB²). Substitution using A²=7I+J+B−A gives

\[
\operatorname{tr}(A^3B)=48T+42n+w-s,
\qquad
\operatorname{tr}(A^5)=428n+w-2s+102T.
\]

A five-step closed walk whose five cyclic vertices are distinct contributes to a simple five-cycle. Otherwise, a repeated position at cyclic distance two yields a backtrack whose removal leaves a triangle. Its used edges form that triangle, possibly with one attached edge used out and back. The used triangle is unique even if the original graph has extra chords. At a fixed triangle there are 30 internal walks (three choices of tripled edge, two directions, five starts) and 180 external walks (3·(8−2) outward edges, two directions, five starts). Thus tr(A⁵)=10C_5+210T.

**T04.** Combining gives 10C_5=428n+w−2s−108T. At a zero N15 row, s_v=10 and Q_2(v)=2·2+1·1=5, so e_v=0. Consequently

\[
5C_5=209\cdot59+\sum_{n\in N}e_n-54T,
\qquad
\sum_{n\in N}e_n+T\equiv4\pmod5.
\]

**B06–B07.** At each nonzero root in the current branch, Q_N=1 and s_N=2. The transport decomposition gives e_n=5+Q_N−s_N−K_n=4−K_n. In a 22 row K_n=4, so e_n=0. In a 1111 row K_n=p_n, so e_n=4−p_n. Hence

\[
s=38\cdot10+10a+6(21-a)=506+4a,
\qquad
\sum_{n\in N}e_n=42-2a+b.
\]

The fourth trace becomes 8C_4=776+4a, so a is even. The fifth-trace congruence gives 49−2a+b≡4 (mod 5), or b≡2a (mod 5).

**B08–B09.** From a+b≤4 and a even, the only cases are a=0,2,4. For a=2 the required residue b≡4 is outside 0≤b≤2; for a=4 the required residue b≡3 contradicts b=0. For a=0 one gets b=0. In particular all 21 nonzero roots have four light zero repeats, contributing 84 distinct cross light incidences. The 38 zero rows each have exactly two light endpoints and can supply at most 76 such incidences. This is the stated contradiction. No conclusion is drawn about the excluded premise's complement.

## Counterexample attempts and boundary checks

The following attacks were checked algebraically against the actual hypotheses; none produced a counterexample.

- Three common zero neighbors: rejected by the two matching weight classes on their independent set.
- Equality-case light or heavy N–N nonedge: both force a ZZ defect pair with too many nonzero common neighbors.
- Transport used at a nonzero root: the row to which N15 is applied is the zero endpoint's row, and symmetry plus commutation transfers the equation.
- Both derived repeats of a q=2 heavy source heavy: their budget forces one triangle at the derived root, and transport creates a forbidden zero triangle.
- Two heavy sources sharing a light target: the target's exactly two common neighbors uniquely recover its source.
- A self-heavy target colliding with a derived light target: the defect weights differ.
- A heavy charged light target also being isolated: in the repeat-free branch the unique nonzero common neighbor cannot be a triangle partner, so transport forces pairing.
- Unpaired 1111 supports: p=0 and p=1 were retained through the correction b, with 2b separately charged slack terms.
- Boundary a=0,2,4 and allowed b: each permitted integer interval was checked; no omitted parity or residue case remains.
- Extra graph chords in a five-walk support: they do not alter the set of traversed edges or the unique triangle assigned to a non-simple walk.

No graph enumeration or unsuccessful numerical search was used as evidence for a universal proof step.

## Obligation closure and artifacts

All 37 micro-claims in `PROOF_SKELETON.md` are discharged above. No assumptions were added, conclusions weakened, or source papers modified. There are no infinite interchanges, stochastic assertions, asymptotic claims, or WLOG reductions requiring further checks. The only choice of target is finite and its injectivity holds for every admissible selection.

The audit is a single fresh semantic review round, with a separate bounded trace-derivation shard. It remains same-family and provisional. The exact N15 hypothesis and the actual-graph interpretation remain explicit mathematical assumptions, and the wider exclusions described above remain open.

User overrides were followed: only Markdown and JSON audit artifacts were written in the requested review directory; no hashes, checksum files, manifests, TeX, PDF or HTML were generated. Papers, formal files and wiki were left untouched by this reviewer.
