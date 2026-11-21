<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Eight-parameter residual: joint slices and near-equality stability

2026-11-19. New isolated continuation of [the synthesis](NMRS_SYNTHESIS_AND_UPPER_BOUND_ROUTES_20261119.md), [RESIDUAL](../../nmrs-20261117/source/reports/n79-overlap-20261116/RESIDUAL.md), and [CASCADE-63](../../nmrs-20261117/source/reports/n79-overlap-20261116/CASCADE-63.md). No external review was invoked. Scientific programs run only on the authoritative Linux server. This report is a same-session research artifact; it does not change prior acceptance records.

## 1. Exact original-input interface

The actual residual has four-subset states of `[10]` satisfying `10 in W => 9 in W`, a 154-state universe. Its three physical layers have 70/56/28 states and hole counts alpha/beta/gamma. The current imported ordinary866 bound58 gives alpha>=12. The B-union-C layer, after deleting common present coordinate9, is the actual84-state three-subset domain on the ordered nine coordinates `{1,...,8,10}`. Write its population as66-e; the nine common-present2x6 faces each have population<=22, hence e>=0. The exact residual population is

`154-alpha-(18+e)=124-(alpha-12)-e`.

These are actual subsets of one mother input. No reverse realization of a hole pattern is used.

## 2. A quantitative extension of the66-point corner rigidity

Fix the actual pair labels sigma on an admissible3x6 assignment with66-e occupied states. Define, point by point,

`I_min(v)=down{sigma(u,v):u<v}`,

`I_max(v)=G \ up{sigma(v,w):v<w}`.

The existing admissibility argument of RESIDUAL section6 applies with the same labels and point order: both assignments remain admissible and injective, and

`I_min(v) subseteq I(v) subseteq I_max(v)`.

It is essential that the same labels occur in both definitions. For any of the three assignments J, let d_t(J) be the number of occupied three-subset states containing coordinate t, and put

`delta_t(J)=22-d_t(J)` for1<=t<=9.

Each delta is a nonnegative integer by the actual2x6 face theorem. Because every state has three coordinates,

`sum_t delta_t(J)=9*22-3*(66-e)=3e`.

For a three-subset state W the ideal area is `sum(W)-6`. Therefore

`sum_v |J(v)| = 22*(1+...+9)-sum_t t*delta_t(J)-6*(66-e)`

`=594+6e-sum_t t*delta_t(J)`.

The weighted deficit lies between3e and27e. Taking the maximum possible area for I_max and minimum possible area for I_min proves

**Joint stability lemma.**

`sum_v |I_max(v) \ I_min(v)| <=24e`.

Consequently at most24e point-states can fail to be fully frozen. When e=0 this recovers the exact pointwise equality of RESIDUAL. When e=1, at least `65-24=41` of the65 physical points satisfy

`I_min(v)=I(v)=I_max(v)`.

Every removable corner at a frozen point is attained by an actual incoming pair; every addable corner is attained by an actual outgoing pair. Indeed a maximal cell of a generated ideal must itself be one of its generating labels, and the complementary assertion follows from the minimal cells of the outgoing up-set.

There is also an actual-deficit refinement. Put `s=sum_t t*delta_t(I)` for the original middle assignment. Then

`sum_v |I(v) \ I_min(v)| <=27e-s`,

`sum_v |I_max(v) \ I(v)| <=s-3e`.

Their sum is the same24e bound. This retains where the three units of face deficit lie when e=1. The lemma is a stability constraint, not a contradiction or a claim that65/66 points exist.

### 2.1 Two-sided actual ranks, stronger simultaneous rigidity

For the actual ordered858 point set, including a physical residual slice with ranks recomputed there, put `M_blue=3,M_red=6`. For the exact pair `(u,v)`, let `l_c(u,v)` be the maximum number of edges of a color-c path ending at this pair, and `f_c(u,v)` the maximum number starting at this pair. Set `u_c(u,v)=M_c+1-f_c(u,v)`.

Concatenating along this identical pair counts the shared edge once, so `l_c+f_c-1<=M_c` and `l<=u` componentwise. Both l and u take values in the same3x6 rectangle and strictly grow on their corresponding colored triples. They therefore produce admissible incoming-minimal and outgoing-maximal ideal families, with `I_min(l) subseteq I_min(u) subseteq I_max(u)`.

Any bounded admissible sigma satisfies `l<=sigma<=u`: grow sigma along an actual maximum ending path for the first inequality and along a maximum starting path for the second. Thus every admissible assigned ideal I has the common envelope `I_min(l) subseteq I subseteq I_max(u)`. The same face/area calculation proves

`sum_v |I_max(u)(v) \ I_min(l)(v)|<=24e`.

For e=1, at least41 physical point-states are consequently frozen simultaneously for all bounded admissible pair labels and ideal choices on this fixed actual coloring and point order.

When e=0, all four families `I_min(l),I_min(u),I_max(l),I_max(u)` and every admissible assigned ideal are equal pointwise. At the second point, the incoming l-ideal is exactly `{(1,1)}`: its sole prior pair has ending ranks `(1,1)`. Equality forces the same pair's u-label to be `(1,1)`. Hence the **same first pair** starts an actual blue4-point path and an actual red7-point path. The last pair has forward ranks `(1,1)`, so its u-label is `(3,6)`. Equality of outgoing-maximal ideals at the penultimate point forces its l-label also to be `(3,6)`. Thus the **same last pair** ends an actual blue4 and an actual red7 path. Their other ends are not asserted to coincide.

Every full22-point coordinate face supplies an actual red7: compressed labels exclude blue4, while the elementary cup-cap bound for avoiding blue4 and red7 is `binom(7,2)=21`. This applies to all nine faces at e=0. At e=1 the nonnegative face deficits sum to3, so at least six faces remain full22 and supply red7. Different faces' supplied paths can intersect or coincide; no disjointness or additive fee follows.

## 3. Exhausting the horizontal short-cap blocks does not by itself exclude66

The isolated [generator](../SOURCE_MAP.md#excluded-sources) imports the frozen native trace generator whose SHA256 is `73d5acace0e342c063de62a932c5e75f0c5525bb7dce4daba4f285c75ac73478`. It explicitly generates all horizontal2x6-to3x6 threshold sequences. There are exactly24, agreeing with RESIDUAL section5. It adds all native trace rows through ordinary coordinate-deletion depth1 and all coordinate2x6<=22 and3x5<=51 slice bounds. After deduplication the relaxation has84 hole variables and563 rows.

The Linux run found the following18-hole set, then checked every inequality with integer set intersections:

```
139 149 158 159 169 179
235 237 246 248 268 269
347 358 367 456 478 578
```

Each of the nine coordinate degrees is exactly6. Thus all nine22-point faces are simultaneously saturated in this *hole relaxation*. Every3x5 coordinate slice has12 holes: deleting coordinate t keeps18-6=12 holes. The same displayed witness therefore also satisfies the tightened current3x5<=50 demand6, although the original probing matrix recorded51.

The witness satisfies all24 horizontal blocks and every generated native trace. It is **not** a signotope, a pair-label realization, or a66-point construction. Its exact feasibility proves the precise limitation that this named set of occupancy inequalities cannot exclude66. The LP and integer optimizer both reported objective18, but this limitation uses the explicit integer witness and elementary face lower bound18, not floating optimization as a proof.

## 4. Whole154-state necessary models and actual execution

The same generator builds all native positive-demand traces through depth2, all common-coordinate numerical bounds866<=58,867<=104,858<=66,857<=51,848<=22, and every horizontal2x6-to4x6 block. There are295 threshold maps before deduplicating their surviving supports. For a block K with forbidden structural states, it adds precisely

`sum_{W in K intersect U} h_W >=6-|K outside U|`,

or equivalently `>= |K intersect U|-22`. Nonpositive demands are omitted. This pays each structural omission once and keeps all hole variables in the same154-state mother.

The deduplicated model has1605 rows. LP reported30. The90-second integer run timed out with a34-hole feasible point; that point was exactly checked. The timeout is not an exclusion of30/31 holes.

Separate controlled external AE queries were then built from the1605-row model, tightening857 to50. Both completed their75-second internal time limits with exit0 and UNKNOWN:

| Hole budget | Variables | Clauses | Exact CNF SHA256 | Result |
|---:|---:|---:|---|---|
|30|24542|47607|`d707a36a34d4625e9c8f93a8b44641248635ef9919cbe5a8d6899a22115c8f3e`|UNKNOWN|
|31|24635|47791|`50ad2c2d51eada9600f5da2d5802631a3853e1bb73a4619fcfbf97c695c70c7e`|UNKNOWN|

No DRAT check was invoked for these UNKNOWN queries. The source [satprobe.py](../SOURCE_MAP.md#excluded-sources) uses only PySAT cardinality encoding; the solver is the authoritative external AE executable, not an in-process PySAT solver.

## 5. Strengthened local866 face import

The [second builder](../SOURCE_MAP.md#excluded-sources) maps all641 pure local866 necessary supports and2876 positive Hall clauses from the frozen full-H11 input snapshots into each of the45 two-excluded-coordinate4x4 faces of the same154-state mother. Source IDs are decoded using the frozen `base/metadata.json` column heights, re-encoded as four-subsets of `[8]`, and lifted through the increasing remaining-coordinate map. A clause containing a forbidden structural state is already satisfied and omitted. Mapped duplicates are removed.

Only the pure local supports and `hall_clauses` are read. Original-P endpoint units, full-base counters and negative literals are excluded. The numerical866<=58 whole-face restriction remains justified separately by the ordinary capacity import. Source hashes and counts are written before solving in each query's `import-bindings.json`.

There are31050 genuinely new mapped clauses after deduplication against the original demand1 rows, giving32655 total rows. Both strengthened queries also returned UNKNOWN after their75-second AE limits, with no proof-check claim:

| Hole budget | Variables | Clauses | Exact CNF SHA256 | Result |
|---:|---:|---:|---|---|
|30|24542|78657|`d5a049146b351a9bd87e57409b3f4dc84615b7871255bacff23b5efffd7ca633`|UNKNOWN|
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]

Their identical mapped-row snapshot SHA256 is `5d7de3f1872555e2693954a6e364a717f3d25a583f78510a677bac1fd2d124e2`. The raw [H30 result](../SOURCE_MAP.md#excluded-sources), [H31 result](../SOURCE_MAP.md#excluded-sources), import bindings and full solver logs are retained with the row snapshots. No process remains running after these bounded calls. In particular the strengthened model has neither an infeasibility proof nor a feasible30/31-hole witness; its mathematical optimum is not established.

## 6. Caller and remaining gap

With current C8<=190,D8<=124, the working exports remain Q8<=314,F8<=315,ES8<=316 unless a new residual exclusion is actually checked. The stability lemma isolates the near-equality label budget on the only e=0/1 branches relevant to a two-point joint gain, but does not close those branches.

The exact18-hole witness rules out repeating only the563-row858 occupancy optimization. A genuine next constraint must use actual shared pair labels/corner attainment, a new valid hereditary support, or a stronger imported theorem. A solver UNKNOWN does not establish inadequacy of the whole154-state integer model and is not a mathematical obstruction certificate.

All new artifacts are isolated in [the evidence directory](../SOURCE_MAP.md#excluded-sources). The authoritative scientific root is `<private-artifact-root>`. Existing sealed jobs, encodings and proof bindings were not changed.

[Operational connection details omitted from this publication excerpt.]

## 7. New interval and repeated-height guarded theorem

The parent supplied a genuine extension of TRANSLATED-PATHS section5.2. This section records the complete used argument and its actual finite tests. Take an admissible a-by-b assignment and integers

`0<=lo<v_a<=...<=v_1<hi<=b`.

Let d be the number of distinct v-heights and put `t=d+hi-lo-m`. Assume t>=0 and, in the applications here, d>=2. Set

`Y=(v_2,...,v_a,lo), S=(v_1,...,v_(a-1),lo)`,

`P=(hi,v_2,...,v_a), E=(hi,v_1,...,v_(a-1))`.

Raise the first through(a-1)st columns from Y to S, skipping exactly the zero steps at equal adjacent heights. This gives d states. Similarly raising the second through ath columns from P to E gives d states. The difference S<P still contains cells only in its first and last columns: the first-column heights exceed v_1, the last-column heights do not exceed v_a.

If the actual shared pair label sigma(S,P) takes the last column, the first private chain followed by P is a blue(d+1)-path. Its successive incoming red-coordinate intervals decrease, and the last bridge interval lies below all preceding intervals. Its red companion on the same endpoints Y,P is

`A_r=sort(v_2,...,v_a,r), lo<=r<=hi`,

with hi-lo+1 states. Each unit r-step adds one cell, whose active column moves only toward the first column. Thus consecutive red-path labels have nonincreasing first coordinates, forcing red. The blue and red interiors are disjoint, and their union has d+hi-lo states.

If sigma(S,P) instead takes the first column, the bridge followed by the second private chain is blue(d+1), with red companion

`C_r=sort(v_1,...,v_(a-1),r), lo<=r<=hi`,

on the same endpoints S,E. Its union has the same size. These are the two exhaustive cases for the *same actual bridge pair*.

The argument survives any deletion of at most t internal vertices from the selected union, provided S and P remain. Skipping private-chain vertices merges adjacent decreasing red-coordinate intervals; skipping red-chain vertices merges intervals of nonincreasing active-column positions. The corresponding inequalities still force blue/red. At least m distinct occupied states remain; they may be trimmed to m while retaining the bridge and common endpoints. This gives a weak-m witness. **S and P are routing anchors and cannot be skipped.**

Write B_L,B_R for the two internal support sets after deleting the four anchors. With all four anchors occupied, it follows that

`|holes intersect B_L|>=t+1 OR |holes intersect B_R|>=t+1`.

More accurately, if S,P are occupied and the bridge label is last-column, then Y is missing or the left deficit is>=t+1; if it is first-column, E is missing or the right deficit is>=t+1. This is the routed condition actually implemented below. Structural forbidden states are paid in the corresponding branch exactly once, reducing that branch's threshold by their number. A forbidden routing anchor makes that instance inactive.

For an interval with v=hi-lo-1 available heights, the number of a-multisets with exactly d distinct heights is `binom(v,d)*binom(a-1,d-1)`: choose the support, then its positive multiplicities. This count does not justify copying distinct-height red-face incidence bounds into the repeated-height case. In particular two repeated-endpoint insertions can have the same sum; no false per-residue uniqueness is used here.

The [guard builder](../SOURCE_MAP.md#excluded-sources) checked all source differences and every set of at most t skipped internal vertices, retaining S/P. It used every allowed interval, reflection, color transpose and common-coordinate subdomain of total size at least8. For858 this produced156 distinct guarded disjunctions. They do reject the old18-hole witness: guard26 has v=(5,3,2), interval[0,6], reflected, and requires one of two branch deficits to reach2.

However the new858 formula is SAT at H18, with a different18-hole witness. Thus rejection of the old witness is a real new constraint but not a new capacity bound.

### 7.1 Sharing the actual bridge labels across inherited uses

The [route builder](../SOURCE_MAP.md#excluded-sources) strengthens independent disjunctions by assigning each identical physical comparable pair S<P one shared mother-grid label choice in `I(P)\I(S)`. A chosen cell enforces the appropriate branch deficiency or endpoint omission in every use of that pair.

For a coordinate-erased subdomain, the image of each source cover cell is reconstructed as the difference of its two lifted mother ideals. These fibers are checked nonempty and pairwise disjoint. Their union on each bridge is checked to be exactly that bridge's mother-grid difference. Reflection reverses the comparable pair and rotates the source cells; transpose exchanges their coordinates. Thus labels are transported by actual difference fibers, rather than treating projected first/last columns as unrelated Boolean choices.

On858 there are98 shared bridge pairs and656 branch implications from328 unmerged template instances. The H18 query remains SAT. On the154-state residual there are125 shared pairs and1016 branch implications from508 instances; the H30 query returned UNKNOWN at75 seconds. The simpler201-disjunction residual H30 and H31 queries also returned UNKNOWN.

| Query | Variables / clauses | Outcome | CNF SHA256 |
|---|---:|---|---|
|858 guarded H18|9362 /18015|SAT, all clauses and guards checked|`63268243abc2dd12fb8971aa4b648e26fcad4bb1ccd25c290a478af1803886bd`|
|858 shared routes H18|9962 /19497|SAT, all clauses and guards checked|`d3ff6bfa8aa656e34f5abda5f22d9a78ae6f1e8bf31286e0585b5d8fdf156d84`|
|D8 shared routes H30|25556 /81494|UNKNOWN|`d915d3f6534719d68758c694abddbc7be02dde31f03b10f4f2d00f335431ef53`|

## 8. Actual saturation consumed through complete six-point templates

The parent's stronger rigidity suggestion was then implemented, rather than leaving section2 as an unused observation. In an actual66-point858 input, the first k points' incoming ranks are unchanged by later points. By simultaneous rigidity their occupied states must therefore contain the canonical incoming ideals of the actual induced k-point signotope. The last k points analogously contain the reflected complementary ideals of a reversed canonical k-point input, using the actual outgoing envelope. For k=6, all2^20 colorings of the twenty lexicographically ordered triples were enumerated. Every four-packet was checked for at most one sign change. There are908 legal colorings; filtering blue5 leaves843. Their canonical incoming ideal supports have284 distinct patterns.

The [first endpoint model](../SOURCE_MAP.md#excluded-sources) existentially selects one entire front template and one entire back template, requires all their states occupied, forbids intersections between the two physical six-point supports, and requires the four extreme states000,100,665,666 occupied. Adding these to all shared-route constraints remains exactly SAT at H18:10530 variables,23055 clauses, CNF `c3931b96ce414626b4aabd47c43db517a5be4e91a33c217e97fb54ca9d309413`.

The [stronger endpoint model](../SOURCE_MAP.md#excluded-sources) retains all843 color tables and their fifteen actual pair ranks. Here the global shared labels may be chosen to be actual incoming ranks l. A selected front table therefore fixes its internal shared-pair labels exactly. A selected reversed back table imposes the valid upper bound `l<=u=M+1-forward_rank`; it does **not** impose l=u. Every shared bridge pair has a unique selected cell.

[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]

```
139 146 159 167 179 189
237 247 249 258 268 269
345 356 357 358 468 478
```

The selected front color mask is7295; its six canonical ideals, in actual point order, have words `123,124,125,126,136,236`. The reversed back color mask is11455; its incoming word sequence is `123,124,125,126,156,235`. The corresponding original suffix words, in actual chronological order after full-grid reflected complementation, are `578,459,489,589,689,789`. The templates are disjoint, all their states avoid the displayed holes, and each complete representative color table and all fifteen pair labels are stored in the [actual result](../SOURCE_MAP.md#excluded-sources) and [complete library](../SOURCE_MAP.md#excluded-sources). Mask bits use the lexicographic triple list stored with the library, with bit0-color blue and bit1-color red.

This is a feasible necessary model with explicit endpoint templates and selected shared-pair route labels. It is not a66-point signotope: it does not assign one full global point order, all pair labels, all triple colors and all corner attainments. Thus the new tests locate the missing coupling beyond k6 endpoints and the selected bridge labels, and do not certify that every label/corner condition is realizable. No larger-k enumeration or longer replay of the same H18 model was started.

### 8.1 Legitimate transport back into the H30 residual branch

For a true residual with H<=30, alpha>=12 and the B-union-C face lower bound18 force alpha=12 and e=0. The same six-point template membership can therefore be imposed on its84-state B-union-C slice. The source states are lifted by adding common coordinate9 and mapping the nine remaining positions through `{1,...,8,10}`.

The residual's inherited mother labels need not be actual incoming l on that slice. Consequently the [residual endpoint builder](../SOURCE_MAP.md#excluded-sources) uses only the legitimate envelopes: front-table l<=compressed sigma and compressed sigma<=back-table u. It maps each comparison back to mother label cells using the common9 deletion fibers. It does not force the inherited label equal to the front-table l.

The actual query has27242 variables and93034 clauses; CNF SHA256 `19e52c4e24db38becf3264796289b1bac5106ddd54df88456deca79c5a419008`. AE reached its75-second limit with exit0 and UNKNOWN. Its [raw result](../SOURCE_MAP.md#excluded-sources), full library and solver log are retained. No DRAT check was claimed, no solver remains running, and there is no D8 numerical improvement from this branch. C8/D8/Q8/F8/ES8 remain190/124/314/315/316.

The848-face saturation and k6 front/back information have now been actually consumed, including shared-pair label envelopes. The next missing physical requirement is a common realization of the entire remaining point order, all pair labels/colored triples and attained corners. Enlarging k without a new reason is not the recorded next action. The explicit18-hole witness and templates above must be preserved as a falsification test for proposed inequalities using only the modeled conditions.

## 9. A new whole-input physical condition: saturated-face blue4 witnesses

The parent supplied the following further physical condition at closure; it is proved here and no extra solver campaign was launched for it. In an actual66-point858 input, let F_j be one of its nine full22-point coordinate faces. It contains no blue4 by the compressed2x6 label bound. Baek's23-point theorem, with the mother's red8/weak8 exclusions inherited by every subset, implies that **every23-point subset of the mother contains an actual blue4**. Hence F_j is a maximum blue4-free set of the whole mother, not merely a maximum compressed face.

For every physical point x outside F_j, the23 points F_j union{x} contain an actual blue4. Since F_j itself contains none, that blue4 consists of x and three points of F_j. More generally, if A is a set of external points and Z is a subset of F_j with |A|>|Z|, then

`(F_j \ Z) union A`

has at least23 points and contains an actual blue4. This is a simultaneous exchange obstruction for the actual blue4 hypergraph of the mother. It uses the same physical F_j,A,Z; independently optimizing replacement sets does not give the statement.

There are `9*(66-22)=396` single-external-point requests labeled by(j,x). Any fixed actual blue4 can serve a request only if coordinate j occurs in exactly three of its four three-subset states; the unique point whose state omits j is then the uniquely served external x. The four states contain exactly12 coordinate incidences. Therefore at most `floor(12/3)=4` coordinates can have degree3, and a fixed blue4 serves at most four requests. It follows that the mother contains at least

**`ceil(396/4)=99` distinct physical blue4 point-sets.**

If one blue4 serves four requests, those four coordinates account for all12 incidences. Its four distinct states are consequently all three-subsets of that same four-coordinate universe. Conversely, whenever those four states are occupied, they form the familiar3x1 blue chain after common coordinate deletions, so all four possible served coordinate requests have the required three-in/one-out incidence pattern. The proof of the99 lower bound needs only the forward implication and does not claim a bound on how many such tetrahedral supports can coexist.

For e=1 at least six faces remain full22. Each has43 external points, giving at least258 labeled requests and at least `ceil(258/4)=65` distinct physical blue4 point-sets. The stronger exchange condition applies in each of those six faces as well. These actual blue4 requirements are absent from the occupancy/prefix/shared-selected-bridge SAT formulas above; the displayed18-hole patterns are not certificates satisfying them.

A useful general version separates the hypotheses. Suppose an actual mother's states are injective a-subsets, and every(B+1)-point subset contains a blue(a+1)-path, while K named coordinate faces have exactly B points and contain no such path. Every face is then a maximum independent set in the physical blue(a+1) hypergraph and obeys the same exchange rule. A fixed physical blue(a+1) witness can serve a single-external request only at a coordinate of degree a in its(a+1) states. Its total incidence is a(a+1), so it serves at most a+1 requests. Thus there are at least

`ceil(K*(n-B)/(a+1))`

distinct physical blue(a+1) witnesses. Equality in this service bound forces its states to be exactly the a-subsets of one(a+1)-coordinate universe. The universal(B+1)-point forcing hypothesis must be proved or imported for the mother's original forbidden objects; it cannot be inferred from a numerical compressed-face capacity alone. The858 application above has this hypothesis directly from Baek with a=3,B=22.

### 9.1 Balanced-incidence refinement: at least104 physical blue4s

The balanced worker supplied the following strengthening, checked here with the exact inequality directions. At e=0 the18 missing three-subsets have degree6 at each of the nine coordinates. Let P count pairs of distinct holes whose intersection has size2. Summing over coordinates counts each hole pair according to its intersection size, so

`2P <= sum_(j=1)^9 binom(6,2)=135`,

and P<=67. Each missing triple is contained in exactly six four-coordinate sets. Thus there are108 hole/four-set incidences. Two missing triples belong to a common four-set exactly when they intersect in two coordinates, in which case that four-set is unique. The two-term inclusion-exclusion lower bound shows that at least `108-P>=41` four-sets are hit by a hole.

There are `binom(9,4)=126` four-coordinate sets altogether. Hence the number F of complete tetrahedral state supports, with all four of their three-subsets occupied, satisfies

`F<=126-41=85`.

Let B be the total number of actual blue4 point-sets and B_4 the number serving four of the396 labeled requests. By the service-four characterization B_4<=F; all other blue4s serve at most three requests. Therefore

`396<=3B+B_4<=3B+F<=3B+85`,

and **`B>=ceil((396-85)/3)=104`**. This supersedes99 as the stronger e=0 bound; they are not additive. The refinement needs only that every four-serving witness has a complete tetrahedral support. It does not need a converse asserting that every complete tetrahedron serves four requests.

### 9.2 Exact red endpoint sets and cross-end physical blue arms

Continue with an actual66-point858 input and its common rigid ideal assignment `D=D_min(l)=D_max(u)`. Let S_R,E_R be the actual points starting/ending a red7 path, and S_B,E_B those starting/ending a blue4 path. Paths here are existential over all actual paths, with no chosen representative. Write the three column heights of D(v) as lambda_1>=lambda_2>=lambda_3.

The first-column height equals6 exactly when an incoming pair has red ending rank6. Consequently

`lambda_1(v)=6 iff v in E_R`.

In the three-subset encoding, this is exactly membership in coordinate face F_9. At the other end, `lambda_3(v)=0` exactly when cell(3,1) is absent from D_max(u)(v). By the definition as the complement of the outgoing up-set, this means some actual outgoing pair has u-label componentwise at most(3,1). Its red coordinate must be1, equivalently its actual forward red rank is6. Thus

`lambda_3(v)=0 iff v in S_R`,

which is exactly membership in F_1. In particular **`S_R=F_1` and `E_R=F_9`**, both of size22.

A red7 starting at v cannot coexist with a blue4 ending at v. If its first next point is r and the blue path's previous point is b, examine the single actual seam triple(b,v,r). If blue, append r to the blue4 and obtain blue5; if red, prepend b to the red7 and obtain red8. Both are forbidden. Reversing the roles gives the dual exclusion: a red7 ending at v cannot coexist with a blue4 starting at v. Therefore

`E_B subseteq X\S_R` and `S_B subseteq X\E_R`.

Now use the saturated-face physical witness theorem, rather than only the numerical face capacities. For x outside F_1=S_R, the required blue4 in F_1 union{x} uses x and three F_1 points. None of those three F_1 points can be its last point by the seam exclusion. Hence x is its last point. This proves the reverse inclusion for E_B. Similarly, for x outside F_9=E_R, the required blue4 with three F_9 points must start at x. We obtain the exact identities

**`S_B=X\E_R` and `E_B=X\S_R`.**

Define `T_B:=S_B intersect E_B`, meaning points that can both start a blue4 and end a blue4. This definition must not be confused with points merely internal to some blue4. Every x in T_B has an actual incoming blue4 with its other three points in S_R and an actual outgoing blue4 with its other three points in E_R. These two arms are joined at the *same physical x*. The common-arm statement is existential at each x; no disjointness between arms belonging to different x is claimed.

Their cardinality is exact:

`|T_B|=66-|S_R|-|E_R|+|S_R intersect E_R|=22+|F_1 intersect F_9|`.

The common face consists of three-subset states containing coordinates1 and9, so it has at most seven states. Thus **`22<=|T_B|<=29`**. This is a whole-input cross-end path conclusion, not another occupancy bound.

There is a useful universal seam consequence for any selected pair of these incoming/outgoing blue4 arms. If the incoming arm is a_1<a_2<a_3<x and the outgoing arm is x<b_2<b_3<b_4, then the actual triple(a_3,x,b_2) must be red. If it were blue, the five physical points a_2,a_3,x,b_2,b_3 would form a blue5, using the blue arm triples on either side of that seam. This holds for every pair of such actual arms at x; it does not replace their complete supports by one representative.
