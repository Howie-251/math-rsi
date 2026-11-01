# Full q=9 closure: source and build order

This is the smallest complete 25-point selection branch. The full paper uses
q=5, q=8 and q=9; the saved q=6/q=7 catalogues are unnecessary. The final source
entry is `ThirtyFour.TwentyFiveNineLowComplete.propertyB`, consuming the actual
`TwentyFiveSelection.NineLowExtension H` and 34 edges. **The full dependency
chain is generated but has not yet passed its ordinary build.**

## Actual-input spine already checked locally

- `TwentyFiveUnitExtension`: actual unit traces form a pair decomposition;
  all promoted multipoint blocks are disjoint; the complete new large family
  equals `extend oldBig selected`. `choices_complete` follows every actual
  membership decision, so recursive pruning is complete.
- `TwentyFiveUnitCatalogue`: analytic six-lock classification gives the nine
  existing K6 representatives. `covers_succ` normalizes the actual old locks,
  lifts their permutation while fixing the actual new lock, then applies an
  explicitly checked permutation to one generated extension.
- `TwentyFiveUnit7Actual`: all 272 extensions of the nine six-lock classes
  reduce to the 22 saved seven-lock families. The full combined local check
  passed in 19.75 seconds, maximum RSS 2.67 GB, only the standard three axioms.
- `TwentyFiveUnitCounts`: all actual multiplicities are reconstructed from
  the full block family, actual edge count, and an arbitrary vector of actual
  lock degrees. Empty and singleton counts are included. The same theorem
  proves nonnegative singleton budgets and the total-edge budget, so impossible
  families are excluded before natural subtraction can hide negative values.
- `TwentyFiveUnitConditional`: degree-aware final extension. Discarding a
  generated family requires failure of the proved actual feasibility predicate;
  retained entries have explicit bijections, degree transport, and all actual
  type counts. Combined local check passed with standard three axioms.

Logs: `unit-extension-r2.log`, `unit-catalogue-r2.log`,
`unit-seven-actual-r1.log`, `unit-counts-r2.log`, `unit-conditional-r2.log`.
These logs do not replace the parent's ordinary module builds.

## Pending finite classification build

Ordinary targets in dependency order:

1. `Aris4Math.ThirtyFour.TwentyFiveUnit7Actual`.
2. `Aris4Math.ThirtyFour.TwentyFiveUnit8Actual`: 22 parents, 1,476 generated
   extensions, 65 canonical representatives.
3. `Aris4Math.ThirtyFour.TwentyFiveUnit9Actual`: 65 parents, 10,271 generated
   extensions, 374 representatives.
4. `Aris4Math.ThirtyFour.TwentyFiveNineLowClassified`: actual 34-edge/six-degree
   feasibility filters the 374 families to the existing 147 q=9 profiles,
   and derives all their actual multiplicities. No colored-search rerun.

Each level separates `Data`, `Checked`, and `Actual`. `Checked` uses
`List.Forall₂` to pair the complete generated extension list with its explicit
permutation witnesses. It verifies bijectivity and exact family images; a
canonicalization hash or graph invariant is never the acceptance criterion.
The Python replay took 0.08 s, 0.83 s and 39.61 s for levels 7, 8 and 9.
That is certificate generation time, not Lean validation time.

Generator: `generate_unit_extension_certificates.py 7|8|9`.
Raw witnesses: `UNIT_EXTENSION_{7,8,9}_CERTIFICATES.json`.

## Numeric closure and tenth lock

`generate_q9_numeric.py` copied saved positions, multiplicities and exact bare
bounds. All q=9 and tenth-lock certificates have zero quota deductions.

- 147 nine-lock cases: 144 strict, residues 0, 3, 6.
- 25 tenth-lock representatives: all strict.
- Numeric batches contain at most 12 cases; their exact targets are listed in
  `Q9_NUMERIC_BUILD_MANIFEST.json`.
- The first actual nine-low numeric caller (case 1) passed in 7.56 s, maximum
  RSS 2.70 GB: `nine-low-numeric-r1.log`.

The tenth-lock coverage reuses the same actual large-family extension, now
with the actual last degree 6 or 7. The complete generated choice counts for
the three roots are 29, 148, 486. Feasibility retains respectively:

| Root | Last degree 6 | Last degree 7 |
|---|---:|---:|
| 0 | 16 | 28 |
| 3 | 102 | 138 |
| 6 | 14 | 14 |

These match the original paper's exact labeled extension counts. The 25 saved
orbits come with explicit label bijections fixing the distinguished tenth lock.
All generated choices, including infeasible ones, occur in the checked list;
the infeasible entries are not silently omitted.

Generators: `generate_q9_classification.py`, `generate_q9_tenth.py`.
Witnesses: `Q9_TENTH_EXTENSION_CERTIFICATES.json`.

After the classification and numeric dependencies pass, build:

- `Aris4Math.ThirtyFour.TwentyFiveNineLowNumeric`;
- `Aris4Math.ThirtyFour.TwentyFiveNineLowTenthComplete`;
- `Aris4Math.ThirtyFour.TwentyFiveNineLowComplete`.

The final theorem is the actual q=9 selection branch. It is not the entire
25-point theorem: q=5 and q=8 remain to be bound to their saved certificates.
All regular builds remain under the root's single-executor queue.

## 2026-10-15: direct rows and short rejection certificates

The original tenth-extension pilot was stopped at 63.66 seconds / 12.7 GB;
that run was not a PASS. Subsequent probes are guarded at 20 seconds or 4 GiB
per process. `lean_light_probe.py` stops only its own process group and records
the stop reason. No full classification batch is run by this worker.

Two representation changes are now implemented:

1. Candidate coverage is an exact equality of a displayed finite set with the
   filtered pair completion, followed by a symbolic membership proof. It does
   not universally scan every subset merely to prove list membership.
2. Every extension row carries its selected blocks, permutation and optional
   rejection witness directly. The projection of all rows onto selected blocks
   is equated once with the complete recursive choice list. Each retained row
   checks only its explicit permutation; each rejected row gives seven or eight
   distinct incident blocks contradicting one actual degree. The checker proves
   these few blocks belong to the pair completion without constructing that
   whole completion. Both alternatives imply the original conditional `Checks`.

All 227 rejected nine-lock families and all 1,014 rejected tenth-lock extensions
have this simple degree obstruction; none needs a total-edge-budget rejection.
There are 312 retained tenth-lock extensions, hence 1,326 rows in all. The same
actual-H feasibility theorem still supplies the contradiction; the rejection
list does not change the mathematical domain.

General modules: `TwentyFiveDegreeObstruction` and `TwentyFiveConditionalRows`.
The latter also has `FamilyRow`/`FamilyCheck` for the 374-to-147 filter. A short
pilot with four genuine rejection rows and one genuine retained permutation
passed in 3.99 seconds / 1.43 GiB; its kernel finite check took 0.612 seconds.
The original conditional computation for just one rejected row took 13.2 seconds.
Evidence: `tenth-one-r1.log`, `tenth-obstruction-r2.log`,
`fast-rows-short-r1.log`. The last pilot included both general correctness proofs
and printed only the standard three axioms for its finite theorem.

The authoritative final generator for these two tables is now
`generate_q9_fast_rows.py`, run after the earlier data generators. It reads the
saved witnesses and does not search layouts. `Q9_FAST_ROWS_BUILD_MANIFEST.json`
lists 110 modules, each with at most 16 direct rows. The final coverage modules
compose these checked batches with their single exact projection equality.
These full batches and the final q=9 theorem remain pending ordinary builds.
The parent already built the four `TwentyFiveUnit*` general modules; that does
not certify the new finite tables or the final branch.

Inventory recovery was also changed to the symbolic `TwentyFiveInventorySupport`
lemma: the empty trace, singletons and listed multipoint blocks are the complete
support. Only their explicit list is checked; the zero-outside-support argument
is general. The first nine-lock and tenth-lock recovery pilot passed, but all
147/25 rows remain subject to their normal module builds.

### Latest stable ordinary build list

Use `Q9_COMPLETE_BUILD_ORDER.json` as the **current** dependency-ordered target
list. Its 206 entries include already-built helpers, data, finite batches and
light aggregates. It is intended for one serial regular-build owner; invoking a
single unbuilt final target could schedule multiple heavy imported modules.

The latest batch sizes supersede the initial 16/32-row snapshot above:

- Uncolored 8/9-lock extension: 128 rows per batch, 24 and 114 batches.
- q=9 filter and tenth-lock extensions: 64 rows per batch, 30 batches total.
- Numeric bounds: unchanged, 12 per batch.

A nontrivial five-row 9-lock pilot passed (`unit-rows-pilot-r1.log`): finite kernel
check 0.398 seconds, peak process RSS 1.47 GiB. Its total 17.95 seconds included
elaborating the complete 374-family catalogue, which ordinary consumers will
import from compiled Data. Batch sizes are a scheduling choice based on this
small pilot, not a guarantee of full-batch memory; the parent owns the first
regular batch and any necessary adjustment.

`TwentyFiveSparseCompletion.complete` supplies exact pair completion from two
explicit lists using only their entries and all vertex pairs. Its general proof
and a genuine 10-lock completion passed in 2.97 seconds / 1.39 GiB, finite check
0.401 seconds, standard three axioms (`sparse-completion-r2.log`). The 147 and 25
inventory completion statements now use this proved list check. Their remaining
recovery arguments retain the earlier sparse-support proof.

Regeneration order (no layout search):

1. Existing `generate_unit_extension_certificates.py` only if the saved explicit
   certificates must be reconstructed; otherwise reuse its JSON.
2. `generate_unit_fast_rows.py 8`, then `... 9`.
3. Original q9 numeric/classification/tenth generators for base data as needed.
4. `generate_q9_sparse_inventory.py` to emit the new exact completion proofs.
5. `generate_q9_fast_rows.py` to emit the final direct-row filter/extension checks.

Earlier 16/32-row generated Batch files can remain as unreferenced artifacts;
they are not in the current build list or final dependency chain. No new branch
is declared proved merely because these sources and generators exist.
