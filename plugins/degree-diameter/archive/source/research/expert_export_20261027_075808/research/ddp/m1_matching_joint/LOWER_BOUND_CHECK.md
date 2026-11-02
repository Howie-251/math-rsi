# Independent check of the matching augmentation lower bound

## Mathematical verdict

The proposed joint score is a valid lower bound on the actual number of bad unordered pairs in the six-matching augmentation. A positive score proves that the candidate fails diameter 5. A score of zero is only a necessary condition and must not be accepted as a successful graph.

Let `G` be the verified diameter-5 source, `M={(a_i,b_i):1≤i≤6}` an oriented matching, `H=G−M`, `A={a_i}`, and `B={b_i}`. Let `F` be the extension by new adjacent vertices `u,v`, with `u` adjacent to all of `A` and `v` to all of `B`. Write `a_G(x)=d_G(x,A)`, `b_G(x)=d_G(x,B)`, and define `a_H,b_H` analogously, allowing infinity in `H`.

For an old edge `e`, let `C_e` consist of **unordered** pairs `{x,y}` with `d_G(x,y)=5` for which every shortest `G`-path uses `e`. Form the set union `C=union(e in M) C_e`; pairs belonging to several `C_e` must be counted only once.

Define

```
K_G(x,y) = min(a_G(x)+a_G(y)+2,
               b_G(x)+b_G(y)+2,
               a_G(x)+b_G(y)+3,
               b_G(x)+a_G(y)+3).
```

The claimed score is

```
L_old = #{ {x,y} in C : K_G(x,y)>5 },
L_u   = #{ old x : a_G(x)>4 and b_G(x)>3 },
L_v   = #{ old x : b_G(x)>4 and a_G(x)>3 },
L     = L_old + L_u + L_v.
```

Thus the four possible repair inequalities are exactly the proposed thresholds 3,3,2,2 on the endpoint-distance sums.

## Proof

1. If `{x,y}` belongs to `C_e` and `e` is deleted, `H` has no path of length at most 5 between them. Any such path would also be a path of length at most 5 in `G`; because `d_G(x,y)=5`, it would be a shortest path avoiding the compulsory edge `e`, a contradiction. Hence every pair in `C` has `d_H(x,y)>5`.

2. Deleting edges cannot shorten endpoint distances: `a_G≤a_H` and `b_G≤b_H`. Therefore `K_G≤K_H` pointwise, including infinite distances.

3. The exact old–old distance in `F` is `min(d_H(x,y),K_H(x,y))`. A shortest path either avoids both new vertices, uses exactly one, or uses both. In the last case their connecting subpath can be replaced by the edge `uv`; these possibilities give the five terms. Conversely every finite term describes a walk. Thus for a pair in `C` with `K_G>5`, both `d_H` and `K_H` exceed 5, so the pair is actually bad in `F`.

4. The exact new-root distances are `d_F(u,x)=min(a_H(x)+1,b_H(x)+2)` and the analogous expression for `v`. If both corresponding `G` distances exceed the threshold, the `H` distances also do, proving every pair counted by `L_u` or `L_v` is bad.

5. The three collections consist respectively of old–old pairs, pairs containing `u`, and pairs containing `v`, so they are disjoint. The new pair `{u,v}` is an edge and is not counted. Summing their sizes yields the stated lower bound without multiplicity.

## What the score omits

There are two mechanisms that can make the original distance-5-only bound strict:

1. A pair originally at distance less than 5 can move beyond distance 5 after the matching is deleted, and remain unrepaired. Such a pair is never in any `C_e`. This already occurs in the saved ten-candidate profile: candidate 02 has a verified bad old pair `(0,1460)`, whose original distance is 4.
2. Several matching edges can collectively meet every original shortest path even though no single matching edge is compulsory. An original distance-5 pair can then be damaged by `M` while lying outside `C`.

The initially suspected third mechanism, failure of an optimistic `G` endpoint repair route after deletion, is **ruled out for this paired augmentation** by the exact shortcut identity proved below. Thus it must not be cited as an actual omission here. The two listed omissions do not create false positives in the lower bound.

## Independent comparison with the ten saved candidates

The script `check_lower_bound_ten.py` used `critical_pairs.txt`, the existing original-graph distance matrix, the ten saved matching parameters, and `m1_matching_augmentation/independent_validation.json`. It performed no graph BFS and generated no candidates. Every lower bound is at most the saved true count, and the new–old part is exact on all ten candidates.

| Candidate | `|C|` | Old–old lower bound | New–old lower bound | Total lower bound | Actual total | Actual old–old pairs omitted |
|---|---:|---:|---:|---:|---:|---:|
| 00 | 420 | 291 | 18 | 309 | 382 | 73 |
| 01 | 413 | 304 | 22 | 326 | 392 | 66 |
| 02 | 389 | 290 | 14 | 304 | 364 | 60 |
| 03 | 540 | 379 | 22 | 401 | 512 | 111 |
| 04 | 522 | 390 | 22 | 412 | 464 | 52 |
| 05 | 467 | 363 | 21 | 384 | 439 | 55 |
| 06 | 425 | 340 | 19 | 359 | 424 | 65 |
| 07 | 454 | 327 | 13 | 340 | 404 | 64 |
| 08 | 390 | 292 | 17 | 309 | 373 | 64 |
| 09 | 452 | 331 | 30 | 361 | 425 | 64 |

Candidates 01, 02, 05, and 06 each have one pair appearing in two selected `C_e` lists. Their set-union sizes are therefore one less than the corresponding sum of list sizes. Set deduplication is required even on these small profiles.

The previously saved checker retained 16 bad old–old examples per candidate, not complete lists of every bad pair. Among those 160 saved examples, 38 have original distance 4 and are omitted by this score; the other 122 are counted. The limited witness sample does not exhibit a joint-cut omission; the aggregate strengthened comparison below does identify such omissions without recovering their endpoints.

For a concrete failure, candidate 02's pair `(0,1460)` has `d_G=4` and the saved full-BFS result gives `d_F=6`. It is automatically outside `C`, independently of the optimistic repair inequalities. Thus extending only the optimization effort on this score cannot eliminate its built-in omission of shorter original pairs. The bound remains useful as a fast necessary filter, and exact final graph evaluation remains essential when the score reaches zero or the profile ends.

The exported `C_e` lists were separately verified by the source agent, including exact agreement with deleted-edge all-root BFS on seven edge-orbit representatives. The independent Python comparison here took 0.129578 CPU seconds. `lower_bound_ten_check.json` records every counted pair, each new-root forced miss, all comparison counts, and the limited saved witnesses used for omission analysis.

## Strengthened compulsory-edge definition: all lengths at most five

The root subsequently authorized a stronger export, kept separate as `critical_upto5_pairs.txt`. Define `D_e` to be the set of old unordered pairs for which **every walk of length at most 5 uses e**, without restricting their original distance to exactly 5. Because the source has diameter 5, every such old pair has at least one walk of length at most 5. Equivalently,

```
{x,y} in D_e  iff  d_(G−e)(x,y)>5.
```

The equivalence is exact for walks as well as paths: a walk avoiding `e` can have cycles removed to produce a path avoiding `e` of no greater length. Repeated traversal therefore introduces no error in this test.

For a fixed root `x`, let `W_k(v)` be the family of walks from `x` to `v` of length at most `k`, and let `I_k(v)` be the intersection of their sets of used edges. Maintain a separate flag indicating whether `W_k(v)` is nonempty. Initially only the root is reachable, with `I_0(x)` the empty set. At step `k`, take the intersection of:

- `I_(k−1)(v)`, if `v` was reachable;
- `I_(k−1)(w) union {wv}`, for every neighbor `w` reachable at step `k−1`.

This recurrence follows from the exact partition into carried-over shorter walks and walks obtained by appending a final edge. For each fixed appended edge `e`,

```
intersection_P (E(P) union {e}) = (intersection_P E(P)) union {e}.
```

The union is a set union, so duplicate edges must be removed. An unreachable predecessor contributes no path family and must be skipped; a reachable predecessor whose common-edge set is empty must participate. Each update must read a frozen previous layer. The distinction between unreachable and reachable-with-empty-intersection is essential. With these conventions the recurrence computes exactly `I_k`, and `e in I_5(y)` exactly records `{x,y} in D_e`.

Replace `C` in the lower-bound proof by the set union of `D_e` over the matching. Every pair in this union is still damaged in `H`, so the same endpoint inequalities give a valid, at least as strong lower bound. This removes the restriction that omitted single-edge damage had to originate at distance 5. It still does not capture every possible joint matching cut. In fact the original-graph endpoint inequalities are exact for shortcut repair in this particular augmentation, as follows.

Old candidate graphs and their full-BFS truth remain unchanged. The old `critical5` export and old comparison are preserved; the strengthened score is a metric change, not a construction improvement.

## Stronger exact identity: original-graph endpoint distances suffice

For every old vertex `x`,

```
d_F(x,u)=a_G(x)+1,     d_F(x,v)=b_G(x)+1.
```

Take a shortest `G` path from `x` to the set `A`. If it uses a deleted matching edge, that edge must be its last step, oriented `b_i→a_i`: otherwise the path has visited an `A` vertex earlier, contradicting minimality of the distance to the set. Therefore either the path remains in `H` and can be followed by `a_i-u`, or its final edge and the attachment can be replaced by `b_i-v-u`. Both give a walk in `F` of length `a_G(x)+1`.

For the reverse bound, the already proved new-root formula gives `d_F(x,u)=min(a_H(x)+1,b_H(x)+2)`. We have `a_G≤a_H`, and `a_G≤b_H+1` because every `B` vertex has its matched neighbor in `A` in `G`. Thus both terms are at least `a_G+1`. The proof for `v` is symmetric. This works even when `H` is disconnected.

Consequently, for old `x,y`,

```
d_F(x,y) = min(d_H(x,y),
                a_G(x)+a_G(y)+2,
                b_G(x)+b_G(y)+2).
```

Each term supplies a walk: an old `H` path or two shortest `F` paths through one specified new vertex. Conversely every shortest `F` path either stays in `H` or contains at least one of `u,v`; its length is at least the corresponding term. Walk concatenations may repeat a vertex, which does not invalidate the upper bound on graph distance.

Since every vertex of `A` is matched to a vertex of `B` in `G`, `|a_G(x)−b_G(x)|≤1`. Hence the two crossed `G` terms with additive constant 3 cannot improve the minimum of the two same-root terms. They are valid but redundant in the proposed lower-bound evaluator. Likewise the new-root lower-bound conditions simplify to `a_G(x)>4` and `b_G(x)>4`, and are **exact**, not just necessary, for every matching of this form.

This also means there is no endpoint-distance approximation error in the strengthened score. Its only remaining omission is a pair damaged by the matching jointly, but not by any selected edge individually, that also fails the exact endpoint repair test.

## Strengthened score on the same ten graphs

The independent script was run with `--upto5`, preserving the old result and writing `lower_bound_upto5_ten_check.json`. It took 0.155358 CPU seconds and ran no BFS. The new compulsory-edge file has 996145 edge/pair incidences and was independently validated by the source agent on the seven edge-orbit representatives. Its distance-5 slices exactly equal the original export.

| Candidate | Old score | New single-deletion union size | New old–old bound | New–old exact count | New total bound | Actual total | Unrepaired joint damage |
|---|---:|---:|---:|---:|---:|---:|---:|
| 00 | 309 | 576 | 364 | 18 | 382 | 382 | 0 |
| 01 | 326 | 538 | 370 | 22 | 392 | 392 | 0 |
| 02 | 304 | 509 | 349 | 14 | 363 | 364 | 1 |
| 03 | 401 | 804 | 488 | 22 | 510 | 512 | 2 |
| 04 | 412 | 642 | 442 | 22 | 464 | 464 | 0 |
| 05 | 384 | 593 | 416 | 21 | 437 | 439 | 2 |
| 06 | 359 | 587 | 405 | 19 | 424 | 424 | 0 |
| 07 | 340 | 598 | 390 | 13 | 403 | 404 | 1 |
| 08 | 309 | 510 | 356 | 17 | 373 | 373 | 0 |
| 09 | 361 | 587 | 395 | 30 | 425 | 425 | 0 |

The strengthened score is exact on six of these ten graphs and misses only one or two actual old–old failures on each remaining graph. This is a comparison of two scores on unchanged graphs, not a construction improvement. The exact shortcut identity makes the residual interpretation rigorous: all six residual failures across the ten candidates come from joint deletion damage outside the union of single-edge damage sets.

For example, in candidate 02 the saved `H` truth has 514 damaged old pairs, whereas the single-edge union contains 509. Of those five jointly damaged pairs outside the union, four are repaired by the new vertices and one is not. This accounts exactly for lower bound 363 versus actual 364. The saved witness `(0,1460)` from the old omitted distance-4 class is now counted. Complete aggregate comparisons are in `lower_bound_metrics_comparison.json`; no new full-BFS run was used.
