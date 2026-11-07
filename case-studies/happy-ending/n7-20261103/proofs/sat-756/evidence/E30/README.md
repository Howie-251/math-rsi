# Erdős–Szekeres: Upper Bounds for Convex Heptagons and Octagons

Michael Schroeder · Independent Researcher  
ORCID: https://orcid.org/0009-0004-3249-0195  
Version 1 · 19 September 2026  
DOI: [10.5281/zenodo.22842891](https://doi.org/10.5281/zenodo.22842891)

The DOI is reserved for this paper and its companion archive in an unpublished Zenodo draft. `ZENODO_RESERVATION.json` preserves the original reservation; `ZENODO_METADATA_SYNC.json` records the subsequently saved title and licence-scope update. The release files have not yet been uploaded. The DOI will resolve publicly once the record is published.

**Results: ES(7) ≤ 81 and ES(8) ≤ 319.** These concern ordinary convex polygons in arbitrary finite real planar sets in general position. Emptiness is not required. The complete upper-bound implications are formalized in Lean, including geometry, encoding semantics, finite coverage, and certificate soundness.

The release uses Lean native evaluation for finite checks: **19** native-evaluation dependencies for ES7 and **8** for ES8, in addition to `propext`, `Classical.choice`, and `Quot.sound`. There is no admitted lemma or additional mathematical axiom in either final declaration. This is not a kernel-only evaluation of every finite computation. No external peer review is claimed.

This is the first public paper version, V1. It includes the complete planar proofs, the restricted theorem's statement audit, and independent finite checks for both polygons. All 208 sealed proof modules are retained, with a supplemental module for statement equivalence and a parser guard. See `RELEASE_NOTES.md` for the release scope and `certificates/README.md` for the data conventions.

Historical draft labels in preserved audit paths and logs identify internal verification snapshots, not earlier public paper versions. The pinned Lean toolchain and Citation File Format schema have their own version numbers.

## Contents

- `paper/main.pdf`: the manuscript.
- `paper/main.tex` and the other `.tex` files: all editable typesetting sources, including the bibliography; no separate BibTeX run is needed.
- `certificates/`: readable JSON versions of the two ES8 omission certificates and their source provenance.
- `formal/sources/`: all 208 Lean project modules, including embedded exact certificates and the attributed Baek port. No project `.olean` files are bundled.
- `formal/PROVENANCE.json`, `formal/MANIFEST.json`: sealed source provenance and hashes.
- `formal/audit/`: records from the completed formalization; historical paths describe the machine on which those checks ran and are not dependencies.
- `audit/`: combined release checks, statement-to-source map, and prior sealed-release evidence.
- `literature/REVIEW.md`: the current primary-source literature assessment.
- `literature/BACKGROUND_MACHINERY_2026_09_15.md`: a dated historical assessment of additional research machinery; some project-relative links require the research archive.
- `tools/verify_release.py`: clean rebuild and exact axiom audit of both endpoints.
- `tools/build_paper.py`: typeset the manuscript and reject unresolved references or overfull boxes.
- `MANIFEST.json`: SHA-256 identities for the release payload.

`formal/` preserves a sealed common library initially packaged at the ES7 completion. Its top-level README therefore emphasizes ES7, while its sources also contain the complete ES8 proof. Read this root README and `audit/THEOREM_MAP.md` for the combined release. Earlier third-party port notes are historical milestone records; their formerly open bridges are closed in the final modules named here.

## Final Lean declarations

```lean
ES7FinalVerified.es7_le_81
ES8Final.es8_le_319
```

Both quantify over `Finset (ℝ × ℝ)`. Each assumes only the indicated cardinality threshold and ordinary general position. Convex position is defined through mathlib's convex hull. The classical lower bounds 33 and 65 are cited in the paper, not claimed to be formalized by these declarations.

## Rebuild the proof

Prerequisites: Python 3.10+, Git, the pinned Lean toolchain, and a built checkout of mathlib with its normal dependencies.

- Lean: `leanprover/lean4:v4.32.0-rc1`
- Lean commit: `b4812ae53eea93439ad5dce5a5c26591c31cb697`
- mathlib commit: `360da6fa66c1273b76b6b2d8c5666fd5ac2e3b56`

A standard setup, in a new external dependency directory, is:

```sh
elan toolchain install leanprover/lean4:v4.32.0-rc1
git clone https://github.com/leanprover-community/mathlib4.git mathlib4
cd mathlib4
git checkout 360da6fa66c1273b76b6b2d8c5666fd5ac2e3b56
lake exe cache get
```

Return to the extracted release root and run:

```sh
python3 tools/verify_release.py --mathlib /absolute/path/to/mathlib4
```

The verifier checks pinned identities, topologically rebuilds every bundled module in a fresh directory using only precompiled mathlib dependencies, and audits both final theorems. It also compiles the supplemental mathlib-convex-independence adapter and checks that its corollaries add no native axioms. Its output directory is printed; `verification.json` and `axioms_and_statements.log` record the actual outcome. An optional `--lean /absolute/path/to/lean` selects the executable, still subject to the version/commit check. `--output /new/audit/directory` chooses a fresh output location.

Allow several gigabytes of free disk and memory. The large certificate modules dominate compilation. This is a source-replay package; a discovery solver, coordinates fixed to a grid, a remote chat, or unavailable download is not needed. Dependency installation needs network access; once prerequisites are present, the proof replay itself does not.

The separate `--audit-existing /path/to/prior/build` mode checks source identities and audits already compiled modules. It is explicitly reported as reuse and does not stand for a clean rebuild. The release records distinguish these operations.

## Independent finite checks

With Python 3.10+ and a C++17 compiler available:

```sh
python3 tools/check_octagon_finite.py --output /tmp/es8_finite.json
python3 tools/check_heptagon_replays.py --output /tmp/es7_replays.json
python3 tools/check_examples_and_counts.py --output /tmp/es_examples.json
python3 tools/check_residual_lower.py --output /tmp/es_residual_lower.json
```

The first reconstructs the two state universes and directed differences, certifies all 3,849 cyclic families and 23 block maps, compares the literal Lean and JSON data, and replays both complete omission trees. It uses Python integers and does not execute Lean. Its connection to the planar theorem uses the geometric lemmas in the paper and Lean; the Python checker itself is not formally verified. The older `check_octagon_arithmetic.py` remains available for an arithmetic-only audit.

The second compiles `tools/strict_rup.cpp` and extracts the five embedded heptagon refutations into a fresh temporary directory. It verifies all four population/closure refutations unchanged. For coverage, it first reproduces the strict rejection of a redundant satisfied hint (step 473998, hint 473786), then omits exactly that hint and strictly replays all 381,647 additions. No source clauses, conclusion clauses, or other hints change. The sealed Lean source still contains the original proof. `--cxx` selects a C++17 compiler. The checker also tests invalid hints, missing conflicts, and malformed source examples. It is separately implemented, not an externally verified LRAT checker.

The third checks the exact 25-point example, the ten-state example, comparison arithmetic, and a scoped project-source scan. The complete general binomial identity is proved algebraically in the manuscript; the numerical loop is only a regression check.

The fourth checks the retained 26-point planar residual example: general position, maximum cup six and cap four, absence of a shared five-cup/four-cap junction, and all 657,800 seven-point hulls. Pair-rank recurrences and direct subset enumeration independently identify the actual junction witnesses. Together with the classical balanced lower construction, this proves that separately optimizing the heptagon partition terms cannot give a bound below 58. This is a limitation of that method, not a lower bound on ES(7). The octagon method floor is 114; the upper endpoint 121 in Section 9 is conditional on the Erdős–Tuza–Valtr conjecture. These lower constructions are not claimed to be formalized in Lean.

These paths strengthen independent reproducibility. They do not change the exact `native_decide` dependencies of the Lean endpoints or constitute a second-platform build.

## Build the paper

Install [Tectonic](https://tectonic-typesetting.github.io/) or use a TeX distribution providing `pdflatex`. With Tectonic:

```sh
python3 tools/build_paper.py
```

This writes `paper/build/main.pdf`. Tectonic may fetch standard TeX resources on its first use. With a conventional installation, run `pdflatex main.tex` three times from `paper/`. The included `paper/main.pdf` is the reviewed output. Both build paths use the same ordinary LaTeX sources.

## Attribution and licenses

Manuscript, original prose, and original accompanying certificate data: **CC BY 4.0** (`LICENSE-PAPER.md`). Original code: **MIT** (`LICENSE-CODE`). Baek's ported `ErdosTuzaValtr` modules retain **Apache-2.0**; see `formal/third_party/baek_port/LICENSE` and `THIRD_PARTY.md`. Lean, mathlib, and their dependencies are external and retain their licenses. No external paper PDFs are redistributed.

The author-approved research-assistance acknowledgment appears in the manuscript. All responsibility for the content and conclusions of this work rests with the author. This bundle is prepared for the existing reserved DOI; packaging it does not upload files or publish the Zenodo record.
