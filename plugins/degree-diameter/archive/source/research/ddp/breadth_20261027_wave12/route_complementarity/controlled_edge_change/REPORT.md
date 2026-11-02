# Frozen P2 prediction: one prescribed edge-direction change

Status: complete route-linear analysis; predictions saved before the controlled graph is generated or measured by root. This task generated no expanded graph, computed no whole-graph score, and ran no BFS or solver. It analyzed exactly the 15 nonzero branch directions on the one prescribed edge, without SLS or an extension of the edge set.

## Controlled variable and selection rule

The source is cached global-label passer68 in wave11/binary72_tight_words/best_parameters.json. Its fixed 72-point controller, all 144 edge matrices, all zero offsets, and the branch vector on every edge except 0<->18 are retained. Source labels are A=0,B=1,C=2,D=3, with inverse labels [3,2,1,0].

The problematic target slot is base0->10. Its two routes are AACA, path0-18-37-64-10, and DCC, path0-54-29-10. The first edge of AACA not shared by DCC is 0<->18. Its forward matrix has columns [2,4,8,1], its inverse columns [8,1,2,4], and its original forward/reverse branch vectors are1/8.

For each b=1..15, change only the forward branch vector of this edge to b, and the reverse vector to T^-1*b. First require AACA rank4; among those directions choose the smallest number of damaged original unique4 ordered controller slots; break ties by the smallest integer b. This rule was fixed before the 15 diagnostics.

## Selection and frozen predictions

Selected b=3, inverse-consistent reverse_b=9. The target route columns change as follows:

    AACA: [14,9,7,1], rank3 -> [10,9,7,1], rank4.

DCC is unchanged (its path does not use the modified edge). A rank4 AACA route supplies every one of the 16 output fiber coordinates from every fixed input fiber coordinate. Therefore all256 ordered fiber pairs from base0 to base10 are predicted to have distance at most4.

Exactly two of the468 cached unique4 ordered slots lose rank. They are reverse slots of one unordered controller pair:

| source->target | unique word/path | columns before | columns after | rank | missing per input | missing ordered fiber pairs |
|---|---|---|---|---|---:|---:|
| 37->63 | DDCC / 37-18-0-36-63 | [7,2,15,11] | [7,4,15,11] | 4->3 | 8 | 128 |
| 63->37 | BBAA / 63-36-0-18-37 | [10,12,2,1] | [10,12,6,1] | 4->3 | 8 | 128 |

For a unique4 slot there is exactly one controller walk of length at most4. Its endpoint set is an affine subspace of size2^rank, so it leaves exactly16-2^rank targets for every input coordinate, irrespective of that affine translate. Thus the predicted256 ordered missing tight fiber pairs represent128 unordered graph pairs between fibers37 and63. These were not bad in the cached source because its468 unique4 slots all had rank4. These numbers are exact local predictions, not a whole-graph bad-pair score.

## All fifteen diagnostics

| forward b | reverse b | AACA rank | damaged ordered unique4 slots |
|---:|---:|---:|---:|
| 1 | 8 | 3 | 0 |
| 2 | 1 | 4 | 12 |
| 3 | 9 | 4 | 2 |
| 4 | 2 | 3 | 8 |
| 5 | 10 | 3 | 6 |
| 6 | 3 | 4 | 10 |
| 7 | 11 | 4 | 4 |
| 8 | 4 | 3 | 8 |
| 9 | 12 | 3 | 6 |
| 10 | 5 | 4 | 6 |
| 11 | 13 | 4 | 8 |
| 12 | 6 | 3 | 10 |
| 13 | 14 | 3 | 4 |
| 14 | 7 | 4 | 12 |
| 15 | 15 | 4 | 2 |

Eight choices repair AACA to rank4. Every one damages at least two original tight ordered slots; b3 and b15 attain the minimum2, so the integer tie break selects b3. Every nonrepairing direction leaves both target routes of rank3. Since offsets remain zero, at input fiber coordinate0 both route images contain0 and their union cannot be all16 points. Accordingly none of these15 one-edge b-only choices can satisfy whole-graph D4. This does not exclude changes on a different edge, coupled edge changes, matrix changes, nonzero offsets in a modified model, or the existing general edge-local construction family.

## Computation and next test

Columns are updated at each directed route step as old_columns -> T*old_columns followed by appending the local branch vector. The changed reverse edge always uses the actual inverse matrix times b. Gaussian elimination uses F2 XOR arithmetic on four-bit vectors. Cached controller slot paths are traversed directly; no graph walks are newly enumerated and no full graph is built. All468 baseline ranks were checked to equal4 before comparing the15 choices.

`analysis.json` contains all15 diagnostics, their468-slot rank arrays, complete damage records, original and modified target columns, the tie-breaking rule, and the frozen target/damage predictions. `analyze.py` reproduces only this prescribed finite linear calculation. Native Python CPU was 0.031998 seconds, under a hard1-CPU-second process limit. There were zero graph generations, BFS calls, solver calls, new seeds, or new lower bounds.

Root's controlled_test.py will generate and measure only the selected b3 graph. It will compare target0->10 coverage and the exact37<->63 tight-slot damage against these predictions. No claim about its actual diameter or whole-graph bad-pair count is made here before that measurement. The test asks whether the selected change repairs the target while transferring a deficit to the two predicted tight slots. Any later construction retaining this change would have to address those slots explicitly.
