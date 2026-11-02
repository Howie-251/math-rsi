# Fixed m50 root00 exact-cover gate: prediction before execution

This batch concerns only the fixed three-base seven-port Schreier rule, modulus 50 and half-shift 25. It does not reopen lower moduli or generate a fiber graph. Root's public degree77 competition gate must arrive before the parameter gate is run; preparing, symbolic verification and compilation are allowed beforehand.

First compare the saved root00 symbolic coefficient set with the following independent set expression, without another finite-field enumeration. Put a=alpha0, s=sigma, t=tau and d1=alpha1, d2=-alpha2, d3=rho. The 50 forms should be the disjoint formal union of

* F7={+a,-a,+3a,-3a,h,h+2a,h-2a};
* for v=s,t: {+a+v,+a-v,-a+v,-a-v,h+v,h-v};
* {0,+s,-s,+t,-t,s-t,t-s};
* for d=d1,d2,d3: block(d)={+z,-z:z in d+{0,s,-t,s-t}}.

The first three bullets give 26 forms; the three blocks give eight each. If the symbolic identity fails, stop and report the discrepancy before search.

At m50 the root00 support must contain all 50 residues, so the evaluated base26 and three block8 sets must be pairwise disjoint and cover Z50. The already completed parity gate requires alpha0 even. Simple controllers exclude alpha0=0. Multiplication of all parameters by a unit modulo50 preserves h=25 and every coverage condition; the two possible gcd classes of nonzero even alpha0 therefore have representatives a=2 and a=10. Enumerate only those two representatives and s,t in 1,...,49, at most 4802 outer pairs. For each, keep d in 1,...,49 only when its block has eight distinct values and avoids the 26 distinct base values. Test triples of disjoint blocks that fill the remaining 24 residues.

Permuting d1,d2,d3 leaves the underlying controller graph unchanged: its base1-to-base2 neighbors have shifts {0,d1,d2,d3}, and the reverse neighbors have their negatives; all other neighbors are unchanged. Each assignment still binds two of these nonzero matchings to a+/a- and the last to r, with a and r satisfying the same simple-controller constraints. Hence retain sorted d1<d2<d3 as one representative per underlying graph, and set (alpha1,alpha2,rho)=(d1,-d2,d3). The output port words will refer to this actual assignment.

Prediction: the exact-cover gate may exclude all m50 candidates or leave a small set on which the nine saved symbolic support classes can test full exact-three-walk coverage. A root00 tiling is necessary only. Stop at the first actual controller passing all nine supports, and export its literal port table and exact three-port-word certificate. If the search exhausts, distinguish root00 tiling failure from failure at later full coverage. Record visited counts, completeness, CPU and actual stopping status.

The new cumulative budget is 20 CPU seconds, including preparation, compilation and export, one worker. No automatic time extension, modulus ladder, controller optimization, fiber graph, BFS, Lean, solver or external review is authorized here.
