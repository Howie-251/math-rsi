<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Near-diagonal 867/868 evidence

The original-input short proof is in
[N8_NEAR_DIAGONAL_STRUCTURAL_SLICES_20261119.md](../N8_NEAR_DIAGONAL_STRUCTURAL_SLICES_20261119.md),
section 4. It proves ordinary 868 <= 164 from saturated 858 endpoints and actual
shared-pair growth. The computational query independently checks the same
necessary-state contradiction. No external review occurred.

All scientific runs used the authoritative Linux project root and
`<private-python-runtime>`. Native template source and frozen
866 imports are read-only and hash-bound in the exported rows. No actual-P
endpoint units from a derived 866 formula were imported.

`near-diagonal-evidence.tar.gz` retains full row snapshots, CNFs, 868 DRAT proof,
solver/checker logs, the tiny extracted proof and exact full-coordinate
enumeration. `evidence-manifest.json` binds every retained source file by hash.
`results.json` gives both final statuses and the archive hash.

After extracting the archive on Linux, replay the successful proof with:

```bash
<private-artifact-root> 868-native-local01/formula.cnf 868-native-local01/proof.drat
<private-artifact-root> short-conflict01/formula.cnf short-conflict01/proof.drat
```

To regenerate in a fresh scoped directory, place `probe.py` there and run:

```bash
<private-python-runtime> probe.py --case 868
<private-python-runtime> analyze_full_faces.py
```

Output directories are create-only. The 867 query returned UNKNOWN after its
single new 45-second controlled AE call; it was not re-budgeted or retried.
The full-coordinate conflict hypergraph has minimum transversal two and maximum
directly surviving full-coordinate count eight. Of 210 six-full-coordinate sets,
four directly conflict. This does not exclude population 164 or improve 867.

`classify_164.py` and `n164-defect-designs.json` were added after the archived
proof package. They enumerate all 2,505 degree-defect designs, verify the degree
identities exactly, and retain 2,405 after the four proven full-face conflicts.
They do not certify occupancy feasibility. Their separate execution receipt is
`classify164.json`; the earlier evidence archive remains unchanged.
