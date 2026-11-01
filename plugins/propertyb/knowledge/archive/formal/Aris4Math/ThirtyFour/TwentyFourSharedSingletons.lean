import Aris4Math.ThirtyThree.ActualBadSlot

namespace Aris4Math.ThirtyFour.TwentyFourSharedSingletons
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.MultiLockRecovery

private theorem collision_three {α : Type*} [DecidableEq α] (f : Fin 3→α)
    (small : (Finset.univ.image f).card≤2) :
    f 0=f 1 ∨ f 0=f 2 ∨ f 1=f 2 := by
  by_contra h
  push_neg at h
  have dom : (Finset.univ : Finset (Fin 3))={0,1,2} := by decide
  rw [dom] at small
  simp [h.1,h.2.1,h.2.2] at small

def first : Fin 3→Fin 3 := ![0,0,1]
def second : Fin 3→Fin 3 := ![1,2,2]
private theorem distinct : ∀p,first p≠second p := by decide +kernel

/-- Three pairwise unit high vertices can all use singleton-low edges at at most
three low labels whose singleton multiplicity is at most two. The chosen bad
collision pair at each label injects into the three high pairs. -/
theorem at_most_three {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (low : Fin n↪Fin v) (high : Fin 3↪Fin v) (S : Finset (Fin n))
    (unit : ∀i j,i≠j→H.codegree (high i) (high j)=1)
    (small : ∀i∈S,count H low {i}≤2)
    (occurs : ∀i∈S,∀j,∃e∈H.edges,lockSignature low e={i} ∧ high j∈e) :
    S.card≤3 := by
  classical
  let I := {i // i∈S}
  have ex (i : I) (j : Fin 3) := occurs i.val i.property j
  choose E member trace contains using ex
  have collision (i : I) : ∃p : Fin 3,E i (first p)=E i (second p) := by
    have sub : Finset.univ.image (E i) ⊆ fiber H.edges (lockSignature low) {i.val} := by
      intro e he
      obtain ⟨j,_,rfl⟩ := Finset.mem_image.mp he
      exact Finset.mem_filter.mpr ⟨member i j,trace i j⟩
    have card := (Finset.card_le_card sub).trans (small i.val i.property)
    obtain h | h | h := collision_three (E i) card
    · exact ⟨0,h⟩
    · exact ⟨1,h⟩
    · exact ⟨2,h⟩
  choose p same using collision
  have injective : Function.Injective p := by
    intro i k eq
    have hi₂ : high (second (p i))∈E i (first (p i)) := by
      rw [same i];exact contains i (second (p i))
    have hk₁ : high (first (p i))∈E k (first (p k)) := by
      rw [eq];exact contains k (first (p k))
    have hk₂ : high (second (p i))∈E k (first (p k)) := by
      rw [eq,same k];exact contains k (second (p k))
    have sameEdge := H.edge_unique_of_codegree_one (unit _ _ (distinct (p i)))
      (member i _) (member k _) (contains i _) hi₂ hk₁ hk₂
    have sig := congrArg (lockSignature low) sameEdge
    rw [trace,trace] at sig
    exact Subtype.ext (Finset.singleton_injective sig)
  have bound := Fintype.card_le_of_injective p injective
  simpa only [I,Fintype.card_coe,Fintype.card_fin] using bound
end Aris4Math.ThirtyFour.TwentyFourSharedSingletons
#print axioms Aris4Math.ThirtyFour.TwentyFourSharedSingletons.at_most_three
