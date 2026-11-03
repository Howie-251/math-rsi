# Actual triple template: canonical U-by-Ta coordinates on Z

This is a necessary labeling refinement of the full61 model, not a new
graph restriction or a triple exclusion. The first actual full61 solve
returned UNKNOWN after47.010298 CPU/48.169828 wall seconds. Its original
input and evidence remain unchanged. Subsequently the grid-normalized
run returned UNSAT and its actual LRAT certificate verified; the complete
integration is in CONNECTED_TRIPLE_EXCLUSION.md.

All symbols and the full partition refer to the same actual graph in
CONNECTED_TRIPLE_REPEAT_LOCAL.md and CONNECTED_TRIPLE_LAYER_INTERFACES.md.
In particular every z in Z has exactly one U neighbor; every z outside
F has exactly one Ta neighbor, while F has no Ta neighbor. Each Ta point
has four Z neighbors, and each U point has six Z neighbors.

## 1. F is a transversal of U, and also of V

For q in U, its full neighborhood is {u, its matched V point} plus six
Z points. None of u or its V partner is adjacent to w. The neighborhood
of w is {a,b,gamma,delta} union F. A U point has no S or T-layer neighbor.
Thus the common neighbors of w,q are exactly N(q) intersect F. The pair
w,q is a nonedge and must have a common neighbor. Each of the four U
points therefore meets F. Each of the four F points has exactly one U
neighbor, so every U point meets F exactly once. The argument for V is
identical. No defect-port inference or assumption on C is used.

## 2. The twenty other Z points have unique (Ta,U) coordinates

Fix t in Ta and q in U. They are nonadjacent. The complete neighbor
classes of t are its parent a, one Tb point, one Tc point, one Td point,
and four Z points. The neighbor classes of q are u, its V partner and
six Z points. No non-Z point can be a common neighbor: t is adjacent to
neither u nor V, and q is adjacent to neither a nor a T-layer point.
Hence a real common neighbor of t,q must be in Z. It cannot be in F,
because F has no Ta neighbors.

There are5*4=20 pairs (t,q), each with at least one such common neighbor.
There are exactly20 points of Z outside F, and each has exactly one Ta
and one U neighbor. Thus each belongs to exactly one of these20 cells.
Every cell is occupied and the total is20, so every cell contains exactly
one point. This is an actual adjacency bijection, not an independent
quotient or an assumed equitable partition. The same reasoning works
for (Ta,V), but its induced maps must remain variable when using the
(Ta,U) labeling below.

## 3. Compatible normalization without losing any graph

Keep all seven core labels and the original Ta/Tb/Tc/Td matching labels.
In Case I, put r,s at Z[0],Z[1] and label the other two F points Z[2],Z[3];
in Case II choose any order of F. Label U[j] as the unique U neighbor
of F[j]. Then label V[j] by the actual matched partner of U[j]. This
preserves the original U/V identity matching; U/V labels had no other
fixed relation to Ta or to F. It does not fix any V-to-F permutation.

For each i=0..4 and j=0..3, label the unique (Ta[i],U[j]) common Z point
as Z[4+4*i+j]. These twenty labels are available independently of F and
the T layers. Consequently the following adjacency entries can all be
fixed, with every other incidence still as in the full61 model:

```text
A[U[j], F[k]] = 1 iff j=k;
A[U[j], Z[4+4*i+k]] = 1 iff j=k;
A[Ta[i], Z[4+4*h+j]] = 1 iff i=h.
```

The original clauses already give A[Ta,F]=0. These choices simultaneously
preserve the four previously normalized matchings, both port cases and
both gamma/delta triangle alternatives. Tb-to-Tc/Td permutations, every
V-to-Z incidence, T-to-Z incidences not fixed above, and all permitted
internal Z edges remain variable. In particular this is not a choice
of C or sigma, nor an automorphism assumption.

Every hypothetical original triple target therefore has this stronger
canonical labeling. Any satisfying graph still satisfies all original
degree8 and real diameter2 clauses. This proves bidirectional graph
coverage up to labels, subject to the inherited local reduction.

## 4. Bounded implementation consequence

Use a separate output directory and the reviewed full61 emitter/runner
without modifying or rerunning its completed input. Add only the proved
fixed adjacency entries above. The genuine change is removal of the
previous free U/F and twenty-point Z labeling choices; no claim of a
measured speedup is made. Generate once and, after checking this delta,
run one equally bounded trial. An UNKNOWN result remains no exclusion;
the partial LRAT from the first UNKNOWN is not an UNSAT certificate.
