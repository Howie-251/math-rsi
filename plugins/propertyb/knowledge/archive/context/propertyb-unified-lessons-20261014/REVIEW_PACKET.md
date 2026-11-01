# Property B across m(5) >= 33, 34 and candidate 35: reusable mathematics and practice

Scope: synthesize reusable results and lessons, not resume the paused T34 solving Goal.
The user requests serious discussion with both Grok and Gemini. No new broad searches,
heavy enumeration, Lean rebuild or framework deployment is needed for this review.

## Ground truth

- T32 (at most32 five-edges): complete actual-input Lean, accepted m(5)>=33.
- T33 (at most33): complete actual-input Lean, accepted m(5)>=34.
- T34 (at most34): complete prose candidate chain; full-paper R1 found no substantive
  gap in its scope. Full Lean NOT complete. Finished <=20,21minimum5/6/8,
  21unique-seven and >=5sevens. Remaining21minimum7 with2/3/4sevens and22–25full
  coloring assembly, Main and final audits. Do not assign a probability of correctness.
- Individual generic lemmas compiled during T34 can be usable independently of T34.
  Old frozen proofs/targets are not changed by this synthesis.

## Proposed mathematical inventory (check rather than endorse as a bundle)

M1. Finite simple r-uniform H, r>=2. An uncovered pair can be identified,
preserving r-uniformity and non-2-colorability (a quotient coloring pulls back).
Duplicate image edges are collapsed, so edge count does not increase.
Thus a vertex-minimal counterexample within an at-most-m class is pair-covering.
Existing Lean reduction is Simple5; generic r formulation needs its own formal port.

M2. For r-uniform H, sum d=rm, sum_{y!=x}lambda(x,y)=(r-1)d(x).
Under pair covering epsilon_x=(r-1)d(x)-(v-1)>=0 equals sum(lambda-1),
and number of partners with lambda>=2 is <=epsilon_x.
Also v*ceil((v-1)/(r-1))<=rm, and if all d>=a then count{d=a}>=(a+1)v-rm.
Example extension of this reasoning: r=5, m<=36, v>=26 would imply
d>=7 everywhere and total d>=182>180. Thus pair-covering five-graphs with
<=36 edges have <=25 vertices; m=37 no longer excludes v=26 by this budget alone.
This is a paper-level consequence, not a newly built Lean theorem or next lower bound.

M3. Finite distinct s-subsets F on N points, s>=2. If q is the number of
unordered distinct intersecting pairs, q>=max(0,ceil((s|F|-N)/(s-1))).
Reason: sum_x(max(d_F(x)-1,0)) >= s|F|-N and <=sum_pairs|A cap B|<= (s-1)q.
For r-uniform edges through x avoiding R, remove x, s=r-1,N=v-1-|R|,
require x notin R. Existing five-uniform quota specializes s=4, denominator3.
Critical: simplicity, distinct unordered pairs, zero/negative deficit, r=2 excluded.

M4. Actual traces on chosen locks S: mu(T)=#{e:e cap S=T}. Under adding z,
p(T)=#{e:e cap S=T,z in e}, so 0<=p<=mu, sum p=d(z),
sum_{T contains i}p(T)=lambda(i,z), and full new counts are mu(T)-p(T),p(T).
Projection sums fibers, relabeling maps the same H; high-trace inclusion inversion
recovers singleton/empty counts exactly. Finite recursive allocation completeness
is a separate theorem from validating saved rows. Existing Lean generic n/v,
but several actual-H wrappers remain Simple5.

M5. Pair-budget/linear large traces: pairwise-unit locks force every |T|>=2
trace multiplicity<=1 and distinct such traces intersect in at most1. On five
locks, at most two >=3 traces, hence32 large-trace patterns. Check exact domain:
do not extrapolate the bound2 or table32 to more locks or nonunit pairs.

M6. Universal shared-vector quota/weak-dual certificate:
0<=z_s<=c_s, sum_s a_qs z_s>=q_q, delta_q>=0 imply
sum_q delta_q q_q - sum_s max(0,sum_q delta_q a_qs-w_s)c_s <= sum_s w_s z_s.
Convex gamma_l>=0,sum gamma=1, sum gamma_l U_l(z)<1 gives some U_l(z)<1.
For H, all layouts refer to one actual bad-pair vector; probability spaces of
different layouts need not coincide. Avoid quantifier reversal forallH existsL vs
existsL forallH, unjustified min/average swaps, independence and LP strong-duality claims.
Existing MixedLayoutDual algebra has arbitrary finite index types over rationals;
actual coloring interface has generic n/v/edgeCount but Simple5 object.

M7. Weighted partition / bounded-conflict selection. A minimum-internal-weight
partition of a finite nonnegative symmetric weighted graph into k>=1 classes
gives internal weighted degree <= total degree/k at each vertex (move one vertex).
Current Lean WeightedThreePartition is a three-class interface. General k is a
paper extension unless already present. Use the exact actual theorem assumptions.

## Source map for review

Read these small core files as needed, not every numeric table:
- formal/Aris4Math/Structure.lean
- formal/Aris4Math/Reduction.lean
- formal/Aris4Math/ThirtyThree/AvoidedLink.lean
- formal/Aris4Math/ThirtyThree/MultiLockRecovery.lean
- formal/Aris4Math/ThirtyThree/FiveLockClassification.lean
- formal/Aris4Math/ThirtyFour/BoundedAllocations.lean
- formal/Aris4Math/ThirtyFour/LockExtension.lean
- formal/Aris4Math/ThirtyFour/PromotionCatalog.lean
- formal/Aris4Math/ThirtyFour/PromotionReconstruction.lean
- formal/Aris4Math/ThirtyFour/LockProjection.lean
- formal/Aris4Math/ThirtyFour/LockRelabel.lean
- formal/Aris4Math/ThirtyFour/MixedLayoutDual.lean
- formal/Aris4Math/ThirtyFour/MixedLayoutApplication.lean
- formal/Aris4Math/ThirtyFour/WeightedThreePartition.lean

Experience/evidence:
- research-wiki/PROPERTY_B_RESEARCH_LESSONS.md
- research-wiki/PROPERTY_B_FAILURE_ATLAS.md
- research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md
- context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md
- context/propertyb34/round01/middle-lean/PERFORMANCE_NOTES.md
- context/propertyb34/round01/high-math/TWENTYFIVE_FORMALIZATION_COST.md
- context/propertyb34/round01/twentyone-lean/DEGREE_SEVEN_CONTINUATION.md

## Discussion questions

1. Which 3–5 results are the genuinely useful reusable core? Give hypotheses,
   scope and a short proof or a concrete counterexample/repair. Distinguish standard
   mathematical machinery from project-specific assembly; do not make novelty claims.
2. Attack M1–M7, especially general r, discrete rounding, same-H quantifiers,
   Nat subtraction, large-trace packing and weighted partition assumptions.
3. What should remain a parameter-specific corollary/catalogue rather than be
   promoted to a universal theorem? What does source actually formalize today?
4. What mistakes caused wasted work or false proximity estimates? Recommend
   concrete improvements grounded in the observed pipeline, not generic rubrics.
5. Prioritize next extraction steps that will reduce end-to-end remaining proof
   work. Coefficient caching for25 has a passing small probe, NOT full acceptance.

HERO constraints: focus on useful mathematical statements and actual bottlenecks;
no gratuitous hashing, huge framework, mechanical scoring, or endless review.
Return actual files read, whether any commands were executed, substantive objections
and actionable synthesis. Reading previous build logs is not independently running Lean.
