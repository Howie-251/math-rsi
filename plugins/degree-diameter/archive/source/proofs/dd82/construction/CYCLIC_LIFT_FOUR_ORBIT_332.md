# Four cyclic orbits: the empty-internal 332 design is impossible

## Claim and status

**PROVABLE AS STATED.** There is no diameter-two graph on four orbits of $\mathbb Z_{15}$ with empty internal sets and cross-size matrix

$$\begin{pmatrix}0&3&3&2\\3&0&2&3\\3&2&0&3\\2&3&3&0\end{pmatrix}.$$

This excludes this quotient only. Other four-orbit quotients are separate cases, and arbitrary $60$-vertex graphs remain outside the statement.

## Notation and dependencies

Write $X=C_{01}$, $Y=C_{02}$, $Z=C_{13}$, $W=C_{23}$ for the size-three voltage sets, and $U=C_{03}$, $V=C_{12}$ for the size-two sets. Edges join $(i,t)$ to $(j,t+c)$ for $c\in C_{ij}$; reversing direction negates the voltage set.

For a set $T$, let $D(T)$ be its set of unsigned nonzero difference classes, represented by $1,\ldots,7$. Convolution identities refer to indicator functions with multiplicity. The proof uses only exact radius-two coverage, the four degree equations, and matching parity in odd cycles.

## Proof

### 1. All four same-orbit coverings are exact

At each orbit the maximum number of nonzero radius-two offsets is

$$3\cdot2+3\cdot2+2\cdot1=14.$$

Thus every size-three set has six distinct directed differences, and the three incident difference sets partition the fourteen nonzero residues. In unsigned form, if $x,y,z,w,u,v$ denote the indicator vectors of the corresponding $D$-sets, then

$$x+y+u=\mathbf1,\quad z+w+u=\mathbf1,\quad
x+z+v=\mathbf1,\quad y+w+v=\mathbf1.$$

Subtracting the sum of the last two equations from the sum of the first two gives $2u=2v$, hence $u=v$. The equations then give $y=z$ and $x=w$.

Consequently the two size-two sets have the same difference. Use an orbit-coordinate translation to write $U=\{0,d\}$, where $1\leq d\leq7$. There is a residue $t$ such that $V=U+t$. Also

$$D(X)\sqcup D(Y)\sqcup\{d\}=\{1,\ldots,7\}.$$

### 2. Cross-orbit coverage produces matchings after deleting three vertices

For the size-three pair of orbits $0,1$, the only paths of length at most two yield

$$X+Y*(-V)+U*(-Z)=J.$$

There are exactly $3+6+6=15$ representations, so this is an equality of indicator functions. Since $-V=U-d-t$, it can be rewritten as

$$X+U*T=J,\qquad T=(Y-d-t)+(-Z),$$

where the plus between the two parenthesized indicators is coefficientwise addition. Exact coverage ensures that $T$ is the indicator of a six-element set. Thus the six edges $\{s,s+d\}$, $s\in T$, form a matching covering precisely $\mathbb Z_{15}\setminus X$.

The size-three pair $0,2$ gives

$$Y+X*V+U*(-W)=J,$$

and therefore gives a matching of the same step-$d$ cycle graph covering precisely $\mathbb Z_{15}\setminus Y$.

### 3. Matching parity contradicts the difference partition

The step-$d$ graph is a disjoint union of $\gcd(d,15)$ odd cycles. Deleting $X$ leaves a graph with a perfect matching, so every one of these odd cycles contains at least one vertex of $X$.

* If $\gcd(d,15)=5$, at least five vertices must be deleted, contradicting $|X|=3$.
* If $\gcd(d,15)=3$, each of the three residue classes modulo three contains exactly one element of $X$. The same is true of $Y$. Hence neither $X-X$ nor $Y-Y$ contains a nonzero multiple of three. The difference set $U-U$ supplies only $\pm d$, leaving two of the four nonzero multiples of three uncovered. This contradicts Step 1.
* If $\gcd(d,15)=1$, multiply all coordinates by $d^{-1}$, so $d=1$. The three cyclic gaps between consecutive vertices of $X$ must be odd: each gap leaves a path of one fewer vertices, and that path must have a perfect matching. None of the gaps equals one, because $\pm1$ belongs to $U-U$ and is forbidden from $X-X$. Thus the three gaps are odd and at least three. They are distinct, because repeated gaps would repeat a directed difference of $X$. Their sum is fifteen, so they must be $3,5,7$. The same argument applies to $Y$. It follows that $D(X)=D(Y)=\{3,5,7\}$, contradicting their disjointness in Step 1.

All possibilities for $d$ have been excluded. $\square$

## Complete finite generation and independent graph check

`computations/dd82/construction/cyclic_lift60_four_orbits.py` independently implements the reduced design search. It lists all triples and their unsigned differences, obtaining twelve difference types and fourteen ordered complementary pairs $(D(X),D(Y),d)$. Normalize $0\in X,Y$ and $U=\{0,d\}$ by the three independent orbit-coordinate translations. Each difference type has six normalized triples. The pair $V$ has fifteen translates, giving

$$14\cdot6\cdot6\cdot15=7,560$$

normalized cases. For each case, all thirty possible $Z$ with the required difference type are checked through their masks $U-Z$; all thirty possible $W$ are handled likewise. Exact coverage determines at most one $Z$ or $W$, because convolution by a two-element set is invertible on an odd-order cyclic group.

The complete run used **0.155 CPU seconds** on CPU 126. No normalized case satisfies even the first exact size-three cross-cover. This finite result corroborates the analytic proof above.

The script also saves a complete diagnostic graph with

$$X=\{0,1,4\},\ Y=\{0,2,10\},\ Z=\{3,5,13\},\ W=\{8,9,12\},$$
$$U=\{0,6\},\quad V=\{4,10\}.$$

All same-orbit pairs have distance at most two. The candidate was selected by minimizing root coverage failures among one greedy completion of each normalized case; no global optimality claim is made. The independent `verify_hs_candidate.py` read its expanded edge table and confirmed $60$ vertices, $240$ edges, degree eight at every vertex, diameter three, and **165 bad unordered pairs**.

Artifacts:

* `computations/dd82/construction/cyclic_lift60_four_orbits.py`
* `computations/dd82/construction/cyclic_lift60_four_orbits.results.json`
* `computations/dd82/construction/cyclic_lift60_four_orbits.best.edges.json`
* `computations/dd82/construction/cyclic_lift60_four_orbits.best.edges.verification.json`

The verification file contains all bad pairs and their common-neighbor lists. No target graph was found. Lean formalization and cross-model review have not been performed.


## Cross-model review receipt

Root read the full argument and Gemini C2 subsequently found no mathematical gap; see [saved raw response](../../../reviews/dd82/20261011_C2_hs59_cyclic_constructions.json). Requested and CLI-selected model was gemini-3.8-flash-high/high, without independent backend attestation. This updates the earlier not-yet-reviewed snapshot; it is not a Lean certificate.
