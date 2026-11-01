# Source-ordered proof skeleton

The canonical target is the theorem stated in PROOF_AUDIT.json. All quantities are finite exact integers or rational probabilities; there are no limits, asymptotic statements, measure-theoretic interchanges, or parameter-uniformity claims. Exchanges of sums are finite.

Typed symbols: H is the original simple35-edge five-uniform hypergraph on21 points; d(v),lambda(u,v),b,e,W,tau are nonnegative integers with lambda>=1 supplied by pair coverage. Gamma is a simple graph on the35 original edge indices, q(F) its degree and s(F)=34-q(F). nj counts unordered distinct outer-edge pairs with intersection j. cj and Cj count actual middle-edge flags, retaining original indices; P=sum Cj is shared. Kd(N) is the minimum integer degree-flag cost; f and B are deterministic integer majorants. U is a rational upper bound on a conditional failure probability; U<1 is sufficient for an original-H coloring. L is half an integer objective, not a probability by itself.

Dependency DAG: original H ->15 spectra ->strong-pair dichotomy. Original H + imported q<=2 + q3/clean-star ->Gamma min4. Small-codegree branch + new/old C3 gates + shared capacities ->15-spectrum scalar ->high-center q4 contradiction. Exceptional branch ->tau/C4 errors + old/new marked C3 gate ->four-spectrum scalar ->original-H two-flip contradiction. Both branches imply target. No branch calls its own conclusion, and no scalar diagnostic is used to establish its own C3 premise.

Assumption ledger and microclaims follow in frozen source order. Each item supplies its actual caller and discharge, with old imports explicitly enumerated in PROOF_AUDIT.md.

## U01-001 — Exact theorem and contradiction scope

H has 21 vertices, 35 distinct five-edges, pair coverage and every degree >=8. These, and only these, are target premises. No criticality, lambda bound, global excess bound or certificate is added.

Status: DISCHARGED (modulo listed imports where used).

## U01-002 — Complete fifteen degree spectra

175=8b+9(21-b)+e gives b=14+e and e<=6; partition e into at most 7-e positive parts. Independently regenerated exact saved list, including 8^20,15. W at sources8,9,11,12 is651,650,655,653.

Status: DISCHARGED (modulo listed imports where used).

## U01-003 — Strong-pair dichotomy

All selected degree pairs with multiplicity and every codegree5..min(du,dv) are covered. Only four source-specific degree/codegree keys are nonstrict. Each source has exactly one unordered pair of its exceptional degrees; all other pairs are <=4 under non-B.

Status: DISCHARGED (modulo listed imports where used).

## U01-004 — Common Gamma minimum four

U04 applies to arbitrary global e; U03 supplies the actual exterior degree8 point. Combined with imported q<=2 repair this gives q(F)>=4 for every actual original edge.

Status: DISCHARGED (modulo listed imports where used).

## U01-005 — Exceptional error and C3 caller

U08 supplies tau<=142 and total C4 bonus5/6. For each triple-intersecting G,J, K not containing both exceptional endpoints meets the old local selected-degree/excess premises; K containing both lies in U09. No converse exactcross-to-valid-middle implication is used.

Status: DISCHARGED (modulo listed imports where used).

## U01-006 — Common capacities and moment domain

All Cj belong to the same original H. Their sum P is bounded once by35 boxes0..30 with total2n1. Three moment identities give U11 domain; tau row bound and397<=n1<=525 are necessary for this same H.

Status: DISCHARGED (modulo listed imports where used).

## U01-007 — Strict original-object conclusion

Every exceptional spectrum domain is strict for the actual-H two-flip criterion. The all-small-codegree case is U02. Hence contradiction for every target H; no conclusion about other21-point branches or the full36 target follows.

Status: DISCHARGED (modulo listed imports where used).

## U02-001 — Small-codegree conditional theorem

The extra all-lambda<=4 assumption is explicit here and supplied by the appropriate U01 dichotomy branch.

Status: DISCHARGED (modulo listed imports where used).

## U02-002 — Delta8 triple-middle cap

U06 covers38 selected degree multisets from all15 spectra;33 meet old local c14/c15/c16 import, five newly checked cover the remainder. Thus actual C3<=13n3.

Status: DISCHARGED (modulo listed imports where used).

## U02-003 — Shared scalar relaxation

For actual nj, use C0<=33n0, C1<=35n1-Kd, C2<=floor((S6-6)/2)n2, C3<=13n3,C4<=4n4. Descending weight fill maximizes a relaxation with one shared budget; no optimizer-realizability premise.

Status: DISCHARGED (modulo listed imports where used).

## U02-004 — All fifteen moment domains

The independently re-executed1,166,584-key scan is complete for tau<=140 and its row lower bound. Thirteen spectra strict; source13 has one residual withE70; source14 has14 residuals withE70..73.

Status: DISCHARGED (modulo listed imports where used).

## U02-005 — High-center removal of remaining keys

Actual degree14 point lies on14 distinct edges of U07 roles; all haveq>=5, other edgesq>=4, soE>=77. Degree15 similarly givesE>=78. These contradict every saved residual. No edge-criticality needed.

Status: DISCHARGED (modulo listed imports where used).

## U03-001 — Nonnegative exterior trace budget

All edges meet F, so every summand |E intersect F|-1>=0. Finite double count gives sum_z hF(z)=BF; at mostBF exterior points have positive integer deficit.

Status: DISCHARGED (modulo listed imports where used).

## U03-002 — Actual clean degree8 choice

C has outside degree8 pool>=15 andBF11; D has pool>=16 andBF10. These use e>=selected excess, never an upper e bound.

Status: DISCHARGED (modulo listed imports where used).

## U03-003 — One common actual star and six-lock map

Chosen z is fixed, has8 original edges and each is a singleton F trace. Pair coverage gives each si>=1, sum8; hence all35 positive five-compositions, eachsi<=4<=ai. Split actual edge indices and add z without changing the original H.

Status: DISCHARGED (modulo listed imports where used).

## U04-001 — Complete q3 orbit and attachment domain

Three exceptional traces are arbitrary multisets from26 masks of sizes0,2,3,4; full3276 labels and91 S5 orbits are rechecked. Safe one-red prefixes leave119 attachment keys.

Status: DISCHARGED (modulo listed imports where used).

## U04-002 — No hidden excess assumption

Fresh INTERFACE_CHECK reconstructs all119 directly from the full orbit record and filters only minimum F degree>=8. Exactly25 remain with excess histogram0:1,1:11,2:11,3:1,4:1, matching old25 keys. The <=4 filter in the older independent verifier is redundant by this independently verified fact.

Status: DISCHARGED (modulo listed imports where used).

## U04-003 — Twenty-three old and seventy new strict certificates

Replay23 accepted five-lock keys and70 actual six-lock keys using original35 distinct indices. Full C/D positive composition set equals saved set. Six-lock free vertices are15, not a reused six-degree-star denominator; maximum141/143.

Status: DISCHARGED (modulo listed imports where used).

## U04-004 — Permutation caller

All locks are actual distinct vertices, all positions distinct; zero quota, no external degree premise. The imported probability theorem turns strict finite conditional bound into a proper coloring of the original H.

Status: DISCHARGED (modulo listed imports where used).

## U05-001 — Degree-pair projection and exact traces

Independent support from spectra and degree multiplicities covers100 keys and all source IDs. Fresh check reconstructs mu0=35-du-dv+c,mu1=du-c,mu2=dv-c,mu3=c for every stored key.

Status: DISCHARGED (modulo listed imports where used).

## U05-002 — All96 strict pair gates and unique exceptions

Original-index replay verifies every one of100 pair bounds, including all nonstrict statuses. Nonstrict exactly(10,12,5),(11,11,5),(10,13,5),(11,12,5), in sources8,9,11,12 respectively.

Status: DISCHARGED (modulo listed imports where used).

## U05-003 — Report subsidiary triple scope

Its exterior z union argument and64 exact three-lock inputs have their own valid assumptions and replay;40 strict and24 nonstrict remain. These are not needed by the complete U01 proof and are not treated as H classification.

Status: DISCHARGED (modulo listed imports where used).

## U06-001 — All selected-degree support

Independent partition generation and four-point degree-count selection gives15 spectra/38 multisets. Exactly33 meet selected max<=13/excess<=4; five named exceptions are the complete complement.

Status: DISCHARGED (modulo listed imports where used).

## U06-002 — Inclusive cross budget and high traces

Actual valid middles imply exactcross total>=14. Paircap4 bounds it by16 and gives t+2p+4q<=16; henceq=0,p<=1. Same-side exactpair multiplicities>=1 come from actual outer edges.

Status: DISCHARGED (modulo listed imports where used).

## U06-003 — New complete domain and symmetry

Full inclusive/Mobius generation equals412 labels, true marked8-group yields62 representatives. Degree and traces transported together; no H automorphism assumed. t16 impossible for these five degree multisets, t15 labels24 are still generated.

Status: DISCHARGED (modulo listed imports where used).

## U06-004 — New strict replay and declared old catalogue

All62 fixed certificates replay against35 indices/1190 ordered distinct pairs, max1427/1716. Older33 degree multisets use the declared full c14/c15/c16 catalogue, not rerun in this audit.

Status: DISCHARGED (modulo listed imports where used).

## U07-001 — Complete q4 role domain

All23751 anomaly multisets per role. Exact singleton ai=di-1-hi sums30; F itself already uses each internal pointpair, so anomaly paircount<=3. Three roles exactly cover actual edges through the lone14/15 point.

Status: DISCHARGED (modulo listed imports where used).

## U07-002 — One-red/tree and fixed remaining inventory

Independently rebuild70 threshold fail sets overa0..30/r0..16. First role has no residual; other two have6 each. Tree subtraction is from the same red-event sample; all red foursets with one common anchor are distinct.

Status: DISCHARGED (modulo listed imports where used).

## U07-003 — Actual twelve-tail repair

All12 retain35 edge indices, zero quotas, old16-position menu. Replayed best bounds11203/12012 and all252 pivot minima match. No old degree-six role filter is used.

Status: DISCHARGED (modulo listed imports where used).

## U08-001 — Tau plus two

Pair coverage giveslambda>=1 andR140. C(lambda-1,2)<=lambda-1 for1..4; unique5 contributes6 instead of4. Thereforetau<=142.

Status: DISCHARGED (modulo listed imports where used).

## U08-002 — C4 total bonus without factor two

Every exceptional unordered outer pair is uniquelyK+u,K+v and injects into both u-only and v-only original edge sets. Their number<=min(du,dv)-5. Each requires at most one extra middle unit above4; no orientation doubling.

Status: DISCHARGED (modulo listed imports where used).

## U09-001 — Actual K supports and fourteen families

Fresh projection from four exceptional degree spectra recovers exactly six highpair/other-degree combinations. Same-side normalization yields6 families; cross-side different9/8 allocations retained, yielding8, total14.

Status: DISCHARGED (modulo listed imports where used).

## U09-002 — All high traces retained

Cross inclusive total<=16(same) or17(cross), with exactcross>=14, forces full4=0 and total triple<=1. Same-side sumdegrees22/23<2*5+14 excludes all6 same families; generated domain independently agrees.

Status: DISCHARGED (modulo listed imports where used).

## U09-003 — Complete425-domain equality

Independent inclusive-pair loops with markedpair exactly5 and five others1..4, all full/triple possibilities allowed by budget, Mobius recovery and nonnegative degrees/empty, equal fresh primary output and family memberships. t17 is allowed before checks and excluded by actual inventory conditions.

Status: DISCHARGED (modulo listed imports where used).

## U09-004 — All425 strict original-index certificates

All425 selected positions from fixed three-layout menu are re-executed. 8925 rows using original35/1190 distinct ordered identities, max25963/29172. No outside-degree, criticality or global e<=4 premise.

Status: DISCHARGED (modulo listed imports where used).

## U09-005 — Every original triple-intersection pair

IfK misses one exceptional endpoint, local maxdegree<=13 and selected excess<=4 verified for every four-index subset of each spectrum. Else it is a marked family. Thereforec<=13 for every pair of the same H and C3<=13n3.

Status: DISCHARGED (modulo listed imports where used).

## U10-001 — Conditional assumptions supplied externally

This scalar file alone assumes all paircaps4,C3cap13 and Gammamin4. U02 supplies each through actual-H lemmas; reading saved scalar degrees in U05 does not import these assumptions.

Status: DISCHARGED (modulo listed imports where used).

## U10-002 — Complete independent integer domain

Fresh tau/t/m scan confirms all1,166,584 keys, per-spectrum maxima and all15 residual keys. Non-strict aggregate keys are not actual H or counterexamples.

Status: DISCHARGED (modulo listed imports where used).

## U11-001 — Exceptional complete domain

tau<=142, rowlower,397<=n1<=525 and nonnegative moments; t<=47 follows from second moment, no added n4 bound. Both n1/t/m parity and tau/t/m parameterizations actually run.

Status: DISCHARGED (modulo listed imports where used).

## U11-002 — Strict bound and maxima

315870 keys, counts77912/79183/79125/79650; maxima2713662/2716104/2718702/2720004, threshold2722720. Every residual count zero; minimum margin2716. Independent grouped costs/deficit boxes match.

Status: DISCHARGED (modulo listed imports where used).

## U11-003 — Conditional C3 premise discharged

The diagnostic itself does not prove C3cap13. U01 section5 and U09 prove it for the same exceptional original H, closing the caller; no circular scalar-to-C3 inference.

Status: DISCHARGED (modulo listed imports where used).

## U12-001 — Two-intersection capacity

Every valid middle is charged at exactly two attachments in the disjoint three-point differences. Eachpoint offers <=d-1 available edges, hence2c<=S6-6. Use general formula, not A2/A3-only S6=54+e.

Status: DISCHARGED (modulo listed imports where used).

## U12-002 — Singleton-intersection cost direction

Actual tv sum n1 and satisfy tv<=C(dv,2). Each middle avoids the shared point, soC1<=35n1-sum dv tv. Cheapest degree-flag relaxation lower-bounds the sum, producing the correct upper direction.

Status: DISCHARGED (modulo listed imports where used).

## U13-001 — Full source reading and execution accounting

All11 named source files read in full. Ten frozen programs run with writes redirected solely into native/replay; original q4 CHECK read and its full-domain logic independently reproduced by audit/VERIFY. No Lean, whole-H search or recursive reviewers.

Status: DISCHARGED (modulo listed imports where used).

## U13-002 — Independent fresh actual-interface checks

Additional native INTERFACE_CHECK checks source-degree completeness, all pair trace counts, no-excess q3 domain, marked-family coverage, local generic-c14 caller and original-H integer probability normalization. All pass.

Status: DISCHARGED (modulo listed imports where used).

