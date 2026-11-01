import Aris4Math.SmallVertices
import Aris4Math.ThirtyThree.Reduction

/-! The equality case of the 34-edge balanced union bound has an actual
positive overlap. This strictness is proved on the permutation sample space. -/
namespace Aris4Math.ThirtyFour.SmallVertices
open scoped BigOperators
open Aris4Math.SmallVertices
universe u
variable {V : Type u} [Fintype V] [DecidableEq V]

theorem propertyB_of_partition_count_overlap (H : Simple5Hypergraph V)
    (red : Finset V)
    (e f : Finset V) (he : e ∈ H.edges) (hf : f ∈ H.edges) (hne : e ≠ f)
    (emono : e ⊆ red ∨ e ⊆ redᶜ) (fmono : f ⊆ red ∨ f ⊆ redᶜ)
    (weak : H.edges.card *
      ((red.card.choose 5 + (Fintype.card V - red.card).choose 5) *
        (Nat.factorial 5 * (Fintype.card V - 5).factorial)) ≤
      (Fintype.card V).factorial) : PropertyB H := by
  classical
  let event := fun e => monochromaticPermutations e red ∪
    monochromaticPermutations e redᶜ
  let bad := H.edges.biUnion event
  let C := (red.card.choose 5 + (Fintype.card V - red.card).choose 5) *
    (Nat.factorial 5 * (Fintype.card V - 5).factorial)
  have event_bound (e : Finset V) (he : e ∈ H.edges) : (event e).card ≤ C := by
    calc
      _ ≤ (monochromaticPermutations e red).card +
          (monochromaticPermutations e redᶜ).card := Finset.card_union_le _ _
      _ = C := by
        rw [monochromaticPermutations_card, monochromaticPermutations_card,
          H.five_uniform e he, Finset.card_compl]
        exact (Nat.add_mul _ _ _).symm
  have eid : Equiv.refl V ∈ event e := by
    rcases emono with hr | hb
    · exact Finset.mem_union_left _ (by simpa [monochromaticPermutations] using hr)
    · exact Finset.mem_union_right _ (by simpa [monochromaticPermutations] using hb)
  have fid : Equiv.refl V ∈ event f := by
    rcases fmono with hr | hb
    · exact Finset.mem_union_left _ (by simpa [monochromaticPermutations] using hr)
    · exact Finset.mem_union_right _ (by simpa [monochromaticPermutations] using hb)
  have fi : f ∈ H.edges.erase e := Finset.mem_erase.mpr ⟨Ne.symm hne,hf⟩
  have intersect : 0 < (event e ∩ (H.edges.erase e).biUnion event).card :=
    Finset.card_pos.mpr ⟨Equiv.refl V,Finset.mem_inter.mpr
      ⟨eid,Finset.mem_biUnion.mpr ⟨f,fi,fid⟩⟩⟩
  have decompose : bad = event e ∪ (H.edges.erase e).biUnion event := by
    dsimp [bad]
    rw [← Finset.insert_erase he,Finset.biUnion_insert]
    simp
  have hcard := Finset.card_union_add_card_inter (event e) ((H.edges.erase e).biUnion event)
  have hrest : ((H.edges.erase e).biUnion event).card ≤ ∑ f ∈ H.edges.erase e, (event f).card :=
    Finset.card_biUnion_le
  have hsum := Finset.sum_erase_add (s := H.edges) (fun f => (event f).card) he
  dsimp only at hsum
  have strict_sum : bad.card < ∑ f ∈ H.edges, (event f).card := by
    rw [decompose]
    omega
  have bad_bound : bad.card < H.edges.card * C := by
    apply lt_of_lt_of_le strict_sum
    calc
      _ ≤ ∑ _e ∈ H.edges, C := Finset.sum_le_sum event_bound
      _ = H.edges.card * C := by simp
  have strict_sample : bad.card < (Finset.univ : Finset (Equiv.Perm V)).card := by
    rw [Finset.card_univ, Fintype.card_perm]
    exact lt_of_lt_of_le bad_bound weak
  obtain ⟨σ, _, hgood⟩ := Finset.exists_mem_notMem_of_card_lt_card strict_sample
  let c : V → Bool := fun x => decide (σ x ∈ red)
  refine ⟨c, ?_⟩
  intro e he
  have not_red : ¬ e.map σ.toEmbedding ⊆ red := by
    intro hmono
    apply hgood
    apply Finset.mem_biUnion.mpr
    refine ⟨e, he, Finset.mem_union_left _ ?_⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ σ, hmono⟩
  have not_blue : ¬ e.map σ.toEmbedding ⊆ redᶜ := by
    intro hmono
    apply hgood
    apply Finset.mem_biUnion.mpr
    refine ⟨e, he, Finset.mem_union_right _ ?_⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ σ, hmono⟩
  have red_witness : ∃ x ∈ e, σ x ∈ red := by
    by_contra hnone
    apply not_blue
    intro p hp
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hp
    exact Finset.mem_compl.mpr (fun hr => hnone ⟨x, hx, hr⟩)
  have blue_witness : ∃ x ∈ e, σ x ∉ red := by
    by_contra hnone
    apply not_red
    intro p hp
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hp
    by_contra hn
    exact hnone ⟨x, hx, hn⟩
  obtain ⟨r, hre, hrred⟩ := red_witness
  obtain ⟨b, hbe, hbblue⟩ := blue_witness
  have hrcolor : c r = true := by simp [c, hrred]
  have hbcolor : c b = false := by simp [c, hbblue]
  have lower : 1 ≤ (e.filter (fun x => c x = true)).card :=
    Finset.card_pos.mpr ⟨r, Finset.mem_filter.mpr ⟨hre, hrcolor⟩⟩
  have subset_erase : e.filter (fun x => c x = true) ⊆ e.erase b := by
    intro y hy
    obtain ⟨hye, hycolor⟩ := Finset.mem_filter.mp hy
    apply Finset.mem_erase.mpr
    refine ⟨?_, hye⟩
    intro hyb
    subst y
    simp [hbcolor] at hycolor
  have upper := Finset.card_le_card subset_erase
  rw [Finset.card_erase_of_mem hbe, H.five_uniform e he] at upper
  exact ⟨lower, upper⟩

/-- Two five-sets can simultaneously be monochromatic in a balanced coloring
at 17 or 18 vertices. The construction concerns just these two events. -/
theorem exists_balanced_overlap {v : ℕ} (lower : 17 ≤ v) (upper : v ≤ 18)
    (e f : Finset (Fin v)) (he : e.card = 5) (hf : f.card = 5) :
    ∃ red : Finset (Fin v), red.card = v/2 ∧
      (e ⊆ red ∨ e ⊆ redᶜ) ∧ (f ⊆ red ∨ f ⊆ redᶜ) := by
  classical
  by_cases disjoint : Disjoint e f
  · have sub : e ⊆ fᶜ := by
      intro x hx
      exact Finset.mem_compl.mpr (fun h => Finset.disjoint_left.mp disjoint hx h)
    have small : e.card ≤ v/2 := by omega
    have large : v/2 ≤ fᶜ.card := by simp only [Finset.card_compl,Fintype.card_fin,hf]; omega
    obtain ⟨red,ered,redsub,hred⟩ := Finset.exists_subsuperset_card_eq sub small large
    refine ⟨red,hred,Or.inl ered,Or.inr ?_⟩
    intro x hx
    exact Finset.mem_compl.mpr (fun h => Finset.mem_compl.mp (redsub h) hx)
  · have inter : 0 < (e ∩ f).card :=
      Finset.card_pos.mpr (Finset.not_disjoint_iff_nonempty_inter.mp disjoint)
    have unioncard := Finset.card_union_add_card_inter e f
    have unionsmall : (e ∪ f).card ≤ 9 := by omega
    obtain ⟨blue,sub,_,hblue⟩ := Finset.exists_subsuperset_card_eq
      (Finset.subset_univ (e ∪ f)) unionsmall
      (by simp only [Finset.card_univ,Fintype.card_fin]; omega : 9 ≤ (Finset.univ : Finset (Fin v)).card)
    refine ⟨blueᶜ,?_,Or.inr ?_,Or.inr ?_⟩
    · simp only [Finset.card_compl,Fintype.card_fin,hblue]; omega
    · simpa using (Finset.subset_union_left.trans sub)
    · simpa using (Finset.subset_union_right.trans sub)

theorem balanced_count_weak (v : ℕ) (lower : 17 ≤ v) (upper : v ≤ 18) :
    34 * (((v/2).choose 5 + (v-v/2).choose 5) *
      (Nat.factorial 5 * (v-5).factorial)) ≤ v.factorial := by
  interval_cases v <;> decide

/-- Actual overlap makes the boundary 34*(1/34)=1 strict. -/
theorem propertyB_seventeen_eighteen {v : ℕ} (lower : 17 ≤ v) (upper : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34) : PropertyB H := by
  by_cases old : H.edges.card ≤ 33
  · exact ThirtyThree.propertyB_of_vertices_le_eighteen upper H old
  have hcard : H.edges.card = 34 := by omega
  obtain ⟨e,he,f,hf,ne⟩ := Finset.one_lt_card.mp (show 1 < H.edges.card by omega)
  obtain ⟨red,hred,emono,fmono⟩ := exists_balanced_overlap lower upper e f
    (H.five_uniform e he) (H.five_uniform f hf)
  apply propertyB_of_partition_count_overlap H red e f he hf ne emono fmono
  simpa only [hcard,Fintype.card_fin,hred] using balanced_count_weak v lower upper

theorem balanced_count_strict (v : ℕ) (lower : 9 ≤ v) (upper : v ≤ 16) :
    34 * (((v/2).choose 5 + (v-v/2).choose 5) *
      (Nat.factorial 5 * (v-5).factorial)) < v.factorial := by
  interval_cases v <;> decide

theorem propertyB_nine_to_sixteen {v : ℕ} (lower : 9 ≤ v) (upper : v ≤ 16)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34) : PropertyB H := by
  classical
  have hhalf : v/2 ≤ (Finset.univ : Finset (Fin v)).card := by
    simpa using Nat.div_le_self v 2
  obtain ⟨red,_,hred⟩ := Finset.exists_subset_card_eq hhalf
  apply Aris4Math.SmallVertices.propertyB_of_partition_count_bound H red
  simp only [Fintype.card_fin,hred]
  exact lt_of_le_of_lt (Nat.mul_le_mul_right _ hsize) (balanced_count_strict v lower upper)

theorem propertyB_of_vertices_le_eighteen {v : ℕ} (hv : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34) : PropertyB H := by
  by_cases small : v ≤ 8
  · exact Reduction.propertyB_of_vertices_le_eight small H
  by_cases medium : v ≤ 16
  · exact propertyB_nine_to_sixteen (by omega) medium H hsize
  · exact propertyB_seventeen_eighteen (by omega) hv H hsize

end Aris4Math.ThirtyFour.SmallVertices
#print axioms Aris4Math.ThirtyFour.SmallVertices.propertyB_of_vertices_le_eighteen

