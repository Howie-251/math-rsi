# 23 vertices, two six-degree vertices

The shared maximum pair-budget high catalogue (3 on pairs 01 and 23, 1 elsewhere)
has passed a direct Lean kernel check. It contains 55 labelled high families and
covers the entire 16-Boolean domain. The theorem depends only on the standard
three axioms. Its normal Lake build is in progress.

The 208 representative profiles have been regenerated from the original 204
baseline successes and four refined replacements (groups 56,57,58,64). All
records were independently recomputed with actual ordered-weight capacities and
two avoided-lock quotas per center. The tightest resulting bound is 7292/7293.
The nine budget pairs have 412 admissible labelled inputs; each has an explicit
color-preserving permutation to a saved representative. Python generation is
not the proof of completeness: `TwentyThreeTwoLowCatalog.lean` checks the finite
map against the kernel-verified high catalogue.

`TwentyThreeTwoLowData.lean` has passed direct Lean. Its first normal build hit
an elaboration heartbeat limit on the large ABC literal; the limit was raised
locally, and the direct retry succeeded. This was not a failed inequality.
Facts, representative mapping, and numeric proofs are being compiled.
`TwentyThreeTwoLowComplete.lean` contains the actual-H chain from exactly two
six-degree vertices to Property B, but is not yet validated; do not report the
branch complete until its build and import audit pass.

Update: the shared 55-type catalogue normal build passed (537 seconds).
`TwentyThreeTwoLowCatalog.classify` has passed direct Lean and uses only the
standard three axioms, completing the full nine-budget representative map.
The exact-two-low selection and actual high-type interface also passed an
isolated probe with the final probability implication as an explicit input.
Facts and Numeric are still being checked; neither probe nor the classifier
alone completes the PB branch.

2026-10-13 14:52: Complete direct build and separate ImportAudit both returned
exit 0. The exact original branch type and standard three transitive axioms
are printed in import-audit.log. REPORT.md is the current completed-branch
record; earlier in-progress statements above are historical. Normal managed
build of the final chain is pending scheduling, not a missing logical input.

2026-10-13 15:26: the normal final build returned exit 0 (1018 jobs), followed
by another independent import audit, also exit 0, exact branch type and standard
three axioms. See final-build.log and import-audit-final.log. No TwoLow job remains.
