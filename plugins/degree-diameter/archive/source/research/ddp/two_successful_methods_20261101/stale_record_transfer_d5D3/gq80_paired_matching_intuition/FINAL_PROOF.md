# Final accepted paper scope: symmetric GQ80, with asymmetric boundary open

The source is the actual cached W(3,3) incidence graph,40 points+40 lines,160 edges. An arbitrary point perfect matching and line perfect matching would give80/200 and degree5. All mixed pairs and old same-side near pairs stay within3; the original1080 far clauses exactly describe the remaining pairs.

The actual common-C5 model is exact on its stated symmetry family:280 block variables,16 matching equations and216 far-orbit clauses, retaining collinear/concurrent blocks. Each side's65625 matching masks was completely saved. The capacity-alone proposal was refuted by114+113=227≥216; it supplied no exclusion by itself.

The later exact superset join pruned only strict capacity impossibilities and queried every remaining P mask against every eligible Q implicitly. All10769 P queries had empty Q intersections, remaining domain0. Therefore there is no D≤3 completion with both matchings invariant under the actual C5. The full proof, program/receipt review and exact stopping boundary are in `PAPER_C5_JOINT_GATE.md`. Sylow5 conjugacy in Sp4(F3) extends the same NO to any pair with some common order-five symplectic subgroup. No arbitrary-matching WLOG is asserted.

The asymmetric fixed-Q/free-P model is a genuine broader rule: it permits a non-C5 point matching, keeps one selected invariant line matching, and uses the same exact original far clauses and full-valid route cuts. Its encoding is reviewed in `PAPER_ASYMMETRIC_QFIX_INTERFACE.md`. That file does not turn a solver timeout, invalid invocation or unproved raw UNSAT into a general exclusion. Other fixed Q choices and the full unrestricted family remain outside the symmetric NO.

This file introduces no new graph/parameter/Lean count. No source, geometry, field, complete matching enumeration, joint query, BFS or solver was repeated for this paper. Historical UNKNOWN windows, the refuted capacity-only prediction and the complete C5 NO are retained as distinct evidence.


Actual asymmetric follow-up: the one fixedQ1361 model returned raw solverUNSAT/exit20 after a legal invocation, with no proof trace; cumulative4.886162516/30CPU includes the two execution-interface failures. It is not incorporated into the strict unrestricted or all-Q NO scope. See the final section of `PAPER_ASYMMETRIC_QFIX_INTERFACE.md` for exact limits.
