# Exactly three degree-six vertices at 23 points

## Claim and status

A pair-covering simple five-uniform hypergraph on 23 vertices with exactly
34 edges has Property B if exactly three vertices have degree six.

This is a complete paper candidate with exact local certificates and actual
selection/coverage arguments. Cross-family review and Lean remain. The local
calculation uses the same general random-order and shared-bad-vector lemmas
as the neighboring branches; it does not enumerate original hypergraphs.

## Actual selection: four common-unit highs, including two sevens

Let L consist of the three degree-six vertices. The other twenty vertices
have degree sum 152 and degree at least seven. At most six have degree at
least nine, since

\[
152\ge 7\cdot20+2h.
\]

Thus at least fourteen of them have degree seven or eight. Also at least
eight have degree exactly seven: at most twelve of the twenty can have degree
at least eight.

For a low vertex x, pair covering gives

\[
\sum_{y\ne x}(\lambda(x,y)-1)=4\cdot6-22=2.
\]

Consequently at most six vertices in total fail to be unit with all three
members of L. Let U be the degree-seven/eight vertices unit with all of L.
Then |U|>=8 and U contains at least two degree-seven vertices. Choose four
distinct members of U including two such sevens. Their degrees may be arranged
in nondecreasing order. It suffices to handle the actual traces on these four
points together with L.

## Complete one-high domain

The three low/low codegrees a,b,c lie in {1,2,3} and satisfy

\[
a+b\le4,\quad a+c\le4,\quad b+c\le4.
\]

These are exactly the necessary internal excess constraints. Append a
degree-seven or degree-eight point unit with all three lows. The complete
four-lock trace inventory, restoring singletons from the selected degrees and
the empty count from 34 edges, has 166 labelled entries and 58 degree-preserving
orbits. Of these, 23 have strict probability bounds and 35 remain.

The generator uses the existing complete four-lock formula `quad_general`;
the actual six pair codegrees are `(a,b,1,c,1,1)` in pair order
`01,02,03,12,13,23`. Every actual trace multiplicity is represented.
Evidence: `V23_THREE_LOW_H1.json`.

## Add common-unit highs with their actual traces

Suppose s selected locks have trace multiplicities n(T), and add an actual
point z of degree d in {7,8}. For each nonempty old trace T of size at most
four, let p(T) count old-trace edges containing z. Then

\[
0\le p(T)\le n(T),\qquad
\lambda(z,i)=\sum_{T\ni i}p(T),\qquad
n'(\{z\})=d-\sum_Tp(T).
\]

Promoting p(T) copies changes T to T union {z}; the remaining new singleton
copies come from the old empty trace. Thus the empty count decreases by
`d-sum p(T)`. Reject negative counts, pair-covering violations, old/new
codegree-excess budget violations, and any imposed low/high unit condition.
These are necessary conditions satisfied by the actual extension. Conversely
every actual extension determines exactly such a promotion vector, so the
local inventory contains all actual inputs.

When a deletion projection is already strict, the original H is colorable
using those selected points, and that extended input needs no further bound.
Otherwise retain the exact projected trace counts. Relabeling permutes only
equal-degree roles and transports the stored positions.

## Two highs

Start from a residual one-high input and append a second actual member of U.
No high/high unit condition is assumed. The initial caps come only from the
actual degrees and codegree-excess budgets. Require both one-high deletion
projections to remain residual.

There are 2,427 labelled promotions, 2,276 retained labels and 1,385 orbits.
Exactly 1,295 orbits are strict and 90 remain. All residual high/high
codegrees are one or two:

| High degrees | Codegree 1 residues | Codegree 2 residues |
|---|---:|---:|
| (7,7) | 7 | 2 |
| (7,8) | 11 | 11 |
| (8,8) | 6 | 53 |

Therefore every actual pair from U has codegree at most two in a putative
counterexample. This deduction, rather than a search restriction, supplies
the cap for subsequent extensions. Evidence: `V23_THREE_LOW_H2.json`.

## Three highs

Append a third actual high using the proved pair cap two, and retain an input
only if every two-high deletion projection is residual. The complete domain
has 7,846 labelled promotions, 1,971 retained labels and 652 orbits. Exactly
621 are strict and 31 remain, with degree-pattern counts

\[
(7,7,7):5,\quad (7,7,8):1,\quad (7,8,8):4,\quad (8,8,8):21.
\]

The six residues containing at least two sevens all have unit low/low pairs.
This observation is consistent with the next selection but is not required
as an additional assumption in its generator. Evidence:
`V23_THREE_LOW_H3.json`.

## Four highs containing the two actual sevens

Use the four members of U selected at the outset. They include at least two
sevens, so their first three points in nondecreasing degree order also include
at least two sevens. Hence they extend one of the corresponding three-high
residues. No loss occurs by restricting the four-high domain to degree
patterns with at least two sevens.

The complete promotion domain for these patterns has 8,470 labelled inputs.
Requiring every actual three-high projection to be residual leaves 45 labels
and ten degree-preserving orbits. All ten have four high degrees equal to
seven. Every one has a strict direct total/pure-quota bound, with maximum

\[
11381/11440<1.
\]

The degree patterns with an eight-degree point disappear because at least
one actual three-high projection is already strict. No hypothetical degree
pattern is silently excluded. Evidence: `V23_THREE_LOW_H4.json`.

Thus the actual seven-lock profile on L and the four chosen highs has a strict
certificate, either at one of its smaller projections or directly at the final
stage. The general random-order coloring lemma gives Property B for H.

## Exact verification and remaining formal work

Direct witnesses were replayed by `SubsetEngine.verify`, which compares raw
A/B/C with independent labelled-injection counts and separately checks the
corrected C after the retained deduction. Every strict shared-layout dual was
checked by `verify_joint_layout.verify` with the actual degree vector, both
ordered pair weights, avoided quotas, capacities and the repaired exact
rational inequality. A single actual bad-count vector is shared by all
layouts; the LP output only proposes the exact certificate.

`audit_v23_three_low.py` regenerates all four complete promotion/projection
domains, checks their equality with the recorded orbit tables, binds each
exact bound to its original trace profile, verifies the actual low/high unit
and degree/excess constraints, and independently replays every strict dual.
Its report is `V23_THREE_LOW_COVERAGE_AUDIT.json`. This regeneration uses the
documented inventory generator, while the probability replay uses a separate
labelled-injection implementation.

No new Lean module has been built by this worker. The remaining work is the
reviewed actual-input formalization and integration with the other 23-point
branches and the original T34 theorem.
