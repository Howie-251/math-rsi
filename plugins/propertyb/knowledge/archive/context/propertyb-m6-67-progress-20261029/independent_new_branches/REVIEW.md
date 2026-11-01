# Independent review: complete35-point branch and34/min11

**Verdict: PASS_WITH_DECLARED_IMPORTS (same-family/provisional).** The complete35-point branch (actual minimum degree7–11) and the34/min11 branch are mathematically covered by the supplied proofs. Every required local type has a strict independently replayed rational bound. No new gap was found. This does not by itself certify the full m(6)≥67 target.

Inputs read: `root/PROOF35_MIN9.md`, `root/LOW_PAIR_CENTER35.json`, its generator and component kernel; the minimum-eleven section of `mid34_38/STATUS35.md`, `MIN11_35.json` and its generator; `34_min11/REPORT.md`, `CERTIFICATE.json` and its generator. The actual minimum-unit-neighbor adaptive mechanism is an explicit import, and its complete 35/min9 continuation domain is replayed here rather than silently assumed numerically.

## 1. 35 points, minimum degree nine

The actual degree excess is exactly396−35·9=81. Fix a degree-nine point x. When it has a unit neighbor of degree at most eleven, the prior actual minimum-unit-neighbor argument applies. The independently reconstructed exact domains are:

- partner degree9: common pool lower11, third degree9,…,16, both actual triple traces (16 types);
- partner degree10: common pool lower6, third degree10,…,19, both traces (20 types);
- partner degree11: common pool lower1, third degree11,…,46, both traces (72 types).

All108 retained layouts are replayed and strict. The generator's degree assignments are checked to be permutations of the original degree tuple. Thus the prior cases are genuinely closed, not merely referenced as table successes without their actual caller.

For the remaining case, all actual unit neighbors A of x have degree at least twelve. Let u=|A|. Pair-cover gives total row excess45−34=11 and u≥23. Charging three degree-excess units to each member of A gives3u≤81, hence23≤u≤27.

There are n=34−u nonunit partners. If l have codegree exactly two, then their row excess is at least l+2(n−l); hence l≥2n−11=57−2u. If all those l points had degree at least eleven, the actual degree excess would be at least

$$3u+2l\ge114-u\ge87>81.$$

The sets counted are disjoint because those partners are nonunit and lie outside A. Therefore some actual codegree-two partner y has degree e=9 or10. This verifies the requested low-partner existence, including the full81-unit budget; it does not presume an arbitrary integer profile is realizable.

For y, at most5e−34 partners are nonunit, and x is one of them outside A. Therefore its actual common unit pool C with x has size at leastu+35−5e. This is at least13 for e9 and8 for e10. Charging A at degree twelve and y separately leaves at most81−3u−(e−9) extra units. An actual lowest-degree member z of C consequently has

$$12\le d(z)\le12+\left\lfloor\frac{81-3u-(e-9)}{u+35-5e}\right\rfloor.$$

For e9 this upper bound is twelve throughout the feasible u range. For e10 it is at most thirteen. The infeasible e10,u27 budget is negative and is correctly excluded rather than interpreted as a negative upper degree. Every feasible integer u,e case is independently checked and saved in CHECK.json.

Thus the complete necessary three-lock degree domain, labelled z,x,y, is(12,9,9),(12,9,10),(13,9,10). Both center–endpoint codegrees are one, the other is two, and the triple multiplicity is zero or one. These are exactly the six recorded local types. Each actual trace is independently rebuilt from degrees and codegrees, agrees with the certificate, and its injection-probability bound equals the submitted fraction. Maximum14882237/14887440<1.

## 2. 35 points, minimum degree eleven

Let R be the actual degree-eleven points, r=|R|. The total degree gives396≥420−r, hence r≥24. Every R-point has at most55−34=21 nonunit partners, so it has at least r−1−21≥2 unit neighbors inside R. A specified actual unit edge in R satisfies

$$110<2\cdot35+2\cdot24-6=112.$$

The previously proved fixed-unit-edge weak-wedge lemma therefore applies to that same edge and R. It produces three actual degree-eleven locks whose pair codegrees are all one or have exactly one doubled pair. The triple multiplicity is zero or one. This is exactly the8 labelled records (the two all-unit records are repeated under the irrelevant doubled-pair index, as declared).

Every multiset trace is rebuilt from those actual pair capacities; all8 recorded bounds equal the independent injection calculation using the original max-of-avoided-pool quota. All are strict, maximum13429/13485. No fourth-lock continuation is required or assumed.

## 3. 34 points, minimum degree eleven: harmonic extremum

The proof's sets are actual degree classes: R has degree11, A degree12/13, C degree at least14. The excess22 gives r≥12, b=a+c≤22, a+3c≤22 and c≤7. If an R-unit pair exists, the first certificate row finishes it. Otherwise R has no unit pair.

Each R-point has at least11 unit partners, all outside R; since c≤7, at least four are in A. Thus a>0. Its actual total unit degree u_x satisfies11≤u_x≤b, making all denominators in the proof positive.

Assume no A-centered unit wedge has two R endpoints of codegree two. Those endpoints cannot have codegree one by the current R assumption, so every such wedge has endpoint codegree at least three. Along each actual unit edge xz from R to A, baseline codegree two on all33 partners of x, corrected for its u_x actual unit entries and the t_z−1 other R-neighbors of z, gives

$$55\ge66-u_x+t_z-1,\qquad t_z\le u_x-10.$$

These positive t_z denominators are used only on actual edges. Summing reciprocals counts a_+, the positive-degree A-points, not all A-points; the proof correctly begins with a≥a_+. Since at most c unit neighbors of x lie in C,

$$a\ge\sum_{x\in R}\frac{u_x-c}{u_x-10}
\ge\frac{ra}{b-10}.$$

The last inequality usesu_x≤b andc<10; the exact difference is

$$(u_x-c)/(u_x-10)-(b-c)/(b-10)
=\frac{(10-c)(b-u_x)}{(u_x-10)(b-10)}\ge0.$$

Sincea>0, this forcesb−10≥r=34−b, henceb≥22. Equality of the degree budget givesb22,r12,a22,c0 and every outside degree12. The reciprocal chain now has equal endpoints. The displayed difference is strictly positive whenu_x<b, so everyu_x=b22. Therefore every R-to-outside pair is unit. The absence of the first wedge then forces every R-pair codegree at least three, and each R row has33 remaining incidence units on11 R-partners, forcing all those codegrees exactly three. The proof's rigidity conclusion follows. A complete independent integer check of the cardinality envelope leaves only(r,a,c)=(12,22,0), saved in CHECK.json.

In the rigid case, fix one degree12 outside point z. Its incident edges partition the12 R-points into disjoint nonempty groups, each of size at most five, because every R-point meets z exactly once. At least three groups are necessary. Selecting one R-point from each of three distinct groups excludes every original edge containing z and two selected R-points. This supplies the actual four-lock interface; it is not an assumed trace restriction.

The selected three R-pairs have codegree three; the z-to-R pairs are unit. The only remaining triple trace is the three R-points, multiplicityτ=0,…,3. Singleton and empty multiplicities are forced as in the paper. This gives exactly four rigid types. Together with one unit-pair type and four low-center wedge types, the complete domain has nine types. Their reconstructed actual traces and independently replayed fractions match every submitted row. All are strict, maximum309781/310155.

## 4. Arithmetic scope and imports

`check.py` writes `CHECK.json`, which includes all replayed fractions and the complete35/min9 integer-budget cases. The initial execution took about0.403CPU seconds and verified6+108+8+9=131 rows; the incremental complete35 audit is recorded below. The new tables6,8,9 are exactly equal fraction by fraction to their supplied values. The prior108 adaptive rows are replayed with independently implemented max-R or exact joint deductions as necessary; every chosen bound remains strict, with maximum29774683/29774880.

The injection kernel is the established pre-existing independent falling-factorial implementation, loaded without executing submitted generators. It is distinct from the binomial conditional-probability implementation that generated the two35-point tables. The34/min11 author already used this same pre-existing injection primitive and also supplied a binomial-kernel replay; this review separately reconstructs its complete actual domain and replays it, but does not claim a third new probability formula for that branch.

Component-support bounds and quotas are declared imports. This auditor authored the component lemma, so this document is not its independent mathematical audit. Separate independent component/table audits exist in `integer_lock_check` and `independent31_33`; their status is maintained by root. Original conditional greedy witness, original-input reduction and the established weak-wedge lemma are also named imports.

All successful probabilities refer to the same actual selected locks and actual original edge traces. Strictness therefore produces a successful actual ordering and a legal coloring, as in the imported probability theorem. No external model, Lean, original-hypergraph enumeration or second-machine reproduction was performed here.


## 5. Increment: complete35/min10 proof

Read the frozen `mid34_38/PROOF35_MIN10.md` and `CERT35_MIN10.json`, which replace the old open discussion for this minimum degree. All three numerical domains are independently reconstructed.

First, a unit pair x,y of degree ten cannot be treated as a directly strict two-lock certificate. The proof correctly continues it to an actual unit triple: x has at least eighteen unit neighbors, so at least seventeen after removing y, whereas y has at most sixteen nonunit partners. Therefore one third point z is unit to both. Its actual degree f is at most56 by the degree sum. For the separate triple trace the empty multiplicity is49−f; for the one-common-edge trace it is48−f. Exactly the79 nonnegative actual types remain: f10–49 separate and f10–48 common. Every one is present and independently replayed; all fifteen impossible negative-multiplicity tuples from the historical broad table are excluded. The actual assigned degrees are checked to be a permutation of(10,10,f). This verifies the actual caller needed to exclude unit degree10 pairs.

Second, the degree tuple(10,11,11), two unit arms and arbitrary peripheral codegree1–11, has exactly21 nonnegative trace types: τ0/1 except peripheral λ11,τ0, whose singleton count would be−1. Every actual type is present and its max-of-avoided-pool fraction matches the independent injection calculation. Therefore a noncolorable actual input cannot have two degree11 unit neighbors at a degree10 point.

Third, excluding those two complete domains yields the proof's genuine low-pair structure. Its total degree excess above ten is46. For a degree10 point with u unit neighbors, no such neighbor has degree ten and at most one has degree eleven; their degree excess is at least2u−1. The exact row excess is16, so18≤u≤23. If l partners have codegree exactly two, then16≥2(34−u)−l, givingl≥52−2u. If all of them had degree at least eleven, the degree excess of these partners and the disjoint unit-neighbor set would be at least

$$(2u-1)+(52-2u)=51>46.$$

Thus there is an actual degree10 partner y of codegree two, rather than merely an integer type satisfying necessary inequalities.

Let P be the degree-at-least12 vertices, c=|P|. Each degree10 point has at least seventeen unit neighbors in P, hencec≥17. Each P-point costs at least two excess units, hencec≤23. The two actual degree10 points have at least34−c common P-unit neighbors. If they all had degree at least thirteen, baseline excess2c plus their additional excess34−c would give at leastc+34≥51>46. Therefore some actual common center has degree exactly twelve. This is precisely the last two certificate types(12,10,10), endpoint codegree two, triple multiplicity0/1. Both independent fractions match and are strict.

Every integer u18–23 and c17–23 used in these two budget contradictions is independently checked in the incremental script. No generic fourth-lock domain or failed exploratory table is used. All102 final minimum-ten records are replayed; the independently chosen valid bounds can differ from the submitted joint-cost fractions, but every one is strict. Maximum3721291/3721860.

## 6. Complete35-point coverage and final evidence

For v35 pair-cover forces actual minimum degree at least7, and the total degree forces it at most11. For δ7/8, `whole35.py` independently reconstructs the entire actual minimum-unit-partner range and, whenever the two-lock bound is not used, the full positive-common-pool third-degree interval and both traces. It verifies24+58=82 additional rows, all strict. These are genuine full minimum-degree branches, not isolated low-degree examples.

The prior δ9/δ11 replay ledger and the34/min11 review are retained without recomputation. The incremental execution adds only the missing δ7/8 and final δ10 records. `CHECK.json` now has `complete35_vertex=true` and the following complete minimum-degree split:

|Actual minimum degree|Replayed necessary types|Largest independent strict bound|
|---:|---:|---:|
|7|24|61407061/61410690|
|8|58|4961743/4962480|
|9|114|29774683/29774880|
|10|102|3721291/3721860|
|11|8|13429/13485|

Thus every actual35-point input reaches an accepted configuration, and its strict conditional failure bound yields an actual successful ordering and legal coloring. The complete35 domain has306 replayed records. The separate34/min11 audit retains its nine complete types, for315 records in the combined ledger.

The added calculation used approximately0.390CPU seconds; the initial audit used0.403CPU seconds. Reproduction from scratch is `python3 independent_new_branches/check.py`, then `python3 independent_new_branches/whole35.py`, with paths resolved from this progress directory. The first writes the initial review ledger; the second reconstructs the additional82+102 types and merges them without duplicating earlier rows. `WHOLE35_INCREMENT.json` preserves the additional minimum7/8 domain details.

Final status remains PASS_WITH_DECLARED_IMPORTS, same-family/provisional. Component-lemma authorship, shared pre-existing injection primitives, and independent implementation scope remain as stated in section4. This document does not perform the overall theorem's external review or certify other34-point minimum-degree branches.
