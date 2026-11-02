# Shared-slope affine matchings on the 124- and 172-vertex bases

## Target and conclusion

**For either of the two fixed loop-free bases below, a diameter-three
affine lift with one common slope per endpoint class must have flat
cycle slopes.** After an affine relabeling inside each vertex orbit,
all edge slopes are one. Thus this proposed enlargement supplies no
diameter-three graph outside the original additive-voltage family.

The two bases, with cross multiplicities ordered 01,02,03,12,13,23, are:

- q=31, multiplicities (2,2,2,2,2,2), degree six, order 124;
- q=43, multiplicities (3,2,2,2,2,3), degree seven, order 172.

This does not exclude diameter-three graphs in the original flat
families, arbitrary graphs of these orders, other base multiplicities,
or bases with loops. It is not a new graph lower bound.

Status: **COHERENT AS STATED**. The proof below is self-contained. A
small complete multiplier calculation and exact symbolic affine
composition agree with its classification. No translation assignment,
lifted graph, or BFS was evaluated.

## 1. Model, simplicity, and gauge

There are four vertex classes indexed by i, each with coordinates
x in Fq. Every edge e in the endpoint class i,j has affine map

    f_e(x) = a_ij*x+b_e,   a_ij != 0.

The reverse edge has map x -> a_ij^(-1)*x-a_ij^(-1)*b_e. All parallel
edges share a_ij and have distinct b_e. This is precisely the condition
that the corresponding affine matchings be disjoint: unequal slopes
would intersect at one input x, whereas equal slopes and unequal
intercepts never do. There are no internal edges in this note.

Relabel each class by x'=s_i*x+t_i, with s_i nonzero. Then

    a'_ij = s_j*a_ij/s_i,
    b'_e = s_j*b_e+t_j-a'_ij*t_i.

On a three-class spanning tree, choose one edge from each class and
successively set its slope to one and intercept to zero. This preserves
simplicity and the degree. Use tree classes 01,02,03. The remaining
three slopes are

    u=a12, v=a13, w=a23,

with reverse slopes their inverses. Flat means u=v=w=1; then all six
endpoint classes have slope one. The remaining intercept dimensions
are nine at q31 and eleven at q43.

## 2. Exact line-cover reformulation

A directed base walk P composes to an affine map

    f_P(x)=A_P*x+B_P.

If an edge map (a,b) is appended, the update is

    (A,B) -> (a*A, a*B+b).

For fixed class endpoints i,j, associate to every walk of length at
most three the line y=A_P*x+B_P in Fq^2. Include the empty walk when
i=j. An immediate edge reversal composes to the identity, so deleting
it preserves the endpoint pair and total map; reduced walks suffice.

For a fixed legal assignment, **all q^2 ordered pairs from classes i
and j have distance at most three exactly when these lines cover all
of Fq^2**. Taking this condition for all sixteen class pairs is exactly
diameter at most three. On the diagonal, x=y is correctly covered by
the empty walk.

Without a separate symmetry proof, four source vertices no longer
verify this property: nonflat slopes generally destroy simultaneous
additive translation. The line-cover condition imposes all x at once.

All line counts below refer to distinct maps or an explicit upper
bound on them. Duplicate walks do not count as extra coverage.

## 3. A basic missing-parallel-line lemma

Fix a slope A. If a line y=A*x+c is absent from a proposed cover, no
other line of slope A meets it, while every line of another slope
meets it at exactly one point. Thus at least q lines of other slopes
are necessary to cover this missing line.

Consequently, if fewer than q available lines have slope different
from A, covering the plane forces **all q intercepts in direction A**.
This is a direct intersection count, not a conjectured general
2q-r lower bound.

In particular, two incomplete parallel classes cannot cover the
plane: a missing line from each class meets at an uncovered point.

## 4. At most five slopes in an off-diagonal slot

Fix distinct i,j and let h,k be the two other vertices. All paths of
length at most three have one of these five slopes:

    a_ij,
    a_ih*a_hj, a_ik*a_kj,
    a_ih*a_hk*a_kj, a_ik*a_kh*a_hj.

The first class contains the direct edge and every length-three
excursion that revisits i or j. The other four classes are the two
length-two paths and the two Hamiltonian length-three paths. Coincident
values among these five slopes must be merged, never treated as
different directions.

Write n=m_ij. The first group's intercept-form capacity is

    D_ij = n + n^2*(n-1)/2
           + n*sum_{z=h,k} [m_iz*(m_iz-1)+m_jz*(m_jz-1)].

For justification, paths using only the i,j class give
n+n*(n-1)+n*C(n-1,2) distinct intercept forms: the single edges,
2*b_e-b_f, and b_e+b_g-b_f with distinct e,g and f outside them.
The affine three-step composition here is
f_g f_f^(-1) f_e(x)=a_ij*x+b_e-b_f+b_g, so this merger is valid at
every slope. Each excursion through another vertex contributes the
last term. This is an upper bound even if a later actual intercept
assignment creates more coincidences.

The other four path groups have respective capacities

    m_ih*m_hj, m_ik*m_kj,
    m_ih*m_hk*m_kj, m_ik*m_kh*m_hj.

For the two bases these numbers are:

| Base / endpoint multiplicity | Direct group | Two-step groups | Hamiltonian groups | Maximum outside direct group |
|---|---:|---|---|---:|
| q31, m_ij=2 | 20 | 4,4 | 8,8 | 24 |
| q43, m_ij=3 | 36 | 4,4 | 12,12 | 32 |
| q43, m_ij=2 | 36 | 6,6 | 18,8 | 38 |

All final-column numbers are strictly less than q. Therefore every
off-diagonal plane cover must contain a **complete parallel class in
the direct slope a_ij**. Other-slope routes cannot repair a missing
line in that direction.

This gives a cheap necessary condition before any intercept search:
add to D_ij just the capacities of the four other path groups whose
slope actually equals a_ij; that sum must be at least q. The resulting
capacity is 44 for flat q31, and 68/74 for flat q43.

## 5. Complete cycle-slope classification

Call a base cycle flat when its oriented product of slopes is one.
An indirect path has the direct-edge slope exactly when it closes
with the inverse direct edge to a flat cycle. The two length-two
paths correspond to adjacent triangles and the two Hamiltonian paths
to the two Hamiltonian four-cycles containing that edge.

### q43

The direct group has capacity 36, so at least seven additional forms
are necessary. One flat Hamiltonian cycle suffices for this capacity
condition. Without one, both adjacent triangles must be flat: one
triangle contributes only four or six forms, while both contribute
eight or twelve. Thus every edge must belong to a flat Hamiltonian
cycle or have both its adjacent triangles flat.

There must be at least two flat Hamiltonian cycles. If none is flat,
the edge conditions force all triangles flat. If exactly one is flat,
its two omitted opposite edges force their four adjacent triangles
flat, again making every cycle flat. Both alternatives contradict
the assumed number of flat Hamiltonian cycles.

In the tree gauge the three Hamiltonian cycle conditions are

    u*w=1,   v=w,   v=u.

At least two hold exactly in the union

    (u,v,w)=(t,t,t), (t,t,t^(-1)), (t,t^(-1),t^(-1)),
    t in F43^*.

Conversely, any two flat Hamiltonian cycles cover all six base edges,
so every displayed triple satisfies the direct-direction capacity
condition. The three families meet only at t=1 and t=-1. Their union
has 3*42-4=122 triples: one flat, one all-minus, and 120 others.

### q31

Here D_ij=20 and at least eleven additional forms are necessary.
The two adjacent triangles together give only eight, so every edge
must belong to a flat Hamiltonian cycle. At least two of the three
Hamiltonian cycles must consequently be flat, giving the same three
families above.

If t is neither 1 nor -1, exactly two Hamiltonian cycles are flat,
and all triangle products are t or t^(-1), never one. An edge lying
in only one flat Hamiltonian cycle then has direct-direction capacity
20+8=28<31. Thus only

    (u,v,w)=(1,1,1) or (-1,-1,-1)

survive this off-diagonal condition. At -1 the count is 36; at 1 it
is 44.

## 6. The all-minus case fails in both fields

The all-minus tree-gauge triple is equivalent, by scaling individual
vertex classes, to putting slope -1 on all six classes. It is not
flat. A walk has slope -1 or +1 according as its length is odd or even.

In a self-slot, the empty walk and two-step returns give at most
seven translation lines at q31, or eleven at q43. Three-step closed
walks are triangles. The affine inverse of a reflection
x -> -x+b is that same reflection. Consequently a triangle walk and
its reversed walk give the same map, not two different forms.

There are 48 directed triangle walks at q31, so there are at most
24 reflection lines. At q43 there are 72, so there are at most 36.
Both self-slots are therefore unions of two incomplete parallel
classes: (7,24) at q31 and (11,36) at q43. By the missing-line lemma,
neither can cover Fq^2. This excludes the all-minus triple.

This forced reverse-walk identification is essential: retaining all
48 or 72 directed words as different reflection lines would give
an incorrect capacity conclusion.

## 7. The remaining q43 triples fail in the self-slots

Take one of the 120 triples with t not in {1,-1}. Every triangle
holonomy is t or t^(-1). Every root has three unoriented triangles,
each with twelve choices of its matching edges. Reversal swaps the
two slopes. The self-slot therefore has only the three directions

    1, t, t^(-1),

with at most 11,36,36 lines respectively. The symbolic calculation
below confirms these exact form counts at every root for every such
triple; actual intercept coincidences can only lower them.

Choose seven missing lines of slope t, with intercept set A, and
seven missing lines of slope t^(-1), with intercept set B. Such sets
exist because 43-36=7. The intersection of

    y=t*x+a,   y=t^(-1)*x+b

has translation-line intercept

    y-x = (a+t*b)/(t+1) = alpha*a+beta*b,
    alpha=1/(t+1), beta=t/(t+1).

Both alpha and beta are nonzero. At this intersection neither of
the chosen directions supplies a covering line. Thus a cover would
require alpha*A+beta*B to be contained in the at most eleven available
translation intercepts.

The following self-contained interpolation argument rules this out.

### Seven-by-seven sumset lemma over F43

If A,B each have seven elements and alpha,beta are nonzero, then
|alpha*A+beta*B| is at least thirteen.

Suppose instead that it has at most twelve elements and extend it
to a set C of exactly twelve field elements. Put

    P(X,Y)=product_{c in C}(alpha*X+beta*Y-c).

This polynomial has total degree twelve and vanishes on A x B. For
D_A(a)=product_{a' in A, a' != a}(a-a'), and D_B analogously, the
coefficient identity is

    [X^6 Y^6]P = sum_{a in A,b in B} P(a,b)/(D_A(a)*D_B(b)).

To prove the identity, apply the one-variable Lagrange leading-
coefficient functional. It sends X^k to zero for k<6 and to one for
k=6. On a monomial X^i Y^j of total degree at most twelve, either one
exponent is below six and annihilates the product functional, or both
are six. If an exponent exceeds six, the other must be below six.
This proves the displayed identity term by term, without requiring
each separate variable degree to be at most six.

The right side is zero because P vanishes on the grid. The left side
is C(12,6)*alpha^6*beta^6, and C(12,6)=924=21 mod43 is nonzero. This is
a contradiction. The lemma is proved.

Applying it to the missing-line sets gives at least thirteen required
translation intercepts, exceeding eleven. Hence no nonflat q43
survivor can cover even a self-slot. This proof uses no unverified
general line-cover bound and needs no external theorem citation.

## 8. Finite symbolic calculation and scope

Two formulations of the same necessary calculation were used:

1. `slope_capacity.py` enumerated the 30^3=27000 slope triples at q31
   and the 42^3=74088 triples at q43, using the explicit path-type
   capacities from Section 4. It retained 2 and 122 triples, agreeing
   with Section 5. CPU: 1.253539828 seconds total.
2. `check_survivor_forms.py` propagated the actual affine pair (A,B),
   with B a coefficient vector in all twelve or fourteen formal
   intercept variables, through every reduced walk of length <=3.
   Reverse edges used (a^(-1),-a^(-1)*b). It deduplicated by the full
   pair (A,B), not by words or B alone. The checks covered all 124
   retained triples and all four roots. CPU: 0.332436774 seconds.

The second calculation checked that every off-diagonal direct-slope
count matched the path-type formula; that every self-slot had exactly
the counts in Sections 6 and 7; and that deleting the three chosen
tree-intercept coordinates preserved equality counts within each
fixed endpoint and fixed slope. Full data are in
`SLOPE_CAPACITY.json` and `SURVIVOR_FORM_CHECK.json`.

The measured calculation CPU was **1.585976602 seconds**, far below
the 60 CPU-second allocation. There were **zero intercept assignments,
zero generated graphs, and zero BFS roots**. No old search was rerun.

## Consequence for construction work

For these two fixed bases, do not start a generic nonflat shared-class-
slope search: the diameter-three line-cover conditions force the three
cycle slopes to one. Any D3 graph in this affine class is fiberwise
affinely isomorphic to a graph in the existing additive Cq family.

This closes only the proposed affine enlargement. It neither upgrades
the observed local minima into exhaustive additive-family exclusions
nor says that a different base or a different matching rule cannot
work. No claim node, wiki page, external review, or graph record was
created by this task.
