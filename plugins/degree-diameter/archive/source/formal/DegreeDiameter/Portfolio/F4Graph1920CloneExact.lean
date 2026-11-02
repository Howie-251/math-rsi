import DegreeDiameter.Portfolio.F4Graph1920CloneInputs
import DegreeDiameter.Portfolio.F4Graph1920SourceExact
namespace DegreeDiameter.Portfolio.F4Graph1920.Clone2016
def orderedCenterLabelData : Array Nat := #[0, 20, 40, 60, 17, 5, 57, 45, 34, 54, 10, 30, 51, 39, 27, 15, 192, 212, 232, 252, 209, 197, 249, 237, 226, 246, 202, 222, 243, 231, 219, 207, 320, 340, 360, 380, 337, 325, 377, 365, 354, 374, 330, 350, 371, 359, 347, 335, 448, 468, 488, 508, 465, 453, 505, 493, 482, 502, 458, 478, 499, 487, 475, 463, 576, 596, 616, 636, 593, 581, 633, 621, 610, 630, 586, 606, 627, 615, 603, 591, 1024, 1044, 1064, 1084, 1041, 1029, 1081, 1069, 1058, 1078, 1034, 1054, 1075, 1063, 1051, 1039]
theorem center_ordered_label : ∀j:Fin 96, (center j).val =
    orderedCenterLabelData.getD j.val 0 := by decide +kernel
theorem label_old (v : Fin 1920) : (label (.inl v)).val=v.val := rfl
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
