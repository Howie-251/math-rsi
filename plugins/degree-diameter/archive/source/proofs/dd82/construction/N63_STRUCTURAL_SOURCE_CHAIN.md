# Order 63: structural source chain, 2026-10-11

## Status
**A complete self-contained order-63 proof is not yet established locally.** The missing publication has been identified and its original proof text read through a public mirror. The exact inherited theorem is located. Full figure-level reconstruction and local proof verification remain.

## Sources actually read
1. Nguyen–Miller, *Structural properties of graphs of diameter 2 and defect 2*, AKCE 7(1) (2010), 29–43, [publisher DOI](https://doi.org/10.1080/09728600.2010.12088909); [public original-paper text](https://www.scribd.com/document/897539022/Propof-Graphs-of-Diameter-2-and-Defect-2). The publisher labels the article free access, but ordinary PDF/epdf/full requests returned HTTP 403. No login was attempted. The mirror's document body was read, excluding its AI description. **The existing `nguyen_miller_2010_mirror_text.txt` is only an incomplete page extraction; do not treat it as the article.**
2. Nguyen–Miller, *Structural properties of graphs of diameter 2 with maximal repeats*, Discrete Math. 308 (2008), 2337–2341, [DOI](https://doi.org/10.1016/j.disc.2006.09.057); [complete author-profile-linked public text](https://www.academia.edu/4488728/Structural_properties_of_graphs_of_diameter_2_with_maximal_repeats). Its ordinary download endpoint was unavailable; no access restriction was bypassed.

## Precise correspondence and dependency map
For a simple diameter-two graph of maximum degree $d$, order $d^2-1$, with $d=8$:

| Obligation | Exact source |
|---|---|
| 2009 structural Theorem 2(i) | 2010 **Theorem 6(i)**, pp. 41–42: $n_0=3$, $n_{2b}=d^2-4$ |
| Its even-degree proof | 2010 **Corollary 3**, **Lemma 9**, **Theorem 4**, respectively pp. 35, 38, 38 |
| $n_{2b}$ even | Corollary 3 |
| Multiple-triangle alternative | Lemma 9: $n_0\ge6\Rightarrow(n_0,n_1,n_{2c})=(9,6,9)$ |
| Eliminate other repeat types | Theorem 4, even $d\ge6$: $(n_1,n_{2c},n_{2a})=(0,0,0)$ |
| Earlier external classification | 2010 Theorem 2, p. 33, from **2008 Theorem 2**, p. 2340: maximal-repeat induced graph is empty, $\overline K_2$, or $C_6$ |

Theorem 6(i) does **not** invoke 2010 Lemma 11, which repeats the problematic arithmetic sentence found in the 2009 version. Theorem 4 uses the four-vertex type-$2a$ components (Lemma 4), earlier neighbor classification, and Corollary 5; those earlier arguments use the maximal-repeat classification. Lemma 9 references Figure 5. Figure 4 supports the type-$2a$ case analysis. Their original graphics were not obtained in this bounded task.

The five local repeat types can be inspected directly in the **2009 published** Figure 1, printed p. 9, now saved as `miller_published_repeat_type_figure.png`. This is evidence for that version's type definitions, not a claim to have downloaded the missing 2010 Figures 4–5.

## Why the identified theorem would suffice
Regularity follows from $63>57$. The common repeat matrix is
$$B=A^2+A-7I-J,$$
so its row sums are $2$. A type-0 point is a triangle point. Theorem 6(i) therefore supplies exactly one triangle, with the remaining $60$ vertices of type $2b$.

Given that structural conclusion, the 2009 Theorem 4 proof yields local five-cycle counts $189,199,200$ for classes of sizes $3,18,42$. Double counting vertex–five-cycle incidences gives
$$5N_5=3(189)+18(199)+42(200)=12549,$$
contradicting divisibility by $5$. This is an accurate conditional chain; locating the structural theorem does not itself complete its independent proof or the Lean chain.

## A bounded replacement for one older external theorem
The 2008 Theorem 2 proof reduces its large maximal-repeat case to a regular graph $H$ of degree $k$, order $k^2+2$, and girth at least $5$, with one missing radius-two point per vertex. It invokes Brown (1967) and Bannai–Ito (1981) to exclude this. For the present parameter, its preceding pairing argument gives even $k\le8$, and its large case gives $k\ge4$. The following original specialization removes the need for that general older exclusion. It **does not prove the preceding reduction**.

### Conditional lemma
There is no simple $k$-regular graph $H$ of girth at least $5$ on $k^2+2$ vertices for $k\in\{4,6,8\}$.

### Proof
Let $M$ be the adjacency matrix and $n=k^2+2$. Girth at least five makes the radius-two vertices from any root distinct, giving exactly $1+k+k(k-1)=k^2+1=n-1$ vertices. Thus each root has exactly one vertex outside its radius-two ball. The relation of being that missing point is symmetric and partitions the vertices into pairs; let $K$ be its perfect-matching adjacency matrix. Entrywise,
$$M^2+M=(k-1)I+J-K.$$
Hence $M$ commutes with $K$ and $J$. The $K=-1$ eigenspace has dimension $n/2=k^2/2+1$, lies in $\mathbf1^\perp$, and on it $M$ satisfies
$$M^2+M-kI=0.$$
For $k=4,8$, its discriminants are $17,33$. The two irrational conjugate eigenvalues have equal multiplicities because this eigenspace is defined over $\mathbb Q$ and the restricted characteristic polynomial has rational coefficients. Its dimension would consequently be even, contradicting $k^2/2+1$ odd.

For $k=6$, $n=38$. On the $K=-1$ space of dimension $19$, the eigenvalues are $2,-3$, with multiplicities $a,b$. On the $K=+1$ space perpendicular to $\mathbf1$, dimension $18$, the equation is $M^2+M-4I=0$; its roots $(-1\pm\sqrt{17})/2$ each have multiplicity nine. The remaining eigenvalue is six. Since $\operatorname{tr}M=0$,
$$a+b=19,\qquad6-9+2a-3b=0,$$
so $a=12,b=7$. The conjugate roots have sum of cubes $-13$. Therefore
$$\operatorname{tr}(M^3)=216+9(-13)+12(8)+7(-27)=6.$$
A triangle-free simple graph has $\operatorname{tr}(M^3)=0$. This contradiction finishes the lemma. ∎

All dimensions, integrality statements, and arithmetic above are exact. No numerical eigenvalue computation was used.

## Smallest current research obligation
For a fully independent graph-theoretic route, establish the **specialized 63-point repeat classification**: every original candidate has exactly three type-0 vertices and all other vertices have type $2b$. This should be decomposed following the mapped 2010 local lemmas, reconstructing Figures 4–5 from exact adjacency relations and checking the 2008 reduction; the bounded spectral lemma above discharges only the latter's final auxiliary nonexistence step. The neighborhood theorem itself can be proved directly from $AB=BA$, without retrieving its conference source.

No claim of full self-contained closure or Lean verification is made here.
