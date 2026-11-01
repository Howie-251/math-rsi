# Mixed five-lock Lean assembly (in progress)

Scope: the 24-vertex branch with five actual unit-codegree locks of degrees
6,6,7,7,7 and the actual low bad-pair avoidance supplied by
`TwentyFourSelection.MixedLocks`. Root handles other branches and reviews.

The generator `computations/propertyb33/round02/generate_v24_mixed.py` transports
saved witnesses from `round01/small-math/V24_SMALL_R_CERTIFICATES.json` to all 32
labelled high-trace families, without an unproved isomorphism quotient.
It produces 48 distinct positional profiles, 210 distinct loss rows and a total
selection function on 32*8*8 = 2048 padded low-slot inputs. Exact Python Fraction
replay agrees with every original witness; the largest resulting bound is
75421/75582. This is preparation evidence, not itself the Lean theorem.

`TwentyFourMixedData.lean` is built. `TwentyFourMixedFacts.lean` kernel-checks
actual-count recovery, complete slot coverage, profile identity and validity.
`TwentyFourMixedNumeric.lean` checks A/B/C formulas, nonnegative two-quota duals,
actual-slot/dual loss selection and strict final inequalities. `TwentyFourMixed.lean`
assembles actual-H classification, actual low bad pairs, both directed weights,
actual avoided-edge quotas and CustomDeletion into Property B. Its final intended
exports are `propertyB_of_mixed_locks` and `propertyB_of_many_sevens`.

Current state: full actual caller source written but not compiled yet; finite
cache layers are being checked first. The first unpartitioned finite proof was
terminated after 8 minutes and about 5GB memory with no completed output. Splitting
by labelled family gave kernel subproofs for all32 count recoveries in ~25 seconds
and for all32 slot-coverage cases in ~63 seconds. Current staged run is session
11107 (`facts-first.log`, profiler enabled); no numeric/caller acceptance claim
until completed build and transitive axiom audit. No sorry/native_decide/new axioms
have been introduced.


Update: Facts completed successfully (`facts-second.log`, exit 0; standard
three axioms). The expensive profile equality was replaced by extensionality on
the five structure fields followed by kernel `decide`; a standalone check of all
48 profiles succeeds in seconds. Numeric is now running as session91020, output
`numeric-first.log`. Actual classification/profile realization, actual low-slot
extraction and the MixedLocks embedding were each independently checked in the
small `CheckActual`, `CheckActualLow`, `CheckEmbedding` Lean callers (all exit0).
These isolated interface checks have no placeholders and do not assert the
unbuilt final PB theorem.


Completed: final `lake build Aris4Math.ThirtyThree.TwentyFourMixed` exit0 (1010 jobs),
and independent ImportAudit exit0 with the original Bool-color count statement.
Both exports have only the standard three axioms; see REPORT.md and final logs.
