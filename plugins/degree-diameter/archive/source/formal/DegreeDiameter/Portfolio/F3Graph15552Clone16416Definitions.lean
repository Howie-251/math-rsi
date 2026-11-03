import DegreeDiameter.Portfolio.F3Graph15552Definitions
namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
abbrev Vertex := Fin 15552 ⊕ Fin 864
def layerData : Array Nat := #[0, 1, 2, 3, 5, 6, 8, 12, 14, 18, 20, 25, 31, 34, 38, 43, 55, 67, 73, 85, 86, 87, 94, 96, 113, 141, 148, 162, 172, 187, 188, 190]
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
