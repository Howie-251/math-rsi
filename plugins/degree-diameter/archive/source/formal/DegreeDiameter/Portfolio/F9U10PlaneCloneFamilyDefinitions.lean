import DegreeDiameter.Portfolio.F9SixFiberDouble56Definitions
namespace DegreeDiameter.Portfolio.F9U10PlaneCloneFamily
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
abbrev BaseIndex := Fin 810
abbrev Vertex (k : Nat) := Fin 56862 ⊕ (Fin k × BaseIndex)
def chosenFiber : Fin 10 → Fin 78 := ![31, 32, 44, 45, 59, 60, 61, 72, 73, 74]
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
end DegreeDiameter.Portfolio.F9U10PlaneCloneFamily
