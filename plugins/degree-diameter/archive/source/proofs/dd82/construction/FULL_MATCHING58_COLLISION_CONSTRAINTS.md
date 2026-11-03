# Exact collision constraints for the full false-twin58 model

Parent run: `dd82-v3-f9-c7-20261013-0749`.
Status: **PROVABLE AS STATED** for the identities and redundant constraints
below. They do not give a whole-family contradiction. This is a bounded
pure derivation using the project formula-derivation/proof-writer workflow;
no enumeration, solver, new group action or input modification was used.

## Claim, assumptions and strategy

Assume the exact general false-twin58 representation from
[FALSE_TWINS58_EIGHT_SIX_FIBERS.md](FALSE_TWINS58_EIGHT_SIX_FIBERS.md),
Sections 1–2. Let $H$ denote the adjacency matrix of its 48-point induced
graph: eight independent fibres $G_i$ of size six, with an arbitrary
perfect matching between every pair of different fibres. Assume that
all cross-fibre pairs have a direct edge or a common neighbour in $H$.
This is precisely the remaining target obligation; it imposes no
automorphism.

Write $D=\operatorname{diag}(J_6,\ldots,J_6)$ and let $J=J_{48}$.
The invariant object is the exact one/two-step count $H^2+H$.
The dependency chain is: matching blocks and coverage imply permutation
excess blocks; these give the commuting excess matrix and upper bounds
on common neighbours; these bounds give triangle/four-cycle identities
and the root-coordinate CNF constraints. All statements are exact.

## 1. The commuting matching-cover excess

Each diagonal block of $H^2$ is $7I_6$: two distinct points of one
fibre have no common neighbour, since each other fibre is joined by a
perfect matching. For $i\ne j$ the corresponding block of $H^2+H$ is

$$
K_{ij}=Q_{ij}+\sum_{k\ne i,j}Q_{ik}Q_{kj}.
$$

Its row and column sums are seven, and coverage says $K_{ij}\ge J_6$.
Thus $E_{ij}=K_{ij}-J_6$ is an integral nonnegative matrix with every row
and column sum one, hence a permutation matrix. Put $E_{ii}=0$.
Transposition of the count blocks gives $E_{ji}=E_{ij}^{T}$. Therefore
$E$ is itself the adjacency matrix of a simple seven-regular matching
cover on the same eight fibres, and

$$
\boxed{H^2+H=7I+J-D+E.} \tag{1}
$$

The matching property also gives

$$
HD=DH=J-D,\qquad HJ=JH=7J.
$$

Equation (1) consequently implies $HE=EH$. This commutativity is an
algebraic consequence of the same $H$ and its actual excess $E$; it
must not be imposed using an independently invented excess graph.

## 2. Exact triangle and four-cycle budget

For different-fibre points $x,y$, write $c_{xy}=|N_H(x)\cap N_H(y)|$.
Every entry of the block $K_{ij}=J_6+E_{ij}$ is one or two. It follows
that

$$
xy\in E(H)\ \Longrightarrow\ c_{xy}\in\{0,1\},
\qquad
xy\notin E(H)\ \Longrightarrow\ c_{xy}\in\{1,2\}. \tag{2}
$$

Thus two triangles cannot share an edge. More precisely, the graph
induced on the seven neighbours of any vertex $x$ is a matching: the
degree there of a neighbour $y$ equals $c_{xy}\le1$.

Every four-cycle uses four different fibres. Indeed an adjacent pair
cannot share a fibre, and opposite vertices in one fibre would have two
common neighbours, contradicting their zero common-neighbour count.
Every four-cycle is induced: a diagonal edge would have the other two
cycle vertices as common neighbours, contrary to (2).

Let $t_x$ be the number of triangles containing $x$, and $q_x$ the
number of four-cycles containing $x$. Exactly $2t_x$ neighbours of $x$
in $H$ lie with $x$ in a triangle. By (1)–(2), these are precisely the
vertices in $N_H(x)\cap N_E(x)$. Each vertex in
$N_E(x)\setminus N_H(x)$ has exactly two common $H$-neighbours with $x$,
and so determines a unique four-cycle with $x$ as an opposite vertex.
Conversely every four-cycle containing $x$ arises this way. Since $E$
has degree seven,

$$
\boxed{2t_x+q_x=7.} \tag{3}
$$

In particular $t_x\le3$ and $q_x$ is one of $1,3,5,7$. If $T$ and $C_4$
count all triangles and four-cycles, summing (3) gives

$$
\boxed{3T+2C_4=168.} \tag{4}
$$

Consequently $T$ is even, $T\le48$, and $C_4\ge12$. These are necessary
counts, not an existence construction or a contradiction.

There is also a blockwise restriction: the number of $H$-edges in any
one interface that belong to triangles cannot be five. Such edges are
exactly the common entries of its two permutation matrices $Q_{ij}$
and $E_{ij}$. Two permutations agreeing on five of six positions agree
on the sixth as well. The permitted intersection counts are therefore
$0,1,2,3,4,6$.

## 3. A direct 630-clause strengthening after the existing root gauge

Use the already justified gauge $Q_{0i}=I_6$ for $1\le i\le7$.
For each coordinate $a$, let $L_a$ be the graph on the seven outer fibre
indices, with edge $ij$ precisely when $x_{i,a}$ is adjacent to
$x_{j,a}$ in $H$.

The root point $x_{0,a}$ has neighbours exactly $x_{i,a}$ for $1\le i\le7$.
Its induced neighbour graph is $L_a$, so (2) proves that $L_a$ is a
matching. Equivalently, for every outer index $i$ and coordinate $a$,

$$
\sum_{j\in\{1,\ldots,7\}\setminus\{i\}}
 x_{i,a,j,a}\le1. \tag{5}
$$

Here $x$ denotes the existing primary edge literal with reversed
indices interpreted by transpose, as in the prepared CNF.
Pairwise at-most-one encodes (5) using

$$
7\cdot6\cdot\binom62=630
$$

binary clauses and no new variable. Explicitly these are
$\neg x_{i,a,j,a}\lor\neg x_{i,a,k,a}$ for distinct $j,k\ne i$.
All are consequences of the existing matching and coverage clauses.
They may expose contradictions earlier in propagation, but there is no
measured performance claim and no new mathematical exclusion.

## 4. Optional broader same-coordinate collision bound

For distinct outer fibres $i,j$, the points $x_{i,a},x_{j,a}$ already
have $x_{0,a}$ as a common neighbour. Their total direct/two-step count
is at most two. Hence

$$
x_{i,a,j,a}+
\sum_{k\in\{1,\ldots,7\}\setminus\{i,j\}}
\sum_{c=0}^{5} z_{i,a,j,a;k,c}\le1, \tag{6}
$$

where the $z$ literals are the existing exact two-edge conjunctions.
Within a fixed middle fibre $k$ at most one of its six $z$ literals
can be true, since the matching from $x_{i,a}$ selects only one point
of $G_k$.

One inexpensive auxiliary encoding of (6) uses a fresh indicator
$g_{i,j,a,k}$ for each such middle fibre. Add the six binary implications
$z_{i,a,j,a;k,c}\Rightarrow g_{i,j,a,k}$, then require at most one among
the direct-edge literal and the five indicators. Reverse implications
are unnecessary for the projection onto the original variables: every
assignment satisfying (6) extends by setting each $g$ to the OR of its
six $z$ values, and the displayed clauses enforce (6) in every extension.
The indicators must be fresh and used only in these stated clauses.

There are $\binom72\cdot6=126$ point pairs of this form. Pairwise
at-most-one gives 630 fresh variables and

$$
126\left(5\cdot6+\binom62\right)=5670
$$

binary clauses. This is an optional second redundant strengthening,
separate from the zero-variable 630-clause rule. Neither has been added
to the running input or experimentally benchmarked.

## Boundary of the deduction

The commuting identity and collision counts expose exact consequences
of the complete model, but they do not close the full false-twin family.
For example, the local possibilities $(t_x,q_x)=(0,7),(1,5),(2,3),(3,1)$
are not individually contradictory, and their global count identity
does not establish that any of them can be assembled into the required
28 matchings. That simultaneous assembly remains the actual CNF
obligation. No additional symmetry, selected interface catalogue or
small restricted subfamily has been substituted for it.
