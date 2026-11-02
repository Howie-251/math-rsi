# Four cyclic orbits: the internal-degree 2222 design is impossible

## Claim and status

**PROVABLE AS STATED.** There is no diameter-two graph on four orbits of $\mathbb Z_{15}$ with internal degree two at every orbit, cross sets of size three between the parts $\{0,1\}$ and $\{2,3\}$, and no other cross edges.

This is a pure analytic exclusion of the declared voltage family. Combined with the separate empty-internal 332 obstruction, the 0022 obstruction, and the complete quotient-capacity screen, it excludes all free four-orbit $\mathbb Z_{15}$ constructions of a $60$-vertex degree-eight diameter-two graph. The companion root-owned files are `CYCLIC_LIFT15_0022_OBSTRUCTION.md` and `computations/dd82/construction/cyclic_lift15_quotient_screen.py` with its saved results. Arbitrary $60$-vertex graphs are not excluded.

## Assumptions and notation

The internal sets are $A_i=\{\pm a_i\}$, with $1\leq a_i\leq7$. Write

$$X=C_{02},\quad Y=C_{03},\quad Z=C_{12},\quad W=C_{13}.$$

All four sets have size three. Set differences refer to cyclic residues, while convolution identities retain multiplicities. $J$ is the all-ones function. The proof uses radius-two coverage, the trace of a primitive fifteenth root, and elementary arithmetic in $\mathbb F_5$.

## Proof

### 1. Exact adjacent-orbit coverings fix every internal step

For each cross set $C_{ij}$, the only cross-orbit paths of length at most two have offsets in

$$C_{ij}+\{0,\pm a_i,\pm a_j\}.$$

There are at most $3\cdot5=15$ representations. Thus $a_i\ne a_j$ and the indicator convolution satisfies

$$C_{ij}*\{0,\pm a_i,\pm a_j\}=J.$$

No $C_{ij}$ can be a coset of the three-element subgroup $\{0,5,10\}$. Such a coset has only two nonzero differences, so the same-orbit radius-two coverage at either endpoint would have at most $5+2+6=13$ residues, less than fifteen.

Let $\zeta=e^{2\pi i/15}$. A sum of three fifteenth roots is zero only if its three roots form an equilateral triangle; therefore $C_{ij}(\zeta)=0$ would make $C_{ij}$ exactly such a subgroup coset. We have excluded this, so the convolution identity implies

$$1+\zeta^{a_i}+\zeta^{-a_i}+\zeta^{a_j}+\zeta^{-a_j}=0.$$

The field trace $c_{15}(a)=\operatorname{Tr}_{\mathbb Q(\zeta)/\mathbb Q}(\zeta^a)$ equals $1,-2,-4$ when $\gcd(a,15)=1,3,5$, respectively. These values follow by summing over the eight primitive exponents, or by the formula $\mu(15/g)\varphi(15)/\varphi(15/g)$ with $g=\gcd(a,15)$.

Taking traces gives

$$8+2c_{15}(a_i)+2c_{15}(a_j)=0.$$

The only way two values from $\{1,-2,-4\}$ sum to $-4$ is $-2+-2$. Hence $a_i,a_j\in\{3,6\}$, and their inequality forces $\{a_i,a_j\}=\{3,6\}$.

The four-edge cross-orbit graph is connected and bipartite. Interchanging its two parts if necessary, we may therefore take

$$A_0=A_1=\{\pm3\},\qquad A_2=A_3=\{\pm6\}.$$

Now each adjacent-orbit covering is convolution with the subgroup

$$H=\{0,3,6,9,12\}.$$

Consequently every cross set is a transversal of the three cosets of $H$, namely it contains one element in each residue class modulo three.

### 2. Same-orbit coverage leaves only two difference types

Use the Chinese remainder coordinates $\mathbb Z_{15}\simeq\mathbb Z_3\times\mathbb F_5$. A cross set is the graph of a function $f:\mathbb Z_3\to\mathbb F_5$. Its differences with first coordinate one have second-coordinate multiset

$$f(1)-f(0),\quad f(2)-f(1),\quad f(0)-f(2),$$

whose sum is zero. Denote the underlying set by $D(f)$.

Internal edges and internal two-step paths cover exactly $H$. Therefore, at each orbit, the two incident cross sets must have $D$-sets whose union is all of $\mathbb F_5$.

Neither $D$-set can have size one, because the other has size at most three. If one has size two, its multiset is $\{d,d,-2d\}$ with $d\ne0$, after naming the repeated element. Its set has sum $-d$, so its three-element complement has sum $d\ne0$. That complement cannot be the other $D$-set, since three distinct cyclic differences sum to zero. Thus both sets have size three.

A three-element subset of $\mathbb F_5$ with sum zero must be one of

$$P=\{0,1,-1\},\qquad Q=\{0,2,-2\}.$$

Indeed, a three-element subset of the four nonzero elements has nonzero sum, equal to the negative of the omitted element. A set containing zero has sum zero precisely when the other two elements are opposite.

The incident types must be different. Hence $X,W$ have one type and $Y,Z$ have the other.

### 3. The remaining cross-orbit covering is impossible

Because $D(f)$ contains zero and two nonzero opposite elements, $f$ has a common value $b$ at two positions and one exceptional value $b+d$ at its third position. The jump $d$ is in $\{\pm1\}$ for type $P$ and in $\{\pm2\}$ for type $Q$.

Write $b_X,b_Y,b_Z,b_W$ for the common values and $d_X,d_Y,d_Z,d_W$ for the jumps. Let $j_X,j_Y,j_Z,j_W\in\mathbb Z_3$ be their exceptional positions.

Orbits zero and one have no edge between them and no possible two-step path except through orbits two and three. Their radius-two offsets are therefore

$$ (X-Z)\cup(Y-W). $$

Consider $X-Z$. At first coordinate $r=j_X-j_Z$, the two exceptional positions align. Subtracting the common base $b_X-b_Z$, its second-coordinate set is

$$A_2=\{0,d_X-d_Z\}.$$

At each of the other two first coordinates, the exceptional positions are distinct, giving

$$A_3=\{0,d_X,-d_Z\}.$$

These sets have exactly two and three elements, respectively, because $d_X$ and $d_Z$ have opposite types. For $Y-W$ the corresponding sets are

$$B_2=\{0,d_Y-d_W\},\qquad B_3=\{0,d_Y,-d_W\},$$

with common relative translation

$$t=(b_Y-b_W)-(b_X-b_Z)\in\mathbb F_5.$$

If the two exceptional first coordinates coincide, their union has at most four elements in that coordinate class, so coverage fails.

If they differ, complete coverage in the first exceptional class requires the disjoint union $A_2\sqcup(t+B_3)=\mathbb F_5$; coverage in the other requires $A_3\sqcup(t+B_2)=\mathbb F_5$. Summing the elements in these two equalities, using $\sum\mathbb F_5=0$, gives

$$d_X-d_Z+3t+d_Y-d_W=0,$$
$$d_X-d_Z+2t+d_Y-d_W=0.$$

Subtracting yields $t=0$. But then $A_2$ and $t+B_3$ both contain zero, contradicting the required disjointness. Thus even the first nonadjacent orbit pair cannot be fully covered. $\square$

## Complete bounded design search and full-graph evidence

`computations/dd82/construction/cyclic_lift60_four_orbits_2222.py` implements the exact reduced construction. There are $125$ cross triples that are transversals modulo three. Three independent orbit-coordinate translations allow $0\in X,Y,Z$, leaving $25$ possibilities for each tree edge, while $W$ ranges over all $125$ triples.

The script checks same-orbit coverage first and then both nonadjacent orbit pairs. In **0.035 CPU seconds** on CPU 126 it examined **12,960** designs satisfying every same-orbit coverage condition. None covered even the first remaining orbit pair. The complete bad-pair histogram is saved in the results JSON; its minimum is **30** bad unordered pairs, attained by $216$ normalized designs.

One saved minimum is

$$X=\{0,1,5\},\quad Y=Z=\{0,2,7\},\quad W=\{0,10,11\},$$

with the internal steps fixed in Step 1. The independent `verify_hs_candidate.py` read the expanded edge table and recomputed all distances by BFS: $60$ vertices, $240$ edges, degree eight at every vertex, diameter three, and **30 bad pairs**. All bad pairs and common-neighbor lists are saved. This is a failed construction, not a target graph.

Artifacts:

* `computations/dd82/construction/cyclic_lift60_four_orbits_2222.py`
* `computations/dd82/construction/cyclic_lift60_four_orbits_2222.results.json`
* `computations/dd82/construction/cyclic_lift60_four_orbits_2222.best.edges.json`
* `computations/dd82/construction/cyclic_lift60_four_orbits_2222.best.edges.verification.json`

The analytic proof does not depend on exhaustive design enumeration. The three-quotient classification is documented separately by the root agent. Lean formalization and cross-model review have not been performed here.


## Cross-model review receipt

Root read the full argument and Gemini C2 subsequently found no mathematical gap; see [saved raw response](../../../reviews/dd82/20261011_C2_hs59_cyclic_constructions.json). Requested and CLI-selected model was gemini-3.8-flash-high/high, without independent backend attestation. This updates the earlier not-yet-reviewed snapshot; it is not a Lean certificate.
