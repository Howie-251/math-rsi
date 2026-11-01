# Two high traces avoiding the common internal set: bounded P-side selection

## Result and current boundary

The complete necessary P-side domain for the missing path $P_4$ was processed: all nine high-trace-pair orbits, containing142436 labeled pair-trace inventories, admit a proper two-blue-point choice covered by existing repair theorems. This is a complete **candidate finite P-side selection result**, awaiting the independent domain and gate replay assigned by the root agent. It does not enumerate exterior sets or original hypergraphs.

The pilot then stopped at the first nongated necessary inventory for missing $P_3+K_2$. It processed27 complete high-trace orbits there and part of the28th, out of49. Missing $3K_2$ was not processed. No partial range is claimed as a whole branch. The explicit remaining inventory is in Section5 below.

Source and full pilot output: [PILOT.py](PILOT.py), [PILOT.json](PILOT.json). Runtime0.573 seconds. No external model, Lean, exterior layout, or new generic repair theorem was used.

## 1. Actual input and degree recovery

Let $H$ have24 points,35 simple five-edges, pair coverage, minimum degree seven, seven high points $P$, and no all-seven-degree edge. Assume exactly three internal $P$ edges and exactly two other edges with $P$ traces $T_1,T_2$ of size three or four, both avoiding the common internal set $C$.

All seven P points have degree eight; the17 exterior points $L$ have degree seven. P hits every original edge. Let $F$ be the three-edge missing graph: an internal edge is $P-e$ for $e\in F$. Write

$$c_v=3-d_F(v),\qquad h_v=|\{i:v\in T_i\}|,$$

for actual internal and high-trace edge incidences. Pair-trace edges form a loopless multigraph $J$ on P, preserving different actual edge indices. Put $s_v=d_J(v)$. If $\alpha=|T_1|,\beta=|T_2|$, total P incidence gives

$$n_2=11-\alpha-\beta\in\{3,4,5\},\qquad
n_1=30-n_2=19+\alpha+\beta.$$

The actual singleton-trace count at $v$ is

$$u_v=8-c_v-h_v-s_v\ge0.\tag{1}$$

Point-pair coverage of $(v,L)$ gives a second necessary capacity bound. The noninternal edges at $v$ have total exterior capacity

$$4u_v+3s_v+\sum_{i:v\in T_i}(5-|T_i|)
=32-4c_v-s_v-\sum_{i:v\in T_i}(|T_i|-1),$$

which must be at least17. Thus every actual J satisfies

$$s_v\le\min\left(8-c_v-h_v,
15-4c_v-\sum_{i:v\in T_i}(|T_i|-1)\right).\tag{2}$$

For any P-pair $\{v,w\}$ not covered by an internal edge or either $T_i$, at least one actual J edge must cover that pair. These are exactly the additional required-support tests in the pilot. Singleton traces cannot cover a P-pair.

These conditions are necessary; no assertion is made that every retained P inventory has an actual exterior realization.

## 2. Restoring a proper blue pair and the full signed system

Given the actual two high traces and J, choose two P points $i,j$ blue, all other P points red. The pair is eligible if

1. $\{i,j\}\notin F$, so no internal edge omits both blue points;
2. it meets both $T_1,T_2$.

Every internal edge then contains a blue point and at least three red points. Each high trace has a blue point and at least one red point, since its size is at least three and only two P points are blue. These edges are already proper.

Let

$$S=s_i+s_j,\qquad k=m_J(i,j).$$

The complete still-active signed system on L has exactly

$$\begin{aligned}
m_4&=16-c_i-c_j-h_i-h_j-S,\\
m_3&=k,\\
t&=n_2-S+k,\\
b&=n_1-m_4.
\end{aligned}\tag{3}$$

Here $m_4$ counts positive four-sets from blue singleton P traces; $m_3$ counts positive triples from all-blue pair traces; $t$ counts negative triples from all-red pair traces; $b$ counts negative four-sets from red singleton traces. The count $n_2-S+k$ subtracts the $S-2k$ mixed pair traces and the $k$ blue pair traces exactly once each. No negative singleton or pair remains, since both high traces have been made proper. No zero-P edge is omitted, because P is an actual hitting set.

All positive and negative constraints have distinct source edges, with their original indices. Each exterior point consequently has total indexed occurrence at most its original degree seven. The exterior ground has17 points. A repair $R\subseteq L$ gives the actual coloring: R red, $L-R$ blue, with the chosen P colors unchanged.

Formula(3) and the following fixed gate tests restore a blue-pair witness algorithmically: scan eligible pairs in lexicographic order, compute the four counts, and take the first pair meeting a listed theorem's hypotheses. This is the same deterministic choice used in the pilot, and involves only21 possible pairs.

## 3. Exact repair gates used

Every gate below has the occurrence cap seven. All positive sizes in this application are three or four; hence the restriction on the number of positive pairs in the new five-small/two-triple theorem is satisfied with zero such pairs.

| Tag in JSON | Exact sufficient conditions used |
|---|---|
|`four_small_3T`|$m_4+m_3\le4$, $t\le3$; arbitrary negative quadruples; [four small / three triples](../../../../../../proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md)|
|`five_small_2T`|$m_4+m_3\le5$, $t\le2$; arbitrary negative quadruples; [five small / two triples](../../../../../../proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)|
|`five_four_10T`|$m_3=0,m_4\le5,t\le10,b\le32$; [five four-sets / ten triples](../../../../../../proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)|
|`six_four_6T`|$m_3=0,m_4\le6,t\le6,b\le35$; [six four-sets / six triples](../../../../../../proofs/propertyb35/SIX_POSITIVE_SIX_TRIPLES_REPAIR.md)|
|`seven_four_4T`|$m_3=0,m_4\le7,t\le4,b\le22$; [seven four-sets / four triples](../../../../../../proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|`eight_four`|$m_3=0,m_4=8$, either $t\le4,b\le17$ ([new eight gate](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR.md)), or $t\le3,b\le20$ ([old eight gate](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md), its20-quadruple strengthening)|
|`seven_mixed`|$m_3\le1,m_4+m_3\le7$, either $t=0,b\le21$ ([zero-triple mixed gate](../../../../../../proofs/propertyb35/SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md)), or $t\le1,b\le20$ ([one-triple mixed gate](../../../../../../proofs/propertyb35/SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md))|
|`eight_mixed_18`|$m_4=7,m_3=1,t=0,b\le20$, ground17 is at most18; [eight mixed gate](../../../../../../proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md)|

An empty positive family uses the empty repair. The pilot never pads positive constraints to reach an exact gate count. Priority among overlapping gates is only for reporting; the mathematical conclusion needs one valid gate.

## 4. Complete missing-$P_4$ candidate domain and transport

Normalize

$$F=\{01,12,23\},\qquad D=\{0,1,2,3\},\quad C=\{4,5,6\}.$$

Both high traces are three- or four-subsets of D; their P traces may coincide, since the actual exterior edge parts can differ. There are five possible trace sets and15 unordered trace pairs with repetition. The two automorphisms of the four-vertex path, identity and reversal, give exactly nine unordered-pair orbits. The pilot forms this quotient by applying both automorphisms to every one of the15 pairs and taking the lexicographically smallest image, rather than assuming a list is complete.

For each representative, every J is a multiset of exactly $n_2\le5$ pairs among the21 unordered P-pairs. `combinations_with_replacement` gives a unique sorted sequence for every such multiset. The raw domain sizes for $n_2=3,4,5$ are respectively1771,10626,53130. Keeping exactly the nonnegative degree counts(1), capacity inequalities(2), and necessary P-pair support conditions cannot exclude an actual input. There are no other filters. Every retained inventory is tested against all eligible blue pairs via(3).

All nine orbit rows finished without a nongated inventory:

| Trace pair | $n_2$ | Retained J inputs |
|---|---:|---:|
|012,012|5|10128|
|012,0123|4|9303|
|012,013|5|44838|
|012,023|5|10128|
|012,123|5|46842|
|0123,0123|3|1075|
|0123,013|4|8401|
|013,013|5|1715|
|013,023|5|10006|
|**Total**||**142436**|

For each row, `PILOT.json` stores the acceptance-tag counts; their sum equals the retained J count. It also records that all nine are complete. Accepted blue pairs are reconstructed by the bounded21-pair scan and the exact gate predicates in the source, rather than by an exterior coloring table.

To return to any actual missing path, first relabel its four support points along the path and its three isolated common points to the displayed sets. If needed reverse the path so that the actual unordered high-trace pair maps to its orbit representative. Carry J along the same relabeling. All label-degree, pair-support and capacity conditions are invariant. The finite result supplies an eligible blue pair in normalized labels; invert the relabeling. Actual constraint counts and properness are preserved, so the corresponding repair gate yields a proper coloring of H by Section2.

This is the complete actual-input connection for a finite P-side selection proof of this shape. Final acceptance of that proof awaits the independent generator and gate replay commissioned by the root agent. No statement here claims the other missing shapes closed.

## 5. Exact stopping inventory for missing $P_3+K_2$

The first nongated necessary inventory is

$$F=\{01,12,34\},\quad C=\{5,6\},\quad
T_1=013,\quad T_2=124,$$

$$J=2\cdot02+04+23+56.$$

Its internal counts are $(2,1,2,2,2,3,3)$, J degrees $(3,0,3,1,1,1,1)$ and actual singleton-trace counts $(2,5,2,4,4,4,4)$. Every necessary P-pair is already covered by an internal edge or high trace; the support requirement adds no further J pair. The degree and exterior capacity tests hold. This is a necessary inventory, not a claimed actual H realization or non-B example.

All proper two-blue choices meeting both high traces give exactly the following signatures:

| Blue pair | $(m_4,m_3,t,b)$ |
|---|---|
|02|$(4,2,1,21)$|
|04 or23|$(6,1,2,19)$|
|13,14,15 or16|$(9,0,4,16)$|

No currently used gate in Section3 accepts these signatures. This does not assert that their actual signed systems lack repairs.

There is one safe additional geometric reduction for the first signature. If the two positive triples $A,B$ for blue02 intersect at $x$, select $x$ red, and forbid a point $z$ of the sole negative triple with $z\ne x$. That triple is discarded. Both positive triples have been hit; the remaining four positive four-sets shrink to sizes at least three after forbidding z. Negative quadruples through x become triples, at most five since x already has at least two positive occurrences; other negative quadruples remain at most21. The elementary four-positive3/4-set lemma with at most eight negative triples and32 negative quadruples in the existing [three-internal partial proof](../../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md) therefore repairs. Negative constraints containing forbidden z are discarded, never shortened. Thus a genuine unresolved actual input for this signature would also require its two positive triples to be disjoint, unless another blue choice repairs it.

No further P inventory or exterior geometry was expanded after this stopping point. The 27 finished and one partial $P_3+K_2$ high-trace rows are exploratory only; $3K_2$ is unprocessed.
