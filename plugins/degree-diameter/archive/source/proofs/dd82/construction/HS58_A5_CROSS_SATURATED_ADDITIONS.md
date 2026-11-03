# HS58 a5: 720 addition matchings for saturated cross deletions

Date: 2026-10-12. This is a complete necessary parameterization of the
old additions in the saturated cross-deletion branch, not a completion
or exclusion theorem. Assume a diameter-two eight-regular extension
of HS50 by eight vertices, exactly two original deletions and five
original-nonedge additions A. Assume both deletions are disjoint and
have an original cross edge, and that all four deletion endpoints
have their maximal two new neighbors. This last assumption follows
when H has four bad pairs; it is not automatic for H with two or three.

By `HS58_REMAINING_DELETION_ORBITS.md`, normalize
\[
D=\{01,23\},\qquad P=\{0,1,2,3\}.
\]
The sole original cross edge is 12. Use the coordinates of
`hs_augmentation.py`: U(i,j)=5i+j and V(k,l)=25+5k+l, with all
coordinates modulo 5. U tracks have cycle step 1, V tracks step 2,
and U(i,j) is adjacent to V(k,l) exactly when l=ik+j.

Write B_x for the new neighbors of old x and let tau=(0 1)(2 3).
The proved zero-set rule `HS58_SATURATED_DISJOINT_ZERO_SET.md` gives:
A is a matching avoiding P; its ten endpoints Z are exactly the
zero-port vertices; Q[Z] is independent; and each q in Z has exactly
one Q neighbor s(q) in P. Its A partner q' satisfies
s(q')=tau(s(q)). For clarity, the exclusion of two-neighbor zero
cells uses the cross edge 12: cells {1,2} have no common neighbor,
{0,2} and {1,3} have their unique common neighbors 1 and 2 inside P,
and a zero in {0,3} would require a partner in the empty {1,2} cell.

The coordinate definition now leaves only twenty possible zeros.
Old vertex 4 has two P neighbors, 0 and 3; the other U vertices
outside P have no P neighbor. Vertex V(k,l) has a P neighbor exactly
when l is in {0,1,2,3}, and that neighbor is l. Consequently
\[
Z\subseteq\{V(k,l):k\in\mathbb Z_5,\ l=0,1,2,3\}.
\]
Each of the five V tracks is a C5, so Q-independence allows at most
two zeros per track. There are ten zeros in total, forcing exactly
two in each. Among {0,1,2,3}, the independent pairs for cycle step
2 are exactly {0,1}, {1,2}, {2,3}.

Let their numbers of tracks be n01,n12,n23. The four cell sizes are
\[
(|Z_0|,|Z_1|,|Z_2|,|Z_3|)
=(n01,n01+n12,n12+n23,n23).
\]
Partner balance |Z0|=|Z1| and |Z2|=|Z3| forces n12=0. Therefore
choose a subset I of the five tracks, with complement J. Precisely
the zeros V(k,0),V(k,1) occur on each k in I, and precisely
V(k,2),V(k,3) occur on each k in J. All additions are then
\[
\begin{split}
A={}&\{\{V(k,0),V(\pi(k),1)\}:k\in I\}\\
 &\cup\{\{V(k,2),V(\sigma(k),3)\}:k\in J\},
\end{split}
\]
where pi and sigma are arbitrary permutations of I and J. These
are original nonedges: different V tracks have no edges, and the
same-track label differences are 1 rather than 2. The choices give
32 zero sets and exactly
\[
\sum_{k=0}^5\binom5k k!(5-k)!=6\cdot5!=720
\]
distinct labeled addition matchings. Every saturated candidate is
represented; this does not assert that any of the 720 admits ports.

There is also a forced port intersection. Vertex 4 is outside P and
Z, hence has exactly one port and no A edge. Its old routes to 1 and
2 originally used the now-deleted edges 01 and 23. Neither endpoint
of those old pairs meets A, so replacement old routes are impossible.
Both pairs require a shared new neighbor. Thus
\[
\varnothing\ne B_4\subseteq B_1\cap B_2,
\qquad |B_4|=1.
\]
Finally, each zero's one two-port endpoint neighbor and six ordinary
one-port Q neighbors must supply all eight new labels without any
repetition. This is stronger than merely counting eight slots.

The actual complete seed
`computations/dd82/construction/hs58_a5_remaining_seeds_run/cross.seed.json`
uses I={0,1,2} and identity permutations, hence
A={25-26,30-31,35-36,42-43,47-48}. Its ports satisfy
B0=B3={1,6}, B1=B2={1,7}, and B4={7}. The accompanying
`cross.analysis.json` records 58 vertices, 232 edges, maximum degree
8, and 72 bad pairs (one old-old, 71 old-new). In particular it is a
failed full graph, despite satisfying the zero-set and slot-count
requirements. No new enumeration or solver was used for this lemma.
