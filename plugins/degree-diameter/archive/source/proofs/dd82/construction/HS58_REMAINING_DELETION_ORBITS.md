# HS58: complete adjacent and cross deletion-pair orbits

Date: 2026-10-12. This result supplies deletion normalization for HS58
augmentation; it is not an UNSAT result for the remaining augmentations.

Let Q be the saved Hoffman–Singleton graph on 0,...,49. Reuse exactly
the six explicitly verified automorphisms in
`computations/dd82/construction/hs58_no_cross_deletion_orbit_run/generators.json`.
Their bijectivity and equality of the complete image edge set with Q
were established in the preceding no-cross run. No new automorphism
search was performed and that no-cross orbit was not repeated.

The new source
`computations/dd82/construction/hs58_remaining_deletion_orbits.py`
directly enumerates unordered pairs of distinct original edges into:

* adjacent pairs, whose two edges share a vertex;
* cross pairs, whose edges are disjoint but have an original Q edge
  between their endpoint sets.

It independently traverses the saved generators' action from each
chosen representative and compares the resulting set with the entire
corresponding direct domain. The completed results are:

| Domain | Representative D | Direct domain | Orbit | Missing |
| --- | --- | ---: | ---: | ---: |
| Adjacent | {01,04} | 1050 | 1050 | 0 |
| Cross | {01,23} | 6300 | 6300 | 0 |

Both orbits stay in their stated domains and are closed under all six
generators. This establishes transitivity of the generated subgroup
on each domain; no assertion about the order or completeness of that
subgroup inside Aut(Q) is needed.

The exact evidence is under
`computations/dd82/construction/hs58_remaining_deletion_orbits_run/`:

* `result.json`: completed direct-domain and orbit counts;
* `adjacent.orbit.json` and `cross.orbit.json`: every deletion pair,
  with its predecessor state index and zero-based generator index;
* `resources.json`: actual process resources.

Following predecessor entries from any state to the root gives an
explicit word carrying the representative to that state. Inverting
the word normalizes the deletion pair. The one pinned-CPU run had a
2-second soft / 3-second hard CPU limit and exited successfully.
Internal CPU/wall were 0.177009687 / 0.1793174259364605 seconds;
cumulative process CPU, including imports, was 0.218311 seconds.
The resource wall measured from entry to `main` through saving the
orbit/result files was 0.1799652762711048 seconds. These distinct
measurement scopes are not interchanged.

For candidate preservation, transport every old vertex, original
nonedge addition, and port under the resulting Q automorphism. This
maps an arbitrary adjacent or cross deletion pair to the corresponding
fixed D without restricting additions or attachments. Independently,
the eight new vertices may be relabeled to put H into its stored
canonical representative. Since all old-new attachments are free in
`hs58_a5_remaining_joint.py`, these two relabelings are compatible.
Thus a candidate in either geometry maps into its corresponding
67-selector CNF, conditional on the already recorded auxiliary-domain
reductions and the encoding verification. Orbit coverage alone does
not decide whether either CNF is satisfiable.
