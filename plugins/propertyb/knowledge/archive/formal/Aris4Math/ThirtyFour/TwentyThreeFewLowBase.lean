import Aris4Math.ThirtyFour.TwentyThreeStrongCodegree

/-! Initial three-lock domains for one or two degree-six locks at 23 points.
These tables recover counts of all 34 edges of the actual hypergraph. -/
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowBase
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxHeartbeats 0
abbrev Case := Fin 6

def oneLow : Case → Finset (Fin 3) → ℕ
  | 0, T => if T=∅ then 17 else if T={0} then 4 else if T={1} then 5 else if T={0,1} then 1 else if T={2} then 5 else if T={0,2} then 1 else if T={1,2} then 1 else 0
  | 1, T => if T=∅ then 16 else if T={0} then 5 else if T={1} then 6 else if T={2} then 6 else if T={0,1,2} then 1 else 0
  | 2, T => if T=∅ then 18 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 2 else 0
  | 3, T => if T=∅ then 17 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={1,2} then 1 else if T={0,1,2} then 1 else 0
  | 4, T => if T=∅ then 19 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 3 else 0
  | 5, T => if T=∅ then 18 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 2 else if T={0,1,2} then 1 else 0

theorem oneLow_coverage : ∀ a : Fin 4, ∀ t : Fin 2,
    1≤a.val → ∀ T, recovered 34 6 7 7 1 1 a.val t.val T =
      oneLow ⟨2*(a.val-1)+t.val, by omega⟩ T := by decide +kernel

def twoLow : Case → Finset (Fin 3) → ℕ
  | 0, T => if T=∅ then 18 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={0,2} then 1 else if T={1,2} then 1 else 0
  | 1, T => if T=∅ then 17 else if T={0} then 5 else if T={1} then 5 else if T={2} then 6 else if T={0,1,2} then 1 else 0
  | 2, T => if T=∅ then 19 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 5 else if T={0,2} then 1 else if T={1,2} then 1 else 0
  | 3, T => if T=∅ then 18 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 6 else if T={0,1,2} then 1 else 0
  | 4, T => if T=∅ then 20 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 5 else if T={0,2} then 1 else if T={1,2} then 1 else 0
  | 5, T => if T=∅ then 19 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 6 else if T={0,1,2} then 1 else 0

theorem twoLow_coverage : ∀ a : Fin 4, ∀ t : Fin 2,
    1≤a.val → ∀ T, recovered 34 6 6 7 a.val 1 1 t.val T =
      twoLow ⟨2*(a.val-1)+t.val, by omega⟩ T := by decide +kernel

theorem actual_oneLow (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 3 ↪ Fin 23)
    (d0 : H.degree (f 0)=6) (d1 : H.degree (f 1)=7) (d2 : H.degree (f 2)=7)
    (unit01 : H.codegree (f 0) (f 1)=1) (unit02 : H.codegree (f 0) (f 2)=1)
    (cap12 : H.codegree (f 1) (f 2)≤3) :
    ∃ c : Case, ∀ T, count H f T=oneLow c T := by
  have low := H.one_le_codegree cover (f.injective.ne (by decide : (1:Fin 3)≠2))
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  rw [unit01] at ta
  let a : Fin 4 := ⟨H.codegree (f 1) (f 2),by omega⟩
  let t : Fin 2 := ⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  refine ⟨⟨2*(a.val-1)+t.val,by have := a.isLt; have := t.isLt; omega⟩,?_⟩
  intro T
  rw [actual_recovered,triple_count_eq,size,d0,d1,d2,unit01,unit02]
  exact oneLow_coverage a t low T

theorem actual_twoLow (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 3 ↪ Fin 23)
    (d0 : H.degree (f 0)=6) (d1 : H.degree (f 1)=6) (d2 : H.degree (f 2)=7)
    (cap01 : H.codegree (f 0) (f 1)≤3)
    (unit02 : H.codegree (f 0) (f 2)=1) (unit12 : H.codegree (f 1) (f 2)=1) :
    ∃ c : Case, ∀ T, count H f T=twoLow c T := by
  have low := H.one_le_codegree cover (f.injective.ne (by decide : (0:Fin 3)≠1))
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  rw [unit02] at tb
  let a : Fin 4 := ⟨H.codegree (f 0) (f 1),by omega⟩
  let t : Fin 2 := ⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  refine ⟨⟨2*(a.val-1)+t.val,by have := a.isLt; have := t.isLt; omega⟩,?_⟩
  intro T
  rw [actual_recovered,triple_count_eq,size,d0,d1,d2,unit02,unit12]
  exact twoLow_coverage a t low T
end Aris4Math.ThirtyFour.TwentyThreeFewLowBase
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowBase.actual_oneLow
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowBase.actual_twoLow
