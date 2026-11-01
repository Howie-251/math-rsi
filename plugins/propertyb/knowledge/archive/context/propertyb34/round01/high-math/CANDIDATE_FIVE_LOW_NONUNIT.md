# Five low vertices with a nonunit pair at 24 vertices

## Claim and status

Let $H$ be a pair-covering simple five-uniform hypergraph on $24$ vertices with
$34$ edges. Suppose exactly five vertices have degree six and some pair among
them has codegree greater than one. Then $H$ has Property B.

**PROVABLE AS STATED**, as a complete paper candidate with exact local
certificates and independent arithmetic replay. Lean and cross-family review
are separate root-owned steps.

## Assumptions and notation

Let $L$ be the five low vertices. Each low has codegree excess one, so its
exceptional partner is unique and has codegree two. Thus the nonunit graph on
$L$ is a matching of size $m=1$ or $m=2$.

The proof uses the previous complete six-lock pair-budget generator, its direct
certificates, and the new shared-actual-vector dual certificates. When one high
still leaves a residual profile, a second actual high gives a strict bound.

## 1. Actual high-lock selection

If $t$ counts degree-seven vertices, the degree sum implies
$$170\ge6\cdot5+7t+8(19-t)=182-t,$$
so $t\ge12$. Delete the at most five exceptional partners of the lows. At least
seven degree-seven vertices remain; each is unit with every vertex of $L$.

Choose one such vertex $x$. Its codegree excess is five, so at most five of the
other six or more usable highs are nonunit with it. Consequently a second
usable high $y$ exists with $\lambda(x,y)=1$. Both are unit with all of $L$.

## 2. One high lock and the complete local domain

The six-lock degree vector is $6^5 7$. Its pair budgets are one everywhere
except the $m$ disjoint low pairs, which have budget two. The first-uncovered-pair
recursion subtracts one from every pair of a proposed trace of size two through
five, choosing only nonnegative residual budgets. This covers every actual
multi-trace multiset: follow a true remaining trace containing the first
uncovered pair. Singleton and empty counts are restored from the degrees and
$34$ edges, and negative counts are discarded.

For $m=2$, the complete domain has $611$ labelled inputs / $142$ colored orbits.
The previous direct witnesses handle $105$; the new exact shared-vector duals
handle the remaining $37$. Thus this entire case is strict.

For $m=1$, the complete domain has $467$ labelled inputs / $84$ colored orbits.
Direct witnesses handle $44$, and the new duals handle another $37$. The three
remaining orbit IDs are $33,34,65$.

All previous direct witnesses used here have now received independent expanded
stub / injection A/B/C replay, recorded in `FIVE_LOW_OLD_STRICT_REPLAY.json`.
The new duals are included in `MIXED_SIX_JOINT_INDEPENDENT.json`. Their slot
inventories fix each low's unique actual bad pair, which is forced to contain
the internal partner for the paired lows; total and avoided quotas at other
centers are applied to a shared actual bad-count vector across layouts.

## 3. The second high removes all three residues

For an actual first-high residue, the old six-lock traces of edges containing
$y$ partition the six old locks, since $y$ is unit with all of them. Promote each
chosen positive old trace of size at most four, subtract one old copy, restore
the new singleton count from degree seven, and decrease the empty count by the
same amount. This is exhaustive even when an old trace has multiplicity two:
the partition can use only one of its copies because every new-old pair occurs
once.

If the separate $L\cup\{y\}$ projection is already strict in Step 2, use it.
Otherwise the complete extension domains reduce as follows:

| First-high residue | Complete extensions | Good other projection | Remaining strict seven-lock inputs |
|---:|---:|---:|---:|
| 33 | 42 | 41 | 1 |
| 34 | 37 | 31 | 6 |
| 65 | 23 | 22 | 1 |

Every one of the eight remaining inputs has an exact strict position bound;
the maximum is $4779/4862$. Their actual counts, positions and independent A/B/C
replay are in `FIVE_LOW_ONE_BAD_EXTENSION.json`. Regeneration and binding of
every discarded projection to its existing strict certificate pass in
`FIVE_LOW_ONE_BAD_COVERAGE.json`.

## 4. Conclusion

Every actual low matching and selected high profile is covered by a strict
bound, either before or after adding $y$. The usual finite conditional
permutation argument therefore yields a proper two-coloring of $H$.
$\square$

This does not address five lows that are all pairwise unit. Together with the
six-or-more-low candidate, it further restricts the remaining 24-point
mathematics but does not close the whole 24-point branch.
