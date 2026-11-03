# Triangle123 closure: symbolic capacity survives at m33

The proposed relation tau13=rho12+sigma23 passes this symbolic capacity gate. The new minimum is49 forms at source3/target3, so it still permits m33 with16 forms of symbolic slack. This is not a constructed controller or an assertion that a numerical assignment exists.

Only the1008 previously saved distinct forms were read. For each coefficient vector, a3 was set to0 and its tau13 coefficient added to both sigma23 and rho12; the tau13 coefficient was then removed and the e coefficient remained modulo3. No three-port word enumeration or field-chart check was repeated. `SUBSTITUTED_FORMS.tsv` saves every resulting form with an inherited witness, while `MERGED_FORM_GROUPS.json` preserves each collision's original vectors, words and input line numbers.

## Actual capacities

| source / target | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 69 | 61 | 55 | 64 |
| 1 | 61 | 57 | 62 | 64 |
| 2 | 55 | 62 | 65 | 63 |
| 3 | 64 | 64 | 63 | 49 |

The symbolic upper bound is m<=49, or **m<=48 when3|m**. The only minimum class is33. The old unconstrained minimum was51, so the closure spends two forms at the bottleneck while imposing a useful quotient/phase alignment. Its actual effect cannot be inferred merely by counting the new triangles.

## Exact triangle and the three CRT lifts

The matching path1->2->3->1 has voltage

```
rho12 + sigma23 - tau13 = 0.
```

Hence every vertex of bases1,2,3 lies on this additional matching triangle, with distinct vertices because the bases differ. The existing B triangles are unchanged, including the deck triangles at base3. At source2/target3, the two-step matching path R21 followed by T13 now has voltage-rho12+tau13=sigma23. Its extension by B± at base3 gives sigma23±e.

The direct S23 edge has voltage sigma23, and the three-step word SSS reaches the same endpoint. Thus the three shifts

```
sigma23, sigma23+e, sigma23-e
```

all occur as three-walk endpoints. At m33, e=11, these are exactly the three CRT lifts above quotient sigma23 modulo11. This proves that this particular direct-edge bucket has enough three-phase route capacity under the relation. It does not certify every quotient bucket or repair the formerly fixed profile3, whose quotient voltages did not satisfy the new relation.

The new relation does not add port words to the topology. It aligns their voltages and therefore creates repetitions as well as the useful bucket coincidence. In particular the sigma23+e forms merge the witnesses(6,5,2) and(4,3,3); the sigma23-e forms merge(6,5,3) and(4,2,2). Both collisions and their reverse analogues are saved in the merged-group JSON.

## New repetition structure

The978 resulting forms comprise951 singleton groups,24 groups of two old forms and3 groups of three. Total loss is24+2*3=30 forms from the old1008. The three triple groups are the zero forms at roots1,2,3: the two orientations of the now closed matching triangle coincide with the already available B³ zero form.

| root | three inherited witnesses that now coincide at zero |
| ---: | --- |
| 1 | (5,4,6), (2,2,2), (6,4,5) |
| 2 | (6,5,4), (2,2,2), (4,5,6) |
| 3 | (4,6,5), (2,2,2), (5,6,4) |

At root3 this triple merging alone changes the minimum51 to49. At roots1 and2, additional repeated ±rho12 forms account for their further capacity losses. Root0's diagonal capacity remains69. The complete27 merged groups cover all such equalities; no numerical residue assignment has been used to infer them.

## Precise simplicity scope

With A3=0, the necessary and sufficient old simple-controller conditions remain

```
0,a0,sigma01 pairwise distinct;
0,a1,rho12 pairwise distinct;
tau02 != 0;
a2 != sigma23;
rho03 != 0.
```

Then set tau13=rho12+sigma23. There is no extra restriction on the resulting tau13: from base1 it is the sole port targeting base3, and from base3 it is the sole port targeting base1. It may even be zero without creating a loop or repeated neighbor, since it exchanges different bases. The remaining conditions still have to be imposed; the closure by itself does not guarantee simplicity. All literal reverse-dart definitions and the fixed F11 inverse-port interface are preserved.

The one symbolic substitution used0.008868824CPU seconds, one worker, within5seconds. PRED, substituted forms, collision witnesses, RESULT and TERMINAL are complete. There were no parameter assignments, controller searches, graphs, BFS, Lean, solver calls, external reviews or automatic follow-up batches. Root decides any numerical test of this changed distribution.
