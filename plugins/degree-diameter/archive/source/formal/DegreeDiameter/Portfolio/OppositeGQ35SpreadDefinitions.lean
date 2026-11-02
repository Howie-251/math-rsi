import DegreeDiameter.Portfolio.OppositeGQ35SpreadGeneric
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev Point := Fin 64
abbrev Line := Fin 96
abbrev Old := Fin 6144
abbrev New := Fin 16
abbrev Vertex := Old ⊕ New
/-- Literal rows in PARAMETERS order; point code is a+4*b+16*c over GF4. -/
def linePointData : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 0, 4, 8, 12, 0, 16, 32, 48, 0, 20, 40, 60, 0, 24, 44, 52, 0, 28, 36, 56, 1, 5, 9, 13, 1, 17, 33, 49, 1, 21, 41, 61, 1, 25, 45, 53, 1, 29, 37, 57, 2, 6, 10, 14, 2, 18, 34, 50, 2, 22, 42, 62, 2, 26, 46, 54, 2, 30, 38, 58, 3, 7, 11, 15, 3, 19, 35, 51, 3, 23, 43, 63, 3, 27, 47, 55, 3, 31, 39, 59, 4, 17, 46, 59, 4, 21, 38, 55, 4, 25, 34, 63, 4, 29, 42, 51, 5, 16, 47, 58, 5, 20, 39, 54, 5, 24, 35, 62, 5, 28, 43, 50, 6, 19, 44, 57, 6, 23, 36, 53, 6, 27, 32, 61, 6, 31, 40, 49, 7, 18, 45, 56, 7, 22, 37, 52, 7, 26, 33, 60, 7, 30, 41, 48, 8, 18, 39, 61, 8, 22, 47, 49, 8, 26, 43, 57, 8, 30, 35, 53, 9, 19, 38, 60, 9, 23, 46, 48, 9, 27, 42, 56, 9, 31, 34, 52, 10, 16, 37, 63, 10, 20, 45, 51, 10, 24, 41, 59, 10, 28, 33, 55, 11, 17, 36, 62, 11, 21, 44, 50, 11, 25, 40, 58, 11, 29, 32, 54, 12, 19, 41, 54, 12, 23, 33, 58, 12, 27, 37, 50, 12, 31, 45, 62, 13, 18, 40, 55, 13, 22, 32, 59, 13, 26, 36, 51, 13, 30, 44, 63, 14, 17, 43, 52, 14, 21, 35, 56, 14, 25, 39, 48, 14, 29, 47, 60, 15, 16, 42, 53, 15, 20, 34, 57, 15, 24, 38, 49, 15, 28, 46, 61, 16, 21, 26, 31, 17, 20, 27, 30, 18, 23, 24, 29, 19, 22, 25, 28, 32, 38, 43, 45, 33, 39, 42, 44, 34, 36, 41, 47, 35, 37, 40, 46, 48, 55, 57, 62, 49, 54, 56, 63, 50, 53, 59, 60, 51, 52, 58, 61]
def pointLineData : Array Nat := #[0, 16, 17, 18, 19, 20, 0, 21, 22, 23, 24, 25, 0, 26, 27, 28, 29, 30, 0, 31, 32, 33, 34, 35, 1, 16, 36, 37, 38, 39, 1, 21, 40, 41, 42, 43, 1, 26, 44, 45, 46, 47, 1, 31, 48, 49, 50, 51, 2, 16, 52, 53, 54, 55, 2, 21, 56, 57, 58, 59, 2, 26, 60, 61, 62, 63, 2, 31, 64, 65, 66, 67, 3, 16, 68, 69, 70, 71, 3, 21, 72, 73, 74, 75, 3, 26, 76, 77, 78, 79, 3, 31, 80, 81, 82, 83, 4, 17, 40, 60, 80, 84, 4, 22, 36, 64, 76, 85, 4, 27, 48, 52, 72, 86, 4, 32, 44, 56, 68, 87, 5, 18, 41, 61, 81, 85, 5, 23, 37, 65, 77, 84, 5, 28, 49, 53, 73, 87, 5, 33, 45, 57, 69, 86, 6, 19, 42, 62, 82, 86, 6, 24, 38, 66, 78, 87, 6, 29, 50, 54, 74, 84, 6, 34, 46, 58, 70, 85, 7, 20, 43, 63, 83, 87, 7, 25, 39, 67, 79, 86, 7, 30, 51, 55, 75, 85, 7, 35, 47, 59, 71, 84, 8, 17, 46, 67, 73, 88, 8, 22, 50, 63, 69, 89, 8, 27, 38, 59, 81, 90, 8, 32, 42, 55, 77, 91, 9, 20, 45, 64, 74, 90, 9, 25, 49, 60, 70, 91, 9, 30, 37, 56, 82, 88, 9, 35, 41, 52, 78, 89, 10, 18, 47, 66, 72, 91, 10, 23, 51, 62, 68, 90, 10, 28, 39, 58, 80, 89, 10, 33, 43, 54, 76, 88, 11, 19, 44, 65, 75, 89, 11, 24, 48, 61, 71, 88, 11, 29, 36, 57, 83, 91, 11, 34, 40, 53, 79, 90, 12, 17, 51, 57, 78, 92, 12, 22, 47, 53, 82, 93, 12, 27, 43, 65, 70, 94, 12, 32, 39, 61, 74, 95, 13, 19, 49, 59, 76, 95, 13, 24, 45, 55, 80, 94, 13, 29, 41, 67, 68, 93, 13, 34, 37, 63, 72, 92, 14, 20, 48, 58, 77, 93, 14, 25, 44, 54, 81, 92, 14, 30, 40, 66, 69, 95, 14, 35, 36, 62, 73, 94, 15, 18, 50, 56, 79, 94, 15, 23, 46, 52, 83, 95, 15, 28, 42, 64, 71, 92, 15, 33, 38, 60, 75, 93]
def linePoint (l : Line) (i : Fin 4) : Point :=
  ⟨linePointData.getD (4*l.val+i.val) 0 % 64, Nat.mod_lt _ (by decide)⟩
def pointLine (p : Point) (i : Fin 6) : Line :=
  ⟨pointLineData.getD (6*p.val+i.val) 0 % 96, Nat.mod_lt _ (by decide)⟩
/-- Incidence is literal membership in the four entries of the chosen line. -/
def Inc (p : Point) (l : Line) : Prop := ∃ i : Fin 4, linePoint l i = p
instance : DecidableRel Inc := fun p l => inferInstanceAs (Decidable (∃ i : Fin 4, linePoint l i = p))
def spread (j : New) : Line := ⟨j.val,by omega⟩
def spreadOwner (p : Point) : New := ⟨p.val / 4,by omega⟩
def oldEquiv : Old ≃ Point × Line := (finProdFinEquiv (m := 64) (n := 96)).symm
def old (p : Point) (l : Line) : Old := oldEquiv.symm (p,l)
def graph : SimpleGraph Vertex := OppositeGQSpread.graph oldEquiv Inc spread
instance : DecidableRel graph.Adj := inferInstanceAs (DecidableRel (OppositeGQSpread.graph oldEquiv Inc spread).Adj)
def label : Vertex ≃ Fin 6160 := finSumFinEquiv

theorem old_label (p : Point) (l : Line) : (old p l).val = l.val+96*p.val := rfl
theorem label_old (v : Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : New) : (label (.inr j)).val = 6144+j.val := rfl
theorem card_vertex : Fintype.card Vertex = 6160 := by simp only [Fintype.card_sum,Fintype.card_fin]

/-- The final target: no incidence, projection or capacity premise is exported. -/
def FinalClaim : Prop := Fintype.card Vertex = 6160 ∧ (∀ v, graph.degree v ≤ 24) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print graph
#print Inc
#print oldEquiv
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.OppositeGQ35Spread
