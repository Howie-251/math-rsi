import DegreeDiameter.Portfolio.F9PlaneClone55Definitions
namespace DegreeDiameter.Portfolio.F9SixFiberDouble56
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
abbrev BaseIndex := Fin 486
abbrev CloneIndex := Fin 972
abbrev Vertex := Fin 56862 ⊕ CloneIndex
def chosenFiber : Fin 6 → Fin 78 := ![0,1,2,3,9,15]
def baseLabel : (Fin 6 × Fin 81) ≃ BaseIndex := finProdFinEquiv
def basePair : BaseIndex ≃ (Fin 6 × Fin 81) := baseLabel.symm
def cloneLabel : (Fin 2 × BaseIndex) ≃ CloneIndex := finProdFinEquiv
def clonePair : CloneIndex ≃ (Fin 2 × BaseIndex) := cloneLabel.symm
/-- This local product-center definition can also be used by a later separately authorized fiber set. -/
def planeCenter {I : Type*} (fibers : I → Fin 78) (i : I × Fin 81) : Fin 56862 :=
  liftAt (fibers i.1) (encodeVec (F9PlaneClone55.plane (F9PlaneClone55.parameters i.2 0)))
def baseCenter (i : BaseIndex) : Fin 56862 := planeCenter chosenFiber (basePair i)
/-- Both copies use the same immutable original56862-source center. -/
def center (k : CloneIndex) : Fin 56862 := baseCenter (clonePair k).2
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph F9Graph56862.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F9Graph56862.graph center).Adj)
def label : Vertex ≃ Fin 57834 := finSumFinEquiv
theorem base_label (u : Fin 6) (a b : Fin 9) :
    (baseLabel (u,F9PlaneClone55.cloneLabel (a,b))).val = b.val+9*a.val+81*u.val := rfl
theorem clone_label (copy : Fin 2) (base : BaseIndex) :
    (cloneLabel (copy,base)).val = base.val+486*copy.val := rfl
theorem label_old (v : Fin 56862) : (label (.inl v)).val = v.val := rfl
theorem label_new (k : CloneIndex) : (label (.inr k)).val = 56862+k.val := rfl
theorem label_new_copy (copy : Fin 2) (u : Fin 6) (a b : Fin 9) :
    (label (.inr (cloneLabel (copy,baseLabel (u,F9PlaneClone55.cloneLabel (a,b)))))).val =
      56862+486*copy.val+81*u.val+9*a.val+b.val := by
  change 56862+((b.val+9*a.val+81*u.val)+486*copy.val) = _
  omega
theorem base_center_source_label (u : Fin 6) (a b : Fin 9) :
    (baseCenter (baseLabel (u,F9PlaneClone55.cloneLabel (a,b)))).val =
      729*(chosenFiber u).val+a.val+9*b.val+81*F.code (F.c4*F.ofCode a.val) := by
  simp only [baseCenter,basePair,Equiv.symm_apply_apply,planeCenter,
    F9PlaneClone55.parameters,F9PlaneClone55.clonePair,F9PlaneClone55.plane,
    Equiv.symm_apply_apply]
  change 729*(chosenFiber u).val +
    (F.code (F.ofCode a.val)+9*F.code (F.ofCode b.val)+81*F.code (F.c4*F.ofCode a.val)) = _
  simp only [F.code_ofCode]
  omega
theorem card_vertex : Fintype.card Vertex = 57834 := by
  simp only [Fintype.card_sum,Fintype.card_fin]
def FinalClaim : Prop := Fintype.card Vertex = 57834 ∧ (∀ v, graph.degree v ≤ 56) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.F9SixFiberDouble56
