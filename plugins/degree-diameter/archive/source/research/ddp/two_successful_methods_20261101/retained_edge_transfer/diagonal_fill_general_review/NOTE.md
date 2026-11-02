# Independent paper attack: diagonal fill reallocation

2026-11-01. Reviewed `../DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md` as a conditional finite-GQ theorem. **Supported: no mathematical gap found in the stated hypotheses or formulas.** This is a new paper review, not a graph experiment, a Lean theorem, a priority result, or an item certified by the old Q8 final C.

The hypotheses remain essential: an actual finite GQ of order `(s,t)` with `s,t>=2`, an actual line spread of size `R=st+1`, an actual partial ovoid of size `p`, and the stated filled-source graph H with its inherited diameter-at-most-3 theorem. No existence of a full ovoid or of a GQ at arbitrary numerical `(s,t)` is inferred.

## 1. Partial ovoid is sufficient; no hidden full-ovoid step

Write `delta=(s+1)(t+1)` and `u=delta*R^2=|U|`. The GQ has `(s+1)R` points and `(t+1)R` lines. A spread partitions all points, so every selected point has exactly one spread owner. Thus O times the spread has exactly `pR` distinct centers and exactly `p` incident centers, even if O is only partial. Counting selected-point/line incidences also gives `0<=p<=R`; no equality is used by coverage or load.

For centers `c=(o,S_j)` and `c'=(o',S_j')`, a common U-neighbor `(v,N)` implies `o,o' in N` and `v in S_j intersect S_j'`. The partial-ovoid condition forces `o=o'`; the spread forces `j=j'`. Consequently the U-neighborhoods of distinct centers are disjoint. Removing the self-slot at an incident center only reduces its own neighborhood and cannot introduce overlap. There are `p` such self-slots, so

`Q = |union_c N_U(c)| = delta*pR-p`.

This is the only packing argument needed. It does not require selected points to meet every GQ line, nor centers to be independent. Clones of the *same* center intentionally have identical neighborhoods, so the old-point load after k copies is k, not 1.

## 2. Coverage attack: k>1 and all endpoint types

The source U has diameter at most 3 directly from the GQ projection axiom. For endpoints `(a,L)` and `(b,M)`, choose `r in L`, `r!=b`, collinear with b, and `s in M`, `s!=a`, collinear with a. If b lies on L, choose another point of L; otherwise use its unique projection, and similarly for a and M. Let `K=rb` and `N=as`. Then

`(a,L), (r,N), (s,K), (b,M)`

has the cross-incidences for each successive step. Delete any consecutive identical vertices to obtain a genuine simple-graph walk of length at most 3. This explicitly supplies the old-U-only route rather than borrowing a route that might pass through a filler. Also, every U degree is delta or delta-1, so there are no isolated vertices. All clone edges are exactly to U.

* Clone to an old U target different from its center: replace the initial endpoint of a shortest U path. To its own center, use `clone(c)-u-c` for any `u in N_U(c)`.
* Two copies of the same center: `clone(c,r)-u-clone(c,r')`, length 2. This is the extra case that must be explicit when k>1.
* Different centers at U-distance 2 or 3: replace both endpoints of a shortest path. If the centers c,d are adjacent, use `clone(c,r)-d-c-clone(d,r')`, length 3. Center adjacency therefore causes no gap.

All these path interiors lie in retained U. They do not use fillers, future clones, or hubs.

For clone-to-filler pairs, a nonincident center has `N_H(c)=N_U(c)` and inherits the first edge of an H-to-filler path. At an incident center `c=(o,S_j)`, its omitted filler edge is precisely to F_j. Choose a line M through o with `M!=S_j`; the flag `(o,M)` is still a U-neighbor of c and also a neighbor of F_j. This gives `clone(c)-(o,M)-F_j`, length 2.

For a different F_l, an H path from c of length at most 3 cannot begin through F_j. Such a path would require an F_j-to-F_l suffix of length at most 2. The fillers have no mutual edge and have disjoint flag neighborhoods, so no such suffix exists. The initial edge lies in U and is retained by the clone. This argument does not use whether any other point of O meets a line.

Every U vertex has a *distinct* flag neighbor in U. For a nonflag `(a,L)`, take the unique point b of L collinear with a and its connector M=ab; `(b,M)` is the required flag neighbor. For a flag `(a,L)`, choose a different line M through a and use `(a,M)`. The stated `s,t>=2` are more than sufficient to make that choice.

Every clone therefore has a flag in its own U-neighborhood. A hub reaches any U vertex or clone by `hub-F_owner(b)-flag-target`, of length at most 3. It reaches every filler in 1 and another hub in 2 through any filler. All k hubs may have the same filler neighborhood; this is allowed in a simple graph because the hubs are distinct vertices. No hub-to-H collapse map is needed or generally supplied.

Thus H-H pairs inherit H, all clone endpoint types are covered as above, and all hub endpoint types are covered. The proof works for a partial ovoid, all integer k>=1, and even the empty partial-ovoid boundary if that convention is admitted.

## 3. Exact counts and maximum degree

Keep every H edge. Each of the k copies of the center code contributes Q clone-U edges; each of the k hubs contributes R hub-filler edges. Thus

`n = delta*R^2+R+k*(pR+1)`,

`m = delta*(delta*R^2+R)/2 + k*(delta*pR+R-p)`.

No clone-filler, clone-clone, clone-hub, or hub-hub edge is present. The counts use only the new rule, not an assumption that a prior full-H-copy graph is retained.

The exact histogram is:

| Degree | Count | Origin |
|---|---:|---|
| delta+k | Q+R = delta*pR-p+R | Q old U pins and all R original fillers |
| delta | delta*R^2-Q+k*(pR-p) | unpinned U and off-diagonal clones |
| delta-1 | k*p | diagonal clones |
| R | k | hubs |

The counts sum to n. The degree sum is `2*mH+2*k*(Q+R)=2*m`, which checks the edge formula independently of the grouping. The four degree values do not collide: `delta-R=s+t>=4`, `delta-1>R`, and `k>=1`. A zero count simply removes that row from the physical histogram. In particular the maximum degree is **exactly** delta+k, not merely at most delta+k, because each of the R original fillers has this degree. The hub bound `R<=delta+k` is automatic.

Relative to k full-H-neighborhood copies of the same `pR` centers, the rule adds k vertices and `k*(R-p)` edges: it removes kp diagonal clone-filler edges and adds kR hub-filler edges. The edge total is unchanged only when p=R. No full-ovoid hypothesis can be silently carried into a partial-ovoid edge budget.

## 4. Prefix validity

The valid generation order is H, then arbitrary modified clones, then hubs. At every clone insertion, its routes to H and earlier clones already use only H (and U for clone-clone routes). Every hub route to an already present clone uses a flag of H and that clone only as its endpoint. Hub-to-hub routes use a filler already present in H.

No future vertex is an internal point in any required route. A prefix has at most k copies per center and at most k hubs, so every old degree is bounded by its final degree delta+k. Clone degrees and hub degrees have the exact bounds above. The claim is not deduced by deleting vertices from a completed maximum graph, and it does not call a deletion from a previously accepted full-H-copy graph a monotone prefix.

## 5. Exact diameter: old U Moore witness survives all k

The proposed witness argument is sound, with the following explicit inequality. Since `s,t>=2`,

`st>=s+t`, `R>=5`, and `delta=R+s+t<=2R-1`.

Hence `R^2-delta >= (R-1)^2 >=16`, so

`|U|-(delta^2+1) = delta*(R^2-delta)-1 >0`.

Fix any vertex a in U. H is simple and delta-regular, so its radius-2 ball about a has at most `1+delta+delta*(delta-1)=delta^2+1` vertices, counting *all* of H, including fillers. Since U alone is larger, some b in U is outside that H ball. The inherited H diameter bound then gives `dist_H(a,b)=3`. This does not confuse a bound on old U balls with a bound on H balls.

There are no new edges between two old U vertices. If a new clone is adjacent to both a and b, its original center is already a genuine common neighbor of a,b in U, contradicting their H distance 3. Centers cannot cause a self-loop exception: a center is not in its own open U-neighborhood. A new hub has only filler neighbors and cannot be the middle point of a 2-step U-to-U path. These exhaust all possible new middle vertices in a length-2 shortcut, independently of k.

Therefore that *old U pair* remains at distance 3 after all additions and at every prefix. Together with the coverage proof, this establishes exact D3. It does not require or assert a graph homomorphism collapsing hubs into H, and it does not reuse the earlier clone-only collapse witness argument in a scope where that map is unavailable.

## 6. Disposition and remaining scope

No counterexample or missing condition was found. Recommended minor editorial strengthening of the root note: explicitly mention the same-center copy route for k>1, spell out the fixed-root Moore inequality above, and state maxdegree equals delta+k because of the original fillers. These are proof clarifications, not repairs to a false conclusion. The reviewed root note itself was not edited.

The next constructive decision is supported: use original U-neighborhoods and route spare filler capacity to hubs, instead of continuing fixed-mandatory-edge augmentation. This paper argument can guide a future generic/concrete Lean theorem. It does not create any instance, extend an external C review scope, resolve exact source-fill or reallocation literature priority, or establish a global degree-diameter record. In particular the accepted q4 instance and the separately dispatched q8 instance retain their own producer/independent/kernel/review receipts; this note is not a substitute for them.

No graph, field, BFS, solver, scalar enumeration, or Lean run was made for this review. Only the given general note and local file I/O were used.

## Short clarification: freeze G1, then use full-neighborhood copies

The root note's new k1-reuse section is correct. In G1 let J contain its first `pR` clones and first hub. J is independent. Its complete open neighborhoods are respectively `N_U(c)` and the original filler set F; these are disjoint from J, pairwise disjoint, and frozen subsets of H. Copying each role vertex in J another `k-1` times therefore gives exactly G_k, up to the explicit copy-index label bijection. It adds no unintended edge to an old J role, because no copied neighborhood meets J.

This matches the actual existing `FullNeighborhoodClones.graph` definition: the source is **G1**, and a new clone's center is the existing first clone (or existing first hub), not its original GQ center. For arbitrary k, use copy indices `(Fin(k-1),J)` and center map ignoring the first coordinate. At every old H point the new load is at most `k-1`; at every old J role it is 0. The generic `degree_le` applied with source bound `delta+1` and load bound `k-1` gives `delta+k`. Each new vertex's degree is its G1 center degree, so the diagonal/off-diagonal/hub degrees remain `delta-1`, `delta`, and R. Source J need not be regular; the actual generic theorem only requires a degree bound.

The generic `diameterAtMost` requires source D3 and no isolates, supplied by the G1 theorem and the positive degrees above. Its `not_diameterAtMost`/`old_walk_bound_iff` preserve G1 non-D2. The associated collapse is now from the copy graph **to G1**, where hub-role centers really exist; it is not the nonexistent claimed collapse of hubs to H. These are valid theorem interfaces, not a report that the new concrete kernel target has already compiled.

For k2 at q8, G1 has labels `0..346515`; its role centers are first clones `342290+h` for `0<=h<4225` and first hub `346515`. The appended labels are `346516+h` and `350741`. The bijection fixes every source label and maps these new labels to copies of exactly those role centers. Thus every one of the 14204970 source edges is retained and the copied-neighborhood rule is literally the stated monotone producer rule. No load or label omission was found. This clarification adds no graph, local-theorem count, Lean completion, or external-review scope; the degree83 producer remains a candidate until its own fresh acceptance is read by root.
