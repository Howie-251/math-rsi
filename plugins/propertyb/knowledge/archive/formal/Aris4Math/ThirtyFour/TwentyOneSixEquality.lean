import Aris4Math.ThirtyFour.TwentyOneFiveStructure
import Aris4Math.ThirtyFour.Incidence

/-! Actual lock selection in the degree-six equality case. The caller supplies
the pair and per-edge conclusions of its local classification; all cardinality,
excess, and common-edge conclusions below come from the actual hypergraph. -/

namespace Aris4Math.ThirtyFour.TwentyOneSixEquality

open scoped BigOperators
open TwentyOneFiveStructure (eights mem_eights)

/-- With one degree-six point and no other degree below eight, at least sixteen
points have degree exactly eight. -/
theorem eights_at_least_sixteen (H : Simple5Hypergraph (Fin 21))
    (size : H.edges.card=34) (x : Fin 21) (dx : H.degree x=6)
    (minimum : ∀ y, y ≠ x → 8 ≤ H.degree y) :
    16 ≤ (eights H).card := by
  classical
  have each (y : Fin 21) : 9 ≤ H.degree y + (if y=x then 3 else 0) +
      (if y ∈ eights H then 1 else 0) := by
    by_cases eq : y=x
    · simp [eq,dx,eights]
    have lo := minimum y eq
    by_cases eight : H.degree y=8
    · simp [eq,eight,eights]
    simp only [mem_eights,eq,eight,if_false,add_zero]
    omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun y _ => each y)
  have budget : 189 ≤ 170+3+(eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,Nat.mul_comm] using sum
  omega

/-- The six x-edges have capacity twelve for the degree-eight unit neighbors.
The four available excess units and the degree budget force equality. -/
theorem equality_cardinalities (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (x : Fin 21) (dx : H.degree x=6)
    (minimum : ∀ y, y ≠ x → 8 ≤ H.degree y)
    (U : Finset (Fin 21))
    (memU : ∀ u, u ∈ U ↔ H.degree u=8 ∧ H.codegree x u=1)
    (capacity : ∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 2) :
    U.card=12 ∧ (eights H \ U).card=4 := by
  classical
  have usub : U ⊆ eights H := by
    intro u hu
    exact (mem_eights H u).mpr ((memU u).mp hu).1
  have unit : (∑ u ∈ U, H.codegree x u)=U.card := by
    calc
      _ = ∑ _u ∈ U, (1 : ℕ) :=
        Finset.sum_congr rfl (fun u hu => ((memU u).mp hu).2)
      _ = U.card := by simp
  have uupper := Incidence.codegree_capacity H x U 2 capacity
  rw [unit,dx] at uupper
  have bsub : eights H \ U ⊆ H.badPartners x := by
    intro b hb
    obtain ⟨hb,notU⟩ := Finset.mem_sdiff.mp hb
    have db := (mem_eights H b).mp hb
    have bx : b ≠ x := by intro eq; subst b; omega
    have low := H.one_le_codegree cover bx.symm
    have notUnit : H.codegree x b ≠ 1 := by
      intro one
      exact notU ((memU b).mpr ⟨db,one⟩)
    exact Finset.mem_filter.mpr ⟨by simp [bx],by omega⟩
  have bad := H.badPartners_card_le_excess cover x
  rw [dx] at bad
  simp only [Fintype.card_fin] at bad
  have bupper := (Finset.card_le_card bsub).trans bad
  have split := Finset.card_sdiff_add_card_eq_card usub
  have many := eights_at_least_sixteen H size x dx minimum
  omega

/-- Saturating all six capacities forces two members of U in every actual
edge through x, rather than only an average of two. -/
theorem two_on_every_edge (H : Simple5Hypergraph (Fin 21))
    (x : Fin 21) (dx : H.degree x=6) (U : Finset (Fin 21))
    (cardU : U.card=12) (unit : ∀ u ∈ U, H.codegree x u=1)
    (capacity : ∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 2) :
    ∀ e ∈ H.edges, x ∈ e → (U ∩ e).card=2 := by
  classical
  have total : (∑ u ∈ U, H.codegree x u)=12 := by
    calc
      _ = ∑ _u ∈ U, (1 : ℕ) := Finset.sum_congr rfl unit
      _ = 12 := by simp [cardU]
  have upper : ∀ e ∈ H.edges.filter (fun e => x ∈ e), (U ∩ e).card ≤ 2 := by
    intro e he
    obtain ⟨he,hxe⟩ := Finset.mem_filter.mp he
    exact capacity e he hxe
  have sums : (∑ e ∈ H.edges.filter (fun e => x ∈ e), (U ∩ e).card) =
      ∑ _e ∈ H.edges.filter (fun e => x ∈ e), (2 : ℕ) := by
    rw [← Incidence.sum_codegrees_subset H x U,total]
    have countX : (H.edges.filter (fun e => x ∈ e)).card=6 := dx
    simp [countX]
  have each := (Finset.sum_eq_sum_iff_of_le upper).mp sums
  intro e he hxe
  exact each e (Finset.mem_filter.mpr ⟨he,hxe⟩)

/-- Eleven codegree-two neighbors spend eleven of an eight-degree point's
twelve excess units. Every point outside U therefore has codegree at most two. -/
theorem outside_codegree_le_two (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (U : Finset (Fin 21)) (cardU : U.card=12)
    (degrees : ∀ u ∈ U, H.degree u=8)
    (pairs : ∀ u ∈ U, ∀ v ∈ U, u ≠ v → H.codegree u v=2)
    (u b : Fin 21) (hu : u ∈ U) (hb : b ∉ U) :
    H.codegree u b ≤ 2 := by
  classical
  have bu : b ≠ u := by intro eq; subst b; exact hb hu
  have notErase : b ∉ U.erase u := by
    intro h
    exact hb (Finset.mem_of_mem_erase h)
  have sub : insert b (U.erase u) ⊆ Finset.univ.erase u := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · simp [bu]
    · exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hz).1,Finset.mem_univ z⟩
  have bound := Finset.sum_le_sum_of_subset sub (f := fun z => H.codegree u z-1)
  rw [H.sum_codegree_excess cover u,degrees u hu] at bound
  simp only [Fintype.card_fin] at bound
  have other : (∑ v ∈ U.erase u, (H.codegree u v-1))=11 := by
    calc
      _ = ∑ _v ∈ U.erase u, (1 : ℕ) := by
        apply Finset.sum_congr rfl
        intro v hv
        have pair := pairs u hu v (Finset.mem_of_mem_erase hv)
          (Finset.mem_erase.mp hv).1.symm
        omega
      _ = 11 := by simp [Finset.card_erase_of_mem hu,cardU]
  rw [Finset.sum_insert notErase,other] at bound
  omega

/-- Select the actual four locks (x,u,v,b) for the five equality profiles.
Their common edge is retained so the caller can bind the exact four-trace. -/
theorem select_equality_locks (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (x : Fin 21) (dx : H.degree x=6)
    (minimum : ∀ y, y ≠ x → 8 ≤ H.degree y)
    (U : Finset (Fin 21))
    (memU : ∀ u, u ∈ U ↔ H.degree u=8 ∧ H.codegree x u=1)
    (pairs : ∀ u ∈ U, ∀ v ∈ U, u ≠ v → H.codegree u v=2)
    (capacity : ∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 2) :
    ∃ b u v e, H.degree b=8 ∧ u ∈ U ∧ v ∈ U ∧ u ≠ v ∧ b ∉ U ∧
      e ∈ H.edges ∧ x ∈ e ∧ b ∈ e ∧ u ∈ e ∧ v ∈ e ∧
      H.codegree x b=2 ∧ H.codegree u b ≤ 2 ∧ H.codegree v b ≤ 2 := by
  classical
  obtain ⟨cardU,cardB⟩ := equality_cardinalities H cover size x dx minimum U memU capacity
  let B := eights H \ U
  have bcard : B.card=4 := cardB
  have bdegree (b : Fin 21) (hb : b ∈ B) : H.degree b=8 :=
    (mem_eights H b).mp (Finset.mem_sdiff.mp hb).1
  have bx (b : Fin 21) (hb : b ∈ B) : b ≠ x := by
    have db := bdegree b hb
    intro eq
    subst b
    omega
  have lower (b : Fin 21) (hb : b ∈ B) : 1 ≤ H.codegree x b-1 := by
    have low := H.one_le_codegree cover (bx b hb).symm
    have notUnit : H.codegree x b ≠ 1 := by
      intro one
      exact (Finset.mem_sdiff.mp hb).2 ((memU b).mpr ⟨bdegree b hb,one⟩)
    omega
  have bsub : B ⊆ Finset.univ.erase x := by
    intro b hb
    simp [bx b hb]
  have upper := Finset.sum_le_sum_of_subset bsub (f := fun b => H.codegree x b-1)
  rw [H.sum_codegree_excess cover x,dx] at upper
  simp only [Fintype.card_fin] at upper
  have lowerSum := Finset.sum_le_sum lower
  have sumB : (∑ b ∈ B, (H.codegree x b-1))=4 := by
    have low : 4 ≤ ∑ b ∈ B, (H.codegree x b-1) := by
      simpa [bcard] using lowerSum
    omega
  have eachExcess : ∀ b ∈ B, (1 : ℕ)=H.codegree x b-1 :=
    (Finset.sum_eq_sum_iff_of_le lower).mp (by simp [sumB,bcard])
  obtain ⟨b,hb⟩ := Finset.card_pos.mp (show 0 < B.card by omega)
  have lambda : H.codegree x b=2 := by
    have excess := eachExcess b hb
    omega
  obtain ⟨e,he,hxe,hbe⟩ := cover x b (bx b hb).symm
  have two := two_on_every_edge H x dx U cardU
    (fun u hu => ((memU u).mp hu).2) capacity e he hxe
  obtain ⟨u,hu,v,hv,uv⟩ := Finset.one_lt_card.mp (show 1 < (U ∩ e).card by omega)
  obtain ⟨hu,hue⟩ := Finset.mem_inter.mp hu
  obtain ⟨hv,hve⟩ := Finset.mem_inter.mp hv
  have bout := (Finset.mem_sdiff.mp hb).2
  have degrees : ∀ u ∈ U, H.degree u=8 := fun u hu => ((memU u).mp hu).1
  exact ⟨b,u,v,e,bdegree b hb,hu,hv,uv,bout,he,hxe,hbe,hue,hve,lambda,
    outside_codegree_le_two H cover U cardU degrees pairs u b hu bout,
    outside_codegree_le_two H cover U cardU degrees pairs v b hv bout⟩

end Aris4Math.ThirtyFour.TwentyOneSixEquality
