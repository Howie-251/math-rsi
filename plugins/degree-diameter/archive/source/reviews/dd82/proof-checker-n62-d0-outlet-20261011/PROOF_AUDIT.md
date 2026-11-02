# Fresh proof audit: D0 components and the D1 outlet

**Verdict: PASS.** All 32 recorded proof obligations are discharged at paper
level. No FATAL, CRITICAL, MAJOR, or MINOR proof issue was found. This is a
same-family review with provisional acceptance; the requested
`gpt-6-astra` / `ultra` backend configuration was not independently attested.

The target is `proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`.
The reviewer is the fresh agent `/root/proof_review_n62_d0_outlet`, invoked
by `/root`. The source proof and shared wiki were not edited. The user's
Markdown/JSON-only and no-hash requirements override the skill's default
TeX, HTML, and digest outputs.

## Scope of the result

For an actual finite simple undirected order-62 graph with maximum degree
eight and diameter at most two, each D0_MATCH root forces a closed weighted
four-cycle of the actual repeat matrix, with alternating weights 2,1,2,1;
the four points are independent in G. Each D0_EDGE_BOUT root forces the same
repeat component, with exactly the two opposite G edges 0b and wa.

Combined with the recovered triple-repeat exclusion, triangle pairing,
and the D2 and BIN exclusions, these local conclusions imply that some root
of every candidate realizes D1_MATCH. The global claim retains the explicit
finite enumeration in the triple-repeat exclusion. It neither contradicts
D1_MATCH nor establishes nonexistence of order-62 graphs.

## Review procedure and original assumptions

The complete target was checked from its actual G premises. Dependency
proofs were read directly; prior review verdicts were not used as proof
premises. The audit checked definitions, every nontrivial lemma application,
all inequality directions, endpoint coincidences, root relabeling, and the
dependency graph. Interchange, stochastic-mode, and asymptotic-uniformity
checks are inapplicable because this is finite exact graph mathematics.

If any vertex had degree at most seven, its radius-two ball would have at
most 1+7+7·7=57 vertices. Therefore G is 8-regular. For the actual matrix
B=A²+A−7I−J, this gives diagonal zero, row sum 64+8−7−62=3, and commutation
with A. Diameter two makes the off-diagonal entries nonnegative; symmetry
and integrality are immediate. The point-pair identity is
c(x,y)+A_xy=1+B_xy for x≠y. Summing along original edges gives
2t(x)=Σ_{y~x}B_xy≤3. Hence t(x)≤1, and every adjacent repeat entry is at
most one. These establish the original hypotheses used throughout.

## Local D0 deductions

The common-neighbor counts between vertices of X are exact, not lower
bounds: X is independent, and only exceptional parent sets can supply a
second common neighbor besides 0. For i∈S={1,2,3}, the other points j,k∈S
give B_ij=B_ik=1; all other X entries and B_i0 vanish. Thus the remaining
unit endpoint c_i really lies in Y. Both ends of a double repeat are
triangle-free: their nonadjacent weight-two entry leaves at most one unit
of incident-edge budget, whereas this budget equals the even number 2t.

In D0_MATCH, w has five ordinary Y neighbors, with no parent in S.
Diameter two requires every one of the other five X labels to occur once,
so B_wx=0 on X and B_w=2e₀+e_b with b∈Y. If b=a, the (i,a) entry of AB
is at least two while BA is at most one; hence b≠a. The same entry now
forces a~c_i. At (c_i,w), AB=A_{c_i b} while BA is at least
Σ_{h∈S}B_{c_i h}≥1. This proves b~c_i and bounds that sum by one. It also
proves the c_i are distinct. Three distinct common neighbors give
B_ab≥2+A_ab. Row a already contains B_a0=1, so A_ab=0 and B_ab=2.
Symmetry exhausts row b as well. This derives all four complete rows.

In D0_EDGE_BOUT, the actual residual endpoint b belongs to
X\(S∪P(a)). At (i,w), AB=2 and BA=2+A_{c_i w}, forcing c_i not adjacent
to w. At (0,c_i), AB≥1 and BA=A_{a c_i}, forcing a~c_i and c_i≠a.
The known row of w excludes c_i=w. At (c_i,w), commutation then forces
b~c_i, so c_i is an ordinary point of C_b. Returning to (0,c_i) gives
Σ_{x∈X}B_{x c_i}=1; hence the three c_i are distinct. Since b∉P(a),
a,b are nonadjacent. The same three-common-neighbor and row-budget
argument gives B_ab=2 and the remaining complete rows.

In each branch the four vertices are distinct. The displayed positive
cycle is connected, and all four entire rows are exhausted, so it is a
connected component of the support of B. In MATCH the six possible G
edges are absent: 0 avoids Y, w avoids a by the branch, w avoids b by
triangle-freeness and B_wb>0, and a avoids b by the row-budget calculation.
In BOUT the two edges 0b and wa are prescribed; the other four pairs are
nonedges by parent locations. These conclusions do not require the global
triple-repeat exclusion.

## Global parity and arbitrary-root coverage

After triple-repeat exclusion, each positive repeat entry is one or two.
Let d count unordered weight-two edges. The total unordered repeat weight
is 93, so there are 93−2d unit edges. Exactly 3T unit edges are original G
edges, because every triangle edge has repeat one and every adjacent
positive repeat lies on a triangle. Nonadjacent unit edges have two common
neighbors; double edges have three; all other pairs contribute zero to
choose(c(x,y),2). Thus

    2 C₄ = Σ_{unordered {x,y}} choose(c(x,y),2)
         = (93−2d−3T) + 3d = 93+d−3T.

Four-cycles here need not be induced. Every four-cycle has precisely two
opposite pairs even if G has chords. Triangle pairing makes T even,
including T=0. Therefore d is odd and positive. The separate simple-B
exclusion is not needed again after this calculation.

The root-coverage application is valid for *each chosen double edge*,
not merely for an unspecified representative. Choose either endpoint as
0 and the other as w. Both are triangle-free, so X is independent.
The root parent excess is three. The chosen mate uses two units through
|P(w)|=3, leaving exactly one point a with |P(a)|=2; all other parent sets
are singletons. The intersection sizes |P(a)∩P(w)| are 0,1,2. A positive
intersection prevents w~a, because it would create a triangle through w.
The latter two cases are exactly D1_MATCH and D2_MATCH. In the disjoint
case, nonadjacency gives D0_MATCH. Under adjacency, the five Y neighbors
of w provide six parent incidences over the five outside labels. Each
label must occur, so precisely one label b occurs twice. It is w's
additional unit repeat endpoint. The two label orbits b∈P(a) and b∉P(a)
are exactly BIN and BOUT. Permuting labels is a relabeling of G and
requires no automorphism of G.

If no D1 root exists, D2 and BIN exclusions therefore leave one of the two
D0 cases for every chosen double edge. The local results place it in a
closed connected component with exactly two double edges. Two such
components cannot partially overlap: connected components of one support
graph that share a vertex coincide, and all four rows exclude any outgoing
positive edge. Hence all d double edges split into pairs, making d even.
This contradicts its odd parity and proves the D1 existence statement.

## Dependency applicability checks

- **S_TOUCH and triangle pairing:** The mate-touching situation in the
  pairing proof creates exactly one double-parent point relative to a
  triangle root. The three saturated rows in the S_TOUCH proof follow from
  nonnegative integer row sum three, with no use of a global bound B≤1.
  The pairing proof explicitly discharges this distinction before applying
  the contradiction. Distinct repeat mates, their separation from the
  triangle neighborhood, and commutation then force a mate triangle. Its
  saturated rows return the original triangle, giving a fixed-point-free
  involution. No triple-repeat exclusion is used there.
- **D2:** The recovered intersection-two case supplies precisely the
  independent X, parent sets 123 and 12, and ordinary singleton classes
  used in the D2 paper. Its row-saturation, perfect matching between C₁
  and C₂, and final AB≥1 versus BA=0 contradiction use actual graph data.
  There is no import of the D0 closure or D1 outlet.
- **BIN:** The disjoint-adjacent inside orbit supplies exactly b∈{4,5},
  B_w=2e₀+e_b, and a~b. The BIN contradiction produces a~c and b~c, then
  obtains the extra positive term at (0,c). BOUT lacks a~b and is correctly
  left to the component argument.
- **Triple repeats:** The recovered proof derives its five cells and
  finite matrices from the actual G. Nonnegative row sum three and
  commutation isolate the cells. The original graph equations force the
  lifted L blocks, the Q label marginals, and the D Gram matrix. No positive
  semidefinite condition or independent matrix realizability is silently
  assumed. The filters used are necessary conditions, so rejection is
  sound. The final paper parity argument includes the required proof that
  the six named permutation types occur once each in any resolution.

## Exact finite-check receipt

The complete 380-line source
`context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_triple_edge_elimination.py`
was inspected and executed once with Python 3. It exited with status 0 in
3.408 seconds of command wall time. This is a small exact enumeration,
not a SAT call. Its branch search lists all possible local Q rows,
filters only symmetry violations, then checks commutation exactly.
The eight canonical lift choices represent all copy gauges.

| Lift bits | Commuting Q count | Elementary Gram survivors |
|---|---:|---:|
| 000 | 13 | 0 |
| 001 | 5 | 0 |
| 010 | 5 | 0 |
| 011 | 1 | 0 |
| 100 | 5 | 0 |
| 101 | 1 | 0 |
| 110 | 1 | 0 |
| 111 | 1 | 1 |

The unique survivor has 24 candidate D-row supports; every V vertex
belongs to four supports; there are zero six-block resolutions.
The explicit GF(2) equations were verified to sum to 0=1. The recovered
paper also independently justifies the multiplicity premise needed to
interpret one copy bit per named permutation. This closes the imported
finite check at its stated paper/computation scope, without promoting it
to a Lean-certified theorem.

## Counterexample and boundary pass

| Attempt | Result |
|---|---|
| Let MATCH's b equal a | Ruled out by (AB)_ia≥2>(BA)_ia. |
| Let some c_i equal a, w, or b | a would force a loop after a~c_i; w contradicts B_wi=0; b would force a loop after b~c_i. |
| Identify c_i and c_j for i≠j | MATCH gives two units in a sum ≤1; BOUT gives two units in a sum equal to 1. |
| Add G edge ab in MATCH | Then B_ab≥3, contradicting B_a0=1 and row sum 3. |
| Add an outgoing repeat to a claimed component | Every displayed row already has weight 3; nonnegative entries forbid it. |
| Let two claimed components overlap only partially | Their connected support and exhausted rows force them to coincide. |
| Take T=0 | T remains even and the global count still forces d odd. |
| Take d=0 after excluding triples | The same parity count contradicts even T; no separate existence assumption is introduced. |
| Allow weight-three repeats in the parity calculation | The simplified count would no longer be justified. The target explicitly excludes these first; the dependency is retained and was checked. |
| Root at the other endpoint of a double edge | The parent-excess and triangle-free argument applies unchanged; coverage is universal in the choice. |
| Have adjacent exceptional points with a shared parent | This creates a triangle at w and is impossible; there is no missing D1_EDGE or D2_EDGE case. |
| Apply the result to an arbitrary commuting weighted graph B | Not allowed: the actual identity with A and exact parent counts are required throughout. |

No verified counterexample or surviving counterexample candidate was found.
These checks support the individual derivations; unsuccessful attempts
are not used in place of those derivations.

## Closure and remaining research

All three target conclusions match their quantified statements. There are
zero open obligations and no circular dependency. No assumption has been
strengthened, no source fix is required, and no independent source matrix
has been promoted to an actual graph. The semantic acceptance remains
same-family/provisional. D1_MATCH exclusion and any subsequent arbitrary
order-62 nonexistence result remain outside this audit. The requested
model/effort metadata remain unattested, rather than being reported as an
observed backend fact.
