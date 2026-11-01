# Final portability and usability audit

2026-11-01. Bounded local audit by a fresh Sol reader. **Relocated discovery and maintained documentation links work. Two missing advertised replay inputs were identified, repaired by Root and verified by complete m8/m9 checker runs in the relocated copy. No outstanding portability blocker was found within this audit's stated scope.** This is not a whole-corpus mathematical acceptance.

## Actual relocation result

A fresh temporary `independent-copy/` received the repository tree, preserving relative symlinks, including `docs/`, `development/`, bundled base and Property B archive. Only `.git`, Python caches, `.DS_Store` and this evidence directory were excluded. Copying the archive did not involve reading or revalidating all its mathematical contents.

From that relocated root, `python3 -B tools/check_links.py` exited 0: **41 documents, 781 local link targets, zero missing**. All **73** discovery symlinks resolve to existing paths inside the relocated copy: 36 `.agents/skills` entries, 36 `.claude/skills` entries and the Claude leaf agent. This includes both host-specific `shared-references` aliases. The resolved paths were compared after canonicalization because macOS `/var` resolves through `/private/var`.

Evidence is in [COMMAND_EVIDENCE.json](COMMAND_EVIDENCE.json), [stdout](relocated-check-links.stdout.log) and [stderr](relocated-check-links.stderr.log). The temporary copy path is recorded in the JSON. The checker covers maintained routes and aliases; it deliberately excludes historical archive link closure, anchors and proof validity.

## Concrete findings before repair

The active [checker capability map](../../../plugins/propertyb/skills/mathrsi-propertyb/references/practice/checker-capabilities.md) advertises the m8 and m9 independent checkers. Both scripts are bundled, but their immediate data inputs were absent in the audited source and fresh copy:

|Checker|Missing archive-relative input|First unconditional read|
|---|---|---|
|`context/propertyb-m8-267-20261029/independent/check.py`|`context/propertyb-m8-267-20261029/CERTIFICATE.json`|line 91, before row checking|
|`context/propertyb-m9-543-20261029/independent/check.py`|`context/propertyb-m9-543-20261029/CANDIDATE.json`|line 160, before row checking|

These were concrete incomplete replay resources, rather than a failure of the m6/k12 command examples or skill discovery. Static tracing found only standard-library imports in both checkers, no author numerical-module imports and no author-machine paths. Each reads just the listed JSON and writes `independent/CHECK.json`. The initial JSON evidence preserves the pre-fix snapshot; the completed repair is recorded separately below.

Root copied the original inputs into the source archive and refreshed its inventory. The audit then copied those exact repaired files into the isolated relocation and ran each independent checker once. The original archived checkers/results were not executed or overwritten. Historical independent timings were 9.401 and 30.090 CPU seconds, so each new command had a 65-second timeout. Both exited 0:

|Repair check|Actual result|CPU / wall seconds|
|---|---|---|
|m8, 943130-byte input|2094 exact strict rows, 299 component quota arguments; `PASS_WITH_DECLARED_IMPORTS`|8.862 / 9.142|
|m9, 1355115-byte input|3450 exact matches and strict rows; original domain and decision tree reconstructed; `PASS_WITH_DECLARED_IMPORTS`|27.740 / 28.179|

Actual argv/cwd/timings are in `COMMAND_EVIDENCE.json` under `repair_verification`; [m8 stdout](m8-repair.stdout.log), [m9 stdout](m9-repair.stdout.log), their stderr files and copied `*-repair-CHECK.json` outputs preserve the actual evidence. This accepts the specific repaired replay inputs and their existing independent calculations. It does not expand the mathematical imports or produce a new theorem/Lean result.

The m6, m7, k12, signed and component resources and their direct JSON inputs exist in the relocated tree. The active examples correctly run writing checkers in independent work copies. The component command requires a C++17 compiler if rebuilding the pilot; its documented Python-only alternative consumes the bundled `PILOT.json`. All selected Python checker sources parse successfully. The already-passing m6/m7/k12/signed/component calculations were not repeated.

The k10/11 example explicitly says to extract the full bundled ZIP rather than copy the standalone verifier. The ZIP exists, and its member table contains both `propertyB_k10_k11_verified.py` and the imported `propertyB_k10_k11_certified.py`. Static inspection of those two members found no external file inputs; the only nonstandard dependency is the documented NumPy. Full k10/11 calculations were not run.

The Lean example points to bundled `formal/`, its `leanprover/lean4:v4.24.0` toolchain declaration, fixed manifest, named main modules and independent audit files. Those resources exist after relocation. The guide accurately requires preparing Lean/Mathlib separately; neither a toolchain nor build cache is claimed bundled. Lean was not invoked.

## Current workflow versus historical paths

The maintained Property B skill tree and executable resources inspected do not require `/Users/.../aris_main` or the original `aris4math` workspace. Archive paths in executable examples derive from the current MathRSI root, and the checkers derive inputs from their copied `__file__` locations. All active Markdown routes checked resolve in the fresh tree.

The external-source-path scan found only provenance/scope text in `AGENTS.md` and explicit instructions in `docs/ARIS_REUSE.md` **forbidding** external `~/.aris/repo` fallback. The latter also correctly explains upstream resolver behavior and requires absolute helpers from this bundled base. Original source provenance, historical logs and historical archived author paths remain original records; they are not current runtime instructions. This audit did not certify every unadvertised historical script as independently runnable.

The existing [base relocation smoke result](../../aris-integration/root-smoke/RESULT.json) was read, not rerun: its 207 upstream-file checks and nine offline helper invocations already cover bundled wiki bookkeeping, reviewer route parsing and both render templates. Its declared scope remains local/offline, without paid model, network, Lean or TeX invocation.

## Reading and acceptance scope

Read `AGENTS.md`, `docs/SKILL_ACCEPTANCE.md`, the four active Property B skill entrances, the knowledge README and the command/requirement portions of the five worked examples, checker map, Lean practice and small-k replay section. Read `tools/check_links.py` in full. Traced imports and file input/output boundaries of the named m6/m7/m8/m9/k12, signed and component checkers; inspected the two relevant k10/11 ZIP members. Read existing base smoke JSON and practice replay summary. After the discovered defect, read m8/m9 independent timing/scope passages and executed their repaired checkers in isolation. The broader mathematical reference corpus was searched for executable examples and source-machine paths, not re-audited theorem by theorem.

This accepts the observed relative discovery, current documentation link resolution and the static command/resource facts above. It does not independently accept all archived mathematics, all historical files, all external service readiness, fresh-host Lean builds, new mathematical results, or general RSI speed/quality gains. No research Goal, remote publication, paid model invocation, original Property B/ECC workspace write or global configuration change occurred. All repository writes for this audit are confined to this evidence directory.
