import ES7CoverageData
namespace ES7CapacityStage
open ES8ActualRanks ES8BalancedGeometry ES7Geometry ES7Subset ES7Residual

/-- The completed restricted numerical input; no remaining mathematical hypothesis. -/
theorem restricted25 : RestrictedBound 25 := ES7CoverageData.restricted25_bound

/-- The geometric five-deletion theorem now gives an unconditional residual capacity. -/
theorem residual30 : ResidualBound 30 := residual_of_restricted restricted25

/-- The sole remaining numerical exclusion required for ES7<=81. -/
def Balanced50Exclusion : Prop := ∀ c : Configuration 50,
  (¬(colorConfig c.cup true).HasNCap 6 (Finset.range 50)) →
  (¬(colorConfig c.cup true).HasNCup 6 (Finset.range 50)) →
  (¬HasConvexHeptagon (Set.range c.point)) → False

/-- Transport the exact 50-point exclusion to the arbitrary-size restricted
capacity. Subset ranks are recomputed by the induced configuration. -/
theorem balanced_bound_of_50_exclusion (exclude : Balanced50Exclusion) : BalancedBound 49 := by
  intro n c noCap noCup noHept
  by_contra high
  have enough : 50≤(Finset.univ : Finset (Fin n)).card := by simp; omega
  obtain ⟨S,_,card⟩ := Finset.exists_subset_card_eq enough
  have noCapS : ¬(colorConfig (ES8Subset.restrict c S).cup true).HasNCap 6 (Finset.range S.card) := by
    intro h
    obtain ⟨xs,hcap,inside⟩ := ES8Subset.hasCap_map c S 6 h
    exact noCap ⟨xs,hcap,fun u hu=>ES8SlopePartition.natSet_bounded S (inside u hu)⟩
  have noCupS : ¬(colorConfig (ES8Subset.restrict c S).cup true).HasNCup 6 (Finset.range S.card) := by
    intro h
    obtain ⟨xs,hcup,inside⟩ := ES8Subset.hasCup_map c S 6 h
    exact noCup ⟨xs,hcup,fun u hu=>ES8SlopePartition.natSet_bounded S (inside u hu)⟩
  have noHeptS : ¬HasConvexHeptagon (Set.range (ES8Subset.restrict c S).point) :=
    fun h=>noHept (heptagon_mono _ _ (ES8Subset.restrict_range c S) h)
  have all50 : ∀ k, k=50 → ∀ d : Configuration k,
      (¬(colorConfig d.cup true).HasNCap 6 (Finset.range k)) →
      (¬(colorConfig d.cup true).HasNCup 6 (Finset.range k)) →
      (¬HasConvexHeptagon (Set.range d.point)) → False := by
    intro k eq
    subst k
    exact exclude
  exact all50 S.card card (ES8Subset.restrict c S) noCapS noCupS noHeptS


/-- Exactly one unresolved finite geometric exclusion remains explicit. -/
theorem es7_le_81_of_balanced50 (exclude : Balanced50Exclusion)
    (S : Finset ES8Geometry.Point) (gp : ES7Final.GeneralPosition S) (size : 81≤S.card) :
    HasConvexHeptagon (↑S : Set ES8Geometry.Point) :=
  ES7Final.es7_le_81_of_capacities (balanced_bound_of_50_exclusion exclude) residual30 S gp size

#print axioms restricted25
#print axioms residual30
#print axioms es7_le_81_of_balanced50
end ES7CapacityStage
