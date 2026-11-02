# 816-point four-pair tight-fiber branch: complete, no D3

The twelve specified four-inverse-pair/four-reflection modes are closed within this fixed family. Iterated necessary linear restrictions reject two modes, and the entire remaining **15,085,980 marked assignments** were evaluated. Of these, **10,317,300 are legal twelve-element generating sets**; every legal assignment fails its first exact tight fiber. There are **zero full-fiber survivors, zero graph constructions and zero BFS traversals**.

This result uses the actual group `F17 semidirect_3 C48`, degree 12 and order 816. It does not concern the other branch being processed by another worker, and no previously completed maximin mode was rerun.

## Necessary reduction

The full preservation argument is in [SCOPE.md](SCOPE.md). Each fiber with exactly seventeen different forms must evaluate bijectively to F17, forcing the sum of those forms to vanish. The complete exact-tight sets are used; no arbitrary subset of a larger fiber is selected. The nontrivial-action translation anchor is removed before the kernel calculation, and restrictions are iterated after each form deduplication.

All twelve modes first lose one dimension, from seven anchored field coordinates to six. Ten stabilize at dimension six. The remaining two modes have new tight fibers 21 and 27 and need a second independent constraint:

| Pair phases | Original tight fibers | New tight fibers | Final dimension | Final minimum capacity | Result |
|---|---|---|---:|---:|---|
| `[1,9,11,15]` | 3,45 | 21,27 | 5 | 12 | Rejected |
| `[5,9,15,17]` | 3,45 | 21,27 | 5 | 12 | Rejected |

The matrices, ranks, bases, intermediate counts and deficient-fiber coefficient witnesses are in `patterns.json`. Ten stable bases and all final restricted forms are saved in `survivors.json`.

The original marked range was **307,754,004**; it was not enumerated. Each six-dimensional surviving kernel contributes `(17^6−1)/16=1,508,598` projective inputs, giving **15,085,980 actually processed inputs**. Only the kernel coordinate z is normalized; the original field vector is restored through the full basis and receives no second projective filter.

## Complete actual enumeration

| Pair phases | Marked inputs | Legal sets | Illegal sets | First tested endpoint phase | Exact first-fiber pass |
|---|---:|---:|---:|---:|---:|
| `[1, 3, 11, 21]` | 1,508,598 | 1,031,730 | 476,868 | 15 | 0 |
| `[1, 3, 13, 21]` | 1,508,598 | 1,031,730 | 476,868 | 9 | 0 |
| `[3, 5, 7, 21]` | 1,508,598 | 1,031,730 | 476,868 | 15 | 0 |
| `[3, 5, 17, 21]` | 1,508,598 | 1,031,730 | 476,868 | 15 | 0 |
| `[3, 7, 19, 21]` | 1,508,598 | 1,031,730 | 476,868 | 9 | 0 |
| `[3, 11, 21, 23]` | 1,508,598 | 1,031,730 | 476,868 | 15 | 0 |
| `[3, 13, 21, 23]` | 1,508,598 | 1,031,730 | 476,868 | 9 | 0 |
| `[3, 17, 19, 21]` | 1,508,598 | 1,031,730 | 476,868 | 9 | 0 |
| `[5, 7, 9, 15]` | 1,508,598 | 1,031,730 | 476,868 | 21 | 0 |
| `[9, 11, 15, 23]` | 1,508,598 | 1,031,730 | 476,868 | 21 | 0 |

Each actual set is checked for twelve distinct nonidentity elements, including all four reflections and all inverse-pair components. Exact field-value masks, not only symbolic form counts, test coverage. All **10,317,300 legal assignments** fail test position zero; no later fiber is claimed to have been evaluated for them. All **4,768,680 illegal assignments** are explicitly accounted for.

The new basis restoration was calibrated once using an actual legal twelve-element example: z=`[1,2,3,4,5,6]` gives fields `[0,14,1,2,3,4,5,6]`. Independent direct group words through length three and evaluated symbolic forms agree as sets in all 48 fibers. Evidence is `restoration_calibration.json`. This one arithmetic example did not create a graph or run BFS, and no repeated calibration or final graph check was needed.

## Files, resources and terminal

`linear.py` performs the exact iterated necessary closure. `search.cpp` reuses the established exact-fiber engine with the actual 6x7 restoration basis and generic twelve-element legality. `inputs.json/.txt` preserve all ten phase modes, bases, fiber order and forms; `production.log`, `terminal.json` and `summary.json` preserve the full actual cursor and counts.

Linear closure and its arithmetic calibration cost **1.010749302 CPU seconds**. Preparation and compilation cost **1.245334 CPU seconds**; the actual complete enumeration used **1.420188 CPU seconds**. Recorded cumulative work including linear closure is **3.680025302 CPU seconds**, within the 120-second budget, one worker and zero restarts.

Status is `COMPLETE_FOURPAIR_TIGHT_SCOPE_NO_SOLUTION`, all ten production modes complete, final cursor 15,085,980 and next position null. No candidate passed all exact fibers, so no best or diagnostic graph was manufactured and no independent final graph check applies. Pending actions are empty. No other mode, group or seed was started.
