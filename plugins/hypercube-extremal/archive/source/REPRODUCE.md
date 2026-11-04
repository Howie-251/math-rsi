# Portable verification and historical research replay

The current Q4-only certificate is `certificate_final_q4/certificate_control.json`.
Its historical `proof_type` label refers to a mixed experiment harness. The actual
certificate has precisely six Gram factors and an empty `q5_cuts` list. The entry
point below rejects any nonempty cuts list and never invokes an optimizer.

## Exact certificate verification

From the package root, with Python 3 and an existing GCC/Clang C++17 compiler:

```text
python tools/verify_handoff.py --require-manifest
python tools/verify_final_q4.py
```

If the compiler is not on PATH:

```text
python tools/verify_final_q4.py --compiler D:/mingw64/bin/g++.exe --work-dir ../q4_verify_work
```

`--compiler` is an executable path, not a command string. `CXX` is also supported.
No Python third-party packages, SDP solver, saved coefficient tables, or original
E: drive are required. The C++ code uses GCC/Clang extensions (`__int128` and
`__builtin_popcount`), so an arbitrary C++17 MSVC compiler is insufficient.
Compilation uses `-UNDEBUG`; assertions must stay enabled.

The default uses the OS temporary directory. In a restricted environment with an
unwritable temporary directory, supply `--work-dir` pointing to a writable folder.
The work folder contains generated matrices, a copy of keys, and the newly compiled
binary. None of these are needed as distributed binaries. Expect under 200 MB RAM
for the checker and several seconds to minutes, depending on CPU/compiler.

`--prepare-only` checks six integer Gram factors, zero Q5 cuts, outward rounding,
64-bit bounds, and exact diagonal constants. It is explicitly **not** full-domain
verification. The default also reconstructs Q3 automorphisms, checks 8,421,604
ordered layer pairs in 90,179 disjoint orbits, enumerates 13,150,453 legal marked
completions and directly verifies 3,312,331 representatives. The tight local result
is `283944735335493492/480000000000000000`, worst graph mask `3602350111`.

The result is an asymptotic bound `23662061277957791/40000000000000000`, outward
decimal `0.59155154`, not a finite-dimensional constant bound and not an SDP
optimality proof. The accompanying proof must include the n-dependent correction:

```text
rho(G) <= C + M_F/(n-3) + M_v*(4*n-6)/((n-2)*(n-3)), n >= 4
M_F = 1288810336780277/1250000000000000
M_v = 324664893404033/625000000000000
```

## Deduplicated research archives

The `inventory.json` file maps every original source path to a logical `target_path`
and the one actually stored `stored_path`; SHA-256 and byte counts are retained.
Do not assume every logical historical path physically exists in the archive.
Restore all paths in a new folder before running historical research scripts:

```text
python tools/materialize_research.py ../q4_research_work
```

The optimized 2026-10-28 certificate itself is physically complete apart from the
excluded prebuilt executable. Other historical certificate and research trees are
deduplicated. Original bytes, absolute paths and old prose are retained as history;
the restored code uses relative paths to neighboring directories.

Optimization replay is optional, CPU based, and was **not run during this handoff**.
It needs NumPy/SciPy (historical environment: Python 3.14, NumPy 2.4.2, SciPy 1.17.0),
GCC with OpenMP, and SciPy's private `_highspy` API. That private API can change.
The archives record floating search iterates, not mathematical optimality.

After materialization, work in `research/optimization_20261028_q4/`. Rebuild the
excluded evaluator binary before instantiating `Model`:

```text
g++ -O3 -shared -fPIC -fopenmp evaluate.cpp -o evaluate.so
g++ -O3 -std=c++17 -UNDEBUG verify_six.cpp -o verify_six
```

On Windows the second output must be `verify_six.exe`. Historical Python launchers
use the extensionless basename and Windows resolves it. The evaluator must retain
the name `evaluate.so` because `model.py` loads that exact filename with ctypes.

`Model` requires `full_meta.npz`, `full_C.npz`, five `face_block_*.npz`,
`face_orbit_meta.npz`, `shadows.bin`, `face_indices.bin`, and `vertex_indices.bin`.
All are archived once. Supporting regeneration uses `prepare_data.py`,
`build_face_orbits.py`, and `generate_models.cpp`, with keys, edges, pair index,
face-pair lookup and vertex-flag codes also included. No regeneration is required
to check the final certificate. The three large arrays consume about 371 MB.

The final historical Q4 control branch lives in the neighboring directory with
historical name `research/q5_empty_moment_20261028/`. Its allowed command is:

```text
python column_lift.py --no-q5 --rounds 20 --prefix replay_control
```

This starts a new optimization and is supplied solely for future, explicitly
budgeted replay. `--no-q5` is essential. Its initial snapshot is the included
`optimization_20261028_q4/q5control_best.npz` (a Q4 PSD initializer despite its name).
The archived `final_control_best.npz` and `final_control_history.json` are the
actual completed final branch. Do not expect a fresh run to match floating iterates
bit for bit across numerical libraries. Independently integer-certify any result.
The actual `column_lift.py` RNG seed is **20261029**; a historical mixed run
manifest says 20261028. Use the executable source as authority and retain the
discrepancy as a provenance limitation. `certify_lift.py` always writes
`certificate.json` and `result.json` regardless of input name, so run historical
certification only in a disposable scratch copy, never in the frozen package.
The mixed `certify_lift.py` and `verify_q5.py` are retained as original provenance
only; use the Q4-only portable checker for this handoff's result.

Historical reports may mention Q5/Q6 next steps. Such prose does not expand this
package's scope. Q5/Q6 candidate snapshots, added cuts, selected partitions, and
Q5/Q6 experiment directories are excluded.
