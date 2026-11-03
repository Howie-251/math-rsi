# AGL1(29), degree 12: complete necessary capacities

All **38,760 phase modes** are complete. Ordinary reduced-word capacity retains **16,075** modes and distinct field-linear-form capacity retains **8,613**. No field assignment, graph, or BFS was generated. This fixed 812-element group is not excluded by these necessary conditions; passing them does not establish a diameter-3 generating set.

The group order 812 exceeds the saved degree-12 diameter-3 threshold 810 by two. The remaining ordinary projective range has **191,545,562,252 marked assignments**, before actual generator legality; it is not a small complete search.

## Actual group and full scope

Take `G=F29 semidirect_2 C28`. The actual arithmetic checks `2^28=1`, `2^14=28=-1`, and `2^4=16` modulo 29 prove that 2 has order 28, since 2 and 7 are the prime factors of 28. The complete 28-entry scalar table is in `metadata.json`.

Multiplication and inverse are

`(x,j)(y,k)=(x+2^j*y mod29,j+k mod28)`,

`(x,j)^(-1)=(-2^(-j)*x mod29,-j mod28)`.

The only nonidentity involutions are the 29 elements `(x,14)`. Non-involution inverse pairs have phase classes 0 through 13: phase 0 has 14 translation pairs, and each of phases 1 through 13 has 29 pairs. Thus there are 391 inverse pairs and `1+29+2*391=812` elements.

For p inverse pairs and i=12−2p involutions, the p pair phases form a nondecreasing multiset from 14 classes. All involution slots have phase 14 but retain separate field variables. The complete count is

`sum_{p=0}^6 C(p+13,p) = C(20,6) = 38,760`.

The actual component pools are large enough for every such phase multiset. Repeated phases are not merged. A future assignment must still reject the phase-zero identity and any coincident actual inverse pairs or involutions.

## Necessary capacity and parameter checks

For directed letter phase multiplicities a, the exact phase count of freely reduced words of lengths 0 through 3 is

`a*a*a + a*a + (2−2d)*a + (1−d)*delta0`, with d=12 and cyclic convolution modulo 28.

Its total is `1+12+132+1452=1597`. Every phase fiber contains 29 elements, so any entry below 29 excludes the entire mode. Modes with at most three inverse pairs all fail this ordinary test; no symbolic word expansion was performed for them.

Only the 16,075 ordinary survivors receive full symbolic expansion. Each component has an independent field variable. The two letters of a phase-j inverse pair have coefficients `X` and `−2^(−j)X`; an involution has one self-inverse letter with its own X. Appending a letter after phase J adds `2^J` times its coefficient. Identical coefficient vectors at the same phase always evaluate to the same element, for every assignment. Fewer than 29 distinct vectors therefore excludes the mode.

The existing C++ framework was actually changed to Q=29, M=28, R=2, reflection phase 14, fourteen pair-phase classes, and degree 12 only. Five bits per coefficient remain injective for values 0 through 28. One new symbolic case with phases `[0,1,4,11]` and four reflections was compared against the independent saved Python symbolic function: all 28 complete form sets and the ordinary convolution counts match. This was an algebraic parameter check, not a graph test. Every ordinary-pass mode also compares its direct reduced-word counts with the convolution vector.

## Complete results and normalization

| Pairs | Involutions | All modes | Ordinary pass | Symbolic pass | Field variables | Marked projective inputs per surviving mode | Remaining marked total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | 1 | 0 | 0 | 12 | 435,732,491,632,351 | 0 |
| 1 | 10 | 14 | 0 | 0 | 11 | 15,025,258,332,150 | 0 |
| 2 | 8 | 105 | 0 | 0 | 10 | 518,112,356,281 | 0 |
| 3 | 6 | 560 | 0 | 0 | 9 | 17,865,943,320 | 0 |
| 4 | 4 | 2,380 | 222 | 174 | 8 | 616,067,011 | 107,195,659,914 |
| 5 | 2 | 8,568 | 3,977 | 3,811 | 7 | 21,243,690 | 80,959,702,590 |
| 6 | 0 | 27,132 | 11,876 | 4,628 | 6 | 732,541 | 3,390,199,748 |

The ordinary affine automorphism is `F_(lambda,t)(x,j)=(lambda*x+(1−2^j)*t,j)`, with lambda nonzero. Each surviving mode has a component with nontrivial scalar action. Translate the first such component to field coordinate zero, then divide the remaining nonzero field vector by its first nonzero coordinate. If m=12−p is the number of component variables, the exact marked projective count is `(29^(m−1)−1)/28`. The zero vector would generate only a conjugate 28-element complement and cannot cover G.

These marked counts retain possible repetitions from slot permutations and inverse-pair orientations. They are not counts of distinct generating sets or graph isomorphism classes. No further projective normalization, quotient-unit action, or slot-permutation reduction was used. The pure-translation all-phase-zero pattern has no such translation anchor, but it fails ordinary capacity and is not included in any surviving normalized range.

Every original mode and its complete ordinary capacity vector is in `patterns.jsonl`. Symbolic vectors and a failing-fiber coefficient witness are saved for the ordinary survivors. `mode_summary.jsonl` gives each mode's minimum ordinary capacity and all minimizing phases, plus the corresponding symbolic information when evaluated. Every symbolic survivor has all 28 capacities, all tightest phases, an anchor index and an exact marked range in `survivors.jsonl`.

The maximum minimum symbolic capacity is **45 for each surviving composition**, with surplus 16 over the required 29. The first maximizers are:

| Pairs / involutions | Pair phases | Tightest phases | Minimum capacity | Single-mode marked inputs |
|---|---|---|---:|---:|
| 4 / 4 | `[1,2,3,7]` | 11, 17 | 45 | 616,067,011 |
| 5 / 2 | `[1,7,8,8,10]` | 4, 10, 18, 24 | 45 | 21,243,690 |
| 6 / 0 | `[3,4,4,6,7,11]` | 12, 14, 16 | 45 | 732,541 |

There are six, six, and two maximizers respectively; all are saved in `SURVIVOR_SUMMARY.json`. The second six-pair maximizer is `[5,7,9,10,12,12]`. These are concrete smaller normalized entry points if a later actual batch is authorized. The symbolic minimum is not a predicted actual miss count. There are also 26, 287 and 794 surviving modes respectively with at least one exactly-29-form fiber; no tight-fiber linear refinement was run in this task.

## Comparison with already saved 820 and 930 capacities

The following table is derived only from the existing stored capacity results; neither old filter was rerun. It compares degree 12 in all three groups.

| Group order / field / quotient | All modes | Symbolic survivors | Best minimum symbolic capacities at p=4 / 5 / 6 | Surpluses over fiber size | Six-pair marked inputs per mode |
|---|---:|---:|---|---|---:|
| 820 / 41 / 20 | 8,008 | 2,139 | 64 / 62 / 58 | 23 / 21 / 17 | 2,896,405 |
| 930 / 31 / 30 | 54,264 | 5,944 | 40 / 44 / 40 | 9 / 13 / 9 | 954,305 |
| 812 / 29 / 28 | 38,760 | 8,613 | 45 / 45 / 45 | 16 / 16 / 16 | 732,541 |

812 improves the best absolute fiber surplus over 930 in all three compositions. It does not improve the best absolute surplus over 820. For the six-pair composition, the capacity-to-target ratios are 45/29≈1.552 versus 58/41≈1.415 and 40/31≈1.290, and one normalized mode is smaller. However, its 4,628 surviving six-pair modes total 3,390,199,748 marked inputs, more than either comparison group's surviving six-pair total. Smaller individual fibers have not made the entire remaining family small.

The 820 table additionally has one surviving three-pair/six-involution mode; 812 and 930 have none. The comparisons establish different necessary coverage margins and assignment costs, not existence or a reliable ordering of practical success probability.

## Resources and terminal

The single execution completed cursor 38,760 with no next pattern, status `COMPLETE_CAPACITY_ONLY`, one worker and zero restarts. Compilation, the one new symbolic calibration, and the complete capacity run cost **2.476004 CPU seconds**; the C++ capacity process itself cost 1.380982 seconds. Deriving the saved per-mode summaries cost another **0.709228001 CPU seconds**, for **3.185232001 recorded compute CPU seconds** before report writing, within the 60-second authorization.

No field assignments were tested, no graph was generated, and no BFS ran. No next parameter or actual search was started. All requested capacity work is complete; the fixed group's existence question remains open.
