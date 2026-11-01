import Aris4Math.ThirtyThree.ActualBadSlot
import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageKernel

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
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitData
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case := Fin 9
def μ : Case→Finset (Fin 6)→ℕ := ![fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={5} then 1 else if T=∅ then 13 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T=∅ then 12 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 10 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={2,3,5} then 1 else if T={1,4,5} then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 3 else if T=∅ then 11 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 10 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T=∅ then 11 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,2,3,4,5} then 1 else if T={0} then 1 else if T={1} then 4 else if T={2} then 4 else if T={3} then 4 else if T={4} then 4 else if T={5} then 4 else if T=∅ then 7 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,2,3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 3 else if T={4} then 2 else if T={5} then 4 else if T=∅ then 9 else 0,fun T=>if T={0,1} then 1 else if T={2,3} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={1,2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={0} then 3 else if T={1} then 3 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 9 else 0]
def upper (T : Finset (Fin 6)) : ℕ := if T=∅ then 34 else if T.card=1 then 6 else 1
abbrev largeCase (i : Case) : TwentyFourNoLowSixData.Case := i.castLE (by omega)
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitData

namespace Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourSixLowUnitData

/-- The same four-label argument handles intersecting and disjoint low triples.
The first/second-high classification must still supply the occurrence premise. -/
theorem impossible_three_typeA (H : Simple5Hypergraph (Fin 24))
    (low : Fin 6↪Fin 24) (high : Fin 3↪Fin 24) (i : Case) (kind : i=3 ∨ i=5)
    (counts : ∀T,count H low T=μ i T)
    (unit : ∀a b,a≠b→H.codegree (high a) (high b)=1)
    (occurs : ∀a j,∃e∈H.edges,lockSignature low e={a} ∧ high j∈e) : False := by
  let S : Finset (Fin 6) := {0,1,2,3}
  have small : ∀a∈S,count H low {a}≤2 := by
    intro a ha
    rw [counts]
    have numerical : ∀i : Case,i=3 ∨ i=5→∀a∈({0,1,2,3}:Finset (Fin 6)),μ i {a}≤2 := by
      decide +kernel
    exact numerical i kind a ha
  have bound := TwentyFourSharedSingletons.at_most_three H low high S unit small
    (fun a _ j=>occurs a j)
  have card : S.card=4 := by decide
  omega

/-- Three highs cannot have opposite A/B labels on every pair. -/
theorem impossible_binary_opposites (kind : Fin 3→Bool)
    (opposite : ∀i j,i≠j→kind i≠kind j) : False := by
  have injective : Function.Injective kind := fun i j eq=>by
    by_contra ne
    exact opposite i j ne eq
  have card := Fintype.card_le_of_injective kind injective
  norm_num at card
end Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions.impossible_three_typeA