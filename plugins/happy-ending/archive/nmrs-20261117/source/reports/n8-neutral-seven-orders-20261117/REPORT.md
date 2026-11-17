# Seven neutral I edges: endpoint and flexible third-point projections

2026-11-17. All scientific computation below ran on the authoritative Linux
server. **The final result is two genuine23-point actual Q8 domains with seven
neutral I edges, one separated and one common-gap, including full blue6/red7
arms and one shared actual p order with actual K/L membership.** Earlier
endpoint and third-point projections are retained below as intermediate work.
No global bound was improved. No independent mathematical review or acceptance
was performed; independent programs directly checked the finite witnesses.

## Final actual full-arm witnesses: seven-edge prohibitions are false

Both complete actual colorings are full ordered rank3 signotopes with no
blue7, red8 or weak8. Set P=[0,1,2,3] and T=[18,19,20,21,22]. For every
displayed I edge(a,b), the actual paths P+a+b and a+b+T are blue6 and red7,
respectively, with every triple independently checked. Every marked b neither
starts nor ends an actual ambient red7. No ambient red6 joins two marked b
endpoints, and their induced set has no blue6. A has neither red6 nor blue6.

* `full-gap`: A=[4,5,6,7,8,9,10], B=[11,12,13,14,15,16,17]. The complete
  actual I graph has43 edges:4→11 and every edge from5..10 to11..17. Its
  maximum matching is7 and includes seven edges across the same gap.
* `full-separated`: A=[4,6,8,10,12,14,16], B=[5,7,9,11,13,15,17]. The complete
  actual I graph is precisely those seven separated matching edges. Its
  maximum matching is7.

`check_full.py` independently checks all actual-color predicates and explicit
full arms. `check_p.py` constructs and directly checks one common strict order
on all253 actual pairs, every minimum incident pair p, the actual R7 split,
and the complete actual I graph/maximal matching. In both cases G is empty,
R=U=P union A, K=A, and B lies in L. Thus these are genuine R7/K/L I examples,
not merely endpoint or third-point projections. Each23-point instance uses
23,255 SAT variables; full-gap has175,098 clauses and full-separated173,340.
Kissat times were0.0645 and0.4654 seconds; direct full-color audits both PASS.

Full coloring hashes:

* `full-gap/colors.json`:
  `df8af0f290ba4a47ea538062bcaefa63a5bb9b30070b1af3a0b09f53dafc7fdb`
* `full-separated/colors.json`:
  `4d62b32960c0a60b488de1739f4d30a6dacf85621fdf03034499fb1e0976d72b`

The examples also obey the parent's new shared-tail third/last-point rules,
the interior source dichotomy and all staircase rectangle length-sum rules.
They refute an unqualified claim that seven separated or seven common-gap
neutral I edges cannot occur, even when full arms and actual shared p/K/L
are required. They are not near-capacity193/124 examples and do not refute
an additional theorem using large population, saturation or deficit conditions.

## Original input and source bridge

Primary input: `N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md` sections9.3–9.5,
`NMRS_STRUCTURAL_ROADMAP_20261117.md` sections5.3–5.5, and the R7 original
section2. These fix one actual eight-parameter domain X, a matching of I edges
(a,b), actual blue6 ending in the pair and red7 starting in the pair, and true
ambient red7-neutral right endpoints b. Y is the selected set of b labels.

Every selected endpoint coloring inherits packets, no blue7/red8/weak8, no
red7 starting or ending at b, and no ambient red6 with both endpoints in Y.
Only the induced Y is required to avoid blue6. Each I pair has the full left
blue and right red fans. The experiments preserve that distinction.

Later parent instructions supplied the following stronger necessary facts.
For every actual I(a,b), an actual interior point z satisfies
blue(a,z,b) iff z is an ambient red7 source. Interior selected a labels are
sources; interior selected b labels are neutral. Transferred actual I edges
therefore close common-gap adjacency toward later a and earlier b. Any full
matching gives the universal staircase a_j→b_k for k<=j after independently
sorting the a and b endpoints. This is an additional parent-provided bridge,
not an independent proof in this report. Its seven-edge case contains K4,4.

## Four initial endpoint models and the stronger universal staircase

All models use14 distinct endpoints and364 color variables. Color true means
BLUE in this report's programs. Independent `check.py` checks every emitted
CNF clause and recomputes each mathematical predicate directly from colors.

| Projection | Clauses | Solver seconds | Independent result |
|---|---:|---:|---|
| Seven separated pairs |210084|0.0645|PASS|
| Common gap, same-order matching |210122|0.1147|PASS|
| Common gap, reverse matching |210122|0.1143|PASS|
| Common gap, rotated matching |210122|0.1146|PASS|
| Separated plus interval monotonicity |210224|0.1147|PASS|
| Universal common-gap staircase plus all role dichotomies |210822|0.0645|PASS|

The first three common-gap examples are explicit order types; they are not
an enumeration of all7! permutations. The last staircase is a necessary
projection common to all matching permutations by the parent's closure proof.
Its SAT witness says this common necessary projection is consistent, not that
all permutations or all complete supporting arms are realizable.

The strong staircase model contains all28 staircase I pairs, their224 fan
units,56 source-interior blue units,56 neutral-interior red units, and406
interval monotonicity clauses. For x<a<b<v, the last clauses express
blue(x,a,v)>=blue(x,b,v). No claimed obstruction was obtained at this level.

## Flexible actual third points, without distinctness assumptions

`flexible.py` represents the union of14 distinct endpoint labels and14
selected witness labels t_i,c_i in at most28 ordered slots. Each label chooses
one slot. Witness labels may coincide with any other witness or any endpoint
consistent with t_i<a_i<b_i<c_i. A slot is active exactly when selected by at
least one label; active slots form a prefix. Only active points must obey the
mathematical coloring conditions. Thus unused padding is not assumed to be
an extendable actual part of X, and coincidence types are not lost.

The projection imposes blue(t_i,a_i,b_i), red(a_i,b_i,c_i), and, for every
earlier neutral b_j<b_i, blue(b_j,b_i,c_i). The last condition is necessary
because a red triple could prepend b_j to the red6 suffix of the actual red7
I witness. Every selected actual point also obeys the parent's interior
source dichotomy for every coded actual I edge. Source flags are ambient role
annotations; a true flag need not have its complete red7 witness in this
selected subset.

The separated case codes its seven actual I edges. The common-gap case codes
all28 universal staircase I edges and selects t_i,c_i for the seven diagonal
edges. Both endpoint sequences are sorted independently; no assertion about
the original matching's permutation is needed. Full blue6 and red7 supporting
paths remain outside this projection.

Path prohibitions use exact-length forward reachability with a fixed start
and shared ending pair. Actual paths imply these auxiliary predicates by
induction. Blue7, red8, neutral red7 endpoints, and Y-to-Y red6 are forbidden.
Two terminal predicates with the same endpoints and lengths summing10 are
incompatible. A separate reachability layer uses only Y points to forbid Y
blue6. This does not forbid arbitrary ambient blue6 between Y endpoints.

Both flexible instances returned SAT and passed independent `check_flexible.py`,
which checks every actual CNF clause, extracts the active coloring, and runs
fresh direct dynamic programs without importing any generator or SAT path
variables.

| Case | Variables | Clauses | Solve seconds | Active actual points |
|---|---:|---:|---:|---:|
| Separated |45493|644970|3.6731|19|
| Common-gap staircase |45493|923178|3.9238|23|

The19-point witness has

```
a = [1,3,6,8,10,14,16]
b = [2,4,7,9,11,15,17]
t = [0,0,5,0,0,13,12]
c = [3,18,18,18,18,18,18]
```

The23-point witness has

```
a = [1,2,3,4,5,6,8]
b = [9,10,11,13,14,15,16]
t = [0,0,0,0,0,0,7]
c = [20,19,12,17,18,22,21]
```

In particular, selected witnesses do coincide: c_1=a_2 in the separated
example and several t/c labels share a point. Independent audits report all
packets and coded I fans, source dichotomy, neutral bridges, global path caps,
weak8 prohibition, neutral endpoint caps, Y-to-Y ambient red6 absence and Y
blue6 absence. The separated model has maximum blue/red lengths6/7; the
common-gap model has6/6. The latter therefore does not contain any actual
red7 support at all, making its projection limitation explicit.

Color hashes:

* `flex-separated/colors.json`:
  `bd069bf27f648c6c2648b4dbaf4bce8af7aeff902e9671ed23edcd87d31979e5`
* `flex-gap/colors.json`:
  `fb7be97bc8041c4b83635744824e614eb3ace4a658d663a8cb56d9dfcb70119c`

## Actual shared minimum partners on both finite projection witnesses

For every I edge (a,b), a common actual p must satisfy a<p(a)<=b and
a<=p(b)<b. Intersecting over all incident actual I edges gives

```
p(a) in (a, min adjacent b]
p(b) in [max adjacent a, b).
```

These are intervals in the original actual order; an unselected physical
point in a gap is allowed. The endpoint-only experiments record those
intervals and do not force p to be an endpoint.

For both flexible positive witnesses, `check_p.py` goes further and constructs
one common strict order of ALL point pairs in the selected actual coloring.
Every red triple imposes ab<ac<bc and every blue triple the reverse. The
checker verifies the full order and computes every vertex's actual first
incident pair. All marked a/b interval requirements hold in that one order,
with a in U and b in L; p(U) lies in L and p(L) lies in U.

Both results are PASS. The separated model's171 pairs have each marked pair
as mutual p partners. In the common-gap model's253-pair order, all marked a
have p(a)=9=b_1 and all marked b have p(b)=8=a_7. This includes the shared
p restrictions from every staircase edge, not independently selected p
choices for different edges. These are actual p on the finite coloring;
they do not supply missing ambient full long arms.

## Evidence and stopping boundary

There is no UNSAT result, no DRAT acceptance claim, and no seven-edge
exclusion. SAT-run proof outputs are retained as raw solver output only.
All solves finished within their explicit20-second (endpoint) or40-second
(flexible) external process limits. No production runtime, sealed campaign,
existing solver process or prior evidence was changed.

Primary artifacts are each instance's `input.json` (endpoint cases),
`result.json`, `formula.cnf`, `solver.log`, `colors.json`, and independent
audit JSON. Flexible cases additionally have `pair-order.json` and
`p-audit.json`. Windows only edited and transferred files. Authoritative
execution root is
`/data/ktqiu_hdd/math_agent/reports/n8-neutral-seven-orders-20261117`.
All Python calls used `/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B`.

The earlier projection's missing full-arm obligation was subsequently closed
by the two actual models described first. The remaining research obligation
must use extra population, shared deficits or saturation beyond the seven-edge
pattern; that pattern with full genuine arms is now an explicitly verified
positive case. No unqualified seven-edge obstruction is available.
