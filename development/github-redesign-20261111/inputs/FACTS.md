# README redesign facts — 2026-11-11

Paths below are relative to the repository root; this is a drafting fact sheet, not a new mathematical audit. Read AGENTS, V4_CHANGES, DOMAIN_ROUTING, current homepage app.js and six cards, the linked case/plugin READMEs and QUICKSTART. No archive proof bodies or original research workspace read; no mathematics or historical Goal run.

## Six research threads: strongest stored statement and its exact scope

| Thread | Concise result sentence suitable for the README | Status and source paths |
| --- | --- | --- |
| Property B | Eight individual bounds, m(5…12) ≥ 35, 67, 131, 267, 543, 1112, 2275, 4664, accompany a uniform improvement over the specified RS budget for every k ≥ 12. | End-to-end Lean covers the uniform theorem and earlier m(5) ≥ 33/34; m(5) ≥ 35 is a complete written candidate with incomplete Lean; other individual bounds retain parameter-specific computational/paper checks. `case-studies/property-b/README.md`, `case-studies/property-b/readers/PROPERTY_B_GENERAL_BOUND.html`, `case-studies/property-b/readers/PROPERTY_B_GENERAL_LEAN.html`. |
| ECC | Four exact binary-code distances are d₂(43,10)=16, d₂(44,10)=17, d₂(44,11)=16 and d₂(42,16)=12. | First three follow from the old exclusion plus constructions; 42/16 applies a published 2020 theorem and is not a new-priority claim. 16 ≤ d₂(45,11) ≤ 17 remains open. Lean reductions retain explicit literature/classification/computation premises. `plugins/ecc/README.md`, `plugins/ecc/evidence/IMPLEMENTATION.md`. |
| Degree–diameter | A 2,567-vertex, 10-regular graph of exact diameter four exceeds the Comellas 2,566 entry checked on 2026-11-05. | Actual run: MathRSI v2 + DD + PR #7 handoff repair. Original independent all-roots BFS and Final2567 Lean assembly/import receipts exist; external formal C review incomplete, portable package lacks full rebuildable Lean project. `case-studies/degree-diameter/README.md`, `case-studies/degree-diameter/evidence/execution_version.md`, `case-studies/degree-diameter/reproduce/d10_d4/`. |
| Erdős 86 | An exact certificate gives π_Q(C₄) ≤ 23662061277957791/40000000000000000 < 0.59155154, improving the specified 0.60318 reference. | Asymptotic density, not a bare every-finite-n bound; conjectured 1/2 remains open. Full local replay covers 13,150,453 legal Q₄ completions, with analytic high-dimensional averaging; no Lean, no claim of SDP optimality/current global record. `plugins/hypercube-extremal/README.md`, `plugins/hypercube-extremal/evidence/IMPLEMENTATION.md`. |
| Ruskey–Savage Q₆ | Every matching of Q₆ extends to a Hamilton cycle; imported results also yield extension for matchings using at most six directions in any dimension. | Stronger stored P6 gives a Hamilton path from every free root to every opposite-parity target. Whole-proof audit same-family/provisional, no Lean; bounded replay rebuilds 1024 forests, 1,048,576 connectivity bits and rank 1024, not all large P6 streams. General conjecture remains open. `plugins/hypercube-hamilton/README.md`, `plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md`. |
| Happy Ending | Received working manuscripts claim N(7,6,7) ≤ 75 and N(7,7,7) ≤ 76, hence ES(7) ≤ 77, tightening the prior 76/77/78 draft. | SAME-SESSION / UNREVIEWED / UNACCEPTED structural manuscripts; independent mathematical review pending, no completed Lean. Restricted capacity b25 retains historical SAT scope; a separately checked 25-point abstract witness is not a geometric upper-bound proof. ≤74 applies only to specified subclasses. `case-studies/happy-ending/README.md`, `case-studies/happy-ending/n7-20261103/proofs/READING_GUIDE.md`, `docs/V4_CHANGES.md`. |

## Execution provenance and evolution boundaries

- v0 is the pre-harness research-tools phase, without a Git tag. Property B was researched using ARIS and later distilled into MathRSI; its v1 chart intake is not a v1 discovery or a speedup experiment.
- ECC v0 already had the 172-parent double scan and the first three exact values. The v1/v2-method continuation deepened Lean reductions, actual-matrix connections, portable certificates and the literature-derived 42/16 closure. v3 integrates these as callable tools; it does not add a fifth exact distance.
- The `[72,36,≥16]` A/B/C branching diagram is an ORGANIZATION/TEACHING DEMO, not a newly solved problem or live search. A 35-dimensional self-orthogonal parent covers only specified B/C subdomains. `plugins/ecc/skills/mathrsi-ecc/examples/node-research.md`.
- Earlier DD catalogue results originate in ARIS. The later ten accepted orders 2558–2567 come from the actual v2 + DD run. Displaying the new result at v4 means research feedback into v4, not v4 execution. Catalogue 163 instances / 44 pairs / 49 concrete Lean instances includes intermediate graphs, not 163 new records.
- Erdős 86, Q6 and the older Happy Ending material feed v3; incorporation and bounded new replays do not retroactively make their original mathematics v3 runs.
- Happy Ending 75/76/77 manuscripts feed v4 and remain working proofs. v4 checker use covers two strategy counterexamples and the lower25 witness, not acceptance of the upper-bound chain.
- Fixed v4 is current release; main is recommended v4 plus later maintenance. Global progress reassessment and ECC node research are main maintenance OUTSIDE the fixed v4 tag. No v5 release is claimed. `docs/V4_CHANGES.md`.
- Retain two distinct evolution tracks: shared base behavior and expanding/deepening domain knowledge. No equal-budget performance or long-task success-rate evidence is established.

## Counts and execution structure checked against actual paths

- Ten MathRSI base SKILL.md files exist: research, prepare, specify, survey, route-loop, prove, assemble, verify, handoff, meta-evolve (all prefixed `mathrsi-`, under `base/skills/`). This is not a count of every bundled ARIS skill.
- Five solving stages are prepare → route-loop → prove → verify → handoff. Specify/survey are internal helpers; assemble is invoked within verify as needed; research orchestrates; meta-evolve is separate maintenance. Local verification and incremental literature return to their callers.
- Fourteen direct domain skills exist across six domains: Property B 4, DD 4, ECC 2, hypercube-extremal 1, hypercube-Hamilton 1, Happy Ending 2. Count direct `plugins/*/skills/*/SKILL.md`, excluding archived copies.
- `docs/DOMAIN_ROUTING.md` maps the six domains to the actual caller stages. The two hypercube plugins concern different objects and are not interchangeable.

## Quickstart: real existing entry points, not a new CLI

- Existing clone URL: `https://github.com/lisresearchgroup/math-rsi.git` (private access required).
- Set `MATHRSI_ROOT` to the clone, `ARIS_REPO="$MATHRSI_ROOT/base"`; keep research output in a separate task workspace.
- `codex --add-dir "$TASK_ROOT"` / `claude --add-dir "$TASK_ROOT"` are documented HOST commands, subject to installed host syntax; no `mathrsi run` executable exists or is needed.
- Actual main entry: `base/skills/mathrsi-research/SKILL.md`; `.agents/skills/mathrsi-research` and `.claude/skills/mathrsi-research` are existing relative symlinks. Natural-language instruction to read the absolute skill path works without refreshed aliases.
- Existing bounded replay script: `python3 examples/proof-repair/replay.py`; actual starter files: `examples/proof-repair/starter/REQUEST.md` and `PROOF.tex`. This fact check confirmed file presence, not a new execution.
- Existing wiki helper: `python3 "$ARIS_REPO/tools/research_wiki.py" --help`. Use this clone’s base, not external ~/.aris or author-machine paths.
- Python 3.9+ is QUICKSTART’s baseline for the simple replay/bridges; ECC explicitly needs ≥3.10 and C++17 for its pair replay. Reviewer CLIs/auth, searches, TeX and pinned Lean environments are external dependencies for selected work.

## Present documentation drift to avoid copying

- `docs/QUICKSTART.md:5` calls v3 current; its later evolution paragraph also calls v3 the current increment. Replace navigation prose with v4/current main; retain historical v3 facts.
- `docs/V3_CHANGES.md:3,107` calls v3 current; those are historical release notes, so frame their scope as historical rather than treating them as current authority.
- README’s v3 domain table still says Happy Ending 75/76 awaits source material; manuscripts ARE received, mathematical review still pending. `docs/V3_CHANGES.md:103` has the same old snapshot.
- README’s evolution-image alt text still calls v3 current; the linked figure is a v3 historical diagram. Do not relabel the existing image as a v4 implementation diagram.
- `case-studies/property-b/README.md` says new tasks will evaluate v1 itself; historical provenance is valid, but README-wide current-version onboarding should use the chosen present revision.
- `case-studies/happy-ending/README.md` says packaging does not constitute v4 release: valid packaging-scope disclaimer, not evidence that today’s v4 release is absent.
