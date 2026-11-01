# Source-star geometry of all nine-positive choices in the P6 residual census

**Result:** all8020 residual inputs having the proposed nine-positive interface have a **two-blue** choice. Their nine positive four-sets always split into exactly two nonempty actual private-star groups. The groups need not include a six-edge star, and their PL-derived union lower bounds need not reach16. The weakest input-level best bound is10, attained by28 necessary inputs. This is an analysis of complete necessary P keys, not a realization of H or a disproof that actual additional geometry could force a larger union.

`ANALYZE.py` reads all8569 original `CENSUS_NONGATED.jsonl` keys. For each key separately it reconstructs C=01234, all indexed higher traces, all indexed J edges and all singleton traces. It tries all15 blue pairs and20 blue triples and classifies all35 source indices directly. It neither imports the census implementation nor transfers a menu's sample blue labels to other members. As a further check, **every member's whole recovered signature menu equals its own saved menu**. CPU was1.913007 seconds; no new P-domain generation, external-layout search or solver was performed.

## Exact actual-source formulas

For each P vertex v let cv=1(v∈C), hv be its higher-trace occurrence, sv its J degree and dv its degree8/9. The number of its private original edges is

uv=dv−cv−hv−sv.

If v is blue, these uv original edges give uv positive exterior four-sets, all belonging to the same true private star. Let their union be Uv. Every other noninternal edge through v contributes at most three exterior points for a pair trace and5−|T| for a higher trace. Pair coverage of v with all18 exterior points therefore gives the safe integer bound

|Uv|≥ℓv=max(0,18−3sv−Σhigher T∋v(5−|T|)).

These are cardinality bounds, not assumptions that different original edges have independent exterior sets. If uv=0 the necessary PL condition forces ℓv=0. All recorded choices satisfy Σblue uv=9, have no positive sets of other sizes, no negative singleton/pair, t=N3≤3 and t+N4≤20. Every positive four-set index is assigned to its own blue endpoint star.

## All choices and input-level conclusions

There are23876 qualifying blue choices across8020 distinct input keys. **Every qualifying choice is a blue pair**, not just one preferred choice per input. Both endpoint groups are nonempty.

|Private-star edge counts, sorted|Qualifying choices|
|---|---:|
|4+5|20881|
|3+6|2986|
|2+7|9|

The signed negative counts are limited to the following five actual interfaces:

|t|b|Choices|
|---:|---:|---:|
|3|17|1986|
|2|17|1142|
|1|18|3266|
|2|18|8340|
|1|19|9142|

No t=0 choice occurs among this nine-positive class. All8020 have a qualifying two-blue choice.7515 can avoid selecting the nine-degree point;4548 can select it;505 are forced to select it for this particular interface. Thus an argument restricted to two eight-degree centers would miss505 inputs.

Only1185 inputs admit any qualifying choice containing a single star with at least six private edges and ℓv≥16. This includes three inputs where the relevant star has seven edges, so this condition alone does not provide a six-positive theorem caller.

For a separate sufficient six-subfamily test, retain min(uv,6) edges of one star and, if needed, add positive edges from the other star until there are six. Removing uv−6 original four-sets can decrease the union by at most4(uv−6). Therefore

L6=maxblue v max(0,ℓv−4 max(0,uv−6))

is a certified lower bound available for some six-edge positive subfamily. It is only a sufficient bound using the recorded star resources, not an optimization over unknown exterior layouts.1182 inputs achieve L6≥16. In particular the record does **not** support a universal reduction to a six-positive large-union16 subfamily. A subfamily repair also would not automatically hit all nine positives; any such later use must account for the other three constraints.

For each input maximize the total positive-union certificate maxblue ℓv over all its qualifying blue pairs. Its distribution is:

|Best total union lower bound|Inputs|
|---:|---:|
|10|28|
|11|292|
|12|619|
|13|2610|
|14|2282|
|15|1004|
|16|821|
|17|364|

Thus only1185 of8020 have even this full-nine-positive union certificate at least16. The precise two-star `(uv,ℓv,nine?)` histograms are in `SUMMARY.json`:85 profiles over all choices, with input-level best profiles separately recorded. Distinct source selections sharing a numeric profile are not asserted isomorphic.

## A weakest explicit necessary P input

Input id86, zero-based in the original nongated JSONL, is

- inventory(n2,n3,n4)=(6,2,0), nine-degree point0;
- higher traces012 and345;
- J=05 twice,13,15,23,25, with all other pair multiplicities zero.

Its **only** qualifying nine-positive blue pair is03. Both selected vertices belong to one higher triple, and both have J degree two. Vertex0 has five private edges and ℓ0=18−6−2=10; vertex3 has four private edges and ℓ3=10. The signed interface is exactly9P4,2N3,17N4. The nine-degree point is necessarily selected. Both the full-positive and the above six-subfamily certificates are10.

This example proves that the necessary P-side data and the stated PL lower-bound rule cannot be reported as uniformly yielding a six-edge private star or a union16 certificate. It does **not** prove an actual exterior realization with union exactly10, nor that the signed family is unrepairable. Any stronger reduction needs a genuinely additional actual-H argument, for example a joint two-center exterior/pair-cover constraint; it cannot follow from the already recorded scalar PL capacities alone by merely choosing another qualifying blue pair.

## Saved evidence and scope

`ALL_NINE_CHOICES.jsonl` saves all23876 choices, their input ids, the two endpoint groups, uv/ℓv, J degrees, higher exterior capacities, nine-degree flags, t/b and the35 source categories. `INPUT_GEOMETRY.jsonl` saves all8020 complete source keys, number of qualifying choices and a best recorded choice. `SUMMARY.json` contains all distributions and examples; `SUPPLEMENT.json` gives the edge-count/negative-budget tables and the weakest key.

This is structural analysis of a pre-existing complete necessary domain. The549 other nongated inputs have no qualifying nine-positive interface and were not silently included in8020. No census source/output or canonical theorem was modified, no extra repair gate was assumed, and no original-H realizability or global PropertyB conclusion is asserted.
