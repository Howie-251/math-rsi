# Fixed-action free translations, implementation ready

This is a new finite parameter family, following the failed source-quadratic C25/F101 transfer. It keeps m=25, p=101, r=25 and positive phases (1,3,6,7,9), and frees the translations (A,B,C,D,E). It does not change actions, phases, field, or group law. Target: n=2525, maximum degree 10, diameter at most 4; saved lower bound 2485. Actual graph diameter remains unmeasured until a hit is independently checked by root.

The right law is (i,x)(j,y)=(i+j,x*r^j+y). Thus (i,x)^-1=(-i,-x*r^(-i)). Conjugating every generator by (0,c), in the convention g^-1*S*g, changes its translation to x+c*(1-r^i). Since r != 1, choose c=A/(r-1) to set A=0. Common nonzero scaling of all translations is a group automorphism. Normalize the last nonzero entry of (B,C,D,E) to 1. The disjoint charts are E=1 (101^3), E=0,D=1 (101^2), E=D=0,C=1 (101), and E=D=C=0,B=1 (1): exactly 1040604 candidates. The excluded zero tuple is disconnected.

The native source enumerates all reduced generator words of lengths 0..4, using immediate inverse cancellation only, and propagates their four linear coefficients with the right law. It deduplicates coefficient vectors within each phase. Any ordinary walk of length at most 4 reduces to one of these words, so their endpoint union is the exact closed radius-4 set from identity. Left translations give vertex transitivity. Distinct nonzero positive/inverse phases guarantee a simple 10-regular graph for every tuple.

Order: test phase 10 first, then phases 0..24 other than 10. No inverse-phase shortcut is used. Separate raw word counts, distinct formal coefficients, evaluated endpoints, first-failed-phase counters, and full hits. Save a first failure witness for each encountered failed phase, and the first thin-phase passer. A full hit is exported and stops the run immediately; a hit therefore does not claim that the remaining projective charts were tested.

Budget: one worker, at most 60 CPU seconds including compilation and the native child. The wrapper deducts compile CPU and reserves output time. The first 1000 candidates are part of the one scan; it records their actual CPU and projects full cost. An excessive forecast stops as PROFILE_UNKNOWN. A running scan checks its CPU deadline between candidates and stops as BUDGET_UNKNOWN. Neither partial state closes the family. The finite-complete no-hit conclusion applies only if all 1040604 charts were evaluated. No BFS, external verifier, or additional action is run here.

Root owns execution. Commands, after review:

    python3 run.py --onecoeff 18 81 76 1
    python3 run.py

The optional one-coefficient mode only evaluates that literal tuple and checks the existing quadratic r25 control's 66 missing endpoints. It is not a scan and does not count as an additional search family. The normal scan already performs the same inexpensive control at preparation and records its per-phase coverage, so the optional command need not be run separately.

Current state: source written for review; no compilation, forms generation, or candidate evaluation has been executed by the implementation agent.
