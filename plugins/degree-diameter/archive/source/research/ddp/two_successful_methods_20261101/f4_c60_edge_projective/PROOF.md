# A3840-vertex20-regular diameter-three graph

## Target and status

The complete literal graph has3840 vertices and38400 edges. Production
verified simplicity, reverse edges and degree20 at every vertex. The full
finite route certificate below proves diameter at most3; Moore(20,2)=401
then proves that the diameter is exactly3. Root-arranged independent graph
validation is separate from this producer certificate.

The source controller is the60-vertex five-port controller literally bound
to Bhakar's author recipe in
`../../more_graphs_20261027/d15_D3_current1620_source/construction.author.json`.
The actual source path relative to the project root is
`research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json`.
Only this controller is inherited. The original F3 matrices and fiber are
not used. This follows the existing affine-line/controller mechanism; it is
not a claim that the general mechanism originated here.

## Field, directions and actual edge rule

Let F=F2[w]/(w²+w+1), encoded0,1,2,3 for0,1,w,w+1. Its addition is XOR;
multiplication reduces the polynomial product modulo w²+w+1. Fix

\[
L_0=(0,0,1),\ L_1=(1,0,0),\ L_2=(1,1,1),\
L_3=(1,w,w+1),\ L_4=(1,w+1,w).
\]

These are the five conic directions infinity,0,1,w,w+1. Any three are
independent. Let C[u][p] be the saved controller permutation table and let
inverse ports be(1,0,3,2,4). Vertices are(u,x) in{0,...,59}×F³, with label
64u+x0+4x1+16x2.

For each dart e=(u,p), v=C[u][p], r=inv(p), PARAMETERS.json contains a
matrix T_e. Insert all edges

\[
(u,x)\sim(v,T_e x+tL_r),\qquad t\in F.
\]

The saved300 matrices satisfy T_reverse=T_e⁻¹ and T_e L_p=L_r. Thus the
reverse formula recovers the same undirected edges. The controller is
simple and5-regular, so the five endpoint fibers are distinct; each
contributes four distinct neighbors. No controller edge is a loop.
Consequently the lifted graph is simple20-regular with3840·20/2=38400
edges, also checked directly during generation.

## How the matrices were constructed

For a conic parameter t in F, use

\[
H_t=\begin{pmatrix}1&0&0\\t&1&0\\0&t&1\end{pmatrix},\qquad
H_\infty=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]

H_p sends L_p to the first coordinate axis. For each undirected controller
edge oriented u<v, a selected2×2 projective map Q on the remaining quotient
coordinates gives

\[
T_{u\to v}=H_r^{-1}\operatorname{diag}(1,Q)H_p.
\]

Assign its actual inverse to v→u. In particular the self-inverse controller
port4 does **not** require a globally self-inverse matrix: opposite ends of
each matching edge use T and T⁻¹. There are150 independent edge choices.
The selector map and PARAMETERS.json bind every one of them literally.

## Nonadjacent and equal controller layers

For a controller word u→a→b→v with ports(p,q,r), the fiber noise vectors
at the final vertex are

\[
T_{b,r}T_{a,q}L_{\operatorname{inv}(p)},\quad
T_{b,r}L_{\operatorname{inv}(q)},\quad L_{\operatorname{inv}(r)}.
\]

Applying the invertible T_{b,r}⁻¹ reduces the rank test to

\[
\det(T_{a,q}L_{\operatorname{inv}(p)},
L_{\operatorname{inv}(q)},L_r)\ne0.
\]

For every one of the3300 ordered nonadjacent/equal controller pairs,
ROUTE_CERTIFICATE.json records a literal nonbacktracking three-word with
this determinant nonzero under the saved matrices. The three noise
coefficients range independently over F, so their image is all F³. The
constant term from any initial source coordinate merely translates it.
Thus all64 targets in that endpoint layer are reached within three steps.
This argument covers every source coordinate, including self-layer pairs.

## Adjacent controller layers

Fix e:u→v with port p and reverse r, and a source x. A backtrack at u through
any i≠p, followed by e, reaches the affine plane

\[
T_ex+\langle L_r,T_eL_i\rangle.
\]

A traversal of e followed by a backtrack at v through any j≠r reaches

\[
T_ex+\langle L_r,L_j\rangle.
\]

All these planes share T_ex+span(L_r). For each of the300 darts, the saved
certificate verifies that their quotient directions exhaust the five
points of PG(1,4). The five planes through a common line cover exactly

\[
4+5(16-4)=64
\]

points, namely the entire target fiber. Additional triangle routes are
allowed but are not needed by this positive certificate.

Together the3300 rank routes and300 adjacent-pencil certificates cover all
3600 ordered controller pairs, and every pair of fiber coordinates.

## Finite synthesis and scope

The SAT model chooses one of48 full-pencil projectivities per undirected
edge, considering all60 elements of PGL(2,4) before this sufficient-domain
filter. It imposes all3300 rank-cover requirements simultaneously. A single
CaDiCaL call returned SAT; every CNF clause, all300 matrix conditions and all
3300 route ranks were independently re-evaluated within the producer before
the graph was written. It is the actual selected matrices and literal route
certificates, not trust in a SAT result alone, that establish the construction.

The result improves the local3750-point20-degree instance by90 vertices.
Current global record status requires a separate public comparison and is
not claimed here. No Lean formalization is claimed. This proof does not
assert that every edge-projectivity choice works, or that previous global
chart impossibility was incorrect: edge dependence is the released condition.
