# Target-free and exact-cardinality encoding audit

## Canonical bases

The genuine order-generic strict base is

```python
lib.erdos.etv_signotope(7, 5, 6, N)
```

for `N=26..35`.  `etv()` defaults to `include_no_gon=True`
(`lib/erdos.py:23-55,229-235`), and `etv_signotope` then adds the signotope
packets at lines 237--259.  In the `(7,5,6)` bounded box, the nontrivial
`no_7_gon` layer excludes the weak shared-outer-endpoint `(4,5)` target.

The target-allowed relaxed gate is

```python
lib.erdos.etv_signotope_extension(7, 5, 6, N)
```

which deliberately calls `etv(..., include_no_gon=False)` at lines 262--280.
Artifacts must use the unambiguous labels `strict_no_target` and
`target_allowed_relaxed`; older tests sometimes use “target-free” to mean
“free of target clauses”.

No explicit symmetry-breaking clauses occur in either builder, the down-set
state encoding, or the totalizer.  `flip_cup=True` is polarity semantics, not a
symmetry reduction.  Because the 5/6 path bounds and 3-by-4 state box are
asymmetric, the first production version records `symmetry_breaking=false` and
must not fix a color or leading triple.

The existing `state_charging.corpus` public modes are not reusable production
scopes: they fix strict N25 or relaxed N26 at
`corpus.py:72-93,243-276,398-417,465-476`.  Its caller-supplied scope trusts
metadata too broadly.  The new wrapper must rebuild and bind the canonical
base, its `(7,5,6,N,include_no_gon)` metadata, clause groups, and hashes.

## Exact count construction

Use `state_charging.obligations.encode_at_most_exact`, the deterministic PySAT
totalizer already truth-table tested in
`tests/test_state_charging_obligations.py:353-375`.

Let

```text
E = [ O[H]  for H in exceptional_catalog ]       # 10 type occupancies
M = [ -O[G] for G in ordinary_catalog ]          # 25 missing-type literals
```

The attachment's `e(X)` counts exceptional state **types**, so `E` must use the
ten `occupancy_vars`; per-endpoint `full_vars[v]` are the wrong quantity.
Encode equality by two at-most constraints:

```text
exact(E,e) = AM(E,e) and AM(-E,10-e)
exact(M,m) = AM(M,m) and AM(-M,25-m).
```

All four calls must thread
`top_id = previous_encoding.num_vars`.  Reusing the original top id would make
totalizer auxiliaries collide and silently change the formula.  When mutating
a SATInstance for export, allocate/register every returned auxiliary ID with
`new_var` before appending its clauses; otherwise `_num_vars` and the DIMACS
header are wrong.  Metadata must record input literals, bounds, auxiliary
ranges, clause hashes, and the final formula hash.

For a canonical cell `A[r,e]`, set `m=r-1` and `N=26+e-r`.  Because every
endpoint has one state, occupancy is iff, and this cell requests exactly
`(25-m)+e=N` occupied types, every satisfying cell assignment is itself
injective by finite counting.  The order-generic injection lemma is still
needed to prove the 55 cells cover every target-free model, rather than merely
to validate models already inside a cell.

## SAT audit requirements

`corpus.audit_model_against_formula` audits a mutable SATInstance but cannot be
used unchanged if cardinality auxiliary clauses/variables live only in an
immutable formula snapshot.  The new audit must inspect the complete final
numeric formula, including all totalizer variables and clauses, then decode
only the registered triple/state atoms.

After full-formula replay it must independently recompute:

- the complete coloring and signotope packets;
- both forbidden-path bounds;
- weak target presence/absence according to formula mode;
- all 35 endpoint states and injection;
- all S/O/F assignments, without requiring start atoms;
- `|ExcOcc|`, `|MissingOrd|`, and `N=25-m+e`;
- the exact requested `(r,e,m,N)` identity.

Strict SAT is accepted only if target absence is independently confirmed.
Relaxed SAT may contain a target and is discovery/nonvacuity evidence only.
