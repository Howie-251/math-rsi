import DegreeDiameter.Portfolio.EvenQ8SourceFullBalancedInputs
import DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Inputs
import DegreeDiameter.Portfolio.Q8DiagonalFillDefinitions
import DegreeDiameter.Portfolio.DiagonalFillReallocationGeometry
namespace DegreeDiameter.Portfolio.Q8DiagonalFill
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem cover_certificate : ∀p,Source.linePoint (Source.spread (Source.spreadOwner p)) (coverSlot p)=p := by decide
theorem spread_cover (p : Source.Point) : Source.Inc p (Source.spread (Source.spreadOwner p)) :=
  ⟨coverSlot p,cover_certificate p⟩
theorem line_two_certificate : ∀l,Source.linePoint l 0 ≠ Source.linePoint l 1 := by decide
theorem line_two (l : Source.Line) : ∃a b,Source.Inc a l ∧ Source.Inc b l ∧ a≠b :=
  ⟨Source.linePoint l 0,Source.linePoint l 1,⟨0,rfl⟩,⟨1,rfl⟩,line_two_certificate l⟩
theorem compat (u v : Source.Old) : Source.graph.Adj (.inl u) (.inl v) ↔ raw.Adj u v := Iff.rfl
theorem raw_D3 : DiameterAtMost raw 3 :=
  DiagonalFillReallocation.raw_diameter_three Source.oldEquiv Source.Inc EvenQ8SourceFull.Balanced.project
theorem raw_no_isolated (v : Source.Old) : ∃w,raw.Adj v w := by
  have ht : ∃t:Source.Old,v≠t := by
    by_cases h0 : v=0
    · refine ⟨1,?_⟩;rw [h0];decide
    · exact ⟨0,h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := raw_D3 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩
theorem load_le_one (v : Source.Old) : FullNeighborhoodClones.load raw center v≤1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique Source.oldEquiv Source.Inc
    Source.ovoid Source.spread EvenQ8BalancedFullOvoidCopy82.ovoid_unique EvenQ8BalancedFullOvoidCopy82.spread_unique
    (.inl v) x.val y.val x.property y.property
theorem flag_route : ∀v,∃j w,Source.graph.Adj (.inr j) (.inl w) ∧ raw.Adj w v :=
  DiagonalFillReallocation.flag_neighbor Source.oldEquiv Source.Inc Source.spread
    Source.spreadOwner spread_cover line_two EvenQ8SourceFull.Balanced.project
theorem filler_route : ∀j c,∃w,∃p:Source.graph.Walk (.inr j) (.inl w),
    p.length≤2 ∧ raw.Adj w (center c) :=
  DiagonalFillReallocation.filler_route Source.oldEquiv Source.Inc Source.spread
    Source.ovoid Source.spreadOwner spread_cover line_two EvenQ8BalancedFullOvoidCopy82.spread_unique EvenQ8SourceFull.Balanced.project
#print axioms load_le_one
#print axioms flag_route
#print axioms filler_route
end DegreeDiameter.Portfolio.Q8DiagonalFill
