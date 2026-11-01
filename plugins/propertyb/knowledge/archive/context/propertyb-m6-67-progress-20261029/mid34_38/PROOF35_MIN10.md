# 35 vertices, minimum degree ten: complete candidate

**Theorem.** Every finite simple six-uniform pair-covering hypergraph with exactly $66$ edges, $35$ vertices, and actual minimum degree ten is two-colorable.

**Status.** Complete computer-assisted proof candidate. Independent replay and cross-family review of this final branch are pending. This proof uses the same exact conditional permutation failure mechanism and valid bad-pair deletion imported in `PROOF36_38.md`. It adds no assumption to the original Property B target: pair coverage and the vertex/degree case are internal counterexample branches.

Let $H$ be this same actual hypergraph. Write $d(x)$ and $\lambda_{xy}$ for its actual degrees and codegrees. Then

$$\sum_xd(x)=396,\qquad d(x)\ge10,\qquad
\sum_{y\ne x}(\lambda_{xy}-1)=5d(x)-34.\tag{1}$$

The total degree excess above ten is $396-35\cdot10=46$. Every degree-ten vertex has at most sixteen nonunit partners, and hence at least eighteen unit-codegree neighbors.

## 1. Complete accepted numerical configurations

`CERT35_MIN10.json` contains only the 102 successful records used in this proof; `finalize_min10_35.py` extracts them from the actual completed calculations and fixes their successful labels, positions, multiplicities and exact rational bounds. These are three complete input domains.

**A. A unit pair of degree-ten vertices.** Suppose $x,y$ both have degree ten and $\lambda_{xy}=1$. The unit neighbors of $x$ other than $y$ number at least seventeen, whereas $y$ has at most sixteen nonunit partners. Thus some actual $z$ has $\lambda_{xz}=\lambda_{yz}=1$. Its degree $f$ lies in $[10,56]$ by the total degree sum. The actual unit triple has one of the two usual complete trace patterns. Nonnegative empty-trace multiplicity imposes $f\le49$ in the separate-edge pattern, and $f\le48$ in the one-triple-edge pattern. Thus precisely $40+39=79$ necessary nonnegative degree/trace types remain. All have strict failure bounds, extracted from `ADAPTIVE_COMPONENT.json`. The broader historical generator also recorded fifteen negative-multiplicity tuples; they are impossible actual inputs and are excluded from the final certificate.

**B. A degree-ten vertex with two degree-eleven unit neighbors.** Here the degrees are $(10,11,11)$, the two codegrees incident to the degree-ten point are one, the other codegree $\lambda$ ranges from one to eleven, and the triple intersection multiplicity $\tau$ is zero or one. Exactly 21 of these tuples have nonnegative actual trace multiplicities; the excluded tuple $\lambda=11,\tau=0$ would require a negative singleton multiplicity. All 21 have strict bounds in `TWO_ARMS35.json` and are copied into the final certificate.

**C. A degree-twelve common unit center of a codegree-two pair of degree-ten points.** Label the degree-twelve center as zero and the degree-ten points as one and two. The codegrees are $\lambda_{01}=\lambda_{02}=1$, $\lambda_{12}=2$. There are exactly two actual trace patterns, indexed by $\tau\in\{0,1\}$:

$$\ell_7=\tau,\quad\ell_3=\ell_5=1-\tau,\quad\ell_6=2-\tau,$$

$$\ell_1=10+\tau,\quad\ell_2=\ell_4=7+\tau,\quad\ell_0=38-\tau.$$

The actual completed calculation `LOW_PAIR_MIN10_35.json` gives

$$\tau=0:\quad U=185588/186093<1,\quad p=(17,18,19),$$

$$\tau=1:\quad U=1644827/1654160<1,\quad p=(17,16,18).$$

The lock positions are indexed by the stated labels. These two rows also appear in the final certificate. Each strict configuration produces an actual coloring, regardless of how those actual locks were selected.

## 2. Low codegree-two partner

Assume for contradiction that $H$ is not two-colorable. Domain A implies that no degree-ten point has a degree-ten unit neighbor. Domain B implies that no degree-ten point has two degree-eleven unit neighbors.

Fix any degree-ten point $x$ and let $A$ be its unit-neighbor set, of size $u$. Then $u\ge18$. Every member of $A$ has degree at least eleven and at most one has degree eleven. Therefore the degree excess contributed by $A$ is at least $2u-1$. Since the entire excess is 46,

$$18\le u\le23.$$

Let $l$ be the number of actual partners $y$ with $\lambda_{xy}=2$. There are $34-u$ nonunit partners in total. The other $34-u-l$ partners have codegree at least three. By the exact row excess in (1),

$$16\ge l+2(34-u-l),\qquad l\ge52-2u.\tag{2}$$

If all these $l$ partners had degree at least eleven, their contribution to the degree excess, together with that of the disjoint set $A$, would be at least

$$(2u-1)+l\ge(2u-1)+(52-2u)=51>46,$$

contradiction. Hence there is an actual degree-ten point $y$ satisfying $\lambda_{xy}=2$.

## 3. An actual degree-twelve common unit center

Let $P=\{z:d(z)\ge12\}$ and write $c=|P|$. Every degree-ten point has at least eighteen unit neighbors, none of degree ten and at most one of degree eleven. Thus it has at least seventeen unit neighbors inside $P$. In particular $c\ge17$. Each member of $P$ contributes at least two units of the total excess, so $c\le23$.

The actual degree-ten points $x,y$ from §2 therefore have at least

$$17+17-c=34-c\ge11$$

common unit neighbors in $P$. Suppose all those common neighbors had degree at least thirteen. Their additional excess beyond twelve is at least $34-c$. Counting the baseline excess two from every member of $P$ would then give

$$46\ge2c+(34-c)=c+34\ge51,$$

contradiction. Hence there is an actual common unit neighbor $z$ of degree exactly twelve. It satisfies

$$d(z)=12,\quad d(x)=d(y)=10,\qquad
\lambda_{zx}=\lambda_{zy}=1,\quad\lambda_{xy}=2.$$

This is precisely accepted numerical domain C. It gives an actual valid coloring of $H$, contradicting the assumption. Therefore the theorem holds. ∎

## Reproducibility and scope

The exact final certificate has 79+21+2=102 rows, all with nonnegative actual multiplicities and strict rational upper bounds. Each row records the deletion method it actually used: the first group uses the common integer avoided-subset vector with the previously proved component-support quota; the other groups use the maximum of the valid single-subset component-quota deductions. Neither method adds overlapping deductions.

`finalize_min10_35.py` regenerates the final certificate from the completed source JSON files. The probability kernel is reused from the project; this is not an independent implementation. The final proof uses none of the non-strict or interrupted fourth-lock exploratory domains documented in `STATUS35.md`.
