# C5 quotient obstructions: at least two orbits must be independent

**Theorem.** Let G be a simple graph on sixty vertices, of maximum degree
at most eight and diameter at most two, with an automorphism consisting
of twelve cycles of length five. At least two of its twelve vertex
orbits are independent sets. In particular, no voltage assignment with
quotient matrix M=2I+A(K6,6) produces such a graph.

No vertex-transitivity or normality of the C5 subgroup is assumed. The
theorem excludes the families with zero or exactly one independent
orbit; it does not exclude the entire twelve-orbit C5 domain. The proof
is purely mathematical, with no enumeration, SAT or BFS computation.

The general orbit construction and quotient notation are recorded in
[CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md](CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md).
The necessary quotient calculation is repeated here to make the stronger
scope explicit.

## 1. Quotient defect and the all-internal-cycle reduction

The target graph is eight-regular: a vertex of degree d≤7 could reach at
most 1+d+7d≤57 vertices within distance two. For its adjacency matrix A,
the matrix

\[
 B=A^2+A-7I-J_{60}
\]

has zero diagonal, nonnegative entries and row sum 64+8−7−60=5. The
twelve equal-sized orbits form an equitable partition, because the given
automorphism acts transitively on each orbit. Let M be its degree quotient.
It is symmetric and has row sum eight. The quotient of B is therefore

\[
 D=M^2+M-7I_{12}-5J_{12}\geq0,
 \qquad D\mathbf1=5\mathbf1.
\]

Write r_a=M_aa∈{0,2,4} and q_ab=M_ab for a≠b. The possibilities for
r_a are exactly the invariant simple graphs on a five-cycle orbit: select
neither, one, or both of the undirected steps {±1}, {±2}. If
s_a=Σ_(b≠a) q_ab², then

\[
 D_{aa}=r_a^2+r_a+s_a-12.
\]

The case r_a=4 gives D_aa=8+s_a≥8, contradicting the nonnegative row sum
five. Thus every internal degree is zero or two.

Suppose for contradiction that all twelve internal degrees are two.
Then Σ_(b≠a)q_ab=6. If some q_ab≥2, its row-square sum satisfies s_a≥8,
so D_aa=s_a−6≥2. Meanwhile

\[
 D_{ab}=5q_{ab}+\sum_{c\ne a,b}q_{ac}q_{cb}-5\geq5.
\]

The same row of D would sum to at least seven. Hence every q_ab is zero
or one, and M=2I+Q for a simple six-regular graph Q on twelve vertices.
Now

\[
 D=Q^2+5Q-I_{12}-5J_{12}\geq0.
\]

Every nonadjacent pair in Q consequently has at least five common
neighbours.

Let R be the complement of Q, a five-regular graph on twelve vertices.
For an edge uv of R, the two sets N_R(u)\{v} and N_R(v)\{u} each have
size four in the ten remaining vertices. Thus

\[
 |N_Q(u)\cap N_Q(v)|=2+|N_R(u)\cap N_R(v)|,
\]

and every edge of R has at least three common neighbours.

We show that any such R must be 2K6. Fix u. The induced graph on the
five vertices N_R(u) has minimum degree at least three, so its complement
is a matching. If there is a missing edge xy inside N_R(u), then x is
adjacent to u and exactly three other vertices in N_R(u); it has a unique
fifth neighbour z outside N_R[u]. A matching on five vertices has an
unmatched vertex t, which here differs from x,y. This t is adjacent to
u and all four other vertices in N_R(u), using its entire degree five.
It cannot be adjacent to z, and u cannot be adjacent to z either.
Of x's five neighbours, u and t therefore are not common neighbours of
x,z, while z cannot be its own neighbour. This leaves at most two common
neighbours for the edge xz, a contradiction.

Hence every N_R(u) is K5. Its closed neighbourhood is a saturated K6
component, and the twelve vertices split into two such components.
Therefore R=2K6 and Q=K6,6. We have reduced the entire all-r_a=2 family
to the particular quotient M=2I+A(K6,6).

## 2. Exact voltage obligations for this quotient

Label the six orbits in its two parts A_i and B_j, with 1≤i,j≤6. In
coordinates t∈F5, let their internal steps be a_i,b_j∈{1,2}. Each
cross-part pair has one matching, with voltage X_ij∈F5:

\[
 (A_i,t)\sim(B_j,t+X_{ij}).
\]

For a cross-part pair the only paths of length at most two are its direct
edge and paths using an internal edge at one of the two ends. Its five
possible target shifts are

\[
 X_{ij},\quad X_{ij}\pm a_i,\quad X_{ij}\pm b_j.
\]

They cover F5 exactly when a_i≠b_j. Requiring this for every i,j forces
all a_i to be equal and all b_j to equal the other step. This necessary
condition accounts for all cross-part coverage.

Two different A orbits have no direct edges or two-step route other
than through one of the six B orbits. Thus each difference between two
rows of X must contain every element of F5. It has six entries, so its
multiset consists of F5 once plus one repeated value. The same statement
holds for every difference between two columns, using two B orbits and
the six intermediate A orbits. The repeated value is the sum of the
six entries, since Σ_(t∈F5)t=0.

## 3. Simultaneous row and column normalization

All calculations in this paragraph are in F5. Set r_i=Σ_j X_ij and
define X'_ij=X_ij−r_i. Since 6=1 in F5,

\[
 \sum_j X'_{ij}=r_i-6r_i=0.
\]

Subtracting a constant from a row translates each relevant row
difference and leaves each column difference unchanged. It preserves
the property of containing F5 once plus a repeat. Let c_j=Σ_i X'_ij.
Because every row of X' sums to zero, Σ_j c_j=0. Define Y_ij=X'_ij−c_j.
Then

\[
 \sum_iY_{ij}=c_j-6c_j=0,
 \qquad
 \sum_jY_{ij}=0-\sum_jc_j=0.
\]

This column subtraction preserves every row difference and translates
each column difference. Consequently all row and column differences of
Y still contain F5 once plus a repeat, and their sums are now zero, so
every repeated value is zero.

These transformations are legitimate voltage gauges: independent
translations of the six A coordinates and six B coordinates add
arbitrary constants to rows and columns. Internal steps are unchanged.
The normalization can also be viewed simply as a transformation
preserving the necessary row/column difference conditions; it uses no
unproved existence or symmetry assumption.

## 4. The two Gram matrices force an impossible row sum

Let ζ be a primitive fifth root of unity and form the complex matrix
H_ij=ζ^(Y_ij). Every row has squared norm six. For two different rows,
their exponent differences contain F5 once and an extra zero, giving
inner product Σ_(t∈F5)ζ^t+1=1. The column condition gives the same result
for columns. Thus, writing J for the six-by-six all-ones matrix,

\[
 HH^*=H^*H=5I+J.
\]

Associativity gives (HH*)H=H(H*H), hence JH=HJ. The (i,j) entry of JH is
the j-th column sum of H, while that of HJ is its i-th row sum. Therefore
all row sums and column sums are one complex number s. In particular
H1=s1 and H*1=conjugate(s)1, so

\[
 |s|^2\mathbf1=HH^*\mathbf1=(5I+J)\mathbf1=11\mathbf1.
\]

Take any row of H and let n_t count its entries equal to ζ^t. Then the
five n_t are nonnegative integers with Σn_t=6. Define, with indices
modulo five,

\[
 S=\sum_tn_t^2,\qquad C_1=\sum_tn_tn_{t+1},
 \qquad C_2=\sum_tn_tn_{t+2}.
\]

Its sum satisfies

\[
 11=|s|^2=S+C_1(\zeta+\zeta^{-1})
                 +C_2(\zeta^2+\zeta^{-2}).
\]

Put α=ζ+ζ^−1. Then α is irrational, satisfying α²+α−1=0, and
ζ²+ζ^−2=−1−α. Rationality of the last display forces C1=C2=C, and
11=S−C. On the other hand,

\[
 36=(\sum_tn_t)^2=S+2C_1+2C_2=S+4C.
\]

Thus C=5 and S=16. No five nonnegative integers of sum six have square
sum sixteen. If their maximum is at most two, the square sum is at most
twelve. If their maximum is three, the other entries sum to three and
have square sum 3, 5 or 9, giving a total of 12, 14 or 18. If their
maximum is at least four, the square sum is at least 4²+2=18.
This contradiction excludes every voltage assignment for the quotient.

Combining it with Section 1 proves that the twelve vertex orbits cannot
all have internal degree two. Internal degree four was already
impossible, so at least one orbit has internal degree zero. The following
additional quotient argument excludes exactly one such orbit.

## 5. Exactly one independent orbit is also impossible

Suppose a is the unique orbit with r_a=0 and every other orbit has
internal degree two. For any orbit b with r_b=2, its external row sums
to six and D_bb=Σ_(c≠b)q_bc²−6. If some q_bc≥3, then its square sum is
at least 3²+3=12, so D_bb≥6, impossible. Thus q_bc≤2. Furthermore a
double interface between two r=2 orbits has D_bb≥2 and D_bc≥5, again
contradicting row sum five. Hence any double interface is incident to a,
and all other interfaces have multiplicity zero or one.

The external row of a has sum eight. Write t for its number of double
interfaces; it has 8−2t single interfaces. Then

\[
 D_{aa}=4t+(8-2t)-12=2t-4\geq0,
\]

so t∈{2,3,4}. The number of other orbits not adjacent to a in the
quotient is

\[
 |T|=11-\bigl(t+(8-2t)\bigr)=3+t\geq5.
\]

Choose b with q_ab=2. Its remaining external neighbours are four distinct
orbits joined by unit interfaces; call this set U. Its diagonal defect
is D_bb=2. If c∈U were also adjacent to a, then q_ac≥1 and the exact
quotient expression would give

\[
 D_{ba}\geq1+q_{ac},\qquad D_{bc}\geq2q_{ac}.
\]

The first inequality uses the intermediate orbit c, in addition to the
base contribution (r_b+r_a+1)q_ba−5=1. The second uses the intermediate
orbit a; its base contribution is (2+2+1)·1−5=0. The diagonal and these
two distinct entries in row b would therefore sum to at least

\[
 2+(1+q_{ac})+2q_{ac}\geq6,
\]

a contradiction. Consequently all four members of U lie in T.

Since |T|≥5, select x∈T\U. This x differs from b, is nonadjacent to both
a and b in the quotient, and has internal degree two. For the b,x
entry, the contribution through a is q_ba q_ax=0. Only the four unit
neighbours in U can contribute; both they and x have r=2, so each
interface to x has multiplicity at most one. Therefore

\[
 D_{bx}=\sum_{c\ne b,x}q_{bc}q_{cx}-5\leq4-5<0,
\]

contrary to D≥0. Exactly one independent orbit is impossible. Together
with Sections 1–4, this proves the stated lower bound of two independent
orbits. No case with two or more independent orbits is excluded here.
