# Three exclusions for an internal double-path vertex

## Claim

Let $A$ be the adjacency matrix of an actual simple $8$-regular graph on
$61$ vertices with diameter at most two, and let $B=A^2+A-7I-J$.
Under the inherited actual-defect conclusions stated below, if $u,v,w$
are consecutive vertices of a path in
$D=\{xy:B_{xy}=2\}$, then
$$A_{uw}=0.$$
Thus every three consecutive vertices of a $D$ path have nonadjacent
outer endpoints. In the Toeplitz notation of
[INTERNAL_DOUBLE_PATH_LOCAL.md](INTERNAL_DOUBLE_PATH_LOCAL.md), this
implies $a_2=0$ on every $D$ path with at least three vertices.

There are two additional necessary conclusions in the same local notation:
$$r h=0,\qquad h\le1,\qquad r=|U\cap W|,\quad h=|P\cap Q|.$$
Together these exclude exactly the three former local types
$$(\epsilon,\beta,r,h)=(1,0,0,0),\ (0,1,1,1),\ (0,1,0,2).$$
They do not exclude an internal $D$ vertex, the other three types,
adjacent isolated double edges, or all order-$61$ graphs.

## Status and assumptions

**PROVABLE AS STATED. Writer-checked and root-checked pure deduction;
all three exclusions passed the explicitly reused same-family provisional
[delta proof check](../../../reviews/dd82/proof-checker-n61-internal-path-20261013/DELTA_ADJACENCY_AUDIT.md).
Gemini rounds1–2 accepted the three exclusions; full round2 record is
[the saved response](../../../reviews/dd82/20261013_V3_n61_internal_proof_model_review.json).**
No computation, solver, certificate verification or formalization was
performed for these pure deductions. The earlier six-type draft remains unchanged
as a historical dependency.

We import the actual-defect facts used in the local note: $B$ is
symmetric and nonnegative integral, has diagonal zero and row sum $4$,
has entries at most $2$, commutes with $A$, and its double-support graph
$D$ is a path forest. For distinct vertices,
$$\mu(x,y)=|N_A(x)\cap N_A(y)|=1+B_{xy}-A_{xy}.$$
All neighborhoods, paths and matrices refer to this same actual $A$.

## Notation, strategy and dependencies

Use the local note's partition and notation:
$$T=N_A(v),\quad U=T\cap N_A(u),\quad W=T\cap N_A(w),$$
$$Z=V(G)\setminus(\{u,v,w\}\cup T),\quad
Z_t=\{z\in Z:N_A(z)\cap T=\{t\}\},$$
$$P=N_A(u)\cap Z,\qquad Q=N_A(w)\cap Z.$$
For any set $X$, $d_X(z)=|N_A(z)\cap X|$.

The proof assumes $A_{uw}=1$, uses the exhausted defect budgets at
$u,w$ to confine $P,Q$ to two parent classes, and compares the required
two attachment neighbors of an ordinary vertex with its available one
neighbor in those classes. The dependencies are:

1. Local sections1–2: $A_{uv}=A_{vw}=0$, $|T|=8$, $|U|=|W|=3$,
   and the commutation equation
   $\sum_{t\in T} B_{tx}=2(A_{ux}+A_{wx})$.
2. Local section3: the disjoint parent partition, sizes
   $|Z_t|=7-1_{t\in U}-1_{t\in W}$, and the ordinary-vertex rule
   $d_{Z_x}(z)=1-1_{x=t}$ for $z\in Z_t\setminus(P\cup Q)$.
3. The actual row-four defect budget and direct common-neighbor counting.
   No new symmetry or attachment normalization is needed.

## Proof

### 1. The endpoint defect rows leave no port to Z

Assume $A_{uw}=1$. Applying the local commutation equation at $x=u$
and $x=w$ gives
$$\sum_{t\in T}B_{tu}=2,\qquad
\sum_{t\in T}B_{tw}=2.$$
The entries $B_{uv}=B_{vw}=2$ already occupy the other two units
in the respective endpoint rows. The sets $T$, $\{v\}$ and $Z$
are disjoint, and $B$ is nonnegative. Therefore
$$B_{uw}=0,\qquad B_{uz}=B_{wz}=0\quad(z\in Z). \tag{1}$$
The actual defect identity at $u,w$ now gives $\mu(u,w)=0$.
Consequently $U\cap W=\varnothing$ and $P\cap Q=\varnothing$.
Since each endpoint has the other endpoint as a neighbor, three
neighbors in $T$, and degree eight,
$$|P|=|Q|=4. \tag{2}$$

### 2. Both attachment sets lie in the two neutral parent classes

Fix $z\in Z_t$ and put $p_z=A_{uz}$, $q_z=A_{wz}$. Its only
neighbor in $T$ is $t$. The complete endpoint neighborhoods are
$N_A(u)=\{w\}\sqcup U\sqcup P$ and
$N_A(w)=\{u\}\sqcup W\sqcup Q$. Thus actual common-neighbor
counting, followed by (1), yields
$$\begin{aligned}
q_z+1_{t\in U}+d_P(z)&=\mu(u,z)=1-p_z,\\
p_z+1_{t\in W}+d_Q(z)&=\mu(w,z)=1-q_z.
\end{aligned}$$
Equivalently,
$$\begin{aligned}
d_P(z)&=1-p_z-q_z-1_{t\in U},\\
d_Q(z)&=1-p_z-q_z-1_{t\in W}.
\end{aligned} \tag{3}$$
If $z\in P\cup Q$, disjointness gives $p_z+q_z=1$.
The nonnegativity of both counts in (3) forces $t\notin U\cup W$.

There are exactly two such neutral parents because $T$ has size eight
and $U,W$ are disjoint three-element sets. Denote them $a,b$. Their
classes both have size seven by the local class-size formula. Hence
$$P\cup Q\subseteq Z_a\cup Z_b,\qquad
|Z_a\cup Z_b|=14,\qquad |P\cup Q|=8. \tag{4}$$
There are exactly six ordinary vertices in
$(Z_a\cup Z_b)\setminus(P\cup Q)$.

### 3. An ordinary neutral vertex needs two neighbors but has only one

Choose one of these six vertices, say $z\in Z_a$; the argument with
$a,b$ interchanged has the same equations. Here $p_z=q_z=0$ and
$a\notin U\cup W$, so (3) requires
$$d_P(z)=d_Q(z)=1.$$
Since $P,Q$ are disjoint and both lie in $Z_a\cup Z_b$, this implies
$$d_{P\cup Q}(z)=2. \tag{5}$$

On the other hand $z$ is ordinary, so the local exact color-degree
rule gives
$$d_{Z_a}(z)=0,\qquad d_{Z_b}(z)=1.$$
By (4),
$$d_{P\cup Q}(z)\le d_{Z_a\cup Z_b}(z)=1,$$
contradicting (5). Therefore $A_{uw}=0$. The choice of consecutive
$u,v,w$ was arbitrary, so the conclusion holds throughout every
double path. In particular every distance-two adjacency coefficient
$a_2$ is zero. $\square$

### 4. A common parent and a common attachment cannot coexist

Suppose $r>0$ and $h>0$. Choose $t\in U\cap W$ and
$z\in P\cap Q$. These are distinct because $t\in T$, $z\in Z$.
The exact local identity
$$B[T]=A(K_3[U])+A(K_3[W])$$
gives total weight $2+2=4$ within the $T$ part of row $t$.
Its full row has weight four and is nonnegative, so $B_{tz}=0$.
But $u,w$ are two distinct actual common neighbors of $t,z$,
because $t\in U\cap W$ and $z\in P\cap Q$. Therefore
$$B_{tz}=\mu(t,z)+A_{tz}-1\ge2+0-1=1,$$
a contradiction. Thus $rh=0$. This step uses no guessed $T$–$Z$
defect entry and does not require fixing an overlap by relabeling.

After the first two conclusions, local equation
$r+h=1+\beta$ and the earlier complete type table leave precisely
$$ (r,h,\beta)=(0,1,0),\ (1,0,0),\ (0,2,1),\ (2,0,1). $$
In particular this second argument removes only the former
$(\epsilon,\beta,r,h)=(0,1,1,1)$ row; it does not prohibit all
positive $r$, all positive $h$, or all $\beta=1$ cases. $\square$

### 5. Two common attachments would saturate and then violate a defect row

Suppose $h\ge2$, and choose distinct $z,z'\in P\cap Q$.
For $z$, the actual local commutation equation gives
$$\sum_{t\in T} B_{tz}=2(A_{uz}+A_{wz})=4.$$
Since $B$ is symmetric, nonnegative and has row sum four, the entire
row of $z$ is already supported on $T$. In particular $B_{zz'}=0$
because $z'\in Z$ and $Z\cap T=\varnothing$.
But $u,w$ are two distinct common $A$ neighbors of $z,z'$. Thus
$$B_{zz'}=\mu(z,z')+A_{zz'}-1\ge2+0-1=1,$$
a contradiction. Therefore $h\le1$. This argument does not assume
whether $z,z'$ are adjacent and introduces no overlap normalization.
It removes the remaining former type $(\epsilon,\beta,r,h)=(0,1,0,2)$.

Combining all three conclusions with the original complete table leaves
exactly
$$ (r,h,\beta)=(0,1,0),\ (1,0,0),\ (2,0,1). \tag{6} $$
These are surviving necessary types, not assertions of realizability.
$\square$

## Remaining scope and review boundary

No hypothesis that a whole graph is triangle-free, no fixed $P/Q$
transversal overlap and no quotient or automorphism was used. The
contradiction depends on the complete endpoint defect rows and the
ordinary-vertex rule for the same original graph; it does not apply
to arbitrary independent incidence arrays. The three final displayed
$\epsilon=0$ types and the existence of internal double vertices
remain unresolved.
The local receipt is an explicitly reused, same-family provisional check,
not a fresh or independent-model review. External review remains pending;
this document does not mark that stage accepted.
