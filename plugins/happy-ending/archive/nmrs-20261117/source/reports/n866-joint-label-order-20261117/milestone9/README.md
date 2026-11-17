# Standalone nine-hole matrix milestone

This immutable package reconstructs all 115 necessary rows from actual Ferrers
cell sets and 11 checked shared-label kernels, checks the exact <=8 counter,
replays every kernel proof and the final proof, and verifies a nine-hole vector.
It also replays the two-cell shared-pair certificate and its two unit branches.

Run on Linux with an existing Python 3 and drat-trim, for example:

```bash
python3 verify.py --directory . --checker /path/to/drat-trim
```

The packet-to-path/state-label interfaces are the mathematical caller; no
geometric realization, independent external acceptance or actual 61-point
construction is claimed. The <=8 exclusion is checked; the nine-hole vector is
only a feasible vector for this necessary matrix. Higher-budget work belongs
in a new appendix and does not modify this milestone.
