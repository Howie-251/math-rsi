# Fixed O22 clone65 build

Use the pinned local `.tools/lean-4.24.0-linux/bin/lean` through `compile.py`. That script reads the existing explicit `LEAN_PATH`, uses one Lean thread, and records a45CPU module limit; no dependency resolution or fetching occurs. `generate_formal.py` reconstructs only the24new-scope Lean sources from the frozen source parameters and the one saved O22 rule. `run_chunks.py` runs the fixed nineteen post-pilot finite modules with at most two workers. The initial pilot was chunk00.

The same concrete source is preserved across the deliberately narrowed imports: Definitions imports existing source Definitions; Inputs imports existing source Incidence; Exact imports the already closed full source Exact. This avoids loading all415old proof modules in each finite chunk, without changing the underlying source graph. The old generic `OvoidSpreadCloneCapacity` and `FullNeighborhoodClones` modules are imported, not rebuilt.

The finite certificate uses400point-owner entries and400line-index entries. Twenty blocks of20lines discharge3200position checks. The224unoccupied lines have default index0, and the certificate's none-or-owner statement remains valid. The22chosen point-owner checks establish the exact index uniqueness hO. The source's existing actual theorem establishes hS. These imply load≤1 even for the observed adjacent centers.

`check_binding.py` separately reads both complete edgefiles, checks all ordered centers and immutable source neighborhoods, and streams every final edge against the old-plus-clone formula. It does not run BFS and does not claim to formalize an ASCII parser. `write_final_receipt.py` gathers all current and retained Lean attempt receipts and verifies the actual final type/body/axiom output. Its authoritative result is `FINAL_COMPILE_RESULT.json`.

All local tasks are terminal. Numerical acceptance and external new-scope reviews belong to root; no accepted counts or shared stage files were changed by this formalization task.
