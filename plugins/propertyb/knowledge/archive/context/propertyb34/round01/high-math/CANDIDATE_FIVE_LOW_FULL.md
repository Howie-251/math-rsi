# The full five-low-vertex case at 24 vertices

## Claim and status

Let $H$ be a pair-covering simple five-uniform hypergraph on $24$ vertices with
exactly $34$ edges. If exactly five vertices have degree six, then $H$ has
Property B.

**PROVABLE AS STATED**, as a complete paper candidate. It combines the verified
nonunit-low branch with a new complete nonunit-high local catalogue and the
general nine-lock criterion. Lean and root-managed model review remain.

## Assumptions and dependency map

Let $L$ be the five low vertices. A low vertex has codegree excess one; a
degree-seven vertex has excess five. The proof proceeds as follows:

1. A nonunit pair in $L$ is handled by `CANDIDATE_FIVE_LOW_NONUNIT.md`.
2. Otherwise at least seven degree-seven vertices are unit with all of $L$.
3. Every nonunit pair among those highs has a complete strict local bound.
4. If there is no such pair, choose four highs, and use the $6^5 7^4$ nine-lock
   criterion from `NINE_LOCK_UNIVERSAL_LEMMA.md`.

## Proof

### 1. Reduce to five pairwise-unit lows

If two lows have nonunit codegree, apply the complete one/two-low-pair proof in
`CANDIDATE_FIVE_LOW_NONUNIT.md`. Assume all pairs within $L$ are unit.

The degree sum gives at least twelve degree-seven vertices. Delete the at most
five exceptional partners of the low vertices. The remaining set $Q$ has at
least seven vertices, all degree seven and unit with every low.

### 2. One-high local input

For each $x\in Q$, the six-lock profile has all pair codegrees one and degrees
$6^5 7$. The complete old catalogue has $352$ labelled inputs / $17$ colored
orbits. Two have old direct strict certificates and one more has a new exact
shared-vector dual certificate. The other fourteen form the local domain for
the next step. Their original records are
`MIXED_SIX_v24_low5_badnone.json` in the completed first-hour directory, with new
duals in this directory's `MIXED_SIX_JOINT.json`.

### 3. Every nonunit high pair is strict

Take $x,y\in Q$ with $c=\lambda(x,y)\ge2$. For $c\ge5$, the direct two-high
bounds in `STRONG_SEVEN_PAIR.json` are strict.

It remains to consider $c=2,3,4$. If either separate one-high profile is already
strict, use it. Otherwise start with one of the fourteen first-high profiles.
The edges containing $y$ and meeting $L$ partition the five low labels into
positive old traces; these traces may also contain $x$. If $b$ of those chosen
traces contain $x$, promote a further $c-b$ copies of the old singleton-$x$
trace. Restore degree seven at $y$ by adding singleton-$y$ edges and subtract
the same number from the old empty count. Negative-count choices are discarded.

Every actual input arises from this construction: unit low incidences determine
the partition, and $c$ determines the remaining $x,y$ incidences. Discard an
input only when the other one-high projection is one of the three known strict
profiles.

The complete generation has $1697$ labelled extension entries, of which $26$
have a known-good other projection. The remaining entries have $377$ orbits
under permutations of the five lows and interchange of the two highs. Exact
position bounds are strict for $371$; the six remaining profiles all have
$c=2$, and all six have strict repaired rational shared-vector dual bounds.

`FIVE_LOW_NONUNIT_HIGH.json` stores the complete local domain and direct
witnesses; `FIVE_LOW_NONUNIT_HIGH_JOINT.json` stores the six strict duals.
Independent A/B/C, both pair directions, actual-slot inventory, avoided quotas,
and capacity penalties are replayed in
`FIVE_LOW_NONUNIT_HIGH_JOINT_INDEPENDENT.json`. Full generation and projection
binding are checked in `FIVE_LOW_NONUNIT_HIGH_COVERAGE.json`. The old two direct
one-high witnesses were independently replayed as part of this binding audit.

### 4. Return from all-unit highs

If any high pair in $Q$ is nonunit, Step 3 gives a coloring. Otherwise choose
four distinct vertices of $Q$. Together with $L$, they form nine pairwise-unit
locks of degrees $6^5 7^4$.

The general nine-lock criterion applies on at most $25$ vertices. Its proof pads
with isolated vertices and uses only the selected degrees and pair codegrees;
its total/pure link-overlap quotas do not require global pair covering. The
complete $q=5$ table gives a strict bound for every such actual profile, with
maximum $12869/12870$. Thus $H$ is properly two-colorable.
$\square$

## Scope and remaining work

This completes the five-low paper branch, and together with the earlier six-or-
more-low candidate leaves only one through four low vertices at $24$ vertices
(the no-low case was completed earlier). The isolated-padding step must call
the general conditional nine-lock lemma, not the pair-covering 25-vertex theorem
directly. Every new selection, local coverage and certificate must still be
connected in Lean.
