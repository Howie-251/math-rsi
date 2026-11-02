# Independent paper check of the conditional counting lemma

Verdict: the stated conditional claim is correct. No counterexample or
missing type of added edge/path was found. This check does not assert
that the actual 585-point source satisfies the hypotheses. The separate
source evidence must discharge them before the claim is applied. No
download, source parsing, graph generation, BFS or numerical search was
performed for this check; the original draft was left unchanged.

Let J be a finite simple supergraph retaining every old edge of G,
with maximum degree9 and diameter at most3, and let X be its nonempty
new-vertex set. The following fills out two short arguments in the
draft, without changing its bound.

First, every newly added edge incident with an old vertex must use a
port: the 520 nonports are already saturated. Any added old–old edge
must therefore join two ports, and each port can use at most one such
edge or one new–old edge, because its old degree is8.

Fix any new vertex x and any port p. On an x-to-p path of length at
most3, let y be its last new vertex and q its next vertex. Then q is
a port, and the new–old edge yq consumes q's sole old-vertex degree
slot. There are at most two edges left from q to p and no new vertex
in that suffix. Its first edge cannot be an added port–port edge,
because q is full after yq. Any original first edge goes from q to
a nonport: distinct ports have old distance3. A second added edge
cannot be incident with that nonport, because it is saturated.
Thus, if q differs from p, the suffix would have to be an original
path of length at most2 between distinct ports, also forbidden.
Hence q=p and p has a new neighbor. This holds for all65ports.
Every free slot is consequently consumed by a new–old edge, so no
added old–old edge can occur anywhere in J. An earlier old/new
excursion in the path prefix does not invalidate this last-new-vertex
argument. This handles arbitrary old–old additions, not just a
particular matching chosen in advance.

Now H=J[X] is finite and nonempty, so it has a minimum-degree vertex
x of H-degree r, with0≤r≤9. Write A for its attached old ports. Then
|A|≤9−r. Each of the r H-neighbors y satisfies deg_H(y)≥r, hence has
at most9−r old port attachments. Their attachment union B therefore
satisfies |B|≤r(9−r). This is an upper bound on a union; repeated ports
would only decrease it. In fact the one-slot property forbids such
repetition, but that stronger observation is unnecessary.

For an old nonport target t, a path from x of length at most3 has
one of two relevant forms. It enters G directly at a port in A and
uses at most two remaining old edges, yielding A intersect S(t)
nonempty; or it takes one H-edge, enters G at a port in B and uses
one old edge, yielding p(t) in B. Two H-edges leave only one step,
whose old endpoint would be a port rather than t. A direct entry
cannot leave G through a different new neighbor at the same port:
the port has only its unique new edge. All other old-to-new reentry
patterns require more than three steps. The draft's two coverage
classes are therefore exhaustive.

The design parameters are consistent and correctly computed. In a
3-(65,9,1) design, a point lies in

    C(64,2)/C(8,2)=72 blocks,

and a pair lies in63/7=9 blocks, while a triple lies in one. Applying
the odd, third-order Bonferroni upper bound to the events p in S(t),
for p in A, gives

    |{t:S(t) intersects A}| <= U(a)
    U(a)=72a−9*C(a,2)+C(a,3).

This is an upper bound, in the correct direction. Its increment is
72−9a+C(a,2), positive for integer0≤a≤8, so a can safely be replaced
by9−r. Each port has exactly8 old nonport neighbors, since its old
degree is8 and ports have no old edges between them. Thus the second
class has at most8|B| members. Adding the two class bounds is safe;
any overlap merely makes the resulting upper bound looser.

The resulting totals for r=0,...,9 are

    408,444,462,461,440,398,334,247,136,0.

Their maximum462 is below520. Thus the chosen new vertex x cannot
reach at least58old nonport vertices within three steps, a
contradiction. The precise conclusion remains the draft's: conditional
on its local degree/port/design hypotheses, no finite connected
proper enlargement can preserve all old edges while retaining
maximumdegree9 and diameter3. It does not exclude deleting old edges,
other sources, unrelated graphs, or establish optimality of N(9,3).

The existing source's all-pairs D3 verification is not used by this
counting argument: the stated local hypotheses already force the
extension obstruction. A new all-source BFS is therefore not needed
to check this deduction. The actual-data premise checks and the
conditional proof remain separate evidence objects.
