# Conditional structural proof for a new complete literal clone graph

This proof applies only after the fresh literal checker binds the graph of
order {{N}}, edge count {{M}}, and {{K}} ordered new roles to the accepted
15552-point source. During interface preparation no graph has been read or
accepted. It is not a new concrete Lean certificate.

Let H be the accepted source, let c_j be the ordered old labels, and let X be
the new graph. Every H edge is retained, no two new vertices are adjacent,
and the exact neighbors of new role j are the immutable simple N_H(c_j).
These are precisely FullNeighborhoodClones.graph H center, under labels
old v -> v and new j -> 15552+j. The checker binds every edge and every role;
it does not use producer neighborhood caches or completed virtual self loops.

The already closed source target is
DegreeDiameter.Portfolio.F3Graph15552.d15_15552, in
formal/DegreeDiameter/Portfolio/F3Graph15552FullExact.lean. It gives order
15552, degree at most15, genuine Walk diameter at most4, and not at most3.
The standalone F3Graph15552FullAudit already passed; no old module is rebuilt.
The source has no isolated vertex since its order is greater than1 and it
has bounded walks between all pairs. The actual accepted source degrees
14/15 provide the same fact.

The generic closed proof is
formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean:
diameterAtMost, old_walk_bound_iff, not_diameterAtMost, degree_old, degree_new.
No assumption that centers form an independent set is required.

The genuine-walk constructions can be read directly in the literal graph:

* Old-old: retain a source walk of length at most4.
* New j to old v distinct from c_j: replace the initial endpoint c_j of a
  positive-length source walk by j; every interior vertex stays old. For
  v=c_j, choose an old neighbor w and use j-w-c_j, of length2.
* Two distinct new roles with equal centers: use j-w-k, of length2.
* New j and k with distinct centers at source distance at least2: replace
  the two endpoints of a source path by j and k. If the centers are
  adjacent, use j-c_k-c_j-k, of length3. This adjacent-center case must not
  be omitted or replaced by a claim of center independence.

All constructions use only source vertices as interior vertices. They
therefore prove D<=4 at every current prefix, without any future clone.
The old degree is d_H(v)+load(v); a new degree is d_H(c_j). The checker uses
the exact pointwise inequality <=16. A load2 at an old source-degree14
vertex must not be incorrectly rejected by imposing an extra load<=1
condition; no unstated packing restriction is needed for the Walk proof.
Every prefix has degrees no larger than the fully checked graph.

Finally collapse each new j to c_j and keep every old vertex fixed. Every
literal edge maps to a source edge. Any X Walk between old vertices of
length <=3 would give an H Walk of the same length. The source theorem
F3Graph15552FullLower.not_diameterAtMost_three uses actual old labels0 and81.
Hence this pair still has no <=3 Walk in X; the upper bound4 makes its
distance exactly4. This transfers the accepted non-D3 witness without a
new source or candidate BFS. Thus the bound is exact diameter4.

This establishes mathematical acceptance from the source theorem and the
fresh complete literal binding. A typed concrete new-center Lean goal,
its external label bridge, public priority, reviews, counts and release
remain separate ROOT tasks; this interface claims none of them completed.
