ARIS's proof skills can develop and review prose arguments, but do not provide a dedicated path from the original mathematical claim to an assembled, checked Lean theorem. This adds `lean-formalize` for both Claude Code and Codex: develop the proof, connect actual inputs to intermediate lemmas, verify the original exported target and its transitive axioms, and provide a reproducible handoff.

The skill activates when the user requests Lean, when continuing a Lean project, or when formal verification addresses a concrete proof obligation. Ordinary derivations and short proofs remain in the existing workflow. Five paired entry points (`proof-writer`, `proof-checker`, `proof-orchestrator`, `formula-derivation`, and `research-pipeline`) delegate scoped work and retain the caller's original proof/audit responsibilities.

The two hosts share references for Lean implementation, adversarial statement/argument/final-assembly review, and verification/handoff. Host adapters preserve Claude→Codex and Codex→configured cross-family routes, distinguish direct consultations from reviewer overlays, and return partial results without upgrading them to a proof of the whole claim. The skill is included in the `theory` installation group; catalogs and live counts are synchronized to 84.

Validation:
- Latest PR CI passed on Linux (761 tests + 44 subtests) and macOS (765 tests + 44 subtests); inventory and helper checks also passed.
- Skill inventory check and 57 existing mirror, grouping, selective-install, and Codex install/update tests passed.
- Four temporary theory-group installations (Claude, Codex, Codex+Claude overlay, Codex+Gemini overlay) preserved the new skill's references and shared references.
- Codex skill validator, both hosts' YAML/package checks, local Markdown links, and `git diff --check` passed.
- Helper lint reported only an existing advisory in the unchanged `research-wiki` skill.

Read-only cross-family instruction reviews completed with Grok (`grok-4.7-build`, xhigh) and Antigravity/Gemini (CLI-selected `gemini-3.8-flash-high`, high); both returned Ready for the inspected integration. Runtime/test evidence above comes from the executed checks, separately from those content reviews.
