# GQ160050 checkpoint B: actual finite-to-generic connection

New actual finite scope; accepted old generic source is reused unchanged.
Review does not depend on reading or rerunning a 5121600-edge table.

Read these actual sources:
- `formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadDefinitions.lean`
- `OppositeGQ77SpreadIncidenceData.lean`, `IncidenceChunk0..7.lean`, `Incidence.lean`
- `OppositeGQ77SpreadInputInterface.lean`
- representative `OppositeGQ77SpreadInputRow000.lean` and `InputRow399.lean`
- actual caller `OppositeGQ77SpreadExact.lean` (full assembly still pending)
- reused `OppositeIncidenceSpreadFamily.lean`, `OppositeIncidenceSpreadSlots.lean`,
  `OppositeGQ35SpreadWalks.lean`, `OppositeGQ35SpreadLowerGeneric.lean`.
All paths above after the first are in the same formal Portfolio directory.

Actual finite facts already kernel compiled:
1. `IncidenceChunk0..7`: all3200 LP entries have the supplied inverse position
   in the actual PL row, and all3200 PL entries have their supplied position in
   the actual LP row. Each certificate checks equality, with no existential scan.
2. `Incidence.pointLine_covers` combines the8×50 decomposition of Fin400 with
   those inverse equalities. `Prod.mk.eta` and the actual fin-product inverse
   identity close the return to an arbitrary original Fin400 label.
3. `pointLine_sound` proves every PL row entry is an actual Inc.
4. `spread_owner_on_rows` checks all50×8 actual spread incidences, and
   `spread_unique` derives the precise generic owner-index obligation.
5. `InputInterface.projection_row_of_check` constructs actual q,m and all3 Inc
   proofs from three supplied Fin8 positions plus a single equality. Shared PL
   soundness supplies p∈m; q∈l is membership by definition; q∈m is the equality.

Per-pair equality is
`linePoint (pointLine p (ix l).2.1) (ix l).2.2 = linePoint l (ix l).1`.
The triple positions have their original meaning and ordering. Blocking the
400 line indices into20×20 storage does not alter any mathematical index.

Execution status is the current `*_RESULT.json`, not the age of this packet.
Definitions, all8 chunks, Incidence and InputInterface actually PASS. Probe
rows000/399 both actually PASS (9.763804/16.876899 CPU); remaining398 rows have
not been claimed compiled by this packet. See PREPARATION_RESULT.json. No old module has been changed/recompiled.

The final caller will pass actual `pointLine_covers`, `spread_unique`, and
universal `projection` into the already compiled Family theorem. Its output is
cardinality160050, degree≤8*8, true-Walk D3 and non-D2. The latter uses the shared
finite forward-neighbor cover and radius-two endpoint-cardinality upper bound,
not a graph BFS. No user-supplied geometry, capacity or success premise remains
on the new concrete target.

Actual input/formula correspondence is in INPUT_BINDING.md and the PASS receipt
INPUT_BINDING_CHECK.json: all6400 incidence entries,50 original ordered spread
labels,400 owners,160000 triples,50×64 ordered pins and every5121600 literal edge
match. That is external correspondence only; the certificate truth and actual
caller closure are the separate kernel obligations above.

Please attack the actual index semantics, inverse-position coverage, owner
quantifiers and projection-to-Inc connection. Do not infer this new input scope
was reviewed merely because the older7242 graph used the same generic theorem.
