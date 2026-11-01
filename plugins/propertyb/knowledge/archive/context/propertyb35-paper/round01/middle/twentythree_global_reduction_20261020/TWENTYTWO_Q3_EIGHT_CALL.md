# Direct reuse of the eight-red lemma at 22-point q3 sources

Let $H$ be22-point, simple, five-uniform, with 35 edges. Suppose an original edge $F$ has exactly three neighbors in the non-unit-intersection graph $\Gamma$. Suppose the three exceptional traces $T_1,T_2,T_3$ all contain one point $v\in F$ and each has size at least two. If exactly eight of the other 31 singleton-intersection edges attach at $v$, then $H$ has Property B.

Color only $v$ red in $F$. This makes $F$ and the three exceptional edges proper. On $L=V\setminus F$, which has 17 points, the remaining constraints are eight red four-sets and23 indexed blue four-sets. The red four-sets are distinct, by simplicity of the original five-edges. The blue four-sets may repeat, and all 23 original indices are retained.

The existing [eight-red-foursets lemma](../eight_red_foursets_seventeen_20261020/PROOF.md) applies on the same outside ten-red/seven-blue sample. Its quantitative proof gives, for eight red sets and $b\le24$ blue sets,

\[
 \#\mathrm{bad}\le8\binom{13}{6}+b\binom{13}{10}-1218.
\]

At $b=23$ this is

\[
 8\cdot1716+23\cdot286-1218
 =19088<\binom{17}{10}=19448. \tag{1}
\]

Thus at least 360 outside samples give a coloring of all 35 original edges. No point-degree, pair-cover, clean-point, or new-layout hypothesis occurs in this local invocation.

## Actual caller

The previously verified complete22-point q3 domain and actual relabeling reduce to the following source labels in [the 22-point source report](../twentytwo_min7_gamma_four_20261020/REPORT.md):

|source|singleton multiplicities on $F_0,\ldots,F_4$|exceptional traces|
|---:|---|---|
|20|8,5,5,6,7|7,27,29|
|21|8,5,5,7,6|7,27,29|
|22|8,5,6,6,6|7,27,29|
|23|8,6,5,6,6|7,27,29|
|24|9,5,5,6,6|7,27,29|

All three trace masks contain bit0. Therefore (1) directly eliminates source20–23 in their actual original hypergraph coordinates. Sources20/21 form one old role,22/23 a second; the only remaining old role is source24. The source fields and proof interface were independently read in [EIGHT_RED_22_CALL_REVIEW.md](EIGHT_RED_22_CALL_REVIEW.md), with exact original inventories checked by [SIX_SEVENTEEN_CHECK.json](SIX_SEVENTEEN_CHECK.json). This is declared reuse of the old eight-red lemma, rather than a new probability calculation.

For source24 the red multiplicity is nine. Removing one red constraint or treating it as blue would not preserve the original coloring problem, so the eight-red theorem does not directly resolve that source.

## A short additional boundary for source24

If source24's nine external red four-sets are pairwise intersecting in at most one point, that source also has a direct coloring. Indeed, write $m$ for their number of intersecting unordered pairs. Their 36 incidences on 17 points imply $m\ge21$: if $\rho_x$ is the number of red four-sets containing $x$, then $\binom{\rho_x}{2}\ge2\rho_x-3$ for every nonnegative integer $\rho_x$, and summing over all seventeen points gives $m\ge72-51=21$. In the same ten-red sample,

\[
 S_2=\binom92\cdot36+84m=1296+84m.
\]

For a triple with $s$ intersecting pairs, the simultaneous event count is bounded by $(0,0,1,8)_s\le3s$. Each pair is in seven triples, hence $S_3\le21m$. Upper Bonferroni gives red-union deduction

\[
 S_2-S_3\ge1296+63m\ge2619.
\]

Adding22 indexed blue events gives

\[
 9\cdot1716+22\cdot286-2619=19117<19448. \tag{2}
\]

Consequently a non-B realization of the remaining source24 must contain two of these nine red outside four-sets intersecting in at least two points. This is a condition on that same actual source, not a new layout search or a proof that source24 is impossible. No unconditional nine-red lemma is asserted here.
