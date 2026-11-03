# A four-point component forces a six-point companion: two quotient exclusions

## Claim

Let $G$ be an actual legal order-62 graph, and let $B$ be its actual
repeat matrix. If a four-vertex component $C$ of the positive support
of $B$ contains an original edge of $G$, then $B$ has a distinct
six-vertex component. More precisely, $C$ is a D0_EDGE_BOUT component
and has the independent unit-prism companion from the D0 theorem.

Consequently the following two actual component-size and internal-degree
patterns are impossible:

| Number of components | Component sizes | Original internal degrees |
|---|---|---|
| $5$ | $(4,8,10,20,20)$ | $(1,2,0,2,1)$ |
| $7$ | $(4,4,4,10,10,10,20)$ | $(1,1,1,0,0,0,2)$ |

This includes the specific five- and seven-component quotient matrices
listed below. Their off-diagonal entries are not needed for the exclusion.

## Status

**PROVABLE AS STATED.** New paper proof awaiting independent review.
The two applications exclude specified actual quotients. They do not
certify the completeness of the separate quotient enumeration and do
not establish a universal order-62 exclusion.

## Assumptions and notation

Use the actual order-62 graph identities and the established local
reductions. In particular, $B$ is symmetric, nonnegative, integral,
zero on the diagonal, and has row sum three; triple-repeat exclusion
gives $B_{uv}\le2$. For distinct vertices,

$$c_G(u,v)+A_{uv}=1+B_{uv}.\tag{1}$$

Use the following precise source results:

1. An original triangle and its mate form a closed connected six-vertex
   repeat component, by `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`,
   Sections 1--4.
2. Every surviving double repeat is D0 or D1, after the established
   D2 and D0_EDGE_BIN exclusions, as used in
   `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`.
3. A D1 heavy component contains six distinct vertices $0,w,a,r,p,q$:
   the normalized rows in `D1_MATCH_HARD_BRANCH_REDUCTION.md`, Section 1,
   give

   $$B_0=2e_w+e_a,\qquad B_w=2e_0+e_r,\qquad
   B_a=e_0+e_p+e_q,$$

   and state that $r,p,q$ are distinct ordinary points, separate from
   $0,w,a$. All six lie in the same repeat component. This elementary
   consequence is enough here; no D1 component minimum-size paper is
   needed.
4. Every D0 component has a distinct closed six-vertex companion unit
   prism, by `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 2. The
   original internal degree of the four-vertex component is zero in
   D0_MATCH and one in D0_EDGE_BOUT; its companion is independent in
   the original graph.

The component quotient is equitable for $A$, as proved in Section 3
of the same global paper. We write $r_{CC}$ for the common original
internal degree of the vertices of $C$.

## Proof strategy and dependency map

Triangle pairing prevents a vertex in a four-point repeat component
from belonging to any original triangle. An original edge in that
component therefore has repeat weight zero. The repeat row budget
then forces a double edge inside the component. The six distinct
vertices already present in every D1 heavy component rule out D1,
so the D0 companion-prism theorem supplies the required six-point
component. The two quotient applications each have an internal edge
in a four-point component and no component of size six.

## Proof of the uniform lemma

### 1. Vertices in a four-point repeat component lie in no original triangle

Let $C$ be a repeat component with $|C|=4$. If a vertex of $C$ belonged
to an original triangle, the triangle-pairing theorem would put that
vertex in a closed connected six-vertex repeat component. Uniqueness
of the repeat component containing a vertex would then give $|C|=6$,
a contradiction.

Thus every vertex of $C$ is triangle-free, regardless of whether the
rest of $G$ contains triangles.

### 2. An original edge forces a double repeat in $C$

Suppose $u,v\in C$ form an original edge. A common neighbor of $u,v$
would create an original triangle through $u$. Hence $c_G(u,v)=0$,
and (1) gives

$$B_{uv}=0.$$

Write $C=\{u,v,x,y\}$. The repeat row of $u$ is supported on $C$,
has zero diagonal, and has total weight three. Therefore

$$B_{ux}+B_{uy}=3.$$

Both entries are integers between zero and two. Their values must
be one and two, in some order. Thus $C$ contains a double repeat.

### 3. The double repeat is D0 and forces a distinct six-point component

By the established local coverage, this double repeat is D0 or D1.
If it were D1, its repeat component would contain the six distinct
vertices specified in the D1 rows above. They cannot fit into $C$.
Thus it is D0.

The D0 component theorem identifies its complete four-vertex component,
which must be $C$. Its companion-prism theorem supplies a separate
closed six-vertex repeat component. Since $G[C]$ contains an edge,
the component cannot be D0_MATCH, whose original internal degree is
zero. It is therefore D0_EDGE_BOUT, with $r_{CC}=1$ and with an
independent original graph on its six-vertex unit-prism companion.
This proves the uniform claim.

## Application 1: the five-component candidate

The proposed sizes and quotient are

$$
n=(4,8,10,20,20),\qquad
R=\begin{pmatrix}
1&2&5&0&0\\
1&2&0&0&5\\
2&0&0&4&2\\
0&0&2&2&4\\
0&2&1&4&1
\end{pmatrix}.
$$

The first component has size four and original internal degree one,
so it contains an original edge. The uniform lemma forces another
repeat component of size six. None of the five displayed component
sizes is six. This contradicts the proposed complete component list.

## Application 2: the seven-component candidate

The proposed sizes and quotient are

$$
n=(4,4,4,10,10,10,20),\qquad
R=\begin{pmatrix}
1&1&1&0&0&5&0\\
1&1&1&0&5&0&0\\
1&1&1&5&0&0&0\\
0&0&2&0&1&1&4\\
0&2&0&1&0&1&4\\
2&0&0&1&1&0&4\\
0&0&0&2&2&2&2
\end{pmatrix}.
$$

Each of the first three components has size four and original internal
degree one. Applying the uniform lemma to any one of them forces a
six-vertex repeat component, whereas no displayed component has size
six. This excludes the proposed seven-component quotient.

## Scope and remaining dependencies

The candidate data were read from
`computations/dd82/n62/component_quotients_5.json` and
`computations/dd82/n62/component_quotients_7.json`. Their enumeration
status and coverage are separate questions; this proof does not use
the claim that either candidate list is exhaustive. It assumes a graph
has one of the displayed actual quotients and obtains a contradiction.

No solver, numerical feasibility assertion, graph-realizability claim,
or new Lean result is used. The proof uses only the six explicitly
distinct D1 vertices, not the later bounds twelve or fourteen. The
earlier three-component proofs are unchanged. Other component-size
patterns and the full order-62 problem remain outside this paper.
Independent review of the new uniform lemma and its applications is
outstanding.
