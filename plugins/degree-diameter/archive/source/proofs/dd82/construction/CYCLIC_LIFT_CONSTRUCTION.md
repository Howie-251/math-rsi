# Cyclic lift constructions at orders 58 and 60

## Claim

1. No simple undirected graph of maximum degree at most $8$ and diameter at most $2$ on $58$ vertices admits a free cyclic action with two orbits of length $29$.
2. No such graph on $60$ vertices admits a free cyclic action with three orbits of length $20$.

These are construction-family exclusions. Neither statement excludes arbitrary graphs of the indicated order. In particular, this does not exclude cyclic lifts having a different number or length of orbits.

## Status

**PROVABLE AS STATED.** The arguments below are complete. The second proof includes an elementary finite screen of $55$ integer quotient patterns, with its full reproducible implementation in `computations/dd82/construction/cyclic_lift60.py`. The actual residual design enumeration is additional evidence, not a replacement for the analytic obstruction.

## Assumptions and notation

All groups are additive. For sets $U,V$ in a cyclic group, $U+V$ and $U-V$ denote set sum and difference. In convolution identities a set denotes its indicator function, $J$ denotes the all-ones function, and $\delta_t$ is the indicator of the single residue $t$. Set addition and convolution multiplicity are distinguished explicitly.

A voltage construction on $r$ orbits of length $m$ has vertices $(i,t)$, where $0\leq i<r$ and $t\in\mathbb Z_m$. An internal set $A_i=-A_i\subseteq\mathbb Z_m\setminus\{0\}$ joins $(i,t)$ to $(i,t+a)$ for $a\in A_i$. For $i<j$, a set $C_{ij}\subseteq\mathbb Z_m$ joins $(i,t)$ to $(j,t+c)$ for $c\in C_{ij}$. Put $C_{ji}=-C_{ij}$.

Every graph in either claim is $8$-regular: if a vertex has degree $d\leq7$, its radius-two ball has at most $1+d+7d\leq57$ vertices. Thus the degree equations below follow from the original maximum-degree assumption.

## Proof strategy and dependency map

1. Use orbitwise radius-two coverage, with commutativity to count distinct internal sums.
2. At order $58$, a cross-orbit covering has only one surplus representation. Prime-order Fourier invertibility forces a symmetric cross set, whose difference set is too small.
3. At order $60$, the degree and coverage capacities leave three quotient patterns. Exact cross-orbit coverings then exclude each pattern by difference sets or elementary Fourier identities.
4. Independently expand a finite residual design family and check its best complete graph with the existing BFS verifier.

## Proof: two orbits on 58 vertices

### Step 1. Degree and coverage capacities

Write the internal sets as $A,B\subseteq\mathbb Z_{29}$ and the cross set as $C$. The degree equations give

$$|A|=|B|=a=8-c,\qquad |C|=c.$$

As a nonzero inverse-closed subset of an odd-order group, $A$ has even size. Hence $c\in\{0,2,4,6,8\}$.

For a set consisting of $r$ inverse pairs, its sumset has at most

$$1+2r+4\binom r2=1+2r^2$$

elements: zero, the doubled elements, and the four signed sums from each two distinct inverse pairs. Consequently $\{0\}\cup A\cup(A+A)$ has at most $1+a+a^2/2$ elements.

* If $c=0$, the two orbits have no connecting edge.
* If $c=2$, the radius-two vertices in the first orbit have offsets in $\{0\}\cup A\cup(A+A)\cup(C-C)$, of size at most $25+2=27<29$.
* If $c=4$, the same bound is $13+12=25<29$.
* If $c=8$, both internal sets are empty, so a path of length at most two between different orbits must be an edge. It reaches only eight of the $29$ possible offsets.

Thus only $c=6$, $a=2$ remains. Put $A=\{\pm a_0\}$ and $B=\{\pm b_0\}$.

### Step 2. Exact cross-orbit coverage forces symmetry

Every cross-orbit offset must lie in

$$C+S,\qquad S=\{0,\pm a_0,\pm b_0\}.$$

If $b_0=\pm a_0$, this set has at most $18$ elements. Otherwise $|S|=5$ and there are exactly $30$ representations for $29$ required offsets. Thus, as convolution functions,

$$C*S=J+\delta_r$$

for one residue $r$. Replacing $C$ by $C-r$, an allowed orbit-coordinate translation, gives $C*S=J+\delta_0$.

Convolution by $S$ is invertible over $\mathbb C$. Its trivial Fourier coefficient is $5$. For any nontrivial $29$th root $\zeta$, the coefficient $S(\zeta)$ cannot vanish: the $0/1$ polynomial representing $S$ has degree at most $28$, while the minimal polynomial of $\zeta$ is $\Phi_{29}(x)=1+x+\cdots+x^{28}$; a polynomial with five nonzero coefficients is not a scalar multiple of $\Phi_{29}$.

Reflection fixes both $S$ and $J+\delta_0$. Therefore $(C-(-C))*S=0$, and invertibility implies $C=-C$.

### Step 3. The same-orbit coverage is now too small

The symmetric six-element set $C$ consists of three inverse pairs, so

$$|C-C|=|C+C|\leq1+2\cdot3^2=19.$$

The other possible offsets in the first orbit are $0,\pm a_0,\pm2a_0$, at most five elements. Since zero also belongs to $C-C$, their union has size at most $19+5-1=23<29$. This is the required contradiction.

The coefficient of $C*S$ at zero in Step 2 is **two**, not one; parity at zero alone gives no contradiction. The difference-set bound is the closing argument.

As a corollary, a $58$-vertex target has no automorphism of order $29$. Such an automorphism could only have one or two nontrivial $29$-cycles. If it had one cycle and fixed vertices, degree at most $8<29$ prevents every edge between the cycle and the fixed set, contrary to connectedness. The remaining case is exactly the two-orbit case above. $\square$

## Proof: three orbits on 60 vertices

### Step 1. Complete quotient-capacity screen

Let $a_i=|A_i|$ and $c_{ij}=|C_{ij}|$. Relabel the orbits so that $0\leq a_0\leq a_1\leq a_2\leq8$. The degree equations uniquely give

$$c_{01}=\frac{8-a_0-a_1+a_2}{2},\quad
c_{02}=\frac{8-a_0-a_2+a_1}{2},\quad
c_{12}=\frac{8-a_1-a_2+a_0}{2}.$$

Only nonnegative integer values are possible. If $a=2r+e$, $e\in\{0,1\}$, an internal set has $r$ inverse pairs and possibly the unique involution $10$. Its internal radius-two coverage is at most

$$g(a)=\min(20,1+a+2r^2+2re).$$

Thus $(g(0),\ldots,g(8))=(1,2,5,8,13,18,20,20,20)$. Every admissible quotient satisfies, for distinct $i,j,k$,

$$g(a_i)+\min(19,c_{ij}(c_{ij}-1))+\min(19,c_{ik}(c_{ik}-1))\geq20,$$

$$c_{ij}(1+a_i+a_j)+c_{ik}c_{jk}\geq20.$$

The first inequality bounds same-orbit offsets; the second counts the possible edge and two-step cross-orbit paths, allowing overcounting. Substituting the degree equations into these inequalities leaves exactly:

| Internal degrees $(a_0,a_1,a_2)$ | Cross sizes $(c_{01},c_{02},c_{12})$ |
| --- | --- |
| $(0,0,0)$ | $(4,4,4)$ |
| $(0,1,1)$ | $(4,4,3)$ |
| $(0,3,3)$ | $(4,4,1)$ |

For a transparent finite check, the numbers of nonnegative integer quotients, those surviving same-orbit capacities, and those surviving both capacities, grouped by $a_0=0,\ldots,8$, are respectively

$$ (15,10,10,6,6,3,3,1,1),\quad
(10,6,3,3,1,3,3,1,1),\quad
(3,0,0,0,0,0,0,0,0). $$

The `capacity_screen()` function exhausts precisely these finite ranges and implements the two displayed inequalities without any graph-search assumptions.

### Step 2. Exclude $(0,0,0;4,4,4)$

Write $X=C_{01}$, $Y=C_{02}$, and $Z=C_{12}$, all of size four, and $\Delta U=(U-U)\setminus\{0\}$.

Across orbits $0,1$ there are only $4+4\cdot4=20$ possible paths. Complete coverage forces all sums in $Y-Z$ to be distinct. Hence $\Delta Y\cap\Delta Z=\varnothing$. Applying the identical representation count to the other two orbit pairs gives pairwise disjoint sets $\Delta X,\Delta Y,\Delta Z$.

Same-orbit coverage in orbit zero requires $|\Delta X|+|\Delta Y|\geq19$. The other two orbits give the other two pair-sum inequalities. Adding them forces $2(|\Delta X|+|\Delta Y|+|\Delta Z|)\geq57$, while disjointness in the $19$ nonzero residues forces the sum to be at most $19$. Contradiction.

### Step 3. Exclude $(0,1,1;4,4,3)$

Now $A_1=A_2=\{10\}$, $|X|=|Y|=4$, and $|Z|=3$.

Coverage across orbits $0,2$ has exactly $4+4+12=20$ possible representations, from $Y$, $Y+10$, and $X+Z$. Hence $Y$ and $Y+10$ are disjoint, every sum in $X+Z$ is distinct, and

$$X*Z=J-Y-(Y+10).$$

The right side is invariant under translation by $10$. Convolution by $Z$ is invertible: a sum of three complex numbers of modulus one vanishes only when they form an equilateral triangle, so their ratios include a primitive cube root; ratios of $20$th roots cannot have order three. This applies to every Fourier coefficient of the three-element indicator $Z$.

Invertibility therefore implies $X=X+10$. But coverage across orbits $0,1$, again with exactly $20$ representations, requires $X$ and $X+10$ to be disjoint. Contradiction.

### Step 4. A four-term root-of-unity lemma

If $U\subseteq\mathbb Z_{20}$ has size four and $\sum_{u\in U}\zeta^u=0$ for a primitive $20$th root $\zeta$, then $U=U+10$.

To prove this, take $\xi=e^{2\pi i/5}$, so $\zeta=i\xi^{-1}$. Group the four terms by the exponent of $\xi$. This yields $\sum_{r=0}^4 d_r\xi^r=0$, where $d_r\in\mathbb Z[i]$. The minimal polynomial of $\xi$ over $\mathbb Q(i)$ is $1+x+\cdots+x^4$: indeed $\mathbb Q(i,\xi)=\mathbb Q(\zeta)$ has degree $\varphi(20)=8$ over $\mathbb Q$, hence degree four over $\mathbb Q(i)$.

Therefore all five coefficients $d_r$ coincide. At least one is zero because there are only four original terms, so they are all zero. In each residue class modulo five, the four possible powers of $i$ are distinct; a subset sums to zero exactly when it is a union of opposite pairs. Each opposite pair corresponds to exponents differing by $10$. This proves the lemma.

### Step 5. Exclude $(0,3,3;4,4,1)$

Translate orbit coordinates to make $Z=\{0\}$. Write

$$A_1=\{10,\pm a\},\quad A_2=\{10,\pm b\},\quad
S_1=\{0,10,\pm a\},\quad S_2=\{0,10,\pm b\},$$

where $1\leq a,b\leq9$. The exact cross-orbit capacities force the convolution equations

$$X*S_1+Y=J,\qquad Y*S_2+X=J.$$

In particular $X\cap(X+10)=\varnothing$. By the preceding lemma, $X(\zeta)\ne0$ for primitive $\zeta=e^{\pi i/10}$. Eliminating $Y$ and evaluating at this character gives

$$X(\zeta)(S_1(\zeta)S_2(\zeta)-1)=0,$$

and therefore

$$[2\cos(\pi a/10)]\,[2\cos(\pi b/10)]=1.$$

For $a=1,2,3,4$, the positive values in order are

$$\sqrt{\frac{5+\sqrt5}{2}},\quad
\frac{1+\sqrt5}{2},\quad
\sqrt{\frac{5-\sqrt5}{2}},\quad
\frac{\sqrt5-1}{2}.$$

The value at five is zero and the other four are their negatives in reverse order. The only two positive values with product one are those at two and four. For example, among products not using the smallest positive value, the minimum is $(5-\sqrt5)/2>1$; multiplying the smallest value by the four values gives respectively a number greater than one, one, a number less than one, and a number less than one. The negative case follows by changing both signs. Hence

$$\{a,b\}=\{2,4\}\quad\hbox{or}\quad\{a,b\}=\{6,8\}.$$

Multiplication by the unit $3\in\mathbb Z_{20}$ carries the first unordered pair to the second. Interchanging orbits if needed, it suffices to treat $a=2,b=4$.

At the order-two character, $S_1(-1)=S_2(-1)=4$, so the eliminated equation forces $X(-1)=0$; the symmetric eliminated equation forces $Y(-1)=0$. At the order-four character, $S_1(i)=0$ and $S_2(i)=4$, so $X(i)=Y(i)=0$.

If $n_j$ counts the elements of $X$ in residue class $j$ modulo four, these equations give

$$n_0=n_2,\quad n_1=n_3,\quad n_0+n_2=n_1+n_3,\quad \sum_jn_j=4.$$

Thus every $n_j=1$. The same conclusion holds for $Y$. Neither $X-X$ nor $Y-Y$ therefore contains $4,8,12,$ or $16$. Orbit zero has no internal edges, and its same-orbit radius-two offsets are exactly $\{0\}\cup(X-X)\cup(Y-Y)$. These four residues are uncovered, contradicting diameter at most two. $\square$

## Complete generator and bounded computation

The script `computations/dd82/construction/cyclic_lift60.py` implements the explicit voltage rule at the beginning of this note. For the residual $(0,3,3;4,4,1)$ design, it gauges $Z=\{0\}$ and $0\in X$, enumerates every $a\in\{1,\ldots,9\}$ and every four-element $X$ containing zero, and derives $Y$ as the complement of $X+S_1$ when this sum has sixteen distinct elements. It then checks every $b\in\{1,\ldots,9\}$ against the second exact cross-cover equation. These gauges preserve every candidate in the declared family.

One run, on CPU 126 with a 90-second outer limit, used **0.034 CPU seconds**. It found:

* $8,721$ normalized $(a,X)$ cases;
* $400$ first exact cross covers;
* $80$ designs satisfying both exact cross covers, with $20$ each for $(a,b)=(2,4),(4,2),(6,8),(8,6)$;
* $64$ expanded graphs with $250$ bad unordered pairs and $16$ with $170$ bad unordered pairs.

Every retained design was expanded and assessed using the voltage coverage formula. The best saved complete graph has

$$a=2,\ b=4,\ X=\{0,1,6,15\},\ Y=\{7,9,12,14\},\ Z=\{0\}.$$

Its full edge table is `computations/dd82/construction/cyclic_lift60.best.edges.json`. The existing independent `verify_hs_candidate.py` read that table and recomputed all graph distances by BFS. It confirmed $60$ vertices, $240$ edges, degree eight at every vertex, diameter three, and exactly **170 bad pairs**. All bad pairs and their common-neighbor lists are saved in `cyclic_lift60.best.edges.verification.json`. This is a failed construction, not a target graph.

Reproduction:

```sh
taskset -c 126 timeout 90s python3 computations/dd82/construction/cyclic_lift60.py
taskset -c 126 python3 computations/dd82/construction/verify_hs_candidate.py computations/dd82/construction/cyclic_lift60.best.edges.json
```

## Boundaries and next design

No new $58$--$61$ target graph has been obtained. Repeating searches in either excluded free cyclic family is unnecessary.

A distinct cyclic direction selected in the follow-up was **four orbits over $\mathbb Z_{15}$**, with empty internal sets and cross-size matrix

$$\begin{pmatrix}0&3&3&2\\3&0&2&3\\3&2&0&3\\2&3&3&0\end{pmatrix}.$$

The internal and cross path capacities do not exclude this quotient: same-orbit coverage has capacity $1+6+6+2=15$, and a size-two cross pair has capacity $2+9+9=20$. For a size-three cross pair the capacity is $3+6+6=15$. Six offset sets of sizes $3,3,2,2,3,3$, inserted in the voltage generator, define all $240$ edges directly. The follow-up completed the specialized design check and found a pure analytic matching-parity obstruction: see `CYCLIC_LIFT_FOUR_ORBIT_332.md`. The separate `CYCLIC_LIFT_FOUR_ORBIT_2222.md` also excludes the all-internal-degree-two quotient, with a saved complete graph having thirty bad pairs and an independent BFS check. These are completed family exclusions, so this paragraph no longer recommends repeating those searches.

## Open risks

There is no remaining mathematical gap within the stated family exclusions. The quotient screen is a small explicit finite computation rather than a Lean theorem. Formalization and cross-model review have not been performed. Arbitrary graphs and other automorphism types remain outside the claims.


## Cross-model review receipt

Root read the full argument and Gemini C2 subsequently found no mathematical gap; see [saved raw response](../../../reviews/dd82/20261011_C2_hs59_cyclic_constructions.json). Requested and CLI-selected model was gemini-3.8-flash-high/high, without independent backend attestation. This updates the earlier not-yet-reviewed snapshot; it is not a Lean certificate.
