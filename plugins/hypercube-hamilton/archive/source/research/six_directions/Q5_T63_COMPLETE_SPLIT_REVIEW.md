# Q5 T63 marked 2/4 split: independent review

2026-11-01. ARIS proof-checker; fresh reviewer `/root/t63_complete_split_review`.
Explicit user route: GPT-6.1-sol / high. Assurance is **same-family / provisional**.

**PASS** for the precise marked split theorem, including zero original crossings.
No mathematical gap was found. This is not acceptance of unrestricted Q5 T63,
complete ten-hole covered targets, the remaining Q6 layers, or full P6.
Producer code, frozen inputs, previous imports, and main state were not edited.

## Quantified statement and dependency ledger

For every matching F of K(Q5) whose uncovered set H consists of six vertices
of one parity, and every U subset H with |U|=3, if there is a coordinate
with face counts (|H_A|,|U_A|)=(2,1), (|H_B|,|U_B|)=(4,2), then a simple
cycle on exactly Q5 minus U contains F and has every other edge short.
The thirteen edges of F may be arbitrary, including long and same-parity
edges. Crossing count zero is included; no partner restriction is added.

| ID | Obligation | Discharge |
|---|---|---|
| S1 | Normalization preserves the conclusion | One common XOR and coordinate permutation acts on both faces and preserves short edges and prescribed edges. A marked hole becomes 0; the other A hole has distance 2 or 4 and becomes 3 or 15. B holes then have odd local parity. |
| S2 | N14 complete canonical domain | Independently recurse over all unordered pairings of the fourteen nonholes for each A representative; set equality and unique record binding give 270270 inputs. |
| S3 | T44 complete canonical domain | Normalize one marked omission to 0 and the other to 3 or 15; choose two other even holes among the six remaining even vertices. Thirty geometries, each with 10395 matchings, give 311850 inputs; exact set equality checked. |
| S4 | Positive local cycle and optional union validity | Every supplied cycle has precisely the retained vertices, contains every prescribed edge, and uses short edges for every other edge including closure. Recomputed witnessed unions equal stored masks. |
| S5 | Positive-crossing reduction | 2|F_A|+c=14 makes c positive even. A perfect matching D of X_A leaves exactly the two A holes. Delete D from the N14 cycle, attach the injective actual crossing edges, and compress into a matching R on X_B disjoint from F_B. T44 applies with the original four B holes and its two marked omissions. Expansion gives one 29-cycle; D and all artificial compressed edges disappear. |
| S6 | Large-union branch | Every N14 witnessed mask has at least 15 short edges. Every nonlow T44 mask has at least 18. The shared cube has 32 short edges, so the masks intersect. Choose just one common edge and its two independent witnessing cycles. |
| S7 | Low branch complete | Exactly the 6978 canonical T44 records with witnessed size below 18 are carried forward, with exact low-file byte equality. |
| S8 | Relative placements complete | All 24 coordinate permutations and 8 odd translations of each low B input are transported in the fixed A coordinates, including mates, unordered omissions and optional masks. Every actual B input has such a normalized description. Duplicate descriptions must have identical witnessed masks. |
| S9 | Exception set complete | Deduplicate to 163152 actual B states, group A masks by width, and compare all pairs with width sum at most 32. Larger sums intersect automatically. Independent reconstruction gives exactly the frozen 1320 ordered matching pairs, without duplicates. |
| S10 | Every exception positive | Exact one-to-one pair coverage by 1320 direct simple 29-cycle certificates, each with exact omissions, all thirteen required edges and short new edges. Local deletion/bridge witnesses independently reproduce the same global cycle edge sets. |
| S11 | Zero-crossing conclusion | F_A and F_B have exactly the above independent complete-graph matching domains. Apply S6 or S10 after S1 and undo the common map. The odd global hole parity is handled by translation too. |
| S12 | Geometry scope and census | Independently enumerate all 160160 marked even-hole geometries and full parity-preserving Q5 orbits. Exactly 133760 geometries in 106 of 135 orbits have a good split; 26400 geometries in 29 orbits remain outside this criterion. |

The dependency graph is acyclic: explicit Q4 positive tables and elementary
symmetry imply the local statements; local statements plus the finite positive
exception coverage imply the marked Q5 theorem. No Q5 T63 or Q6 conclusion is
used to establish its inputs. The local tables reestablish the required N14
and T44 statements directly; previous accepted imports are consistent and hash-bound.

## Independent computation

New checker `Q5_T63_COMPLETE_SPLIT_REVIEW_check.cpp` was compiled with
`D:\mingw64\bin\g++.exe -std=c++17 -O2` and executed successfully.
Its result is `Q5_T63_COMPLETE_SPLIT_REVIEW_check.json`. No producer executable
or producer Python module was run or imported. Exhaustive matching domains
were rebuilt as sets, independently of producer iteration order.

| Check | Independently obtained |
|---|---:|
| Canonical N14 inputs | 270270 |
| Canonical T44 inputs | 311850 |
| Positive N14 cycles replayed | 3228001 |
| Positive T44 cycles replayed | 1848666 |
| Canonical low T44 inputs | 6978 |
| Low transformed descriptions | 1339776 |
| Distinct actual low B states | 163152 |
| Width-filtered scalar comparisons | 65760096 |
| Exact disjoint witnessed-mask pairs | 1320 |
| Direct positive global cycles | 1320 |
| Four-bridge positive cycles | 1308 |
| Six-bridge positive cycles | 12 |

The N14 union histogram equals the candidate's complete histogram. The T44
low histogram is 8:60, 12:426, 13:224, 14:652, 15:988, 16:1632, 17:2996;
the remaining 304872 masks have width at least 18. All 58 manifest hashes
and sizes match. These files were rehashed after checking and were unchanged.
Supplementary checking in `TEN_COVERED_T63_SPLIT_REVIEW_check.py`, run with
`D:\anaconda\python.exe`, validates all local positive interfaces and the
geometry census, with results in its JSON sidecar. The machine review JSON
binds the candidate, manifest, all declared manifest entries and checker evidence.

The exception domain SHA-256 is
`754c496aa2c853de9f6f21941b268d822bbf9400070e0348496fbab611d50b2c`;
the direct cycle file SHA-256 is
`40993fde32fabaa38ab133eaf19708fb5aa5d2079c6de1c50b7681d40dcabe36`.

## Adversarial checks and limits

Checked degeneracies include c=0, the smallest c>0 (c=2), arbitrary long
artificial/required edges, disjoint positive masks, duplicated transported
descriptions, unordered B omissions, and closing edges. The original
one-common-edge approach cannot be assumed in the 1320 disjoint-mask branch;
all those cases instead have independently checked direct positive cycles.
No failed DFS or failed four-port search is accepted as a nonexistence result.
The review accepts the displayed 1308 four-bridge and 12 six-bridge positive
constructions, without claiming that six bridges are minimal for the latter.
Witnessed optional unions are used only as lower bounds on the true optional
unions; completeness of any local Hamilton search is unnecessary.

Zero open FATAL, CRITICAL, MAJOR or MINOR mathematical issues in this scope.
The full Q5 T63 theorem and full ten-hole/P6 conclusions remain **OPEN**.
