# Conditional edge-critical re-sieve on the frozen n4≤13 frontier

## Scope of the conditional import

This note assumes the previously described A2/A3 necessary domain, generic Γ-minimum-degree-three import, and the separately supplied n4≤13 paper-local structural bound. It additionally assumes that every deletion H−F is colorable, so the hypothetical non-B35-edge H is edge-critical. The proposed route to this last assumption uses the old≤34-edge local low-degree theorem and remains an **external conditional import here**. Neither this script nor this note establishes that old theorem's precise actual interface.

The consequence of edge-criticality itself is elementary. Fix an original edge F and a proper coloring of H−F. The edge F must be monochromatic, otherwise H is colored. For each v∈F, flipping v must create a new bad original edge, or H would be colored after that flip. Such an edge has v as its only vertex of F's color and hence intersects F exactly in{v}. For different v these witness edges are distinct. Thus F has at least five singleton-intersection original neighbors. Applying this to every original F gives

\[
5\le s_F\le31,\qquad\sum_{F\in H}s_F=2n_1.
\]

The upper bound uses the separate minimum-Γ-degree-three import as before. This derivation does not assert that edge-criticality follows without the supplied deletion theorem.

## Exact convex-box capacity

Write f(s) for the balanced five-group wedge maximum already used in the original filter. Its discrete derivative is nondecreasing. Under the35-slot box5≤sF≤31 and fixed sum, saturating as many slots as possible at31 maximizes Σf(sF). Let

\[
v=2n_1-175,\qquad a=\lfloor v/26\rfloor,\qquad b=v-26a.
\]

The box is impossible unless0≤v≤910. For a<35 the exact box maximum is

\[
P_{[5,31]}=a f(31)+f(5+b)+(34-a)f(5),
\]

and when a=35 necessarily b=0 and the maximum is35f(31). At b=0 this equals a f(31)+(35−a)f(5), as required. Here f(5)=10 and f(31)=384. This is a complete scalar35-slot bound, not a claim that the optimizing list is a graph degree sequence.

We replace the saved budget by the minimum of this bound and the former min(T,P31). All five middle capacities and the strict objective threshold remain unchanged. We re-filter only the frozen6953 keys with n4≤13; monotonicity guarantees that none of the previously excluded keys can reappear. No new DP or original-H domain is generated.

## Result

The conditional6953-key domain reduces to **5813 degree-labeled survivors**, or4032 distinct moment keys. All sixteen spectra still have a survivor. The projection remains0≤n4≤13 and0≤τ≤28. Thus this additional conditional import is useful but does not close a degree spectrum in the present aggregate relaxation.

|a7|a8|High-excess partition|Former n4≤13 count|Conditional critical count|Closest surviving L−2722720|
|---:|---:|---|---:|---:|---:|
|2|7|empty|127|102|32|
|2|8|1|171|137|368|
|2|9|1+1|232|186|56|
|2|9|2|297|239|56|
|3|5|empty|171|137|368|
|3|6|1|223|182|296|
|3|7|1+1|297|239|56|
|3|7|2|368|305|77|
|3|8|1+1+1|368|305|77|
|3|8|1+2|450|373|128|
|3|8|3|641|545|8|
|3|9|1+1+1+1|465|382|56|
|3|9|1+1+2|556|468|44|
|3|9|1+3|772|656|14|
|3|9|2+2|658|557|50|
|3|9|4|1157|1000|14|

The previous closest configuration with n1=517 is removed exactly: its critical-box bound is12696 instead of12720, and its objective becomes2721282<2722720.

The new closest surviving configuration is in the A3 spectrum6,7³,8⁸,9⁸,12 (W=656,e=3):

\[
(n_0,n_1,n_2,n_3,n_4)=(30,518,12,26,9),\qquad\tau=4.
\]

Now2n1=1036=33·31+8+5, giving

\[
P_{[5,31]}=33\cdot384+f(8)+f(5)=12707.
\]

Its capacity vector is(990,13863,300,364,36), and the greedy allocation is

\[
(C_0,C_1,C_2,C_3,C_4)=(0,12007,300,364,36),
\]

with L=2722728. This is eight above the strict threshold and is only a necessary scalar-relaxation witness; no original-H realization or non-colorability is claimed.

## Exact checks and evidence

[CONDITIONAL_CRITICAL_RESIEVE.py](CONDITIONAL_CRITICAL_RESIEVE.py) and [its result](CONDITIONAL_CRITICAL_RESIEVE_RESULT.json) record the complete calculation and all per-spectrum closest/minimum-high witnesses. [CONDITIONAL_CRITICAL_SURVIVORS.json](CONDITIONAL_CRITICAL_SURVIVORS.json) records all5813 full surviving keys and allocations.

[CONDITIONAL_CRITICAL_CHECK.py](CONDITIONAL_CRITICAL_CHECK.py) does not import the re-sieve implementation. It starts with35 explicit five-valued slots, successively fills each to31, independently computes f from five-group pair products, and re-evaluates every one of the6953 frozen source keys. Its expected survivor-key set agrees exactly with all5813 saved keys; all per-spectrum counts, rational-free integer objectives and the former closest source's rejection agree. [CONDITIONAL_CRITICAL_CHECK.json](CONDITIONAL_CRITICAL_CHECK.json) is PASS. CPU was0.060689 seconds for the re-sieve and0.341765 seconds for the independent check.

The scope is conditional aggregate diagnosis, with same-family/provisional mathematical checking. Old results are preserved. No new imported local theorem, n4 bound, canonical proof, navigation, Lean, v2 or original-H search was produced here.
