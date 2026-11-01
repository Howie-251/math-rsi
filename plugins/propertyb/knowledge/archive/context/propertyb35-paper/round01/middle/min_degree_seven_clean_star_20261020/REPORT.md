# General minimum-degree-seven q3 gate: bounded clean-star result

The complete bounded calculation leaves a precise partial result. From the entire119 generic q3 attachment inputs, imposing only minimum degree seven on the five actual F points gives102 inputs. The fixed16 old five-lock menu closes97 and leaves five tails, including a new tail of F high excess eight. Every tail has nonempty exception traces, so the clean exterior-star lemma applies. Their full necessary clean-star domain has1171 inputs. With only the original best five-point positions plus six old insertion slots,1053 are strict and118 remain nonstrict. Both domains and every selected fixed bound were independently reconstructed and replayed. No further layout search was performed.

In particular the two tails D and the newly found E are completely closed under the general minimum-degree-seven assumption, without any global high-excess bound. The proposed general Gamma minimum-degree-four theorem is **not** established: A, B and C retain the118 explicit necessary inputs listed in `RESIDUALS.md` and `STAR_RESULT.json`.

## 1. Exact source and complete q3 domain

Let H have21 vertices and35 distinct five-element edges, cover all point pairs, and have minimum degree at least seven. Let F be an actual original edge of nonunit-graph degree three. Number its points0,...,4. Its three different nonunit neighbors have traces T1,T2,T3 in F; each trace has size0,2,3 or4, with repetitions allowed. The other31 edges have singleton traces with exact counts a_v. Thus

\[
\sum_{v\in F}a_v=31,\qquad
h_v=\#\{j:v\in T_j\},\qquad d_H(v)=1+a_v+h_v.
\]

The complete existing3276-label/91-S5-orbit q3 safe-anchor classification leaves exactly119 generic trace/attachment inputs. Its source is

`../three_nonunit_direct_repair_20261020/RESULT.json`.

`FIVE.py` reads the corresponding complete generic tail and filters **only** d_H(v)>=7 for every v in F. It does not assume e<=4, degree-six uniqueness, a bound on global seven-degree counts, or a pointpair codegree bound. It obtains102 necessary inventories. `VERIFY.py` independently rebuilds all119 from the source complete safe/failure sets and the full integer increment-composition domain, then applies the same local minimum-degree requirement and obtains exactly the same102 keys and actual degrees.

For each inventory the original35 five-lock traces are one mask31 edge F, the three exceptional masks, and a_v singleton copies at v. The fixed16 menu is exactly the old q3 menu: six central profiles on9,...,14 with one slot omitted, five exact existing end profiles, and their reflections. All quotas are zero. Ninety-seven inputs are strict. The **complete** remaining five tails are:

|Source|Name|Exception masks|Singleton counts a|Original F degrees|F excess above9|D_F=sum F degrees|
|---:|---|---|---|---|---:|---:|
|0|A|7,11,28|6,7,7,6,5|9,10,10,9,7|2|45|
|1|B|7,25,30|4,7,7,7,6|7,10,10,10,9|3|46|
|2|C|7,25,30|5,7,7,6,6|8,10,10,9,9|2|46|
|3|D|7,27,29|9,5,5,6,6|13,8,8,9,9|4|47|
|4|E|15,23,27|9,9,5,4,4|13,13,8,7,7|8|48|

Tail E is genuinely additional to the earlier e<=4 analysis. No high-excess restriction was used to discard it. None of these five tails has an empty trace, and every other original edge has a singleton trace, so **every original edge intersects F**.

## 2. A genuine clean exterior point of bounded degree

Use the proved general lemma `proofs/propertyb35/CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md`. For z outside F define

\[
h_F(z)=\sum_{G\ni z}(|G\cap F|-1),\qquad
B_F=\sum_{G\in H}(|G\cap F|-1)(5-|G\cap F|).
\]

Every G meets F in the five current tails, so all terms are nonnegative. Exchanging sums gives

\[
\sum_{z\notin F}h_F(z)=B_F.
\]

An exterior point is clean when h_F(z)=0; all its original incident edges then have singleton F trace. There are16 exterior points, at most B_F dirty ones, and at least16-B_F clean ones.

Let c be the **actual** number of clean points. Its value need not equal16-B_F. Suppose every clean point has degree at least R+1. Since every dirty point still has degree at least seven, the total exterior degree satisfies

\[
175-D_F\ge7(16-c)+(R+1)c
=112+(R-6)c.
\]

For R>=7 the last expression increases with c. Since c>=16-B_F, this implies

\[
175-D_F\ge7B_F+(R+1)(16-B_F).
\]

Consequently there exists a clean actual point z whose degree r obeys

\[
7\le r\le R_F:=
\left\lfloor\frac{175-D_F-7B_F}{16-B_F}\right\rfloor.
\]

This justifies the average argument with **at least**16-B_F clean points: using their minimum guaranteed number weakens the degree lower bound in the safe direction. The global minimum degree seven is essential for the dirty-point contribution; no global high-excess assumption is used.

Only the three exceptional traces contribute to B_F. The exact budgets and degree bounds are:

|Tail|B_F|Guaranteed clean points|Exterior total degree|R_F|
|---|---:|---:|---:|---:|
|A|12|4|130|11|
|B|11|5|129|10|
|C|11|5|129|10|
|D|10|6|128|9|
|E|9|7|127|9|

For example E has three four-point traces, each costing3, so B_F=9; its two thirteen-degree F points do not invalidate the clean-point argument.

## 3. Exact common-star inventory, with no independent projections

Choose the one actual clean z supplied above and write

\[
s_v=\#\{G\ni z:G\cap F=\{v\}\}.
\]

Every incident edge of z has singleton F trace, so these are the original pair codegrees lambda(z,v). Pair coverage and actual trace availability give

\[
s_v\ge1,\qquad \sum_vs_v=r,\qquad s_v\le a_v.
\]

Conversely these necessary integer conditions cover every possible actual clean star; no assertion that every positive vector extends to a whole H is needed. Label z as bit0 and shift the five F bits one place. From old F inventory mu, the exact new counts are

\[
\nu_{2m}=\mu_m\quad(|m|\ne1),\qquad
\nu_{2^{v+1}}=a_v-s_v,\qquad
\nu_{2^{v+1}+1}=s_v.
\]

This preserves the same35 original indices and the F projection, and gives selected degree vector(r,d_F0,...,d_F4). It is one common actual star, not separately optimized local views.

The bounded complete counts, after s_v<=a_v, are:

|Tail|r7|r8|r9|r10|r11|Total|
|---|---:|---:|---:|---:|---:|---:|
|A|15|35|70|125|203|448|
|B|15|35|69|121|—|240|
|C|15|35|70|125|—|245|
|D|15|35|70|—|—|120|
|E|15|35|68|—|—|118|
|Total||||||1171|

The primary generator recursively composes r-5 nonnegative increments. The independent generator chooses four cut positions among1,...,r-1, producing the positive compositions by a different parameterization. It constructs35 explicit F-edge indices, selects s_v actual singleton indices for each v, inserts z into exactly those indices, and verifies the projection and selected degrees. Its full1171-key set and every lifted count vector match the primary result.

## 4. Pilot, fixed positions and exact residuals

Each source keeps its pre-existing best F positions from the fixed16 menu:

\[
P_A=(4,3,12,2,1),\quad
P_B=P_C=(11,3,2,12,1),\quad
P_D=P_E=(9,11,12,13,14).
\]

Insert z only into an unused position from the six old slots

\[
\{1,9,10,11,20,21\}.
\]

No F relabeling, additional permutation menu, position solver or LP is run. Every certificate has zero quota. The one-case pilot was A, r=7, s=(1,1,1,1,3); its best bound4899/5005<1 used0.027732 CPU seconds including complete-domain construction. The same predetermined positions were then applied to all1171 inputs; the primary full calculation used0.617699 CPU seconds.

There are1053 strict and118 nonstrict inputs. The exact failure counts and first witnesses are:

|Tail|r|Nonstrict count|First s witness|Exact best fixed bound|
|---|---:|---:|---|---|
|A|10|35|1,1,2,1,5|3005/3003|
|A|11|55|1,1,2,2,5|2162/2145|
|B|7|3|2,1,1,1,2|718/715|
|B|9|10|1,1,1,2,4|5072/5005|
|C|10|15|1,1,1,2,5|6449/6435|

D and E have no nonstrict input. Their maximum bound, in each complete domain, is6359/6435<1. Thus each of those two actual F types gives a legitimate original-H coloring through the conditional permutation lemma, for arbitrary global minimum degree at least seven and no high-excess cap. The A/B/C rows above remain open for this fixed argument. A bound exceeding one is a failure of the sufficient estimate, not evidence that the corresponding H is noncolorable or even realizable.

`RESIDUALS.md` lists **all118** s vectors, chosen positions and exact bounds. `STAR_RESULT.json` also retains every fixed position tested for each input. No new positions were attempted after the failures.

## 5. Independent deterministic verification and limits

`VERIFY.py` independently rebuilds the full119 generic failure tail, the102 min-F-seven inputs, all five actual nonempty tails and their average-degree bounds, and the1171 clean-star inputs. It then replays the chosen fixed certificate for **all1273** five-lock and six-lock inputs, including the nonstrict ones. Each replay expands35 actual edge indices and sums all1190 ordered distinct pairs by falling-factorial injection arithmetic at each of21 positions. All26733 rows reproduce the primary factorial-scaled total and strict/nonstrict status exactly.

The1150 strict certificates (97 five-lock plus1053 six-lock) are saved with their original35 masks, fixed positions, zero quota and every A/B/C row in `VERIFY_RESULT.json`. The independent run reports `PASS_COMPLETE_FIXED_DOMAINS_AND_REPLAYS`, CPU2.345946 seconds. The first five-lock run used0.310023 seconds and the primary star run0.617699 seconds, for approximately3.274 CPU seconds in total, below the fifteen-second budget.

Mathematical imports are the existing complete q3 safe-anchor classification, the clean exterior-star double-counting lemma, and the conditional permutation-to-original-coloring theorem. The scripts verify finite local coverage and exact arithmetic; they do not independently reprove those mathematical lemmas, provide a Lean derivation, or constitute cross-family review. This partial result remains same-family/provisional until the parent records its actual acceptance.

Artifacts:

- `FIVE_RESULT.json`: complete102 min-F-seven inputs, old16 menu and all five tails.
- `STAR_DOMAIN.json`: complete1171 positive common-star inventories and source/r counts.
- `STAR_PILOT.json`: the first-case profile.
- `STAR_RESULT.json`: every predetermined fixed value,1053 strict and118 nonstrict inputs.
- `RESIDUALS.md`: readable full118 residual table.
- `VERIFY_RESULT.json`: complete independent coverage and fixed-certificate replays.
- `FIVE.py`, `STAR.py`, `VERIFY.py`: bounded reproduction scripts, in that order.

No other source, frozen manuscript, wiki navigation, Lean project or unrelated branch was changed. The general Gamma-minimum-degree-four target is left unproved: the precise remaining issue is selecting a clean actual point or exploiting its common structure sufficiently to exclude the118 A/B/C necessary inventories, rather than continuing an uncontrolled layout search.
