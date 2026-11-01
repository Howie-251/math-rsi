import Aris4Math.General.Structure.Definitions
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Push
import Lean.Elab.Tactic.Omega

namespace Aris4Math.General.RS

open scoped BigOperators
universe u
variable {V : Type u} [DecidableEq V]

private theorem eq_of_single_inter {e f : Finset V} (h : (e ∩ f).card = 1)
    {x y : V} (hx : x ∈ e ∩ f) (hy : y ∈ e ∩ f) : x = y := by
  obtain ⟨z, hz⟩ := Finset.card_eq_one.mp h
  rw [hz] at hx hy
  simpa using (Finset.mem_singleton.mp hx).trans (Finset.mem_singleton.mp hy).symm

/-- A star centered outside a member has at most `k` members. -/
theorem singleIntersecting_star_card_le {E : Finset (Finset V)} {k : ℕ}
    (hU : Uniform E k) (hS : SingleIntersecting E)
    {x : V} {f : Finset V} (hf : f ∈ E) (hxf : x ∉ f) :
    (E.filter (fun g => x ∈ g)).card ≤ k := by
  classical
  let pick : Finset V → V := fun g => if h : (g ∩ f).Nonempty then h.choose else x
  have hp {g : Finset V} (hg : g ∈ E.filter (fun g => x ∈ g)) : pick g ∈ g ∩ f := by
    obtain ⟨hgE, hxg⟩ := Finset.mem_filter.mp hg
    have hgf : g ≠ f := by rintro rfl; exact hxf hxg
    have hn := Finset.card_pos.mp (by rw [hS g hgE f hf hgf]; omega)
    simpa [pick, hn] using hn.choose_spec
  calc
    _ ≤ f.card := Finset.card_le_card_of_injOn pick
      (fun g hg => (Finset.mem_inter.mp (hp hg)).2) (by
        intro g hg h hh heq
        by_contra hne
        have hxg := (Finset.mem_filter.mp hg).2
        have hxh := (Finset.mem_filter.mp hh).2
        have hpg := hp hg
        have hph := hp hh
        have hxy := eq_of_single_inter (hS g (Finset.mem_filter.mp hg).1 h
          (Finset.mem_filter.mp hh).1 hne)
          (Finset.mem_inter.mpr ⟨hxg, hxh⟩)
          (Finset.mem_inter.mpr ⟨(Finset.mem_inter.mp hpg).1,
            heq.symm ▸ (Finset.mem_inter.mp hph).1⟩)
        exact hxf (hxy ▸ (Finset.mem_inter.mp hpg).2))
    _ = k := hU f hf

/-- With no common vertex, a uniform single-intersecting family has at most
`k²-k+1` members. -/
theorem singleIntersecting_card_le_of_no_common {E : Finset (Finset V)} {k : ℕ}
    (hU : Uniform E k) (hS : SingleIntersecting E) (_hk : 2 ≤ k)
    (hN : ¬ ∃ x : V, ∀ e ∈ E, x ∈ e) : E.card ≤ k * k - k + 1 := by
  classical
  by_cases hE : E.Nonempty
  · obtain ⟨e, he⟩ := hE
    have hstar (x : V) : (E.filter (fun g => x ∈ g)).card ≤ k := by
      have hnx : ∃ f ∈ E, x ∉ f := by
        by_contra h
        push_neg at h
        exact hN ⟨x, h⟩
      obtain ⟨f, hf, hxf⟩ := hnx
      exact singleIntersecting_star_card_le hU hS hf hxf
    let parts : V → Finset (Finset V) := fun x => (E.filter (fun g => x ∈ g)).erase e
    have hcover : E.erase e ⊆ e.biUnion parts := by
      intro f hf
      obtain ⟨hne, hfE⟩ := Finset.mem_erase.mp hf
      have hn := Finset.card_pos.mp (by rw [hS f hfE e he hne]; omega)
      let x := hn.choose
      obtain ⟨hxf, hxe⟩ := Finset.mem_inter.mp hn.choose_spec
      exact Finset.mem_biUnion.mpr ⟨x, hxe, Finset.mem_erase.mpr ⟨hne,
        Finset.mem_filter.mpr ⟨hfE, hxf⟩⟩⟩
    have hpbound {x : V} (hx : x ∈ e) : (parts x).card ≤ k - 1 := by
      have hem : e ∈ E.filter (fun g => x ∈ g) := Finset.mem_filter.mpr ⟨he, hx⟩
      dsimp [parts]
      rw [Finset.card_erase_of_mem hem]
      exact Nat.sub_le_sub_right (hstar x) 1
    have hcount : (E.erase e).card ≤ k * (k - 1) := calc
      _ ≤ (e.biUnion parts).card := Finset.card_le_card hcover
      _ ≤ ∑ x ∈ e, (parts x).card := Finset.card_biUnion_le
      _ ≤ ∑ _x ∈ e, (k - 1) := Finset.sum_le_sum fun x hx => hpbound hx
      _ = k * (k - 1) := by simp [hU e he]
    rw [Finset.card_erase_of_mem he] at hcount
    have hpoly : k * (k - 1) = k * k - k := by
      rw [Nat.mul_sub_left_distrib, Nat.mul_one]
    rw [hpoly] at hcount
    have hpos := Finset.card_pos.mpr (show E.Nonempty from ⟨e, he⟩)
    omega
  · have : E = ∅ := Finset.not_nonempty_iff_eq_empty.mp hE
    simp [this]

/-- After removing a common vertex, all member remainders are disjoint. -/
theorem singleIntersecting_common_point_bound [Fintype V]
    {E : Finset (Finset V)} {k : ℕ} (hU : Uniform E k)
    (hS : SingleIntersecting E) {x : V} (hx : ∀ e ∈ E, x ∈ e) :
    E.card * (k - 1) + 1 ≤ Fintype.card V := by
  classical
  let rem : Finset V → Finset V := fun e => e.erase x
  have hd : (E : Set (Finset V)).PairwiseDisjoint rem := by
    intro e he f hf hne
    apply Finset.disjoint_left.mpr
    intro y hy hf_y
    have hyE := Finset.mem_erase.mp hy
    have hyF := Finset.mem_erase.mp hf_y
    exact hyE.1 (eq_of_single_inter (hS e he f hf hne)
      (Finset.mem_inter.mpr ⟨hyE.2, hyF.2⟩)
      (Finset.mem_inter.mpr ⟨hx e he, hx f hf⟩))
  have hbound : (E.biUnion rem).card ≤ (Finset.univ.erase x).card := by
    apply Finset.card_le_card
    intro y hy
    obtain ⟨e, he, hy⟩ := Finset.mem_biUnion.mp hy
    exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hy).1, Finset.mem_univ y⟩
  rw [Finset.card_biUnion hd] at hbound
  have hsum : (∑ e ∈ E, (rem e).card) = E.card * (k - 1) := by
    calc
      _ = ∑ _e ∈ E, (k - 1) := Finset.sum_congr rfl fun e he => by
        dsimp [rem]
        rw [Finset.card_erase_of_mem (hx e he), hU e he]
      _ = _ := by simp
  rw [hsum] at hbound
  have hvpos : 0 < Fintype.card V := Fintype.card_pos_iff.mpr ⟨x⟩
  simp only [Finset.card_erase_of_mem (Finset.mem_univ x), Finset.card_univ] at hbound
  omega

/-- The common-point dichotomy bounds every actual single-intersecting family,
including the empty family. -/
theorem singleIntersecting_card_le_cliqueBudget [Fintype V]
    {E : Finset (Finset V)} {k : ℕ} (hU : Uniform E k)
    (hk : 2 ≤ k) (hS : SingleIntersecting E) :
    E.card ≤ cliqueBudget k (Fintype.card V) := by
  classical
  by_cases hcommon : ∃ x : V, ∀ e ∈ E, x ∈ e
  · obtain ⟨x, hx⟩ := hcommon
    have hb := singleIntersecting_common_point_bound hU hS hx
    have hkpos : 0 < k - 1 := by omega
    have hm : E.card * (k - 1) ≤ Fintype.card V - 1 := by omega
    exact (Nat.le_div_iff_mul_le hkpos).mpr hm |>.trans (Nat.le_max_right _ _)
  · exact (singleIntersecting_card_le_of_no_common hU hS hk hcommon).trans
      (Nat.le_max_left _ _)

/-- A clique consists of actual distinct original edges, so the combinatorial
family bound applies without any realization hypothesis. -/
theorem singleGraph_isClique_card_le_cliqueBudget [Fintype V]
    {E : Finset (Finset V)} {k : ℕ} (hU : Uniform E k) (hk : 2 ≤ k)
    (s : Finset {e : Finset V // e ∈ E})
    (hs : (singleGraph E).IsClique (s : Set _)) :
    s.card ≤ cliqueBudget k (Fintype.card V) := by
  classical
  let F : Finset (Finset V) := s.image Subtype.val
  have hFU : Uniform F k := by
    intro e he
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp he
    exact hU a.val a.property
  have hFS : SingleIntersecting F := by
    intro e he f hf hne
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp he
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hf
    have hab : a ≠ b := fun h => hne (congrArg Subtype.val h)
    convert (hs ha hb hab).2 using 1
    congr 1
    ext x
    simp
  have hc : F.card = s.card := Finset.card_image_of_injective s Subtype.val_injective
  rw [← hc]
  exact singleIntersecting_card_le_cliqueBudget hFU hk hFS

end Aris4Math.General.RS
