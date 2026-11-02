# Three fixed quotient profiles: no CRT phase repair

The prediction in `PRED.md` is false. No phase choice repairs all sixteen supports in any of the three fixed Z11 quotient profiles. The returned status is `COMPLETE_NO_REPAIR_IN_THREE_FIXED_QUOTIENT_PROFILES`; this does not exclude the m33 topology with other quotient voltages.

The three profiles are taken literally from the existing diagnostic at attempts777398,867355,1180635. A3 remains0 and e remains11. In variable order(a0,a1,a2,a3,sigma01,sigma23,tau02,tau13,rho03,rho12), their fixed mod11 coordinates are

```
profile1: (3,3,5,0,6,10,10,3,1,2)
profile2: (0,4,9,0,3,6,10,10,4,5)
profile3: (0,7,10,0,5,0,9,2,4,8).
```

All nine remaining phases are free. No a0 orbit representative is imposed; actual nonzero a0 values are screened only by simplicity. If q is a fixed residue modulo11 and phi its chosen phase modulo3, the unique voltage modulo33 is

```
x = q + 11 * (2*(phi-q) mod3).
```

This ranges over every voltage with that fixed quotient. Hence enumerating the complete nine-dimensional phase cube covers all3^9 phase assignments for a capacity-passing profile.

## Capacity distinguishes missing routes from phase collisions

For every one of the16 ordered base pairs, every saved symbolic form is placed into its fixed quotient-residue bucket modulo11. Within a bucket its output phase is the affine function

```
sum(c_j*phi_j) + 2*c_e modulo3,
```

using the nine free coefficients and e=2 modulo3. Two forms defining the same function cannot yield different phase values at any assignment. To cover all three residues modulo33 above one quotient residue, the bucket therefore needs at least three distinct affine functions. This is a necessary gate, not a sufficient independent choice of phases for each bucket.

Profiles1 and2 pass all176 buckets, with minimum function count3. Profile3 fails six buckets, each containing exactly two distinct symbolic forms and two distinct affine functions:

| source | target | quotient residue | first-word witness lines in DISTINCT_FORMS.tsv |
| ---: | ---: | ---: | --- |
| 0 | 3 | 3 | 215,230 |
| 1 | 3 | 5 | 473,486 |
| 2 | 3 | 5 | 729,730 |
| 3 | 0 | 8 | 784,799 |
| 3 | 1 | 6 | 846,859 |
| 3 | 2 | 6 | 922,923 |

For example, source0 to target3 above quotient3 has only the two forms tau02+tau13-rho12 and a2-sigma23+rho03, witnessed by words(5,6,5) and(6,4,0). Whatever their phases, two values cannot cover the three shifts{3,14,25}. This is insufficient route capacity, not a removable collision between many available phase functions. `profile3/CAPACITY.json` preserves all six exact buckets, vectors, functions, word witnesses and source line numbers. Its phase cube was correctly skipped.

## Complete phase-cube results

For profiles1 and2, `phase_cube.cpp` enumerates all nine phases lexicographically and reconstructs the voltages by the CRT formula. It filters the exact simple-controller conditions, then evaluates the full saved33-residue support masks in the established increasing-capacity check order. The actual counts are

| profile | phase assignments visited | simple assignments tested | full16-class solutions |
| ---: | ---: | ---: | ---: |
| 1 | 19683 | 19683 | 0 |
| 2 | 19683 | 13122 | 0 |
| 3 | 0, capacity excluded | 0 | 0 |

Profile2 has6561 illegal phases because a0=0 at one phase, while every other stated condition is automatically separated by its mod11 residues. Both evaluated cubes completed, without a timer stop.

The first-failure counts are

| profile | 33 | 02 | 11 | 01 | 12 | 03 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 17721 | 1886 | 56 | 14 | 4 | 2 |
| 2 | 11800 | 1156 | 134 | 30 | 0 | 2 |

Every other first-failure count is zero. These are complete finite counts for the two cubes, rather than a random sample.

## The surviving phase choices cannot repair the shared gap

Each evaluated profile has exactly two phases that preserve the first eight checked classes:33,02,20,11,01,10,12,21. Both then fail03. Their complete actual tuples, read from the saved phase records without another support search, are

```
profile1:
 (3,25,27,0,17,21,32,25,12,2)
 (3,14,27,0,28,21,10,14,12,13)

profile2:
 (22,26,31,0,25,17,21,21,4,27)
 (11,4,20,0,14,28,21,21,26,27).
```

Within each pair, the second tuple is23 times the first modulo33. The unit23 is1 modulo11 and-1 modulo3, so it fixes the quotient and flips phases. Multiplying deck coordinates by23 scales every free voltage and sends e=11 to-e. The undirected B neighbors at base3 are still the same pair±e, while all other controller edges transform literally. Thus the two phase choices give isomorphic underlying controllers and the same route deficits under multiplication of shifts by23. This is a controller statement; no F11 lift isomorphism is asserted.

The saved representative for profile1 misses03 shifts{2,8} and13 shift{29}; its partner misses{13,19} and{7}. The profile2 representative misses03 shift{5} and13 shift{8}; its partner misses{16} and{19}. These partner deficits follow from the exact unit isomorphism, without extra support evaluation. Other recorded deficits of the original representatives remain in their complete signatures.

The distinction is therefore concrete: profile3 lacks enough quotient-bucket routes, whereas profiles1 and2 have enough local bucket functions but their shared nine phase variables cannot satisfy the support requirements jointly. In particular, preserving the first eight checked classes already forces the two isomorphic surviving phase choices, neither of which fixes03. This closes the proposed phase-only repair of these profiles without asserting that another mod11 profile cannot work.

## Data and receipts

`PHASE_ATTEMPTS.bin` records all39366 evaluated phase assignments, including illegal ones, exactly511758bytes. Each13-byte record contains profile id, the nine phases in free-variable order, simple flag, first failed class, and failing support size. Illegal records use failed class254; a complete record would use255. `DEEP_PHASES.json` preserves the four deep tuples and their exact phase indices.

Capacity checking used0.015862218CPU seconds; compilation1.280931; the complete cube process0.012181; wrapper approximately0.002251; and the final read-only phase-record description0.004358499. Total accounted CPU is **1.315583923seconds**, one worker, within20seconds. There were no failed compilations or retries. `RESULT.json` and `TERMINAL.json` record completion and no active process.

No candidate passed, so no successful controller,462-edge file or17424-word certificate is exported. The success-only literal checks were not claimed as executed. There were no new random samples, changed quotient voltages, second template, changed modulus, F11 graph, BFS, Lean, solver or external review. Only these three quotient profiles under phase repair are closed.
