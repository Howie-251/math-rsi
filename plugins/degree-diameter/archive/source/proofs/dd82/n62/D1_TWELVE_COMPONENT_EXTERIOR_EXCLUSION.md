# Exterior type counts exclude the twelve-by-twelve D1 component pair

## Claim and status

**PROVABLE AS STATED, new paper derivation awaiting independent review.**
An actual order-62 graph cannot have two distinct twelve-vertex
components of the repeat matrix with original cross degrees four in
both directions and original internal degrees zero and one.

Consequently, using `D1_COMPONENT_MINIMUM_SIZES.md`, the component
containing the generated unit triangle of every D1 double edge has
at least fourteen vertices. This excludes the $(12,4,4)$ alternative
in that paper; it does not exclude all D1 configurations.

## Assumptions, notation, and dependencies

Use the actual identities

$$A\mathbf1=8\mathbf1,\qquad
 B=A^2+A-7I-J,\qquad B\mathbf1=3\mathbf1,\qquad AB=BA,$$

with $B$ nonnegative, integral, symmetric, and zero on the diagonal.
Use the established exclusion of repeat entries three.

A component means a component of the positive support of $B$.
The component partition is equitable for $A$, as established in
`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`. Use the exact exterior moments
and pointwise common-neighbor inequalities proved in Section 8 of
`D1_COMPONENT_MINIMUM_SIZES.md`.

Suppose the two prohibited components exist. Denote by $C$ the one
with original internal degree zero and by $D$ the one with original
internal degree one. Both have size twelve and cross degree four.
For each of the 38 vertices outside $C\cup D$, put

$$x_v=|N_G(v)\cap C|,\qquad y_v=|N_G(v)\cap D|.$$

For nonnegative integers $i,j$, let $n_{ij}$ be the number of exterior
vertices with $(x_v,y_v)=(i,j)$.

## Proof strategy

The exact moments restrict $x_v,y_v$ to $\{0,1,2\}$. Equitability
then forces all six vertices having $y_v=2$ into one common type.
The three possible types each contradict the remaining moments and
the minimum size of a component.

## 1. Exact moments and the minimum nonempty type size

The exterior formulas give

$$\begin{aligned}
\sum_v1&=38,&\sum_vx_v&=48,&\sum_vy_v&=36,\\
\sum_vx_v(x_v-1)&=24,&
\sum_vy_v(y_v-1)&=12,&
\sum_vx_vy_v&=48.
\end{aligned} \tag{1}$$

The pointwise inequalities are

$$x_v+4y_v\le12,\qquad 4x_v+2y_v\le12. \tag{2}$$

Each component has even size: its total repeat row sum, three times
its size, is twice its unordered repeat weight. A size-two component
would have its unique off-diagonal entry equal to three, which is
excluded. Therefore every component has at least four vertices.

Both $x_v$ and $y_v$ are constant on each exterior component, by
equitability. Every exterior type is a union of entire components.
Consequently

$$n_{ij}=0\quad\text{or}\quad n_{ij}\ge4,
\qquad n_{ij}\text{ is even}. \tag{3}$$

This applies to the type $(0,0)$ as well. The argument below needs
the lower bound four; it does not replace it with evenness alone.

## 2. Both coordinates are at most two

Inequalities (2) first give $0\le x_v,y_v\le3$. If $y_v=3$, then
$x_v=0$. A nonempty type $(0,3)$ would have at least four vertices,
contributing at least $4\cdot3\cdot2=24$ to the $y_v(y_v-1)$ moment.
This contradicts its total value 12. Thus $y_v\le2$.

If $x_v=3$, (2) forces $y_v=0$. A nonempty type $(3,0)$ has at least
four vertices, while the $x_v(x_v-1)$ total 24 permits at most four.
It would therefore contain exactly four vertices and exhaust that
entire moment. All remaining vertices would have $x_v\le1$.
Then $x_vy_v\le y_v$ at every exterior vertex, including the four
vertices with $y_v=0$. This contradicts

$$48=\sum_vx_vy_v\le\sum_vy_v=36.$$

Hence

$$x_v,y_v\in\{0,1,2\}. \tag{4}$$

The two factorial moments in (1) now say

$$n_{20}+n_{21}+n_{22}=12,\qquad
 n_{02}+n_{12}+n_{22}=6. \tag{5}$$

By (3), the three nonnegative counts in the second equation cannot
have two positive terms: their sum would be at least eight. Thus
exactly one of $n_{02},n_{12},n_{22}$ equals six and the other two
are zero.

## 3. All three possible locations of the six vertices are impossible

Put $u=n_{21}$.

### 3.1. Suppose $n_{22}=6$

Then $n_{02}=n_{12}=0$. The first equation of (5), the mixed moment,
the first moments, and the total count in (1), in that order, give

$$\begin{aligned}
n_{20}&=6-u, & n_{11}&=24-2u,\\
n_{01}&=u, & n_{10}&=2u, & n_{00}&=2-u.
\end{aligned}$$

In particular $n_{21}+n_{00}=2$. Each of these two counts must be
zero or at least four by (3), so their sum cannot be two.

### 3.2. Suppose $n_{12}=6$

Now $n_{02}=n_{22}=0$. The same moment equations give

$$n_{20}=12-u,\qquad n_{11}=36-2u,\qquad n_{01}=u-12.$$

Nonnegativity of $n_{20},n_{01}$ forces $u=12$. It follows that
$n_{20}=n_{01}=0$, $n_{11}=12$, and $n_{10}=6$. Together with
$n_{12}=6$ and $n_{21}=12$, these account for 36 exterior vertices.
The remaining count is $n_{00}=2$, contradicting (3).

### 3.3. Suppose $n_{02}=6$

Here $n_{12}=n_{22}=0$. The first equation of (5) gives
$n_{20}=12-u$. The mixed moment gives $n_{11}=48-2u$, and the
$y$ first moment then gives $n_{01}=u-24$. Nonnegativity would
require both $u\le12$ and $u\ge24$, a contradiction.

All possibilities are exhausted. Therefore the asserted component
pair does not exist.

## 4. Consequence for a D1 generated-triangle component

The preceding minimum-size paper proves that a D1 generated-triangle
component $K$ has size at least twelve. If it has size twelve, its
heavy component $H$ is distinct, also has size twelve, has cross
degrees four with $K$, and the two internal degrees are zero and
one in some order. Relabeling those two components as $C,D$ gives
exactly the configuration just excluded. Thus $|K|>12$, and its
even size gives

$$\boxed{|K|\ge14}.$$

## Remaining gap

The four other size/incidence triples for a twelve-vertex heavy
component remain subject to separate arguments. This proof also
does not exclude larger components or the case where a heavy edge
and its generated triangle lie in the same component. No solver,
linear-programming infeasibility claim, or unverified finite table
is used in this exclusion.
