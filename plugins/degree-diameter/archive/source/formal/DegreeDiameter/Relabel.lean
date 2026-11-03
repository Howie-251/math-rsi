import DegreeDiameter.Definitions

namespace DegreeDiameter

attribute [local instance] Classical.propDecidable
noncomputable section

variable {V W : Type*} [Fintype V] [Fintype W]

theorem degree_bound_of_iso {G : SimpleGraph V} {H : SimpleGraph W}
    (e : G ≃g H) (h : degreeAtMostEight G) : degreeAtMostEight H := by
  intro w
  have heq : G.degree (e.symm w) = H.degree w := by
    rw [← SimpleGraph.card_neighborSet_eq_degree, ← SimpleGraph.card_neighborSet_eq_degree]
    exact Fintype.card_congr ((e.mapNeighborSet (e.symm w)).trans
      (Equiv.setCongr (congrArg H.neighborSet (e.apply_symm_apply w))))
  have hb := h (e.symm w)
  rw [heq] at hb
  exact hb

omit [Fintype V] [Fintype W] in
theorem diameter_bound_of_iso {G : SimpleGraph V} {H : SimpleGraph W}
    (e : G ≃g H) (h : diameterAtMostTwo G) : diameterAtMostTwo H := by
  intro u v huv
  have hne : e.symm u ≠ e.symm v := fun hh => huv (e.symm.injective hh)
  rcases h (e.symm u) (e.symm v) hne with ha | ⟨w, huw, hwv⟩
  · left
    simpa using e.map_adj_iff.mpr ha
  · right
    refine ⟨e w, ?_, ?_⟩
    · simpa using e.map_adj_iff.mpr huw
    · simpa using e.map_adj_iff.mpr hwv

/-- Every finite original graph, in any universe, has an actual Fin n copy. -/
theorem finite_relabel (G : SimpleGraph V) {n : ℕ} (hn : Fintype.card V = n)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G) :
    ∃ H : SimpleGraph (Fin n), degreeAtMostEight H ∧ diameterAtMostTwo H := by
  exact ⟨G.overFin hn, degree_bound_of_iso (G.overFinIso hn) hdeg,
    diameter_bound_of_iso (G.overFinIso hn) hdiam⟩

/-- The Type 0 existence specification accepts arbitrary-universe finite graphs. -/
theorem exists82_of_original_graph (G : SimpleGraph V) {n : ℕ}
    (hn : Fintype.card V = n) (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G) : Exists82 n := by
  obtain ⟨H, hd, hp⟩ := finite_relabel G hn hdeg hdiam
  exact ⟨Fin n, inferInstance, H, Fintype.card_fin n, hd, hp⟩

/-- Existence can equivalently be stated on the canonical finite carrier. -/
theorem exists82_iff_fin (n : ℕ) : Exists82 n ↔
    ∃ H : SimpleGraph (Fin n), degreeAtMostEight H ∧ diameterAtMostTwo H := by
  constructor
  · rintro ⟨V, inst, G, hn, hd, hp⟩
    letI := inst
    exact finite_relabel G hn hd hp
  · rintro ⟨H, hd, hp⟩
    exact ⟨Fin n, inferInstance, H, Fintype.card_fin n, hd, hp⟩

end
end DegreeDiameter
