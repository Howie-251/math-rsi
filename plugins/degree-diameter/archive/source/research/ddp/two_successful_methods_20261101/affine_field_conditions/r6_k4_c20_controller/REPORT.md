# K4 / Z20 controller: exhausted fixed anchored family

**STOP_EXHAUSTED_ANCHORED_FAMILY.** The one deterministic search tried all 2,476,099 assignments in the predicted domain and found none satisfying the complete NB3 source interface. The last assignment was `(g01,g02,g03,g12,g13,g23)=(1,19,19,19,19,19)`. This is a finite-domain negative result; it does not rule out arbitrary six-shift Z20 constructions or other 80-vertex controllers. The unit anchor is not a WLOG normalization over composite Z20.

For each of four root bases, all 150 length-three nonbacktracking port words were precomputed. Equal source/target bases receive 48 words; every different-base group receives 34. Each word records its exact target base and six signed integer shift coefficients in `WORD_COEFFICIENTS.tsv`. A separate 600-row symbolic audit reconstructed every base step and coefficient and passed, without a second parameter search or any graph construction.

For each candidate, each root/target-base group was evaluated into a 20-bit residue mask. Equal-base groups require all 20 residues. Different-base groups require all residues except the two adjacent residues `0` and the signed corresponding shift. Thus acceptance means all 296 required translation classes, equivalently all 5,920 ordered same/nonadjacent vertex pairs, have an actual NB3 route. The first failed group rejects the assignment. Every assignment failed, as summarized below; these are counts of assignments rejected at their first failed group, not counts of missing vertex pairs.

| Root base | Target 0 | Target 1 | Target 2 | Target 3 |
|---|---:|---:|---:|---:|
| 0 | 1,984,117 | 475,964 | 13,601 | 1,799 |
| 1 | 0 | 272 | 261 | 65 |
| 2 | 0 | 0 | 14 | 6 |
| 3 | 0 | 0 | 0 | 0 |

These entries sum to the complete 2,476,099-element domain. Zero entries include groups not reached after earlier failure; they are not assertions that those groups always pass. No assignment survived the first three root bases.

CPU: C++ compilation 0.613433 seconds, search plus coefficient output 0.471266 seconds, measured driver total 1.089915516 seconds. The supplementary symbolic encoding check used 0.004729529 seconds, bringing measured task CPU to 1.094645045 seconds, within the original 30-second total. One worker; no timer continuation.

The rule itself always defines a simple 6-regular 80-vertex / 240-edge controller and contains a K4 at each fixed deck. Because the NB3 gate has no passing assignment, no literal controller edge table, port table, triangle table or pair witnesses were emitted. No fiber graph, BFS, solver, Lean, old-graph revalidation, installation, alternate modulus, hashes or accepted-count changes occurred. The r6/F9 local PASS remains valid but does not by itself produce a 58,320-vertex lift here. Any unanchored/nonunit extension would be a separate, newly justified scope; it is not dispatched by this result.

Files: `PREDICTION.md` is the pre-run fixed scope; `search.cpp` and `run_once.py` implement the single search; `RESULT.json` records the complete search outcome and CPU; `WORD_ENCODING_CHECK.json` records the symbolic audit. `TERMINAL.json` freezes this scope as STOP.
