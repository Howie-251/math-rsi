# v3: stronger evidence loops and three new research domains

MathRSI v3 develops the existing v2 implementation through [mathrsi-meta-evolve](../base/skills/mathrsi-meta-evolve/SKILL.md). It retains the five solving workflows, the separate maintenance workflow, and **10 MathRSI base skills**. **v3 is the current release**; `main` follows the recommended version, and the fixed v1/v2 snapshots remain unchanged. Record the actual checked-out revision when starting or handing off a task.

The main contribution is executable domain capability backed by scientific source materials, together with four targeted improvements to how existing workflows consume evidence. The [maintenance record](../development/evolution/v3-20261104/EVOLUTION.md) owns integration and review status. Gemini 4 and Opus 5.5 each completed two rounds of source-based maintenance review. Their concrete fixes, reading scopes and corrections are preserved in the [review disposition](../development/evolution/v3-20261104/reviews/DISPOSITION.md). They did not rerun the mathematical programs.

## How v3 follows the earlier versions

- **v0** names the original Property B and ECC research experience, before the MathRSI repository workflows were extracted; it is a history label, not a repository release tag.
- **v1** established the five solving workflows and initial domain plugins from those projects.
- **v2** added and actually used the separate evolution workflow, absorbed DD, and changed the existing base at its real call sites. Its [change record](V2_CHANGES.md) remains the historical account of that release.
- **v3** retains those workflows, adds the evidence-consumption actions and domain capabilities below, and records their actual bounded use in the [v3 maintenance record](../development/evolution/v3-20261104/EVOLUTION.md).

These versions describe implemented workflow changes and their sources. They do not relabel the archived mathematical results as new-version reruns or establish a measured speedup.

## Four changes inside the existing base

| Research issue | Implemented action | Existing skill that owns it |
| --- | --- | --- |
| A candidate looks good on an active working set but violates the full domain. | Keep working-set, full-domain, exploration-best and accepted-best values distinct. Return an actual violating input to candidate generation; recheck the final exact object before replacing accepted evidence. | [route-loop](../base/skills/mathrsi-route-loop/SKILL.md), [verify](../base/skills/mathrsi-verify/SKILL.md), [handoff](../base/skills/mathrsi-handoff/SKILL.md) |
| A symmetry, completion or contraction changes the meaning of a root, target or required edge. | Transport all marked data through the same map, compose the maps, and recover original partners and required edges at the actual caller. | [prove](../base/skills/mathrsi-prove/SKILL.md), verify |
| The remaining universal input family is too large for direct enumeration. | Ask the domain for a proved finite rank/basis/coverage mechanism. If a sufficient gate fails, retain legal objects for a different positive-certificate interface. | route-loop, prove |
| A Lean export has standard axioms but still accepts external mathematical premises. | Read every explicit theorem parameter and unfold its definitions; distinguish kernel-proved reductions and actual data from literature, classification or scan assumptions. | verify, handoff |

These additions extend existing paragraphs and return paths. They do not create a second orchestrator, require every task to use ranks, or replace mathematical judgment with a universal score. The [base change report](../development/evolution/v3-20261104/base/BASE_CHANGES.md), [actual use](../development/evolution/v3-20261104/base/USE.md) and [results](../development/evolution/v3-20261104/base/USE_RESULTS.json) connect each change to a real source example.

## Six domains using the same five workflows

Property B and degree–diameter retain their established capabilities. ECC is upgraded within its existing plugin; three new domains are added.

| Domain | New usable capability | Scientific assets and actual checks |
| --- | --- | --- |
| [ECC](../plugins/ecc/skills/mathrsi-ecc/SKILL.md) and [ecc-certificate](../plugins/ecc/skills/ecc-certificate/SKILL.md) | Binary linear-code construction/exclusion, common-coordinate reductions and coset/pair constraints; separate actual-matrix acceptance from whole-domain exclusion and inspect both Lean projects' explicit premises. | Matrices, 172 parents and saved sets, source checkers/scanners, two Lean reduction projects, papers and one complete parent pair stream. [Implementation](../plugins/ecc/evidence/IMPLEMENTATION.md). |
| [Hypercube extremal](../plugins/hypercube-extremal/README.md) | Common Q4 completions, synchronised rooted flags, full-domain separation, exact integer Gram PSD certificates and the high-dimensional averaging bridge. | Final certificate, keys and complete geometric checker, mathematical reports and search/failure histories. [Full finite-domain replay](../plugins/hypercube-extremal/evidence/IMPLEMENTATION.md). |
| [Hypercube Hamilton extension](../plugins/hypercube-hamilton/README.md) | Root-preserving maximalization, universal forest-rank arguments, positive certificates over local maximal domains, marked reductions and dependency assembly. | Q6 proof/ledger/source reports and the complete small A10 certificate. [Independent bit-by-bit replay](../plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md). |
| [Happy Ending](../plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md) and [happy-ending-certificate](../plugins/happy-ending/skills/happy-ending-certificate/SKILL.md) | Cup/cap and signotope definitions, weak/split distinctions, state counts, common matching compensation, legitimate chart transport and scoped SAT/witness verification. | Archived reports, proofs, programs and witness material; [fresh lower-25 witness result](../plugins/happy-ending/evidence/lower25-independent.json). |

Prepare/survey consumes each domain's definitions, imports and literature; route-loop consumes its failed gates and discriminating probes; prove executes its reductions and constructions; verify consumes its actual inputs and checker output; handoff receives its commands and evidence boundaries. Each plugin returns to the calling stage rather than starting another complete research workflow.

ECC is no longer excluded as a draft from the default domain selection. Its second-round implementation keeps `mathrsi-ecc` and adds the independently useful certificate skill; it does not create an ECC2 replacement tree. The two new cube plugins each use one substantial domain skill with mathematical, failure and reproduction references. Happy Ending separates research from certificate consumption.

## Bounded commands from the current clone

Run from the repository root. Keep generated files in a task scratch directory. These commands consume frozen scientific input without starting an archived Goal, running an optimizer or rebuilding every historical proof.

**Base behavior examples** — choose the historical best rather than the last iteration, inspect a root-preserving counterexample and finite forest interface, and read ECC's explicit Lean parameter:

```sh
python3 development/evolution/v3-20261104/base/use_cases.py
```

**Erdős 86 final Q4 certificate** — Python standard library plus an existing C++17 compiler:

```sh
run_dir=$(mktemp -d)
python3 plugins/hypercube-extremal/archive/source/tools/verify_final_q4.py --work-dir "$run_dir"
```

The actual run exited 0 in 3.436 seconds, including preparation/compilation. It checked coverage of 8,421,604 ordered Q3 pairs by 90,179 orbits, all 13,150,453 legal completions, and 3,312,331 scoring representatives. The exact maximum is `283944735335493492/480000000000000000`, yielding the safe upper bound `0.59155154`. The [log](../plugins/hypercube-extremal/evidence/final-q4-replay.log) records the complete local finite computation; the high-dimensional averaging proof is a separate mathematical component.

**Q6 A10 universal-rank certificate** — Python standard library, original independent checker executed on a copy because it writes its result beside the input:

```sh
run_dir=$(mktemp -d)
cp plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3* "$run_dir/"
python3 "$run_dir/A10_ORBIT3_UNIVERSAL_REVIEW_check.py"
```

The actual run exited 0 in 5.10 seconds: 1024 legal forests, all 1,048,576 matrix bits reconstructed by DSU, and an independent low-column GF(2) elimination of rank 1024. The [result](../plugins/hypercube-hamilton/evidence/a10-independent-result.json) supports the A10 finite premise; the imported rank upper bound and row-space argument supply its universal meaning. Full Q6 remains at its historical same-family/provisional assurance level.

**ECC complete single-parent replay** — uses the included index169 stream and an existing C++17 compiler:

```sh
run_dir=$(mktemp -d)
python3 -B plugins/ecc/tools/replay_one.py --output-dir "$run_dir"
```

The recorded run exited 0 and replayed all 148,785 pairs of that parent with actual low-weight rejection, together with 546 accepted members and 69,888 F-distance checks. Other recorded ECC use covers 429,024 saved records across 172 parents and complete 42/16 matrix enumeration. See [ECC implementation](../plugins/ecc/evidence/IMPLEMENTATION.md) for commands and read domains. The 43/10 lower-bound matrix deliberately tested against distance17 failed with actual distance16, preserving a useful failure witness.

**Happy Ending lower-25 abstract witness** — Python standard library:

```sh
run_dir=$(mktemp -d)
python3 plugins/happy-ending/tools/check_lower25.py \
  plugins/happy-ending/archive/source/working/package/proofs/sat-756/color.tsv \
  --output "$run_dir/lower25.json"
```

The [recorded result](../plugins/happy-ending/evidence/lower25-independent.json) checks all 2300 triples, 12650 signotope packets, all 300 outer pairs for weak7 absence, and the exact path/state-count identities. It establishes this abstract lower witness; it does not certify planar realizability, the upper bound or later structural thresholds.

These are uses of the actual candidate skills and source interfaces, not equal-budget performance experiments. Commands and results are preserved at their own scopes; running all of them does not constitute every domain's complete mathematical final review.

## Scientific source material and reproducibility

Each plugin carries an explanatory layer plus frozen `archive/source` materials. Existing proof texts, code, reports, failure histories and concrete inputs remain readable from the clone. New task results go to the user's workspace; archive status and historical Goal commands are not resumed.

The [ECC inventory](../plugins/ecc/archive/INVENTORY.json) identifies omitted large pair streams; one complete parent stream is included. The [extremal inventory](../plugins/hypercube-extremal/archive/INVENTORY.json) omits generated optimization coefficient tables while retaining everything used by the final portable Q4 checker. The [Hamilton inventory](../plugins/hypercube-hamilton/archive/INVENTORY.json) includes the complete A10 closed replay and identifies other large Q6 streams and generated tables that are not shipped. Their proof/source/report records remain available; the current clone does not claim full P6 large-certificate recomputation readiness.

## Research history and current adoption

ECC's story is **v0 initial results → continued research using methods/workflow inherited through v1/v2 → evidence for subsequent evolution**. The new package deepens Lean reductions, their connection to actual matrices, portable certificate publication and the 42/16 literature route. The old 172-parent double scans and 43/10 results keep their original attribution; distance17 for 45/11 remains open. A fixed-release invocation at every step is not a prerequisite for describing method inheritance.

Happy Ending's newly reported 75/76 values await proof source material. The plugin uses the received archive, retains its structural drafts' unreviewed/unaccepted status, and separates the historical SAT acceptance from the fresh lower witness check.

The two overview figures are intentionally preserved as **v2 historical snapshots**. Their ECC-draft and future-v3 labels describe that version; the current domain table and actual skill bodies describe v3. No new diagram is needed to make the existing implementation usable.

The source ARIS snapshot, copyright, dual-host implementations and four MCP bridge contracts are retained. External reviewer CLIs/accounts, Lean and TeX remain task environment dependencies. The [maintenance record](../development/evolution/v3-20261104/EVOLUTION.md) records adopted changes, actual use and both cross-model review rounds. PR #7 is a small repair to the existing v2 workflow and is integrated into v3; it is not counted as a separate research-driven iteration. v3 is the current adopted version; fixed earlier releases remain available for tasks that need their original workflow.

## New-candidate interfaces added during review

Opus identified that frozen replays alone did not implement the new-candidate route promised by the skills. Two thin tools now close that gap:

- [Q4 candidate checker](../plugins/hypercube-extremal/tools/check_q4_candidate.py): computes the exact full-domain bound and error constants from a supplied six-block integer Gram certificate, rather than trusting its bound metadata. Two different historical candidates were actually evaluated; see [inputs and results](../plugins/hypercube-extremal/evidence/candidate-inputs/README.md).
- [Forest rank checker](../plugins/hypercube-hamilton/tools/check_forest_rank.py): accepts dimension, root, holes, forests and matching columns, reconstructs all connectivity bits, and returns legality and the universal-rank gate separately. It was used on A10 and a different Q3 geometry; see [reproduction](../plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/references/reproduction.md).

The [search materializer](../plugins/hypercube-extremal/tools/materialize_search.py) restores available deduplicated source aliases while identifying the five omitted generated tables. Actual optimization remains optional and was not started. These tools serve the existing domain workflows; they do not introduce a Python research scheduler.
