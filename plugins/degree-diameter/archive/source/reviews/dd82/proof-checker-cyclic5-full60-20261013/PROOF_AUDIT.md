# Full free-C5 order-60 encoding: local review

**Verdict: PASS for candidate preservation and the actual prepared input.**
This is a same-family, provisional local review, not a SAT result or an
external Gemini acceptance. Run: `dd82-v3-c5-full60-20261013`.

The reviewed domain is all simple order-60, degree-eight, diameter-two
graphs admitting a free C5 action (cycle type 5^12), up to a relabeling of
the twelve orbits. It fixes neither a quotient nor the six-Petersen
structure. It does not cover arbitrary order-60 graphs or C5 actions
with fixed vertices.

## Candidate preservation

1. Coordinates `(a,t)`, with `0 <= a < 12` and `t` modulo five, give
   330 cross-orbit edge choices and 24 internal choices: shifts 0 through
   4 for each of the 66 orbit pairs, and undirected steps 1 or 2 within
   each orbit. These 354 sets partition all 1,770 unordered vertex pairs;
   each set has five edges. Thus their Boolean variables describe every
   invariant simple graph.

2. Each representative vertex has 59 actual potential neighbors. The
   55 cross-orbit literals occur once each, while each of its two
   internal literals occurs twice. The 59-input unary threshold DP
   therefore counts internal degree with weight two. Its bidirectional
   recurrence defines the prefix thresholds exactly, including repeated
   inputs; asserting threshold eight and negating threshold nine gives
   exact degree eight. Orbit invariance supplies the same degree at the
   other four vertices. There are 5,940 threshold variables and 22,968
   degree clauses.

3. For each of the 354 pair-orbit representatives `(u,v)`, the encoding
   uses all 58 real vertices `w != u,v`, with an exact three-clause
   definition of `z <-> (edge(u,w) and edge(w,v))`. Its coverage clause
   is the direct-edge literal or any of those 58 path literals. This
   is the original distance-at-most-two condition. Repeated edge inputs
   in a path remain valid; no fictitious or deduplicated intermediate
   is introduced. The 20,532 path variables account for 61,596 clauses,
   followed by 354 coverage clauses.

4. The quotient cuts are necessary for a target. For
   `D = M^2 + M - 7I - 5J`, nonnegativity and row sum five imply internal
   degree `r` is zero or two, never four. They also imply `q <= 3`
   unconditionally, `q <= 2` if either endpoint has internal degree two,
   and `q <= 1` if both do. The actual 5,610 clauses comprise 330
   unconditional four-of-five exclusions, 2,640 exclusions guarded by
   one selected internal step, and 2,640 exclusions guarded by selected
   steps at both endpoints. The negative guards correctly disable a
   conditional cut when its premise is absent.

5. The pure argument in `CYCLIC5_K66_QUOTIENT_EXCLUSION.md` excludes
   zero or exactly one independent vertex orbit. I checked its quotient
   reduction, the row/column voltage gauges, both complex Gram matrices,
   and the exactly-one-independent-orbit argument. Consequently a target
   has at least two independent orbits. Renaming any two as orbits 0 and
   1 is legitimate because the full palette is retained; the four
   negative internal-step units lose no target up to orbit labels.

The twelve internal-at-most-one clauses and four normalization units,
together with the counts above, give exactly 26,826 variables and 90,544
clauses. Conversely, a satisfying assignment expands directly to a
simple 60-vertex graph with all degrees eight and all distinct pairs at
distance at most two; the added necessary cuts do not substitute for
that exact coverage.

## Actual-file check and seed interpretation

The independent checker
[`cyclic5_full60_independent_check.py`](../../../computations/dd82/construction/cyclic5_full60_independent_check.py)
imports no preparation-generator code. It reconstructed the pair
partition, unary recurrence, guarded subset cuts, and every real-middle
Tseitin clause, then compared the complete expected clause sequence
against the actual DIMACS input. All 90,544 clauses matched. Its own
values for all 26,826 variables also matched the saved seed assignment.

The seed fails exactly coverage clauses 86519, 86869, 87744 and 88094,
with representatives `(40,57)`, `(40,59)`, `(45,52)` and `(45,54)`.
Expanding each orbit gives exactly the 20 bad pairs in the existing
independent BFS, after applying the saved coordinate relabeling. No new
BFS was run. The only other failures are normalization units 22982 and
22983. They are expected: the failed seed has a selected internal cycle
in each orbit, including 0 and 1. It is not a witness for the target
CNF, and the normalization is not an assertion that this seed satisfies
the target's necessary conditions.

The actual result is
[`independent_check.json`](../../../computations/dd82/construction/cyclic5_full60_run/independent_check.json).
This one check used 0.204569269 CPU seconds and 0.299563210 wall seconds.
Solver calls, new BFS runs and search runs were all zero. No concrete
encoding error was found; the prepared input is ready for the parent's
separately authorized bounded solve.

## Workflow scope

I read and applied the local `.agents/skills/proof-checker/SKILL.md`
under the sole V3 plan's DD82 adaptation: one focused delegated
mathematical/source/input review, no additional review agents, generic
audit platform, rendering, hashes, shared-wiki changes or solver work.
The parent owns the Gemini review and any subsequent decision evidence.

Reviewed sources: `cyclic5_full60_prepare.py`, the actual run directory's
encoding/sanity/variable/coverage/degree-counter/DIMACS/assignment files,
the reused unary-threshold helper, and
`CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md` plus
`CYCLIC5_K66_QUOTIENT_EXCLUSION.md`.
