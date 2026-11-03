# Two shared parents: exact endpoint defect ports

Date: 2026-10-13. **PROVABLE AS STATED; reused local check and Gemini round2 accepted.**
The actual local receipt is DELTA_PORT_MODEL_AUDIT.md in
reviews/dd82/proof-checker-n61-internal-path-20261013/; full external response
is reviews/dd82/20261013_V3_n61_internal_proof_model_review.json.
This pure deduction used formula-derivation and proof-writer, without
enumeration, solver or formalization. It does not exclude this branch or
an order-61 graph.

## Scope and notation

Use the actual graph and defect matrix of
[INTERNAL_DOUBLE_PATH_LOCAL.md](INTERNAL_DOUBLE_PATH_LOCAL.md):
$A$ is a simple 8-regular diameter-two graph on 61 vertices,
$B=A^2+A-7I-J$ is nonnegative with zero diagonal and row sum four,
and $AB=BA$. All neighborhoods and defect entries below come from this
same $A$. Assume only the specified local type
$$ (\epsilon,\beta,r,h)=(0,1,2,0). $$

Write the consecutive double-path vertices as $u,v,w$, put
$T=N_A(v)$, and label
$$ U=T\cap N_A(u)=\{a,b,c\},\qquad
   W=T\cap N_A(w)=\{a,b,d\}. $$
The other four members of $T$ are called neutral parents. For the
50-point set $Z$ and its parent classes $Z_t$, let
$$ P=N_A(u)\cap Z,\quad Q=N_A(w)\cap Z,\quad
   O_t=Z_t\setminus(P\cup Q),\quad O=\bigcup_{t\in T}O_t. $$
The imported local formulas give disjoint $P,Q$, each of size five:
$P$ has one point in $Z_d$ and each neutral class; $Q$ has one in
$Z_c$ and each neutral class. Write these special points as
$p_0\in P\cap Z_d$ and $q_0\in Q\cap Z_c$. Each $O_t$ has size five.
For an ordinary point $z\in O_t$,
$$ d_{Z_s}(z)=1-1_{s=t},\qquad B[T,z]=0. \tag{1} $$

Each endpoint has a unique unit defect port in $Z$:
$$ B_{u*}=2e_v^T+e_w^T+e_x^T,\qquad
   B_{w*}=2e_v^T+e_u^T+e_y^T,\qquad x,y\in Z. \tag{2} $$
Indeed the entries at $v,w$ already use three units, and the local
commutation identity makes $B[T,u]=B[T,w]=0$.

## Result

Exactly one of the following three necessary configurations occurs.
Here a matching statement refers to actual $A$ edges unless marked $B$.

| Port locations | $A[P,Q]$ | $B[P]$ and $B[Q]$ |
|---|---|---|
| $x=q_0,\ y=p_0$ | A perfect matching on $P,Q$ | Both zero |
| $x\in O_c,\ y\in O_d$ | A perfect matching between the four neutral-parent points on each side; $p_0,q_0$ isolated in this interface | Both zero |
| $x\in O_d,\ y\in O_c$ | The same four-by-four matching description | Each consists of one unit edge: between the two $P$ neighbors of $x$, and between the two $Q$ neighbors of $y$, respectively |

In particular the two ports are distinct. The matching does not have
to preserve neutral-parent labels. These are necessary configurations,
not asserted realizable templates.

## 1. Endpoint common-neighbor equations

For $z\in Z_t$, exact counting against the neighborhoods
$N_A(u)=U\sqcup P$ and $N_A(w)=W\sqcup Q$ gives
$$
\begin{aligned}
d_P(z)&=1+1_{z=x}-1_{z\in P}-1_{t\in U},\\
d_Q(z)&=1+1_{z=y}-1_{z\in Q}-1_{t\in W}.
\end{aligned} \tag{3}
$$
Every point of $P$ has parent outside $U$, so
$\sum_{p\in P}d_P(p)=1_{x\in P}$. The left side is twice an integer.
It follows that $x\notin P$ and $P$ is independent. Applying the
second equation to $Q$ gives $y\notin Q$ and independence of $Q$.
Summing the first equation over $Q$ and the second over $P$ yields
$$ e_A(P,Q)=4+1_{x\in Q}=4+1_{y\in P}. \tag{4} $$
Thus either both ports lie in the opposite attachment sets, or both
are ordinary.

The internal defect rows at the two shared parents are saturated:
$$ B_{a*}=2e_b^T+e_c^T+e_d^T,\qquad
   B_{b*}=2e_a^T+e_c^T+e_d^T. \tag{5} $$
The local color-degree formula for $p\in P$ therefore gives
$d_{Z_a}(p)=d_{Z_b}(p)=0$; for $q\in Q$ it gives the same conclusion.
Consequently (3) at an ordinary point in $Z_a$ or $Z_b$ forces
$$ x,y\notin Z_a\cup Z_b. \tag{6} $$

## 2. Two port-location equations

For $p\in P$, the color-degree formula at $c$ is
$$ B_{cp}=d_{Z_c}(p). $$
Counting this interface from $Z_c=\{q_0\}\sqcup O_c$ and using (3)
gives
$$ \sum_{p\in P}B_{cp}
 =d_P(q_0)+\sum_{z\in O_c}d_P(z)
 =1_{x=q_0}+1_{x\in O_c}=1_{x\in Z_c}. \tag{7} $$

At $q\in Q$ the color-degree formula instead gives
$$ d_{Z_c}(q)=1+B_{cq}-1_{q=q_0}. $$
Summing over $Q$ gives $4+\sum_Q B_{cq}$. Counting the same interface
from $Z_c$, independence of $Q$ gives $d_Q(q_0)=0$, while (3) gives
$\sum_{O_c}d_Q(z)=5+1_{y\in O_c}$. Hence
$$ \sum_{q\in Q}B_{cq}=1+1_{y\in O_c}. \tag{8} $$
Row $c$ of $B$ already has unit entries at $a,b$. It has no entries
at $u,v,w$ or ordinary points; therefore its remaining two units
are precisely on $P\cup Q$. Equations (7),(8) imply
$$ 1_{x\in Z_c}+1_{y\in O_c}=1. \tag{9} $$

The exchange
$(u,w,c,d,P,Q,x,y)\mapsto(w,u,d,c,Q,P,y,x)$ preserves all premises
and equations used above. Applying (9) under this exchange gives
$$ 1_{y\in Z_d}+1_{x\in O_d}=1. \tag{10} $$

If $x\in Q,y\in P$, equation (9) forces $x=q_0$, and (10) forces
$y=p_0$. If both ports are ordinary, (9),(10) say that exactly one
port is in $O_c$ and exactly one is in $O_d$. Since the two classes
are disjoint, the other two rows of the result table follow. This
also rules out coincident ports.

Equation (3) gives all $P$–$Q$ degrees. In the first case each is
one. In the other cases $p_0,q_0$ have degree zero and every neutral
attachment point has degree one. This proves the asserted matching
descriptions without fixing any matching labels.

## 3. Internal and external defect interfaces of the attachments

For $p\in P$, the $(u,p)$ entry of $AB=BA$, using (2),(5), is
$$ B_{cp}+\sum_{p'\in P}B_{p'p}=A_{xp}. \tag{11} $$
The right side is at most one. Thus $B[P]$ is a unit matching and
its support is contained in $N_A(x)\cap P$. Summing (11), then using
(7) and (3) at $x$, gives
$$
2\sum_{\{p,p'\}\subseteq P}B_{pp'}
=d_P(x)-1_{x\in Z_c}
=2-2\,1_{x\in Z_c}. \tag{12}
$$
For the last equality, $x\notin P\cup Z_a\cup Z_b$, so (3) gives
$d_P(x)=2-1_{x\in Z_c}$. Therefore $B[P]=0$ if $x\in Z_c$;
otherwise it is the single unit edge joining the two $P$ neighbors
of $x$. Exchanging the endpoint roles gives the stated conclusion
for $B[Q]$. Together with the port locations this proves the table.

The same commutation equation gives useful exact residual interfaces:
$$
\begin{aligned}
\sum_{p\in P}B_{pz}&=A_{xz},&
\sum_{q\in Q}B_{qz}&=A_{yz} &&(z\in O),\\
\sum_{p\in P}B_{pq}&=1+A_{xq}-B_{cq} &&&&(q\in Q),\\
\sum_{q\in Q}B_{qp}&=1+A_{yp}-B_{dp} &&&&(p\in P).
\end{aligned} \tag{13}
$$
For example, the first equality follows because the other $U$
terms in $(AB)_{uz}$ vanish at ordinary $z$, whereas $(BA)_{uz}$
equals $A_{xz}$. The second displayed row has the additional term
$A_{wq}=1$; the last has $A_{up}=1$.
Thus an ordinary vertex has a unit $B$ neighbor in $P$ exactly when
it is an actual $A$ neighbor of $x$, and that $B$ neighbor is unique.
The assertion for $Q,y$ has identical quantified content.

## Remaining obligation

The three rows retain all possibilities under the stated local type.
They do not determine the remaining $A[Z]$ interfaces or the common
neighbors of arbitrary pairs of ordinary vertices. Connectedness of
$B$ has not produced a further contradiction here. In particular a
matching or defect interface satisfying the displayed equations alone
is not a complete graph construction or a realizability certificate.
