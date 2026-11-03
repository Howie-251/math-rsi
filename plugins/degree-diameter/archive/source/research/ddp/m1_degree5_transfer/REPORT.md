# Exact degree-five pruning of the saved702- and720-vertex lifts

Date:2026-10-26. Scope: exactly eight specified subgraphs, no random search. The startup public comparison is `(5,5)=650`, but **none of these candidates satisfies diameter≤5**, so no new lower bound or current-record claim is made and no new record lookup was triggered.

## Construction and evidence

For each saved degree-seven two-fiber lift, the internal voltage sets `A,B` each consist of two inverse pairs, and the cross set `S` has three elements. Keep exactly one original inverse pair in each fiber and keep all of `S`, producing four subgraphs per source. The group rule and original labels are preserved; the resulting graphs have exactly five distinct neighbors at every vertex.

Sources:

- `computations/ddp/m1/d7_profile/D7_Meta_13_27_3.json/.edges`, group `(a,b)(c,d)=(a+3^b c mod13,b+d mod27)`, group order351 and graph order702.
- `computations/ddp/m1/d7_profile/D7_Meta_15_24_2.json/.edges`, group `(a,b)(c,d)=(a+2^b c mod15,b+d mod24)`, group order360 and graph order720.

The independent script `check_prunings.py` reconstructed each entire degree-seven source edge list from its formulas and checked exact equality before pruning. Each pruned edge set was checked to be a subset of that source, simple, and5-regular. It then ran Python BFS from the two fiber-identity roots. The existing C++ verifier independently rebuilt adjacency from each exported edge list and ran BFS from **every vertex**. The full ordered distance histograms and missing-pair counts agree exactly with the predictions from the two roots and the proved left regular group action. All eight C++ runs returned1 because the diameter requirement failed, not because of an execution error.

## Exact results

`a0,a1` and `b0,b1` are the lexicographically ordered inverse pairs from the source, explicitly listed below. Root-missing means the number of targets at distance greater than5 from the two fiber identity roots.

|Saved candidate|A retained|B retained|Diameter|Root-missing pair|Bad unordered pairs|
|---|---|---|---:|---|---:|
|n702_a0_b0|97,335|61,236|6|87,81|29484|
|n702_a0_b1|97,335|152,307|6|27,27|9477|
|n702_a1_b0|170,235|61,236|6|39,43|14391|
|n702_a1_b1|170,235|152,307|6|53,53|18603|
|n720_a0_b0|2,22|131,133|7|79,75|27720|
|n720_a0_b1|2,22|145,311|6|57,55|20160|
|n720_a1_b0|81,159|131,133|7|73,83|28080|
|n720_a1_b1|81,159|145,311|6|38,63|18180|

The cross voltages remain `[0,265,180]` for702 and `[0,30,41]` for720. Every graph is connected. All702-point outputs have1755 edges; all720-point outputs have1800 edges.

Distance spectra below list counts at distances `0,1,...` for the two representative roots; complete all-source spectra are in each JSON record.

|Candidate|Root0 spectrum|Other fiber identity spectrum|
|---|---|---|
|n702_a0_b0|1,5,20,78,222,289,87|1,5,20,76,222,297,81|
|n702_a0_b1|1,5,20,80,274,295,27|1,5,20,80,264,305,27|
|n702_a1_b0|1,5,20,78,239,320,39|1,5,20,76,227,330,43|
|n702_a1_b1|1,5,20,80,239,304,53|1,5,20,80,237,306,53|
|n720_a0_b0|1,5,20,74,205,336,78,1|1,5,20,70,209,340,74,1|
|n720_a0_b1|1,5,20,80,246,311,57|1,5,20,80,244,315,55|
|n720_a1_b0|1,5,20,74,213,334,72,1|1,5,20,70,206,335,82,1|
|n720_a1_b1|1,5,20,80,257,319,38|1,5,20,80,236,315,63|

The best of these eight by number of bad pairs is702_a0_b1, but its9477 unordered distance-six pairs still invalidate `(5,5)`. The complete conclusion is only that **these eight direct pruning choices do not transfer the saved lifts into new `(5,5)` graphs**. This does not exclude different voltages, different subgraphs, or the broader two-fiber mechanism. No parameter cascade or subsequent optimization was started.

## Artifacts and recomputation

Each `n*_a*_b*.edges` is an explicit full edge list with an `n m` header. Its matching JSON contains the retained parameters, both representative distance spectra, the independent all-source check, and the exact source link. `results.json` collects the eight records.

From the project root:

```
python3 research/ddp/m1_degree5_transfer/check_prunings.py
```
