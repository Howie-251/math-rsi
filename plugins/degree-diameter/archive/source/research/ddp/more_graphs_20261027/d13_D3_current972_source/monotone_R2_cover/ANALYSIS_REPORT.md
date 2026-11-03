# Exact integer obstruction to a 13-pin append

The cached cover matrix gives a strict mathematical lower bound of15 pins. Therefore the fixed972-vertex source cannot be extended by only one new vertex of degree at most13, with the source induced graph unchanged, while keeping diameter at most3. This is an obstruction to this append family, not a new graph or a claim about arbitrary helpers or changed old edges.

The actual source profile has108 vertices of degree12 and864 of degree13. All36 consecutive27-vertex blocks have exactly3 free vertices. A single new vertex can use only those108 free vertices as old neighbors. For each free pin p let B_p be its closed radius2 ball in the source. A new vertex has radius3 covering all old targets exactly when its chosen B_p cover all972 targets.

Use the972 nonnegative integer row weights in INTEGER_ROW_WEIGHTS.json. There are72 positive weights. The exact cached-matrix check gives

    W = sum over all targets of w(t) = 14775252,
    C = max over the108 pins of sum over t in B_p of w(t) = 999999.

For any k selected pins whose balls cover every target, double counting nonnegative target weights gives W <= sum selected ball weights <= k*C. Here

    W - 14*C = 775266 > 0,
    W - 13*C = 1775265 > 0.

Hence k >= ceil(14775252/999999)=15. The weights need not be an exact feasible LP dual. Any nonnegative integer weights satisfying these directly checked sums give the proof; the LP merely supplied a useful choice. No floating-point conclusion or solver infeasibility certificate is needed for this inequality.

ANALYSIS_integer_weights_check.py independently sums all108 cached columns, checks the complete exported column-weight list, and binds their eligible labels to SOURCE_PROFILE.json. It independently parses source972.edges and rebuilds only the first pin5 sphere: degree12, closed R2 size139, exactly matching its cached column. The remaining107 spheres reuse the producer's actual source computation rather than being recomputed. Check cost0.007978562 CPU seconds, with zero LP/MIP runs, graph generations or source diameter BFS. The producer's weights and radius2_sets.json remain the literal certificate inputs.

The earlier fractional optimum14.7752896474 and threshold13 MIP infeasibility are consistent diagnostics, but the strict15-pin conclusion above follows solely from the integer matrix inequality. No candidate973 graph, global diameter, or ordinary unordered bad-pair count was produced. The fixed13-pin single-vertex append family is closed and this analysis is stopped.
