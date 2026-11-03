import json
from pathlib import Path
from time import process_time

start=process_time()
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
Q=R/'formal/DegreeDiameter/Portfolio';F=R/'formal'
prefix='GQ77Published33CloneFamily';ns='DegreeDiameter.Portfolio.'+prefix
selected=json.loads((D.parent.parent/'ACTUAL_POINTS.json').read_text())['point_ids']
geometry=json.loads((D.parent.parent.parent/'PARAMETERS.json').read_text())
lines=[r['points']for r in geometry['lines']]
owner=['none']*400
for i,p in enumerate(selected):owner[p]='some '+str(i)
lineindex=[]
for line in lines:
    indices=[i for i,p in enumerate(selected)if p in line]
    assert len(indices)<=1
    lineindex.append(str(indices[0]if indices else 0))
def vec(v):return '!['+', '.join(v)+']'
def blocks(v):return vec([vec(v[i:i+20])for i in range(0,400,20)])
defs=f'''import DegreeDiameter.Portfolio.OppositeGQ77SpreadDefinitions
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace {ns}
namespace Source
abbrev Vertex := OppositeGQ77Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev BaseIndex := Fin 1650
abbrev CloneIndex (k : Nat) := Fin k × BaseIndex
abbrev Vertex (k : Nat) := Source.Vertex ⊕ CloneIndex k
/-- An explicit reproduction of the published size33, in the immutable source's point order. -/
def ovoid : Fin 33 → OppositeGQ77Spread.Point := {vec(list(map(str,selected)))}
def baseLabel : (Fin 33 × Fin 50) ≃ BaseIndex := finProdFinEquiv
def basePair : BaseIndex ≃ (Fin 33 × Fin 50) := baseLabel.symm
def baseCenter (b : BaseIndex) : Source.Vertex :=
  OvoidSpreadCloneCapacity.center OppositeGQ77Spread.oldEquiv ovoid OppositeGQ77Spread.spread (basePair b)
/-- All copies retain their owner and its full neighborhood in the original160050 source. -/
def center (k : Nat) (j : CloneIndex k) : Source.Vertex := baseCenter j.2
def graph (k : Nat) : SimpleGraph (Vertex k) :=
  FullNeighborhoodClones.graph OppositeGQ77Spread.graph (center k)
instance (k : Nat) : DecidableRel (graph k).Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph OppositeGQ77Spread.graph (center k)).Adj)
def cloneLabel (k : Nat) : CloneIndex k ≃ Fin (1650*k) :=
  (finProdFinEquiv (m:=k) (n:=1650)).trans (finCongr (Nat.mul_comm k 1650))
def label (k : Nat) : Vertex k ≃ Fin (160050+1650*k) :=
  (Equiv.sumCongr OppositeGQ77Spread.label (cloneLabel k)).trans finSumFinEquiv
theorem base_label (i : Fin 33) (j : Fin 50) :
    (baseLabel (i,j)).val = j.val+50*i.val := rfl
theorem clone_label (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (cloneLabel k (copy,base)).val = base.val+1650*copy.val := rfl
theorem center_source_label (b : BaseIndex) :
    (OppositeGQ77Spread.label (baseCenter b)).val =
      (OppositeGQ77Spread.spread (basePair b).2).val+400*(ovoid (basePair b).1).val := rfl
theorem label_old (k : Nat) (v : Source.Vertex) :
    (label k (.inl v)).val = (OppositeGQ77Spread.label v).val := rfl
theorem label_new (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (label k (.inr (copy,base))).val = 160050+1650*copy.val+base.val := by
  change 160050+(base.val+1650*copy.val) = _
  omega
theorem label_new_coordinates (k : Nat) (copy : Fin k) (i : Fin 33) (j : Fin 50) :
    (label k (.inr (copy,baseLabel (i,j)))).val =
      160050+1650*copy.val+50*i.val+j.val := by
  change 160050+((j.val+50*i.val)+1650*copy.val) = _
  omega
theorem card_vertex (k : Nat) : Fintype.card (Vertex k) = 160050+1650*k := by
  simp only [Vertex,CloneIndex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin]
  omega
def ovoidOwnerBlocks : Fin 20 → Fin 20 → Option (Fin 33) := {blocks(owner)}
def ovoidOwner (p : OppositeGQ77Spread.Point) : Option (Fin 33) :=
  OppositeGQ77Spread.lookup400 ovoidOwnerBlocks p
/-- Index0 on the136 unoccupied lines; the finite certificate uses an implication. -/
def lineOvoidIndexBlocks : Fin 20 → Fin 20 → Fin 33 := {blocks(lineindex)}
def lineOvoidIndex (l : OppositeGQ77Spread.Line) : Fin 33 :=
  OppositeGQ77Spread.lookup400 lineOvoidIndexBlocks l
def FinalClaim (k : Nat) : Prop := Fintype.card (Vertex k) = 160050+1650*k ∧
  (∀ v, (graph k).degree v ≤ 64+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2
#print ovoid
#print center
#print graph
#print label
#print FinalClaim
end {ns}
'''
(Q/(prefix+'Definitions.lean')).write_text(defs)
oldprefix='GQ77Cubic22Clone65'
for b in range(20):
    text=(Q/(oldprefix+f'InputChunk{b:02d}.lean')).read_text().replace(oldprefix,prefix)
    (Q/(prefix+f'InputChunk{b:02d}.lean')).write_text(text)
inputs=(Q/(oldprefix+'Inputs.lean')).read_text().replace(oldprefix,prefix).replace('Fin 22','Fin 33')
inputs=inputs.replace('load_le_one','base_load_le_one').replace('clonePair','basePair')
inputs=inputs.replace('graph center w','graph baseCenter w')
copyproof='''
theorem copy_load_le (k : Nat) (w : Source.Vertex) :
    FullNeighborhoodClones.load OppositeGQ77Spread.graph (center k) w ≤ k := by
  have hbase : ∀ x y : {b : BaseIndex // OppositeGQ77Spread.graph.Adj w (baseCenter b)}, x = y :=
    Fintype.card_le_one_iff.mp (base_load_le_one w)
  let copyIndex : {j : CloneIndex k // OppositeGQ77Spread.graph.Adj w (center k j)} → Fin k :=
    fun j => j.val.1
  have hinj : Function.Injective copyIndex := by
    intro x y hcopy
    have hbaseval : x.val.2 = y.val.2 :=
      congrArg Subtype.val (hbase ⟨x.val.2,x.property⟩ ⟨y.val.2,y.property⟩)
    apply Subtype.ext
    exact Prod.ext hcopy hbaseval
  have hcard := Fintype.card_le_of_injective copyIndex hinj
  simpa only [Fintype.card_fin] using hcard
#print axioms copy_load_le
'''
inputs=inputs.replace('end '+ns,copyproof+'end '+ns)
(Q/(prefix+'Inputs.lean')).write_text(inputs)
oldexact=(Q/(oldprefix+'Exact.lean')).read_text()
noisolated=oldexact[oldexact.index('theorem source_no_isolated'):oldexact.index('theorem old_walk_bound_iff')]
exact=f'''import DegreeDiameter.Portfolio.{prefix}Inputs
import DegreeDiameter.Portfolio.OppositeGQ77SpreadExact
namespace {ns}
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
'''+noisolated+'''
theorem old_walk_bound_iff (k : Nat) (u v : Source.Vertex) (n : Nat) :
    (∃ p : (graph k).Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : OppositeGQ77Spread.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff OppositeGQ77Spread.graph (center k) u v n
theorem degree_le (k : Nat) : ∀ v, (graph k).degree v ≤ 64+k :=
  FullNeighborhoodClones.degree_le OppositeGQ77Spread.graph (center k) 64 k
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.1 (copy_load_le k)
theorem diameterAtMost_three (k : Nat) : DiameterAtMost (graph k) 3 :=
  FullNeighborhoodClones.diameterAtMost OppositeGQ77Spread.graph (center k) 3 (by decide)
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated
theorem not_diameterAtMost_two (k : Nat) : ¬DiameterAtMost (graph k) 2 :=
  FullNeighborhoodClones.not_diameterAtMost OppositeGQ77Spread.graph (center k) 2
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.2
theorem fixed_family_target (k : Nat) : Fintype.card (Vertex k) = 160050+1650*k ∧
    (∀ v, (graph k).degree v ≤ 64+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2 :=
  ⟨card_vertex k,degree_le k,diameterAtMost_three k,not_diameterAtMost_two k⟩
theorem fixed_family_claim (k : Nat) : FinalClaim k := fixed_family_target k
'''
endpoints=[]
for k in range(1,9):
    degree=64+k;n=160050+1650*k;name=f'd{degree}_{n}';endpoints.append({'k':k,'degree':degree,'n':n,'theorem':name})
    target=f'Fintype.card (Vertex {k}) = {n} ∧ (∀ v, (graph {k}).degree v ≤ {degree}) ∧\n  DiameterAtMost (graph {k}) 3 ∧ ¬DiameterAtMost (graph {k}) 2'
    exact+=f'theorem {name} : {target} := fixed_family_target {k}\n'
    exact+=f'def FinalClaim{degree} : Prop := {target}\n'
    exact+=f'theorem final_claim{degree} : FinalClaim{degree} := {name}\n'
exact+='#print axioms fixed_family_target\nend '+ns+'\n'
(Q/(prefix+'Exact.lean')).write_text(exact)
audit=f'''import DegreeDiameter.Portfolio.{prefix}Exact
open DegreeDiameter.Portfolio
set_option pp.explicit true in
#print DiameterAtMost
#print OppositeGQ77Spread.Vertex
#print {prefix}.ovoid
#print {prefix}.baseCenter
#print {prefix}.center
#print {prefix}.graph
#print FullNeighborhoodClones.graph
#print {prefix}.label
'''
for name in ['base_label','clone_label','center_source_label','label_old','label_new','label_new_coordinates','ovoid_unique','base_load_le_one','copy_load_le','source_no_isolated','old_walk_bound_iff']:
    audit+=f'#check {prefix}.{name}\n'
for name in ['ovoid_unique','base_load_le_one','copy_load_le','old_walk_bound_iff']:
    audit+=f'#print axioms {prefix}.{name}\n'
for e in endpoints:
    k,degree,n,name=e['k'],e['degree'],e['n'],e['theorem']
    audit+=f'#check ({prefix}.label {k} : {prefix}.Vertex {k} ≃ Fin {n})\n'
    audit+=f'#check {prefix}.{name}\n#print {prefix}.{name}\n#print {prefix}.FinalClaim{degree}\n'
    audit+=f'#print axioms {prefix}.{name}\n#print axioms {prefix}.final_claim{degree}\n'
(F/(prefix+'Audit.lean')).write_text(audit)
compiler=(R/'research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/formalization/compile.py').read_text()
compiler=compiler.replace('F9U10PlaneCloneFamily',prefix).replace('spent+budget<=600','spent+budget<=900')
(D/'compile.py').write_text(compiler)
(D/'TARGETS.json').write_text(json.dumps({'namespace':ns,'actual_source_carrier':'OppositeGQ77Spread.Vertex = Fin160000 ⊕ Fin50','endpoints':endpoints},indent=2)+'\n')
(D/'PREPARATION_RESULT.json').write_text(json.dumps({'status':'NEW_SCOPE_SOURCES_WRITTEN','CPU_seconds':process_time()-start,'point_ids':selected,'old_modules_changed_or_recompiled':False,'finite_chunks':20,'finite_incidence_positions':3200},indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps({'status':'SOURCES_READY_DEFINITIONS_NOT_YET_COMPILED','running':False,'active_modules':[],'definitions_compiled':False,'finite_chunks_compiled':0,'exact_compiled':False,'audit_compiled':False,'independent_acceptance':'pending'},indent=2)+'\n')
print(json.dumps({'status':'SOURCES_WRITTEN','prefix':prefix,'CPU_seconds':process_time()-start,'modules':24,'point_ids':selected}))
