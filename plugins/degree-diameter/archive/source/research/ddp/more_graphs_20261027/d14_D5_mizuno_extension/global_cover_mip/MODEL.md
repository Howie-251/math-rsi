# Global14pin cover model

For all3685 cachedfreevertices p, choose x_p in{0,1}. Require sum(x)<=14 and, for each currentoldvertex v in0..94185, sum{x_p:v inR4(p)}>=1. Objective0. This is exactly the single-point extension criterion for the inherited94186source, with alloldedges retained and newdegree<=14.

Use exactconstraint-generation only: begin with128lowest-support and128evenlyspaced targets; preserve all3685columns. Everymodelincumbent is checked on all94186targets by OR of its literalcachedR4columns. Failure adds up to1024actualviolated rows, drawn deterministically fromlow-support andevenlyspaced missingIDs. Eachcut is an originalconstraint, so no fullsolution is lost. Fullcoverage is the sole SATacceptance; no incumbent/timeout is UNKNOWN, and untrustedsolverinfeasible is not a certified familyexclusion.

At most8modelcandidates; stop onfirstfullcover orfirstnoincumbent. Cumulative solverCPU<=30sec, wholeprocessCPU<=60sec/wall<=180sec, oneHiGHSthread. Firstwindow5sec and subsequentchanged-model windows up to8sec, bounded by the remaining29secworking allowance. No repeatedgreedy, same-model coldrestart, oldBFS/balls, dependencies or hashes.
