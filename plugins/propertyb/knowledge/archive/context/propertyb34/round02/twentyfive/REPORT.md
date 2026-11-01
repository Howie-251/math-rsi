# 25-point exact grouped rows and a real q=5 caller

2026-10-15. This closes the proposed arithmetic bridge and a saved strict
numeric witness, not the whole 25-point classification or T34.

## Checked mathematical bridge

`formal/Aris4Math/ThirtyFour/CachedRows.lean` proves, for every valid Numeric
profile with no exceptional empty-pair cap:

- `edgeWeight_factor`: a compatible left/right trace times a coefficient
  depending only on N, the side-slot count, pivot status and residual size.
- `pairWeight_factor`: the joint left/right compatibility indicator times the
  exact ordered coefficient. The lock intersection is proved to be exactly the
  pivot; at a free pivot opposite-side traces are proved disjoint. The formula
  preserves without-replacement denominators and residual-size guards.
- `rows_eq`: A and B equal six-bucket linear forms; C equals the 6 by 6 quadratic
  form minus the actual same-edge diagonal. It does not drop this diagonal or
  replace ordered pairs by unordered pairs.
- `diagonal_compatible_iff` / `cachedDiagonal_eq`: the only trace eligible on
  both sides is [k] at a lock and [] at a free pivot. The correction is exactly
  its multiplicity times its diagonal coefficient. Zero multiplicities cause
  no subtraction error.
- `propertyB_of_counts`: actual H/count equations and complete type labels build
  the existing realization internally and return the original Property B.

These theorems are parameter-general: they also apply to the 21-point five- and
six-lock cases. No special N >= 10 assumption is needed; impossible residual
combinations retain their guards in the coefficients. Quota loss/penaltySum has
not been grouped and remains at its existing type-pair interface.

The local incremental check `cached-r7.log` exited 0 in 4.71 seconds. The parent
also executed the normal module build: `CachedRows-build.log`. Three printed
transitive axiom lists contain only propext, Classical.choice and Quot.sound.

## Sparse actual-input binding

`CachedSparseApplication.lean` proves `realizes_sparse` and
`propertyB_of_sparse_counts`. A finite label list need only contain the support
of μ. Every actual edge contributes to a positive actual trace count; the
assumption count(H,T)=μ(T), for every trace T, therefore proves that all actual
edges occur in that list. No object-domain restriction is added.

This was necessary in the first nine-lock pilot: checking an explicit 512-item
complete list grew beyond 5 GiB resident memory before the useful numeric work.
That process was stopped. The sparse pilot has only the 25 positive trace
labels. Its support proof is symbolic, not an unverified coverage assertion.

## Common coefficient tables

`CachedCoefficients16.lean` checks 204 endpoint and 1224 ordered-pair scalars
against the original binomial formulas. It indexes the 17 possible left counts
and both pivot statuses, retaining one unused free geometry for uniform indexing.
B uses the same endpoint table at the right count. There are no multiplicities in
this common table; all nine-lock 25-point layouts and five-lock 21-point layouts
have N=16 and can reuse it. Six-lock 21-point layouts have N=15 and cannot use
this table unchanged.

The small coefficient-only concatenated check `coefficients-r1.log` exited 0 in
6.60 seconds including rechecking the general bridge. The parent normal build is
`CachedCoefficients16-build.log`.

`CachedIntegerRows.lean` additionally proves exact integer scaling of A and C,
and an integer strict sum implies the corresponding rational strict sum for a
positive common denominator. C subtracts in integers, not truncated naturals.
`CachedCoefficients16Scaled.lean` checks the same common constants at denominator
16! = 20922789888000. Its local check is `scaled-coefficients-r1.log` (7.47 seconds,
including imports). The integer bridge is checked in `integer-r3.log`.

`generate_coefficients.py OUTPUT_DIRECTORY` regenerates the four literal arrays
from exact Fraction/binomial formulas; it does not search profiles or layouts.
The Lean coefficient equalities, rather than that generator, certify the data.

## Actual first numeric caller

`TwentyFiveCoefficientPilot.lean` uses saved q=5 bare witness 4423, copied without
search into `Q5_WITNESS_4423.json`. This is the bare witness with the smallest
successful margin: positions 9 through 17 and bound 12869/12870. Its 25 positive
types total 34 actual edges. The theorem `propertyB_of_counts` takes an arbitrary
H on Fin 25, any actual nine-lock vertex injection, and the complete count
binding. It constructs realization internally and returns PropertyB H. Profile
validity, coefficient binding, and the strict inequality are proved in Lean.

The combined source check `pilot-combined-r3.log` (uncompressed grouping) passed
in 6.90 seconds, RSS 2.68 GB. `pilot-cached-r1.log` also connects the common
coefficient table and passes in 13.58 seconds including rechecking the shared
bridge and coefficient table. The parent normal build is
`TwentyFiveCoefficientPilot-build.log`.

`TwentyFiveCoefficientPilotInteger.lean` repeats this actual-H conclusion through
the integer-scaled row theorem. `pilot-integer-r1.log` passes with only the
standard three axioms; the numeric integer equality itself cost 2.68 seconds.
The combined file includes its shared integer/scale proofs and cost 10.08 seconds.
Normal independent module build is requested separately.

## Measured performance and retained unsuccessful optimization

A same-input comparison is `ProfileComparison.lean` / `profile-comparison-r2.log`
(exit 0). All three exact values are the same 12869/12870. Lean's kernel type
checking profiler reports:

| Finite numeric obligation | Kernel checking time |
|---|---:|
| Original Numeric A/B/C | 12.7 s |
| Six-bucket grouping, direct geometric coefficients | 3.22 s |
| Grouping plus current Fin34 rational coefficient table | 4.57 s |
| Grouping plus 16! integer coefficients, separate run | 2.68 s |

These are one input's incremental measurements, not a prediction for every
profile. The rational lookup vector alone was slower than direct grouped
binomial evaluation. Thus a batch should first use rows_eq and measure actual
throughput before migrating to a more involved table representation.

A further attempt to pre-materialize the 300 masses cost 1.12 s for the mass
equalities plus 3.01 s for the integer value. It was worse than leaving the masses
inside the integer row formula. Its source/log are retained as
`PilotIntegerMassTableAttempt.lean` / `pilot-integer-r2.log`, but it was removed
from the production pilot. This is a representation outcome, not a mathematical
failure. No runtime improvement is inferred from merely declaring a cache.

## Remaining 25-point obligations

This work has not proved the q=5/8/9 catalogues complete in Lean, exported all
11,692 + 840 + 147 callers, recovered the 358 omitted q=5 quota certificates, or
closed the ten-lock promotions. The original structural selection modules and
paper catalogues remain the next inputs. The theorem still requires a specific
trace count binding: it is an actual numeric caller, not an unconditional
25-point theorem. Grok/Gemini review is coordinated by the parent and is not
claimed by these local build logs.
