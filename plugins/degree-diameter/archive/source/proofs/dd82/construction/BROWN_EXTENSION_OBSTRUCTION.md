# Proof Package: at least eight deleted old edges in a Brown57-to-58 extension

## Claim
Fix the explicit Brown graph $B$ of `BROWN57_PROOF.md`. Let $G$ be any graph on $V(B)\cup\{x\}$ satisfying the original degree-$8$, diameter-at-most-$2$ conditions. No old edge is presumed fixed: arbitrary old-edge deletion and addition are allowed. Then
$$|E(B)\setminus E(G)|\ge8.$$
The number of added edges between old vertices equals the number of deleted old edges. This is a restriction on extensions of this particular labeled $57$-point substructure, not a nonexistence theorem for all $58$-point graphs.

## Status
PROVABLE AS STATED, with explicit finite Brown-graph structural premises checked by integer computation. The argument after those premises is a uniform paper proof. No full $58$-point graph has been found, and the bound $8$ is not asserted attainable.

## Assumptions and notation
$C$ is the set of the $8$ degree-$7$ vertices of $B$. Let $I$ be the old vertices outside $C$ with no neighbor in $C$, and let $E=V(B)\setminus(C\cup I)$. The symbol $E$ here denotes a vertex set, while $E(B)$ denotes an edge set. Write $R=E(B)\setminus E(G)$, $r=|R|$, and $S=N_G(x)$.

The exact finite premises are:
- $|I|=21$, $|E|=28$; every vertex outside $C$ has degree $8$.
- $C$ is independent, and no $C$–$I$ edge exists.
- Every edge of $B$ lies in at most one triangle.
- Each vertex of $I$ lies in exactly $4$ old triangles.

`triangle_edit_obstruction.py` checks these premises from the explicit edge list, without importing the generator. The identity $C$ independent also follows from the projective proof: two distinct isotropic orthogonal vectors would span a two-dimensional totally isotropic subspace in a nondegenerate three-dimensional space, impossible because that subspace would lie in its one-dimensional orthogonal complement.

## Dependency Map
1. A radius-two count forces every vertex of $G$ to have degree $8$.
2. A second radius-two count bounds every triangle count in $G$ by $3$.
3. Destroying the excess old triangles forces $r\ge7$.
4. Equality $r=7$ forces a degree-deficit pattern that cannot provide two-step coverage from $x$.

## Proof
**Step 1: regularity and edge balance.** A vertex of degree at most $7$ can reach at most $1+7+7\cdot7=57$ vertices within two steps. Since $|V(G)|=58$, $G$ is $8$-regular. Therefore $|E(G)|=232$, $|S|=8$, and exactly $224$ edges of $G$ lie between old vertices. Since $|E(B)|=224$, the old-edge addition and deletion counts are equal.

**Step 2: local triangle budget.** Fix $v\in V(G)$ and let $t_G(v)$ be its triangle count. The $8$ neighbors have $56$ incidences available after excluding their edges back to $v$. Edges between those neighbors consume $2t_G(v)$ of these incidences. Even if all remaining incidences reach different new vertices, the two-step ball has size at most $65-2t_G(v)$. Thus $58\le65-2t_G(v)$ and $t_G(v)\le3$.

**Step 3: seven deletions are necessary.** Every $i\in I$ initially lies in $4$ old triangles. At least one of these must have an edge in $R$, because adding edges cannot remove a surviving triangle. Every deleted old edge destroys at most one old triangle. A triangle contains at most three vertices of $I$. The $21$ required vertex incidences therefore imply $21\le3r$, giving $r\ge7$.

**Step 4: characterize equality.** Suppose $r=7$. Every inequality in Step 3 must be tight. Exactly seven distinct old triangles are destroyed; each contains three vertices of $I$; and these triangles partition $I$. Each is destroyed by exactly one deleted edge. Consequently the seven deleted edges form a matching on fourteen vertices of $I$.

After these deletions the old graph has degree $7$ on the set $D$ consisting of $C$ and those fourteen internal endpoints, and degree $8$ at its remaining $35$ vertices. Thus $|D|=22$, every deficit is exactly one, and no old vertex outside $D$ can receive any new edge. All vertices of $S$ belong to $D$ and use their sole remaining incidence on $x$. The seven added old edges are therefore a matching on $D\setminus S$. In particular **no added old edge touches $S$**.

**Step 5: reachability contradiction.** For each $c\in C$, a path $x-s-c$ would require $s\in S\subseteq D$ and an old edge $sc$: new old edges cannot touch $S$. But $D\subseteq C\cup I$, and $c$ has no neighbor in $C\cup I$. Hence the diameter condition forces $x$ adjacent to every $c\in C$. Since both $S$ and $C$ have size eight, $S=C$. No internal vertex $i\in I$ is adjacent to $x$ or has a neighbor in $S=C$. Thus $x$ and $i$ have no path of length at most two, a contradiction. Therefore $r\ge8$. ∎

## Exact finite work and independent diagnostic
`triangle_edit_obstruction.py` finds $56$ old triangles: $14$ of type $III$ and $42$ of type $IEE$. It enumerates all $\binom{14}{7}=3432$ seven-triangle subsets and finds exactly two partitions of $I$. Consequently all equality-case deletion patterns are the $2\cdot3^7=4374$ choices stored in `seven_edge_deletion_patterns.json`. This is only a classification of a necessary equality case.

The C++ program `r7_domination.cpp` separately asks, for every pattern, whether any subset of at most eight deficit vertices dominates all $57$ old vertices after deletion. Its branch search returned no such subset for all $4374$ patterns in $0.077$ seconds on one CPU, with $17720$ search nodes. The CSV and JSON summary are retained. This computation prompted the uniform Step 5 argument and is not needed as a trusted global nonexistence oracle.

An earlier weaker closed-neighborhood count proving $r\ge3$ is retained in `insertion_obstruction.py` and its JSON for reproducibility; the present result supersedes it.

## Next meaningful construction task
For $r\ge8$, degree deficits can overlap and some added old edges may touch $S$. The matching simplification of Step 4 must therefore be rederived per deletion pattern. A useful next representation fixes a deletion set, computes exact deficits, and solves for all added edges and the new-vertex neighborhood in the same true graph; it must verify every old–old pair and every $x$–old pair. No $r\ge8$ family has been excluded here.

## Open Risks
The finite Brown premises and paper argument are not yet Lean-compiled. The result does not claim novelty, does not decide arbitrary $58$-point graphs, and does not close the full Brown extension family.
