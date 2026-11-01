# Reusable method from the 23-point seven-degree branch

The decisive change was to select a fixed-size set minimizing its total internal codegree excess, instead of relying only on a large color class with small internal maximum degree.

For a nonnegative weighted graph on r vertices with weighted degree at most D, choose a k-set S minimizing total internal weight W. For x in S and y outside, the swap inequality is d_S(y)>=d_S(x)+w(x,y). Summing it and charging the other k-1 selected vertices by D gives

    (r-k-1)d_S(x)+2W <= D(k-1).

Averaging also gives W<=floor(D*k*(k-1)/(2*(r-1))). Both inequalities are proved for the actual chosen set, not imposed on a convenient test family. Equality can be unusually rigid: in the present D=6,k=6,r>=14 case, W=6 forces two actual K7 components through zero-cost swaps. This then gives a real additional lock with exactly known unit codegrees.

The numerical work supported the structural proof by identifying only five residual cluster graphs. A seventh vertex selected by cut-weight averaging reduced to finitely many exact neighbor vectors. Requiring every deletion projection to remain residual was much stronger than independently testing one selected layout; it cut20949 promotions to1125 profiles, with only one profile needing the shared-bad-count dual.

Practical lessons: normalize full trace profiles before expensive subset-position DP; in this run, an initial3378 labelled prefix became a complete725-orbit six-point domain. Joint-layout searches at120 sampled orders are proposals, not an optimum over orders: a subsequent720-order pass settled33 of111 old residues. The saved strict certificates are valid at any order count, but a failed sampled pass is not a mathematical obstruction.

A targeted literature check found Caro–Hansberg's general k-independence bound, which at ordinary maximum/average degree6 and induced degree2 gives only r/3, no improvement over the three-color selection for this task. Only the primary abstract/metadata were read; no weighted version was assumed. Source: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i1p33/ (2013), arXiv:1208.4734. The minimum-set exchange lemma above is derived directly here and does not depend on that paper.
