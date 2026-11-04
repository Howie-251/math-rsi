# A6 consequences and state accounting: independent check

Date: 2026-11-01. Verdict: **PASS**, relative to the previously audited proof
packages. Review independence: same-family; acceptance status: provisional.
This check does not revise the already hashed A6 main audit or its proof.

The current `A6_AND_EIGHT_FREE_CLOSED.md` accurately states arbitrary K(Q5)
A6, universal balanced six-hole K6, G6-local, and the complete Q6 eight-hole
FREE-target consequence. It explicitly retains R8-covered and the full
10,12,14,16,18-hole obligations. It preserves the distinction between a union
of optional edges over cycles and simultaneously prescribing those edges.
The manifest proof hash and all three review-report hashes were recomputed
and agree with the actual files and the current state records.

The old sample account was independently recomputed without importing or
running `account_samples_after_a6.py`. For each of the 187 input records,
the check verifies a 28-edge short matching, 56 distinct covered vertices,
a free root, an opposite-parity target, and preservation of every original
record field in the output. It independently normalizes the root, computes
all six target-side (a,b) rows and compares every saved good-cut list and
classification. The result is exactly **169 covered good-cut cases plus
18 FREE-target cases = 187**. No source record is omitted or added; source
SHA256 agrees. `remaining_samples_after_a6.json` correctly has zero historical
sample residuals and explicitly sets full_eight_hole_proved=false and
full_p6_proved=false. The requested output artifact is
`remaining_samples_after_a6.json`; there is no separate
`account_samples_after_a6.json`, which the script neither promises nor needs.

The new 66127/1498 numbers have the correct limited meaning. The geometry
census records 19530+22472+24125=66127 hole configurations for normalized
covered targets 1,7,31, with 278+875+345=1498 target-stabilizer coordinate
orbits. Orbit-list lengths and sums of orbit sizes agree, as do the three
binary record sizes (seven bytes per geometry). Its independent check's
three source hashes agree. This follow-up checks aggregate consistency and
scope; it does not claim to have rerun that complete census. Neither number
counts required matchings or certifies matching realizability. The new
consequence document, NEXT_OBLIGATIONS top and PROOF_PACKAGE top all state
this limitation and do not claim Hamilton extension for R8-covered.

RUN_STATE.json and PROOF_CHECK_STATE.json both set A6/K6/G6-local and all
eight-hole free targets true, and **full_eight_hole_proved=false,
full_p6_proved=false**. Their retained full-P6 hole levels are
8,10,12,14,16,18, with eight holes limited to R8-covered. The top-level global
status remains NOT_CURRENTLY_JUSTIFIED. Old sample count zero is explicitly
labelled sample-only and is not substituted for a universal proof.

During the check, four unlabelled stale exploration descriptions were found
in RUN_STATE (A6/A4/E3 still described as open). The parent corrected the
current_exploration object, six_hole_next_reduction and
a4_edge_elimination_reduction; their final versions were reread and match
the accepted current status. No unresolved issue remains. The apparent
Chinese encoding problem in an early terminal display was also checked:
NEXT_OBLIGATIONS contains valid Chinese Unicode and zero U+FFFD replacement
characters. It was a display issue, not file corruption.

`A6_CONSEQUENCES_STATE_REVIEW.json` records hashes of the final files checked.
Historical prose below explicitly dated/latest-status headers is not being
promoted to a current proof claim. The remaining work remains mathematical:
R8-covered and the higher hole layers are unproved.
