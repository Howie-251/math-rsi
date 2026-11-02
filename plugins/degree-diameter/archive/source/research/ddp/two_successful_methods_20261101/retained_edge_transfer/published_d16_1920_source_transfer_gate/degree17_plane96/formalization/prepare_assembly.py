from pathlib import Path
import json,time
start=time.process_time();D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());O=R/'formal/DegreeDiameter/Portfolio'
def write(name,text):
    p=R/'formal'/f'{name}.lean'if name.endswith('Audit')else O/f'{name}.lean'
    assert not p.exists(),name;p.write_text(text)
imports='\n'.join('import DegreeDiameter.Portfolio.F4Graph1920Row'+str(i)+'Walks'for i in range(30))
term='(fun a : Fin 0 => Fin.elim0 a)'
for i in reversed(range(30)):term=f'(Fin.cases Row{i}.row{i}_full_walk_bound {term})'
s=imports+'''
namespace DegreeDiameter.Portfolio.F4Graph1920
def CompleteRow (a : Fin 30) : Prop := ∀(x : Fin 64)(v : Fin 1920),
  ∃w:graph.Walk (liftAt a x) v,w.length≤3
theorem all_controller_rows : ∀a,CompleteRow a :=
  '''+term+'''
theorem diameterAtMost_three : DiameterAtMost graph 3 := by
  intro u v
  have h := all_controller_rows (controllerOf u) (fiberOf u) v
  simpa only [liftAt_parts] using h
#print axioms diameterAtMost_three
end DegreeDiameter.Portfolio.F4Graph1920
'''
write('F4Graph1920SourceDiameter',s)
lower='''import DegreeDiameter.Portfolio.F4Graph1920Routes
namespace DegreeDiameter.Portfolio.F4Graph1920
open F4Graph3840
theorem zero_ne_192 : (0 : Fin 1920)≠192 := by decide
theorem no_controller_one : ∀p:Fin 4,controller 0 p≠(3:Fin 30) := by decide +kernel
theorem no_controller_two : ∀p q:Fin 4,controller (controller 0 p) q≠(3:Fin 30) := by decide +kernel
theorem no_one_step_zero_192 : ∀(p:Fin 4)(t:F),forward 0 p t≠192 := by
  intro p t h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller 0 p=(3:Fin 30) at hc
  exact no_controller_one p hc
theorem no_two_steps_zero_192 : ∀(p q:Fin 4)(t s:F),forward (forward 0 p t) q s≠192 := by
  intro p q t s h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller (controller 0 p) q=(3:Fin 30) at hc
  exact no_controller_two p q hc
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 := by
  intro h
  obtain ⟨w,hw⟩ := h 0 192
  obtain ⟨z,hfirst,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne zero_ne_192 w
  rw [heq] at hw
  change tail.length+1≤2 at hw
  obtain ⟨p,t,h1⟩ := (adj_iff_forward 0 z).mp hfirst
  by_cases hzero : tail.length=0
  · have hz : z=192 := SimpleGraph.Walk.eq_of_length_eq_zero hzero
    exact no_one_step_zero_192 p t (h1.trans hz)
  · have hone : tail.length=1 := by omega
    have hadj : graph.Adj z 192 := SimpleGraph.Walk.adj_of_length_eq_one hone
    obtain ⟨q,s,h2⟩ := (adj_iff_forward z 192).mp hadj
    apply no_two_steps_zero_192 p q t s
    rw [h1]
    exact h2
#print axioms not_diameterAtMost_two
end DegreeDiameter.Portfolio.F4Graph1920
'''
write('F4Graph1920SourceLower',lower)
exact='''import DegreeDiameter.Portfolio.F4Graph1920SourceDiameter
import DegreeDiameter.Portfolio.F4Graph1920SourceLower
namespace DegreeDiameter.Portfolio.F4Graph1920
def source_label : Fin 1920 ≃ Fin 1920 := Equiv.refl _
abbrev FinalClaim := SourceFinalClaim
theorem d16_1920 : Fintype.card (Fin 1920)=1920 ∧ (∀v,graph.degree v≤16) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨Fintype.card_fin _,degree_le_sixteen,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d16_1920
#print axioms final_claim
end DegreeDiameter.Portfolio.F4Graph1920
'''
write('F4Graph1920SourceExact',exact)
audit='''import DegreeDiameter.Portfolio.F4Graph1920SourceExact
open DegreeDiameter.Portfolio.F4Graph1920
#check (graph : SimpleGraph (Fin 1920))
#check (source_label : Fin 1920 ≃ Fin 1920)
#print SourceFinalClaim
#print d16_1920
#print axioms d16_1920
#print final_claim
#print axioms final_claim
#print axioms diameterAtMost_three
#print axioms not_diameterAtMost_two
'''
write('F4Graph1920SourceAudit',audit)
clone='''import DegreeDiameter.Portfolio.F4Graph1920CloneInputs
import DegreeDiameter.Portfolio.F4Graph1920SourceExact
namespace DegreeDiameter.Portfolio.F4Graph1920.Clone2016
theorem card_vertex : Fintype.card Vertex=2016 := by
  simpa only [Fintype.card_fin] using Fintype.card_congr label
theorem degree_le : ∀v,graph.degree v≤17 :=
  FullNeighborhoodClones.degree_le F4Graph1920.graph center 16 1 F4Graph1920.final_claim.2.1 load_le_one
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost F4Graph1920.graph center 3 (by decide)
    F4Graph1920.final_claim.2.2.1
    (fun v => ⟨F4Graph1920.forward v 0 0,F4Graph1920.forward_adj v 0 0⟩)
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost F4Graph1920.graph center 2 F4Graph1920.final_claim.2.2.2
theorem d17_2016 : Fintype.card Vertex=2016 ∧ (∀v,graph.degree v≤17) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d17_2016
theorem old_walk_bound_iff (u v : Fin 1920)(n:Nat) :
    (∃w:graph.Walk (.inl u) (.inl v),w.length≤n) ↔ ∃w:F4Graph1920.graph.Walk u v,w.length≤n :=
  FullNeighborhoodClones.old_walk_bound_iff F4Graph1920.graph center u v n
#print axioms final_claim
end DegreeDiameter.Portfolio.F4Graph1920.Clone2016
'''
write('F4Graph1920CloneExact',clone)
cloneaudit='''import DegreeDiameter.Portfolio.F4Graph1920CloneExact
open DegreeDiameter.Portfolio.F4Graph1920.Clone2016
#check (graph : SimpleGraph Vertex)
#check (label : Vertex ≃ Fin 2016)
#print FinalClaim
#check d17_2016
#print d17_2016
#print axioms d17_2016
#print final_claim
#print axioms final_claim
#print axioms load_le_one
#print axioms old_walk_bound_iff
#print axioms label_new
'''
write('F4Graph1920CloneAudit',cloneaudit)
record=dict(status='NEW_SOURCE_AND_CLONE_ASSEMBLY_SOURCE_WRITTEN_NOT_COMPILED',CPU_seconds=time.process_time()-start,
    sequential_modules=['F4Graph1920SourceDiameter','F4Graph1920SourceLower','F4Graph1920SourceExact','F4Graph1920SourceAudit',
        'F4Graph1920CloneInputs','F4Graph1920CloneExact','F4Graph1920CloneAudit'],old_or_passed_modules_modified=False)
(D/'ASSEMBLY_PREPARATION_RESULT.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
