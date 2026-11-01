# S2 real seven-degree pool: a precise failed fixed-layout prefix

The genuine selection argument is valid, and the first feasible lifted inventory is strict. The fifth necessary lifted inventory is nonstrict under all four authorized insertion slots. The calculation stops at that first failure. The worst-source domain has470 necessary inputs, of which only five were evaluated; the other465 and the remaining five original sources were not evaluated. No new positions, quotas or grids were tried.

## Actual selection and imported local gates

The actual whole spectrum S2 is7^9,9^8,10^4. Select K as its four actual degree-ten points. The six nonstrict abstract c13 inventories from the prior pilot all have mu0=14, no triple/full-four trace, and exactly two singleton-trace original edges in total. Each such edge contains only four points outside K. Their exterior union therefore has at most eight vertices; among the nine actual degree-seven points outside K there is at least one point z on neither singleton-trace edge.

All seven original edges through this one actual z consequently have K trace either empty or one of the six pairs. The two singleton original indices remain unlifted. This does not assert that a freely selected seven-degree point has that property, or that every necessary lifted inventory can occur in an H.

The already strict double-lock degree7/10 gates apply without assumptions about other point degrees. In `../two_six_transfer_20261020/PAIR_RESULT.json`, codegrees5,6,7 have exact zero-quota bounds20041/20995,82887/92378,698285/831402, all at fixed positions(10,21), with actual35-index arithmetic recorded there. Thus in a non-B H each actual z/K-point pair has inclusive codegree between one and four. This is a direct use of those selected-degree fixed certificates and does not import a global two-six role assumption.

All six old sources were read before any lift calculation: their singleton sums are2,2,2,2,2,2. Their exact pair capacities in mask order(3,5,6,9,10,12) are

\[
(3,4,3,3,3,3),\ (3,3,3,4,3,3),\
(3,4,2,3,4,3),\ (3,3,4,3,3,3),\
(3,4,3,2,4,3),\ (3,3,3,3,4,3).
\]

In particular two sources contain a capacity two. The implementation uses the exact counts, rather than assuming that every cell has capacity three or four.

## Complete worst-source necessary domain

For the first worst source, the old mask0,...,15 counts are

\[
\mu=(14,0,1,3,0,4,3,0,1,3,3,0,3,0,0,0).
\]

Let c_p be the number of its exact K-pair-p edges through the chosen z, with p in(3,5,6,9,10,12), and let c0 be the number of its K-empty edges through z. Exact actual conditions are

\[
0\le c_p\le\mu_p,\quad c_0=7-\sum_pc_p\in[0,14],\quad
1\le\sum_{p\ni i}c_p\le4\quad(i=0,1,2,3).
\]

The four inclusive rows are original codegrees lambda(z,K_i). They are positive by pointpair coverage and at most four by the previously strict7/10 gates. The source contains no other eligible K-trace type.

Primary Cartesian cell enumeration gives exactly470 inputs. `VERIFY_PREFIX.py` independently fixes c0 and composes7-c0 among the six pair cells, imposes their actual capacities and row bounds, and obtains the identical470 keys.

Label z by new bit0 and shift K bits one place. Each actual source mask p has mu_p-c_p unlifted original indices and c_p lifted indices; empty masks are treated the same way with c0. This recovers35 original indices and actual selected degrees(7,10,10,10,10). Singleton c is identically zero by the selection argument.

## Single-case pilot, first failure and stopping point

The four old insertion slots were fixed in advance:

\[
(z,K_0,K_1,K_2,K_3)=(a,8,9,20,21),\quad a\in\{1,10,11,12\}.
\]

Every calculation has zero quota. The first feasible cell vector is

\[
(c_3,c_5,c_6,c_9,c_{10},c_{12})=(0,0,0,1,1,1),\quad
c_0=4,\quad\lambda(z,K)=(1,1,1,3).
\]

Its first-case pilot is strict18167/20592, independently replayed over35 actual indices. Therefore the same fixed slots were allowed to continue through the first source.

The fifth necessary input, after four strict ones, is

\[
(c_3,c_5,c_6,c_9,c_{10},c_{12})=(0,0,1,1,0,0),\quad
c_0=5,\quad\lambda(z,K)=(1,1,1,1).
\]

The actual z is on two complementary K-pair edges and five K-empty edges. Its lifted exact trace counts, including zero-count entries to specify every proposed cell, are

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
m&0&1&4&6&7&10&11&12&13&16&18&19&20&21&24&25\\
\hline
\nu_m&9&5&1&3&0&4&0&2&1&1&2&1&3&0&3&0
\end{array}
\]

All other masks are absent. The best fixed bound is2897/2860>1, attained at slots1,10,12; slot11 gives6541/6435. This is an exact failed sufficient bound, not a noncolorable or realized H certificate. The first failure terminates the requested prefix; the other source types are not silently counted as covered.

`VERIFY_PREFIX.py` replays all five actually tested best fixed bounds using the independent falling-factorial implementation, expanding35 distinct original indices and1190 ordered distinct pairs at each of21 pivot positions. All five totals agree exactly, including the first failure. `VERIFY_PREFIX.json` explicitly records the untested465 inputs and includes the full typed failure, original35 masks and independent A/B/C rows.

## Artifacts and scope

- `PILOT_RESULT.json`: all-six singleton check, imported7/10 gate values, first feasible lifted input and four fixed slot values.
- `WORST_SOURCE_DOMAIN.json`: complete470-key necessary domain for the first source.
- `RESULT.json`: the five checked inputs, four strict and the first nonstrict, marked as a stopped prefix.
- `VERIFY_PREFIX.json`: independent complete470-domain reconstruction and all five actually evaluated fixed bounds.
- `PILOT.py`, `PROFILE.py`, `VERIFY_PREFIX.py`: bounded reproduction scripts.

The first pilot used0.021334 CPU seconds, the checked profile0.011672 seconds, and the independent domain/prefix check is recorded in its JSON. All work is far below the twenty-second budget. No original six-tail receipt, old gate, SHARP report, wiki or Lean source was changed. This proves neither an unconditional c13 gate nor its S2-specific completion; it identifies the exact surviving typed obstruction for the parent to judge mathematically.
