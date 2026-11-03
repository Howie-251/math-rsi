# Degree 6, q61 coset tower: complete finite batch

The authorized A1, A0 and B ranges are **complete, with no diameter-5
solution**. The run visited **1,980,602 raw loop slots**, rejected the 29
duplicate-pair slots, and handled all **1,980,573 valid candidates**. The
necessary head-head test rejected 308,883; all **1,671,690** remaining
candidates received the exact three-root score. There was one worker, no
restart and no additional parameter. Total CPU including preparation was
**103.72 seconds**, within the 180-second budget.

The best saved HH-passing candidate is type A1,

`S={(1,15),(44,2),(43,28),(41,4),(22,26)}`.

Its leaf, block and head roots miss **118, 95 and 60** vertices at distance
at most 5. The weighted bad unordered-pair count is **127,185**. An
independent agent ran the existing generic checker on the complete saved
edge list, from **all 2,257 roots**, confirming a **simple, connected,
6-regular graph with 6,771 edges and diameter 6**, and exactly the same
127,185 bad pairs. This graph fails the D5 target; no new-record claim is
made. See `search.best.edges`, `search.best.json` and
`best.independent_verify.json`.

## Construction and candidate ranges

Use `G=Z_61 semidirect C30` with r=4, whose action has order 30, and

`(x,i)(y,j)=(x+4^i*y mod61,i+j mod30)`.

There are 1,830 leaves `x+61*i`, 366 blocks
`1830+x+61*b` for `b=0..5`, and 61 heads `2196+x`. Leaf `(x,i)` attaches
to block `(x,i mod6)`; block `(x,b)` attaches to head x. Each block has
five leaf children, each head six blocks, and each leaf five Cayley
neighbours from a distinct, inverse-closed, nonidentity S. Thus the graph
has degree 6 and `n=(30+6+1)*61=2257` vertices.

The subgroups are `H=<(0,6)>` of order 5 and `K={(0,i)}` of order 30.
Left multiplication acts on the leaf, block and head orbits, so three
ordinary BFS runs to depth 5 give exact missing counts a,b,c, and

`bad unordered pairs = (1830*a+366*b+61*c)/2`.

Only simultaneous field scaling `x -> lambda*x` was used for normalization;
it fixes H and K. No inner translation conjugation or free-port choice was
introduced. The 61 involutions are `(x,15)`. The other 1,768 nonidentity
elements form **884 noninvolutory inverse pairs**, represented by the smaller
integer leaf label. The representative list includes all 14 pairs with
x=0, and is saved in `search.inverse_pairs.json`.

- **A1:** two distinct inverse pairs and a nonzero-translation involution,
  scaled to `(1,15)`. Choose both pairs unordered: `C(884,2)=390286`.
- **A0:** two distinct inverse pairs and `(0,15)`. If all translations
  vanish, no edge connects distinct x groups. Otherwise scale a nonzero
  pair element to `(1,i)`, for all 29 choices `i!=15`, then choose the
  second pair among all 884 representatives. The 29 identical-pair slots
  are invalid, leaving `29*883=25607` valid candidates.
- **B:** one inverse pair and three distinct involutions. At least one
  involution is nonzero, so scale one to `(1,15)`. Choose the other two
  translations unordered from `F_61\{1}`: `C(60,2)=1770`, and choose
  any inverse pair, giving `1770*884=1564680` candidates.

The five-involution family was **not enumerated**. Its separate block-index
obstruction is the parent's mathematical coverage argument. The program's
finite scope consists exactly of the three ranges above, not an additional
unreported scan of all S.

## HH filter, complete counts and remaining coverage

A head-to-head path of length at most 5 descends two tree edges, takes one
leaf edge, and ascends two tree edges. Thus every D5 candidate must have
nonzero generator translations meeting both multiplicative orbits of
`<4>` in `F_61*`. These are the two 30-element square/nonsquare classes.
This necessary filter only checks head-head pairs, not full head coverage.

The 884 inverse pairs split into 435 square-translation pairs, 435
nonsquare-translation pairs and 14 zero-translation pairs. Therefore the
expected HH-pass counts are `C(884,2)-C(449,2)=289710` for A1,
`29*435=12615` for A0, and `(1770-435)*884+435*435=1369365` for B. These
counts were also checked independently on paper by the math agent. The
actual loop counts match all of them:

| Type | Raw slots | Invalid duplicates | Valid candidates | HH excluded | Fully scored | Best scored bad pairs |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 390,286 | 0 | 390,286 | 100,576 | 289,710 | 127,185 |
| A0 | 25,636 | 29 | 25,607 | 12,992 | 12,615 | 197,640 |
| B | 1,564,680 | 0 | 1,564,680 | 195,315 | 1,369,365 | 204,045 |
| Total | 1,980,602 | 29 | 1,980,573 | 308,883 | 1,671,690 | 127,185 |

The following metrics were accumulated during those same BFS evaluations.
They are over HH-passing, fully scored candidates. The three component
minima need not occur in the same candidate.

| Type | Minimum leaf miss | Minimum block miss | Minimum head miss | Leaf-zero count | Block-zero count | Head-zero count | Head+block-zero count |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 112 | 80 | 0 | 0 | 0 | 108 | 0 |
| A0 | 176 | 135 | 90 | 0 | 0 | 0 | 0 |
| B | 202 | 95 | 0 | 0 | 0 | 696 | 0 |

Thus **804 normalized candidates achieve full head-root coverage**, while
none of the HH-passing candidates achieves block-root coverage. In
particular none achieves head and block coverage together. The head-zero
and head+block-zero counts are also complete over the whole declared valid
range, since an HH failure itself prevents head-zero. The other minima and
zero counts retain their explicitly stated HH-conditioned scope.

The first full-head witness, at candidate cursor 31,230, is

`S={(1,15),(6,1),(29,29),(18,2),(37,28)}`,

with root misses **263,195,0**, saved in `search.first_head_zero.json` and
`search.A1.first_head_zero.json`. Type B's first full-head witness is
`S={(1,15),(2,15),(9,15),(29,6),(51,24)}`, with root misses **1153,820,0**,
saved in `search.B.first_head_zero.json`. A0 has no such file because its
head-zero count is zero. These are S witnesses and measured scores, not
claims of full D5 graphs.

For reference, A0's saved best is
`S={(0,15),(1,2),(19,28),(54,14),(33,16)}`, with misses 176,180,120.
B's saved best is
`S={(1,15),(8,15),(43,15),(16,14),(3,16)}`, with misses 202,95,60.
Each branch best has a complete edge list. Only the overall best received
the requested independent final full-root check.

The best bad-pair values are minima among **HH-passing** candidates. Skipped
HH failures were not fully scored, so these are not claimed as global
bad-pair minima over the entire raw range. Nevertheless all skipped
candidates fail D5 by the necessary condition, and all passed candidates
were completely scored, so the finite D5-negative result is complete.

## Generalization checks, profile and budget

The engine generalized degree-dependent values to
`m=d(d-1)`, leaf count `mq`, block count `dq`, head count q, block children
`d-1`, and leaf generator count `d-1`. It was checked against exactly two
saved q41/d5 samples, the former A-best and B-best. The **entire labelled
edge sets**, including all subgroup-parent edges, and all three missing
counts matched the old files. No old enumeration or large regression was
repeated. `preflight.json` records these two comparisons.

The first **2,000 raw loop slots** were the profile and were not rerun.
They included 1,432 complete scores, with 0.068541 CPU seconds of setup and
0.113051 seconds in the profile loop. The estimate charged every remaining
slot at the observed cost per fully scored candidate, giving **156.385 CPU
seconds** total against **178.07** seconds available. The same process
therefore continued from cursor 2,000.

Actual search CPU was **102.286966 seconds**; compilation, the two old-sample
checks and orchestration brought the total to **103.72 seconds**. One CPU
affinity was used, with a cumulative 180-second allowance and a soft timer
margin. Stop-on-D5 was enabled. The final independent best-graph checker
reported about 0.06917 seconds.

The terminal is `COMPLETE_NO_SOLUTION`, cursor **1,980,602**, with no next
parameter. `scope.json`, `search.profile.json`, `search.terminal.json` and
`terminal.json` preserve the requested scope, actual costs, counters,
per-branch complete score histograms, root metrics and terminal state.
The source, executable, run log, first-head witnesses and complete best
graphs remain in this directory. Wiki and HTML were not modified.
