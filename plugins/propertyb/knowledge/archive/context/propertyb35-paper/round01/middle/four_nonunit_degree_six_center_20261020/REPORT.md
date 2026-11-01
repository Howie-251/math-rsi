# A bounded degree-four gate at the unique six-degree center

The requested local gate succeeds. Its complete marked trace domain leaves five necessary inputs after the one-red anchor bound and the stated local constraints. Every one of those five has a strict zero-quota certificate from the existing sixteen-layout menu. No new layout search, LP, whole-H search or Lean run was used.

## Precise local statement

Let H be a simple five-uniform hypergraph on 21 vertices with 35 edges, and let x be its unique vertex of degree six. Let F be an actual edge through x. Assume:

1. Every other vertex of F has degree at least seven, at most three vertices of F have degree seven, and the sum over v in F of max(d(v)-9,0) is at most four.
2. Every point pair inside F has codegree at most four.
3. The six edges through x cover every other vertex of H.
4. Exactly four other edges G have intersection size with F different from one.

Then H has Property B. These hypotheses are consequences of the specified non-B A3 branch as supplied by the parent; this report proves the local implication and does not independently certify those upstream imports.

The conclusion only concerns F through the unique six-degree point. No statement about arbitrary degree-four vertices of the nonunit graph is claimed.

## Actual trace and degree interface

Number F by 0,1,2,3,4, with x=0. The four distinct exceptional original edges have traces T1,...,T4 in F. Each trace has size 0,2,3 or 4; repeated traces are allowed. Every other edge except F has a singleton trace. Thus, if a_v counts singleton traces at v and h_v counts exceptional traces containing v,

    sum a_v = 30,          d_H(v) = 1+a_v+h_v,
    a_0 = 5-h_0.

Pair codegree at most four gives, for each pair i,j in F,

    #{t : i,j in T_t} <= 3,

because F itself is one additional edge through the pair.

The six x edges have 24 incidences with the other twenty vertices, and all twenty must occur. Their total repetition excess is therefore four. On the four other points of F, the initial edge F already contributes one incidence each. Every exceptional trace containing x contributes |T|-1 further incidences, so necessarily

    sum_{T contains x} (|T|-1) <= 4.

The remaining stated degree restrictions give d(v)>=7 for v!=0, at most three degree-seven values, and total excess above nine at most four. In particular d(v)<=13.

## Complete anchor calculation

Choose v in F red, the other four F points blue, and choose r of the sixteen exterior vertices red. Let C(n,k)=0 outside the valid range. The sample count and singleton-event bounds are

    D=C(16,r), R=C(12,r-4), B=C(12,r), J=C(8,r-8),
    a_v R + (30-a_v) B - max(a_v-1,0) J.

The subtraction is the ordinary red-event tree bound: two red singleton edges require at most eight exterior points jointly red, giving an intersection of size at least J. A tree induced by the active red events has at most one fewer edges than vertices, so the pointwise union bound remains valid. It does not assume independent bad events.

The exceptional contribution for a trace T is zero when v belongs to T; the trace then already contains both colors. When T is empty it is C(11,r-5)+C(11,r). Otherwise, when v is outside T, it is C(11+|T|,r). Adding the four contributions gives U(v,a_v,r). Any U<D supplies an actual proper coloring of all 35 original edges.

For each of the C(8,4)=70 multisets of four residual types P,0,2,3,4, `VERIFY.py` evaluates every a=0,...,30 and every r=0,...,16 as integers. It retains the full failure set; it never treats a first threshold failure as a monotone failure tail.

There are C(29,4)=23,751 labeled trace multisets on F. The permitted symmetry is S4 on the other four F points, fixing x. It has exactly 1,563 trace orbits. Each representative's actual S4 image is reconstructed, disjointness is checked, and their union is verified equal to the full labeled domain.

The orbit outcomes are: 162 violate the pair restriction; 576 violate x-star coverage; 645 have a strict x-anchor bound; 175 more have no attachment composition compatible with the remaining strict-anchor failure sets and degree restrictions. Only five orbits retain an attachment composition, exactly one each. Enumerating singleton counts uses all failed values with 7<=1+a_v+h_v<=13 for v!=0, the exact sum thirty, and the exact degree restrictions. This is complete over a necessary domain and makes no claim that every retained input is globally realizable.

`INDEPENDENT_VERIFY.py` performs a separate pass over all 23,751 labeled inputs, using incidence-count signatures and complementary-binomial arithmetic. It imports no primary orbit or threshold routine. It obtains exactly forty labeled trace/attachment inputs in five joint marked orbits, the same five listed below; it also checks all seventy complete threshold failure sets against the primary output.

## The five fixed certificates

The complete remaining inventory is:

|Exceptional trace masks|Singleton counts a0,...,a4|Original F degrees|Fixed positions of labels 0,...,4|Exact upper bound|
|---|---|---|---|---|
|0,0,3,30|4,8,6,6,6|6,11,8,8,8|4,3,12,2,1|36739/40040|
|0,0,6,26|5,8,5,6,6|6,11,7,8,8|4,3,12,2,1|3383/3640|
|0,0,7,30|4,8,8,5,5|6,11,11,7,7|11,3,2,12,1|38477/40040|
|0,6,25,30|4,6,6,7,7|6,9,9,10,10|4,3,12,2,1|233003/240240|
|0,7,26,30|4,8,6,6,6|6,12,9,9,9|4,12,3,2,1|213/220|

For each row the exact five-lock trace multiplicities are reconstructed as one mask-31 edge F, the four listed exceptional masks with their repetitions, and a_v copies of singleton mask 2^v. Their sum is thirty-five and the five actual degrees are checked.

The certificate uses the established conditional permutation A/B/C bound, as stated and proved in Section 4 of `proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md`. The five locked vertices are F itself; x is already lock 0. There is no sixth lock or promotion. Every pair quota is zero. The only tested layouts are the same pre-existing sixteen profiles used by the q3 bounded pilot: six central profiles on positions 9,...,14 with one position omitted, and the five existing exact end profiles and their reflections. The displayed profile is an existing member of that fixed menu.

For a fixed layout the exact bound is the sum, over the 21 pivot positions k, of min(A_k,B_k,C_k). The A/B terms count eligible one-edge events, and C counts eligible ordered distinct original-edge pairs using their trace compatibility. Each reconstructed inventory is separately expanded to thirty-five distinct edge indices, and all 1,190 ordered distinct pairs are processed by `computations/independent_structure_bounds.py`, whose falling-factorial injection arithmetic is different from the primary binomial engine. Each of the 105 row minima, and each total, matches exactly. The largest total is 233003/240240<1. The established conditional permutation lemma therefore yields an actual proper coloring of H in each remaining case.

The orbit action fixes x. Moving other labels transports the certificate positions together with their actual vertices, so the forty labeled residual inputs are covered by these five representatives.

## Actual execution and limits

The three completed runs used approximately 0.229, 0.0265 and 0.139 CPU seconds respectively, well below the authorized twenty CPU seconds. Their actual outputs are `RESULT.json`, `FIVE_LOCK_FULL5.json` and `INDEPENDENT_RESULT.json`. The five-lock file contains every tested layout, the selected exact certificate, all thirty-five original trace indices and every independently replayed A/B/C row.

Reproduction:

```sh
python3 context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/VERIFY.py
python3 context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py
python3 context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py
```

This is a complete finite local gate with deterministic arithmetic checks. Its mathematical imports are the conditional permutation-to-coloring lemma and the parent-supplied non-B A3 restrictions. It is not a Lean result, an external-model review, or a claim that the full m(5)>=36 problem is solved. The parent retains responsibility for verifying the actual A3 caller and any integration with the remaining degree-profile branches.
