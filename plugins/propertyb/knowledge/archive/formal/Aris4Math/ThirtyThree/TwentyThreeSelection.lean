import Aris4Math.LowDegree
import Mathlib.Tactic.FinCases
import Mathlib.Data.Fin.VecNotation

/-!
Actual degree counts and lock selection for the 23-point, 33-edge branches.
All sets and codegrees below are computed from the original hypergraph.
-/
namespace Aris4Math.ThirtyThree.TwentyThreeSelection

open scoped BigOperators
variable {V : Type*} [Fintype V] [DecidableEq V]

def sevenVertices (H : Simple5Hypergraph V) : Finset V :=
  Finset.univ.filter fun x => H.degree x = 7

@[simp] theorem mem_sevenVertices (H : Simple5Hypergraph V) (x : V) :
    x ∈ sevenVertices H ↔ H.degree x = 7 := by simp [sevenVertices]

theorem min_degree_six (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (x : V) : 6 ≤ H.degree x := by
  have h := H.pairCovering_degree_bound cover x
  rw [vertices] at h
  omega

/-- The complete degree split starts from the actual incidence sum 165. -/
theorem six_seven_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 23) :
    19 ≤ 2 * H.sixVertices.card + (sevenVertices H).card := by
  have each (x : V) : 8 ≤ H.degree x +
      (if H.degree x = 6 then 2 else 0) + (if H.degree x = 7 then 1 else 0) := by
    have hm := min_degree_six H cover vertices x
    split_ifs <;> omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have sixsum : (∑ x : V, if H.degree x = 6 then 2 else 0) =
      2 * H.sixVertices.card := by
    rw [← Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices,Nat.mul_comm]
  have hs : 8 * Fintype.card V ≤ 165 + 2 * H.sixVertices.card +
      (sevenVertices H).card := by
    simpa only [Finset.sum_add_distrib, sixsum, H.sum_degrees, edges,
      Finset.sum_boole, Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
      Simple5Hypergraph.sixVertices, sevenVertices, Nat.mul_comm] using h
  rw [vertices] at hs
  omega

theorem degree_count_cases (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 23) :
    4 ≤ H.sixVertices.card ∨
    (H.sixVertices.card = 3 ∧ 13 ≤ (sevenVertices H).card) ∨
    (H.sixVertices.card = 2 ∧ 15 ≤ (sevenVertices H).card) ∨
    (H.sixVertices.card = 1 ∧ 17 ≤ (sevenVertices H).card) ∨
    (H.sixVertices.card = 0 ∧ 19 ≤ (sevenVertices H).card) := by
  have h := six_seven_budget H cover edges vertices
  omega

theorem six_badPartners_le_two (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {x : V} (degree : H.degree x = 6) :
    (H.badPartners x).card ≤ 2 := by
  have h := H.badPartners_card_le_excess cover x
  simpa [vertices,degree] using h

theorem seven_badPartners_le_six (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {x : V} (degree : H.degree x = 7) :
    (H.badPartners x).card ≤ 6 := by
  have h := H.badPartners_card_le_excess cover x
  simpa [vertices,degree] using h

/-- Restricting the excess sum to any actual set of other vertices is sound. -/
theorem six_subset_excess_le_two (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {x : V} (degree : H.degree x = 6)
    (S : Finset V) (apart : x ∉ S) :
    (∑ y ∈ S, (H.codegree x y - 1)) ≤ 2 := by
  have sub : S ⊆ Finset.univ.erase x := by
    intro y hy
    refine Finset.mem_erase.mpr ⟨?_,Finset.mem_univ y⟩
    intro h
    exact apart (h ▸ hy)
  have h := Finset.sum_le_sum_of_subset sub (f := fun y => H.codegree x y - 1)
  rw [H.sum_codegree_excess cover x, vertices, degree] at h
  exact h

theorem six_codegree_le_three (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {x y : V} (degree : H.degree x = 6)
    (distinct : x ≠ y) : H.codegree x y ≤ 3 := by
  have h := six_subset_excess_le_two H cover vertices degree {y} (by simpa using distinct)
  simp only [Finset.sum_singleton] at h
  omega

/-- The local pair-budget constraint is inherited by any injectively indexed
lock set containing a six-degree center. -/
theorem indexed_six_excess_le_two (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {n : ℕ} (f : Fin n → V)
    (injective : Function.Injective f) (i : Fin n) (degree : H.degree (f i) = 6) :
    (∑ j ∈ Finset.univ.erase i, (H.codegree (f i) (f j) - 1)) ≤ 2 := by
  let S := (Finset.univ.erase i).image f
  have apart : f i ∉ S := by
    intro h
    obtain ⟨j,hj,equal⟩ := Finset.mem_image.mp h
    exact (Finset.mem_erase.mp hj).1 (injective equal)
  have h := six_subset_excess_le_two H cover vertices degree S apart
  dsimp [S] at h
  rw [Finset.sum_image (fun a _ b _ eq => injective eq)] at h
  exact h

/-- Delete the union of the bad-neighbor sets of actual low-degree locks. -/
def commonUnitSevens (H : Simple5Hypergraph V) (L : Finset V) : Finset V :=
  sevenVertices H \ L.biUnion H.badPartners

theorem commonUnitSevens_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (L : Finset V)
    (degrees : ∀ x ∈ L, H.degree x = 6) :
    (sevenVertices H).card ≤ (commonUnitSevens H L).card + 2 * L.card := by
  have h1 := Finset.card_le_card_sdiff_add_card
    (s := sevenVertices H) (t := L.biUnion H.badPartners)
  have h2 := Finset.card_biUnion_le (s := L) (t := H.badPartners)
  have h3 := Finset.sum_le_sum (s := L)
    (fun x hx => six_badPartners_le_two H cover vertices (degrees x hx))
  have h4 : (∑ _x ∈ L, (2 : ℕ)) = 2 * L.card := by simp [Nat.mul_comm]
  rw [h4] at h3
  change (sevenVertices H).card ≤ (commonUnitSevens H L).card +
    (L.biUnion H.badPartners).card at h1
  omega

theorem commonUnitSevens_degrees (H : Simple5Hypergraph V) (L : Finset V)
    {y : V} (hy : y ∈ commonUnitSevens H L) : H.degree y = 7 :=
  (mem_sevenVertices H y).mp (Finset.mem_sdiff.mp hy).1

theorem commonUnitSevens_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (L : Finset V) (degrees : ∀ x ∈ L, H.degree x = 6)
    {x y : V} (hx : x ∈ L) (hy : y ∈ commonUnitSevens H L) :
    x ≠ y ∧ H.codegree x y = 1 := by
  have dx := degrees x hx
  have dy := commonUnitSevens_degrees H L hy
  have xy : x ≠ y := by intro h; rw [h] at dx; omega
  have good : y ∈ H.goodPartners x := by
    apply Finset.mem_sdiff.mpr
    refine ⟨Finset.mem_univ y, ?_⟩
    intro hi
    rcases Finset.mem_insert.mp hi with hyx | hbad
    · exact xy hyx.symm
    · exact (Finset.mem_sdiff.mp hy).2 (Finset.mem_biUnion.mpr ⟨x,hx,hbad⟩)
  exact ⟨xy,((H.mem_goodPartners cover x y).mp good).2⟩

omit [Fintype V] [DecidableEq V] in
/-- Label actual selected vertices, without any assumptions about a profile. -/
theorem exists_indexed_subset (S : Finset V) {n : ℕ} (size : n ≤ S.card) :
    ∃ f : Fin n → V, Function.Injective f ∧ ∀ i, f i ∈ S := by
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq size
  let e : ↥T ≃ Fin n := Fintype.equivFinOfCardEq (by simpa using card)
  refine ⟨fun i => (e.symm i).val, ?_, ?_⟩
  · exact Subtype.val_injective.comp e.symm.injective
  · intro i
    exact sub (e.symm i).property

/-- The r≥4 branch may choose four arbitrary distinct six-degree vertices. -/
theorem exists_four_sixes (H : Simple5Hypergraph V) (many : 4 ≤ H.sixVertices.card) :
    ∃ f : Fin 4 → V, Function.Injective f ∧ ∀ i, H.degree (f i) = 6 := by
  obtain ⟨f,inj,inside⟩ := exists_indexed_subset H.sixVertices many
  exact ⟨f,inj,fun i => (Finset.mem_filter.mp (inside i)).2⟩

/-- Three low locks exclude at most six of the seven-degree points. -/
theorem exists_three_sixes_two_sevens (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices : Fintype.card V = 23)
    (lows : 3 ≤ H.sixVertices.card) (highs : 8 ≤ (sevenVertices H).card) :
    ∃ f : Fin 5 → V, Function.Injective f ∧
      (∀ i, H.degree (f i) = if i.val < 3 then 6 else 7) ∧
      (∀ i j, i.val < 3 → 3 ≤ j.val → H.codegree (f i) (f j) = 1) := by
  obtain ⟨L,Lsub,Lcard⟩ := Finset.exists_subset_card_eq lows
  have Ldeg (x : V) (hx : x ∈ L) : H.degree x = 6 :=
    (Finset.mem_filter.mp (Lsub hx)).2
  have budget := commonUnitSevens_budget H cover vertices L Ldeg
  have Psize : 2 ≤ (commonUnitSevens H L).card := by omega
  obtain ⟨a,ainj,ainside⟩ := exists_indexed_subset L (n := 3) (by omega)
  obtain ⟨b,binj,binside⟩ := exists_indexed_subset (commonUnitSevens H L) Psize
  let f : Fin 5 → V := Fin.append a b
  have finj : Function.Injective f := by
    apply Fin.append_injective_iff.mpr
    refine ⟨ainj,binj,?_⟩
    intro i j
    exact (commonUnitSevens_unit H cover L Ldeg (ainside i) (binside j)).1
  refine ⟨f,finj,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,Fin.append] <;>
      first | exact Ldeg _ (ainside _) | exact commonUnitSevens_degrees H L (binside _)
  · intro i j hi hj
    fin_cases i <;> fin_cases j <;> norm_num at hi <;> norm_num at hj <;>
      exact (commonUnitSevens_unit H cover L Ldeg (ainside _) (binside _)).2

theorem exists_three_sixes_two_sevens_of_count (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 33)
    (vertices : Fintype.card V = 23) (count : H.sixVertices.card = 3) :
    ∃ f : Fin 5 → V, Function.Injective f ∧
      (∀ i, H.degree (f i) = if i.val < 3 then 6 else 7) ∧
      (∀ i j, i.val < 3 → 3 ≤ j.val → H.codegree (f i) (f j) = 1) := by
  have budget := six_seven_budget H cover edges vertices
  exact exists_three_sixes_two_sevens H cover vertices (by omega) (by omega)

/-- In a large set of seven-degree vertices choose a center with two unit
neighbors. Only the pair between those neighbors remains unrestricted. -/
theorem exists_three_sevens_two_unit (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices : Fintype.card V = 23)
    (S : Finset V) (degrees : ∀ x ∈ S, H.degree x = 7) (many : 9 ≤ S.card) :
    ∃ a ∈ S, ∃ b ∈ S, ∃ c ∈ S,
      a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ H.codegree a c = 1 ∧ H.codegree b c = 1 := by
  obtain ⟨c,hc⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
  let B := insert c (H.badPartners c)
  have badsize := seven_badPartners_le_six H cover vertices (degrees c hc)
  have insertSize := Finset.card_insert_le c (H.badPartners c)
  have budget := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
  have manyUnit : 1 < (S \ B).card := by dsimp [B] at budget ⊢; omega
  obtain ⟨a,ha,b,hb,ab⟩ := Finset.one_lt_card.mp manyUnit
  obtain ⟨haS,haB⟩ := Finset.mem_sdiff.mp ha
  obtain ⟨hbS,hbB⟩ := Finset.mem_sdiff.mp hb
  have agood : a ∈ H.goodPartners c := Finset.mem_sdiff.mpr ⟨Finset.mem_univ a,haB⟩
  have bgood : b ∈ H.goodPartners c := Finset.mem_sdiff.mpr ⟨Finset.mem_univ b,hbB⟩
  obtain ⟨ac,ca⟩ := (H.mem_goodPartners cover c a).mp agood
  obtain ⟨bc,cb⟩ := (H.mem_goodPartners cover c b).mp bgood
  exact ⟨a,haS,b,hbS,c,hc,ab,ac,bc,
    (H.codegree_comm a c).trans ca,(H.codegree_comm b c).trans cb⟩

/-- Two low locks and three high locks leave only the disjoint pairs 01 and
23 unrestricted. Their remaining eight codegrees are exactly one. -/
theorem exists_two_sixes_three_sevens (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices : Fintype.card V = 23)
    (lows : 2 ≤ H.sixVertices.card) (highs : 13 ≤ (sevenVertices H).card) :
    ∃ f : Fin 5 → V, Function.Injective f ∧
      (∀ i, H.degree (f i) = if i.val < 2 then 6 else 7) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) := by
  obtain ⟨L,Lsub,Lcard⟩ := Finset.exists_subset_card_eq lows
  have Ldeg (x : V) (hx : x ∈ L) : H.degree x = 6 :=
    (Finset.mem_filter.mp (Lsub hx)).2
  obtain ⟨x,hx,y,hy,xy⟩ := Finset.one_lt_card.mp (show 1 < L.card by omega)
  let P := commonUnitSevens H L
  have budget := commonUnitSevens_budget H cover vertices L Ldeg
  have Psize : 9 ≤ P.card := by dsimp [P]; omega
  have Pdeg (z : V) (hz : z ∈ P) : H.degree z = 7 :=
    commonUnitSevens_degrees H L hz
  obtain ⟨a,ha,b,hb,c,hc,ab,ac,bc,cac,cbc⟩ :=
    exists_three_sevens_two_unit H cover vertices P Pdeg Psize
  have cross (u : V) (hu : u ∈ L) (v : V) (hv : v ∈ P) :
      u ≠ v ∧ H.codegree u v = 1 := commonUnitSevens_unit H cover L Ldeg hu hv
  obtain ⟨xa,cxa⟩ := cross x hx a ha
  obtain ⟨xb,cxb⟩ := cross x hx b hb
  obtain ⟨xc,cxc⟩ := cross x hx c hc
  obtain ⟨ya,cya⟩ := cross y hy a ha
  obtain ⟨yb,cyb⟩ := cross y hy b hb
  obtain ⟨yc,cyc⟩ := cross y hy c hc
  let f : Fin 5 → V := ![x,y,a,b,c]
  have finj : Function.Injective f := by
    intro i j heq
    fin_cases i <;> fin_cases j <;>
      simp [f,xy,xy.symm,xa,xa.symm,xb,xb.symm,xc,xc.symm,
        ya,ya.symm,yb,yb.symm,yc,yc.symm,ab,ab.symm,ac,ac.symm,bc,bc.symm] at heq <;> rfl
  refine ⟨f,finj,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,Ldeg x hx,Ldeg y hy,Pdeg a ha,Pdeg b hb,Pdeg c hc]
  · intro i j hij h01 h23
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;>
      simp [Fin.ext_iff] at h01 <;> simp [Fin.ext_iff] at h23 <;>
      first | exact cxa | exact cxb | exact cxc | exact cya |
        exact cyb | exact cyc | exact cac | exact cbc

theorem exists_two_sixes_three_sevens_of_count (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 33)
    (vertices : Fintype.card V = 23) (count : H.sixVertices.card = 2) :
    ∃ f : Fin 5 → V, Function.Injective f ∧
      (∀ i, H.degree (f i) = if i.val < 2 then 6 else 7) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) := by
  have budget := six_seven_budget H cover edges vertices
  exact exists_two_sixes_three_sevens H cover vertices (by omega) (by omega)

end Aris4Math.ThirtyThree.TwentyThreeSelection

#print axioms Aris4Math.ThirtyThree.TwentyThreeSelection.degree_count_cases
#print axioms Aris4Math.ThirtyThree.TwentyThreeSelection.indexed_six_excess_le_two
#print axioms Aris4Math.ThirtyThree.TwentyThreeSelection.exists_four_sixes
#print axioms Aris4Math.ThirtyThree.TwentyThreeSelection.exists_three_sixes_two_sevens_of_count
#print axioms Aris4Math.ThirtyThree.TwentyThreeSelection.exists_two_sixes_three_sevens_of_count
