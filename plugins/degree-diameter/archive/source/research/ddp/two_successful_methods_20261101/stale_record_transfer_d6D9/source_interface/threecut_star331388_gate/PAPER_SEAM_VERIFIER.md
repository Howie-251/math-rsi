# Exact seam verifier for one fixed three-cut/six-star candidate

This is a paper derivation, not an executed verifier. It reads only the actual source interface and small profile schema; it runs no distance/count DP, source validity test, sphere/point-pair enumeration, graph, BFS, solver or Lean. The source and RIGHT Cayley convention are those in `PAPER_INTERFACE.md` and `HISTORY_SOURCE_GATE.json`.

## Objects and inherited data

Let G be the fixed331387-vertex Rodriguez–Canale6-regular Cayley source of diameter≤9. Its working RIGHT law is(j,n)*(a,c)=(j+a,n*41^a+c) with the cached six inverse-closed generators, and label6763*j+n. Delete three distinct vertex-disjoint source edges F={a_i—b_i : i=1,2,3}. Let P be their six endpoints, H=G−F, and J the graph obtained by adding z adjacent to every point of P. All old source edges except F are retained. This is only the proposed331388/994164 rule.

For old v put r(v)=d_G(P,v). Since all deleted edges have both endpoints in P, the earlier nearest-source proof gives d_H(P,v)=d_G(P,v). Hence

d_J(z,v)=1+r(v),
d_J(u,v)=min(d_H(u,v),r(u)+2+r(v)).

The profile schema now lists actual identity distances and shortest-word counts exported for this new support question; this paper does not read or validate their binary arrays. Its distances≤8 are measured support, and distance9 for the remaining elements uses the inherited source diameter bound. Counts must still be exact integer shortest-path counts, including the distance-nine values; the diameter bound alone does not supply them. Such values can be derived from distance-eight neighbors without a new all-root search: c(g) for d(g)=9 equals the sum of c(h) over its RIGHT-generator neighbors h with d(h)=8.

## Universal path repair and the safe domain

Take a shortest old u→v path of length L≤9. If it contains no deleted edge it survives. Otherwise take the segment from the entering pin of its first cut to the exiting pin of its last cut and replace that whole segment by p—z—q of length2. The segment has length at least1, so the new walk has length≤L+1. If it contains at least two cuts, their disjointness makes the segment at least3 edges long, and the replacement shortens the route by at least1.

Consequently every candidate J has diameter≤10: old–old pairs have the replacement bound and z-to-old pairs have1+r≤10. Every old pair of source distance≤8 is automatically within9. For a source-distance-nine pair, any old geodesic avoiding F is safe, and any one containing at least two cuts gives a repaired walk of length≤8.

The star route is also safe whenever r(u)+r(v)≤7. Thus old pairs needing further analysis have source distance9 and r(u)+r(v)≥8.

## Why the cut-geodesic families become disjoint

Suppose a source9-geodesic contained two or more deleted edges. The first-cut to last-cut segment has length≥3. Its prefix and suffix reach two pins, so

r(u)+r(v)≤9−segment_length≤6.

Therefore when r(u)+r(v)≥8 no source9-geodesic can contain more than one cut. This is the reason no inclusion–exclusion is needed in the count formula below. It is not an assumption about distinct critical-cut matrices or uniqueness of the geodesic.

A source9-geodesic using even one cut a→b gives d_G(u,a)+d_G(b,v)=8 and therefore r(u)+r(v)≤8. In particular any actually damaged old pair must have **exactly** r(u)+r(v)=8. If the sum were larger, every source9-geodesic would avoid F, so an old9-route would remain. On a seam parameter the sum is automatically≤8, making the only nonsafe case the equality8.

## Exact avoiding-geodesic count and orientations

Let d(g)=d_G(e,g) and c(g) count shortest RIGHT-generator words from e to g. Left translation gives the total number of old u→v source geodesics as c(u^(-1)*v).

For any directed orientation(a,b) of a deleted edge, a source9-geodesic uses that orientation if and only if it splits into a shortest u→a prefix, the edge a→b, and a shortest b→v suffix with

d_G(u,a)+d_G(b,v)=8.

When this equality holds, every prefix/suffix concatenation has length9 and is geodesic because d_G(u,v)=9. Conversely the split is unique. Its exact count is

c(u^(-1)*a) * c(b^(-1)*v).

If the distance equality fails, its contribution is zero. Under source distance9 a sum below8 is impossible, since it would give a shorter u→v route.

For the ordered pair(u,v), sum over **all six directed orientations of the three deleted edges**, not only the three chosen positive representatives. When r(u)+r(v)≥8 the six geodesic families are mutually disjoint: a shortest path never repeats a cut, and the previous lemma forbids two different cuts. Thus the exact number of source9-geodesics avoiding F is

A_F(u,v) = c(u^(-1)*v)
           − sum over (a,b) in directed(F), d_G(u,a)+d_G(b,v)=8
               c(u^(-1)*a) * c(b^(-1)*v).

It is nonnegative under the stated premises. Positive means an old9-geodesic survives in H. Zero means H has no route of length≤9, since every such route would already be a source9-geodesic.

For r(u)+r(v)=8, therefore:

- A_F(u,v)>0 implies d_J(u,v)=9: the retained geodesic has length9 and the star route has length10;
- A_F(u,v)=0 implies d_J(u,v)=10: no old≤9 route remains and the star route has length10, while the universal upper bound is10.

Both orientations can contribute for one fixed ordered pair. Enumerating positive orientations to cover unordered pairs does **not** justify omitting the reverse-orientation terms from this subtraction.

For the equality-sum case, the contributing orientations can equivalently be recognized by d_G(u,a)=r(u) and d_G(b,v)=r(v), since each is bounded below by its nearest-pin distance and their sum must be8.

## Complete seam enumeration without all old pairs

Choose one fixed orientation a_i→b_i for each of the three cuts. For each i and each k=0..8, consider

u in S_k(a_i),  v in S_(8−k)(b_i),

where S_k denotes an exact source-distance sphere. Every such parameter gives a source walk of length9 through that oriented edge; some have shorter actual endpoint distance and are simply safe.

Any hypothetical bad old pair has source distance9, no retained geodesic and no star repair. Hence at least one source9-geodesic crosses a cut. If it crosses that cut opposite to the chosen orientation, reverse the entire geodesic and exchange u,v. The resulting ordered pair occurs in the corresponding chosen-orientation seam for its prefix length k. Therefore these three oriented seam families cover every unordered old pair that could be bad. Duplicate parameter occurrences are harmless; completeness does not require deduplicating them.

For each seam parameter, an exact verifier may skip source distance≤8 and r-sum≤7. The remaining parameters have source distance9 and r-sum8 and are decided by the exact avoiding count above. If all are positive, no old bad pair exists. If one is zero, it is a genuine distance10 counterexample for the candidate. This is a full old-pair test, not just the4+1+4 critical subset.

The degree-six sphere bounds are |S_0|=1 and |S_k|≤6*5^(k−1) for k≥1. Therefore a single oriented cut has at most

sum(k=0..8)|S_k(a)|*|S_(8−k)(b)|
 ≤2*(6*5^7)+7*(36*5^6)=4,875,000

parameters. The three cuts have at most14,625,000 parameters before actual sphere-size improvements or duplicate elimination. This is a finite mathematical upper bound, not an executed count or an n² scan.

## Lookup convention and constant work per parameter

Precompute for each of the six pins p the arrays

D_p[x]=d(p^(-1)*x),  C_p[x]=c(p^(-1)*x),

and r(x)=min_p D_p[x]. Undirected path reversal gives c(u^(-1)*p)=c(p^(-1)*u), so the directed-cut product is C_a[u]*C_b[v], with the distance condition D_a[u]+D_b[v]=8. Each parameter needs one identity-table lookup of d/c(u^(-1)*v) and at most six such cut tests/products. This uses path reversal, not a false claim that arbitrary right translations are Cayley automorphisms.

Source spheres can be translated by LEFT multiplication: S_k(p)=p*S_k(e). The products p^(-1)*x and u^(-1)*v must use the actual RIGHT group law. Counts for the phase quotient, unconditioned nonbacktracking prefixes or another field are not substitutes. The profile's stored sphere-four critical matrices cover only k=4; they cannot replace the complete k=0..8 seams.

## Full-candidate conclusion and exact diameter

For one valid fixed cut triple, the two conditions

1. max_v r(v)≤8 (the exact missing-set-intersection/newroot gate), and
2. no failing parameter in the complete three-cut seam verifier,

prove all point pairs in J have distance≤9. This is a complete all-pair interface based on the inherited source diameter and exact source counts, without running331388 root BFS searches.

To assert **exact** diameter9, retain a distance9 witness as well. If the actual maximum r is8, any old v with r(v)=8 gives d_J(z,v)=9. Alternatively any checked source9 seam pair with r-sum8 and positive avoiding count has d_J(u,v)=9. The weaker inequality max r≤8 alone does not preserve a source non-D8 witness, because adding the star may shorten old distances.

No candidate triple or verifier is evaluated by this note. The profile data are inputs for a possible separately authorized exact candidate check, not a proof that one exists. The three-cut matching requirement, both directions in the count sum, complete source9 counts and final distance9 witness remain explicit obligations. This changes no graph, parameter, Lean, source-validity or priority count.
