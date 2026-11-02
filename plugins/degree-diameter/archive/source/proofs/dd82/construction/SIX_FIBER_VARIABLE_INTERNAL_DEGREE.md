# Nonuniform internal degrees in an equitable six-by-ten partition

Current boundary: later proofs exclude all 98 saved matrices, including
the final 24 by the local hub obstruction (C14); see
[the integrated frontier](SIX_FIBER_EQUITABLE_MODEL_FRONTIER.md).
The 98-matrix enumeration and intermediate counts below are preserved.

Date: 2026-10-12. One complete necessary-quotient enumeration leaves four
orbits, one of which is then excluded analytically. The remaining three
orbits are construction obligations, not sixty-vertex graph witnesses.
The four previously studied uniform internal-degree domains were not rerun.

## Bounds without a uniform-degree assumption

Let an eight-regular diameter-two graph have an equitable partition into
six fibers of size ten. Fiber $i$ has internal degree $d_i$; every vertex
of fiber $i$ has $q_{ij}$ neighbors in fiber $j$. Equal fiber sizes and
undirectedness imply $q_{ij}=q_{ji}$. Put $q_{ii}=0$ and

$$k_i=\sum_{j\ne i}q_{ij}=8-d_i,\qquad
s_i=\sum_{j\ne i}q_{ij}^2.$$

For a fixed vertex in fiber $i$, the total number of direct and two-step
routes ending in fiber $j\ne i$ is

$$h_{ij}=(1+d_i+d_j)q_{ij}+(Q^2)_{ij}\ge10.\tag{1}$$

The terms respectively count a direct edge, a path with its intermediate
vertex in either endpoint fiber, and a path through a different fiber.
Multiplicity only increases this route count, so covering all ten targets
requires the inequality. Summing over the five other fibers gives

\begin{align*}
\sum_{j\ne i}h_{ij}
&=(1+d_i)k_i+\sum_j d_jq_{ij}
  +\sum_jq_{ij}(8-d_j)-s_i\\
&=(9+d_i)(8-d_i)-s_i\\
&=72-d_i-d_i^2-s_i\ge50.
\end{align*}

Thus $s_i\le22-d_i-d_i^2$. For the nine other vertices within fiber $i$,
the internal direct/nonbacktracking routes contribute at most
$d_i+d_i(d_i-1)=d_i^2$ slots. Returning through external fiber $j$
contributes $q_{ij}(q_{ij}-1)$ slots. Therefore

$$d_i^2+s_i-k_i\ge9,\qquad
17-d_i-d_i^2\le s_i\le22-d_i-d_i^2.\tag{2}$$

Since the entries are nonnegative integers, $s_i\ge k_i=8-d_i$.
Combining with the upper bound in (2) yields $d_i^2\le14$, so

$$d_i\in\{0,1,2,3\}\qquad\text{for every fiber }i.$$

No step used equality of the six internal degrees. Also

$$48-\sum_i d_i=\sum_i k_i=2\sum_{i<j}q_{ij}$$

is even. This parity condition follows from the symmetric integer quotient,
not from a claim that an individual ten-vertex internal graph has even
degree.

## Exact finite domain and implementation

Relabel fibers so $d_0\le\cdots\le d_5$. There are
$\binom{9}{3}-4=80$ nonconstant tuples. Forty have odd sum and are excluded
by the proved parity condition; the other forty are enumerated.

For each $d\in\{0,1,2,3\}$ the
[C++ implementation](../../../computations/dd82/construction/six_fiber_variable_internal_search.cpp)
generates every ordered nonnegative integer five-tuple with sum $8-d$
and squared norm in the interval (2). The complete pattern counts are

| Internal degree | Ordered row patterns |
| ---: | ---: |
| 0 | 185 |
| 1 | 140 |
| 2 | 90 |
| 3 | 51 |

In particular degree-one rows include permutations of $(4,1,1,1,0)$.
No bound $q_{ij}\le3$ from an older uniform-degree argument is imported.
The present row bounds only force $q_{ij}\le4$.

For each sorted degree tuple, row $i$ is selected from its full pattern
list after inserting a zero at diagonal position $i$. Selection requires
its prefix in columns $0,\ldots,i-1$ to equal the entries already assigned
by preceding rows. Each selected suffix is copied symmetrically.
Consequently every symmetric matrix with these row conditions is produced
exactly once. No cross-capacity pruning is done before a complete matrix
is counted. At each complete matrix all fifteen quantities in (1) are
calculated, and the matrix survives exactly when their minimum is at least
ten.

The [single run](../../../computations/dd82/construction/six_fiber_variable_internal_run/search.json)
completed **all forty eligible tuples**:

* 5,196,079 recursive nodes;
* 79,313 complete symmetric matrices satisfying the row conditions;
* 98 matrices satisfying all fifteen cross-capacity conditions;
* `complete: true`, `stop_reason: complete_domain`;
* zero uniform-degree tuples searched.

Every one of the eighty degree tuples has its status and actual counts in
the result JSON, including the forty parity exclusions. All 98 surviving
matrices are retained, without a sample limit, in
[the JSON-lines output](../../../computations/dd82/construction/six_fiber_variable_internal_run/search.survivors.jsonl).

The [runner](../../../computations/dd82/construction/six_fiber_variable_internal_run.py)
used one pinned CPU, a ten-second internal CPU cap, and a 1 GiB memory
limit. Actual process CPU was **0.129702 seconds**, wall time
**0.131382 seconds**, and peak resident memory **7,164 KiB**;
[resource records](../../../computations/dd82/construction/six_fiber_variable_internal_run/resources.json)
are retained. This was one invocation, with no extension or second domain
search.

## Independent checks and four quotient orbits

A separate [direct verifier](../../../computations/dd82/construction/six_fiber_variable_internal_verify.py)
reads the saved 98 matrices and checks their symmetry, integer entries,
row sums, row norms, all cross capacities, uniqueness, and agreement with
the recorded counts. It also computes the defect quotient by ordinary
matrix multiplication:

$$R=\operatorname{diag}(d)+Q,\qquad
D=R^2+R-7I_6-10J_6.\tag{3}$$

All entries of $D$ are nonnegative, and every row sums to five.
This is the quotient of the actual path-defect matrix
$A^2+A-7I_{60}-J_{60}$ whenever the proposed quotient is realized.

Relabeling the saved matrices by all permutations preserving the degree
tuple yields exactly four orbits. The verifier checks that every member
of each such orbit is present in the saved list; this groups existing
output and does not repeat the quotient enumeration. It used 0.070994146
CPU seconds. All four representatives, their full matrices $R,D$, and
the checks are in
[verification.json](../../../computations/dd82/construction/six_fiber_variable_internal_run/verification.json).

| Orbit | Sorted internal degrees | Labeled matrices | Subsequent status |
| ---: | --- | ---: | --- |
| 1 | $(0,0,1,2,2,3)$ | 2 | Necessary quotient remains open |
| 2 | $(1,1,1,1,1,3)$ | 12 | Excluded by the odd-cycle determinant argument below |
| 3 | $(1,1,1,1,1,3)$ | 60 | Necessary quotient remains open |
| 4 | $(1,1,1,1,3,3)$ | 24 | Necessary quotient remains open |

## The simplest quotient and its analytic obstruction

Orbit 2 has five degree-one fibers forming a cycle, with cross degree
three on the cycle edges. The sixth fiber has internal degree three and
is joined to each cycle fiber by a perfect matching. One labeling gives

$$Q=\begin{pmatrix}
0&0&0&3&3&1\\
0&0&3&0&3&1\\
0&3&0&3&0&1\\
3&0&3&0&0&1\\
3&3&0&0&0&1\\
1&1&1&1&1&0
\end{pmatrix},\qquad
D=\begin{pmatrix}4I_5&\mathbf1\\\mathbf1^T&0\end{pmatrix}.$$

This was selected by the search as its simplest representative; its
[record](../../../computations/dd82/construction/six_fiber_variable_internal_run/search.representative.json)
is preserved unchanged even though the quotient is now excluded.

Independently relabel the five outer fibers to make all five matchings
to the central fiber identity matrices. Index the outer cycle by
$i\in\mathbb Z_5$, and let $Y_i$ be the oriented cubic interface from
$i$ to $i+1$. For the nonadjacent pair of fibers $i,i+2$, the only possible
intermediate fibers are $i+1$ and the central fiber. Their exact capacity
is $3\cdot3+1=10$. Covering all ten targets with these ten slots requires

$$Y_iY_{i+1}+I_{10}=J_{10},\qquad
Y_iY_{i+1}=K:=J_{10}-I_{10}\quad(i\bmod5).\tag{4}$$

The eigenvalues of $K$ are $9$ once and $-1$ nine times, so
$\det K=-9$. Take determinants in all five equations (4) and multiply:

$$\left(\prod_{i=0}^4\det Y_i\right)^2=(-9)^5<0,$$

which is impossible over the reals. Therefore **the whole twelve-matrix
orbit is unrealizable**, allowing arbitrary internal graphs and arbitrary
individual cubic interfaces. No cyclic homogeneity of the $Y_i$ was
assumed.

## An explicit remaining construction quotient

For example, orbit 1 remains after this obstruction. With
$d=(0,0,1,2,2,3)$, an explicit necessary quotient and its defect quotient
are

$$Q=\begin{pmatrix}
0&1&3&0&3&1\\
1&0&3&3&0&1\\
3&3&0&0&0&1\\
0&3&0&0&2&1\\
3&0&0&2&0&1\\
1&1&1&1&1&0
\end{pmatrix},\qquad
D=\begin{pmatrix}
3&1&0&0&0&1\\
1&3&0&0&0&1\\
0&0&4&0&0&1\\
0&0&0&3&1&1\\
0&0&0&1&3&1\\
1&1&1&1&1&0
\end{pmatrix}.$$

Thus the complete necessary screen and the stated analytic obstruction
leave **86 labeled matrices in three orbits**. No full sixty-vertex graph
was generated, no graph/SAT search was run, and no nonuniform-family
nonexistence claim is made beyond the excluded orbit. Constructing or
excluding compatible ten-vertex internal graphs and interface matrices
for the remaining three quotients is still required.
