# Independent ARIS review: exact ordinary mixed-omission classification

**PASS**, modulo the explicit generic matching-connectivity rank theorem.
For H={0,1,3,31}, U={0,31}, and the specified seven-edge matching R,
EVERY arbitrary complete-graph perfect matching F on K=Q5 minus H extends
to an ordinary simple30-cycle on Q5 minus U by adding only short edges
**if and only if R is not a subset of F**. No additional edge3-7 or
other opening edge is prescribed or guaranteed.

Reviewer `/root/higher_q5_nearbalanced_review`, user-directed GPT-6.1-sol /
high, independently checks the root producer's new mechanism under ARIS
proof-checker. Review independence is same-family; acceptance is provisional.
No producer proof, certificate or production state was changed. This local
theorem accepts NO actual Q6 application and makes NO decrement to the235
remaining covered-target geometries. Full twelve-hole and P6 remain OPEN.

The reviewed proof SHA256 is
`ab1efb5e28860e0407ed54c99e4a8d607b29b999cb3be4cb209264c55887aa34`.
All13 manifest-bound file hashes match and are rechecked after computation.
The independent verifier checks exact certificate record lengths as well as
all physical forests, pairings, columns, matrix bits and rectangular rank.

## Exact objects, imported ranks and quantified statement

R consists of the disjoint short pairs
{4-6,8-10,13-15,16-18,21-23,25-27,28-30}, all with endpoints in K.
Let B denote ALL perfect matching columns G on K containing every R edge.
Let L=K minus V(R); |K|=28 and |L|=14. Every G in B is exactly R union G'
for an arbitrary perfect matching G' of L. Required edges of F,G and
auxiliary row matchings may be long or same-parity.

H_K is the binary matching-connectivity matrix indexed by every perfect
matching of the complete graph on K. Its entry is1 exactly for a single
connected alternating union, retaining the two matching labels. A common
pair is a labelled two-edge component. V is its complete row space;
rho:V -> GF(2)^B restricts coordinates to B; E=ker(rho). This definition
keeps the kernel inside the actual row space, not an unrestricted ambient
coordinate kernel or a count of sampled bad columns.

The [primary accepted manuscript of Cygan--Kratsch--Nederlof](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf)
was directly inspected in this independent audit series. Its abstract
defines the matrix on all complete-graph perfect matchings, and
Theorem3.4/Corollary3.5 on PDF page9 give rank_GF2(H_t)=2^(t/2-1) for
every even t>=2. Thus dim(V)=8192 and rank(H_L)=64. No bipartite
restriction, smaller-case extrapolation or related half-layer theorem
is imported. The cited Gregor--Novotny--Skrekovski result is motivation
only and is not a premise of this proof.

## Mathematical obligation ledger

| ID | Obligation and discharge |
|---|---|
| M01 | Necessity uses the cut A={x:x&2=0}. Its odd half-layer is EXACTLY R plus1-3; none of these eight edges meets omitted0,31. For any candidate cycle C, S=C minus F has degree1 at K, degree2 at included holes1,3 and degree0 at U, with all S edges short. In A, retained odd total S-degree is9 and even total is7. Internal short edges cancel, so odd-A/even-B crossings minus even-A/odd-B crossings equals2. If F contains R, none of those seven physical edges is in S and only1-3 remains in the odd half-layer; at most1 crossing cannot meet the required difference2. This proves necessity for arbitrary F without a bipartite assumption. |
| M02 | For any complete row matching P, P+R has degree2 on V(R), degree1 on L, and components are alternating paths/cycles. A shared P/R pair is a labelled two-edge cycle. Any cycle lies wholly in V(R), persists after adding arbitrary G' on L, and is a proper component because L is nonempty. Such a restricted row is identically zero. |
| M03 | If P+R has no cycle, its paths have endpoint set exactly L. Compress them to a perfect matching P' of L. For every G', P+(R union G') is connected iff P'+G' is connected. Hence every nonzero restricted row is a row of H_L, giving rank(rho(V))<=64. This covers ALL complete row matchings P and ALL bad columns, not only supplied finite rows/columns. |
| M04 | Conversely let any perfect matching P' of L be given and choose any one edge a-b of it. Order/orient the seven disjoint R pairs (r_i,s_i). Replace a-b by the alternating path a-r1-s1-r2-s2-...-r7-s7-b, putting its eight intervening links in P and keeping all six other P' edges. Each K vertex occurs in exactly one P edge; P is a valid complete-graph matching, with no shortness/parity constraint. P+R compresses exactly to P'. Therefore every H_L row occurs as a restricted row, so rank(rho(V))=64 exactly. |
| M05 | Rank-nullity on the finite-dimensional V now gives dim(E)=8192-64=8128. The required restriction image is the span of restricted complete rows, which is exactly the row space of the restricted matrix. No independence or maximality of the producer's search is assumed. |
| M06 | Every certified S has16 distinct short edges, omitted degree0, covered degree1 on28 terminals and degree2 at included1,3; DSU rejects cycles. Thus it has14 vertex-disjoint paths on all30 retained vertices, with full endpoint pairing P_S on K. All supplied pairings are independently reconstructed. |
| M07 | Every such short degree pattern satisfies the same half-layer difference2. Since the odd half-layer has only1-3 outside R, S must physically contain at least one R edge. Its two endpoints are covered and have degree1, so this edge is a length-one forest component and an endpoint pair of P_S. Every G in B shares this pair, making H_K[P_S,G]=0. Thus each selected COMPLETE row lies in E directly. This independently strengthens the proof's necessity-based kernel-membership justification and avoids assuming any searched bad-column exhaustion. |
| M08 | The supplied8128-by8192 restriction has independently recomputed row rank8128. Therefore the8128 selected complete rows are independent. They lie in E and their number equals dim(E), so they are a basis of E. The8192 supplied columns need only be valid arbitrary matchings; they need not enumerate all columns or form an assumed standard basis. |
| M09 | Let F fail to contain R and choose e=pq in R minus F. Its endpoints belong to distinct F pairs, say(a,p),(q,b), with all four vertices distinct. Put these two oriented F edges consecutively in a cyclic ordering of all fourteen F edges and join each end to the next start. This defines a perfect matching P containing pq, with P+F one alternating28-cycle. P may be an arbitrary long/same-parity matching, which is legal as a row of H_K. It is a separating row, not itself claimed to be a short forest solution. |
| M10 | Every G in B contains e and therefore shares it with this P, giving a separate labelled two-edge component. Hence H_K[P,G]=0 for ALL G in B and the complete row lies in E, while its F coordinate is1. This proves that evaluation at EVERY F outside B is nonzero on E; no unproved generic separation assertion is needed. |
| M11 | Express the separating row in the selected forest-row basis of E. Its F coordinate is1 over GF(2), so at least one selected forest row has F coordinate1. Expand THAT single forest's endpoint paths to a connected degree2 graph on all30 retained vertices. A shared physical F/S edge would be a length-one forest component and common endpoint pair, creating an isolated labelled two-edge component on28 endpoints; connectedness forbids it. The resulting cycle is simple, contains all F, and adds only short edges. No algebraic combination of forests is physically combined. |
| M12 | M01 supplies necessity and M02-M11 supply sufficiency for exactly the same arbitrary-F domain. A common cube automorphism transports H,U,R,F and the cycle together, preserving required edges and short added edges. The conclusion is an ORDINARY cycle; no chosen opening edge, actual Q6 transfer or residual decrement appears in the quantified theorem. |

The new kernel argument therefore supplies the missing implication that
rank8128 alone would not establish. It identifies the complete bad-column
image analytically, proves every certified row belongs to its kernel, and
constructs an explicit separator for every other matching column. A
deficient finite search without these steps would not imply this iff.

## Independent exhaustive certificate audit

Fresh TWELVE_MIXED_HALF_LAYER_REVIEW_check.cpp does not import/include or
execute the producer search or preparation code. It reads only the exact
frozen forest, pairing, column and matrix data. It validates all labels,
short edges, edge uniqueness, degrees, support, omissions and acyclicity;
reconstructs every endpoint pair; and validates each arbitrary column's
complete28-terminal support without a parity restriction.

It also directly checks oddCross-evenCross=2 in each selected forest and
at least one actual R pair in its endpoint matching. Observed selected R
pair counts range1 through6, which certifies vanishing on every bad column
without enumerating those columns. These min/max values are observations
about the supplied certificate only, not an exhaustive forest theorem.

For every matrix entry the checker contracts fourteen actual row pairs,
adds the actual column edges with DSU and requires thirteen successful
unions for connectedness. Shared pairs remain loops at a contracted
component. Every bit is compared with the frozen little-bit-first matrix.
Fresh increasing-column Gaussian elimination on the RECOMPUTED rectangular
matrix then gives row rank8128. Producer saved pivots/combos are hash-bound
but not used to establish this rank.

| Independent check | Complete result |
|---|---:|
| Legal physical short forests |8128|
| Reconstructed endpoint pairings |8128|
| Valid arbitrary complete matching columns |8192|
| Recomputed connectivity bits |66584576|
| Rectangular dimensions |8128 x8192|
| New GF(2) row rank |8128|
| Selected rows directly annihilating all bad columns |8128|

The checker exits0 and its JSON result is PASS. The13 frozen hashes are
verified before and after the run. Search limits, examined-forest counts,
generator completeness, saved pivot/combo derivations and metadata rank
are not premises of the verdict.

## Counterexample pressure and finite small-model checks

The separate fresh Python math checker independently verifies the exact
seven-edge R plus1-3 half-layer, omitted-vertex disjointness, degree totals
9/7, K/L sizes and config. It then exhausts small complete matching models
at(n,|R|)=(6,1),(8,1),(8,2),(8,3). It checks2040 restriction/compression
entries including shared-pair and leftover-cycle cases, constructs22 lifts
of all small H_L rows, and checks552 explicit separators for every missing
fixed edge. Small restriction ranks are respectively2,4,2,1, matching the
appropriate H_L ranks. These pressure tests support the general derivations
M02-M04/M09-M10; they do not replace them or extrapolate the large ranks.

Adversarial possibilities examined include a hidden cycle in P+R, an
unused R vertex in a purported lift, an extra matching/parity constraint
on separator P, using only an upper bound for the bad restriction, kernel
taken outside V, rows that vanish merely on sampled bad columns, a chosen
missing edge actually in F, a common pair treated as a simple edge,
finite-column/universal-F confusion, and interpreting a GF(2) combination
as a physical union of forests. M01-M12 explicitly exclude these gaps.
No limit, asymptotic, probability or analytic interchange occurs.

Reproduction: compile the reviewer C++ with
D:/mingw64/bin/g++.exe -std=c++17 -O3; run it with this directory as sole
argument, saving stdout to TWELVE_MIXED_HALF_LAYER_REVIEW_check.json.
Run TWELVE_MIXED_HALF_LAYER_REVIEW_math.py using D:/anaconda/python.exe.
Only newly named reviewer artifacts are written.

## Accepted boundary

The exact local ordinary-cycle iff statement passes with zero open
mathematical issues. A usable Q6 opening edge is a SEPARATE obligation.
The reported rank8031 force-edge3-7 probe is not audited as a classification
or a negative certificate here, and ordinary-cycle acceptance cannot
upgrade it. No related bipartite half-layer paper is used as a theorem
input. No actual short-matching realizability assertion or Q6 coverage
count is inferred. The235 existing covered-target geometries remain
unchanged; complete twelve-hole Q6 and full P6 are not proved by this
local package. Semantic assurance remains same-family/provisional relative
to the explicit primary generic rank theorem.
