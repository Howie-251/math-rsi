# GF64/C42 coset tower: complete three-inverse-pair batch

The authorized **1,058,400 inputs were all completed**, with **no diameter-5
solution**. Every input was legal and passed the actual head-head coverage
check; none was skipped. All received the exact three-root BFS score. The
single-worker batch used **about 109.92 CPU seconds** including preparation
and final serialization, within the original 180-second budget. There was
no restart, extra parameter or search of another generator composition.

This closes the **three noninvolutory inverse-pair branch** for the specified
3200-point tower, using the candidate-preservation proof in [SCOPE.md](SCOPE.md).
**Two inverse pairs plus two involutions remain unsearched and open.** The
result does not exclude the entire tower family and does not establish a
new degree-diameter record.

## Best saved graph

The first saved optimum over the declared inputs has first quotient 2,
other pair indices `(151,62)`, and

`S={(1,2),(62,40),(19,8),(46,34),(61,3),(52,39)}`.

Here the first coordinates are binary polynomial encodings in
`F2[t]/(t^6+t+1)`, not integers modulo 64. Its leaf, block and head root
missing counts are **48,78,42**, giving exactly

`(2688*48+448*78+64*42)/2 = 83,328`

bad unordered pairs. The complete graph is `search.best.edges`, with
parameters in `search.best.json`. An independent run of the existing
generic checker on this saved edge list checked **all 3,200 roots** and
confirmed a simple connected **7-regular graph with diameter 6**, 11,200
edges and exactly **83,328 bad unordered pairs**. The result is saved in
`best.independent_verify.json`; the check took 0.209921 seconds. Its
`valid=false` means the graph fails the requested diameter-5 bound.

## Complete per-quotient results

Every row contains 176,400 raw, legal, HH-passing and fully scored inputs.
The component minima in the next table need not occur in the same S.

| First quotient | Best bad pairs | Min leaf miss | Min block miss | Min head miss | Head-zero candidates |
|---:|---:|---:|---:|---:|---:|
| 1 | 85,344 | 46 | 54 | 0 | 488 |
| 2 | 83,328 | 46 | 54 | 0 | 488 |
| 3 | 83,328 | 48 | 54 | 0 | 708 |
| 6 | 85,344 | 49 | 54 | 0 | 708 |
| 7 | 133,056 | 78 | 120 | 0 | 312 |
| 14 | 177,408 | 110 | 120 | 0 | 312 |

In **every row**, the leaf-zero count, block-zero count and simultaneous
head-and-block-zero count are all **zero**. A total of **3,016 normalized
candidates** achieve full head-root coverage, but none achieves block-root
coverage. These are candidate counts, not counts of nonisomorphic graphs.
The metrics were accumulated during the same three BFS evaluations, with
no additional graph searches or BFS evaluations for these counters.

The first head-zero witness, cursor 2,988, is

`S={(1,1),(57,41),(28,1),(34,41),(27,3),(56,39)}`,

with root misses **399,204,0** and 581,952 bad pairs. It is saved in
`search.first_head_zero.json`. Each first-quotient branch also preserves its
first head-zero S and its best full graph and parameters. Complete score
histograms, minima, zero counts and cursor are in `search.terminal.json`.

## Exact finite scope and construction

The field is `GF64=F2[t]/(t^6+t+1)`, encoded by six-bit polynomials. The
primitive element g=t has code 2 and order 63; r=g^3 has code 8 and order
21. The group retains **all 42 quotient indices**:

`(x,i)(y,j)=(x+r^i*y,i+j mod42)`.

Addition of field coordinates is XOR. The inverse is
`(r^-i*x,-i mod42)`; characteristic two removes the minus sign from the
field coordinate, not from the quotient index. The action is nonfaithful,
but the group and graph are not reduced to 21 quotient indices.

Leaves are labelled `x+64*i`, blocks `2688+x+64*b` with `b=i mod7`,
and heads `3136+x`. Leaves attach to their blocks, blocks to their heads,
and right Cayley multiplication by S gives the six leaf neighbours. Thus
the graph has 2,688 leaves, 448 blocks, 64 heads, 3,200 vertices and 11,200
edges. Its degree is 7. With `H=<(0,7)>` and `K={(0,i)}`, left group
multiplication preserves all edges and is transitive on each of the three
layers. This proves the exact weighted three-root score used above.

The nonidentity involutions are all `(x,0)` with x nonzero and all `(x,21)`,
127 in total. The other 40 quotient indices give noninvolutory inverse
pairs. Each of the three nonzero multiplicative orbits of `<r>` has 21
elements and contributes **420 inverse pairs**; zero translation contributes
20 more. Three inverse pairs can cover all head-head pairs only by choosing
one pair from each nonzero orbit. Thus zero-translation pairs and repeated
orbits are excluded by a necessary condition, not arbitrarily omitted.

Simultaneous field scaling fixes H and K and puts the first chosen element
at `(1,i)`. Frobenius together with quotient multiplication,
`(x,i)->(x^2,23*i)`, is an actual subgroup-preserving group automorphism.
Changing to the inverse first element and then scaling by `r^i` realizes
`i->-i`. The multipliers 23 and -1 generate all units modulo 42, giving the
six complete first-index classes represented by **1,2,3,6,7,14**. Frobenius
may exchange the other two field-coordinate orbits; enumerating their full
420-by-420 pair product preserves those images. No ordinary integer
modular field arithmetic, inner translation conjugation, or unsupported
quotient-unit automorphism was used.

Consequently the complete input range is `6*420*420=1,058,400`. The
independent math agent's [SCOPE.md](SCOPE.md) and `scope_check.json` verify
the polynomial, primitive orders, involution/pair counts and normalization
coverage. The search separately generated the real inverse pairs and
checked each candidate's legality and actual 64-head coverage mask.

## Preflight and resource record

This engine implements characteristic-two GF64 and cannot directly reuse
the characteristic-five F25 baseline. The authorized fallback was used:
GF64 arithmetic/group-inverse checks, followed by exactly two actual
expanded graphs and independent generic full-source BFS.

The C++ engine checked a 63-element primitive cycle, the order-21 action,
and left/right inverse and identity equations for all 2,688 group elements.
Independent Python field multiplication reconstructed the entire edge set
for both samples, including the subgroup-parent edges. The sets matched
the C++ outputs exactly. The existing generic checker then checked all
3,200 roots of each sample, agreeing with the three-root weighted scores:

| First quotient | Other pair indices | Three root misses | Diameter | Bad unordered pairs |
|---:|---|---|---:|---:|
| 1 | `(0,0)` | 794,597,420 | 7 | 1,214,304 |
| 7 | `(123,321)` | 209,330,210 | 6 | 361,536 |

Both were simple connected 7-regular graphs. `preflight.json` and the two
`preflight_*.generic_verify.json` files preserve the actual checks. No
previous full candidate enumeration was repeated.

The first **2,000 raw slots** formed the requested profile and were not
rerun. All 2,000 were scored. Setup used 0.014982 CPU seconds; the profile
loop used 0.252138 seconds. The resulting whole-batch estimate was
**133.446 CPU seconds**, below the available **177.566** seconds, so the
same process continued from cursor 2,000. Actual search CPU was
**107.974425 seconds**; the full preparation and run used about 109.92.

Stop-on-D5 was active both in preflight and production; no hit occurred.
The final status is `COMPLETE_NO_SOLUTION`, cursor **1,058,400**, with no
next parameters. `terminal.json` combines the runtime, profile, counts,
preflight and final verification reference. Sources, executable, run log,
pair-class lists, first-head witnesses and complete best graphs remain in
this directory. Wiki and HTML were not modified.

## Central-kernel concentration

The kernel involution `k=(0,21)` is central and lies in H. Its left action
fixes every block and head, while pairing leaves `(x,i)` and `(x,i+21)`
within each block. For every leaf edge, its image under k therefore joins
the same pair of blocks. These two edges are distinct: a leaf edge could
be fixed as an unordered pair only if its generator were k, which is
absent from the three noninvolutory inverse pairs.

Every distinct pair of head groups has exactly four leaf edges between
them, because each nonzero field difference belongs to exactly one of
the three selected multiplicative orbits, with two quotient preimages
for each of that pair's two generators. The central-kernel pairing shows
that this uniform head-level count still contains concentration at block
level. For first quotients 7 and 14, both signs of that first generator
also preserve the block index modulo 7; these two branches have minimum
block-root missing count 120, compared with 54 in the other four branches.
This gives a concrete structural feature alongside the observed failures.
It does **not** establish a uniform route-capacity upper bound or exclude
the unsearched two-pair/two-involution branch. No additional computation
was performed for this observation.
