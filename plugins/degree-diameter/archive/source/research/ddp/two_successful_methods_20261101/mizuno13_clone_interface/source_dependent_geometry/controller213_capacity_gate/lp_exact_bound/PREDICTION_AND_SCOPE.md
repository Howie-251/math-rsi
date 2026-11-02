# Prediction and one-LP scope

The original one-call integer feasibility log reports one processed node, zero cuts and an infeasible result, but does not expose an explicit root-LP primal/dual status or a checked infeasibility certificate. Do not infer an LP bound from that log alone.

Make exactly one continuous LP call maximizing sum x, subject to the original364 target rows<=3, the fixed source-cost row<=1092, and0<=x<=1. Omit the sumx>=213 row when maximizing. Existing installed scipy/HiGHS, one thread, whole-process CPU at most10 seconds. No integer solver, new cut, seed, BFS, or graph.

If the numerical LP optimum is below213, read inequality and upper-bound dual marginals. Rationalize their negatives with Fraction, and verify a nonnegative exact dual linear combination column by column. Any tiny rationalization deficit may be repaired by adding its exact amount to the corresponding x<=1 multiplier. The resulting exact rational objective must remain strictly below213. Store the exact coefficients, all364 column inequalities and the exact bound. If this fails or the LP does not separate213, stop and preserve only the raw integer result. No additional LP call or certificate extension.

Prediction is undecided until the single continuous solve. An accepted exact bound would exclude only the specified full27 affine W-transverse block domain through its already justified necessary rows, not all full-neighborhood cloning or nonlinear/partial center sets.
