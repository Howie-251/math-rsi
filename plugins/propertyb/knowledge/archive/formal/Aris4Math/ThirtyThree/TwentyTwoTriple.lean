import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.TwentyTwoPureDeletion
import Aris4Math.ThirtyThree.CustomDeletion

namespace Aris4Math.ThirtyThree.TwentyTwoTriple
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.TripleProfiles

def positionFn : Fin 2 → Fin 3 → Fin 22 := ![
  ![12,7,8],
  ![12,7,10]]
theorem positionFn_injective : ∀ i,Function.Injective (positionFn i) := by decide

def positions (i : Fin 2) : Fin 3 ↪ Fin 22 := ⟨positionFn i,positionFn_injective i⟩
def counts (i : Fin 2) : Finset (Fin 3) → ℕ := recovered 33 7 7 7 2 2 1 i.val

def p (i : Fin 2) : Numeric.Profile :=
  pruneZero ⟨22,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T,counts i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Fin 2) : p i =
    profile (positions i) (counts i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 2 → Numeric.Profile := ![
  ⟨22,[8,9,13],[⟨[],17⟩,⟨[13],3⟩,⟨[8],4⟩,⟨[9],4⟩,⟨[8,13],2⟩,⟨[9,13],2⟩,⟨[8,9],1⟩],none,[13,8,9]⟩,
  ⟨22,[8,11,13],[⟨[],16⟩,⟨[13],4⟩,⟨[8],5⟩,⟨[11],5⟩,⟨[8,13],1⟩,⟨[11,13],1⟩,⟨[8,11,13],1⟩],none,[13,8,11]⟩]
theorem p_eq_computed (i : Fin 2) : p i=computed i := by fin_cases i <;> rfl
def c : Fin 2 → Fin 3 → ℚ := ![
  ![0,0,55/12597],
  ![0,55/12597,0]]
def d : Fin 2 → Fin 3 → ℚ := ![
  ![42/4199,55/8398,55/25194],
  ![42/4199,55/25194,42/4199]]
def lossAt : Fin 2 → Fin 3 → ℚ := ![
  ![0,0,110/12597],
  ![0,275/25194,42/4199]]

def loss (i : Fin 2) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then lossAt i 0 else
  if k=(positions i 1).val+1 then lossAt i 1 else
  if k=(positions i 2).val+1 then lossAt i 2 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem certificates : ∀ i : Fin 2,
    Numeric.validProfile (p i) 33 ∧
    (∑ k : Fin 22,min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 3,let k := (positions i j).val+1
      0 ≤ c i j ∧ 0 ≤ d i j ∧
      loss i k ≤ 3*c i j + ((4*counts i {j}+2-19)/3 : ℕ)*d i j -
        TwentyTwoPureDeletion.penaltySum (p i) k (c i j) (d i j) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card=33)
    (vertices : Fin 3 ↪ Fin 22) (i : Fin 2)
    (hd : ∀ j,H.degree (vertices j)=7)
    (hc01 : H.codegree (vertices 0) (vertices 1)=2)
    (hc02 : H.codegree (vertices 0) (vertices 2)=2)
    (hc12 : H.codegree (vertices 1) (vertices 2)=1)
    (ht : tripleCodegree H (vertices 0) (vertices 1) (vertices 2)=i.val) : PropertyB H := by
  obtain ⟨hv,hs,hbounds⟩ := certificates i
  have hm : ∀ T,count H vertices T=counts i T := by
    intro T
    rw [actual_recovered,triple_count_eq,edges33,hd 0,hd 1,hd 2,hc01,hc02,hc12,ht]
    rfl
  have real : RealizesProfile H vertices (positions i) (p i) 33 := by
    rw [p_eq] at hv ⊢
    exact realizes_profile H vertices (positions i) (counts i) hm _ hv
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    obtain ⟨hcn,hdn,hfinite⟩ := hbounds j
    apply TwentyTwoPureDeletion.realized_dual_deduction H cover vertices (positions i) (p i)
      real j _ 3 ((4*counts i {j}+2-19)/3) (counts i {j}) (c i j) (d i j) _ rfl
    · simp [hd]
    · exact hm {j}
    · exact le_rfl
    · exact hcn
    · exact hdn
    · exact hfinite
  · intro k hk
    have hne : ∀ j : Fin 3,k ≠ (positions i j).val+1 := by
      intro j heq
      apply hk
      rw [heq]
      change _ ∈ List.ofFn (fun j => (positions i j).val+1)
      exact List.mem_ofFn.mpr ⟨j,rfl⟩
    simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2)]
  · exact hs

theorem propertyB_of_path (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card=33)
    (vertices : Fin 3 ↪ Fin 22) (hd : ∀ j,H.degree (vertices j)=7)
    (hc01 : H.codegree (vertices 0) (vertices 1)=2)
    (hc02 : H.codegree (vertices 0) (vertices 2)=2)
    (hc12 : H.codegree (vertices 1) (vertices 2)=1) : PropertyB H := by
  have htle : tripleCodegree H (vertices 0) (vertices 1) (vertices 2) ≤ 1 := by
    rw [← hc12]
    apply Finset.card_le_card
    intro e he
    obtain ⟨he,_,h1,h2⟩ := Finset.mem_filter.mp he
    exact Finset.mem_filter.mpr ⟨he,h1,h2⟩
  exact propertyB_of_data H cover edges33 vertices
    ⟨tripleCodegree H (vertices 0) (vertices 1) (vertices 2),by omega⟩ hd hc01 hc02 hc12 rfl

end Aris4Math.ThirtyThree.TwentyTwoTriple
#print axioms Aris4Math.ThirtyThree.TwentyTwoTriple.propertyB_of_path
