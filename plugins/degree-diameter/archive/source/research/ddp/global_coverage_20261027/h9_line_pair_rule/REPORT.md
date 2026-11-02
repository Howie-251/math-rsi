# H9 line images: global D5 rules, center-capacity obstruction, and the canonical-anchor gap

This is one paper-derivation round on the existing H9 partial fold. It gives an explicit global D5 line-image rule and then rules out its concentrated adjacent-center version as a route to the required987 new points on the fixed core. One authorized edge-intersection pass was used; there was no graph generation, BFS, clique search, packing, solver, or local repair.

The canonical one-anchor idea remains a precisely stated missing condition, not a claimed universal D5 theorem or a constructed H9 counterexample. Current810 non-star vertices have not been identified as geometric line-image vertices by this report.

## Fixed objects and mandatory pins

Let Gamma be the incidence graph of H(9), with point set P and line set L. It is bipartite with diameter6 and girth12. Use the source's actual point-line bijection sigma: on every phi-pair choose tau or tau^-1 consistently, where phi=tau^2. Let G_sigma be the point graph from Lemma3.1, and pi:P->V(K) the actual partial-fold map. The fixed K=G(S,c) has41356 vertices, diameter at most5, maximum degree12 and minimum degree7. It is not the41636 blowup or the later graph prefix.

For every proposed new vertex z_i, choose a geometric line L_i and require its core pins to contain **every** folded point image on that line:

    P(L_i) = {pi(p): p is incident with L_i} subseteq N(z_i) intersect K.

Duplicate folded images are one pin. Every z_i is a distinct new graph vertex. Different new vertices may represent the same line; that is allowed unless an explicit one-per-line restriction is stated. The rule is about actual incidence and the actual partial fold, not a numerical label guess.

Additional core anchors and new-new edges may be included. Their degree budget must be checked independently:

    d_K(u) + number of new neighbors of u <=12,
    number of distinct core pins of z_i + number of new neighbors of z_i <=12.

A line has10 points before folding, so its mandatory pin set has at most10 elements. This does not automatically leave two anchors in every case: the number allowed is exactly12 minus its distinct pins and new-neighbor count. No positive routing argument below dispenses with these budgets.

## Complete projection proof: old core to any new line vertex

Choose a core vertex u and any representative x in pi^-1(u). The H9 incidence graph has an odd point-to-line path

    x=x_0, M_1, x_1, ..., M_(j-1), x_(j-1), M_j=L_i

with2j-1<=5. Replace each interior line M_k by the point sigma^-1(M_k). End at the new vertex z_i rather than replacing the last line. This gives

    x_0, sigma^-1(M_1), x_1, ...,
    sigma^-1(M_(j-1)), x_(j-1), z_i.

Every interior consecutive pair is an edge of G_sigma, or is the same point, because the adjacent point lies on the indicated sigma-image. The last point lies on L_i, so its folded image is a mandatory pin of z_i. Apply pi to all old points; consecutive equal images are deleted. The remaining walk lies in K plus z_i and has length at most2j-1<=5. Hence every old core vertex is at distance at most5 from every line-image vertex.

This proof uses all line images as pins. Omitting an inconvenient pin can break it; an extra unrelated anchor does not replace the missing incidence step.

## Line to line: the exact missing parity step

An incidence path from L_i to L_j has even length at most6. Replacing its interior lines by their sigma-preimage points, folding those points, and replacing its two end lines by z_i,z_j gives a walk of the same length at most6. If the two lines have incidence distance at most4, it gives at most4.

For opposite lines at incidence distance6, the proof alone still has6 steps. It does not supply a fifth-step shortcut. A collapse of consecutive projected vertices or another cross-route can shorten it, but that must be proved from the particular sigma/fold or anchor configuration. The source's point-to-line odd-path theorem has not supplied such a uniform collapse for arbitrary opposite-line pairs.

Thus a route for the new classes is a separate concrete geometric requirement. This report neither declares all opposite-line pairs bad in K nor invents an unmeasured H9 counterexample.

## Rule1: one center line, no extra anchor required

Fix a geometric center line M_0. Choose any family of lines L_i that meet M_0. For each new z_i add its entire P(L_i) pin set. For two distinct new vertices choose p in L_i intersect M_0 and q in L_j intersect M_0. The incidence walk

    L_i, p, M_0, q, L_j

has length at most4 after deleting repeated endpoints. Its projection is

    z_i, pi(p), pi(sigma^-1(M_0)), pi(q), z_j,

with consecutive equal old vertices removed. All required edges follow from the mandatory line pins and incidence with sigma(sigma^-1(M_0)). Hence new-new distance is at most4. Combined with the previous proof and K's D5, the entire augmented graph has D<=5. Extra anchors or new-new edges can only shorten these routes.

The number of distinct lines meeting M_0, including M_0, is

    1+(q+1)q=q^2+q+1=91 at q=9.

If each geometric line is used at most once, this gives at most91 new vertices. This number is not an upper bound when one line is represented by multiple distinct new vertices. Such repeated vertices share core pins and have distance2; the same routing theorem still works, but their total degree load must be charged separately.

## Rule2: adjacent projected centers

Choose geometric points a_1,...,a_c whose distinct actual core images C={pi(a_i)} form a clique in K. Use center line M_i=sigma(a_i). Assign every proposed line L to a center i such that L meets M_i. If p is an intersection point, then pi(p) belongs to the closed core neighborhood N_K[pi(a_i)], and

    d(z_L, pi(a_i))<=2.

The possible equality pi(p)=pi(a_i) only shortens the walk. Thus for new vertices assigned to different centers,

    d(z_L,z_M) <=2 + d_K(pi(a_i),pi(a_j)) +2 <=5.

For equal projected centers the bound is4. The old-new proof is unchanged. This is an explicit global D5 construction rule for any permitted line family and any number of distinct new vertices per line, provided the degree budgets pass. It does not require a new point's pins to contain a complete core star.

With one geometric center line per distinct core center and at most one vertex per geometric line, there are at most91c distinct lines. Line overlaps only lower that count. Repeated line vertices must instead be treated by the degree-budget bound below; they cannot be excluded from the whole class by91c alone.

## Frozen P7 and the one cheap core check

P7_PREDICTION.json froze the prediction that this adjacent-center rule cannot provide987 new points on fixed K. Its initial one-per-line test was whether K could even have11 mutually adjacent centers: a K11 would require every edge to have at least9 common neighbors.

One pass intersected the two endpoint neighborhoods of every one of K's234318 edges. The observed counts are:

| common neighbors of an edge | edges |
|---:|---:|
| 0 | 233940 |
| 1 | 378 |

The maximum is1. Edge656--3819 has the common neighbor8051, so a triangle exists; no edge has two common neighbors, hence K has no K4. Its clique number is therefore exactly3, without enumerating cliques. The adjacent-center rule has c<=3. Under the one-per-line restriction this gives at most273 new vertices, far below987.

This is a statement about the fixed K. It does not restrict center sets joined by longer core paths or a different routing rule; none of those is searched here.

## A duplicate-safe global capacity bound: at most165 new vertices

A degree-load argument closes the entire adjacent-center rule even if geometric lines are repeated arbitrarily many times. Let

    U = union_(c in C) N_K[c].

Every new line vertex has at least one mandatory pin in U: its chosen line meets sigma(a_i) at p, and pi(p) is in N_K[pi(a_i)]. Therefore, counting actual new-core edges,

    number of new vertices
        <= number of new-core edges incident with U
        <= sum_(u in U) (12-d_K(u)).

The first inequality counts each new vertex at least once. It holds for multiple vertices with the same line label, extra anchors, and new-new edges.

For a clique of c centers in a maximum-degree12 core, each center has c-1 neighbors already inside the clique and at most13-c outside it. Thus

    |U| <= c+c(13-c)=c(14-c).

Since c<=3 and every core vertex has degree at least7,

    number of new vertices <=5*max_(1<=c<=3)c(14-c)
                           =5*33=165.

This is a coarse but rigorous global upper bound, requiring no packing optimization. The total order of this class is at most41356+165=41521, and so it cannot approach42343. The number165 here is a budget bound for this proposed geometric rule; it is not an identification of the current source's last165 vertices with that rule.

Even before the core edge pass, the generic c<=13 bound would give |U|<=49 and at most245 new vertices. The actual common-neighbor data strengthens that to165. These bounds are independent of the one-per-line restriction.

## One universal anchor: what is proved and what is not

For a proposed line vertex z_L, a natural canonical anchor is

    a_L = pi(sigma^-1(L)).

Adding this one anchor preserves the old-new guarantee. However, applying the source odd-path proof from a_L to another line M gives distance at most5 from that anchor to z_M, and the first z_L--a_L edge gives only6. The source theorem alone therefore does not prove that this canonical anchor formula resolves every opposite-line pair. This is a missing proof condition, not an assertion that the rule is false in H9.

A sufficient extra condition would be that all these actual anchors have pairwise core distance at most3: the anchor-to-anchor route then gives z_L--a_L ... a_M--z_M of length at most5. It is not necessary, because the line pins may supply alternative routes. No such large anchor family, degree-feasible realization, or current geometric witness has been recovered here, and no search for one is launched.

If instead one common core vertex is attached to every new line vertex, new-new distances are trivially2, but its degree budget allows at most12-d_K(a)<=5 such vertices. That cannot be a large-scale solution. A common formula a_L depending on L must not be confused with this single shared anchor.

The construction question still missing for a large family is explicit opposite-line routing with distributed degree load. It must give the actual lines, their complete folded images and anchors, and a uniform <=5 route between every new class, possibly through other new classes. The measured helpers42177/42291 motivate that possibility, but this report has not identified those helpers as geometric centers or line vertices. In particular no existing helper fact is promoted to a universal anchor theorem.

## Decision, evidence, and computation scope

The line-pencil and adjacent-center rules supply complete positive diameter proofs without requiring full core stars. Their concentrated form is nevertheless globally too small under the fixed core's degree budgets. Thus the next rule cannot simply replicate line images around a core clique or add one common anchor. A larger construction needs a distributed pair-routing guarantee that changes this concentration constraint; this report does not start another center template or local search.

P7_RESULT.json records the one common-neighbor pass, an exact witness and histogram, the clique bound, and both counting scopes. RESULT.json records the paper rules and their limits. The sole arithmetic/graph-data pass used 0.399005 CPU seconds on one worker. BFS0, candidate graphs0, clique enumeration0, packing0, solver0. The core input is the saved bare_core.edges; no old full-graph verification was repeated.

Primary proof source: the local H9 partial-fold paper, Lemma3.1, Lemma4.1 and Theorem5.1 in wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt. The previous global-rule source analysis and current core identity are in ../h9_global_rule/REPORT.md and ../h9_relation/REPORT.md. The all-star343 bound remains a separate result in ../h9_bare_core_clones/REPORT.md; it is not used to exclude the non-star line-image class here.
