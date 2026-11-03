import json,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;Q=R/'formal/DegreeDiameter/Portfolio';N='F9U10PlaneCloneFamily';t=time.process_time()
p=json.loads((P/'PARAMETERS.json').read_text());U=p['selected_controllers'];assert U==[31,32,44,45,59,60,61,72,73,74]
owner=['none']*78
for i,row in enumerate(p['controller_target_rows']):
 for port,v in enumerate(row):assert owner[v]=='none';owner[v]=f'some ({i},{port})'
def vec(x):return '!['+', '.join(map(str,x))+']'
defs=f'''import DegreeDiameter.Portfolio.F9SixFiberDouble56Definitions
namespace DegreeDiameter.Portfolio.{N}
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
abbrev BaseIndex := Fin 810
abbrev Vertex (k : Nat) := Fin 56862 ⊕ (Fin k × BaseIndex)
def chosenFiber : Fin 10 → Fin 78 := {vec(U)}
def baseLabel : (Fin 10 × Fin 81) ≃ BaseIndex := finProdFinEquiv
def basePair : BaseIndex ≃ (Fin 10 × Fin 81) := baseLabel.symm
def baseCenter (i : BaseIndex) : Fin 56862 :=
  F9SixFiberDouble56.planeCenter chosenFiber (basePair i)
/-- Copy count changes only the index type; every owner remains in the fixed original source. -/
def center (k : Nat) (j : Fin k × BaseIndex) : Fin 56862 := baseCenter j.2
def graph (k : Nat) : SimpleGraph (Vertex k) := FullNeighborhoodClones.graph F9Graph56862.graph (center k)
instance (k : Nat) : DecidableRel (graph k).Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F9Graph56862.graph (center k)).Adj)
def cloneLabel (k : Nat) : (Fin k × BaseIndex) ≃ Fin (810*k) :=
  (finProdFinEquiv (m:=k) (n:=810)).trans (finCongr (Nat.mul_comm k 810))
def label (k : Nat) : Vertex k ≃ Fin (56862+810*k) :=
  (Equiv.sumCongr (Equiv.refl (Fin 56862)) (cloneLabel k)).trans finSumFinEquiv
theorem base_label (u : Fin 10) (a b : Fin 9) :
    (baseLabel (u,F9PlaneClone55.cloneLabel (a,b))).val = b.val+9*a.val+81*u.val := rfl
theorem clone_label (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (cloneLabel k (copy,base)).val = base.val+810*copy.val := rfl
theorem label_old (k : Nat) (v : Fin 56862) : (label k (.inl v)).val = v.val := rfl
theorem label_new (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (label k (.inr (copy,base))).val = 56862+810*copy.val+base.val := by
  change 56862+(base.val+810*copy.val) = _
  omega
theorem label_new_coordinates (k : Nat) (copy : Fin k) (u : Fin 10) (a b : Fin 9) :
    (label k (.inr (copy,baseLabel (u,F9PlaneClone55.cloneLabel (a,b))))).val =
      56862+810*copy.val+81*u.val+9*a.val+b.val := by
  change 56862+((b.val+9*a.val+81*u.val)+810*copy.val) = _
  omega
theorem base_center_source_label (u : Fin 10) (a b : Fin 9) :
    (baseCenter (baseLabel (u,F9PlaneClone55.cloneLabel (a,b)))).val =
      729*(chosenFiber u).val+a.val+9*b.val+81*F.code (F.c4*F.ofCode a.val) := by
  simp only [baseCenter,basePair,Equiv.symm_apply_apply,F9SixFiberDouble56.planeCenter,
    F9PlaneClone55.parameters,F9PlaneClone55.clonePair,F9PlaneClone55.plane,Equiv.symm_apply_apply]
  change 729*(chosenFiber u).val+
    (F.code (F.ofCode a.val)+9*F.code (F.ofCode b.val)+81*F.code (F.c4*F.ofCode a.val)) = _
  simp only [F.code_ofCode]
  omega
theorem card_vertex (k : Nat) : Fintype.card (Vertex k) = 56862+810*k := by
  simp only [Vertex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin]
  omega
def FinalClaim (k : Nat) : Prop := Fintype.card (Vertex k) = 56862+810*k ∧
  (∀ v, (graph k).degree v ≤ 54+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2
#print baseCenter
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.{N}
'''
(Q/(N+'Definitions.lean')).write_text(defs)
inputs=f'''import DegreeDiameter.Portfolio.{N}Definitions
import DegreeDiameter.Portfolio.F9SixFiberDouble56Inputs
namespace DegreeDiameter.Portfolio.{N}
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
/-- A60-entry partial inverse certificate, avoiding a repeated60×60 target comparison. -/
def targetOwner : Fin 78 → Option (Fin 10 × Fin 6) := {vec(owner)}
theorem target_owner : ∀ (u : Fin 10) (p : Fin 6),
    targetOwner (controller (chosenFiber u) p) = some (u,p) := by decide +kernel
theorem controller_targets_injective : Function.Injective
    (fun ip : Fin 10 × Fin 6 => controller (chosenFiber ip.1) ip.2) := by
  rintro ⟨u,p⟩ ⟨v,q⟩ h
  have ho := congrArg targetOwner h
  simp only [target_owner] at ho
  exact Option.some.inj ho
theorem common_base_pin_index_unique (w : Fin 56862) (i j : BaseIndex)
    (hi : F9Graph56862.graph.Adj w (baseCenter i))
    (hj : F9Graph56862.graph.Adj w (baseCenter j)) : i = j := by
  apply basePair.injective
  exact F9SixFiberDouble56.common_plane_pin_index_unique chosenFiber controller_targets_injective
    w (basePair i) (basePair j) hi hj
theorem base_load_le_one (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph baseCenter w ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_base_pin_index_unique w x.val y.val x.property y.property
theorem copy_load_le (k : Nat) (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph (center k) w ≤ k := by
  have hbase : ∀ x y : {{b : BaseIndex // F9Graph56862.graph.Adj w (baseCenter b)}}, x = y :=
    Fintype.card_le_one_iff.mp (base_load_le_one w)
  let copyIndex : {{j : Fin k × BaseIndex // F9Graph56862.graph.Adj w (center k j)}} → Fin k := fun j => j.val.1
  have hinj : Function.Injective copyIndex := by
    intro x y hcopy
    have hbaseval : x.val.2 = y.val.2 :=
      congrArg Subtype.val (hbase ⟨x.val.2,x.property⟩ ⟨y.val.2,y.property⟩)
    apply Subtype.ext
    exact Prod.ext hcopy hbaseval
  have h := Fintype.card_le_of_injective copyIndex hinj
  simpa only [Fintype.card_fin] using h
#print axioms target_owner
#print axioms base_load_le_one
#print axioms copy_load_le
end DegreeDiameter.Portfolio.{N}
'''
(Q/(N+'Inputs.lean')).write_text(inputs)
exact=f'''import DegreeDiameter.Portfolio.{N}Inputs
import DegreeDiameter.Portfolio.F9Graph56862Exact
namespace DegreeDiameter.Portfolio.{N}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem source_no_isolated (v : Fin 56862) : ∃ w, F9Graph56862.graph.Adj v w :=
  ⟨F9Graph56862.forward v 0 F9Graph56862.F.c0,F9Graph56862.forward_adj v 0 F9Graph56862.F.c0⟩
theorem old_walk_bound_iff (k : Nat) (u v : Fin 56862) (n : Nat) :
    (∃ p : (graph k).Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : F9Graph56862.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff F9Graph56862.graph (center k) u v n
theorem degree_le (k : Nat) : ∀ v, (graph k).degree v ≤ 54+k :=
  FullNeighborhoodClones.degree_le F9Graph56862.graph (center k) 54 k
    F9Graph56862.degree_le_fifty_four (copy_load_le k)
theorem diameterAtMost_three (k : Nat) : DiameterAtMost (graph k) 3 :=
  FullNeighborhoodClones.diameterAtMost F9Graph56862.graph (center k) 3 (by decide)
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated
theorem not_diameterAtMost_two (k : Nat) : ¬DiameterAtMost (graph k) 2 :=
  FullNeighborhoodClones.not_diameterAtMost F9Graph56862.graph (center k) 2
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.2
/-- An unconditional fixed-source family theorem; only the five explicit qualified cases below are concrete endpoints. -/
theorem fixed_family_target (k : Nat) : Fintype.card (Vertex k) = 56862+810*k ∧
    (∀ v, (graph k).degree v ≤ 54+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2 :=
  ⟨card_vertex k,degree_le k,diameterAtMost_three k,not_diameterAtMost_two k⟩
theorem fixed_family_claim (k : Nat) : FinalClaim k := fixed_family_target k
'''
for k in range(1,6):
 n=56862+810*k;degree=54+k
 claim=f'Fintype.card (Vertex {k}) = {n} ∧ (∀ v, (graph {k}).degree v ≤ {degree}) ∧\n  DiameterAtMost (graph {k}) 3 ∧ ¬DiameterAtMost (graph {k}) 2'
 exact+=f'''theorem concrete_{degree}_{n} : {claim} := fixed_family_target {k}
def FinalClaim{degree} : Prop := {claim}
theorem final_claim{degree} : FinalClaim{degree} := concrete_{degree}_{n}
#print axioms concrete_{degree}_{n}
#print axioms final_claim{degree}
'''
exact+=f'#print axioms fixed_family_target\nend DegreeDiameter.Portfolio.{N}\n'
(Q/(N+'Exact.lean')).write_text(exact)
audit=f'''import DegreeDiameter.Portfolio.{N}Exact
open DegreeDiameter.Portfolio
set_option pp.explicit true in
#print DiameterAtMost
#print {N}.baseCenter
#print {N}.center
#print {N}.graph
#print FullNeighborhoodClones.graph
#print {N}.label
#check {N}.base_label
#check {N}.clone_label
#check {N}.label_old
#check {N}.label_new
#check {N}.label_new_coordinates
#check {N}.base_center_source_label
#check {N}.base_load_le_one
#check {N}.copy_load_le
#check {N}.old_walk_bound_iff
#print axioms {N}.base_load_le_one
#print axioms {N}.copy_load_le
'''
for k in range(1,6):
 n=56862+810*k;degree=54+k
 audit+=f'''#check ({N}.label {k} : {N}.Vertex {k} ≃ Fin {n})
#check {N}.concrete_{degree}_{n}
#print {N}.concrete_{degree}_{n}
#print {N}.FinalClaim{degree}
#print axioms {N}.concrete_{degree}_{n}
#print axioms {N}.final_claim{degree}
'''
(R/'formal'/(N+'Audit.lean')).write_text(audit)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(dict(CPU_seconds=time.process_time()-t,new_namespace=N,module_count=4,target_owner_checks=60,explicit_cases=list(range(1,6)),k6_case_created=False,old_modules_changed=False),indent=2)+'\n')
print('Generated fixedU10generic family and five explicit original targets; new4modules only.')
