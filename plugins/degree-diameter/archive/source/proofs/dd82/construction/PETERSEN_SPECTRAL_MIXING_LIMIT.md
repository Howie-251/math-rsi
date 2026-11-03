# Petersen spectral mixing: exact identities and the remaining gap

## Result of the bounded analysis

No positive lower bound for the cycle energy was established in this round. The exact identities below show that a diameter-two construction must mix the two nonconstant Petersen eigenspaces substantially; imposing $DC=CD$ would exclude every target. They also identify precisely the mixed terms not controlled by the current trace and gap information.

No graph search, solver run, or formalization was performed for this note.

## Setup

Let $A=D+C$, where $D$ is the adjacency matrix of six disjoint Petersen graphs and $C$ is the adjacency matrix of the fifteen cross-fiber matchings. Let $U$ be the six-dimensional space of vectors constant on each fiber, and $W=U^\perp$. Both $D$ and $C$ preserve these spaces. On $U$, $D=3I$ and $C$ is the adjacency matrix of $K_6$. On $W$,

$$D^2+D=2I,\qquad \operatorname{spec}(D)=1^{30},(-2)^{24}.$$

For a pair of fibers, let $q_{ij}$ count the edges common to the source Petersen graph and the pulled-back target Petersen graph under its matching. Put $Q=\sum_{i<j}q_{ij}$. For a target, the proved necessary matching constraint gives $0\leq q_{ij}\leq5$, hence $0\leq Q\leq75$.

## 1. Commutativity is impossible for a target

The diagonal blocks of $C^2$ are $5I_{10}$, so

$$\operatorname{tr}(D^2C^2)=5\operatorname{tr}(D^2)=900.$$

For one ordered fiber pair, the corresponding contribution to $\operatorname{tr}(DCDC)$ is $2q_{ij}$. Counting both orientations gives

$$\operatorname{tr}(DCDC)=4Q.$$

Consequently

$$\boxed{\|DC-CD\|_F^2=2\operatorname{tr}(D^2C^2)-2\operatorname{tr}(DCDC)=1800-8Q.}$$

For any target this implies

$$1200\leq\|DC-CD\|_F^2\leq1800.$$

The entire commutator lies in $W$, because $D$ is scalar on $U$. Thus neither commutativity nor a small commutator is a valid simplifying construction assumption. This quantitative restriction is a reformulation of the existing matching-overlap information, not an independent family exclusion.

## 2. Exact block energies on the two Petersen eigenspaces

Choose an orthonormal decomposition $W=W_+\oplus W_-$, where $D$ equals $1$ on $W_+$ and $-2$ on $W_-$. Write

$$C|_W=\begin{pmatrix}X&Z\\Z^\mathsf T&Y\end{pmatrix},$$

with $X$ of size $30$ and $Y$ of size $24$. The zero diagonal fiber blocks of $C$ give

$$\operatorname{tr}X=\operatorname{tr}Y=0.$$

Furthermore $\operatorname{tr}_W C^2=270$ and $\operatorname{tr}_W(DC^2)=-90$. The first subtracts the $K_6$ contribution $30$ from $\operatorname{tr}C^2=300$. For the second, $\operatorname{tr}(DC^2)=5\operatorname{tr}D=0$ on the full space, while the contribution on $U$ is $3\operatorname{tr}(K_6^2)=90$.

Therefore

$$\|X\|_F^2+\|Z\|_F^2=150,\qquad
\|Y\|_F^2+\|Z\|_F^2=120.$$

The spectral separation between $1$ and $-2$ gives $\|[D,C]\|_F^2=18\|Z\|_F^2$. Combining the identities yields

$$\boxed{\begin{aligned}
\|Z\|_F^2&=100-\frac49Q,\\
\|X\|_F^2&=50+\frac49Q,\\
\|Y\|_F^2&=20+\frac49Q.
\end{aligned}}$$

In particular the squared norm of the cross-eigenspace block lies between $200/3$ and $100$ for a target. Neither within-eigenspace block can vanish.

## 3. Why the spectral gap alone does not close the problem

On $W$, the defect matrix is $B=A^2+A-7I$. Its blocks are

$$B_{++}=X^2+ZZ^\mathsf T+3X-5I,$$
$$B_{--}=Y^2+Z^\mathsf TZ-3Y-5I,$$
$$B_{+-}=XZ+ZY.$$

The target spectral condition is exactly $-5I\preceq B\preceq5I$, equivalent to $\operatorname{spec}(A|_W)\subseteq[-4,-2]\cup[1,3]$.

It does not force the cross block to vanish or become small. Already the two-dimensional blocks

$$D_0=\begin{pmatrix}1&0\\0&-2\end{pmatrix},\qquad
C_0=\begin{pmatrix}0&t\\t&0\end{pmatrix}$$

have

$$\operatorname{spec}(D_0+C_0)=\left\{\frac{-1\pm\sqrt{9+4t^2}}2\right\}.$$

For every $0<t\leq\sqrt{10}$ these lie in the two required intervals, despite a nonzero commutator. This example addresses the gap implication only; it is not asserted to be a complete graph or to satisfy every cover constraint.

The exact cycle energy from `PETERSEN_CYCLE_ENERGY.md` becomes

$$4E=\|B_{++}\|_F^2+\|B_{--}\|_F^2+2\|XZ+ZY\|_F^2-270.$$

The identities in Section 2 fix second moments. They do not fix the cubic terms in $X,Y$, the alignment of $X^2$ with $ZZ^\mathsf T$, or $XZ+ZY$. No strict inequality making the right side positive was derived. Treating these terms as independent would discard the actual permutation and fiber constraints; treating the gap as forcing commutativity would be false.

The remaining obligation is therefore specific: obtain a valid lower bound of at least $274$ for the displayed sum of three squared norms, or an incompatible integral/cover condition at its equality value $270$. The current argument supplies neither. It leaves the exact-energy construction experiment as the directly justified next step.
