import DegreeDiameter.Portfolio.F9Graph56862Linear
import DegreeDiameter.Portfolio.FullNeighborhoodClones
import Mathlib.Logic.Equiv.Fin.Basic

namespace DegreeDiameter.Portfolio.F9PlaneClone55
open F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

abbrev CloneIndex := Fin 81
abbrev Vertex := Fin 56862 ⊕ CloneIndex
def cloneLabel : (Fin 9 × Fin 9) ≃ CloneIndex := finProdFinEquiv
def clonePair : CloneIndex ≃ (Fin 9 × Fin 9) := cloneLabel.symm
def parameters (i : CloneIndex) (t : F) : Vec :=
  ![F.ofCode (clonePair i).1.val, F.ofCode (clonePair i).2.val, t]
def plane (x : Vec) : Vec := ![x 0, x 1, F.c4 * x 0]
def center (i : CloneIndex) : Fin 56862 :=
  liftAt 0 (encodeVec (plane (parameters i 0)))
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph F9Graph56862.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F9Graph56862.graph center).Adj)
def label : Vertex ≃ Fin 56943 := finSumFinEquiv

theorem clone_label (a b : Fin 9) : (cloneLabel (a,b)).val = b.val+9*a.val := rfl
theorem label_old (v : Fin 56862) : (label (.inl v)).val = v.val := rfl
theorem label_new (i : CloneIndex) : (label (.inr i)).val = 56862+i.val := rfl
theorem card_vertex : Fintype.card Vertex = 56943 := by
  simp only [Fintype.card_sum,Fintype.card_fin]

theorem center_source_label (i : CloneIndex) :
    (center i).val = (clonePair i).1.val + 9*(clonePair i).2.val +
      81*F.code (F.c4 * F.ofCode (clonePair i).1.val) := by
  change 729*0+(F.code (F.ofCode (clonePair i).1.val)+
    9*F.code (F.ofCode (clonePair i).2.val)+
    81*F.code (F.c4*F.ofCode (clonePair i).1.val)) = _
  simp only [Nat.mul_zero,Nat.zero_add,F.code_ofCode]

def pinMap (p : Fin 6) (x : Vec) : Vec := stepVec 0 p (x 2) (plane x)

def FinalClaim : Prop := Fintype.card Vertex = 56943 ∧ (∀ v, graph.degree v ≤ 55) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2

#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.F9PlaneClone55
