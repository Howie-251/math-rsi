# q7, r1, c3 head-triangle tower: complete finite result

The complete **28,894,320 normalized HH inputs** for this fixed tower and its stated candidate-preserving normalization are excluded by the necessary quotient BB test followed by the exact original BB test. All **230,496** original inputs surviving the quotient test have a missing BB target; the minimum is **29**. No diameter-5 graph or new lower bound was found. This conclusion concerns this specified normalized construction scope, not arbitrary degree-8 graphs or the whole M2 mechanism.

The run is complete, with no remaining cursor or running worker. Preparation, compilation, one actual sample and production consumed **2.661823 CPU seconds** of the fresh 60-second single-worker budget. The parent-owned independent final verification is complete, adding 1.718837 CPU seconds; the cumulative total including that check is **4.380660 CPU seconds**. No separate full-source preflight check was performed. The single final-graph check verifies the new action's actual edges as well as all distances.

## Actual r1 group and complete graph

Here A=F7²×C3, x=(u,v,w) encoded u+7v+49w. The new K law is

    (b,j)(d,l)=(b+d mod7,j+l mod6),
    (b,j)^(-1)=(-b mod7,-j mod6),
    (b,j)(u,v,w)=(3^j(u+bv),3^j v,w).

G multiplication is (x,k)(y,l)=(x+k(y),kl); its inverse is (-k^-1(x),k^-1). Addition is modulo 7,7,3, including w-negation. K is abelian in this r1 case. The old r5 multiplication, inverse lists and internal indices were not reused. All 6,174 group inverses and 42²×147 action-composition identities were checked while rebuilding the actual tables.

Leaf labels are x+147(b+7j); block labels are 6174+x+147j; head labels are 7056+x. Each leaf joins its seven right Cayley neighbors and its block; each block joins its head. For fixed (u,v), the three heads w=0,1,2 form K3. These rules give 6,174 leaves, 882 blocks and 147 heads: **7,203 vertices, degree 8, 28,812 edges**, including the 147 head-triangle edges. The graph builder checks every degree and the absence of loops or repeated neighbors.

Left G acts transitively on each layer and preserves the head triangles. Actual BFS roots 0,6174,7056 therefore have weights 6174,882,147, and the exact number of unordered pairs at distance greater than 5 is

    (6174*m_leaf + 882*m_block + 147*m_head)/2.

## Scope preservation and actual counts

The normalization proof and parameter change are in [HEAD_TRIANGLE_PARAMETER_EXTENSION.md](../d8_head_triangles/HEAD_TRIANGLE_PARAMETER_EXTENSION.md), with the underlying HH proof in [STRUCTURE_SCOPE.md](../d8_head_triangles/STRUCTURE_SCOPE.md). The two w=1 cross representatives have field vectors (1,0) and (0,1), and each has all 42 K choices. The three w=0 internal generators cover the axis and offaxis colors. The freshly generated r1 lists have involution counts 1/6/42 and noninvolutory inverse-pair counts 20/123/861 for zero/axis/offaxis.

The five branches below cover all 16,380 internal sets, each with 42² cross choices. These are preserved normalized inputs; no claim of nonisomorphic output counting is made.

| Internal allocation | Internal sets | Full normalized inputs | Allowed quotient blocks | Exact original BB tests | Minimum BB missing |
|---|---:|---:|---:|---:|---:|
| axis pair + offaxis involution | 5,166 | 9,112,824 | 588 | 28,812 | 29 |
| offaxis pair + axis involution | 5,166 | 9,112,824 | 1,764 | 86,436 | 36 |
| two axis + one offaxis involutions | 630 | 1,111,320 | 0 | 0 | None |
| one axis + two offaxis involutions | 5,166 | 9,112,824 | 2,352 | 115,248 | 41 |
| axis + offaxis + zero involutions | 252 | 444,528 | 0 | 0 | None |

Every branch has zero original BB passes. The branches with no quotient passes receive no original BB tests; their minimum is undefined (`None` in the table). There were no fully scored BB survivors, so their root minimum statistics are null and their root-zero counts refer to the empty scored population.

We checked all **589,680** new internal-set/cross-exponent keys. Projected Q codes are v+7w+21j; the projected generator set is sorted and deduplicated before matching the 16 allowed sets in [QUOTIENT_BB_ALLOWED.json](../d8_head_triangles/QUOTIENT_BB_ALLOWED.json). The overlapping 24 parameter-pattern records were not used to generate duplicate inputs. Exactly **4,704** keys pass. Each is expanded over all 49 pairs of cross b-coordinates, giving **230,496** original BB checks. The remaining **28,663,824** normalized inputs fail the necessary quotient test. All five counts match the independently regenerated r1 counts in the parameter-extension JSON. No old r5 internal index or lift-key list was used.

The original enumeration order and complete selected-key list are saved in `production.metadata.json`, `production.selected_keys.jsonl` and `production.inputs.txt`. Production starts at filtered cursor 0; the single preflight sample is not an enumeration prefix. Final filtered cursor is 230,496 with no next position.

## Exact BB filter and one calibration sample

For each quotient index j, the six 147-bit original BB masks are

    M_j = H*{x_w : w in W<=3, exponent(w)=j}
          union H*{0,x_s : s in S}
          union H*{0,D_(j-j_s)x_s : s in S}
          union {(0,0,1),(0,0,2)}.

D is the new r1 action with b=0; H acts by u -> u+bv. The final two points incorporate the additional head-triangle routes. The implementation enumerates all words up to length 3 after deleting immediate inverse backtracks, which does not change this endpoint union. Missing BB targets are the sum of 147 minus the six mask sizes. This is an exact original-graph test, not quotient BB sufficiency.

The one actual sample is

    S=[1079,5245,5348,2040,2396,4884,3088].

All **882 BB targets** match the actual block-root BFS individually. The same three complete BFS runs give root missing counts **910/310/414**, representative eccentricities **6/7/6**, BB missing **52**, and **2,976,309** bad unordered pairs. The tables, actual edges and pointwise check are saved in `structure.json`, `preflight.edges`, `preflight.parameters.json`, `preflight.json` and `preflight.check.json`. No old sample or large historical regression suite was rerun.

## Complete result and saved diagnostic graph

Among the 230,496 quotient survivors, BB missing ranges from 29 to 73; exactly 14 normalized inputs attain 29. The five minima are 29,36,undefined,41,undefined. All fail before the three-root scoring stage. The saved terminal histogram contains the complete original BB distribution.

With no BB survivor, exactly one minimum-BB input was expanded and scored as the authorized fallback:

    S=[1079,5245,5495,1896,2207,5004,3107]
    branch=0, new internal_index=2953, cross K codes=[7,37]
    filtered cursor=5098, original scope cursor=5209633
    root missing=[1238,320,444]
    missing by source/target layer L,B,H:
      [1195,37,6]
      [259,29,32]
      [252,192,0]
    bad unordered pairs=3,995,460.

This is `one_minimum_original_BB_fallback_not_a_scored_population_minimum`. It is **not** a bad-pair optimum over this family. The complete graph is saved in `production.best.edges`, with parameters and selection label in `production.best.json`. The layer weights give LL 3,688,965; LB 228,438; LH 37,044; BB 12,789; BH 28,224; HH 0. These are deductions from the saved representative-root counts, not additional graph searches.

## Runtime and evidence

`prepare.terminal.json` records 2.001999 CPU seconds for table/list reconstruction, all quotient keys, compilation and preflight; compilation accounts for 1.405518 seconds. The production driver adds 0.659817 seconds, with 2.661823 cumulative seconds (driver snapshots differ by a few microseconds). Production's own clock is 0.657498 seconds. The first 10,000 original BB checks completed in 0.026745 seconds. One worker, no restarts and no budget extension were used. The terminal's fine-grained BFS bucket records zero although the authorized fallback was actually expanded and scored; use the outer process/driver CPU for the aggregate cost, which includes that work.

Files `production.terminal.json`, `production.summary.json`, `production.first_stage.json`, `production.log` and `terminal.json` contain the actual counts, terminal state and budget. The independently completed mathematical scope computation is separate from this implementation budget. No new parameter or further search was started.

## Independent final verification

The independent checker reconstructed the r1 direct-product K law and scalar-shear action without the producer's arithmetic tables. All **28,812 edges agree exactly**, including all 147 head-triangle edges. A single generic all-source BFS checked **7,203 roots**, finding a simple connected 8-regular graph with **diameter 6** and **3,995,460** bad unordered pairs, all at distance 6. The full distance histogram agrees with the weighted three representative-root histograms.

The results are in `production.best.independent_check.json` and `best.independent_verify.json`; the independent reconstruction program is `independent_best_check.py`. Its actual CPU cost was 0.09732343 seconds for Python plus 1.621514 seconds for the generic checker, totaling **1.71883743 seconds**. Combined with production/preparation, the completed task used **4.38066043 CPU seconds**. There was no repeated preflight, second full-source check or further search. The saved graph remains a minimum-BB fallback and fails the requested diameter-5 target.
