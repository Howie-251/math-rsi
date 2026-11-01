# Weighted conflict graphs force complete components

## Statement

Let $W$ be a finite graph with nonnegative integer pair weights, with zero diagonal, such that the sum of weights incident with each vertex is an integer $D\ge3$. Let $F$ be its simple support graph, let $n=|V(F)|$, let $a=\alpha(F)$, and let $s$ be the number of connected components of $F$ isomorphic to $K_{D+1}$. Then

$$a\ge s+\left\lceil\frac{n-s(D+1)}D\right\rceil=\left\lceil\frac{n-s}D\right\rceil,$$

and consequently $s\ge n-Da$. Every such complete component has all its internal weights equal to one and all weights to the other vertices zero.

## Proof and external ingredient

Positive weights are integers, so the ordinary degree in $F$ is at most $D$. Delete its $s$ complete components. The remaining graph has maximum degree at most $D$ and no complete component on $D+1$ vertices. Brooks' coloring theorem, for $D>2$, gives a proper coloring of this remainder with $D$ colors. A largest color class is independent and has at least $\lceil(n-s(D+1))/D\rceil$ vertices. Add one vertex from each deleted component. There are no support edges between different components, so their union is independent. This proves the first inequality. The equality follows by moving the integer $s$ inside the ceiling. Since $a$ is an integer, $a\ge\lceil(n-s)/D\rceil$ implies $Da\ge n-s$, giving the claimed bound on $s$.

Inside a $K_{D+1}$ component each vertex already has $D$ positive integral incident weights. Their sum is exactly $D$, so every one equals one. The absence of support edges to the complement is the definition of a component. This proves the last assertion. ∎

The imported theorem is R. L. Brooks, “On colouring the nodes of a network,” *Proceedings of the Cambridge Philosophical Society* **37** (1941), 194–197. The original statement and its finite-graph proof were read in the reprint, Appendix A, pp. 537–539 (PDF pages 1–3): [original-paper reprint](https://www.tu-ilmenau.de/fileadmin/Bereiche/MN/komgra/BackMatterSMM.pdf). Its stated condition is maximum degree at most $D>2$ with no $K_{D+1}$ component. This note imports that theorem; it does not claim a new proof of Brooks' theorem.

## Application to the 25-point all-seven-degree branch

For a pair-covering five-uniform $H$ on 25 vertices in which every degree is seven, set $w(u,v)=\lambda_H(u,v)-1$. Pair coverage makes these weights nonnegative integers, and

$$\sum_{v\ne u}w(u,v)=4d_H(u)-24=4.$$

Here $D=4$ and independent sets of $F$ are exactly sets of vertices with all pair codegrees one. If their maximum size is $a=6$, there is at least one $K_5$ component. If $a=5$, there are at least five such components, so all 25 vertices partition into five $K_5$ components. In either case each such five-set $G$ satisfies $\lambda_H(u,v)=2$ inside $G$ and $\lambda_H(u,z)=1$ for $u\in G,z\notin G$.

Thus the single-group inventory and one-external-star representation may be used for an actual $G$ even in the $a=6$ branch. A proof must still check every numerical catalogue assumption. The later $a=5$ two-external-star caller uses the partition of *all* vertices into five groups, and cannot be transferred from this lemma alone. This result supplies an actual structural input; it does not finish $a=6$ or the 25-point theorem.
