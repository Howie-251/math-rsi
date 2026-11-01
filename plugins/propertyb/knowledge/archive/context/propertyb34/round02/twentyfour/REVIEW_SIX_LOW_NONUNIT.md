# Review request: 24 vertices, at least six low vertices, one nonunit low pair

Scope: this branch only. Please attack the actual selection, normalization, and mathematical input binding. Do not treat local exact inequalities as a proof of all 24 vertices or T34. Do not redo unchanged layout searches. Follow HERO: identify substantive mathematical issues; no invented audit work or arbitrary scores.

## Original conditional statement

Let H be a simple 5-uniform hypergraph on 24 vertices, with exactly 34 edges and covering every pair. If H has at least six vertices of degree six and two distinct such vertices have codegree different from one, then H has Property B.

No local profile, certificate, matching labeling or probability bound is an additional premise of the final statement. See `formal/Aris4Math/ThirtyFour/TwentyFourSixLowBadComplete.lean`, `propertyB_of_nonunit_low_pair`.

## Actual selection

For each degree-six vertex x,

    sum_(y != x) (codegree(x,y) - 1) = 4 * 6 - 23 = 1.

All terms are nonnegative. Thus x has one partner of codegree two and all other codegrees are one. Pick a specified nonunit low pair x,y and four more distinct low vertices. The first pair has codegree two; both endpoints have codegree one with all four further points. Any nonunit pairs among those four form a matching. Normalize that matching by a genuine permutation of the four points, then append x,y. This produces exactly the canonical possibilities {01}, {01,23}, {01,23,45}. The exact finite lemma ranges over all 64 graphs on four vertices, with symmetry built into the six-edge encoding.

Sources:

- `TwentyFourSixLowSelection.lean`: `exists_labeled`.
- `TwentyFourSixLowPairPatterns.lean`: `normalize`.
- `TwentyFourMatchingSelection.lean` and the imported T33 low-vertex lemmas.

## Complete local data

For the actual six-label embedding f, `count H f T` counts original edges with exact trace T, preserving multiplicity. The high entries are all 41 subsets of sizes three through five. Every such trace includes a unit pair, since the nonunit pairs form a matching; hence its count is at most one. The actual high counts obey every pair capacity (one, or two on the specified nonunit pairs). `ActualAllocations.mem_enumerate` places this vector into the complete bounded domain.

The three labelled domains have 467, 611 and 787 vectors. Each ordered row contains the exact binary allocation code and one actual permutation with one of 37 + 90 + 54 = 181 profiles. The rows decode to precisely the complete bounded catalogue; this equality is checked once. There is no lookup during the matching checks. `CheapMatch` checks binary counts, equality of the actual nonunit-pair set with the permuted representative nonunit-pair set, and equality of the sparse high-trace sets. No permutation-invariant fingerprint is used as equality. `TwentyFourSixLowBadSparseBridge.cheap_correct` lifts these support equalities to every low upper count and every exact high trace, using `TwentyFourSparseDecode.decode_indicator` and a separate exact check of all 181 representative high supports against their original μ functions.

`TwentyFourPermutation.perm` is a composition of five swaps, so bijectivity is structural. It need not be proved to enumerate every permutation: each actual count vector needs one checked genuine witness. The forward transportation convention is

    count H (sigma.toEmbedding.trans f) T = count H f (T.map sigma.toEmbedding).

`TwentyFourSixLowBadActual.lean` binds the transformed counts back to H. Low upper counts are empty=34, singleton=6 and pair=1/2. High counts together with these upper counts recover every exact trace, including singletons and the empty trace. Traces larger than five are proved zero from uniformity.

## Exact strict inequalities

The 181 layouts and rational quota multipliers are the already saved first-hour certificates, not a new search:

- `context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_bad3.json`
- `.../MIXED_SIX_v24_low6_bad3_12.json`
- `.../MIXED_SIX_v24_low6_bad3_12_48.json`

The exact independent replay gives maximum 48617/48620. Each single-layout certificate includes actual avoided-lock quotas and overlap-capacity penalties. Numeric evaluation is factored through the proved `CachedRows.rows_eq`; its result is translated back to the original A/B/C formula before application of `SingleLayoutApplication.propertyB_of_single_layout`.

Sources: `TwentyFourSixLowBadData.lean`, `TwentyFourSixLowBadNumeric.lean`, `TwentyFourSixLowBad.lean`.

## Questions to answer

1. Does the six-vertex selection really cover every actual low nonunit pair, without assuming six is the total number of low vertices?
2. Does the high-count capacity domain contain every actual trace vector, including repeated original edges with the same trace?
3. Is the relabeling direction correct and is the final recovery of all actual counts justified?
4. Does the final Property B theorem have exactly the premises above, and are the numeric certificates applied to the same actual graph/counts?

Report exact files actually read and whether any commands were run. Pending builds are not passes; model agreement is not Lean verification. This branch does not address the all-unit low case, r=1–5, or complete T34.

## Current new-code validation boundary

Five actual catalogue entries with five or six high blocks passed the bounded pilot, together with the general low/high bridge API (10.21 seconds, 2.26 GB process-group peak). The pilot uses an explicit representative-support-correctness premise; the formal module checks that premise for all 181 original μ functions. Full numeric, domain, row and actual-branch builds are still pending in the parent queue. Exact records are in `sixlow-bad-sparse-pilot-r3.log/json` and `SIX_LOW_BAD_SPARSE_PILOT.json`. Do not report those five rows as full-branch acceptance.
