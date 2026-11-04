# Complete twelve-hole Q6 theorem for two prescribed free endpoints

2026-11-01. ARIS proof-writer assembly. Status: PROVABLE AS STATED
relative to the explicitly listed accepted imports and the final actual
application review. Independent assembly review pending.

## Exact theorem

For every short matching M of Q6 with exactly 26 edges (twelve uncovered
vertices), and every two prescribed uncovered vertices u,v of opposite
parity, Q6 has a Hamilton u--v path containing every edge of M.
All path edges are cube edges. This theorem requires BOTH endpoints free.
It does not assert the twelve-hole covered-target branch or complete P6.

## Dependency map

1. `TEN_HOLE_FULL_CLOSURE.md` / `TEN_HOLE_FULL_REVIEW.json`: complete
   preceding ten-hole theorem, including covered opposite targets.
2. `HIGHER_Q5_FULL_NEARBALANCED.md` / `HIGHER_Q5_FULL_REVIEW.json`:
   predecessor reduction, near-balanced cut theorem and exact normalized
   residual domains. Only its twelve-hole part is used here.
3. `HIGHER_Q5_FULL_REUSE_PROOF.md` /
   `HIGHER_Q5_FULL_REUSE_REVIEW.json`: accepted marked local inputs and
   exact further residual, including all free-target quantifiers.
4. `HIGHER_Q5_FULL_T37_APPLICATION.md` /
   `HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json`: actual free residuals
   covered by either of two independently applicable routes. The T37
   route imports `Q5_T37_INDEPENDENT_REVIEW.json`; the forced T17 route
   imports `Q5_T17_RANK_BATCH_REVIEW.json` and
   `HIGHER_FORCED_CHERRY_REVIEW.json`.

All finite sets below are over-domains of hole geometries: no exclusion
for non-realizability by a short matching is used. Every successful
geometry transfers uniformly for every realizing original short matching.
Completion pairings may depend on that matching. None of these inputs
depends on the desired complete twelve-hole theorem.

## Step 1: remove adjacent free holes using the full preceding layer

Suppose two holes x,y are adjacent. Add xy to M, obtaining a short
27-edge matching. If xy differs from uv, at least one of u,v stays free.
Use that endpoint as the root in the complete ten-hole theorem and the
other as target. Reverse the resulting Hamilton path if necessary. The
path contains M and has the prescribed endpoints; its extra xy is short.

If xy=uv, choose another free root r of the augmented matching and any
cube neighbor s of r. There are ten free vertices after augmentation,
so r exists and is distinct from u,v. The full ten-hole theorem supplies
a Hamilton r--s path containing M and uv. The edge rs is not already in
this 64-vertex path, because it joins its two endpoints. Add rs to form
a Hamilton cycle, then delete uv. The resulting Hamilton u--v path
contains M. Neither the deleted uv nor rs was an original required edge
incident to a free vertex.

It therefore remains to treat matchings whose entire twelve-hole set
is independent. This step genuinely uses the full ten-hole theorem,
including its covered-target quantifier when needed.

## Step 2: normalize all independent geometries

Translate u to zero and permute coordinates. Its opposite-parity target
has odd Hamming weight 1,3 or5 and can be normalized to v=1,7 or31.
Translation and permutation preserve short edges and matchings; a final
path transports back to the original prescribed endpoints. Write the
hole set as {0} union Z union W, with five nonzero even vertices Z and
six odd vertices W, and v in W. Because the holes are independent,
the v=1 case cannot occur here.

For each actual target-oriented coordinate face A, put
a=|Z intersect A| and b=|W intersect A|. The accepted near-balanced
theorem covers b-a in {0,1,2} with b>=1. In its odd-source row the source
must avoid v and the root mirror; full-hole independence excludes the
root mirror from W, so a legal source exists. All target/omission
conditions are part of the imported theorem, not an endpoint relaxation.

The independently exhaustive normalized census leaves precisely the
following free records after these cuts:

| normalized target | near-balanced residual | after accepted reuse | after final application |
|---:|---:|---:|---:|
|1|0|0|0|
|7|80622|27|0|
|31|107984|20|0|
|total|188606|47|0|

The first column is the exact remaining set in
`HIGHER_Q5_FULL_residual_h12_v{1,7,31}_free.bin`, not a random sample.

## Step 3: accepted reuse and the forty-seven final witnesses

The accepted reuse application checks all records against its precise
already accepted marked local registry and multi-source transfer. Its
success witnesses and remaining files partition the input in original
order. The only remaining free records are the 27 and20 above, in
`HIGHER_Q5_FULL_reuse_remaining_h12_v{7,31}_free.bin`.

For EACH of these47 records, the final application supplies both:

- a legal two-source T37 cut whose actual marked (holes,omissions) is
  a common automorphic image of one of the55 accepted full-rank inputs;
- a legal three-source forced-T17 cut whose actual obstruction pair
  excludes the global root, satisfying the accepted generic safe-transfer
  theorem and one of the seven accepted conditional local classifications.

Either route alone suffices. Neither assumes an unrestricted T37 or
ignores a forbidden artificial matching edge. In the T37 route the
local theorem quantifies over every compressed required matching. In
the forced route the accepted completion construction proves that the
ACTUAL compressed matching avoids the forbidden pair. The source sets
exclude the prescribed free target and root mirror as required. Both
routes preserve every original edge and the tag deletion restores exactly
the prescribed Hamilton u--v endpoints. The c=0 branch is covered by
the explicit accepted five-direction import in the transfer theorem.

The final three free residual files are empty, and the application
review verifies exact record sets and witnesses, not merely counts.
Thus every independent free-endpoint geometry has been covered. Together
with Step1 and the reversible normalization this proves the theorem.

## Scope of closure

The complete twelve-hole FREE-target theorem follows once the final
application and this assembly receive independent PASS. The covered-target
branch remains OPEN; the combined application still leaves215243 covered
geometries. In particular this free-endpoint theorem cannot serve as the
full predecessor theorem required for all fourteen-hole reductions.
Complete twelve/fourteen/sixteen/eighteen-hole P6 layers and full P6 remain
OPEN. Acceptance is relative to explicit literature imports and exact
finite certificates, same-family/provisional and not formal verification.
