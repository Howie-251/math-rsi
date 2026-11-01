import Aris4Math.ThirtyFour.TwentyOneFiveClassData
import Aris4Math.ThirtyFour.TwentyOneFiveQuad

namespace Aris4Math.ThirtyFour.TwentyOneFiveClassification
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)

theorem residual_of_not_propertyB (H : Simple5Hypergraph (Fin 21))
    (size : H.edges.card=34) (noB : ¬ PropertyB H) (f : Fin 4 ↪ Fin 21) (kind : Kind)
    (hd : ∀ j, H.degree (f j)=degrees kind j)
    (unit : ∀ j : Fin 3, H.codegree (f 0) (f j.succ)=1)
    (hc : ∀ j, H.codegree (f (first j)) (f (second j)) ≤ 2)
    (cover : H.PairCovering)
    (assumptions : Assumptions kind
      (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j))) :
    Residue kind (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  have lo (j : Fin 6) : 1 ≤ H.codegree (f (first j)) (f (second j)) :=
    H.one_le_codegree cover (f.injective.ne (by fin_cases j <;> decide))
  let a : Fin 2 := ⟨H.codegree (f 1) (f 2)-1,by have h := hc 3; change H.codegree (f 1) (f 2) ≤ 2 at h; omega⟩
  let b : Fin 2 := ⟨H.codegree (f 1) (f 3)-1,by have h := hc 4; change H.codegree (f 1) (f 3) ≤ 2 at h; omega⟩
  let c : Fin 2 := ⟨H.codegree (f 2) (f 3)-1,by have h := hc 5; change H.codegree (f 2) (f 3) ≤ 2 at h; omega⟩
  have coeq (j) : co (a.val+1) (b.val+1) (c.val+1) j =
      H.codegree (f (first j)) (f (second j)) := by
    have u0 := unit 0; have u1 := unit 1; have u2 := unit 2
    have l3 := lo 3; have l4 := lo 4; have l5 := lo 5
    fin_cases j <;> simp [co,a,b,c,first,second] at * <;> omega
  have cofun := funext coeq
  have bounded := high_le_two H f hc
  let h : Fin 5 → Fin 3 := fun j => ⟨count H f (highLabels j),by have := bounded j; omega⟩
  have ass : Assumptions kind (co (a.val+1) (b.val+1) (c.val+1)) (fun j => (h j).val) := by
    simpa only [cofun] using assumptions
  have inv : ∀ j, highPairSum (fun z => (h z).val) j ≤ co (a.val+1) (b.val+1) (c.val+1) j := by
    intro j; rw [coeq]; exact high_inventory H f j
  rcases coverage kind a b c h ass inv with residue | ⟨i,deq,ceq,heq⟩
  · simpa only [cofun] using residue
  · exact False.elim (noB (TwentyOneFiveQuad.propertyB_of_data H size f i
      (fun j => (hd j).trans (deq j)) (fun j => (coeq j).symm.trans (ceq j)) heq))
end Aris4Math.ThirtyFour.TwentyOneFiveClassification
