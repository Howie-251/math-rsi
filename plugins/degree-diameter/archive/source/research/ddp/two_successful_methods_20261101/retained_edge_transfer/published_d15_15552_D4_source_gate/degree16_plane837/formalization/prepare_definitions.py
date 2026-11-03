import json,os,re,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
gate=D.parent.parent
bound=json.loads((gate/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json').read_text())
params=json.loads((D.parent/'PARAMETERS.json').read_text())
def arr(x):return '#['+', '.join(arr(v)if isinstance(v,list)else str(v)for v in x)+']'
path=R/'formal/DegreeDiameter/Portfolio/F3Graph15552Definitions.lean';assert not path.exists()
data=('def controllerData : Array (Array Nat) := '+arr(bound['transition'])+'\n'+
      'def matrixData : Array (Array Nat) := '+arr([[v for row in t['B']for v in row]for t in bound['types']])+'\n'+
      'def directionData : Array (Array Nat) := '+arr([t['v']for t in bound['types']])+'\n'+
      'def constantData : Array (Array Nat) := '+arr([t['c']for t in bound['types']])+'\n')
text='''import DegreeDiameter.Portfolio.FullNeighborhoodClones
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
abbrev F := ZMod 3
abbrev Vec := Fin 4 → F
abbrev Mat := Fin 4 → Fin 4 → F
def basisVec (j : Fin 4) : Vec := fun i => if i=j then 1 else 0
def act (A : Mat) (x : Vec) : Vec := fun i =>
  A i 0*x 0+A i 1*x 1+A i 2*x 2+A i 3*x 3
'''+data+'''
def controller (a : Fin 192) (p : Fin 5) : Fin 192 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 %192,Nat.mod_lt _ (by decide)⟩
def matrix (p : Fin 5) : Mat := fun i j =>
  ((matrixData.getD p.val #[]).getD (4*i.val+j.val) 0 : F)
def direction (p : Fin 5) : Vec := fun i => ((directionData.getD p.val #[]).getD i.val 0 : F)
def constant (p : Fin 5) : Vec := fun i => ((constantData.getD p.val #[]).getD i.val 0 : F)
theorem constant_zero : ∀p,constant p=0 := by decide +kernel
def inverseType : Fin 5 → Fin 5 := ![0,3,4,1,2]
theorem controller_reverse_type : ∀a p,controller (controller a p) (inverseType p)=a := by decide +kernel
def encodeVec (x : Vec) : Fin 81 :=
  ⟨(x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val,by
    have h0:=ZMod.val_lt (x 0);have h1:=ZMod.val_lt (x 1)
    have h2:=ZMod.val_lt (x 2);have h3:=ZMod.val_lt (x 3)
    omega⟩
def decodeVec (x : Fin 81) : Vec := fun i => (x.val/3^i.val%3 : Nat)
theorem decodeVec_encodeVec (x : Vec) : decodeVec (encodeVec x)=x := by
  have h0:=ZMod.val_lt (x 0);have h1:=ZMod.val_lt (x 1)
  have h2:=ZMod.val_lt (x 2);have h3:=ZMod.val_lt (x 3)
  funext i
  fin_cases i
'''
total='(x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val'
for i,d in enumerate([1,3,9,27]):
    text+=f'''  · change ((({total})/{d}%3 : Nat) : F)=x {i}
    rw [show ({total})/{d}%3=(x {i}).val by omega]
    exact ZMod.natCast_zmod_val _
'''
text+='''theorem encodeVec_decodeVec : ∀x,encodeVec (decodeVec x)=x := by decide +kernel
def controllerOf (u : Fin 15552) : Fin 192 := ⟨u.val/81,by have h:=u.isLt;omega⟩
def fiberOf (u : Fin 15552) : Fin 81 := ⟨u.val%81,Nat.mod_lt _ (by decide)⟩
def liftAt (a : Fin 192) (x : Fin 81) : Fin 15552 :=
  ⟨81*a.val+x.val,by have ha:=a.isLt;have hx:=x.isLt;omega⟩
theorem controllerOf_liftAt (a : Fin 192) (x : Fin 81) : controllerOf(liftAt a x)=a := by
  apply Fin.ext
  change (81*a.val+x.val)/81=a.val
  have hx:=x.isLt;omega
theorem fiberOf_liftAt (a : Fin 192) (x : Fin 81) : fiberOf(liftAt a x)=x := by
  apply Fin.ext
  change (81*a.val+x.val)%81=x.val
  have hx:=x.isLt;omega
theorem liftAt_parts (u : Fin 15552) : liftAt(controllerOf u)(fiberOf u)=u := by
  apply Fin.ext
  change 81*(u.val/81)+u.val%81=u.val
  omega
def stepVec (p : Fin 5) (t : F) (x : Vec) : Vec := act(matrix p)x+constant p+t • direction p
def forward (u : Fin 15552) (p : Fin 5) (t : F) : Fin 15552 :=
  liftAt (controller(controllerOf u)p) (encodeVec(stepVec p t (decodeVec(fiberOf u))))
def graph : SimpleGraph (Fin 15552) where
  Adj u v := u≠v ∧ ((∃p t,forward u p t=v) ∨ (∃p t,forward v p t=u))
  symm := by intro u v h;exact ⟨Ne.symm h.1,h.2.elim Or.inr Or.inl⟩
  loopless := by intro u h;exact h.1 rfl
instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u≠v ∧ ((∃p t,forward u p t=v) ∨ (∃p t,forward v p t=u)))
  infer_instance
theorem forward_adj_of_ne (u : Fin 15552) (p : Fin 5) (t : F) (h : u≠forward u p t) :
    graph.Adj u (forward u p t) := ⟨h,Or.inl ⟨p,t,rfl⟩⟩
theorem forward_liftAt (a : Fin 192) (x : Vec) (p : Fin 5) (t : F) :
    forward (liftAt a (encodeVec x)) p t=liftAt(controller a p)(encodeVec(stepVec p t x)) := by
  simp only [forward,controllerOf_liftAt,fiberOf_liftAt,decodeVec_encodeVec]
def source_label : Fin 15552 ≃ Fin 15552 := Equiv.refl _
def SourceFinalClaim : Prop := Fintype.card(Fin 15552)=15552 ∧
  (∀v,graph.degree v≤15) ∧ DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3
namespace Clone16389
abbrev Vertex := Fin 15552 ⊕ Fin 837
'''
text+='def layerData : Array Nat := '+arr(params['selected_controller_labels'])+'\n'
text+='''def layer (i : Fin 31) : Fin 192 := ⟨layerData.getD i.val 0 %192,Nat.mod_lt _ (by decide)⟩
def planeVec (a b c : Fin 3) : Vec := ![(a.val:F),0,(b.val:F),(c.val:F)]
def center (j : Fin 837) : Fin 15552 :=
  liftAt(layer ⟨j.val/27,by have h:=j.isLt;omega⟩)
    (encodeVec(planeVec ⟨j.val%3,Nat.mod_lt _ (by decide)⟩
      ⟨j.val/3%3,Nat.mod_lt _ (by decide)⟩ ⟨j.val/9%3,Nat.mod_lt _ (by decide)⟩))
abbrev graph := FullNeighborhoodClones.graph F3Graph15552.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F3Graph15552.graph center).Adj)
def label : Vertex ≃ Fin 16389 := finSumFinEquiv
theorem label_new (j : Fin 837) : (label(.inr j)).val=15552+j.val := rfl
theorem label_old (v : Fin 15552) : (label(.inl v)).val=v.val := rfl
def FinalClaim : Prop := Fintype.card Vertex=16389 ∧ (∀v,graph.degree v≤16) ∧
  DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3
#check (label : Vertex ≃ Fin 16389)
end Clone16389
#print axioms forward_adj_of_ne
end DegreeDiameter.Portfolio.F3Graph15552
'''
text=re.sub(r"(?<=[A-Za-z0-9_')])\(",' (',text)
text=re.sub(r'(?<=\))(?=[A-Za-z0-9_])',' ',text)
path.write_text(text)
(D/'DEFINITIONS_PREPARATION_RESULT.json').write_text(json.dumps(dict(status='NEW_ACTUAL_DEFINITIONS_WRITTEN',
    CPU_seconds=time.process_time()-started,source=str(path.relative_to(R)),controller_entries=960,
    matrix_code_entries=80,direction_entries=20,constant_entries=20,old_modules_modified=False),indent=2)+'\n')
print(path)
