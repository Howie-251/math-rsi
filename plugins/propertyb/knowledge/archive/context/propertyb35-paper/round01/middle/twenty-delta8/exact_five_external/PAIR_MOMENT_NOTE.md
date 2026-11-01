# Why the new pair-moment inequalities do not strengthen the current relaxation

Fix any of the 49 exact five-low inventories μ remaining in `../five_join/FIVE_REMAINDERS.json`. For a low pair ij, let

    Qij = sum_{T containing i,j} (5-|T|) μT
        = 3 cij - sum_{k notin {i,j}} Iijk.

The first equality counts the pairs (e,y) in which e contains i,j and y is an external vertex of e. The second expands (5-|T|)=3-(|T|-2). Thus the same fifteen external vertices necessarily have total inclusive triple count Qij.

For each admissible five-dimensional external cross-codegree profile a, the complete residual (8,8,9) gate gives an allowed set of inclusive triple counts at each pair ij. Every nonempty allowed set contains both 0 and 1; the twelve sets are explicitly recorded in the table in `STRUCTURE_REPORT.md` and in `mixed_triples/GENERAL_GATE.json`. Hence

    t_min(ij,a)=0,       t_max(ij,a)>=1.

Every old feasible profile distribution x has x_a>=0 and sum_a x_a=15. It therefore satisfies

    sum_a t_min(ij,a) x_a = 0,
    sum_a t_max(ij,a) x_a >= 15.

On all 49 source inventories the exact moments satisfy 2<=Qij<=9. More generally nonnegativity and cij<=3 already give 0<=Qij<=9. Thus every one of the twenty proposed inequalities

    sum_a t_min(ij,a) x_a <= Qij <= sum_a t_max(ij,a) x_a

holds automatically for every old feasible profile distribution. These constraints add no restriction. In particular the old positive distributions in `MARGINAL_PILOT.json` remain valid; no additional LP is needed for this conclusion.

This diagnoses the limitation of the separate min/max pair relaxation. It does not show that the simultaneous triple counts can be realized by one external vertex's old-slot promotion, nor by all fifteen actual vertices. Such common-slot compatibility would be a genuinely new constraint and has not been proved or tested here.

No further domain or DP expansion was undertaken. The already submitted tiny LP process finished before the instruction to stop arrived and is retained as `PAIR_MOMENT_PILOT.json`/`.log`, with 49 rational feasible supports; it is unnecessary for the analytic conclusion above and is not claimed as a new exclusion result.
