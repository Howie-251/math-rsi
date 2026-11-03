# HS58: joint a=6,7,8 encoding check

Date: 2026-10-12. This is a read-only candidate-preservation review
of `computations/dd82/construction/hs58_two_delete_all_remaining.py`
and the three actual `encoding.json` / DIMACS headers under
`hs58_two_delete_all_remaining_run/`. No solver, CNF regeneration,
or certificate checker was run for this review.

No candidate-preservation gap was found. For each fixed deletion
representative, the primary variables comprise all 1050 original
nonedge additions, all 400 old-new edges, and all 28 auxiliary edges.
There is no fixed-H catalog, port saturation, matching, spectral
restriction, or old-vertex normalization in this source.

Let a be the selected addition count, b the attachment count, and
h the H-edge count. Summing the fifty exact old-degree constraints
gives 2(175-2+a)+b=400, hence b=54-2a. Summing the eight exact
new-degree constraints gives b+2h=64. Therefore h=a+5 for every
satisfying assignment, without an additional addition counter.
The source's `hcount[10]` asserts h>=11 and `-hcount[13]` asserts
h<14; these are exact unary thresholds and therefore select precisely
a in {6,7,8}. No endpoint or attachment degree is only an upper bound.

The auxiliary-degree sorting clauses are
`degree(a+1)>=k -> degree(a)>=k` for all consecutive labels and
k=1,...,7. These express nonincreasing H degrees. Any H admits such
an ordering by relabeling the eight new vertices independently of
the old ones. All attachment columns remain free, so this restriction
preserves every candidate in the stated range, including tied degrees.

The edge accessor fixes exactly Q-D, sets deleted edges and self
edges false, and otherwise returns the appropriate free variable.
The coverage loop considers all 1653 unordered vertex pairs. A pair
is skipped only if Q-D alone already covers it. Every other pair's
clause contains its direct edge and every two-edge route through all
58 intermediates, using complete AND equivalences. Thus addition-
addition, addition-attachment, attachment-attachment, attachment-H,
and H-H routes are all represented wherever their endpoint types
permit them. Deduplicating a Boolean OR's terms is harmless. The
same generic exact-cardinality / conjunction helpers already checked
in `HS58_A5_REMAINING_JOINT_ENCODING_REVIEW.md` are reused; no graph
constraints from their historical module are instantiated.

| Geometry | Fixed D | Variables | Clauses | Fixed-covered pairs | Remaining old-old / old-new / new-new |
| --- | --- | ---: | ---: | ---: | --- |
| Adjacent | {01,04} | 33205 | 101997 | 1200 | 25 / 400 / 28 |
| Cross | {01,23} | 33249 | 102131 | 1199 | 26 / 400 / 28 |
| No cross | {01,10-11} | 33249 | 102131 | 1199 | 26 / 400 / 28 |

All three actual headers agree with the saved metadata. Each instance
has 1478 primary graph variables. The complete saved deletion orbits
normalize arbitrary D in the respective geometries, independently
of a and independently of the subsequent H-degree ordering.

This establishes the theory-to-CNF connection for the entire a=6,7,8
range of the fixed HS edit family. To conclude an exclusion for all
addition counts additionally requires the separate lower-count
exclusions, the upper bound a<=8, and successful checked-UNSAT
outcomes for these three actual inputs. This review itself reports
neither solver outcomes nor a new exclusion, and it does not rely
on the narrower saturated-disjoint theorem.
