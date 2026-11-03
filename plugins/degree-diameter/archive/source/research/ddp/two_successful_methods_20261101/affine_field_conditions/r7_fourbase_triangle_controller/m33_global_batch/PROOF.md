# One m33 global batch: sample cap reached, no controller found

The single authorized batch returned **UNKNOWN_SAMPLE_CAP_REACHED** after2,000,000 legal candidates. It did not find a controller with complete exact-three-walk coverage. This is not a fixed-family exclusion, and the unused CPU allowance does not authorize another run. No modulus or topology change was made.

## Actual search domain and generation

The target was only m33, e11, four bases and the fixed A/B/S/T/R topology. Its conditional lift target175692 exceeds the located public degree77 guarantee169750 by5942. This experiment produced no lift graph or accepted graph.

The deck gauge changes base3's coordinate by+a3, setting A3=0 and changing a2,sigma23,tau13,rho03 by+a3. All zero B edges and e remain fixed. Units u modulo33 with u=1 modulo3 also preserve e. The nonzero a0 orbits have representatives[1,2,3,11,22] and sizes[10,10,10,1,1]. These facts were also checked on paper by the complementary agent, without repeating the symbolic word enumeration.

Candidates use those representatives in a repeating five-branch cycle and directly satisfy every exact simplicity condition. Each candidate's other voltages is independently drawn; no candidate is modified in response to its coverage score. The PRNG is `std::mt19937_64`, decimal seed2026110107, with rejection-based unbiased bounded draws. The completed batch consumed16,191,788 raw PRNG outputs. Each of the five branches received exactly400,000 legal candidates. This sampling distribution is uniform within each normalized branch's specified legal coordinates, rather than uniform over all labelled graphs or over symmetry orbits.

`ATTEMPTS.bin` preserves all2,000,000 actual candidates in order: exactly24,000,000bytes, twelve unsigned bytes per row. Its first ten fields are

```
(a0,a1,a2,a3,sigma01,sigma23,tau02,tau13,rho03,rho12),
```

followed by first failed class encoded as4*source+target and that class's support size. A successful record would use255 and33 for those last fields. There are no successful records. The PRNG seed and complete record format are also fixed in `PRED.md` and `search.cpp`.

## Actual support gate

Each candidate uses the complete previously saved symbolic endpoint forms evaluated modulo33, with e=11. Classes are checked in increasing symbolic capacity, with lexicographic order for ties:

```
33,02,20,11,01,10,12,21,03,23,30,32,13,31,00,22.
```

Here a two-digit class denotes source base followed by target base. The first class33 has51 symbolic forms, and the next two classes02 and20 have56 each. A candidate stops at its first failed class. Inverse symmetry explains why reverse classes do not cause new failures after their forward class passes; these zero entries are not skipped checks.

| First failed class | Candidates |
| --- | ---: |
| 33 | 1962566 |
| 02 | 36946 |
| 11 | 386 |
| 01 | 84 |
| 12 | 15 |
| 03 | 3 |
| Every other first-failure class | 0 |

Thus37,434 candidates passed the51-form first gate,488 passed the next02 gate,102 passed11,18 passed01, and3 passed12. None passed03. The actual first-gate support-size histogram is preserved in `RESULT.json`; its maximum is33. No sampling conclusion is extrapolated to exhaustive failure.

## Complete signature of an actual sampled candidate

The report representative maximizes the number of completed classes in the specified order, then the size at its first failing class, among candidates actually sampled. Choosing it for reporting did not affect subsequent generation. Its voltage tuple is

```
(22,26,31,0,25,17,21,21,4,27).
```

Its complete16-class coverage-size signature is

| source / target | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 33 | 33 | 33 | 32 |
| 1 | 33 | 33 | 33 | 32 |
| 2 | 33 | 33 | 31 | 33 |
| 3 | 32 | 32 | 33 | 33 |

The missing residues are03:{5},13:{8},22:{9,24},30:{28},31:{25}. These are recorded literally in `EXAMPLE_COVERAGE.json`. This representative completes eight classes in the check order and eleven classes overall. It is not asserted to minimize the total deficit among the entire family or even among all sampled candidates.

## Receipts and terminal scope

Compilation passed on its first attempt. The compile process used1.337469CPU seconds, the full batch process0.482482, and the wrapper approximately0.002335; cumulative accounted CPU is **1.822285705seconds** within the30-second single-worker budget. The stopping condition was the2,000,000-candidate cap, not the CPU cap. All attempts, seed, failure counts and actual terminal state are saved.

Since no candidate passed, the conditional success branch for a literal132-vertex controller,924 inverse equations,132 B triangles,1372 word bindings and17424 ordered-pair word certificate was not executed. No purported successful controller or certificate was exported. No full F11 graph, BFS, Lean, solver, hillclimb, second seed, automatic retry, other modulus or external review was run. `TERMINAL.json` records no active process. Any further study requires root's separate mechanism decision.
