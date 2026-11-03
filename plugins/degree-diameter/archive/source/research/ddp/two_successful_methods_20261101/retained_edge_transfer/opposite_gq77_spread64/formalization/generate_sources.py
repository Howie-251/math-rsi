import json
from pathlib import Path

R = Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
D = Path(__file__).resolve().parent
P = D.parent
F = R / 'formal/DegreeDiameter/Portfolio'
x = json.loads((P / 'PARAMETERS.json').read_text())
lp = [l['points'] for l in x['lines']]
pl = x['point_incident_lines']
spread = x['spread_line_labels']
owner = x['point_spread_owner']
rows = json.loads((P / 'PROJECTION_INDEX_INPUTS.json').read_text())['point_rows']
assert len(lp) == len(pl) == len(owner) == len(rows) == 400
assert len(spread) == 50
assert all(len(a) == 8 and all(0 <= v < 400 for v in a) for a in lp + pl)
assert all(0 <= v < 400 for v in spread)
assert all(0 <= v < 50 for v in owner)
assert all(len(a) == 400 and all(len(t) == 3 and all(0 <= v < 8 for v in t) for t in a) for a in rows)

def vec(a):
    return '![' + ', '.join(map(str, a)) + ']'

def blocked(a, render=str):
    assert len(a) == 400
    return vec([vec([render(v) for v in a[i:i+20]]) for i in range(0, 400, 20)])

header = '''namespace DegreeDiameter.Portfolio.OppositeGQ77Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
'''
tail = 'end DegreeDiameter.Portfolio.OppositeGQ77Spread\n'
defs = '''import DegreeDiameter.Portfolio.OppositeIncidenceSpreadFamily
''' + header + '''abbrev Point := Fin 400
abbrev Line := Fin 400
abbrev Old := Fin 160000
abbrev New := Fin 50
abbrev Vertex := Old ⊕ New

/-- Row-major blocking changes lookup cost only. Index n is row 20*(n/20)+(n%20). -/
def lookup400 {α : Type*} (table : Fin 20 → Fin 20 → α) (n : Fin 400) : α :=
  let ij := (finProdFinEquiv (m:=20) (n:=20)).symm n
  table ij.1 ij.2

/-- Literal PARAMETERS incidence, with the original point/line labels.
The field geometry is externally bound; this definition asserts no ZMod49 arithmetic. -/
'''
defs += 'def linePointBlocks : Fin 20 → Fin 20 → Fin 8 → Point := ' + blocked(lp, vec) + '\n'
defs += 'def linePoint (l : Line) : Fin 8 → Point := lookup400 linePointBlocks l\n'
defs += 'def pointLineBlocks : Fin 20 → Fin 20 → Fin 8 → Line := ' + blocked(pl, vec) + '\n'
defs += 'def pointLine (p : Point) : Fin 8 → Line := lookup400 pointLineBlocks p\n'
defs += 'def spread : New → Line := ' + vec(spread) + '\n'
defs += 'def spreadOwnerBlocks : Fin 20 → Fin 20 → New := ' + blocked(owner) + '\n'
defs += 'def spreadOwner (p : Point) : New := lookup400 spreadOwnerBlocks p\n'
defs += '''
abbrev Inc (p : Point) (l : Line) : Prop := OppositeIncidenceSpread.Inc linePoint p l
instance : DecidableRel Inc := inferInstanceAs (DecidableRel (OppositeIncidenceSpread.Inc linePoint))
def oldEquiv : Old ≃ Point × Line := (finProdFinEquiv (m:=400) (n:=400)).symm
def old (p : Point) (l : Line) : Old := oldEquiv.symm (p,l)
def graph : SimpleGraph Vertex := OppositeIncidenceSpread.graph oldEquiv linePoint spread
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (OppositeIncidenceSpread.graph oldEquiv linePoint spread).Adj)
def label : Vertex ≃ Fin 160050 := finSumFinEquiv
theorem old_label (p : Point) (l : Line) : (old p l).val = l.val+400*p.val := rfl
theorem label_old (v : Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : New) : (label (.inr j)).val = 160000+j.val := rfl
theorem card_vertex : Fintype.card Vertex = 160050 := by
  simp only [Fintype.card_sum,Fintype.card_fin]
def FinalClaim : Prop := Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print graph
#print Inc
#print oldEquiv
#print label
#print FinalClaim
''' + tail
(F / 'OppositeGQ77SpreadDefinitions.lean').write_text(defs)

# Explicit inverse positions eliminate an existential search at each positive entry.
lp_pos = [[pl[p].index(l) for p in pts] for l, pts in enumerate(lp)]
pl_pos = [[lp[l].index(p) for l in lines] for p, lines in enumerate(pl)]
data = 'import DegreeDiameter.Portfolio.OppositeGQ77SpreadDefinitions\n' + header
data += 'def lpPositionBlocks : Fin 20 → Fin 20 → Fin 8 → Fin 8 := ' + blocked(lp_pos, vec) + '\n'
data += 'def lpPosition (l : Line) : Fin 8 → Fin 8 := lookup400 lpPositionBlocks l\n'
data += 'def plPositionBlocks : Fin 20 → Fin 20 → Fin 8 → Fin 8 := ' + blocked(pl_pos, vec) + '\n'
data += 'def plPosition (p : Point) : Fin 8 → Fin 8 := lookup400 plPositionBlocks p\n'
data += '''def blockIndex (k : Fin 8) (r : Fin 50) : Fin 400 := finProdFinEquiv (k,r)
def IncidenceChunkCheck (k : Fin 8) : Prop :=
  (∀ r i, pointLine (linePoint (blockIndex k r) i) (lpPosition (blockIndex k r) i) = blockIndex k r) ∧
  (∀ r i, linePoint (pointLine (blockIndex k r) i) (plPosition (blockIndex k r) i) = blockIndex k r)
''' + tail
(F / 'OppositeGQ77SpreadIncidenceData.lean').write_text(data)
for k in range(8):
    (F / f'OppositeGQ77SpreadIncidenceChunk{k}.lean').write_text(
        'import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceData\n' + header +
        f'theorem incidence_chunk_{k} : IncidenceChunkCheck {k} := by\n  unfold IncidenceChunkCheck\n  decide\n' + tail)

inc = ''.join(f'import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk{k}\n' for k in range(8))
inc += 'import Mathlib.Tactic.FinCases\n' + header
inc += '''theorem incidence_chunks : ∀ k, IncidenceChunkCheck k := by
  intro k
  fin_cases k
''' + ''.join(f'  · exact incidence_chunk_{k}\n' for k in range(8))
inc += '''theorem pointLine_inverse (l : Line) (i : Fin 8) :
    pointLine (linePoint l i) (lpPosition l i) = l := by
  let kr := (finProdFinEquiv (m:=8) (n:=50)).symm l
  have h := (incidence_chunks kr.1).1 kr.2 i
  simpa only [blockIndex,kr,Prod.mk.eta,Equiv.apply_symm_apply] using h
theorem pointLine_covers : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  rintro p l ⟨i,rfl⟩
  exact ⟨lpPosition l i,pointLine_inverse l i⟩
theorem pointLine_sound (p : Point) (j : Fin 8) : Inc p (pointLine p j) := by
  let kr := (finProdFinEquiv (m:=8) (n:=50)).symm p
  have h := (incidence_chunks kr.1).2 kr.2 j
  refine ⟨plPosition p j,?_⟩
  simpa only [blockIndex,kr,Prod.mk.eta,Equiv.apply_symm_apply] using h
theorem spread_owner_on_rows : ∀ j i, spreadOwner (linePoint (spread j) i) = j := by decide
theorem spread_unique : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  rintro p j ⟨i,rfl⟩
  exact (spread_owner_on_rows j i).symm
#print axioms pointLine_covers
#print axioms pointLine_sound
#print axioms spread_unique
''' + tail
(F / 'OppositeGQ77SpreadIncidence.lean').write_text(inc)

iface = 'import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidence\n' + header + '''
/-- Three actual Fin8 positions. First and second incidences come from membership
and shared soundness; the remaining equality is discharged in each concrete row. -/
def ProjectionIndexCheck (p : Point) (ix : Line → Fin 8 × Fin 8 × Fin 8) : Prop :=
  ∀ l, linePoint (pointLine p (ix l).2.1) (ix l).2.2 = linePoint l (ix l).1
def ProjectionRow (p : Point) : Prop := ∀ l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m
theorem projection_row_of_check (p : Point) (ix : Line → Fin 8 × Fin 8 × Fin 8)
    (h : ProjectionIndexCheck p ix) : ProjectionRow p := by
  intro l
  exact ⟨linePoint l (ix l).1,pointLine p (ix l).2.1,
    ⟨(ix l).1,rfl⟩,pointLine_sound p (ix l).2.1,⟨(ix l).2.2,h l⟩⟩
#print axioms projection_row_of_check
''' + tail
(F / 'OppositeGQ77SpreadInputInterface.lean').write_text(iface)
for p, row in enumerate(rows):
    name = f'{p:03}'
    s = 'import DegreeDiameter.Portfolio.OppositeGQ77SpreadInputInterface\n' + header
    s += f'def projectionIndicesBlocks{name} : Fin 20 → Fin 20 → Fin 8 × Fin 8 × Fin 8 := '
    s += blocked(row, lambda t: '(' + ','.join(map(str,t)) + ')') + '\n'
    s += f'def projectionIndices{name} (l : Line) : Fin 8 × Fin 8 × Fin 8 := lookup400 projectionIndicesBlocks{name} l\n'
    s += f'theorem projection_check_{name} : ProjectionIndexCheck {p} projectionIndices{name} := by\n  unfold ProjectionIndexCheck\n  decide\n'
    s += f'theorem projection_row_{name} : ProjectionRow {p} :=\n  projection_row_of_check {p} projectionIndices{name} projection_check_{name}\n'
    s += tail
    (F / f'OppositeGQ77SpreadInputRow{name}.lean').write_text(s)

inputs = ''.join(f'import DegreeDiameter.Portfolio.OppositeGQ77SpreadInputRow{p:03}\n' for p in range(400))
inputs += 'import Mathlib.Tactic.FinCases\n' + header
inputs += 'theorem projection_rows : ∀ p, ProjectionRow p := by\n  intro p\n  fin_cases p\n'
inputs += ''.join(f'  · exact projection_row_{p:03}\n' for p in range(400))
inputs += 'theorem projection : ∀ p l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m := projection_rows\n#print axioms projection\n' + tail
(F / 'OppositeGQ77SpreadInputs.lean').write_text(inputs)
exact = 'import DegreeDiameter.Portfolio.OppositeGQ77SpreadInputs\n' + header + '''
/-- All finite hypotheses of the generic family are supplied by the fixed literal inputs. -/
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 := by
  have h := OppositeIncidenceSpread.order_degree_and_exact_D3 oldEquiv linePoint pointLine spread spreadOwner
    (by decide) pointLine_covers spread_unique projection (by decide)
  simpa only [Fintype.card_fin] using h
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
''' + tail
(F / 'OppositeGQ77SpreadExact.lean').write_text(exact)
audit = '''import DegreeDiameter.Portfolio.OppositeGQ77SpreadExact
open DegreeDiameter.Portfolio
#print OppositeGQSpread.graph
#print OppositeIncidenceSpread.Inc
#print OppositeGQ77Spread.graph
#print OppositeGQ77Spread.Inc
#print OppositeGQ77Spread.oldEquiv
#print OppositeGQ77Spread.label
#print OppositeGQ77Spread.spread
#check OppositeGQ77Spread.old_label
#check OppositeGQ77Spread.label_old
#check OppositeGQ77Spread.label_new
#check OppositeGQ77Spread.concrete_order_degree_and_exact_D3
#print OppositeGQ77Spread.concrete_order_degree_and_exact_D3
#print OppositeGQ77Spread.FinalClaim
#print axioms OppositeGQ77Spread.concrete_order_degree_and_exact_D3
#print axioms OppositeGQ77Spread.final_claim
'''
(R / 'formal/OppositeGQ77SpreadAudit.lean').write_text(audit)
(D / 'GENERATION_RESULT.json').write_text(json.dumps({
    'actual_PARAMETERS_read': True, 'linePoint_entries': 3200, 'pointLine_entries': 3200,
    'ordered_spread_entries': 50, 'spreadOwner_entries': 400,
    'projection_triples': 160000, 'all_literal_Fin_inputs_in_bounds_before_emission': True,
    'lookup_layout': '20x20 row-major for unchanged Fin400 index',
    'old_modules_changed_or_recompiled': False, 'kernel_status': 'NOT_YET_COMPILED',
    'remaining': 'definitions, positive incidence chunks, row000/399 probes then bounded remaining rows and final import'
}, indent=2) + '\n')
print('Generated actual definitions, incidence, 400 projection rows and exact/audit targets.')
