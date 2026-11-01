# A2/A3 joint-moment frontier after the degree-sensitive capacities

## Result

The two actual-H capacity inequalities are correct; their complete short proofs are in [CAPACITY_LEMMAS.md](CAPACITY_LEMMAS.md):

\[
C_2\le(24+\lfloor e/2\rfloor)n_2,\qquad
C_1\le35n_1-K_d(n_1).
\]

The specified T-only first filter **does not close any of the sixteen distinct degree spectra**. The32 degree-spectrum/role rows in the supplied CHECK.json reduce to16 distinct degree lists after removing the nonunit-seven role label. Their total1,357,926 degree-labeled moment configurations reduce to1,355,158 after the wedge/excess test, and then to35,083 surviving degree-labeled configurations under the common-P weighted bound. There are23,133 distinct surviving (n0,…,n4,τ) keys when the spectrum label is dropped.

Overall remaining ranges are

\[
0\le n_4\le33,\qquad0\le\tau\le58,\qquad504\le n_1\le558.
\]

These are projections of a finite necessary relaxation, not an assertion that all combinations in the ranges survive or have any actual H realization. [FRONTIER.json](FRONTIER.json) gives the exact minimum/maximum τ and survivor count at each n4. No original-H generation, degree-sequence DP, or new local inventory was used.

## Necessary domain and imports

For each actual spectrum let W=Σ_v C(dv,2). Pair covering and35 five-edges on21 points give Σ_P(λP−1)=350−210=140. Under the separately supplied strong-pair reduction λP≤4, define τ=Σ_P C(λP−1,2); then0≤τ≤140. The ordinary intersection moments are

\[
\sum_{j=0}^4 n_j=595,\quad
\sum_{j=0}^4 j n_j=W,\quad
\sum_{j=0}^4\binom j2 n_j=140+\tau.
\]

Writing m=n3 and t=n4, they uniquely give

\[
n_1=W-280-2\tau+3m+8t,
\]
\[
n_2=140+\tau-3m-6t,
\]
\[
n_0=735-W+\tau-m-3t.
\]

The filter visits every integer τ∈[0,140], t∈[0,floor((140+τ)/6)] and m∈[0,floor((140+τ−6t)/3)], retaining nonnegative nj and397≤n1≤595. The lower bound397 is the already established global private-pair repair import; the upper bound595 is just the number of unordered original edge pairs. In particular no old A1 upper bound546 is imposed.

It also imposes the newly proved wedge capacity

\[
3W_{Q,\min}(35,t)\le4\tau,
\quad
W_{Q,\min}=(35-b)\binom a2+b\binom{a+1}2,
\quad2t=35a+b,\ 0\le b<35.
\]

The shared-middle identity and threshold majorant are the previously proved [common-middle theorem](../../../../../proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md). With

\[
f(s)=\frac{s^2-(5-r)a^2-r(a+1)^2}{2},\quad s=5a+r,
\]

its threshold recurrence is

\[
T(n,m,r)=\max\{f(r)+T(n-1,m,r),\
f(n-1+r)+T(n-1,m-n+1,r+1)\},
\]

with invalid m outside0,…,C(n,2) excluded and T(0,0,r)=0. We use only P≤T(35,n1,0); no linear P bound, A1 n4≤8, or D0-specific n4 bound is imported. The full T table is recomputed for every397≤n1≤595 and agrees with every preexisting saved table entry. The additional pending Γ-minimum-degree theorem is not used to modify this threshold domain.

The capacity vector is exactly

\[
(C_0,C_1,C_2,C_3,C_4)
\le(33n_0,\ 35n_1-K_d(n_1),\
(24+\lfloor e/2\rfloor)n_2,\ 14n_3,\ 4n_4).
\]

Here C3≤14n3 uses the newly verified selected-high-excess gate, whose hypotheses follow from global λ≤4 and total e≤4. C0≤33n0 excludes the two outer edges; C4≤4n4 follows by charging a valid middle to the exclusive pair and using its codegree cap4. All Cj share the same budget ΣCj=P≤T. Allocating P greedily to weights(36,120,330,792,1716) in decreasing order gives the exact maximum of this scalar relaxation. If

\[
L=\frac12\sum_j w_jC_j+3432n_1<2722720,
\]

then the existing [global two-flip repair theorem](../../../../../proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md) supplies an original-H coloring. The saved survivors are precisely those for which this sufficient inequality is not strict. They are not counterexamples to that theorem or to Property B.

## Complete spectrum results

The partition lists the positive increments above the nine-degree baseline. The role parameter r distinguishing unit/nonunit seven-degree points is not rerun: all rows with an identical degree list share one calculation.

|a7|a8|High-excess partition|W|e|Survivors|n4 range|τ range|
|---:|---:|---|---:|---:|---:|---|---|
|2|7|empty|649|0|1219|0–29|0–37|
|2|8|1|650|1|1394|0–30|0–40|
|2|9|1+1|651|2|1614|0–30|0–41|
|2|9|2|652|2|1823|0–30|0–43|
|3|5|empty|650|0|1394|0–30|0–40|
|3|6|1|651|1|1588|0–30|0–41|
|3|7|1+1|652|2|1823|0–30|0–43|
|3|7|2|653|2|2046|0–31|0–46|
|3|8|1+1+1|653|3|2046|0–31|0–46|
|3|8|1+2|654|3|2289|0–31|0–47|
|3|8|3|656|3|2810|0–32|0–52|
|3|9|1+1+1+1|654|4|2330|0–31|0–47|
|3|9|1+1+2|655|4|2586|0–31|0–49|
|3|9|1+3|657|4|3150|0–32|0–52|
|3|9|2+2|656|4|2863|0–32|0–52|
|3|9|4|660|4|4108|0–33|0–58|

The exact surviving (t,τ) lower frontier across all spectra is τmin=0 for0≤t≤17. For t18,…,33 it is respectively

    1,3,4,6,7,9,10,12,16,22,28,34,40,46,52,58.

Thus the wedge inequality is active near t18,…,25, while the global weighted filter adds a stronger lower requirement at t≥26. This is only a description of this aggregate domain.

## One exact relaxation witness and the actual bottleneck

For spectrum6,7²,8⁷,9¹¹, W=649,e=0, a minimum-total-high-pair witness is

\[
(n_0,n_1,n_2,n_3,n_4)=(28,527,18,2,20),\qquad\tau=4.
\]

Its singleton-allocation minimum is Kd(527)=4418, so C1≤14027. The threshold budget is P≤13447 and the capacity vector is

\[
(924,14027,432,28,80).
\]

The greedy allocation is

\[
(C_0,C_1,C_2,C_3,C_4)=(0,12907,432,28,80),
\]

and L=2734092≥2722720, so this relaxation cannot reject it. Its Q convex wedge minimum at t20 is5, satisfying3·5≤4·4. It obeys all displayed original intersection moments, but no graph or hypergraph realization is asserted.

In fact **none of the35,083 surviving configurations saturates the new C1 upper bound**. The C1 lemma is valid, but in this first T-only filter it is not the active obstruction: the shared P threshold and higher-intersection capacities leave more room than the C1 degree-allocation bound removes. A further actual common-degree or forest constraint would have to couple those resources; merely improving C1 while it remains above its allocated value would not remove these witnesses. No new such constraint is claimed here.

## Reproduction and scope

[FILTER.py](FILTER.py) reads the supplied32-row spectrum source, reconstructs and deduplicates all16 actual degree lists, computes all199 required T entries, and runs the complete integer domain above. [RESULT.json](RESULT.json) records all spectrum counts and extremal witnesses; [SURVIVORS.json](SURVIVORS.json) records all35,083 complete surviving keys and allocations; [THRESHOLD_TABLE.json](THRESHOLD_TABLE.json) contains397,…,595 with no truncation. CPU2.049938 seconds.

[CHECK.py](CHECK.py) separately checks every saved survivor, the three moment identities, wedge restriction, all capacity values, grouped-degree mincost, common P budget, greedy optimum and final exact integer objective. [CHECK.json](CHECK.json) is PASS, CPU0.368166 seconds. It also confirms the actual survivor range extends to n1=558; omitting the old-table missing entries would have lost genuine relaxation cases. Full-domain completeness is justified by the explicit finite ranges and formulas in FILTER.py, while CHECK independently verifies all retained keys and arithmetic rather than pretending to generate original H.

This is a necessary-domain diagnosis with same-family/provisional mathematical checking. It proves the two capacity lemmas and a finite scalar non-closure statement, not A2/A3 colorability, nor an actual H with the displayed moments. No canonical, navigation, Lean, v2, or original-H search was changed.

## Additional bounded re-sieve: singleton degree at most31

The original result above is retained. The following three re-sieves use only its frozen35,083 surviving full keys; no new graph-degree optimization or moment-domain generation is performed. They assume the separately assembled generic minimum-Γ-degree-three repair import. Since s(F) is the singleton-intersection graph degree, Γ-minimum-degree at least three gives

\[
0\le s(F)\le31,\qquad\sum_Fs(F)=2n_1.
\]

Thus2n1≤35·31=1085, or n1≤542. Because f(s+1)−f(s)=s−floor(s/5) is nondecreasing, repeatedly moving mass from a smaller positive entry to a larger nonsaturated entry cannot decrease Σf(s). Saturating entries to31 therefore proves the genuine35-slot upper bound

\[
P\le P_{31}(n_1):=a f(31)+f(b),\qquad
2n_1=31a+b,\quad0\le b<31,\qquad f(31)=384.
\]

The inequality is only a degree-sum relaxation: its saturated list need not be a graph degree sequence. A valid original degree list is covered because it has exactly35 slots and obeys the stated cap and sum. We use min(T(35,n1,0),P31(n1)), then reallocate that shared budget among the same five capacities, with the same weights and strict threshold as before. All configurations excluded by the original upper bound remain excluded by this smaller one, so filtering only the frozen survivors is complete for this refinement.

The three modes are:

|Additional assumptions after the original filter|Degree-labeled survivors|Distinct moment keys|n4 range|τ range|Smallest L−2722720 among survivors|
|---|---:|---:|---|---|---:|
|minΓ≥3 only|20995|14055|0–31|0–46|2|
|minΓ≥3 and the separately supplied n4≤25 import|20199|13505|0–25|0–43|2|
|minΓ≥3 and **conditional** n4≤13|6953|4803|0–13|0–28|2|

The n4≤25 structural argument is a separate deleted-star/forest import supplied by the main proof project; this scalar check does not prove it. The stronger n4≤13 mode is explicitly conditional on the actual mixed-four-core repair argument and its subsequent structural consequence, not a new unconditional claim of this note. Neither cap closes a full degree spectrum here.

Per-spectrum retained counts, with columns in exactly those three mode orders, are:

|a7|a8|High-excess partition|minΓ3 only|plus n4≤25|conditional n4≤13|
|---:|---:|---|---:|---:|---:|
|2|7|empty|603|586|127|
|2|8|1|723|702|171|
|2|9|1+1|879|852|232|
|2|9|2|1032|998|297|
|3|5|empty|723|702|171|
|3|6|1|852|825|223|
|3|7|1+1|1032|998|297|
|3|7|2|1197|1155|368|
|3|8|1+1+1|1197|1155|368|
|3|8|1+2|1373|1322|450|
|3|8|3|1763|1692|641|
|3|9|1+1+1+1|1414|1361|465|
|3|9|1+1+2|1606|1545|556|
|3|9|1+3|2032|1946|772|
|3|9|2+2|1809|1736|658|
|3|9|4|2760|2624|1157|

A common closest surviving witness in all three modes is the A3 degree spectrum6,7³,8⁹,9⁵,10²,11, whose W=655 and e=4. It has

\[
(n_0,n_1,n_2,n_3,n_4)=(35,517,1,32,10),\qquad\tau=17.
\]

Its former T bound is12989, but the31-cap bound is

\[
P\le33f(31)+f(11)=33\cdot384+48=12720.
\]

With capacities(1155,13858,26,448,40), the greedy allocation is

\[
(C_0,C_1,C_2,C_3,C_4)=(0,12206,26,448,40),
\]

and L=2722722, just two above the strict repair threshold. It is an exact aggregate-relaxation witness and is not claimed to be a realizable original H. Each mode's full closest witness, minimum-high witness, and each spectrum's closest margin are recorded in RESIEVE_RESULT.json.

The former illustrative A2 witness with n1=527 is indeed removed:2n1=34·31, so P≤34·384=13056 rather than13447. Its L falls by391·120/2=23460, from2734092 to2710632, below2722720. This confirms that the new shared budget has a real effect, while the closer A3 witness above shows that the strengthened scalar relaxation is still insufficient.

[RESIEVE.py](RESIEVE.py) and [RESIEVE_RESULT.json](RESIEVE_RESULT.json) preserve the complete three-mode counts and witnesses; [RESIEVE_SURVIVORS.json](RESIEVE_SURVIVORS.json) saves all20,995 keys surviving the minΓ3 refinement. Exactly1990 old keys violate the total singleton-degree cap immediately. [RESIEVE_CHECK.py](RESIEVE_CHECK.py) independently saturates an explicit35-slot list rather than using the discovery divmod formula, recomputes f by pair products of balanced five-group sizes, and checks equality of every retained full key, all allocations/objectives and all16 per-mode counts. [RESIEVE_CHECK.json](RESIEVE_CHECK.json) is PASS. Measured CPU is0.233251 seconds for the re-sieve and1.384051 seconds for this verification. Original results and source evidence are unchanged; no additional structural gate or original-H realization is asserted.

## Conditional critical box refinement on the6953-key mode

A further separately conditional deletion-theorem import would make H edge-critical, hence force every original edge to have at least five singleton-intersection neighbors. In combination with the preceding minΓ3 input this gives5≤sF≤31. The complete proof of that implication, exact35-slot convex-box capacity, scope separation and arithmetic are in [CONDITIONAL_CRITICAL_RESIEVE.md](CONDITIONAL_CRITICAL_RESIEVE.md).

On the frozen6953-key n4≤13 mode, the refinement leaves5813 degree-labeled keys (4032 distinct moment keys), with all16 degree spectra still nonempty. The previous closest margin2 witness is removed, but the new closest survivor has n=(30,518,12,26,9),τ4 in spectrum6,7³,8⁸,9⁸,12; its box budget12707 gives L2722728, margin8. The independently regenerated full survivor-key set is identical, with CHECK PASS. No unconditional criticality, full spectrum exclusion or new graph-degree DP is asserted.
