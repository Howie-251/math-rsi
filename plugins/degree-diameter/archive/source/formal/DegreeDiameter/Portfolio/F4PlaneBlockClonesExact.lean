import DegreeDiameter.Portfolio.F4PlaneBlockClonesLoad
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
instance : DecidableRel graph21.Adj :=
  inferInstanceAs (DecidableRel (FullNeighborhoodClones.graph F4Graph3840.graph (center layers21)).Adj)
instance : DecidableRel graph22.Adj :=
  inferInstanceAs (DecidableRel (FullNeighborhoodClones.graph F4Graph3840.graph (center layers22)).Adj)

theorem degree21 : ∀ v, graph21.degree v ≤ 21 :=
  FullNeighborhoodClones.degree_le F4Graph3840.graph (center layers21) 20 1 degree_le_twenty
    (load_le_capacity layers21 1 capacity21)

theorem degree22 : ∀ v, graph22.degree v ≤ 22 :=
  FullNeighborhoodClones.degree_le F4Graph3840.graph (center layers22) 20 2 degree_le_twenty
    (load_le_capacity layers22 2 capacity22)

theorem diameter21 : DiameterAtMost graph21 3 :=
  FullNeighborhoodClones.diameterAtMost F4Graph3840.graph (center layers21) 3 (by decide)
    diameterAtMost_three source_no_isolated

theorem diameter22 : DiameterAtMost graph22 3 :=
  FullNeighborhoodClones.diameterAtMost F4Graph3840.graph (center layers22) 3 (by decide)
    diameterAtMost_three source_no_isolated

theorem not_diameter21_two : ¬ DiameterAtMost graph21 2 :=
  FullNeighborhoodClones.not_diameterAtMost F4Graph3840.graph (center layers21) 2 not_diameterAtMost_two

theorem not_diameter22_two : ¬ DiameterAtMost graph22 2 :=
  FullNeighborhoodClones.not_diameterAtMost F4Graph3840.graph (center layers22) 2 not_diameterAtMost_two

theorem label21_old (v : Fin 3840) : (label21 (.inl v)).val = v.val := rfl
theorem label21_new (j : Fin (9*16)) : (label21 (.inr j)).val = 3840+j.val := rfl
theorem label22_old (v : Fin 3840) : (label22 (.inl v)).val = v.val := rfl
theorem label22_new (j : Fin (22*16)) : (label22 (.inr j)).val = 3840+j.val := rfl

/-- The concrete144clone recipe, on the explicitly labeled Sum carrier. -/
theorem concrete_d21_n3984 :
    Fintype.card V21 = 3984 ∧ (∀ v, graph21.degree v ≤ 21) ∧
      DiameterAtMost graph21 3 ∧ ¬DiameterAtMost graph21 2 :=
  ⟨card21,degree21,diameter21,not_diameter21_two⟩

/-- The concrete352clone recipe, on the explicitly labeled Sum carrier. -/
theorem concrete_d22_n4192 :
    Fintype.card V22 = 4192 ∧ (∀ v, graph22.degree v ≤ 22) ∧
      DiameterAtMost graph22 3 ∧ ¬DiameterAtMost graph22 2 :=
  ⟨card22,degree22,diameter22,not_diameter22_two⟩

#print axioms concrete_d21_n3984
#print axioms concrete_d22_n4192
end DegreeDiameter.Portfolio.F4PlaneBlockClones
