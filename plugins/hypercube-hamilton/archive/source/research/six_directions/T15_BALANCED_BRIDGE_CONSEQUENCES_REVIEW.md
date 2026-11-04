# Four balanced-bridge cores: independent geometry consequences

Verdict: **PASS**, `same-family / provisional`. The new geometry accounting
is independently reproduced from the three raw
`remaining_eight_after_single_face_{1,7,31}.bin` inputs. No author checker
or producer is imported. Reviewer configuration is `gpt-6.1-sol / high`,
fresh review context `fork_turns=none`; the original four-core proof review
remains unchanged. All its audited input hashes were rechecked.

| Target | Input configurations | Newly covered | Remaining |
|---|---:|---:|---:|
| 1 | 9385 | 3180 | 6205 |
| 7 | 11663 | 4428 | 7235 |
| 31 | 12590 | 4680 | 7910 |
| Total | 33638 | 12288 | 21350 |

The independent script reconstructed **94779 eligible coordinate
projections**, and obtained 21300 remaining configurations with an a2b1
projection and 50 without one. It verified each of the three new binary
files by exact byte equality with its independently filtered sequence;
all 21350 saved candidate rows were independently reconstructed and
compared as well.

## Reconstruction and hypotheses

For every seven-byte raw record I checked canonical ordering, distinct
holes including the implicit hole 0, target distinct from the holes,
six-bit range, the stated even Z/odd W parity, and the preprocessed Z-W
nonadjacency condition. I checked every coordinate, including the absence
of an a1b4 coordinate already closed by the preceding stage.

For each cut having exactly two Z holes and one W hole in the target's
face, let q be the other Z hole. Mirror the two same-face Z holes across
the cut, then translate by q and explicitly extract the five retained
coordinates. The mirrored Z holes become the two marked avoided majority
holes; the three opposite-face W holes become the included majority
holes, while q is the normalized minority hole 0. This is an actual cube
map; the marked avoidance roles are retained. Each projected label was
checked odd. The core lookup was independently reconstructed from the
representatives and all 120 five-coordinate permutations, using the
inverse permutation convention from the producer. Overlapping lookup
entries were required to give the same core index. No saved core-map
JSON was used to obtain choices.

Every raw record has no choice in the previously closed set
{13,14,19,31,32,35,37,38}. I classified it as newly covered precisely when
at least one independently obtained choice lies in {2,7,10,44}. Counting
records once handles multiple qualifying cuts without double counting.

The deduction of new coverage imports the previously accepted geometric
projection reduction and old eight-core theorem; this appendix does not
re-audit those results. The additional four-core theorem was separately
audited in `T15_BALANCED_BRIDGE_REVIEW.md`; its full arbitrary-matching
quantifier makes a geometry choice sufficient for every realizable
matching in that geometry. The appendix's counts are **normalized marked
hole configurations**, not matching counts or certificates that every raw
configuration is realized by a surviving matching.

## Minimum additional orbit cover

For the remaining **21300 configurations having an a2b1 projection**, the
minimum number of additional complete T15 core orbits sufficient through
these reconstructed choices is exactly **10**. This is a finite hitting
set statement for these projection choices, not a lower bound on all
possible proof methods.

The singleton choice patterns force the nine distinct cores
{0,1,4,5,8,15,23,24,27}. Remove every pattern already meeting this set.
The remaining constraints are exactly

- {18,26};
- {21,26};
- {25,26}.

All three are disjoint from the nine forced cores. Consequently at least
one more core is necessary, proving the lower bound 10. Their common
intersection is {26}, so choosing 26 covers every remaining constraint
and achieves the bound. The sufficient set is therefore
**{0,1,4,5,8,15,23,24,26,27}**; it is the unique minimum-cardinality set
within this finite choice-cover problem. The 50 configurations without
an a2b1 projection are outside this cover statement and remain separate
obligations.

## Reproducibility and limits

Run `python T15_BALANCED_BRIDGE_CONSEQUENCES_check.py`. Its JSON includes
every source/result hash, all pattern multiplicities, per-core projection
counts, the forced cores and residual constraint group. It writes only
its own JSON. Producer metadata are compared only after independent
reconstruction. Existing four-core proof, review, checker, and checker
result hashes were checked unchanged before completion.

This appendix neither modifies a global state file nor claims full T15,
the complete eight-hole layer, P6, or matching realizability. No issue was
found in the stated geometry counts or the restricted minimum-cover claim.
