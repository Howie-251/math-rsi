import Aris4Math.ThirtyFour.TwentySevenPairs
import Aris4Math.ThirtyFour.TwentySevenTriples
import Aris4Math.ThirtyFour.TwentySevenQuad

namespace Aris4Math.ThirtyFour.TwentySevenMany
open scoped BigOperators
open Aris4Math.ThirtyFour.NineteenPairs
open Aris4Math.ThirtyThree.QuadProfiles (first second)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)

variable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
  (edges34 : H.edges.card = 34)
include cover edges34

theorem propertyB_of_unit (x y : Fin 20) (ne : x ≠ y)
    (dx : H.degree x = 7) (dy : H.degree y = 7) (hc : H.codegree x y=1) : PropertyB H :=
  TwentySevenPairs.propertyB_of_case H cover edges34 x y ne ⟨7,7,1,10,11⟩ (by decide) dx dy hc

theorem propertyB_of_high (x y : Fin 20) (ne : x ≠ y)
    (dx : H.degree x = 7) (dy : H.degree y = 7 ∨ H.degree y = 8)
    (hc : 4 ≤ H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at upper
  rcases dy with dy | dy
  · have mem : (⟨7,7,H.codegree x y,1,11⟩ : PairCase) ∈ TwentySevenPairs.cases := by
      interval_cases h : H.codegree x y <;> decide
    exact TwentySevenPairs.propertyB_of_case H cover edges34 x y ne _ mem dx dy rfl
  · have mem : (⟨8,7,H.codegree x y,1,11⟩ : PairCase) ∈ TwentySevenPairs.cases := by
      interval_cases h : H.codegree x y <;> decide
    exact TwentySevenPairs.propertyB_of_case H cover edges34 y x (Ne.symm ne) _ mem dy dx
      (H.codegree_comm y x)

def sevens : Finset (Fin 20) := Finset.univ.filter (fun x => H.degree x=7)

omit cover edges34 in
theorem mem_sevens (x : Fin 20) : x ∈ sevens H ↔ H.degree x=7 := by simp [sevens]

omit cover edges34 in
theorem exists_indexed_subset (S : Finset (Fin 20)) {n : ℕ} (size : n ≤ S.card) :
    ∃ f : Fin n ↪ Fin 20, ∀ i, f i ∈ S := by
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq size
  let e : ↥T ≃ Fin n := Fintype.equivFinOfCardEq (by simpa using card)
  refine ⟨⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩,?_⟩
  intro i
  exact sub (e.symm i).property

theorem seven_pair_bounds (noB : ¬ PropertyB H) (x y : Fin 20) (ne : x ≠ y)
    (dx : H.degree x=7) (dy : H.degree y=7) :
    2 ≤ H.codegree x y ∧ H.codegree x y ≤ 3 := by
  have one := H.one_le_codegree cover ne
  have notOne : H.codegree x y ≠ 1 := fun h => noB (propertyB_of_unit H cover edges34 x y ne dx dy h)
  have notHigh : ¬ 4 ≤ H.codegree x y := fun h => noB (propertyB_of_high H cover edges34 x y ne dx (Or.inl dy) h)
  omega

theorem seven_pairs_two (noB : ¬ PropertyB H) (many : 3 ≤ (sevens H).card)
    (x y : Fin 20) (ne : x ≠ y) (dx : H.degree x=7) (dy : H.degree y=7) :
    H.codegree x y=2 := by
  have ⟨lo,hi⟩ := seven_pair_bounds H cover edges34 noB x y ne dx dy
  by_contra hn
  have three : H.codegree x y=3 := by omega
  have third : ∃ z ∈ sevens H, z ≠ x ∧ z ≠ y := by
    by_contra hn
    have sub : sevens H ⊆ {x,y} := by
      intro z hz
      by_cases zx : z=x
      · simp [zx]
      by_cases zy : z=y
      · simp [zy]
      exact False.elim (hn ⟨z,hz,zx,zy⟩)
    have bound := Finset.card_le_card sub
    have pairCard : ({x,y} : Finset (Fin 20)).card ≤ 2 := by simp [ne]
    omega
  obtain ⟨z,hz,zx,zy⟩ := third
  have dz := (mem_sevens H z).mp hz
  have bxz := seven_pair_bounds H cover edges34 noB x z (Ne.symm zx) dx dz
  have byz := seven_pair_bounds H cover edges34 noB y z (Ne.symm zy) dy dz
  exact noB (TwentySevenTriples.propertyB_of_three_sevens H cover edges34 x y z
    ne (Ne.symm zx) (Ne.symm zy) dx dy dz lo bxz.1 byz.1 hi bxz.2 byz.2 (Or.inl three))

/-- Complete actual-input branch with at least four degree-seven vertices. -/
theorem propertyB_of_four_sevens (many : 4 ≤ (sevens H).card) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨f,hf⟩ := exists_indexed_subset (sevens H) many
  have hd (i : Fin 4) : H.degree (f i)=7 := (mem_sevens H (f i)).mp (hf i)
  have hc (i j : Fin 4) (ne : i ≠ j) : H.codegree (f i) (f j)=2 :=
    seven_pairs_two H cover edges34 noB (by omega) (f i) (f j) (f.injective.ne ne) (hd i) (hd j)
  apply noB
  apply TwentySevenQuad.propertyB_of_quad H cover edges34 f 0
  · intro j
    fin_cases j <;> simpa [TwentySevenQuad.degree] using hd _
  · intro j
    have ne : first j ≠ second j := by fin_cases j <;> decide
    simpa [TwentySevenQuad.co] using hc (first j) (second j) ne

/-- Complete minimum-seven branch once three degree-seven vertices exist. -/
theorem propertyB_of_many_sevens (minimum : ∀ x, 7 ≤ H.degree x)
    (many : 3 ≤ (sevens H).card) : PropertyB H := by
  classical
  by_cases four : 4 ≤ (sevens H).card
  · exact propertyB_of_four_sevens H cover edges34 four
  have cardThree : (sevens H).card=3 := by omega
  by_contra noB
  have eight : ∃ z, H.degree z=8 := by
    by_contra hn
    have each (x : Fin 20) : 9 ≤ H.degree x + (if x ∈ sevens H then 2 else 0) := by
      by_cases member : x ∈ sevens H
      · have dx := (mem_sevens H x).mp member
        simp [member,dx]
      · have dx : H.degree x ≠ 7 := fun h => member ((mem_sevens H x).mpr h)
        have dn : H.degree x ≠ 8 := fun h => hn ⟨x,h⟩
        have lo := minimum x
        simp only [member,if_false,add_zero]
        omega
    have sum := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
    have impossible : 180 ≤ 176 := by
      simpa [Finset.sum_add_distrib,H.sum_degrees,edges34,cardThree] using sum
    omega
  obtain ⟨z,dz⟩ := eight
  obtain ⟨f,hf⟩ := exists_indexed_subset (sevens H) many
  have hd (i : Fin 3) : H.degree (f i)=7 := (mem_sevens H (f i)).mp (hf i)
  have ne (i j : Fin 3) (h : i ≠ j) : f i ≠ f j := f.injective.ne h
  have nz (i : Fin 3) : f i ≠ z := by intro h; have := hd i; rw [h,dz] at this; omega
  have hc (i j : Fin 3) (h : i ≠ j) : H.codegree (f i) (f j)=2 :=
    seven_pairs_two H cover edges34 noB many (f i) (f j) (ne i j h) (hd i) (hd j)
  have upper (i : Fin 3) : H.codegree (f i) z ≤ 3 := by
    have notHigh : ¬ 4 ≤ H.codegree (f i) z := fun h => noB
      (propertyB_of_high H cover edges34 (f i) z (nz i) (hd i) (Or.inr dz) h)
    omega
  have uniform (j : Fin 3) (hj : 0 ≠ j) :
      H.codegree (f 0) z = H.codegree (f j) z ∧ H.codegree (f 0) z ≠ 3 := by
    have bad : ¬ (H.codegree (f 0) z ≠ H.codegree (f j) z ∨ H.codegree (f 0) z=3) := by
      intro good
      exact noB (TwentySevenTriples.propertyB_of_mixed H cover edges34 (f 0) (f j) z
        (ne 0 j hj) (nz 0) (nz j) (hd 0) (hd j) dz (hc 0 j hj) (upper 0) (upper j) good)
    exact ⟨by by_contra h; exact bad (Or.inl h),fun h => bad (Or.inr h)⟩
  have u1 := uniform 1 (by decide)
  have u2 := uniform 2 (by decide)
  have lower := H.one_le_codegree cover (nz 0)
  have upper0 := upper 0
  have alternatives : H.codegree (f 0) z=1 ∨ H.codegree (f 0) z=2 := by omega
  let vertices := fourVertices (f 0) (f 1) (f 2) z
    (ne 0 1 (by decide)) (ne 0 2 (by decide)) (nz 0)
    (ne 1 2 (by decide)) (nz 1) (nz 2)
  have hdv (kind : Fin 3) (hk : kind ≠ 0) : ∀ j,
      H.degree (vertices j) = TwentySevenQuad.degree kind j := by
    intro j
    fin_cases j <;> simp [vertices,fourVertices,TwentySevenQuad.degree,hk,hd,dz]
  rcases alternatives with h1 | h2
  · apply noB
    apply TwentySevenQuad.propertyB_of_quad H cover edges34 vertices 1 (hdv 1 (by decide))
    intro j
    have a := hc 0 1 (by decide)
    have b := hc 0 2 (by decide)
    have c := hc 1 2 (by decide)
    have d : H.codegree (f 1) z=1 := u1.1.symm.trans h1
    have e : H.codegree (f 2) z=1 := u2.1.symm.trans h1
    fin_cases j <;> simp [vertices,fourVertices,first,second,TwentySevenQuad.co,a,b,c,d,e,h1]
  · apply noB
    apply TwentySevenQuad.propertyB_of_quad H cover edges34 vertices 2 (hdv 2 (by decide))
    intro j
    have a := hc 0 1 (by decide)
    have b := hc 0 2 (by decide)
    have c := hc 1 2 (by decide)
    have d : H.codegree (f 1) z=2 := u1.1.symm.trans h2
    have e : H.codegree (f 2) z=2 := u2.1.symm.trans h2
    fin_cases j <;> simp [vertices,fourVertices,first,second,TwentySevenQuad.co,a,b,c,d,e,h2]

end Aris4Math.ThirtyFour.TwentySevenMany
#print axioms Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_four_sevens

#print axioms Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_many_sevens
