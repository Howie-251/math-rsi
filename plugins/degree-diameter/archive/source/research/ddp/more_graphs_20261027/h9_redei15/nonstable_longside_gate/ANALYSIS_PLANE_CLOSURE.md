# Nonstable Rédei planes: projectivities, safe closure and stopping scope

Status: **VALID paper analysis using the stated saved interfaces**. This analysis ran no field enumeration, line gate, pool, R4 check, graph or solver. The producer's saved line-gate data are distinguished below from deductions and from later production.

Throughout phi is coordinate Frobenius x->x^3 on raw Q(6,9) points. In the source files it equals the square of the order-four point-line duality tau; tau itself is not used as a point involution.

## Nonstable planes sharing a stable line exist

Let ell be an F3-defined totally singular projective line. Its underlying vector space has dimension two. The residual quadratic space ell-perp/ell has dimension three and Witt index one. Its singular points form Q(2,9), a conic with ten points, in bijection with the maximal singular planes containing ell. Exactly four are Frobenius-fixed, since the residual F3 conic has four points. The other six form three conjugate pairs of nonstable planes.

For any such nonstable plane Pi, both Pi and phi(Pi) contain ell and are distinct, so their intersection is exactly ell. Their vector span has dimension four but is not totally singular; there is no contradiction with ambient Witt index three. A fixed raw point in Pi must also be in phi(Pi), hence Pi has exactly the four F3 points of ell as its Frobenius-fixed points.

There are364 F3 singular points,40 singular lines through each, and four points per line:364*40/4=3640 rational singular lines. Each nonstable plane in this class has the unique intersection ell=Pi intersect phi(Pi), so the number of these planes is3640*6=21840. This is a theoretical family count, not a statement that this analysis generated them.

## Complete projectivities for the chosen long side

The companion long-side argument identifies the four-point complement of the source's six-point direction line as a Baer subline and maps it to PG1(F3). In the saved field convention u=3,u^2=2, the source complement is {infinity,0,3,6}; multiplication by u^-1=6 gives {infinity,0,1,2}. Thus its six selected points map to all six nonfixed points of ell. This does not require an unsupported cross-ratio assumption.

After this fixed preliminary map and a fixed plane basis, all projectivities taking the chosen source line to ell and its six selected points to ell's six nonfixed points have representatives

    [ 1   0   0 ]
    [ t1    A   ]
    [ t2        ],

where the lower-right block is A=a*M, M ranges over24 fixed representatives of PGL2(F3), a ranges over the eight nonzero F9 scalars, and (t1,t2) ranges over F9^2. Normalizing the first diagonal entry to one removes the global projective scalar. Distinct M have distinct PGL2(F9) classes, and a is then unique. Hence the complete parameter count is24*8*81=15552 per selected plane/basis. These are projectivity parameters, not distinct pinsets or nonisomorphic graphs.

No extra factor three is needed merely to choose which of the source's three six-point sides maps to ell. To see their transitivity, take the three pairwise side intersections as triangle coordinates (z0,z1,z2). The four nonvertex points on the sides have ratios z1/z0 in Q, z2/z0 in N, and z2/z1 in N, where Q is the square subgroup of F9* and N its nonsquare coset. For the infinity side, write its mixed slope m=(1+s)/(1-s), with s nonsquare. The triangle-coordinate ratio is (1-m)/(1+m)=-s, still nonsquare since -1 is square. Rescale z2 by the inverse of a nonsquare. All three ratio conditions become membership in Q. Coordinate permutations then preserve the set, giving a source automorphism subgroup transitive on the three sides. Composing with such an automorphism covers the same embedded sets using one fixed source side.

## Whole-class closure is the safe map interface

Let B be an embedded15-point Rédei set in Pi, with its six-point side exactly the six nonfixed points of ell. Then B intersect phi(B) is precisely those six points. All other nine B points lie off ell and have their mates outside Pi. No B point is Frobenius-fixed. Thus U=B union phi(B) has24 raw points, in twelve distinct phi classes.

Let rho map raw points to the33397 Frobenius classes, and let q map the actual current core to those same labelled classes. A safe mandatory set is

    C=q^-1(rho(B)).

This selects every actual current representative of each selected class. For any compatible raw-to-core numbering pi, this is also pi(B union phi(B)), and pi^-1(C)=U. It is unchanged by orientation flips inside a split class. It does not claim that pi maps every raw edge to a current edge.

If t of the twelve selected classes are split in the actual core, then |C|=12+t. More generally, for any raw B, if j is the number of nonfixed phi pairs wholly inside B and t counts selected split classes, then

    |C|=|B|-j+t.

The lack of collisions between different classes is essential here. For degree13 it is bound by the degree13-specific construction in `../../d13_D5_h9_transfer/bind_source.py`, not borrowed from the old degree11/12 PAIRING file: raw_labels[p]=p and raw_labels[phi(p)] is either phi(p) or p, with fixed points labelled themselves; sorting labels preserves these and only these identifications. The script asserts disjoint core classes and covers all50554 core vertices. Its saved `RESULT.json` has status D13_CORE_PARTITION_BOUND and class sizes16240 singletons/17157 pairs; `fold13_classes.json` stores the partition. This is the class/fiber interface, not the false claim of a fully oriented raw graph map. The separate old-core gauge failure remains valid.

The inherited blocking proof gives radius-four coverage in the full quotient F: restrict any target polar functional to Pi, obtain a line or the whole plane, and use that B meets every line. The current core's verified complete/perfect-matching class blocks allow reverse lifting from any target vertex to a selected whole class C. Therefore C covers the entire actual core in radius four without recovering raw orientation. All existing extras still require actual whole-current-graph R4 checking, and every pin needs actual degree slack.

## No hidden complete Q-line or Baer13 footprint

Because the six intersection points are phi-stable, U intersect Pi=B and U intersect phi(Pi)=phi(B). A projective F9 line not contained in either plane meets their union in at most two points. A line contained in one plane meets U exactly in that plane's Rédei set, which contains no complete ten-point line. Consequently U contains no full F9 line.

Let T be a Baer13 subplane and Sigma its F9 projective span. If Sigma is neither Pi nor phi(Pi), its intersection with either is at most a line. A Baer subplane meets an ambient line in at most four points, so T has at most4+4=8 points in the union, not thirteen. If Sigma is one of the two planes, T would lie in B or phi(B). The existing Rédei set contains no Baer13: its three supporting lines each contribute at most four Baer points, giving at most twelve. These properties are preserved by projectivity.

Hence if the folded image of any full Q-line or Baer13 were contained in C, its raw set would be contained in pi^-1(C)=U, a contradiction. This statement concerns C alone; unrelated added anchors can alter subset containment. It does not assert that no other rule shares the same metric coverage.

## First gate budgets and actual scope

The three long-side classes cost3+t_ell actual pins. The other nine raw points represent nine different additional classes and cost at least nine. The necessary first gate is therefore long-side closure<=3 at cap12, and<=4 at cap13, with every such pin free. Cap13 must allow one split long-side class; testing only all-three-merge would be incomplete.

For cap12, any final candidate in this whole-class frame needs all twelve classes unsplit, so |C|=12 and no anchor remains. At cap13, at most one class can be split in total; if none is split the twelve pins leave one anchor. These statements concern the chosen whole-class rule. In particular, degree12 may have other correctly oriented direct-image rules outside this conservative closure frame.

The producer's saved RESULT reports3640 complete line checks per current source: degree12/source42402 has64 eligible lines; degree13/source51457 has none under the complete cap4 gate. No nonstable plane or projectivity was enumerated in that gate, and no R4 or graph was computed there. The64 positive degree12 lines only opened a candidate domain. The later producer completed all384 planes. Its15552 affine projectivity parameters per plane were exactly deduplicated into486 nine-point masks, each of multiplicity32, giving186624 actual mask tests covering5971968 raw parameters. The degree-legal pool is empty, so it ran no R4 or graph. These execution facts are inherited from `../nonstable_longside_production/REPORT.md` and its results, not evaluated by this paper.

## Degree12 closure covers every nonstable-plane Rédei placement

The completed scope is larger than an arbitrary preselected long-side footprint. For any projective image B of this15-point set in a nonstable singular plane Pi, a closure of at most12 pins requires j-t>=3. Every internal complete phi pair lies in Pi intersect phi(Pi). An empty or point intersection cannot contain such a nonfixed pair. If the intersection is a line ell, the maximal line intersection of B has size six, so 2j<=6 and j<=3. Therefore j=3 and t=0: B meets ell in exactly six nonfixed points, all three pairs, and no additional fixed point.

Such an ell is a rational singular line. If all twelve closure pins are degree-free, its three on-line pins pass precisely the completed cap3 degree12 gate, so ell is among the64 saved lines. Pi is one of its six nonstable extensions. Its B embedding lies in the complete15552-projectivity family, using source long-side transitivity above. Hence the empty completed pool excludes **all** nonstable-plane projective Rédei15 placements with whole-class closure at most12 on the specified current42402 source. It is not just a failure of a convenient footprint. The bound j<=3 also shows that a cap11 whole-class rule in a nonstable plane cannot fit this raw15-point shape, independently of degrees.

This does not cover arbitrary PGL3(F9) placements in stable planes: when Pi=phi(Pi), the conjugate intersection is the entire plane, so the line bound on j is inapplicable. The old stable702 orbit used only PGL3(F3); a genuinely different stable-plane F3 orbit remains outside that old pool and this nonstable-plane closure.

## Data-dependent stronger degree13 corollary

The degree13 line result has exactly two forms over all3640 stable singular lines:1764 have all three pairs merged and all three resulting pins saturated13;1876 have all three pairs split. Mixed line classes have count zero. This follows from the complete gate loop and saved closure-size/blocked histograms, with pair classes asserted disjoint. Optional per-line diagnostic serialization failed after the complete RESULT and two eligible pools had been saved, due to a mechanical capture-screen false positive on numeric data. This analysis does not pretend to have read a missing per-line file or rerun that gate.

It follows that whenever a nonfixed raw phi pair spans a totally singular line and is merged in the current degree13 class map, its merged pin is saturated. The spanning line is phi-stable and is one of the3640 rational lines, so the corresponding all-merged/saturated line case applies.

Now let B be **any**15-point subset of a totally singular plane, not necessarily Rédei, stable, or blocking, and choose its whole-class closure C. Any phi pair fully inside B spans a singular stable line. If that pair were merged, C would contain a saturated pin and be degree-illegal. Therefore in a degree-legal C every doubly hit pair must be split. With the globally bound class interface, t>=j and |C|=15-j+t>=15>13. No such C can be used as the mandatory neighborhood of one cap13 new vertex.

This corollary is conditional on, and explicitly inherits, the saved complete line pattern plus the degree13 global class binding. It requires no additional point or plane scan. It closes all single-newvertex, fifteen-raw-point, one-singular-plane **whole-class** degree13 pin rules on this current source. It does not exclude smaller raw sets, other multi-plane shapes, unbound orientation-dependent direct images, multiple helpers, degree changes or general51458-vertex graphs. Degree12 production is unaffected.

Evidence: local `PREDICTION.json`, `RESULT.json`, `gate.py`, the companion long-side proof; `../theory/PROOF.md`, `../SHAPE.json`; `../../d13_D5_h9_transfer/{bind_source.py,RESULT.json,fold13_classes.json,CORE_COVER_TRANSFER.md}` and its `raw_map_recovery/{REPORT.md,CLOSURE_INTERFACE.json,GAUGE_RESULT.json}`. Every source traversal, class binding and line gate cited here is inherited; this paper ran none of them.
