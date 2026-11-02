# Universal graph foundations

## Claim and status

For every finite simple undirected graph of maximum degree at most 8 with the explicit one-or-two-edge path property, its order is at most 65. If its order exceeds 57 it is 8-regular. The exact integer defect identities below then hold. Orders 65 and 64 are impossible, giving the classical weaker upper bound 63 without using historical SAT results.

Status: complete elementary paper arguments below, not yet a kernel-checked result. These are baseline results, not a claimed improvement of the published record. The exact N(8,2) problem remains open in this project. The known 63 exclusion is a separate literature/formalization obligation.

## Assumptions and notation

V is a finite set, G is simple and undirected, n=|V|, and every distinct pair has an edge or a genuine two-edge path. Write N(v) for the neighbors of v. Once regularity has been established, A is the integer adjacency matrix, I the identity, J the all-one matrix, and delta=65-n. The matrix B is defined by integer subtraction, never truncated natural subtraction.

## Strategy and dependencies

Count the root ball, then use exact adjacency identities. For the two largest orders, use a rational invariant space and an irreducible quadratic. No solver output or structural classification is used.

## 1. Root ball and regularity

For any root r, all vertices belong to {r}, N(r), or N(u) minus {r} for some u in N(r). Each latter set has at most 7 elements, since u has degree at most 8 and r is an actual neighbor. Overlaps only decrease the union cardinality, so

n <= 1 + deg(r) + 7 deg(r) = 1 + 8 deg(r).

If V is nonempty, this gives n<=65. If V is empty, n=0 gives the same bound. If n>57, each root must have degree greater than 7, hence exactly 8. Summing degrees gives |E(G)|=4n.

## 2. The defect is derived from the actual graph

Assume now n>57. Let B=A^2+A-7I-J. Symmetry follows from the symmetry of A. On the diagonal (A^2)vv=8, so Bvv=0. Off the diagonal,

Buv=|N(u) intersect N(v)| + Auv - 1 >= 0,

by the path condition. Since A1=8*1, B1=(64+8-7-n)*1=delta*1. Also AJ=JA=8J, so AB=BA. These are identities for this G, not constraints on an independently chosen matrix.

Fix r, put P=N(r), Y=V minus ({r} union P), H=G[P] and Sy=N(y) intersect P. Each Sy is nonempty. The eight vertices in P have 56 edge incidences after their root edges are removed; an H-edge uses two and a P-Y edge uses one. Hence

sum_y |Sy| = 56 - 2|E(H)|,
2|E(H)| + sum_y (|Sy|-1) = 65-n.

For an edge vu, Bvu counts its common neighbors. Every triangle through v is counted on its two edges incident with v, giving

sum_(u adjacent v) Bvu = 2t(v),
2t(v) + sum_(u outside N[v]) Bvu = delta.

In particular t(v)<=floor(delta/2). All these statements use the same actual G.

## 3. Rational quadratic lemma

Let T act on a finite-dimensional rational vector space, and suppose T^2+T-kI=0 where q(X)=X^2+X-k is irreducible over Q. The action of X as T makes the space a vector space over K=Q[X]/(q). Indeed every nonzero residue a(X) has a polynomial inverse modulo q, whose action is an inverse to a(T). Choose a K-basis. Each basis vector and its T-image form a rational basis of its two-dimensional K-line. On that line T has matrix [[0,k],[1,-1]]. Thus the rational dimension is 2a and the trace is -a for a nonnegative integer a.

For k=7 and 8 the discriminants are 29 and 33, respectively, both nonsquare rational integers. Their quadratics are therefore irreducible over Q. An integer which is a rational square is an integer square: a reduced fraction a/b with square integral forces b=1. Consecutive-square comparison verifies that neither 29 nor 33 is a square.

## 4. Exclusion of order 65

Here delta=0. Nonnegativity and zero row sums imply B=0, so A^2+A-7I=J. The rational space W of coordinate-sum-zero vectors has dimension 64, is invariant under A, and J acts as zero there. Section 3 gives trace(A|W)=-32. The complementary constant line has eigenvalue 8. Hence trace(A)=8-32=-24. This contradicts the zero diagonal of A. Thus order 65 is impossible.

## 5. Exclusion of order 64

Here delta=1. Each row of B has one entry equal to 1, all others zero; B is symmetric and has zero diagonal. Therefore its nonzero entries form 32 disjoint pairs, and its +1 eigenspace U consists exactly of vectors constant on each pair. This is a 32-dimensional rational space. Since AB=BA, A preserves U. It also preserves coordinate sums, so the subspace W=U intersect 1-perp is invariant and has dimension 31. On W, B=I and J=0. The definition of B gives A^2+A-8I=0 there. Section 3 forces dim W even, contradicting 31. Thus order 64 is impossible.

Together with the Moore bound, any original graph has order at most 63. No claim about orders 58 through 63 follows from these two exclusions alone.

## Outstanding connections

The finite relabelling bridge, Lean implementations of the counting and matrix arguments, the complete 57-point witness theorem, the precise 63-point literature proof, and all remaining 58-62 exclusions or larger constructions still require their own evidence. The paper proof above does not certify any historical RAW branch or the exact extremal value.
