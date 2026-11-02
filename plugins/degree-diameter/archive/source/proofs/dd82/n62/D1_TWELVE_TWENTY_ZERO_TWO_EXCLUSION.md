# Quotient divisibility excludes the last twelve-by-twenty partner case

## Claim

An actual legal order-62 graph cannot have distinct components $H,K$ of
the positive support of its repeat matrix $B$ with

$$
(|H|,|K|,r_{HK},r_{KH},r_{HH},r_{KK})=(12,20,5,3,0,2).
$$

The notation $r_{CD}$ means the number of original-graph neighbors in
$D$ of each vertex of $C$; the direction of its subscripts matters.
The claim applies to arbitrary such components, including the remaining
size-twenty partner case for a twelve-vertex D1 heavy component.

## Status

**PROVABLE AS STATED.** New paper proof, awaiting independent review.
This is not a Lean theorem and does not exclude all order-62 graphs.

## Assumptions

Let $G$ be an actual 62-vertex graph of maximum degree eight and diameter
at most two, in the established regular order-62 reduction. Its adjacency
matrix $A$ and repeat matrix $B$ satisfy

$$
A\mathbf1=8\mathbf1,\qquad
B=A^2+A-7I-J,\qquad B\mathbf1=3\mathbf1,
$$

where $B$ is nonnegative and symmetric. Use the actual component quotient
proved in `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 3: the component
partition of $B$ is equitable for $A$, and its integer quotient $R$ obeys

$$
R\mathbf1=8\mathbf1,\qquad
R^2+R=10I+\mathbf1 n^T,\qquad
|C|r_{CD}=|D|r_{DC}.
\tag{1}
$$

Here $n$ is the vector of component sizes. No assertion that $A$ preserves
each individual component is made or used.

## Notation

Let $E$ range over the components other than $H,K$. Put

$$
e=|E|,\qquad p=r_{HE},\quad q=r_{KE},\quad
x=r_{EH},\quad y=r_{EK}.
\tag{2}
$$

All these numbers are nonnegative integers. Balance in (1) gives

$$12p=ex,\qquad 20q=ey.$$ 

## Proof strategy and dependency map

1. The row sum at $H$ bounds every positive $p$ by three.
2. The two balance equations force $5\mid py$.
3. The actual common-neighbor identity bounds $y$ by three whenever
   $x>0$. These facts rule out every exterior component meeting both
   $H$ and $K$ in the original graph.
4. The $(H,K)$ entry of the quotient identity requires a positive
   contribution from such a component, giving a contradiction.

Only the component quotient result is essential. The pointwise inequality
used below is also the specialization of Section 8 of
`D1_COMPONENT_MINIMUM_SIZES.md`. The exterior moment check at the end
uses that paper's exact formulas; it is not a separate assumption.

## Proof

### 1. The exterior row budget at $H$

The assumed internal and cross degrees and the row sum in (1) give

$$
\sum_{E\ne H,K}r_{HE}=8-r_{HH}-r_{HK}=3.
\tag{3}
$$

In particular $0\le p\le3$. If $x>0$, balance $12p=ex$ and $e>0$
imply $p>0$.

### 2. An exterior component cannot meet both $H$ and $K$

Suppose $x>0$ and $y>0$ for an exterior component $E$. Multiplying the
two balance equations respectively by $y$ and $x$ gives

$$12py=exy=20qx,$$

and hence

$$3py=5qx\quad\Longrightarrow\quad 5\mid py.$$

By (3), $p\in\{1,2,3\}$; each is relatively prime to five. Therefore

$$5\mid y.\tag{4}$$

For completeness, the required pointwise upper bound on $y$ follows
directly from the same actual graph identity. Define
$d_H=A\mathbf1_H$. Since $B\mathbf1_H=3\mathbf1_H$,

$$
(A^2+A)\mathbf1_H=10\mathbf1_H+12\mathbf1.
$$

At a vertex $v\in E$ this says

$$\sum_{u\in N_G(v)}d_H(u)+x=12.$$

Every neighbor $u\in K$ has $d_H(u)=r_{KH}=3$. There are $y$ such
neighbors, and every other contribution is nonnegative. Consequently

$$x+3y\le12.$$

Since $x\ge1$, this implies $1\le y\le3$, contradicting (4).
Thus every exterior component satisfies

$$xy=0,\qquad py=0.\tag{5}$$

The second equality follows because $x=0$ implies $p=0$ by balance.

### 3. The off-diagonal quotient identity requires a mixed component

The $(H,K)$ entry of (1) is

$$
r_{HH}r_{HK}+r_{HK}r_{KK}
 +\sum_{E\ne H,K}r_{HE}r_{EK}+r_{HK}=|K|.
$$

Substitution gives

$$0+10+\sum_{E\ne H,K}py+5=20,$$

so

$$\sum_{E\ne H,K}py=5.$$

Every summand is zero by (5), a contradiction. This proves the claim.

## Exterior-moment interpretation

The exact exterior data in the stated case are

$$
\sum1=30,\quad \sum x=36,\quad \sum x(x-1)=48,
\quad \sum y=60,\quad \sum y(y-1)=120,\quad \sum xy=60.
$$

Their integer domain is

$$x+y\le8,\qquad x+3y\le12,\qquad5x+3y\le20.$$

The preceding proof shows directly that $xy=0$ at every exterior vertex,
contradicting the positive mixed moment. Equivalently, balance gives

$$
\sum_{v\notin H\cup K}x_vy_v
=\sum_E e x y=12\sum_E p y=60.
$$

A useful general constraint behind this argument is that every exterior
type $T_{xy}$, being a union of entire $B$ components, satisfies

$$12\mid |T_{xy}|x,\qquad20\mid |T_{xy}|y.$$

Indeed the number of neighbors in $T_{xy}$ is constant on $H$ and on
$K$, by summing the corresponding integer quotient entries; counting
the edges into the type gives the two divisibilities. Thus even type
sizes alone omit relevant arithmetic information. No enumeration of
type counts is required for the exclusion above.

## Scope and open risks

Together with the size-twenty internal-degree-one exclusion in
`D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`, this removes both surviving
size-twenty partners of a twelve-vertex D1 heavy component. With the other
cited twelve-component reductions, only the seven size-sixteen cases
remain on that earlier necessary list. This combined consequence is
conditional on the source results and their separate review status.

No triangle-free hypothesis for all of $G$, parity of D1 double edges,
component-size classification, solver output, or numerical relaxation is
used. The proof does not decide the size-sixteen cases or any case with
a heavy component of size at least fourteen. Independent review of this
new quotient-divisibility argument remains outstanding.
