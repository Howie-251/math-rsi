# The minimum-eight branch: shorter general argument

The starting hypotheses and local certificates are exactly those of `context/propertyb34-hour1-20261013/low-math/EIGHT.md`. Let L be the degree-eight set, |L|≥10. Assume the strict local alternatives have not already yielded a coloring. Codegree≥4 is excluded by strict doubles; codegree3 is excluded by the same general incidence argument in the original note. Consequently every low-low pair has codegree1 or2.

Let R(x,y) mean x≠y and λ(x,y)=1. The existing four-lock residue implies triangle-freeness, no induced P3+P1, the common-edge property for C4, and zero common-four multiplicity for a claw and an independent four-set. The C4 and claw statements imply that two distinct vertices have at most two common unit neighbors: two C4-containing actual edges sharing a unit pair must coincide; three shared unit neighbors would then put a claw quadruple in that edge, contradicting its zero count.

## Uniform universal-vertex argument

If x has at least three unit neighbors, select three distinct ones a,b,c. They are pairwise nonadjacent. Suppose z is a different low point not adjacent to x. Then z is different from a,b,c. It must be adjacent to at least two of them: otherwise x and two missed neighbors, together with z, form P3+P1. It cannot be adjacent to all three because x,z would have three common unit neighbors. If it is adjacent to exactly two, those two together with z and the missed third neighbor form P3+P1 again. This contradiction proves that x is universal.

If there is no universal point, every unit degree is at most2. Suppose b has two neighbors a,c. Every other low point must be adjacent to at least one of a,b,c, by no P3+P1. It cannot be adjacent to b, whose two neighbors are already a,c. Each of a,c has at most one further neighbor, so there are at most two other low points. This gives |L|≤5, a contradiction. Therefore the unit graph is either a universal star or has maximum degree at most1. This argument does not enumerate graphs and does not use the no-2K2 condition.

## Rule out the star by one leaf's incidence capacity

Let x be its center and p any leaf. Put S=L minus {x,p}; then |S|≥8 and λ(p,z)=2 for every z∈S. Thus Σ_(z∈S) λ(p,z)=2|S|≥16.

Any edge through p contains at most two members of S: three would form an independent four-leaf set with p in one common edge. Any edge through both p and x contains at most one member of S: two would form the claw quadruple x,p,a,b in a common edge. There are d(p)=8 edges through p and λ(p,x)=1 of them also contain x. Counting the actual p-to-S incidences gives

    Σ_(z∈S) λ(p,z) + λ(p,x) ≤ 2 d(p) = 16.

The left side is at least17. This directly excludes the star, without an equality case or a global pair-incidence sum.

## Rule out maximum unit degree at most1

Choose any p∈L and put S=L minus {p}, so |S|≥9. All λ(p,z) are1 or2, and at most one equals1. Thus Σ_(z∈S) λ(p,z)≥2|S|−1≥17.

Every edge through p contains at most two other low points. Otherwise four low points including p lie in a common edge. In the residual table a positive common-four count forces C4, in which p has two unit neighbors, contradicting its unit degree at most1. Hence the actual edge capacities give Σ_(z∈S) λ(p,z)≤2d(p)=16. This is the final contradiction.

These replacements remove the need for Σ_E choose(|E∩L|,2), the star equality analysis, and the proof that the whole unit graph has at most one edge. They retain the actual four-lock classification and actual edge binding. The Lean declarations in `UnitGraph.lean`, `Incidence.extra_capacity`, `TwentyEightGraph.lean`, and `TwentyEight.lean` implement these exact obligations; their current acceptance is determined by the corresponding build/audit logs, not by this note.
