# HS58: saturated disjoint deletions for every addition count

Date: 2026-10-12. Pure combinatorial result; no new enumeration,
solver, or auxiliary catalog is used. Let Q be HS50, let D={xy,zw}
be two disjoint original edges, and extend Q-D by eight new vertices
and a original-nonedge additions A to an eight-regular diameter-two
graph. Assume all four vertices P={x,y,z,w} have their maximal two
new neighbors. Then:

* if the deleted edges have an original cross edge, a<=5;
* if they have no original cross edge, a<=6.

In the second case equality leaves exactly four possible zero-port
sets and 56 possible labeled addition matchings after the established
normalization of D. These are necessary templates, not successful
complete graphs. In particular no saturated disjoint-D candidate can
have a>=7. Combining the first item with the existing exclusion of
all a<=5 also excludes every saturated cross-D extension.

## The zero-set argument is independent of a

For an old vertex t let p_t be its number of new neighbors and a_t
its addition degree. Degree eight gives p_t+a_t=1+d_D(t). Saturation
of P therefore makes A avoid P. Outside P, a_t<=1, so A is a matching
of size a, with zero-port endpoint set Z of size 2a. Every old vertex
outside P union Z has one port. Put tau=(x y)(z w), and for q in Z
write q' for its A partner and S(q)=N_Q(q) intersect P.

Vertex q has its seven Q neighbors and the zero-port neighbor q'.
Unless S(q) is nonempty, these supply at most seven new labels,
contrary to diameter two. By triangle-freeness S(q) contains at most
one end of each deleted edge, and hence has size one or two.

If t lies in S(q), the unique original two-step route from q to
tau(t) was q-t-tau(t), now broken by D. There is no new intermediary
because q has no port. Vertex tau(t) has no addition, whereas q's
only addition is qq'. Thus its replacement old path must be
q-q'-tau(t). Applying this also to q' proves

\[
S(q')=\tau(S(q)).                                      \tag{1}
\]

When |S(q)|=1, its seven Q neighbors carry at most 2+6=8 ports.
Any other zero among them would reduce this to seven. Such a q
therefore has no Q neighbor in Z. For two zeros with |S|=2, an edge
between them would make a triangle if their S sets overlap. If their
S sets are disjoint, they contain opposite ends of each deletion,
and that edge makes a four-cycle through a deleted original edge.
Thus Q[Z] is independent. No step has used a=5.

Equation (1) also shows that every A edge pairs tau-opposite cells.
Such pairs are automatically original nonedges: a putative Q edge
qq' would give the four-cycle t-q-q'-tau(t)-t for t in S(q).

## Cross edges: at most ten zeros

Suppose xz is an original cross edge. The two-neighbor cell {x,z}
is empty by triangle-freeness. The cells {x,w} and {y,z} have their
unique common neighbors z and x inside P, so contain no zeros.
Finally a zero in {y,w} would require an A partner in the empty
{x,z} cell. Therefore every q in Z has |S(q)|=1.

Use the complete cross-deletion orbit to normalize D={01,23}.
In the actual coordinates U(i,j)=5i+j, V(k,l)=25+5k+l, indices
are modulo five; U edges have step 1, V edges step 2, and
U(i,j)-V(k,l) is an edge precisely when l=ik+j.
The only possible single-neighbor zeros are V(k,l) with
l in {0,1,2,3}. Indeed old vertex 4 has two P neighbors, the other
U vertices outside P have none, and V(k,l)'s P neighbor is l
when l belongs to that four-set. Each of the five V tracks is C5
and contains at most two independent zeros. Thus 2a=|Z|<=10.
This bound does not use the a=5 equality or its 720-template count.

## No cross edges: four isolated cells and two eight-cycles

Use the complete no-cross orbit to normalize D={01,10-11} and
P={0,1,10,11}. All possible zero vertices lie in
T=N_Q(P) minus P. Its four double-neighbor vertices are

| Vertex | S(vertex) | Forced A partner when selected |
| --- | --- | --- |
| 25 | {0,10} | 26 |
| 26 | {1,11} | 25 |
| 35 | {0,11} | 41 |
| 41 | {1,10} | 35 |

The four singleton cells are

\[
\begin{array}{ll}
T_0=\{4,30,40,45\}, & T_1=\{2,31,36,46\},\\
T_{10}=\{14,32,39,48\}, & T_{11}=\{12,33,42,49\}.
\end{array}
\]

The double-neighbor vertices are isolated in Q[T]. A proposed edge
to a vertex with an overlapping S set makes a triangle. If the S
sets do not overlap, some S neighbor of the latter is the deleted
partner of an S neighbor of the former, making a four-cycle.

Each singleton vertex has degree two in Q[T]. If its P neighbor is
p, it cannot have a T neighbor sharing p (triangle) or adjacent to
tau(p) (four-cycle through p-tau(p)). For each of the two endpoints
of the other deleted edge, the unique common neighbor lies outside
P, lies in T, and is a singleton. These two common neighbors are
distinct, since the other deleted edge has no common neighbor.
They are all its T neighbors. This argument proves the degree claim
without checking an unlisted set of possible edges.

The coordinate edge formula displays the following two disjoint
cycles on all sixteen singleton vertices:

\[
\begin{split}
C&=(4,39,36,12,45,48,46,49),\\
C'&=(2,32,30,33,31,14,40,42).
\end{split}
\]

Every consecutive pair, including the last-first pair, is a Q edge.
Since every listed vertex already has its two T neighbors in these
cycles, there are no further induced edges. Therefore

\[
Q[T]=4K_1\;\dot\cup\;C_8\;\dot\cup\;C_8,
\qquad |Z|\le4+4+4=12.
\]

This proves a<=6 using only the explicit twenty-vertex induced
subgraph and the all-a independent-zero lemma.

## Equality gives 56 complete addition matchings

If a=6, equality requires all four double vertices, together with
one alternating half of each C8. The two halves of C are

\[
C_L=\{4,36,45,46\},\qquad C_R=\{39,12,48,49\},
\]

and those of C' are

\[
C'_L=\{2,30,31,40\},\qquad C'_R=\{32,33,14,42\}.
\]

Each L half contains two vertices from each of T0,T1; each R half
contains two from each of T10,T11. Thus all four independent choices
already satisfy the necessary singleton cell balances. The two
double-cell additions are forced to be 25-26 and 35-41. The remaining
four additions are arbitrary bijections between the selected T0/T1
vertices and between the selected T10/T11 vertices.

If k of the two cycles choose their L half, these cell sizes are
2k,2k and 4-2k,4-2k. Thus the numbers of addition matchings are
24 for k=0, 4 for each of the two k=1 zero sets, and 24 for k=2:
56 in total. By the original-nonedge argument following (1), each
is indeed a six-edge matching of original nonedges. This defines
the finite necessary addition domain without enumerating it.
Port assignment, auxiliary H, and all other pair coverage still
have to hold simultaneously. No impossibility or existence is
asserted for these a=6 templates here.

The normalizations used above are justified by the saved explicit
automorphism orbits in `HS58_REMAINING_DELETION_ORBITS.md` and
`HS58_A5_NO_CROSS_DELETIONS_EXCLUSION.md`. Their orbit statements
depend only on Q and D, not on the number of additions.
