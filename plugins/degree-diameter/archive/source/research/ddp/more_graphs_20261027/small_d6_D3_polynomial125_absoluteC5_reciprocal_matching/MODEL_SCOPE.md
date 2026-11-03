# Exact fixed reciprocal-matching family on125 points

The old source in new coordinates is(a,y,h) in F5^3. With inverse2=3, each old dart parameter t gives

    (a,y,h) -> (a+t,-y-3t^2,-h+4ty+t^3).

The reverse parameter is -t. Its only loops are t=0 and(y,h)=(0,0); these are omitted. Actual source construction gives five absolute points of degree4,120 other points of degree5 and310 undirected edges. The old source is retained in every candidate; its diameter was not recomputed. The source gauge from old coordinates is y=b-3a^2,h=c-a^3-4ay, with the inverse described in the paper reviews.

The absolute points(v=0) receive the a-step-one C5. For nonzero v=(y,h), write v=s*rep_L where the first nonzero coordinate of rep_L is one. Directions are ordered(0,1),(1,0),(1,1),(1,2),(1,3),(1,4). Independently choose kappa_L in{1,2,3,4} and add

    (a,v) -- (a+kappa_L/s,-v).

Since tau(-v)=-tau(v), this is a fixed-point-free involution on the120 nonabsolute vertices, giving60 matching edges. It cannot duplicate an old edge: an old edge sending v to -v forces t=0 by its y equation, but the new a shift is nonzero. The source has no absolute-to-absolute edge, so the five C5 edges are also new. Thus every4096 parameter setting is an actual simple6regular125-vertex graph with375 edges. The producer checked this literal degree/symmetry property on each candidate.

Translation of a by any field element preserves all old darts, the absolute C5 and every new matching edge. It acts freely with25 orbits indexed by v. Therefore all25 representatives(a=0,v) would suffice for a positive global diameter-at-most-three certificate. This is not a Cayley or full-vertex-transitivity assertion. A single representative failure is sufficientnegative, with exact global diameter left unknown. The degree6 radius2 Moore bound37<125 would make a complete positive's diameter exactly3.

The canonical tuple in the chosen direction order is(1,1,1,1,4,1), lexicographic index12. It is tested first; the remaining4095 indices are then visited once each. No other source, exponent, absolute-cycle step, field, phase or matching topology occurs in this finite family.

PRED_CONTROL.json checks the four predeclared old-coordinate paths against the actual canonical adjacency. All twelve path edges are present and all four oldvertical targets(0,0,c), c1..4 have actual distance3 fromroot0. The canonical root0 radius is nevertheless only107 vertices, with shells1,6,30,70; it misses18 and its first missing state isID2=(a0,y2,h0). The same root0 traversal supplies the control distances and the family's negative test; it was not repeated.

All4096 settings fail the root0 radius3 test, so no remaining24 representatives or whole-graph distance BFS was needed. This is a complete negative result for the stated reciprocal family, not for arbitrary C5-equivariant matchings, all maxdegree6 preserved-edge augmentations, all125-vertex graphs or the general(6,3) cell. The old single-matching bound is not reused as an exclusion: the absoluteC5 adds two edges per absolute and is a genuinely different rule.

Only histograms, missingcounts and firstmissing states were retained percase; fulluncovered masks were not. Consequently no exact intersection of the4096 missing sets was computed, and no candidates/BFS were rerun to manufacture that statistic. The correct stopping conclusion is supportedlocalrouteprediction but refutedjointcoverage, not further optimization of18 or any smaller missingcount.


## 既存结果触发的后续代数判断

只读4096条CASES的first_missing字段发现它们全部等于ID2（gauge坐标(0,2,0)，也是原坐标(0,2,0)），已存SAVED_FIRST_WITNESS_SUMMARY.json。这不是重跑图或计算完整缺项集合交集。

随后独立纸面核对的ANALYSIS_ANTIPODAL_OBSTRUCTION严格证明：保留absolute C5时，不论怎样给12个非零v的对向pair选择非零shift，只要M(a,v)=(a+tau(v),-v)且tau(-v)=-tau(v)，p0到该Q都没有三步路线。这将停止范围从实测4^6=4096扩大为纸面4^12=16777216；实际枚举数仍只有4096，追加图/BFS为0。未排其它配偶拓扑或一般125点图。

因此下一步不会继续调kappa、同拓扑内的指数或shift。四条事前预测确实修复了原缺路，最终的共同失败是配偶拓扑造成的特定代数障碍，不能以局部修复支持继续该拓扑。
