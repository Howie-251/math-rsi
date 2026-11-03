import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
D=Path(__file__).resolve().parent;P=D.parent;S=P.parents[1]
t=time.process_time(); F=R/'formal'; Q=F/'DegreeDiameter/Portfolio'
p=json.loads((S/'PARAMETERS.json').read_text())
g=json.loads((P/'PRECHECK_RESULT.json').read_text())
ov=g['point_ids']; assert ov==[57,119,165,251,265,347,399,71,133,179,216,279,312,364,85,147,193,230,293,326,378,1]
owner=['none']*400
for i,x in enumerate(ov):owner[x]=f'some {i}'
line_index=[]
for row in p['lines']:
 pts=row['points']
 found=[ov.index(x) for x in pts if x in ov]
 assert len(found)<=1
 line_index.append(str(found[0] if found else 0))
def vec(x):return '!['+', '.join(x)+']'
def blocks(x):return vec([vec(x[j:j+20]) for j in range(0,400,20)])
prefix='GQ77Cubic22Clone65';ns='DegreeDiameter.Portfolio.'+prefix
defs=f'''import DegreeDiameter.Portfolio.OppositeGQ77SpreadDefinitions
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace {ns}
namespace Source
abbrev Vertex := OppositeGQ77Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev CloneIndex := Fin 1100
abbrev Vertex := Source.Vertex ⊕ CloneIndex
/-- The literal ordered three cubic cosets and infinity, bound externally to GF7 geometry. -/
def ovoid : Fin 22 → OppositeGQ77Spread.Point := {vec(list(map(str,ov)))}
def cloneLabel : (Fin 22 × Fin 50) ≃ CloneIndex := finProdFinEquiv
def clonePair : CloneIndex ≃ (Fin 22 × Fin 50) := cloneLabel.symm
/-- Fixed original160050-source owners; point index outer, original spread index inner.
Every clone uses the immutable original source neighborhood, including its original bonuses. -/
def center (k : CloneIndex) : Source.Vertex :=
  OvoidSpreadCloneCapacity.center OppositeGQ77Spread.oldEquiv ovoid OppositeGQ77Spread.spread (clonePair k)
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph OppositeGQ77Spread.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph OppositeGQ77Spread.graph center).Adj)
def label : Vertex ≃ Fin 161150 :=
  (Equiv.sumCongr OppositeGQ77Spread.label (Equiv.refl CloneIndex)).trans finSumFinEquiv
theorem center_source_label (k : CloneIndex) :
    (OppositeGQ77Spread.label (center k)).val =
      (OppositeGQ77Spread.spread (clonePair k).2).val+400*(ovoid (clonePair k).1).val := rfl
theorem clone_label (i : Fin 22) (j : Fin 50) : (cloneLabel (i,j)).val = j.val+50*i.val := rfl
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (OppositeGQ77Spread.label v).val := rfl
theorem label_new (k : CloneIndex) : (label (.inr k)).val = 160050+k.val := rfl
theorem card_vertex : Fintype.card Vertex = 161150 := by
  simp only [Fintype.card_sum,Fintype.card_fin]
/-- Auxiliary finite certificate records the unique chosen point index, when present. -/
def ovoidOwnerBlocks : Fin 20 → Fin 20 → Option (Fin 22) := {blocks(owner)}
def ovoidOwner (p : OppositeGQ77Spread.Point) : Option (Fin 22) :=
  OppositeGQ77Spread.lookup400 ovoidOwnerBlocks p
/-- Arbitrary index0 for the224 unoccupied lines; used only in an implication. -/
def lineOvoidIndexBlocks : Fin 20 → Fin 20 → Fin 22 := {blocks(line_index)}
def lineOvoidIndex (l : OppositeGQ77Spread.Line) : Fin 22 :=
  OppositeGQ77Spread.lookup400 lineOvoidIndexBlocks l
def FinalClaim : Prop := Fintype.card Vertex = 161150 ∧ (∀ v, graph.degree v ≤ 65) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end {ns}
'''
(Q/(prefix+'Definitions.lean')).write_text(defs)
for b in range(20):
 text=f'''import DegreeDiameter.Portfolio.{prefix}Definitions
namespace {ns}
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Literal20-line block:160 incidence positions; no native computation oracle. -/
theorem line_index_chunk_{b:02d} : ∀ (j : Fin 20) (k : Fin 8),
    let l := (finProdFinEquiv (m:=20) (n:=20)) (({b} : Fin 20),j)
    ovoidOwner (OppositeGQ77Spread.linePoint l k) = none ∨
      ovoidOwner (OppositeGQ77Spread.linePoint l k) = some (lineOvoidIndex l) := by decide
#print axioms line_index_chunk_{b:02d}
end {ns}
'''
 (Q/(prefix+f'InputChunk{b:02d}.lean')).write_text(text)
# The exact module follows the completed7531 proof pattern, with a literal Fin1100 carrier.
old=(Q/'OvoidProduct26Exact.lean').read_text()
exact=old.replace('OvoidProduct26',prefix).replace('OppositeGQ44Spread','OppositeGQ77Spread').replace('twenty_six','sixty_five').replace('7531','161150').replace('≤ 26','≤ 65').replace(' center 25 1',' center 64 1')
exact='import DegreeDiameter.Portfolio.OppositeGQ77SpreadExact\n'+exact
(Q/(prefix+'Exact.lean')).write_text(exact)
imports='import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidence\n'+''.join(f'import DegreeDiameter.Portfolio.{prefix}InputChunk{b:02d}\n' for b in range(20))
inputs=imports+f'''namespace {ns}
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem owner_of_ovoid : ∀ i, ovoidOwner (ovoid i) = some i := by decide
theorem line_index_certificate : ∀ l k,
    ovoidOwner (OppositeGQ77Spread.linePoint l k) = none ∨
      ovoidOwner (OppositeGQ77Spread.linePoint l k) = some (lineOvoidIndex l) := by
  intro l
  obtain ⟨b,j⟩ := cloneBlock l
  fin_cases b
'''
# An explicit20×20 equivalence avoids a400-way tactic split.
inputs=inputs.replace('  obtain ⟨b,j⟩ := cloneBlock l\n', '''  let e := (finProdFinEquiv (m:=20) (n:=20))
  obtain ⟨⟨b,j⟩,rfl⟩ := e.surjective l
''')
inputs+=''.join(f'  · exact line_index_chunk_{b:02d} j\n' for b in range(20))
inputs+=f'''
theorem ovoid_index_of_incidence (l : OppositeGQ77Spread.Line) (i : Fin 22)
    (h : OppositeGQ77Spread.Inc (ovoid i) l) : i = lineOvoidIndex l := by
  obtain ⟨k,hk⟩ := h
  have hi : ovoidOwner (OppositeGQ77Spread.linePoint l k) = some i := by
    rw [hk]
    exact owner_of_ovoid i
  rcases line_index_certificate l k with hnone | hsome
  · rw [hnone] at hi
    cases hi
  · exact Option.some.inj (hi.symm.trans hsome)
theorem ovoid_unique : ∀ l i i', OppositeGQ77Spread.Inc (ovoid i) l →
    OppositeGQ77Spread.Inc (ovoid i') l → i = i' := by
  intro l i i' hi hi'
  exact (ovoid_index_of_incidence l i hi).trans (ovoid_index_of_incidence l i' hi').symm
theorem spread_unique : ∀ p j j', OppositeGQ77Spread.Inc p (OppositeGQ77Spread.spread j) →
    OppositeGQ77Spread.Inc p (OppositeGQ77Spread.spread j') → j = j' := by
  intro p j j' hj hj'
  exact (OppositeGQ77Spread.spread_unique p j hj).trans (OppositeGQ77Spread.spread_unique p j' hj').symm
theorem load_le_one (w : Source.Vertex) : FullNeighborhoodClones.load OppositeGQ77Spread.graph center w ≤ 1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  apply clonePair.injective
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique OppositeGQ77Spread.oldEquiv
    OppositeGQ77Spread.Inc ovoid OppositeGQ77Spread.spread ovoid_unique spread_unique
    w (clonePair x.val) (clonePair y.val) x.property y.property
#print axioms ovoid_unique
#print axioms load_le_one
end {ns}
'''
(Q/(prefix+'Inputs.lean')).write_text(inputs)
audit=(F/'OvoidProduct26Audit.lean').read_text().replace('OvoidProduct26',prefix)
audit=audit.replace('open DegreeDiameter.Portfolio\n','open DegreeDiameter.Portfolio\nset_option pp.explicit true in\n#print DiameterAtMost\n')
audit=audit.replace(f'#check {prefix}.load_le_one\n',f'#check {prefix}.load_le_one\n#check {prefix}.ovoid_unique\n#check {prefix}.source_no_isolated\n')
(F/(prefix+'Audit.lean')).write_text(audit)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(dict(status='GENERATED_NEW_SCOPE_ONLY',CPU_seconds=time.process_time()-t,source_modules_changed=False,source_oleans_recompiled=False,chosen_points=ov,carrier='(Fin160000⊕Fin50)⊕Fin1100',finite_certificate_checks=3200),indent=2)+'\n')
print('Generated definitions,20 bounded finite chunks,inputs,exact,and independent audit.')
