# Faithful semilinear F64 tower: complete three-pair branch

The authorized **5,058,306 normalized inputs are all complete**, with
**no diameter-5 solution**. There were 4,484,088 HH passes and **1,240 BB
passes**. Every BB pass received ordinary BFS from all three orbit roots
of the actual 3,200-point graph. None achieved simultaneous head-root and
block-root coverage.

The best graph **among the 1,240 completely scored BB passes** has 51,072
bad unordered pairs. Its saved edge list was independently checked from
all 3,200 roots: it is simple, connected, 7-regular, has 11,200 edges and
**diameter 6**. The 51,072 bad pairs are exactly the pairs at distance 6.
This is not a new degree-diameter record. The result closes the declared
three-noninvolutory-inverse-pair branch of this fixed semilinear tower;
generator sets containing involutions were not searched.

## Scope and the changed group action

The field is `F2[t]/(t^6+t+1)`, encoded by six-bit polynomials. Put r=t^3,
which has order 21, and F(x)=x^8. The group operation is

`(x,a,e)*(y,b,f)=(x+r^a*y^(8^e), a+8^e*b mod21, e+f mod2)`.

The implemented inverse is the actual semilinear inverse

`(x,a,e)^-1=(r^(-8^e*a)*x^(8^e), -8^e*a mod21, e)`.

It does not use the previous cyclic-group inverse. The group has 2,688
elements, with `K=C21 semidirect C2` of order 42 and `H=<r^7,F>` of order
6. Leaves are labelled `x+64*(a+21e)`, blocks `2688+x+64*(a mod7)`, and
heads `3136+x`. Each leaf joins its block, each block its head, and six
right Cayley generators give the remaining leaf edges. The full graph
is 7-regular and has layer sizes 2,688/448/64.

This action is faithful. In particular, the old central involution
fixing all blocks and heads is absent; the old central quotient and
16-bit lift criterion were not applied. H has genuine three- and
six-point field-coordinate orbits. [STRUCTURE.md](STRUCTURE.md) gives the
independent group and subgroup check.

Exactly 1,300 true noninvolutory inverse pairs were generated using the
new inverse: 19 have zero field coordinate, 420 lie over the 21-point K
orbit, and 861 lie over the 42-point K orbit. This includes valid general
elements `(x,0,1)` with `x^8 != x`; only the normalized first element has
the restriction a!=0.

HH requires both nonzero K orbits. Select a first pair over the 21-point
orbit and use actual K rotation conjugation, which changes a as well as
x when e=1, to normalize one endpoint to x=1. Frobenius and inverse-pair
reorientation give six first representatives

`(1,a,e), a in {1,3,7}, e in {0,1}`.

For each first pair, all unordered choices of two different pairs from
the other 1,299 are included. Thus each branch has C(1299,2)=843,051
legal inputs. The independent proof in [NORMALIZATION.md](NORMALIZATION.md)
gives 747,348 HH passes per branch, totaling 4,484,088. Actual counts
agree exactly. No arbitrary field scaling or unsupported quotient-unit
reduction was used.

## Exact filtering and complete per-branch results

HH is checked by the actual K-orbit field mask. The BB filter computes
the exact set

`H W3 H union K W1 H union H W1 K`

as seven 64-bit masks. Every word of length at most three is included.
For its endpoint `(x,a,e)`, left H changes x within its true S3 orbit
and preserves a modulo 7. Both source-head and target-head terms are
retained. A BB failure is an actual five-step block-to-block failure,
so rejecting it cannot remove a diameter-5 graph.

Only a BB pass triggers the actual graph's three-root BFS. The exact
number of bad unordered pairs is

`(2688*missing_leaf + 448*missing_block + 64*missing_head)/2`,

because left group multiplication is transitive on each layer and
preserves all graph edges. No quotient leaf score is used.

Each row below has 843,051 raw and legal inputs, 747,348 HH passes and
95,703 HH failures. Root statistics and best scores are conditional on
the BB passes that actually received BFS; component minima need not
occur for the same S.

| First (a,e) | BB passes / three-root BFS | Min BB miss | Best scored bad pairs | Min root misses L/B/H | Head-zero scored candidates |
|---|---:|---:|---:|---|---:|
| (1,0) | 291 | 0 | 51,072 | 32 / 6 / 0 | 66 |
| (1,1) | 301 | 0 | 55,104 | 33 / 18 / 0 | 67 |
| (3,0) | 342 | 0 | 59,136 | 36 / 6 / 0 | 66 |
| (3,1) | 288 | 0 | 51,072 | 32 / 18 / 0 | 76 |
| (7,0) | 18 | 0 | 228,480 | 153 / 102 / 0 | 6 |
| (7,1) | 0 | 3 | unscored | unscored | unscored |

Totals are 5,058,306 raw/legal, zero invalid, 574,218 HH failures,
4,484,088 exact BB evaluations, and 1,240 three-root BFS evaluations.
Among those scored candidates, 281 have full head-root coverage; no
leaf root or block root has zero missing vertices. The 281 count is
not a count of all head-zero candidates in the raw range, and it is
not a count of nonisomorphic graphs. Simultaneous head-and-block coverage
is zero on the complete range, since an HH or BB failure also precludes
that joint condition.

The failure remains a shared coverage issue: BB is achievable in this
changed action, but the same generators do not supply all required
block-to-leaf and head/leaf routes. This observation does not establish
a new uniform capacity theorem for other generator compositions.

## Saved best and independent verification

The first best fully scored input has cursor 266,295, first branch (1,0)
and other pair indices `(225,745)` in the saved 1,300-pair table. Its S is

`[(1,1,0),(57,20,0),(33,4,0),(52,17,0),(13,2,1),(59,5,1)]`.

It covers every block from the block root, but its full root misses are
**32,27,63**, giving **51,072** bad pairs. The complete edge list is
`production.best.edges`, with parameters and seven BB masks in
`production.best.json`. `best.independent_verify.json` records the
independent 3,200-root check: n=3,200, m=11,200, degree 7, connected,
diameter 6 and exactly 51,072 bad unordered pairs. The checker took
0.220874 seconds. Its `valid=false` refers to the requested D5 bound.

A subsequent three-root layer decomposition, without repeating the
generic full-source check, gives:

| Root | Missing leaves | Missing blocks | Missing heads |
|---|---:|---:|---:|
| Leaf | 27 | 4 | 1 |
| Block | 24 | 0 | 3 |
| Head | 42 | 21 | 0 |

The corresponding unordered bad-pair counts are LL=36,288,
LB=10,752, LH=2,688, BB=0, BH=1,344 and HH=0, totaling 51,072.
Thus this saved graph has solved BB and HH, while leaf-involving routes
and some head-to-block routes remain. The decomposition is saved in
`production.best.bad_pair_types.json` and used 0.01104 CPU seconds.

BB-failing inputs were not fully scored, so the report does not claim
that 51,072 is the global minimum bad-pair count over every raw input.
The separate `production.best_BB.json` records the first zero-BB-missing
input, which need not be the best fully scored graph.

## Preflight, profile and exact continuation

Before profiling, two new actual graphs were independently reconstructed
using the semilinear operation and compared edge for edge. Both complete
11,200-edge sets matched. The source agent also checked all 448 BB targets
against the formula and ran the generic full-source checker once on each
graph. Results are in `preflight.independent_check.json` and
`preflight_0/1.independent_verify.json`:

| Sample inverse-pair representatives | Root misses L/B/H | BB miss | Bad pairs | Actual D |
|---|---|---:|---:|---:|
| (1,1,0), (2,0,1), (3,3,1) | 123 / 207 / 147 | 60 | 216,384 | 6 |
| (1,7,1), (0,1,0), (2,5,1) | 247 / 234 / 357 | 51 | 395,808 | 6 |

The first sample deliberately includes a=0,e=1 with x^8!=x. The C++
setup also checked both inverse identities for all 2,688 elements and
the actual 87-involution/1,300-inverse-pair counts. These were checks of
the new group, not reruns of historical candidate batches.

The initial profile visited `[0,2437)`: 2,437 legal raw inputs, exactly
2,000 HH passes, zero BB passes and minimum BB missing count 3. It
stopped as requested. Its first best missed only blocks `(5,0)`, `(18,0)`
and `(23,0)`; that prefix did not exclude the branch. The short prefix's
rough 2.25-second frontend estimate excluded unobserved downstream BFS
cost, and sub-stage times were below the timer's useful resolution.

After a separate authorization, the same executable continued over
`[2437,5058306)`, without repeating any prefix input or either preflight.
It found the BB passes above and fully scored them. Stop-on-D5 was
enabled throughout; no hit occurred. The final cursor is **5,058,306**,
with no next parameters. No optional extra head filter was introduced.

Cumulative charged CPU through the search was **12.503756 seconds**,
including preparation, compilation, independent preflight CPU, prefix
profile and continuation; the continuation itself used 10.317341
seconds. The final best-graph check added the separate 0.220874-second
checker run, comfortably within the authorized 180-second cumulative
budget; the later layer decomposition added 0.01104 CPU seconds. There
was one search worker. The final status, six completed
branch counters, histograms, cursor intervals and independent validation
are in `terminal.json`; `profile.run.json` preserves the original profile
record. The source, executable, real pair table, logs and full best graph
are saved in this directory. No other group or generator composition was
started, and no formal proof-assistant certification is claimed.
