# P6 pilot after the new eight-four and eleven-four repair gates

## Fresh run and exact boundary

The full proof of [ELEVEN_POSITIVE_FOUR_SET_REPAIR](../../../../../proofs/propertyb35/ELEVEN_POSITIVE_FOUR_SET_REPAIR.md) was read. The fresh gate list adds precisely its hypothesis: at most11 positive four-sets, no negative triples, at most17 negative quadruples, ground at most18 and D7. It also adds the new [EIGHT_POSITIVE_18_TWO_TRIPLES](../../../../../proofs/propertyb35/EIGHT_POSITIVE_18_TWO_TRIPLES.md): exactly eight positive four-sets, at most two negative triples, at most18 negative quadruples, ground at most18 and D7.

The records [PILOT.json](PILOT.json), [RUN_WITH_L18.json](RUN_WITH_L18.json) and [RUN_WITH_NEW_EIGHT.json](RUN_WITH_NEW_EIGHT.json) are preserved. This final run is [RUN_WITH_NEW_EIGHT_ELEVEN_THREE_BLUE.py](RUN_WITH_NEW_EIGHT_ELEVEN_THREE_BLUE.py), with [complete output](RUN_WITH_NEW_EIGHT_ELEVEN_THREE_BLUE.json). It tries every eligible blue pair first, then every eligible three-blue P subset when no pair is accepted. It took0.0252 CPU seconds and stopped at a new necessary P inventory in the first high-trace orbit. Other high-trace orbits, the nine-at-a case and the second requested inventory were not processed. No exterior layouts or original hypergraphs were enumerated.

The accurate18-point gates from the previous run remain present. No17-point eight-positive theorem is used on18 exterior points. Existing generic positive/mixed gates do not directly accept the final listed signatures.

## True first stopping inventory for this gate list

The unique internal edge is $C=01234$, $a=5$. The degree-nine point is0, all other P points have degree eight. The higher traces and pair-trace multigraph are

$$T_1=012,\qquad T_2=345,$$

$$J=01+02+2\cdot05+15+25.$$

Thus

$$s=(4,2,2,0,0,4),\qquad
u=(3,4,4,6,6,3),\qquad n_1=26.$$

This necessary inventory has all required a--C pairs05,15,25 covered; the degree and exterior-capacity inequalities in the initial [report](REPORT.md) hold. It is not asserted to have an actual H realization.

All nine eligible blue-pair signatures are:

| Blue pair | Positive four-sets | Positive triples | Negative triples | Negative quadruples |
|---|---:|---:|---:|---:|
|03 or04|9|0|2|17|
|05|6|2|0|20|
|13 or14|10|0|4|16|
|15 or25|7|1|1|19|
|23 or24|10|0|4|16|

The closest unproved interfaces are therefore nine positive four-sets with two negative triples and17 negative quadruples; or six positive four-sets plus two positive triples with no negative triple and20 negative quadruples; or seven positive four-sets plus one positive triple with one negative triple and19 negative quadruples. The corresponding existing eight-pure, eight-mixed and seven-mixed results do not automatically cover these changes.

## Three-blue classification, including all-blue higher traces

For a selected three-blue set $S\subseteq P$ meeting both higher traces, the internal edge is proper: S meets C and has at most three blue points on a five-edge. The exact counts are

$$\begin{aligned}
m_4&=\sum_{i\in S}u_i,\\
m_3&=\sum_{\{i,j\}\subseteq S}J_{ij},\\
m_2&=|\{k:|T_k|=3,\ T_k\subseteq S\}|,\\
t&=\sum_{\{i,j\}\subseteq P-S}J_{ij},\\
b&=n_1-m_4.
\end{aligned}$$

An all-blue higher three-trace is **not** proper and gives a positive exterior pair, counted in $m_2$. Higher traces meeting both P colors are already proper. Since each S meets both traces, no all-red higher trace is discarded. For $m_2>0$, only the existing small-positive gates allowing positive pairs are tested, with their exact size/count conditions; mixed3/4 gates are not misapplied.

In this particular first-stop inventory, $T_1,T_2$ are disjoint triples. A three-blue set equal to one whole trace misses the other trace. Consequently the18 eligible three-blue sets all have $m_2=0$, as direct classification confirms. The source still computes $m_2$ explicitly, so this is a property of this inventory, not a deletion rule for general inputs.

None of these18 signatures is accepted. They group as follows, with tuple order $(m_4,m_3,m_2,t,b)$:

| Three-blue subsets | Signature |
|---|---|
|013,014,023,024,135,145,235,245|$(13,1,0,1,13)$|
|015,025|$(10,4,0,0,16)$|
|034|$(15,0,0,2,11)$|
|035,045|$(12,2,0,0,14)$|
|123,124|$(14,0,0,2,12)$|
|125|$(11,2,0,0,15)$|
|134,234|$(16,0,0,4,10)$|

Every still-unresolved original edge has its exact sign, with source labels retained; the total signed occurrence is at most the original exterior degree seven. This is the proper stopping boundary of the present gate selector, not a counterexample to colorability. No further generic gate or external-point domain was introduced after it.
