import Aris4Math.LinkDeletion
import Aris4Math.TypeCounting

/-! Direction-sensitive lower bounds for the finite type tables used in the
link correction. These checks enumerate table types, never hypergraphs. -/

open scoped BigOperators

namespace Aris4Math.LinkWeightCertificates

open Aris4Math.Numeric Aris4Math.TypeCounting Aris4Math.LinkDeletion

/-- Allowed distinct incident edges must have different types or at least two
actual members of their shared type. -/
def IncidentWeightBound (p : Profile) (k : ℕ) (c : ℚ) : Prop :=
  ∀ t ∈ p.types, ∀ u ∈ p.types,
    k ∈ t.locks → k ∈ u.locks →
    (t.locks = u.locks → 2 ≤ t.count) →
    c ≤ pairWeight p t u k + pairWeight p u t k

instance (p : Profile) (k : ℕ) (c : ℚ) : Decidable (IncidentWeightBound p k c) := by
  unfold IncidentWeightBound
  infer_instance

theorem v21_d7_weight : IncidentWeightBound v21_d7 11 (42/4199) := by decide +kernel

theorem v22_67_weight : IncidentWeightBound v22_67 12 (3/323) := by decide +kernel

theorem v22_77_weight_left : IncidentWeightBound v22_77 11 (3/323) := by decide +kernel

theorem v22_77_weight_right : IncidentWeightBound v22_77 12 (3/323) := by decide +kernel

theorem v23_66_weight_left : IncidentWeightBound v23_66 11 (11/1292) := by decide +kernel

theorem v23_66_weight_right : IncidentWeightBound v23_66 12 (22/2261) := by decide +kernel

theorem v23_677_weight_middle : IncidentWeightBound v23_677 12 (3/323) := by decide +kernel


variable {α : Type*} [DecidableEq α]

/-- A shared type of two distinct actual objects has at least two members. -/
theorem shared_type_count_ge_two (E : Finset α) (classify : α → List ℕ)
    (p : Profile) (real : TableRealization E classify p)
    (a b : α) (ha : a ∈ E) (hb : b ∈ E) (hab : a ≠ b)
    (t : EdgeType) (ht : t ∈ p.types)
    (hta : classify a = t.locks) (htb : classify b = t.locks) : 2 ≤ t.count := by
  rw [← real.counts t ht]
  have hsub : {a,b} ⊆ fiber E classify t.locks := by
    simp only [Finset.insert_subset_iff, Finset.singleton_subset_iff]
    exact ⟨Finset.mem_filter.mpr ⟨ha,hta⟩, Finset.mem_filter.mpr ⟨hb,htb⟩⟩
  have hcard := Finset.card_le_card hsub
  simpa only [Finset.card_pair hab, multiplicity] using hcard

/-- Transfer a finite type certificate to two actual distinct objects. -/
theorem realized_pair_weight_bound (E : Finset α) (classify : α → List ℕ)
    (p : Profile) (real : TableRealization E classify p)
    (k : ℕ) (c : ℚ) (cert : IncidentWeightBound p k c)
    (a b : α) (ha : a ∈ E) (hb : b ∈ E) (hab : a ≠ b)
    (hka : k ∈ classify a) (hkb : k ∈ classify b) :
    c ≤ pairWeight p ⟨classify a,0⟩ ⟨classify b,0⟩ k +
      pairWeight p ⟨classify b,0⟩ ⟨classify a,0⟩ k := by
  obtain ⟨t,ht,hta⟩ := List.mem_map.mp (real.covers a ha)
  obtain ⟨u,hu,hub⟩ := List.mem_map.mp (real.covers b hb)
  have hcap : t.locks = u.locks → 2 ≤ t.count := by
    intro htu
    exact shared_type_count_ge_two E classify p real a b ha hb hab t ht
      hta.symm (hub.symm.trans htu.symm)
  have bound := cert t ht u hu (hta ▸ hka) (hub ▸ hkb) hcap
  change c ≤ pairWeight p ⟨t.locks,0⟩ ⟨u.locks,0⟩ k +
    pairWeight p ⟨u.locks,0⟩ ⟨t.locks,0⟩ k at bound
  rwa [hta,hub] at bound

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Actual edge-type bookkeeping weight, retaining ordered direction. -/
def typeWeight (p : Profile) (classify : Finset V → List ℕ) (k : ℕ)
    (d : Finset V × Finset V) : ℚ :=
  pairWeight p ⟨classify d.1,0⟩ ⟨classify d.2,0⟩ k

/-- No arbitrary hypergraph enumeration is involved: table completeness and
true multiplicities transfer the finite comparison to every actual bad pair. -/
theorem realized_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (classify : Finset V → List ℕ) (p : Profile)
    (real : TableRealization H.edges classify p) (k q : ℕ) (c : ℚ)
    (center : ∀ e ∈ H.incidentEdges x, k ∈ classify e)
    (hq : q ≤ (H.badLinkPairs x).card) (hc : 0 ≤ c)
    (cert : IncidentWeightBound p k c) :
    (q : ℚ) * c ≤ ∑ d ∈ directedBadPairs H x, typeWeight p classify k d := by
  apply uniform_bad_weight_lower H x (typeWeight p classify k) q c hq hc
  apply unordered_bound_of_incident_bound
  intro a ha b hb hab
  exact realized_pair_weight_bound H.edges classify p real k c cert a b
    (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab (center a ha) (center b hb)

/-- Membership of a locked center in an edge is exactly membership of its
one-based position in the canonical position-type list. -/
theorem center_mem_positionType {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices positions : ι ↪ Fin v) (e : Finset (Fin v)) (j : ι) :
    (positions j).val + 1 ∈ positionType vertices positions e ↔ vertices j ∈ e := by
  simp only [positionType, Finset.mem_sort, positionSignature, Finset.mem_image,
    mem_lockSignature]
  constructor
  · rintro ⟨i,hi,hij⟩
    have : i = j := positions.injective (Fin.ext (Nat.add_right_cancel hij))
    simpa only [this] using hi
  · exact fun h => ⟨j,h,rfl⟩


section Centers

variable {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The geometric center, actual P8 count and finite table comparison combine
to a lower bound for the actual distinct ordered deletion entries. -/
theorem realized_center_deduction {edgeCount : ℕ} (H : Simple5Hypergraph (Fin v))
    (cover : H.PairCovering) (vertices positions : ι ↪ Fin v) (p : Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : ι) (k q : ℕ) (c : ℚ)
    (hk : (positions j).val + 1 = k)
    (hq : q ≤ (4 * H.degree (vertices j) - (v - 1) + 2) / 3)
    (hc : 0 ≤ c) (cert : IncidentWeightBound p k c)
    (hded : deduction p k ≤ (q : ℚ) * c) :
    deduction p k ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight p (positionType vertices positions) k d := by
  apply hded.trans
  apply realized_bad_weight_lower H (vertices j) (positionType vertices positions)
    p real.table k q c _ _ hc cert
  · intro e he
    rw [← hk, center_mem_positionType]
    exact (Finset.mem_filter.mp he).2
  · exact hq.trans (by simpa only [Fintype.card_fin] using
      H.link_bad_pair_lower_bound cover (vertices j))

end Centers

/-- Actual deletion lower bound for the 21-vertex profile at position 11. -/
theorem v21_d7_deduction_11 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 21)
    (real : RealizesProfile H vertices positions v21_d7) (j : ι)
    (hk : (positions j).val + 1 = 11) (hdegree : H.degree (vertices j) = 7) :
    deduction v21_d7 11 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v21_d7 (positionType vertices positions) 11 d := by
  apply realized_center_deduction H cover vertices positions v21_d7 real j 11 3 (42/4199) hk
  · simp [hdegree]
  · norm_num
  · exact v21_d7_weight
  · decide +kernel

/-- Actual deletion lower bound for the 22-vertex profile at position 12. -/
theorem v22_67_deduction_12 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 22)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 22)
    (real : RealizesProfile H vertices positions v22_67) (j : ι)
    (hk : (positions j).val + 1 = 12) (hdegree : H.degree (vertices j) = 7) :
    deduction v22_67 12 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v22_67 (positionType vertices positions) 12 d := by
  apply realized_center_deduction H cover vertices positions v22_67 real j 12 3 (3/323) hk
  · simp [hdegree]
  · norm_num
  · exact v22_67_weight
  · decide +kernel

/-- Actual deletion lower bound for the 22-vertex profile at position 11. -/
theorem v22_77_deduction_11 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 22)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 22)
    (real : RealizesProfile H vertices positions v22_77) (j : ι)
    (hk : (positions j).val + 1 = 11) (hdegree : H.degree (vertices j) = 7) :
    deduction v22_77 11 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v22_77 (positionType vertices positions) 11 d := by
  apply realized_center_deduction H cover vertices positions v22_77 real j 11 3 (3/323) hk
  · simp [hdegree]
  · norm_num
  · exact v22_77_weight_left
  · decide +kernel

/-- Actual deletion lower bound for the 22-vertex profile at position 12. -/
theorem v22_77_deduction_12 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 22)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 22)
    (real : RealizesProfile H vertices positions v22_77) (j : ι)
    (hk : (positions j).val + 1 = 12) (hdegree : H.degree (vertices j) = 7) :
    deduction v22_77 12 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v22_77 (positionType vertices positions) 12 d := by
  apply realized_center_deduction H cover vertices positions v22_77 real j 12 3 (3/323) hk
  · simp [hdegree]
  · norm_num
  · exact v22_77_weight_right
  · decide +kernel

/-- Actual deletion lower bound for the 23-vertex profile at position 11. -/
theorem v23_66_deduction_11 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 23)
    (real : RealizesProfile H vertices positions v23_66) (j : ι)
    (hk : (positions j).val + 1 = 11) (hdegree : H.degree (vertices j) = 6) :
    deduction v23_66 11 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v23_66 (positionType vertices positions) 11 d := by
  apply realized_center_deduction H cover vertices positions v23_66 real j 11 1 (11/1292) hk
  · simp [hdegree]
  · norm_num
  · exact v23_66_weight_left
  · decide +kernel

/-- Actual deletion lower bound for the 23-vertex profile at position 12. -/
theorem v23_66_deduction_12 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 23)
    (real : RealizesProfile H vertices positions v23_66) (j : ι)
    (hk : (positions j).val + 1 = 12) (hdegree : H.degree (vertices j) = 6) :
    deduction v23_66 12 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v23_66 (positionType vertices positions) 12 d := by
  apply realized_center_deduction H cover vertices positions v23_66 real j 12 1 (22/2261) hk
  · simp [hdegree]
  · norm_num
  · exact v23_66_weight_right
  · decide +kernel

/-- Actual deletion lower bound for the 23-vertex profile at position 12. -/
theorem v23_677_deduction_12 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 23)
    (real : RealizesProfile H vertices positions v23_677) (j : ι)
    (hk : (positions j).val + 1 = 12) (hdegree : H.degree (vertices j) = 7) :
    deduction v23_677 12 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v23_677 (positionType vertices positions) 12 d := by
  apply realized_center_deduction H cover vertices positions v23_677 real j 12 2 (3/323) hk
  · simp [hdegree]
  · norm_num
  · exact v23_677_weight_middle
  · decide +kernel


/-- Same finite comparison with a specified exceptional type family. -/
def IncidentWeightBoundExcept (p : Profile) (k : ℕ) (c : ℚ)
    (exceptionTypes : List (List ℕ)) : Prop :=
  ∀ t ∈ p.types, ∀ u ∈ p.types,
    k ∈ t.locks → k ∈ u.locks →
    (t.locks = u.locks → 2 ≤ t.count) →
    (t.locks ∉ exceptionTypes ∨ u.locks ∉ exceptionTypes) →
    c ≤ pairWeight p t u k + pairWeight p u t k

instance (p : Profile) (k : ℕ) (c : ℚ) (ts : List (List ℕ)) :
    Decidable (IncidentWeightBoundExcept p k c ts) := by
  unfold IncidentWeightBoundExcept
  infer_instance

theorem v23_677_weight_last_nonnegative : IncidentWeightBound v23_677 13 0 := by
  decide +kernel

theorem v23_677_weight_last_except :
    IncidentWeightBoundExcept v23_677 13 (3/323) [[11,13],[12,13]] := by
  decide +kernel

/-- The finite exceptional-type comparison is transferred to actual edges. -/
theorem realized_pair_weight_bound_except (E : Finset α) (classify : α → List ℕ)
    (p : Profile) (real : TableRealization E classify p)
    (k : ℕ) (c : ℚ) (ts : List (List ℕ))
    (cert : IncidentWeightBoundExcept p k c ts)
    (a b : α) (ha : a ∈ E) (hb : b ∈ E) (hab : a ≠ b)
    (hka : k ∈ classify a) (hkb : k ∈ classify b)
    (hout : classify a ∉ ts ∨ classify b ∉ ts) :
    c ≤ pairWeight p ⟨classify a,0⟩ ⟨classify b,0⟩ k +
      pairWeight p ⟨classify b,0⟩ ⟨classify a,0⟩ k := by
  obtain ⟨t,ht,hta⟩ := List.mem_map.mp (real.covers a ha)
  obtain ⟨u,hu,hub⟩ := List.mem_map.mp (real.covers b hb)
  have hcap : t.locks = u.locks → 2 ≤ t.count := by
    intro htu
    exact shared_type_count_ge_two E classify p real a b ha hb hab t ht
      hta.symm (hub.symm.trans htu.symm)
  have bound := cert t ht u hu (hta ▸ hka) (hub ▸ hkb) hcap
    (by simpa only [hta,hub] using hout)
  change c ≤ pairWeight p ⟨t.locks,0⟩ ⟨u.locks,0⟩ k +
    pairWeight p ⟨u.locks,0⟩ ⟨t.locks,0⟩ k at bound
  rwa [hta,hub] at bound

/-- Two exceptional actual edges give a capacity-one exception, even if the
exceptional pair is itself bad and carries zero weight. -/
theorem realized_exceptional_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (classify : Finset V → List ℕ) (p : Profile)
    (real : TableRealization H.edges classify p) (k q : ℕ) (c : ℚ)
    (center : ∀ e ∈ H.incidentEdges x, k ∈ classify e)
    (hq : q ≤ (H.badLinkPairs x).card) (hc : 0 ≤ c)
    (nonneg : IncidentWeightBound p k 0)
    (ts : List (List ℕ)) (cert : IncidentWeightBoundExcept p k c ts)
    (S : Finset (Finset V)) (hS : S.card ≤ 2)
    (hmem : ∀ e ∈ H.edges, classify e ∈ ts → e ∈ S) :
    ((q - 1 : ℕ) : ℚ) * c ≤ ∑ d ∈ directedBadPairs H x, typeWeight p classify k d := by
  apply two_exceptional_edges_weight_lower H x S hS (typeWeight p classify k) q c hq hc
  · intro a ha b hb hab
    exact realized_pair_weight_bound H.edges classify p real k 0 nonneg a b
      (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab (center a ha) (center b hb)
  · intro a ha b hb hab hout
    apply realized_pair_weight_bound_except H.edges classify p real k c ts cert a b
      (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab (center a ha) (center b hb)
    rcases hout with haS | hbS
    · exact Or.inl (fun hm => haS (hmem a (Finset.mem_filter.mp ha).1 hm))
    · exact Or.inr (fun hm => hbS (hmem b (Finset.mem_filter.mp hb).1 hm))

/-- The exceptional type families xz and yz contain only one actual edge each.
Consequently they can consume at most one of the two guaranteed bad slots. -/
theorem v23_677_deduction_13 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices positions : ι ↪ Fin 23)
    (real : RealizesProfile H vertices positions v23_677) (j : ι)
    (hk : (positions j).val + 1 = 13) (hdegree : H.degree (vertices j) = 7) :
    deduction v23_677 13 ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight v23_677 (positionType vertices positions) 13 d := by
  let classify := positionType vertices positions
  let S := fiber H.edges classify [11,13] ∪ fiber H.edges classify [12,13]
  have hcount1 : (fiber H.edges classify [11,13]).card = 1 :=
    real.table.counts ⟨[11,13],1⟩ (by decide +kernel)
  have hcount2 : (fiber H.edges classify [12,13]).card = 1 :=
    real.table.counts ⟨[12,13],1⟩ (by decide +kernel)
  have hS : S.card ≤ 2 := by
    have := Finset.card_union_le (fiber H.edges classify [11,13]) (fiber H.edges classify [12,13])
    simpa only [hcount1,hcount2] using this
  have hq : 2 ≤ (H.badLinkPairs (vertices j)).card := by
    have := H.link_bad_pair_lower_bound cover (vertices j)
    simpa only [Fintype.card_fin, hdegree] using this
  have bound := realized_exceptional_bad_weight_lower H (vertices j) classify v23_677
    real.table 13 2 (3/323) (by
      intro e he
      rw [← hk, center_mem_positionType]
      exact (Finset.mem_filter.mp he).2) hq (by norm_num)
    v23_677_weight_last_nonnegative [[11,13],[12,13]] v23_677_weight_last_except S hS (by
      intro e he htype
      simp only [List.mem_cons, List.not_mem_nil, or_false] at htype
      rcases htype with h1 | h2
      · exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨he,h1⟩)
      · exact Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨he,h2⟩))
  have hded : deduction v23_677 13 ≤ ((2-1 : ℕ) : ℚ) * (3/323) := by decide +kernel
  exact hded.trans bound

end Aris4Math.LinkWeightCertificates

#print axioms Aris4Math.LinkWeightCertificates.v21_d7_weight
#print axioms Aris4Math.LinkWeightCertificates.v23_677_weight_middle

#print axioms Aris4Math.LinkWeightCertificates.realized_bad_weight_lower
#print axioms Aris4Math.LinkWeightCertificates.center_mem_positionType

#print axioms Aris4Math.LinkWeightCertificates.v21_d7_deduction_11
#print axioms Aris4Math.LinkWeightCertificates.v23_66_deduction_12
#print axioms Aris4Math.LinkWeightCertificates.v23_677_deduction_12

#print axioms Aris4Math.LinkWeightCertificates.v23_677_deduction_13
#print axioms Aris4Math.LinkWeightCertificates.v22_67_deduction_12
#print axioms Aris4Math.LinkWeightCertificates.v22_77_deduction_11
#print axioms Aris4Math.LinkWeightCertificates.v22_77_deduction_12
#print axioms Aris4Math.LinkWeightCertificates.v23_66_deduction_11
