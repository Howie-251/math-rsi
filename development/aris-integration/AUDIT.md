# ARIS integration source audit — 2026-11-01

Read-only source audit; this document is the only authored artifact. No installation, model call, source-project mutation or commit was performed. Source: `/Users/rfy_naiveai/Desktop/aris_main`, HEAD `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`. Its untracked user files are unrelated and must not enter the snapshot.

## Decision

The user's correction requires actual complete ARIS skill implementations inside MathRSI. Use a **bounded vendored snapshot**, preserving upstream structure, such as `vendor/aris/skills/<selected-name>/`, `vendor/aris/skills/skills-codex/<selected-name>/`, both `shared-references/` trees, and the helpers those skills use. This is self-contained and requires neither another local repository nor a submodule checkout. Preserve the upstream LICENSE and source revision notice. Whole selected skill directories must be copied, including resources; tiny rewritten SKILL.md dispatchers are not a replacement.

For agent discovery, repository-relative symlinks may point `.agents/skills/<name>` to `../../vendor/aris/skills/skills-codex/<name>` and `.claude/skills/<name>` to `../../vendor/aris/skills/<name>`. Their containing directories are two levels below MathRSI's root. These are internal links to actual in-repository source, not dependencies on `/Users/.../aris_main`. If the intended public structure puts the real Codex skills under `base/skills/`, full copies there are also valid, but their two reference layouts must remain resolvable as described below. Prefer one canonical copy per host and internal aliases rather than duplicate edited implementations.

Do not invoke upstream installers for this integration: they create absolute links and write a global pointer. Explicitly set `ARIS_REPO` to the vendored snapshot in the same shell as each helper invocation, from the task workspace. This uses ARIS's existing first helper lookup and avoids a replacement runtime. Task outputs/wiki stay in the task workspace.

## Selected skills and dependencies

A useful direct selection is these **14** skills:

```
research-lit research-wiki wiki-enrich formula-derivation
proof-writer proof-checker proof-orchestrator research-review
auto-review-loop lean-formalize render-html citation-audit
system-profile novelty-check
```

Their upstream catalog closure adds **result-to-claim** and **training-check**, for **16 actual skills per host**. `tools/skill-groups.tsv` specifies:

- `wiki-enrich -> research-wiki`.
- `proof-checker -> render-html`.
- `citation-audit -> render-html`.
- `auto-review-loop -> result-to-claim,training-check,render-html`.

Do not silently omit the latter two while claiming the complete auto-review-loop contract. They are dependencies because default/conditional training-health and results-to-claims phases live in the original workflow. Installing them does not make them mandatory mathematical proof criteria; MathRSI should explain the original ML-oriented scope and invoke the complete workflow only for tasks where it applies.

`citation-audit` matters for real theorem/import attribution; `system-profile` supports measured computational bottlenecks; `novelty-check` supports literature novelty claims rather than theorem correctness. `research-refine` is optional, not part of the minimal fixed-theorem core: its source explicitly targets implementable foundation-model methods, trainable components, paper contribution and score >=9. `formula-derivation`/`proof-writer`/`research-review` better match proof-route work. Additional research/search/paper skills may be vendored when the user wants them, but should not be advertised as mathematical progress merely because copied. `paper-compile`, `citation-crosscheck`, `analyze-results` are sensible optional additions with their complete source/resources; no hard catalog dependencies for these three.

## Resources that cannot be dropped

Copy the whole chosen directories from **both** main Claude `skills/` and Codex `skills/skills-codex/`:

- `proof-orchestrator/references/`: `dispatch-prompts.md`, `stress-tests.md`, `notation-audit.md`, `deepseek-routing.md`, `proof-audit-rubric.md`, `audit-output-contract.md`. The main Claude directory additionally has `NOTICE.md`; preserve it.
- `lean-formalize/references/`: `adversarial-review.md`, `lean-working-loop.md`, `verification-and-handoff.md`. Codex also has `agents/openai.yaml`.
- `render-html/scripts/render_html.py` and `scripts/templates/academic.html`, `scripts/templates/dashboard.html`, for each host. The helper is skill-local; **there is no `tools/render_html.py` shim**. Templates are not optional.
- Other selected directories currently contain their full SKILL.md only, but copy directories rather than assuming future versions remain one-file.
- `skills/shared-references/`: 32 non-cache files, 345,880 bytes.
- `skills/skills-codex/shared-references/`: 32 non-cache files, 268,377 bytes. The two reference packs differ; do not substitute one for the other.
- `agents/aris-fanout-leaf.md` preserves Claude fan-out instructions used by `research-lit` and `proof-checker`. Upstream installs it as `.claude/agents/aris-fanout-leaf.md`; an internal relative alias to the vendored file can supply that discovery path.
- Upstream LICENSE; a source note identifying revision and selected paths. Exclude `__pycache__`, `.pyc`, original `.git`, local untracked archives and credentials.

## Real path and helper failures

1. A standalone SKILL.md loses the proof-orchestrator and Lean references, and render-html loses its renderer/templates.
2. Most Codex links are `../shared-references/...`, but Codex `auto-review-loop` and `research-refine` also contain `../../shared-references/output-*.md`. Preserving upstream `skills/skills-codex/<name>` plus `skills/shared-references` satisfies both. A flat actual `base/skills/<name>` copy must deliberately supply both `base/skills/shared-references` (Codex) and `base/shared-references` (main) or adjust the references transparently. A lexical link checker should resolve symlink parents before collapsing `..`; otherwise it can report false failures on valid upstream-layout aliases.
3. `research-wiki.py` lives in upstream `tools/`, not the skill directory. It imports sibling `threat_scan.py`; dropping the sibling silently loses its scan. `save_trace.sh` imports sibling `review_gate.py`. Keep sibling layout.
4. `research-lit` actually resolves `arxiv_fetch.py`, `semantic_scholar_fetch.py`, `deepxiv_fetch.py`, `exa_search.py`, `openalex_fetch.py`, and `verify_papers.py`. Copying prose alone does not deliver these capabilities.
5. Reviewer skills resolve `tools/reviewer_route.py`, a parser, not an MCP client. Actual native/MCP reviewer availability still depends on the host. No model services or toolchains are installed by copying skills. Read-only static model review remains distinct from actual Lean execution.
6. Explicit `ARIS_REPO` works when a task workspace is elsewhere than MathRSI and has no MathRSI `.aris` manifest. Otherwise fallback may accidentally pick the author's global install or unrelated `~/.aris/repo` revision.
7. Upstream `render-html --offline` disables CDN assets and leaves raw math delimiters; it does **not** embed rendered offline SVG math. Do not claim the package reproduces the old Property B single-volume offline math rendering from this option alone.

## Helper inclusion

A bounded full upstream `tools/` snapshot is small: **53 non-cache files / 904,661 bytes**. It is acceptable as reused upstream support, with an explicit note that helpers for unselected skills are dormant and some shims target omitted skill implementations. It is not a new MathRSI Python framework. If minimizing copied support, the selected skills directly mention the following functioning helpers:

```
arxiv_fetch.py capture_filter.py copilot_native_evidence.py deepxiv_fetch.py
evidence_check.py exa_search.py openalex_fetch.py research_wiki.py
review_gate.py reviewer_route.py save_trace.sh semantic_scholar_fetch.py
verify_paper_audits.sh verify_papers.py verify_wiki_coverage.sh watchdog.py
```

Add `threat_scan.py` for `research_wiki.py`. Common shared-reference support also references `provenance.py`, `run_state.py`, `iteration_log.py`, and related gates; preserving all `tools/` avoids a brittle incomplete support subset. `openalex_fetch.py` imports third-party `requests`; preserving source does not install that dependency. Other literature helpers and optional integrations have their own actual external requirements. Existing install/update scripts may remain as upstream source, but MathRSI must not run or advertise them as its no-global-write setup path.

## Existing upstream installer behavior (reference only)

Exact existing commands for a **normal separately managed local ARIS install**, not the chosen MathRSI integration:

```bash
bash /path/to/aris/tools/install_aris_codex.sh /path/to/task \
  --aris-repo /path/to/aris --skills research-lit,research-wiki,wiki-enrich,formula-derivation,proof-writer,proof-checker,proof-orchestrator,research-review,auto-review-loop,lean-formalize,render-html,citation-audit,system-profile,novelty-check \
  --quiet --no-doc

bash /path/to/aris/tools/install_aris.sh /path/to/task \
  --platform claude --aris-repo /path/to/aris \
  --skills research-lit,research-wiki,wiki-enrich,formula-derivation,proof-writer,proof-checker,proof-orchestrator,research-review,auto-review-loop,lean-formalize,render-html,citation-audit,system-profile,novelty-check \
  --quiet --no-doc --no-agent-profiles
```

Both accept `--dry-run`, `--reconcile`, `--uninstall`, `--groups`, `--skills`, `--exclude`, `--all`, `--skip-new`, `--add-new`, `--replace-link`. Codex also supports reviewer overlays; do not install them by default, as the base pack already provides selectable reviewers. Claude supports migration/adoption options and `--no-agent-profiles`; Codex does not support that last flag.

Crucial side effects/limitations:

- Fresh `--quiet` with **no selection flags installs all skills**. Always specify `--skills` for a bounded install.
- Catalog hard dependencies expand transitively. Explicitly excluding a required skill warns but still permits the broken combination.
- Both create absolute skill links and absolute `repo_root` manifests; relocating or cloning those generated outputs does not give portable links.
- Both write **`~/.aris/repo`**, even with `--no-doc`; no opt-out flag exists. `--no-doc` suppresses only the managed AGENTS/CLAUDE document block.
- Codex links `.agents/skills`, including its support tree, and does not create `.aris/tools`. Claude links `.claude/skills`, `.aris/tools`, the bounded leaf agent where needed, and potentially Copilot profiles unless disabled.
- `install_aris.sh` platform autodetection can choose Claude when AGENTS.md alone exists; explicit `--platform claude` or direct `install_aris_codex.sh` avoids ambiguity.
- `--reconcile` requires an existing manifest. Manifests preserve installed selections; explicit `--skills` adds selections, and merely rerunning with a shorter list does not necessarily prune old ones.

The self-contained MathRSI snapshot and internal aliases avoid these installer side effects entirely. Verification should resolve all selected SKILL.md and load-bearing resources from a relocated copy with global fallback unavailable, run useful existing helpers against disposable fixtures, and avoid calling real reviewers or starting a research Goal during integration testing.
