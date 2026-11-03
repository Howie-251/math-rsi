# Divisible exterior types exclude all remaining twelve-by-sixteen cases

## Claim

An actual legal order-62 graph cannot have distinct repeat-support
components $H,K$ with sizes $12,16$, original cross degrees
$r_{HK}=4$, $r_{KH}=3$, and internal degrees $(s,t)=(r_{HH},r_{KK})$ in

$$
\{(0,0),(0,1),(0,2),(1,1),(1,2),(2,0),(2,1)\}.
\tag{1}
$$

Consequently, combined with the separately established size-twelve
partner list and its other exclusions, every D1 heavy component has
at least fourteen vertices.

## Status

**PROVABLE AS STATED.** New paper derivation, awaiting independent
review. The combined D1 consequence is conditional on the cited source
results and their review status. This is not a Lean theorem or a complete
order-62 exclusion.

## Assumptions and notation

Use the actual order-62 graph identities, component equitability, and
quotient balance in `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 3:

$$
A\mathbf1=8\mathbf1,\quad
B=A^2+A-7I-J,\quad B\mathbf1=3\mathbf1,\quad
R^2+R=10I+\mathbf1 n^T,
$$

with $B$ nonnegative, symmetric, integral, and zero on the diagonal.
Every repeat-support component has even size, because three times its
size is twice its total unordered repeat weight.

For each of the $34$ vertices outside $H\cup K$, define

$$x_v=d_H(v)=|N_G(v)\cap H|,\qquad
y_v=d_K(v)=|N_G(v)\cap K|.$$

Let $N_{ij}$ be the number of these vertices with $(x_v,y_v)=(i,j)$.
Each type is a union of whole repeat-support components. In particular
its size is even. Equitability from $H$ and $K$ into the union, followed
by edge counting, gives the further necessary divisibilities

$$12\mid iN_{ij},\qquad16\mid jN_{ij}.\tag{2}$$

No assumption that $A$ preserves an individual repeat component is used.

The exact exterior formulas of `D1_COMPONENT_MINIMUM_SIZES.md`, Section
8, specialize to

$$
\begin{aligned}
S_x:=\sum x_v&=48-12s,&
F_x:=\sum x_v(x_v-1)&=72-12s^2,\\
S_y:=\sum y_v&=80-16t,&
F_y:=\sum y_v(y_v-1)&=144-16t^2,\\
C:=\sum x_vy_v&=48(3-s-t).
\end{aligned}\tag{3}
$$

Their pointwise domain is

$$
x_v+y_v\le8,\qquad(s+1)x_v+3y_v\le12,
\qquad4x_v+(t+1)y_v\le16.
\tag{4}
$$

For later use, the original matrix identity gives, for any repeat
component $L$ and any vertex $v\notin L$,

$$
(A d_L)(v)+d_L(v)=|L|.
\tag{5}
$$

Indeed $B\mathbf1_L=3\mathbf1_L$, so
$(A^2+A)\mathbf1_L=10\mathbf1_L+|L|\mathbf1$.

## Proof strategy and dependency map

First, the divisibilities (2) leave only two possible mixed exterior
types, which cannot coexist. This excludes the two largest mixed
moments. The three cases with mixed moment $48$ reduce either to a
moment contradiction or to a forbidden internal degree on a six-vertex
component. The two zero-mixed-moment cases are decided by pure-type
counting, with the last case contradicted by (5).

The argument uses the actual component quotient and exterior moment
identities. The seven-case input (1) is the size-sixteen part of
`D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`. The proof below is explicit
integer arithmetic and does not use an LP or graph search.

## Proof

### 1. The only possible mixed types

Call a type mixed if both coordinates are positive. Since $s,t\ge0$,
(4) implies $1\le x,y\le3$ for every mixed type. Combining evenness
with (2), its size is divisible by the indicated number:

| $(x,y)$ | $(1,1)$ | $(1,2)$ | $(1,3)$ | $(2,1)$ | $(2,2)$ | $(2,3)$ | $(3,1)$ | $(3,2)$ | $(3,3)$ |
|---|---|---|---|---|---|---|---|---|---|
| divisor of $N_{xy}$ | $48$ | $24$ | $48$ | $48$ | $24$ | $48$ | $16$ | $8$ | $16$ |

Each entry is
$\operatorname{lcm}(2,12/\gcd(12,x),16/\gcd(16,y))$.
There are only $34$ exterior vertices. Thus the divisor-$48$ types
cannot occur. A type $(3,1)$ or $(3,3)$ would contribute at least
$16\cdot3\cdot2=96$ to $F_x$, exceeding $F_x\le72$.

A type $(2,2)$ would have exactly $24$ vertices, contributing $48$ to
$S_x$. If $s>0$ this exceeds $S_x$. If $s=0$ it exhausts $S_x$, so
every other vertex has $x=0$; its contribution $48$ to $F_x$ cannot
then reach the required $72$. Thus this type is also impossible.

Consequently the only possible mixed types and sizes are

$$
P=(1,2)\text{ with }N_{12}=24,
\qquad M=(3,2)\text{ with }N_{32}=8.
\tag{6}
$$

For the second assertion, a larger allowed size is at least $16$ and
would again contribute at least $96$ to $F_x$.

The two types in (6) cannot coexist. Together they contribute $48$ to
$S_x$ and $48$ to $F_x$. When $s>0$ the first value exceeds $S_x$;
when $s=0$ it exhausts $S_x$ but leaves $F_x=72$ unattained. Each type
in (6) contributes exactly $48$ to $C$. It follows that

$$C\in\{0,48\}.\tag{7}$$

### 2. Internal degrees $(0,0)$ and $(0,1)$

Formula (3) gives respectively $C=144$ and $C=96$, contradicting (7).

### 3. Internal degrees $(0,2)$, $(1,1)$, and $(2,0)$

Here $C=48$, so exactly one of the two types in (6) occurs.

For $(s,t)=(0,2)$, type $M$ violates $4x+3y\le16$ because
$4\cdot3+3\cdot2=18$. Hence type $P$ occurs. Its $24$ vertices
exhaust $S_y=48$, while contributing only $48$ to $F_y=80$. Every
remaining vertex has $y=0$, giving a contradiction.

For $(s,t)=(2,0)$, type $M$ violates $3x+3y\le12$. Type $P$ therefore
occurs and exhausts $S_x=24$, while contributing zero to $F_x=24$.
Again the remaining vertices cannot supply the missing moment.

For $(s,t)=(1,1)$, suppose first that type $P$ occurs. The remaining
vertices have total $x$-sum $12$ and factorial moment $60$. But (4)
gives $x\le4$, hence $x(x-1)\le3x$ at each vertex. Their factorial
moment is therefore at most $36$, a contradiction.

It remains to treat $(s,t)=(1,1)$ with the eight vertices of type $M$.
They contribute $24$ to $S_x$ and $48$ to $F_x$. All other positive-$x$
vertices are pure types, and their residual moments are

$$\sum x=12,\qquad\sum x(x-1)=12.$$

Pure-type divisibility gives $4\mid N_{30}$ and $6\mid N_{40}$.
A nonempty one of those types would contribute at least $24$ or $72$
to the residual factorial moment, respectively. Thus neither occurs.
The residual moments then force exactly six vertices of type $(2,0)$,
and no vertices of type $(1,0)$. Denote this six-vertex type by $X$.

Both $M$ and $X$ are individual repeat components. Every component
inside $M$ has size divisible by eight, by applying (2) to that component
itself; their total size is eight. Every component inside $X$ has size
divisible by six and their total size is six.

The function $d_H$ equals $1$ on $H$, $3$ on $K$ and $M$, $2$ on
$X$, and zero on every other exterior vertex. For $v\in M$, (5) gives

$$12=3\cdot1+2\cdot3+3d_M(v)+2d_X(v)+3,$$

so $d_M(v)=d_X(v)=0$. In particular there are no original edges from
$M$ to $X$. For $v\in X$, equation (5) now gives

$$12=2\cdot1+2d_X(v)+2,$$

and therefore $d_X(v)=4$. This means $r_{XX}=4$. But the $(X,X)$ entry
of the actual quotient identity implies

$$r_{XX}^2+r_{XX}\le |X|+10=16,$$

whereas the left side is $20$. This excludes the last branch with
$s+t=2$.

### 4. Internal degrees $(2,1)$

Now $C=0$, so every exterior vertex has $x=0$ or $y=0$. Let $U$ be
the positive-$x$ support and $V$ the positive-$y$ support; they are
disjoint. The $x$ moments are $S_x=24$, $F_x=24$. For every positive
integer $x$, $x-1\le x(x-1)/2$, so

$$|U|\ge S_x-F_x/2=12.\tag{8}$$

By (4), $y\le4$. Since positive-$y$ types are pure, (2) permits us to
write their counts as

$$N_{01}=16a,\quad N_{02}=8b,\quad N_{03}=16c,\quad N_{04}=4d,$$

with $a,b,c,d$ nonnegative integers. The moments $S_y=64$, $F_y=128$
give

$$a+b+3c+d=4,\qquad b+6c+3d=8.\tag{9}$$

The first equation gives $c\le1$. If $c=1$, then
$a+b+d=1$ and $b+3d=2$. For $d=0$ the latter forces $b=2$, contrary
to the former; for $d\ge1$ the latter forces $b<0$. Thus $c=0$.
Equations (9) then give $a=2d-4$, $b=8-3d$. Nonnegativity forces
$d=2$, whence $a=0$, $b=2$.

Therefore $N_{04}=8$, $N_{02}=16$, and $|V|=24$. Together with (8),
this gives at least $36$ exterior vertices, contradicting their total
number $34$.

### 5. Internal degrees $(1,2)$

Again $C=0$, so all positive-coordinate types are pure. The $x$ moments
are $S_x=36$, $F_x=60$, and $x\le4$. A nonempty pure type with $x=4$
has at least six vertices and contributes at least $72$ to $F_x$, so
it cannot occur. Put $u=N_{10}$, $v=N_{20}$, $w=N_{30}$. Their moments
give

$$u+2v+3w=36,\qquad v+3w=30,$$

or $u=3w-24$, $v=30-3w$. Thus $8\le w\le10$. Since $4\mid w$,

$$N_{30}=8,\qquad N_{20}=6,\qquad N_{10}=0.\tag{10}$$

The $y$ moments are $S_y=48$, $F_y=80$. A type with $y=3$ would have
at least sixteen vertices and contribute at least $96$ to $F_y$, so
it is absent. Put $a=N_{01}$, $b=N_{02}$, $d=N_{04}$. Then

$$a+2b+4d=48,\qquad b+6d=40,$$

so $a=8d-32$, $b=40-6d$. Nonnegativity gives $4\le d\le6$; since
$4\mid d$, it follows that

$$N_{04}=4,\qquad N_{02}=16,\qquad N_{01}=0.\tag{11}$$

The four nonzero type counts in (10)--(11) sum to $34$. Hence there
are no vertices of type $(0,0)$, and the full exterior distribution is

$$
(3,0):8,\quad(2,0):6,\quad(0,4):4,\quad(0,2):16.
\tag{12}
$$

Choose a vertex $z$ of type $(0,4)$. It has no neighbor in $H$ and
exactly four neighbors in $K$. Each of those neighbors has $d_H=3$.
Equation (5), with $L=H$, gives

$$
12=3\cdot4+
3|N_G(z)\cap T_{30}|+2|N_G(z)\cap T_{20}|.
$$

Thus $z$ has no neighbor in either positive-$x$ exterior type. Its four
remaining neighbors must lie in $T_{04}\cup T_{02}$, because (12)
exhausts all exterior vertices. Every neighbor of $z$ therefore has
$d_K\ge2$: the four in $K$ have $d_K=t=2$, and the other four have
$d_K=4$ or $2$. Applying (5) with $L=K$ yields the contradiction

$$16=(A d_K)(z)+d_K(z)\ge8\cdot2+4=20.$$

All seven cases in (1) have now been excluded.

## Consequence for D1 heavy components

`D1_COMPONENT_MINIMUM_SIZES.md` gives $|H|\ge12$ and its five
size/incidence choices when $|H|=12$. The size-twelve partner is excluded
by `D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`; the size-twenty-eight
partner and all but the displayed internal-degree choices are excluded
by `D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`. The size-twenty-four and
one size-twenty case are excluded by
`D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`, and the remaining
size-twenty case by `D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`.

This paper excludes the seven remaining size-sixteen cases. Therefore
$|H|\ne12$, and evenness of component sizes gives

$$\boxed{|H|\ge14}.$$

The earlier twelve-by-twelve exclusion already gives $|K|\ge14$ for
the generated-triangle component. Thus, conditional on the cited
reductions, both D1-associated components have size at least fourteen;
they may coincide.

## Corrections and open scope

The mixed type $(3,2)$ has minimum permissible size eight and must be
retained. Omitting it would leave a gap in the $(1,1)$ exclusion.
Section 3 handles it using the actual six-vertex component and quotient
diagonal identity.

This paper uses even component sizes but does not use $B\le2$ or the
minimum nonempty type size four in its seven-case exclusion. Those
hypotheses may remain dependencies of the earlier D1 reductions.
No all-vertex triangle-free hypothesis, graph search, LP feasibility
interpretation, or unrestricted component-preservation assumption is
used. Configurations with D1 heavy components of size at least fourteen
remain open. Independent review of this new proof is outstanding.
