import ast,json,re,time
from pathlib import Path
started=time.process_time()
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
F=R/'formal'; P=F/'DegreeDiameter/Portfolio'; G=D.parent.parent
selected=json.loads((G/'controller_pack32_gate/SELECTED_BLOCKS.json').read_text())['selected_controllers']
assert len(selected)==32
source=(P/'F3Graph15552Definitions.lean').read_text()
controller=ast.literal_eval(re.search(r'def controllerData .*? := (.*?)\ndef matrixData',source,re.S).group(1).replace('#',''))
owners={controller[a][p]:(i,p) for i,a in enumerate(selected) for p in range(5)}
assert len(owners)==160
def balanced(lo,hi,indent='  '):
    if hi-lo==1:
        a,b=owners.get(lo,(0,0));return indent+f'({a}, {b})'
    m=(lo+hi)//2
    return indent+f'if n < {m} then\n'+balanced(lo,m,indent+'  ')+'\n'+indent+'else\n'+balanced(m,hi,indent+'  ')
defs='''import DegreeDiameter.Portfolio.F3Graph15552Definitions
namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
abbrev Vertex := Fin 15552 ⊕ Fin 864
def layerData : Array Nat := #SELECTED
def layer (i : Fin 32) : Fin 192 := ⟨layerData.getD i.val 0 %192,Nat.mod_lt _ (by decide)⟩
abbrev planeVec := Clone16389.planeVec
def center (j : Fin 864) : Fin 15552 :=
  liftAt (layer ⟨j.val/27,by have h:=j.isLt;omega⟩)
    (encodeVec (planeVec ⟨j.val%3,Nat.mod_lt _ (by decide)⟩
      ⟨j.val/3%3,Nat.mod_lt _ (by decide)⟩ ⟨j.val/9%3,Nat.mod_lt _ (by decide)⟩))
abbrev graph := FullNeighborhoodClones.graph F3Graph15552.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F3Graph15552.graph center).Adj)
def label : Vertex ≃ Fin 16416 := finSumFinEquiv
theorem label_new (j : Fin 864) : (label (.inr j)).val=15552+j.val := rfl
theorem label_old (v : Fin 15552) : (label (.inl v)).val=v.val := rfl
theorem center_label (j : Fin 864) : (center j).val =
    81*(layer ⟨j.val/27,by have h:=j.isLt;omega⟩).val +
      j.val%3+9*(j.val/3%3)+27*(j.val/9%3) := by
  simp [center,liftAt,encodeVec,planeVec,Clone16389.planeVec,
    ZMod.val_natCast,Nat.add_assoc]
def FinalClaim : Prop := Fintype.card Vertex=16416 ∧ (∀v,graph.degree v≤16) ∧
  DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3
#check (label : Vertex ≃ Fin 16416)
#print axioms label_new
end DegreeDiameter.Portfolio.F3Graph15552.Clone16416
'''.replace('#SELECTED','#'+str(selected))
(P/'F3Graph15552Clone16416Definitions.lean').write_text(defs)
old=(P/'F3Graph15552FullCloneInputs.lean').read_text()
tail=old[old.index('def cloneBlock'):].replace('837','864').replace('Fin 31','Fin 32').replace('Clone16389','Clone16416')
inputs='''import DegreeDiameter.Portfolio.F3Graph15552Clone16416Definitions
import DegreeDiameter.Portfolio.F3Graph15552FullCloneInputs
namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
open Clone16389 (recover recover_plane)
def ownerIndex (n : Nat) : Fin 32 × Fin 5 :=
'''+balanced(0,192)+'''
def owner (a : Fin 192) : Fin 32 × Fin 5 := ownerIndex a.val
/-- Only the new 32×5 positive table, including self-controller targets. -/
theorem owner_forward : ∀(i : Fin 32)(p : Fin 5),
    owner (controller (layer i) p)=(i,p) := by decide +kernel
'''+tail
(P/'F3Graph15552Clone16416Inputs.lean').write_text(inputs)
exact=(P/'F3Graph15552FullCloneExact.lean').read_text().replace('F3Graph15552FullCloneInputs','F3Graph15552Clone16416Inputs').replace('Clone16389','Clone16416').replace('16389','16416')
exact=exact.replace('theorem final_claim : FinalClaim := d16_16416','''theorem original_concrete_goal : Fintype.card Vertex=16416 ∧ (∀v,graph.degree v≤16) ∧
    (∀u v,∃w : graph.Walk u v,w.length≤4) ∧ ¬DiameterAtMost graph 3 := d16_16416
theorem final_claim : FinalClaim := original_concrete_goal''')
(P/'F3Graph15552Clone16416Exact.lean').write_text(exact)
audit=(F/'F3Graph15552FullCloneAudit.lean').read_text().replace('F3Graph15552FullCloneExact','F3Graph15552Clone16416Exact').replace('Clone16389','Clone16416').replace('16389','16416')
audit+='\n#print original_concrete_goal\n#print axioms original_concrete_goal\n#print axioms center_label\n'
(F/'F3Graph15552Clone16416Audit.lean').write_text(audit)
result=dict(status='FOUR_NEW_MODULE_SOURCES_READY',code_preparation_CPU_seconds=time.process_time()-started,
    initial_read_and_prediction_reserve_CPU_seconds=0.2,selected_controllers=selected,positive_owner_equations=160,
    modules=['F3Graph15552Clone16416'+s for s in ['Definitions','Inputs','Exact','Audit']],
    reused_symbolic_theorems=['Clone16389.recover_stepVec','Clone16389.recover_plane'],new_old_field_checks=0)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
