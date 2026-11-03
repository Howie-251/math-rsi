# Full61 adjacent-double model with actual defect-port propagation

This is a substantive extension of the first seven-type full61 model.
At source delivery, **this directory has no generated CNF and no solver
or checker execution**. The preceding run and all its artifacts remain
untouched in `../adjacent_double_full61_run/`. No conclusion follows from
that run's UNKNOWN outcome. This implementation does not attest mathematical,
independent source, or Gemini review acceptance.

All labels, seven C types, true original-graph variables and normalizations
are unchanged from the
[baseline scope](../adjacent_double_full61_run/SCOPE.md). The mathematical
sources are
[ADJACENT_DOUBLE_REPEAT_LOCAL.md](../../../../proofs/dd82/n61/ADJACENT_DOUBLE_REPEAT_LOCAL.md),
[ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md](../../../../proofs/dd82/n61/ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md),
and the new
[ADJACENT_DOUBLE_PORT_PROPAGATION.md](../../../../proofs/dd82/n61/ADJACENT_DOUBLE_PORT_PROPAGATION.md).
The root must check the new proof and this source before executing the revision.

## Preserved original model

The copied encoder emits every original variable and clause in its original
order through the all-pairs actual-path group. It still has1830 primary
A variables,107970 actual two-edge path auxiliaries, all61 exact degrees,
all1830 true distance-at-most-two coverage clauses, every original exact
actual-B constraint, both sets of fiber degree constraints, and all seven
C selectors in one CNF. C type, S–T adjacency pattern, and q's transversal
remain unfixed beyond the already proved conditions.

Only after this complete original prefix are any new variables or clauses
emitted. Preparation records the prefix's actual variable/clause counts and
the added totals in `encoding.json`. The original run directory is neither
written to nor rerun by this source. The root can compare the new prefix directly
with the retained old input after authorized preparation; no hashes are used.

## New clauses and exact same-A meaning

For any distinct pair let `c=mu+A=1+B`. The original actual path count
already defines exact unary thresholds for `c>=1,2,3,4` on pairs whose B
was not fixed. The following456 pairs all belong to that category:
36 S×T pairs and420 (S∪T)×Z pairs.

The new source collects their **existing** `c>=2` and `c>=3` threshold
variables without changing the original emission. After the prefix it
negates `c>=3`. Since original coverage requires `c>=1`, each such pair
now has `c∈{1,2}`, and its existing `c>=2` variable is exactly the actual
B entry in `{0,1}`. It is not an independent B choice or a proposed
common-neighbor count. The original path AND equivalences are retained.
The necessity of these unit bounds is local equations (11),(14).

The extension then imposes these proved identities:

- `P=B[S,T]` has exactly one actual B unit in every row and every
  column, by local equation (11). The six-point matching stays variable.
- For every S×T pair except `(q,p)`, a binary clause forbids simultaneous
  A adjacency and a B unit. This is the new theorem that the possible
  overlap of `K=A[S,T]` and P is confined to `(q,p)`. Both A and B
  values at `(q,p)` remain variable.
- For each z∈Z, `sum_{x∈S} B_xz=A_pz` and
  `sum_{y∈T} B_yz=A_qz`, local equation (14). Each sum is encoded
  as an exact count of its six actual-B threshold variables: zero
  under a false adjacency guard and one under a true guard.
- For each x∈S, `sum_{z∈Z} B_xz=1+[x=q]−A_xp`;
  for each y∈T, the sum is `1+[y=p]−A_yq`, local equation (16).
  These are exact guarded counts over the35 actual-B unit variables.
  Ordinary rows require1 or0 according to the guard; the special
  q/p row requires2 or1. Guards are actual S–T adjacency variables.
- For each of the12 possible S/T parents x and each of the595
  unordered Z pairs z,z', a ternary clause forbids
  `A_xz AND A_xz' AND A_zz'`. These7140 clauses encode the new
  independence theorem for every actual S/T-parent class in Z.
  No Z point is assigned a new parent or a fixed neighbor by this step.

The new parent-class independence and overlap claims require the connected
actual-defect argument in the new proof. Their validity is not inferred
from UNKNOWN or from observing any solver pattern. There is still no
separate B-support-connectivity constraint: the theorem supplies necessary
clauses for the intended connected branch. The double-defect path forest
and variable internal B[S]/B[T] edge identities remain intentionally
unencoded.

The94 exact/guarded port count records and456 actual threshold mappings
are saved as `port_constraints.json` during preparation. The existing
`defect_constraints.json` keeps its original clause locations and adds
each strengthened pair's appended upper-bound location and final bound.
All variable/clause counts in execution records are measured from the
actual emitter, not predicted here.

## Scope and outcome

Every actual adjacent-double target, after the same three justified label
choices as the first model, satisfies all original clauses and all new
port identities. Thus, subject to accepted proof and source coverage, a
checked contradiction of this complete seven-type model excludes the
entire adjacent-double branch at61. It still does not exclude nonadjacent
double defects or order61 itself. A SAT model still gives an actual complete
graph and must undergo the unchanged independent graph verification.

The parent runner is copied unchanged from the original adjacent-double
directory and uses the new directory as HERE. Parent preparation is bounded
by20 CPU/30 wall seconds. The parent CNF is prepared once but **is not itself
solved** in the selected execution plan: `prepare_cases.py` copies it into
seven branches, each adding one positive selector unit and1050 clauses
ordering labels within the existing U/V cells. There is no extra variable,
V-parent choice, S/T relabeling or original-clause change. The header clause
count increases by1051; the complete seven-selector metadata is retained
alongside `selected_case`.

The additional normalization sorts the Z labels within each fixed U/V cell
lexicographically by their actual S-parent and T-parent indices. An actual
graph can be relabeled this way independently in each cell without changing
any previously fixed parent or the selected C type. For each consecutive
label pair in a cell,15 binary clauses prohibit a descending S parent;
90 four-literal clauses prohibit a descending T parent when the S parents
are equal. There are35−25=10 such consecutive pairs in every type, hence
1050 ordering clauses. Equal parent keys remain freely ordered.

Every original target reaches one of the seven cases after these proved
cell relabelings, and the case selectors remain mutually exclusive. This
is coverage of original graphs up to the allowed relabeling: the sorted
case inputs do not retain every unsorted assignment of the parent CNF.
The root's full-graph model gives the new normalization proof; it also
requires source review. A selector unit enables the existing conditional
V-parent clauses by ordinary Boolean propagation. This is an expected
propagation benefit, not a measured speedup or a diagnosed cause of the
earlier timeout.

Each generated `case_0` through `case_6` contains its own exact input,
encoding metadata and copied edge map. Its decode-only `encode.py` wrapper
imports the parent encoder and changes HERE to the case directory. Its
runner wrapper imports the parent runner and likewise changes only HERE;
ROOT, solver, checker and independent BFS paths remain anchored correctly
to the project. Case `prepare` is explicitly rejected because only the
parent `prepare_cases.py` generates these inputs. No wrapper launches a
process at import.

Each branch solve is bounded by50 CPU/70 wall seconds, with4 GiB address
space and256 MiB per solver output file. SAT alone invokes complete clause
validation and independent all-pairs BFS, each with5 CPU/10 wall seconds.
The4 GiB limit is address space, not a measurement or limit stated as RSS.
No automatic repeat, internal solver-state retention, or certificate job
is added. The root chooses actual bounded parallelism after checking current
resources; this source adds no scheduler or batch launcher.

Commands are for the root after review; the implementation agent has not
executed them:

```bash
python computations/dd82/n61/adjacent_double_ports61_run/runner.py prepare --cpu 1
python computations/dd82/n61/adjacent_double_ports61_run/prepare_cases.py
python computations/dd82/n61/adjacent_double_ports61_run/case_0/runner.py solve --cpu 1
```

The last command is illustrative for case0; the root launches each of
case0..6 at most once, using actual available CPUs. UNKNOWN, timeout,
output limit and failure have no exclusion meaning. A checked UNSAT for
one case excludes only its C type. Excluding the whole adjacent-double
branch requires checked contradictions for all seven cases together with
the reviewed complete reduction. One valid SAT graph in any case is an
original target. An exit20 is only RAW_UNSAT until the root separately
launches that case's exact-input LRAT checker, which requires exit20 and
`s VERIFIED`:

```bash
python computations/dd82/n61/adjacent_double_ports61_run/case_0/runner.py check --cpu 1
```

The certificate applies to this saved CNF only. Mathematical transfer
still depends on the original and new proof and source reviews. The
changed input is justified by substantive proved port constraints, not
by renaming an unchanged solver restart.
