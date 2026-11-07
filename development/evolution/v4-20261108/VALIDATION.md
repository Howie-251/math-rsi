# Bounded v4 integration validation — 2026-11-08

PASS for the checks below. Implementation files were read-only during this validation; only this report and `validation.json` were written. No fresh whole-problem, Lean, BFS, browser or solver run.

| Check | Actual result and coverage |
| --- | --- |
| `git diff --check` | exit 0; tracked working-tree diff whitespace checks. It does not check the contents of untracked files. |
| `python3 tools/check_links.py` | exit 0; **124 documents / 1869 local link targets / 0 missing**. The existing helper checks maintained root/examples/case landing/docs/MCP/MathRSI-native skills/plugin curated docs and aliases. It excludes original archive documents and embedded ARIS resource closure; checks existence, not anchors, remote URLs or proof validity. |
| Changed/new curated Markdown relative links | **35 documents / 620 local relative file targets / 0 missing**. Input is tracked changed plus untracked Markdown under native base, plugins, docs, root and this evolution record. Excluded archive originals, homepage history, original case studies, deliverables, raw review replies and usage outputs. Fenced/code/math text, anchors, remote URLs and absolute paths excluded. Exact file list and checks are in validation.json. |
| Entrypoints | **10 native base skills / 6 domain directories / 14 domain skills**. Each of the 24 skill entries exists at its source and resolves through both `.agents/skills` and `.claude/skills`: **48 aliases valid**. |
| HE new Python | `plugins/happy-ending/tools/check_strategy_examples.py` parsed with `ast.parse`: PASS. Syntax only; not executed again. |
| ARIS embedded resources | `git status --porcelain --untracked-files=all -- base/skills`, excluding native `mathrsi-*`, reports **no changed or new embedded ARIS paths**. This is Git worktree coverage, not a separate byte-by-byte upstream audit. |
| Branch / preserved v3 | Current branch **feat/v4-evidence-20261108**. `v3` tag object `ced9921c734faf342e09c969f841c85957cfd6e1`, peeled commit `44130fd0` (PR8 merge). Validation used read-only Git commands and did not move tags/branch. No before/after external tag mutation audit claimed. |

## Consumed actual usage evidence

Read the six JSON result/resource files already present under `usage/`; did not rerun their computations. DD `RESULT.json` records exit0 finite-edit replay of ten graphs 2558–2567 and current literal size/simple/degree10 readback, with search/BFS/Lean and accepted-original comparison all false. DD source-copy receipt has 30 byte-equal source files and curated links no missing.

HE `strategy-examples.json` records two fixed abstract counterexamples, 11/10 vertices, 2036/1013 increasing subsets checked. It rejects the stated strategy implications; it is not a universal upper-bound proof. `resource-check.json` records 65 curated links with no broken links, 303 copied-source files without byte mismatches, two domain skills and Python syntax pass. `lower25.json` records a fresh earlier check of one 25-vertex abstract coloring: all 2300 triples/12650 packets, 300 outer pairs, 35-state catalogue, 25 occupied states and e=m=9, all checks true. Its scope is lower25 only, not upper25, coordinate realizability or the later ES(7) upper bound. This validation only read that existing result.

## Not covered

No independent mathematical reacceptance, remote priority check, full Lean source reconstruction, all-root BFS rerun, copied-original archive navigation repair, remote URL fetch, image rendering, HTML/browser regression, embedded ARIS full resource-closure smoke or new reviewer session. Prior original receipts and reviewers keep their recorded scopes; HE upper-bound manuscripts and DD final formal C retain their declared limitations. Existing unrelated uncommitted homepage, case-study, deliverable and AGENTS changes were not edited by this validator.
