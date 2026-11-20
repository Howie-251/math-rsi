# Q7 closure: portable E38 structural replay

This archive preserves the small, runnable final structural calculation from the
supplied **Ruskey–Savage conjecture n=7** package. A fresh local run on 2026-11-20
compiled both original C++ implementations and consumed their actual outputs.
It verified the E38 structural core. It did **not** replay the historical E36 and
earlier dependencies needed for the full R7 result.

The project records its full result as **sound-modulo-imports / same-family /
provisional**. This replay is deterministic evidence for the finite E38
calculation, not an external review or a formal proof of the full theorem.

## Run

Requires Python 3.10 or newer, a C++17 compiler (`c++`, or set `CXX`), and a
little-endian host for the original RAW binary format. From this directory:

```sh
python3 replay.py --output /tmp/q7-e38-replay
```

Choose a new empty output directory outside this archive. The runner compiles
with assertions enabled, regenerates all data, invokes the original consumer's
geometric part, and compares every regenerated entity with the frozen output.
It writes `REPLAY_RESULT.json` in the output directory. Frozen inputs are read-only
from the runner's perspective; no packaged executable or model service is used.

## Actual result

| Minor-side size r | Raw single faces | Ordered independent cross-face pairs | Minimum maxᵢ\|δᵢ\| | Pairs with maxᵢ\|δᵢ\| ≤ 7 |
| --- | ---: | ---: | ---: | ---: |
| 6 | 21,760 | 14,875,520 | 9 | 0 |
| 7 | 8,320 | 2,437,120 | 11 | 0 |
| 8 | 2,880 | 414,720 | 11 | 0 |
| 9 | 2,400 | 509,760 | 11 | 0 |
| Total | 35,360 | 18,237,120 | 9 | 0 |

The author implementation partitions the 35,360 faces into 9/3/1/2 symmetry
orbits and checks 6,173/868/144/423 representative-first compatible pairs:
7,608 in total. The independent implementation enumerates the full raw face
sets and cross-independent pairs without using those orbits. The original
consumer compares complete face sets after converting the author's 32-bit
color-index masks to physical 64-bit masks, reconstructs every one of the 7,608
actual Q7 hole sets and all seven signed δ coordinates, and checks all
orbit-weighted histograms against the raw counts.

Every regenerated JSON/JSONL entity matched the supplied frozen outputs. All
four RAW binaries matched byte for byte. Windows CRLF versus local LF explains
the text-byte differences; comparisons use parsed JSON entities. The saved run
and its actual compiler/system/command information are in
[verification/REPLAY_RESULT.json](verification/REPLAY_RESULT.json).

## How this final calculation connects to R7

The mathematical source first proves, for an inclusion-maximal 45-edge short
matching of Q7, that every direction has at most seven prescribed edges. Some
direction must attain seven, giving two Q6 faces with 19 holes each. The four
minor-side sizes above exhaust the possible local hole parameters. The finite
calculation shows that no independent pair of those faces can satisfy all seven
necessary bounds |δᵢ| ≤ 7. This excludes maximal 45-edge matchings.

The sparse bridge preserves the original matching: add actual edges between
free adjacent vertices until an inclusion-maximal extension N is obtained. An
elementary incidence count gives |N| ≥ 45, and E38 raises this to |N| ≥ 46. The
historical E36 theorem together with its denser predecessors must then supply a
Hamilton cycle containing **all** edges of N, hence all edges of the original
M. One cannot replace this import by a theorem preserving only a 46-edge
subset of a larger N, or flip edges of M and infer preservation afterward.

## Historical dependencies remain separate

The supplied archive identifies itself as a lite package: source programs,
proof texts and the E38 core are retained, but some older certificates and
intermediate payloads are intentionally omitted. A direct intersection of
E36's 1,182-item author binding with the omission manifest identifies **439
explicitly omitted items**, with 15,792,946 original logical bytes. Examples and
the exact static-check scope are recorded in
[verification/DEPENDENCIES.json](verification/DEPENDENCIES.json).

No old-layer certificate, local-rank table, R6/P6 theorem, universal matching
connectivity rank bound, or E18–E36 finite responsibility is marked revalidated
by this replay. Reconstructing omitted payloads and consuming all corresponding
proof interfaces is a separate task. P7 with prescribed endpoints, long-edge
matchings, and dimensions n ≥ 8 are outside the claimed R7 result.

## Files and provenance

`source/high/FACE19_EXHAUSTIVE.cpp`,
`source/mid/INDEPENDENT_RAW_FACES.cpp`, and
`source/mid/INDEPENDENT_CONSUMER.py` retain the original program bytes from
`evidence/E_new_problem/research/seven_directions/e38_2026_11_19/` in the supplied
archive. `expected/` retains the corresponding original author outputs and
independent RAW/result files. Neither executables nor private histories,
runtime distributions, host credentials, or original machine path bindings
are included.

The original consumer remains intact. Its second part reads E36 bindings and
payloads. The portable runner explicitly executes only the geometric prefix
before `bindings=`, following the source package's own lite-core entry point;
the result JSON records that scope. This boundary is not a substitute for
successful execution of the omitted second part.
