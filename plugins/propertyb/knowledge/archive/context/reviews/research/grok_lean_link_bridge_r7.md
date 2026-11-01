Scoped no issue found in the actual derivation of these conditional bridges. Source reading only; nothing was executed, and this pass does not claim a build.

The chain that is discharged is per position, and the subtraction sits inside the minimum:

\[\sum_k \min(A_k,\min(B_k,C_k-D_k))<1.\]

`Numeric.positionBound` is that minimum, with \(D_k=\) `Numeric.deduction`. `ProfileApplication.propertyB_of_corrected_profile` sends `totalBound p < 1` to `ConditionalUnion.propertyB_of_weighted_position_bounds` as exactly that sum. `totalBound_eq_sum_of_eq` is the rewriting step.

## What each layer hands off

`LinkCounting.link_bad_pair_lower_bound` is P8 on the hypergraph. Pair covering gives \(\sum_{y\neq x}(\lambda_{xy}-1)=4d(x)-(v-1)\) with every codegree at least 1, so the natural subtraction does not truncate. That excess is at most the sum of \(|(e\setminus\{x\})\cap(f\setminus\{x\})|\) over incident pairs, each bad pair contributes at most 3, and empty-intersection pairs contribute 0. Hence

\[q(x)\ge\bigl(4d(x)-(v-1)+2\bigr)/3,\]

the integer form of \(\lceil(4d-(v-1))/3\rceil\). The count is a count of unordered bad pairs.

`LinkDeletion` turns that count into a deletion set. `directedBadPairs` is the disjoint union of the two `offDiag` directions of each unordered bad pair, so the directed sum equals the sum of forward-plus-reverse weights, and the cardinality is twice the unordered count. The multiplier in `uniform_bad_weight_lower` is the unordered \(q\), applied to a constant that already adds both directions. A one-sided or zero direction stays inside that sum. `directed_bad_intersection` puts both the locked vertex and another common vertex in \(e\cap f\), so the intersection size is not 1, and `critical_ratio_zero_of_intersection` gives those ordered pairs probability 0. `pair_sum_le_weighted_deletion` then removes their bookkeeping weights once each from the ordered-pair upper bound. The deleted set is a `Finset`, so one ordered pair is not removed twice at the same position.

`exceptional_weight_lower` allows `cap` unordered slots to miss the constant \(c\), using nonnegativity on the whole family. `exceptional_pair_capacity` is \(\binom{|S|}{2}\le 1\) whenever \(|S|\le 2\). `two_exceptional_edges_weight_lower` charges that one unordered slot, including when the slot is bad and has weight 0.

`LinkWeightCertificates` moves a finite type inequality onto realized edges. `shared_type_count_ge_two` is the guard that a repeated lock list has count at least 2; `pairWeight` ignores the dummy count 0 in `typeWeight`. For the seven uniform centers the checked constant is a lower bound on every incident forward-plus-reverse weight, and `deduction ≤ q·c` is the comparison with `Numeric.deduction`. The concrete inputs match P8 and the profile tables:

| Theorem | \(d\) | unordered \(q\) | constant |
|---|---:|---:|---:|
| `v21_d7_deduction_11` | 7 | 3 | \(42/4199\) |
| `v22_67_deduction_12`, both `v22_77` centers | 7 | 3 | \(3/323\) |
| `v23_66_deduction_11` | 6 | 1 | \(11/1292\) |
| `v23_66_deduction_12` | 6 | 1 | \(22/2261\) |
| `v23_677_deduction_12` | 7 | 2 | \(3/323\) |

`v23_677_deduction_13` is the same shape with one exceptional slot. The realized fibers of `[11,13]` and `[12,13]` each have size 1, so their union \(S\) has size at most 2 and \(S\) contains every edge of either type. Any incident pair with an edge outside \(S\) is outside the exception list, so its two-direction weight is at least \(3/323\). At most one unordered pair sits inside \(S\). With \(q\ge 2\),

\[\mathrm{deduction}(v23\_677,13)\le(2-1)\cdot(3/323)\le\sum\mathrm{typeWeight}.\]

Hand calculation of `pairWeight` at position 13 agrees with that split: \(\{z,z\}\) sums to \(42/4199\), each \(\{z,xz\}\) and \(\{z,yz\}\) sums to \(3/323\), and \(\{xz,yz\}\) is 0 in both directions because both extra locks lie before 13. At position 12, \(\{xy,yz\}\) has one direction \(6/323\) and the other 0, so the uniform \(3/323\) still applies. The kernel `decide` steps were not re-run.

`ProfileDeletion.correctionDeleted` at a correction position is exactly `directedBadPairs` of the unique lock at that position, and it is empty elsewhere, where `deduction` is 0. The same geometric pair may be deleted at two positions, because each position has its own \(C_k\), \(D_k\), and weights. `all_position_deletion_lower` is the hypothesis `propertyB_of_weighted_position_bounds` names `deletion_lower`.

`boundC` is the sum of `pairWeight` over every ordered pair in `edges.offDiag`. The deletion removes weights that this sum still contains. Endpoint sums are equal to `boundA` and `boundB`. Weights are nonnegative because each is an upper bound of a nonnegative probability, which is what `weighted_deletion_bound` uses.

## Attacks that do not produce a counterexample

Direction multiplicity, duplicate deletion inside one position, a zero-weight exceptional pair, integer rounding of \(q\), and codegree truncation are the quantities proved above. `Numeric.deduction` enters only as a rational already computed from the profile; each certificate shows that same rational is at most the sum of the actual deleted direction weights. For position 13 that rational is the one cheap slot \(3/323\), the same number `v23_677_link_13` records, obtained by discarding one unordered slot rather than by multiplying a directed count.

No failing obligation remains inside these conditional statements. Each concrete center theorem still takes pair covering, a `RealizesProfile`, the stated degree, and the locked index as inputs. `propertyB_of_corrected_profile` still takes the center inequalities and `totalBound p < 1` as inputs. Those are the stated hypotheses of the local bridges.
