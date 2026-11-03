# Connected order61 defect: the triple-repeat obligation

## New mechanism, inherited scope, and intended decision

The preceding disconnected-defect mechanism completed its four-round
review and all computations. Its structural theorem is an explicit
import: every arbitrary order61 target has connected actual weighted
defect B. No prior quotient or size computation is reopened here.

This new mechanism asks whether an entry `B_uv=3` is possible in the
same original adjacency/defect pair. A complete exclusion would prove
`B_uv<=2` for every distinct pair in every order61 target, materially
reducing the remaining original-graph domain. A surviving local pattern
must be recorded with all unresolved actual-adjacency interfaces; it is
not a graph construction or evidence of existence. A merely growing
list of local constraints is not an automatic reason to keep extending
the mechanism. At most four substantive same-thread Gemini rounds apply.

Original objects: A is the binary symmetric zero-diagonal adjacency on61
vertices, A1=8*1, and B=A^2+A-7I-J is symmetric nonnegative integral,
zero-diagonal, row4 and connected, with AB=BA. All conclusions below
refer to these same matrices. No binary-defect or CP02 H/no-O hypothesis
is assumed. No CPU search, graph enumeration or solver has run for this
new obligation. A targeted literature check is in progress; no novelty
claim is made.

## Initial deductions checked locally

An entry B_uv=4 would consume both rows and create a closed two-vertex
support component, contradicting connectedness. Thus every entry is at
most3.

For an original adjacency edge uv with lambda common A-neighbors,
B_uv=lambda. Each common neighbor w forms a triangle uvw, so B_uw>=1.
Consequently the B row at u has weight at least2lambda. Thus an A-edge
has B weight at most2. If B_uv=3, u,v are nonadjacent and
`S=N_A(u) intersect N_A(v)` has size4.

Every distinct x,y in S has two common A-neighbors u,v, so B_xy>=1.
If xy were an A-edge within S, the two triangles uxy and vxy would
also give B_xu>=1 and B_xv>=1. The three S-internal positive B entries
already consume3, giving row weight at least5. Therefore S is
A-independent. Its B submatrix has all six edges at least1; any
additional internal weight is a matching, since each S row has only
one unit beyond its three mandatory neighbors.

There are unique residual B-neighbors p,q satisfying
`B e_u=3e_v+e_p`, `B e_v=3e_u+e_q`. At this stage p=q is NOT assumed.
The author is deriving the complete p/q cases directly from AB=BA in
CONNECTED_TRIPLE_REPEAT_LOCAL.md. The result is not yet independently
checked. It must retain every permissible p/q location and cannot drop
an original adjacency completion because a relaxed local design fails.

## A precise conditional signed reduction

If the local analysis proves p=q=w, let f=e_u-e_v. Then Bf=-3f and
Jf=0. The actual identity gives `A^2 f+A f=4f`. Put
`P=N_A(u) minus S`, `Q=N_A(v) minus S` (four vertices each) and
`g=Af=1_P-1_Q`. Hence

`Ag=4f-g`, `Bg=-3g`.

The actual A-invariant span(f,g) has matrix `[[0,4],[1,-1]]` and
characteristic polynomial `x^2+x-4`. This polynomial is not itself a
contradiction. If the local argument also establishes that N_A(u) and
N_A(v) are independent, then Ag implies A[P,Q] is a perfect matching.
Every other vertex outside {u,v} and P,Q has equally many A-neighbors
in P and Q.

Independently of that neighborhood independence, Bg=-3g and row4 force,
for every x in P, internal B weight a, cross-Q weight b and outside
weight c to satisfy `a-b=-3`, `a+b+c=4`; thus `2a+c=1`.
Therefore a=0,c=1,b=3. The same holds for Q. The matrix W=B[P,Q]
has nonnegative integral row and column sums3. Each P/Q vertex has
exactly one unit B edge to the zero set of g; each zero-set vertex
receives equally many of these ports from P and Q.

Under the additional neighborhood-independence conclusion, label the
perfect A-matching as P_i Q_i. Let
`R=V minus ({u,v} union S union P union Q)`, so |R|=47. The zero B
entries inside P show that two P vertices have only u as common
A-neighbor; similarly two Q vertices have only v. Each P_i is adjacent
to u,Q_i and six R vertices, and similarly each Q_j. A zero-set vertex
has equal P/Q neighbor counts and at most one of each. Thus exactly24
distinct R vertices attach to one P and one Q, and23 attach to neither.
The counts C_ij of common R-neighbors are

`C_ij=W_ij+1-delta_ij`, with every row and column sum6.

Also W_ii<=1: each of the C_ii=W_ii vertices in the triangle P_i Q_i r
contributes at least one to the external B budget of P_i, which is1.
These are necessary same-graph interfaces, not sufficient local data.

## Next actual work and stopping scope

Read and check the complete residual-port cases; either obtain a
contradiction for all triples or isolate the remaining realizability
problem with its actual interface variables. The signed reduction can
be applied only after its stated premises are proved. If a finite exact
test becomes useful, specify its full domain, necessary pruning and
scope first, then run one bounded profile rather than an open queue.

Ask Gemini whether this changes the general61 problem rather than
repeating old quotient or fixed-family work, and to identify the smallest
missing mathematical step or a direct executable alternative. Check
relevant primary literature for a theorem whose hypotheses truly cover
degree8, diameter2, defect4. No claim of full order61 exclusion, new graph,
formal proof or original-goal completion is made.
