# GQ(7,7) spread extension: actual encoding checkpoint A

This scope is a new concrete instance. The accepted 6160/7242 reviews establish no
review verdict for these new literal tables. Root coordinates the external review.

Actual definition source:
`formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadDefinitions.lean`.
The bodies have been generated from the actual frozen `../PARAMETERS.json`, not
from an anticipated field geometry. `GENERATION_RESULT.json` records input sizes
and range checks. No field structure or `ZMod49` is introduced in Lean.

The graph carrier is `Vertex := Fin 160000 ⊕ Fin 50`. `oldEquiv` is the inverse of
`finProdFinEquiv` for 400×400, so old `(p,l)` has value `400*p+l`.
`label : Vertex ≃ Fin 160050 := finSumFinEquiv` gives old labels unchanged and
new `j` label `160000+j`; the corresponding three label theorems are `rfl`.

`linePointBlocks` and `pointLineBlocks` contain all 3200 entries each, in the
PARAMETERS order. `lookup400 table n` uses the pair decomposition 20×20 of the
same Fin400 index; blocking affects lookup cost only. Incidence is exactly
`∃ i : Fin 8, linePoint l i = p`. `spread` has the original 50 GF49 slope-order
line labels, and `spreadOwner` has the original 400 owner indices. Spread is not
sorted. The coordinate/field explanation is an external binding of these labels,
not a Lean field-existence premise.

Actual graph body follows these compiled generic definitions:
- `OppositeIncidenceSpreadSlots.lean`: `Inc`, `graph`.
- `OppositeGQ35SpreadGeneric.lean`: `OppositeGQSpread.graph`.
Old-old adjacency means distinct old vertices `(p,l),(q,m)` with `Inc p m` and
`Inc q l`. Old-new means the old vertex is a flag and its point is on spread j.
New-new is false. These are the same formulas as the actual producer parameters.

Proposed concrete target (actual source written but not yet compiled):
`OppositeGQ77SpreadExact.lean`:
```
theorem concrete_order_degree_and_exact_D3 :
  Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```
There is no user certificate or geometry hypothesis on this theorem.
`DiameterAtMost` is the existing true-Walk project definition.
`OppositeGQ77SpreadAudit.lean` separately imports the entrypoint and prints the
actual final type, bodies and transitive axioms after assembly.

Highest unclosed interface:
`OppositeIncidenceSpread.order_degree_and_exact_D3` in
`OppositeIncidenceSpreadFamily.lean`. Its actual caller in new Exact supplies:
1. 0<8, by decide;
2. positive LP→PL coverage, from the new finite inverse-position equalities;
3. unique spread owner, from actual 50×8 spread row entries;
4. all 400×400 point-line projections, each checked by three Fin8 positions;
5. 1+64+64²<400*400+50, by decide.
The generic neighbor-slot proof supplies degree≤8*8, its genuine Walk proof
supplies D3, and its genuine Walk/cardinality lower bound supplies non-D2.

Finite proof organization:
`IncidenceData` defines actual inverse positions and 8 chunks of 50 rows.
`IncidenceChunk0..7` each check two sets of 400 positive equalities.
`Incidence` combines them and checks 400 owner entries.
`InputInterface` proves a projection from a single equality per pair plus shared
PL soundness. Each `InputRow000..399` contains one original point row; the row's
400 triples are blocked 20×20 without changing line index. Rows000 and399 are
first probes; no other row batch starts until measured and budgeted.

Current kernel status: Definitions actually PASS (12.299547 CPU); consult current
`*_RESULT.json` for subsequent finite modules. Positive incidence is in progress. This packet does not claim final compilation,
axiom audit, external review, literal acceptance, novelty or global record.
The complete literal binding now actually PASSes in `INPUT_BINDING_CHECK.json`: all
ordered inputs and pins plus 5121600 streamed edge-formula comparisons. This is a
finite external correspondence check, not an ASCII parser theorem. No BFS, solver, native_decide, extra axiom, hash or installation is used.
