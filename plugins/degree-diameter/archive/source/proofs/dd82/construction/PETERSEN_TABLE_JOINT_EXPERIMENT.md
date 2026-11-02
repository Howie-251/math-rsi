# Joint use of the fixed-root matching table

Date: 2026-10-11. The complete 18,624-permutation domain from
[the fixed-root constraints](PETERSEN_FIXED_ROOT_CONSTRAINTS.md) was actually
used in one new joint SAT input. This run ended **OUTPUT_LIMIT**, without a
SAT or UNSAT decision. The fixed-root family remains open.

The normalized graph has root fiber 5 with internal graph P, five outer
fibers with internal graph Q, and five identity root matchings. All ten
outer matchings are independent. The input contains:

- Exactly-one constraints on every matching row and column.
- A complete allowed-table selector for each matching. Each selector implies
  its ten edges, and at least one selector is true. Different permutations
  disagree in a row, so the row constraints already prevent two selectors
  being true. Reverse support clauses connect every edge back to its table
  selectors and do not narrow the allowed domain.
- Entrywise root coverage: each required T neighbor occurs among the four
  incident outer matchings. The total off-T edge count is at most 25, an
  explicit redundant consequence of the same root coverage.
- Direct-edge or two-step coverage for every cross-fiber vertex pair. The
  internal Petersen graphs already cover all within-fiber pairs.
- At most two direct/two-step witnesses for each cross-fiber pair, a
  necessary consequence of eleven slots covering ten targets.

The path terms are exact. For a fixed endpoint pair, a one-variable route
edge uniquely identifies its middle vertex; a pair of variable edges also
uniquely identifies that vertex. Direct edges are separate. Therefore the
implementation's set of terms never merges distinct route slots. Fixed
paths are counted separately, and conjunction variables are equivalences.

The code rechecks that every retained table row is a permutation passing
both local support tests. Completeness of the table uses the already saved
full 10! enumeration. A separate agent read the actual new encoding and
the cardinality helper and found no candidate-preservation or exactness
gap; no duplicate solver run was made.

The input has **343,415 variables and 2,426,235 clauses**. Encoding took
3.399 wall seconds. The solver was pinned to one CPU, with a 60 CPU-second
budget, 4 GiB address-space limit and 256 MiB output-file limit. It exited
with signal 25 after **36.898368 CPU seconds / 37.351528 wall seconds**,
having reached that output limit. Its partial LRAT is not an UNSAT
certificate. No graph or completed exclusion resulted. The large table
encoding has not demonstrated a performance improvement over prior edge
encodings.

Files:

- `computations/dd82/construction/petersen_fixed_root_table_sat.py`
- `computations/dd82/construction/petersen_fixed_root_table_sat/input.cnf`
- `encoding.json`, `solver.log`, `result.json` in that directory.

The later [layer obstruction](PETERSEN_FIXED_ROOT_LAYER_OBSTRUCTION.md)
additionally requires at least two same-layer outer edges. It was obtained
after this run and was **not** present as an explicit clause in this input.
The full graph constraints logically imply it. No unchanged-input rerun is
scheduled, and there is no resumable solver state.
