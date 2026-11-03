# A commuting internal graph cannot repair the GQ D3 coverage gap

Status: self-contained paper derivation complete. No graph generation, MILP, BFS, group enumeration, or new lower bound. This is a structural obstruction within the retained-incidence GQ mechanism, not an exclusion of all internal graphs.

**Scope correction:** parity excludes an exactly r-regular graph on an odd side when r is odd. It does not exclude maximum-degree-r graphs. In particular, q=8 permits 585-vertex internal graphs of maximum degree 3 with one degree-2 vertex; the 1170-point degree-cap-12 template remains open for noncommuting choices. The result below excludes its commuting subclass as well as the commuting subclasses of all three regular necessary passes.

## Statement, including unequal degree bounds

Retain every incidence edge of GQ(q,q), where each side has N=(q+1)(q^2+1) vertices. Let P be the simple undirected internal adjacency matrix on the point side, Q the one on the line side, and C the binary closed-collinearity matrix on points. Suppose

    P C = C P.

Then P is automatically regular, with some degree p. If Q has maximum degree at most s, every point root can reach at most

    U_comm(q;p,s) = p q^2 + s q(q+1)
                   + p(p-1) + p(p-1)^2

of its q^3 noncollinear point targets in at most 3 steps. Consequently U_comm(q;p,s)<q^3 makes diameter 3 impossible. The assertion is dual if the line-side adjacency commutes with its own closed-intersection matrix. The other side may be arbitrary subject to its stated degree bound; it need not commute, share an automorphism, or have any symmetry.

When both sides are r-regular, this becomes

    U_comm(q,r) = r q^2 + r q(q+1) + r(r-1) + r(r-1)^2.

The missing r q^2 compared with the previous average bound is the exact endpoint-route overlap forced by commutation, rather than a heuristic assumption about overlap.

## Proof of the pointwise capacity bound

For a point x, let C(x) be x and all its collinear points. The GQ axioms give |C(x)|=q^2+q+1, and |C(x) intersect C(u)|=q+1 for every distinct x,u. Thus |C(u) minus C(x)|=q^2. Each point has exactly q^3 noncollinear targets.

An internal edge followed by up to two incidence steps has endpoint support equal to the support of P C. An incidence two-step route followed by an internal edge has support equal to that of C P. Since P C=C P entry by entry, these supports are identical, including after restricting to far targets. They therefore contribute their union only once. At a point root x, its p internal neighbors u give at most p q^2 far endpoints in the support of P C. This bound is pointwise: no average estimate for C P is being silently used.

For the remaining two-incidence route, write B for the point-to-line incidence matrix. A path with a line-internal edge in the middle is represented by B Q B^T. From x, choose one of its q+1 incident lines and at most s internal line neighbors of that line. A resulting line through x has no far points; a line not through x has exactly q far points, because it has one point collinear with x. This gives at most s q(q+1) far endpoints.

A purely point-internal path of length 1 is already in the support of P C because C has its diagonal. A length-2 path with an immediate reversal returns to x, so at most p(p-1) further far endpoints can occur. A length-3 path with an immediate reversal ends at an internal neighbor of x and is already counted; at most p(p-1)^2 other paths remain. Repeated endpoints and near endpoints only reduce coverage.

These cases exhaust every same-side path of length at most 3: the number of incidence edges must be even, hence zero or two. Summing the four endpoint bounds proves the stated U_comm. In particular, commutation removes one whole endpoint-route term without overlooking an additional path pattern. Retaining incidence still gives D<=4, so any missing far endpoint here is at distance exactly 4.

## Why commutation forces regularity

The closed-collinearity identities also give

    C^2 = q^2 I + (q+1) J.

Indeed, each diagonal entry counts |C(x)|=q^2+q+1, and each off-diagonal entry counts a q+1-element intersection. From P C=C P we obtain P C^2=C^2 P, hence P J=J P. For an undirected adjacency matrix, entry (x,y) of P J is degree(x), while entry (x,y) of J P is degree(y). All degrees are therefore equal. This regularity conclusion is derived from commutation; it is not imposed on the original maximum-degree problem.

## Consequences for every order-improving capacity survivor

| q | n | degree cap | saved D3 lower bound | commuting-side p used | other-side max s | U_comm | far targets | missing per root at least |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 80 | 5 | 72 | 1 | 1 | 21 | 27 | 6 |
| 5 | 312 | 8 | 253 | 2 | 2 | 114 | 125 | 11 |
| 7 | 800 | 11 | 715 | 3 | 3 | 333 | 343 | 10 |
| 8 | 1170 | 12 | 810 | 2 | 3 | 348 | 512 | 164 |

For q=3,5,7 these inequalities exclude a commuting adjacency on either side for the three exact-regular capacity survivors. They also cover maximum-degree versions: a commuting side becomes regular of degree p<=r, and the displayed upper bound uses the largest allowed p.

For q=8, each side has N=585 odd vertices. A commuting side must be regular, and the handshake identity forces its degree to be even. Under internal maximum degree 3 it therefore has degree 0 or 2. Taking the larger degree 2 while allowing the other side its full maximum degree 3 gives

    U_comm(8;2,3) = 2*64 + 3*8*9 + 2 + 2 = 348 < 512.

This excludes a commuting side without incorrectly assuming the other side is regular. It does not exclude two noncommuting near-regular internal graphs. For example, a degree sequence consisting of one 2 and 584 threes has even total degree and is compatible with the degree cap; exact 3-regular parity is irrelevant to its legitimacy.

A commuting side would force at least N*(q^3-U_comm)/2 unordered distance-4 pairs wholly within that side: respectively 120, 858, 2000, and 47970 in the four rows. These are proven lower bounds under the commuting hypothesis, not measured bad-pair counts from generated graphs.

## Which automorphism constructions are covered

If M is the permutation matrix of a collinearity automorphism, then M C M^T=C, hence M C=C M. A sum P of such matrices also commutes with C. Therefore the obstruction covers such a sum when it is already a simple undirected adjacency matrix: zero diagonal, entries only 0 or 1, and symmetry. One sufficient symmetry condition is an inverse-closed list of automorphisms; no fixed points and no repeated image at a vertex ensure the other two conditions.

This includes the intended simple edge-disjoint automorphism factors. For q=3,r=1, a perfect matching that is itself a fixed-point-free involutory collinearity automorphism is ruled out even if the matching on the other side is unrestricted.

Do not extend the claim to every graph described as coming from automorphisms. Removing loops, collapsing repeated edges, or taking an entrywise support of a weighted sum is not the same linear matrix operation; commutation may be lost. Such a graph is covered only if its actual simple adjacency is proved to commute with C. Merely being invariant under some group also does not establish this matrix equality.

## Direction change and remaining scope

For all four order-improving maximum-degree capacity survivors, **both actual internal adjacencies must fail to commute with their respective closed geometry matrices** if D3 is to hold. Selecting simple edge-disjoint factors from collinearity automorphisms cannot repair these gaps. A useful future construction must break that commuting geometry on each side; no new search is authorized or run by this derivation.

The unrestricted q=3,r=1 exact-matching MILP already had one separate bounded window, ending UNKNOWN with no incumbent. The q=5,r=2 finite two-start profile had a graph of actual D4 and 4090 bad unordered pairs; that does not exclude its whole noncommuting family. No q=7 or q=8 graph is produced here. No previous window is resumed.

## Evidence and proof status

`RESULT.json` saves the exact integer substitutions, mixed-degree formula, scope, and lower bounds on missing targets. `check.py` performs only those substitutions. The previous general bound and its maximum-degree clarification are in ../gq_internal_capacity/REPORT.md. Existing finite runs are referenced through ../gq80_paired_matchings/terminal.json and ../../breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json.

The proof above is a same-model paper derivation, with no external-review or formal-proof claim. Its assumptions and path exhaustiveness are stated explicitly. It supplies a mathematical obstruction, not a new graph record.
