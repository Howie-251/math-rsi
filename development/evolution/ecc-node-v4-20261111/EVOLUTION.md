# ECC branch placement and homepage explanation — 2026-11-11

## Adopted change

[PR #19](https://github.com/lisresearchgroup/math-rsi/pull/19), contributor head `bbaa8652c4195a31251b47c1bb3532ce61d31df2`, was merged as `52f6f85143478dc6bf9af0e1da8d3b37d5cfb933`. The contributor's authorship is preserved. This is subsequent v4 maintenance on `main`; the fixed v4 tag stays at `e6c9821aebb3e8830717044075b2e8a72035c31c`.

The existing ECC research skill now checks branch placement before an advance, restart, method change or dispatch. A stable mathematical node is distinct from execution attempts. Actual code identity, target distance and coverage determine reuse of exclusions; shared computations have multiple consumers and one task. The certificate skill checks the local result and the coverage required for a parent conclusion. The existing base global-reassessment protocol still decides whether continuing the route is useful. No base skill, scheduler or mathematical result was added.

## Review and bounded checks

- Root read the complete PR diff and checked its relationship to the base protocol. A read-only GPT-6.1 Sol independently checked the algebra and workflow; no substantive issue was found. This is same-family review, not a cross-family approval.
- Root replayed the small algebra example: for `n=6`, `S=span(3,12)`, the 60 vectors outside S split into A=4, B=24 and C=32. Gram ranks are respectively 0 and 2 for A/B; for C the even subcode is S. These are vector counts, not distinct extensions.
- A separate read-only Sol checked all 33 local Markdown link occurrences (15 unique targets) in the seven changed files, including nine added occurrences and three new targets; all resolved in the patched tree. Both skill entry names and frontmatter were checked.
- The first Gemini 4 Argon/high call returned `ERROR` with a five-minute stream idle timeout, not a review. The exact prompt and response are preserved in `GEMINI_PROMPT.md` and `GEMINI_RESPONSE.json`. No approval is inferred from the selected model label.

## Public explanation

The user then requested an expandable method animation in the ECC results card. It explains how the example `[72,36,≥16]` is partitioned, how one parent-code computation serves multiple branches, and why remaining coverage matters. A/B/C are algebraic categories, not solved research branches. A fixed self-orthogonal 35-dimensional parent reaches only hull dimension 34 within B, and only its own even-subcode family within C. A valid original-target witness and a full-domain exclusion have different completion requirements.

The mathematical result blocks and four exact ECC distances are unchanged. The v4 Plugins row separately identifies the ECC maintenance on main. English and Chinese README, capability notes and homepage copy describe the same change. The interactive example is a teaching aid; the actual executable agent instructions remain in the plugin skills and references.

## Gemini design consultation and implementation

The second, specifically scoped design call returned `SUCCESS`, selecting Gemini 4 Argon/high, thread `db8135a1-5011-42bb-a16b-05caeb52c460`. Its full prompt and response are preserved in `GEMINI_DEMO_PROMPT.md` and `GEMINI_DEMO_RESPONSE.json`. Gemini provided the classification-tree/shared-task separation, three-step interaction, exact B/C scope wording and bilingual copy. This is a design consultation grounded in the PR, not an independent acceptance of a new theorem or a completed-code review.

Root and Sol adopted that separation and the short step labels, retained a compact fixed-height panel, and used branch labels to connect the shared task to its consumers. The larger all-visible mockup was not copied: it would overwhelm the narrow results card. The original question stays above the classification tree; the fixed-parent task is shown separately. Playback advances every five seconds and stops on the last step; collapsing or hiding the page pauses it. Users can choose every step and branch directly. Reduced-motion settings remove the transitions.

## Delivery checks

- JavaScript syntax and diff whitespace checks passed.
- Root browser checks at 1440, 390 and 350 px covered both languages, all three steps and all three branches (54 combinations), without page or component overflow or JavaScript errors. Each language retained a constant component height across steps and branches. Language changes preserved the open state and selection; remembered Chinese loaded correctly and switched back to English. Evidence: [browser record](../../homepage-redesign-20261105/checks/ecc-node-20261111/browser.json) and adjacent screenshots.
- Root visually inspected the rendered Chinese shared-task scene. Sol additionally checked real-time playback, collapse/pause and reduced-motion behavior in Chromium; these were local browser checks, not research execution.
- The mathematical result list and timeline counts are unchanged. The website adds an ECC plugin-maintenance note and the teaching example, with 49 demo translation entries (46 new keys) and seven maintenance strings.

No historical mathematical Goal, large scan or Lean build was started.
