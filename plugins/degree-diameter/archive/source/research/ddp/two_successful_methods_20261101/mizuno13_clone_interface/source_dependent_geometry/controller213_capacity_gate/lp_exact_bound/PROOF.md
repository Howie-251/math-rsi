# Exact linear exclusion of213 affine full27 blocks

Consider cap14 full-old-neighborhood clones of the fixed Mizuno13D5 source, using one complete27-point affine W-transverse center block H_a+c per selected original fiber a. The prior finite geometry gates give the following necessary conditions for its binary selection vector x:

- For each of364 target fibers b, sum_{a ordinary->b} x_a + x_mate(b)<=3. The mate is one of the four ordinary providers and hence has coefficient2. Self-loop loci allow at most9 removed points from the self provider; this preserves the inequality. P only adds load.
- sum_a c_a*x_a<=1092, with c_a=5 for the203 sources with a locally legal g4 block, and c_a=6 for the other161 sources. This is the optimistic consequence of the exact non-W-output exclusivity argument; locally unverified g3 cases remain allowed.
- 0<=x_a<=1.

The complete integer rows/costs are in ../MODEL.json and LP_INPUT.json. The underlying self-loop, M, and g4 scope is documented in ../../exceptional_g4_gate/PROOF.md. The364 rows and columns of the controller matrix each sum5; matching overlap is counted with coefficient2.

## Short exact certificate

SIMPLIFIED_DUAL_CERTIFICATE.json gives365 nonnegative integer multipliers Y for the364 controller rows and the cost row, and364 nonnegative integer multipliers Z for the upper bounds x_a<=1. All multipliers share denominator10000. Multiplying the necessary inequalities by their integer numerators yields

    sum_a q_a*x_a <=2061908,
    q_a = sum_b A[b,a]*Y_b + Z_a.

Pure integer arithmetic verifies all364 coefficients q_a>=10001, and all multiplier numerators are nonnegative. Since x_a>=0, weakening10001 to10000 gives

    10000*T <=2061908,
    T <=515477/2500 =206.1908 <207.

For integral selections, T<=206. Thus this rule gives at most5562 clones and final order94014, below saved14D5=94186 by172. The213 full blocks required for a strict improvement are impossible in this stated domain.

No solver status is needed to verify this final implication. Run verify_exact.py: it imports no solver, reads the saved integer rows/multipliers, checks every sign and column, recomputes the exact right-hand side, and checks the strict inequality. Its saved result is EXACT_CHECK.json, status PASS_EXACT_INTEGER_ARITHMETIC.

## How the coefficients were obtained

The original MIP log exposes raw infeasibility, one processed node, zero cuts, and621 LP iterations; it does not expose an explicit root-LP status. This batch made one continuous LP call maximizing sumx over the same rows/cost/bounds, omitting the cardinality lower row. Its numerical optimum was206.1371673076. Inequality and upper-bound marginals were rationalized, exact per-column deficits were repaired, then every multiplier was rounded upward to denominator10000. All input coefficients are nonnegative, so this upward rounding preserves the dual column inequalities. The final integer arithmetic was checked without invoking the LP solver again.

One LP, zero new MIPs, one worker. Solver CPU0.021435857 seconds; extraction process0.915757263; simplification0.016294812; standalone exact check0.016518553; total measured0.948570628 seconds. No cuts, seed extension, timer continuation, BFS, complete graph, or clone graph was used.

## Exact boundary

This closes all364-source selections of full27 affine W-transverse blocks, with source-dependent slopes and phases, for cap14 full-N cloning of this fixed source. It does not close nonlinear27-point W-transversals, partial blocks, mixed full/partial rules, different clone neighborhoods, or other source graphs. It proves no new degree/diameter construction and is not a Lean formalization. Original raw MIP artifacts and earlier predictions remain preserved; this finite batch is terminal with no pending work.
