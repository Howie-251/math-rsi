# Complete sixteen- and eighteen-hole prescribed-endpoint steps

2026-11-02. ARIS proof-writer final-assembly submission. Every named
pending gate remains an obligation until independently accepted. This
file alone does not change the acceptance ledger.

## Theorems and dependency order

For h=16 and h=18, let M be any short matching in Q6 with exactly h
uncovered vertices. For every u outside V(M) and every v of opposite
parity, including a covered v, there is a Hamilton u-v path containing M.
The16-hole matching has24 edges; the18-hole matching has23 edges.

The full fourteen-hole theorem is imported only after
FOURTEEN_HOLE_FULL_REVIEW has formally passed. This discharges the
predecessor condition in all sixteen-hole reductions. No free-target-only
theorem is substituted for the complete predecessor. Prove16 first and
then apply the already independently accepted implication16=>18.

## Sixteen-hole proof

Normalize u to0 and v to1,7 or31 by a common cube automorphism. The
HIGHER_Q5_FULL_REVIEW reduction at h16 is now unconditional on earlier
open work: its complete14 predecessor has been supplied. It covers all
inputs outside the exact2,472,168 covered-target and42,846 free-target
records. The remaining accepted chain is:

| Gate | Remaining covered | Remaining free |
|---|---:|---:|
| HIGHER_Q5_FULL_REVIEW, h16 | 2472168 | 42846 |
| HIGHER_POST12_REUSE_REVIEW, reuse | 18200 | 0 |
| HIGHER_POST12_REUSE_REVIEW, explicit Hall exclusions | 1211 | 0 |
| HIGHER_POST12_T39_REVIEW | 1012 | 0 |
| SIXTEEN_LOCAL_REVIEW | 148 | 0 |
| union of SIXTEEN_STAR_REVIEW and SIXTEEN_SMALLCUT_REVIEW | 0 | 0 |

Each positive route covers every realizing original short matching.
Each Hall exclusion directly contradicts the existence of the original
matching by a strict covered-neighborhood deficiency. Retained streams
are exact complements in original source order, so an actual unsolved
input passes to the next row without loss of cases.

The last148 records are in the three SIXTEEN_LOCAL_remaining streams.
The root-star construction covers30 target31 records and retains118;
the small-cut construction covers the complementary118 (18 at target7,
100 at target31) and retains those same30. Both reviews establish their
complete arbitrary-matching quantifiers. The final checker must verify
these sets are complementary, by their actual15-byte records and source
indices; adding their counts is not enough.

The root-star argument preserves every original internal-A edge under
maximal completion and restores the actual target mate and endpoints.
The small-cut argument has its own explicitly proved two-source/root-in-B
transfer: it uses a path rather than an intact tagged cycle to avoid
the prescribed same-parity pair. It must not be justified by silently
applying the older three-source hypothesis. Its independently checked
local theorem uses a compulsory original short edge and a conditional
forbidden pair, with both hypotheses verified for every actual input.

Consequently every normalized sixteen-hole input is solved. Undo the
normalization to obtain the required path for the original u,v,M.

## Eighteen-hole proof

HIGHER_POST12_T39_REVIEW independently establishes the exact implication:
the complete sixteen-hole prescribed-endpoint theorem implies the complete
eighteen-hole prescribed-endpoint theorem. The antecedent is the theorem
just proved, including covered targets. Therefore the implication applies.

For clarity, its accepted finite partition is80,805 covered records,
73,605 positive reuse routes,7,050 explicit impossibility certificates,
and150 positive routes using the single universal T39 index54. No free
record remains in its initial reduction. This partition is already
audited; no claim that18 alone implies any smaller hole level is used.

## Required final checks and scope

Final acceptance requires formal PASS and current hash agreement for the
full14 predecessor, higher source/reuse/T39, SIXTEEN_LOCAL, SIXTEEN_STAR
and SIXTEEN_SMALLCUT gates; complete interface equality; the complementary
last148 partition; and an acyclic dependency chain14=>16=>18. It does not
assume P6 or the two target theorems themselves. Combined with the already
accepted lower layers and the rooted18-hole bound, these theorems can be
used in a separate full-P6 assembly. Same-family/provisional audit is not
proof-assistant formalization.
