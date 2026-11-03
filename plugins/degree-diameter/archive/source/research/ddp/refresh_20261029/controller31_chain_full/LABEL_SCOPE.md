# First-discovery labels for only the eight new triangle blocks

The seven initial motif labels0,…,6 stay fixed. The eight additional disjoint K3 blocks may be freely reordered, and each of their vertices freely relabeled within its block; these operations preserve the complete candidate family.

Begin with the seven motif vertices labeled. Process assigned vertices in increasing label order. For each encountered unlabeled K3, assign it the next three consecutive labels, assigning its touched endpoint the first label. Process multiple newly touched blocks in any order. Every connected completion is eventually fully labeled. Connectivity follows from the required shared-route condition, rather than being an extra restriction.

For block b with start s_b=7+3b, its first touching parent is smaller than s_b. No earlier processed vertex can be another earlier neighbor with a smaller label, since it would have discovered the block first. Thus the first touching parent is exactly the minimum label of a neighbor outside this block; it is adjacent to s_b. The scan order also makes these minimum parent labels nondecreasing across b. Later-discovered vertices have larger labels and cannot change that minimum.

The CNF encodes exact prefixes P[b,j]=OR of edges from vertices0,…,j to block b, for0≤j<s_b. Require P[b,s_b−1]; when P[b,j] first becomes true, require edge(j,s_b). Across consecutive blocks require P[b+1,j]⇒P[b,j] for j<s_b. Larger j need no clause because the previous parent is already<s_b. No root edge or first-parent value is fixed.

This proof uses only relabelings of the eight new K3 blocks. It does not assume the overlapping initial three triangles form a triangle factor, and imports none of C33's block-capacity restrictions.
