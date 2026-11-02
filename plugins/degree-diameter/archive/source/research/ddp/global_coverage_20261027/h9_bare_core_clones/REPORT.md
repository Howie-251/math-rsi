# Bare H9 partial fold: all ordinary independent clones have optimum343

The frozen macro prediction is supported by an exact global certificate. For the bare41356-point partial fold K, allowing arbitrary ordinary full-neighborhood clone counts of every vertex still gives **at most343 clones**. The known280 H3 copies plus63 padding vertices, with all extra-extra edges removed, attain343 as ordinary independent clones of K. Therefore this whole fixed-K clone class has maximum order41699, below saved(12,5) lower bound42342 and644 vertices short of strict improvement42343.

This is a new calculation on bare K, with a larger domain than the previous fixed41636-core bound63. The previous bound was not used as an upper bound here. No LP, MILP, whole-graph score, or BFS was needed; there is no incremental clone optimization to continue.

## Frozen question and exact domain

PREDICTION.json was saved before recovering the bare-core support. The falsifiable hypothesis was that the total ordinary clone count is below987, the amount needed for41356->42343. The computation instead establishes the sharp maximum343.

Fix the author's split set S and colors, and retain every edge of their partial fold before any H3 blowup or final pads. This is K with41356 vertices. For each vertex v of K choose any integer t_v>=0. Add t_v new vertices whose neighborhood is exactly N_K(v); put no edges between any new vertices. Prototypes range over every K vertex, without a group, orbit, region, or generic/H3 restriction.

The source partial-fold theorem gives K diameter at most5 for this S/color choice. Lemma2.2 gives the same global D5 bound after any such clone batch: equal prototypes have a common old neighbor; prototypes at distance>=2 use an old route's inner vertices; clones of adjacent prototypes use a3-step route. Thus this question is entirely a maximum-degree packing problem. Removing extra-extra edges from the source343 added vertices is justified by recognizing the resulting graph as a clone batch on K and applying that lemma; arbitrary edge deletion is not being assumed to preserve diameter.

## Bare-core recovery and old343 lower bound

The saved41636-core edge table was read once, retaining only IDs0..41355. Author numbering appends the280 H3 copies after these IDs, then63 final pads. The resulting bare K has234318 edges and the following degree distribution:

| degree | vertices |
|---:|---:|
| 7 | 168 |
| 9 | 112 |
| 10 | 6174 |
| 11 | 14112 |
| 12 | 20790 |

For each of the280 removed H3 copies, its K-neighborhood was matched exactly to a K prototype's complete neighborhood. The63 pad prototypes are already explicit K IDs in the author witness. old343_clone_mapping.json saves these280 exact matches and the63 pad assignments. Their combined343 counts pass every old-vertex degree budget on K. The known lower bound is therefore a checked feasible clone packing, independently of the removed extra-extra edges.

This does not regenerate H9 geometry, rerun the author verifier, or repeat a graph BFS. It uses the previously checked source ordering and explicit adjacency, together with the inherited D5 theorem. It does not change S, colors, or any core edge.

## Complete degree packing

For u in V(K), write d_u=degree_K(u) and delta_u=12-d_u. The exact model is

    maximize sum_v t_v
    subject to sum_{v in N_K(u)} t_v <= delta_u for every u,
               t_v >=0 integer.

The added clones themselves have degree d_v<=12. Thus the old-vertex inequalities are both necessary and sufficient for the maximum-degree cap in this model.

There are20790 saturated vertices. If a prototype v has even one saturated neighbor, that neighbor's zero budget forces t_v=0. This eliminates40782 prototypes and leaves574. Their degrees and individual integer bounds are:

| allowed core degree | prototypes |
|---:|---:|
| 7 | 168 |
| 9 | 112 |
| 11 | 294 |

| individual bound | prototypes |
|---:|---:|
| t_v<=1 | 490 |
| t_v<=2 | 84 |

The sum of individual bounds is658, already less than987. That alone closes the possibility of crossing42342 without any solver. The total unused degree27636 would be much weaker by itself; its location around the eligible prototypes is decisive.

All574 variables, exact neighborhoods, individual bounds, the3556 nonempty reduced degree rows, and the feasible343 assignment are in clone_packing.json. forced_zero.json gives an explicit saturated-neighbor witness for every excluded prototype. The model includes all K vertices; pruning is proved by the zero-budget inequalities.

## Sharp global certificate: a partition of all574 variables

A cheap weighted row cover selects287 original degree-budget inequalities. Their variable supports are pairwise disjoint and cover every eligible variable exactly once. They have only these three types:

| groups | variables per group | total allowed clone count in group | total contribution |
|---:|---:|---:|---:|
| 196 | 1 | <=1 | 196 |
| 63 | 2 | <=1 | 63 |
| 28 | 9 | <=3 | 84 |
| total287 | total574 | | 343 |

Summing gives sum_v t_v<=196+63+84=343. integer_upper_bound.json contains all287 selected old vertex IDs, budgets, and the complete variable lists. The partition property was checked exactly, with each of the574 variable IDs appearing once.

The source343-clone assignment attains every selected budget row and satisfies all3556 remaining rows. Consequently the upper bound is attained: the integer packing optimum is343. The same integral feasible point and nonnegative row-sum upper bound also prove the fractional optimum343, although no LP was run. This is a direct global certificate rather than an uncertified solver infeasibility result.

## Decision and limits

Every graph formed solely by ordinary independent full-neighborhood clones of this fixed bare K has at most41356+343=41699 vertices. More clone seeds, longer optimization, or selecting a few more prototypes cannot reach the required987 clones. This closes that entire fixed-K clone mechanism as a record route, beyond the earlier fixed41636/63 scope.

The result does not bound mixed augmentations whose new vertices have different neighborhoods, or whose useful global routing depends on a separate proved mechanism. It also does not bound changing S/colors, adding core edges, or a different core. No such extension is launched here, and no stopped H9 state search is resumed. The known41699 witness remains a source result, not a new lower bound from this task.

## Artifacts and resources

- PREDICTION.json: hypothesis frozen before support/packing computation.
- bare_core.edges and bare_core_degrees.json: the known K and exact budgets.
- clone_packing.json: every eligible prototype and the complete reduced model.
- forced_zero.json: saturated-neighbor witnesses for all eliminated prototypes.
- old343_clone_mapping.json: exact core-neighborhood reconstruction of the source343 twins and its feasible count vector.
- integer_upper_bound.json: the287-row partition certificate with total budget343.
- RESULT.json and terminal.json: attained upper bound343 and total-order bound41699.
- screen.py: recovery, support reduction, weighted row cover, and exact checks.

Core recovery, support filtering and certificate calculation took 0.430727 CPU seconds on one worker. LP calls0, MILP calls0, BFS0, default author verifier0, new target graphs0, new lower bounds0. No hashes or dependencies were created. The authorized threshold MILP was unnecessary and was not started.


## Macro extension: every added vertex containing a complete core star

The same343 bound covers a strictly larger class without any new optimization. Let G be a simple graph of maximum degree at most12 containing the fixed K with all its vertices and edges retained. New vertices may have extra anchors in K and arbitrary edges between new vertices. For a new vertex i, write

    A_i = N_G(i) intersect V(K).

Call i star-containing if some core vertex v satisfies

    N_K(v) subseteq A_i.

The inclusion is in this direction: the complete core neighborhood is contained in the new point's core anchors. Merely having A_i subseteq N_K(v) is insufficient. Choose exactly one qualifying prototype v(i) for every star-containing new point, even when several choices exist, and let t_v be their counts.

For any old vertex u, the number of its incident new edges is at least the number of chosen prototype neighborhoods containing u. Because K is retained,

    sum_{v in N_K(u)} t_v
        <= number of star-containing new points adjacent to u
        <= degree_G(u) - degree_K(u)
        <= 12 - degree_K(u).

Thus the chosen t satisfies the exact same packing inequalities as ordinary clones. The existing287-row certificate immediately gives

    number of star-containing new points = sum_v t_v <=343.

This remains true if other, non-star-containing new points also occur: their incident edges only use more old-vertex degree budget. Extra old anchors or new-new edges cannot reduce the mandatory incidence of a selected complete star. No enumeration, LP/MILP, or BFS is needed for this deduction.

Consequently an augmentation in which every added point contains a complete core star still has at most41356+343=41699 vertices. The known343 ordinary independent clones attain that order. Such all-star-containing augmentations also inherit D<=5: choose a qualifying prototype for each new point and retain only the ordinary-twin edges as a spanning subgraph; Lemma2.2 gives D<=5 there, and the extra anchors/edges cannot increase distance. The bound is therefore sharp even in this larger globally routed class.

The result includes repeated cloning followed by extra anchors when every added point retains a traceable core prototype with its complete N_K(v) inside its current K-neighborhood. This can be proved inductively for clones of already qualifying points while K is retained. It does not cover an arbitrary iterative rule merely because it is called cloning: the full-star containment must actually hold at every counted new point.

For a mixed augmentation with E new vertices, at least max(0,E-343) must contain no complete core star at all. In particular:

- At the current order42342, E=986, so at least643 new points must fail N_K(v) subseteq A_i for every v in K.
- A strict improvement with at least42343 points has E>=987, so at least644 new points must have that property.

These are unconditional degree-budget consequences within the retained-K scope. They are lower bounds on the number of structurally non-star points, not a classification or recount of the current source's986 extras. The earlier source observation that some extras look clone-like is not used to strengthen the certificate numerically.

Most pencil constructions cannot be included by name: a pencil vertex may have only a partial or otherwise different anchor set and contain no complete N_K(v). This proof makes no claim about all pencils, all shortcuts, or a graph obtained after deleting/changing K edges. In a new model the containment direction and the retained core must be checked before invoking the bound.

The macro decision is therefore stronger than ordinary-clone exhaustion. A record construction on this fixed K needs a large genuinely non-star component: at least644 new points at the first improving order. Enlarging the class only by adding anchors or edges to traceable full-star clones cannot overcome the343 cap. This guides attention to non-star safe shortcuts with their own global D5 argument, rather than filling a few more clones. No new candidate or template is started by this extension.
