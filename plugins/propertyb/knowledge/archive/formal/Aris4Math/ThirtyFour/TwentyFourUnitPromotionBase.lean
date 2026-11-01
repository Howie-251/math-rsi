import Aris4Math.ThirtyFour.PromotionReconstruction
namespace Aris4Math.ThirtyFour.TwentyFourUnitPromotionBase
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog
variable {n v : ℕ}

/-- Exact low-new codegrees can be tested on the decoded nonempty inventory;
the omitted empty promotion contributes zero at every old label. -/
theorem decoded_codegree (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1)↪Fin v) (entries : List (Finset (Fin n)×ℕ))
    (support : ∀T,T≠∅→T∉entries.map Prod.fst→promotion H f T=0) (i : Fin n) :
    (∑T : Finset (Fin n),if i∈T then
      BoundedAllocations.decode entries (entries.map (fun e=>promotion H f e.1)) T else 0)=
      H.codegree (f i.castSucc) (f (Fin.last n)) := by
  rw [←sum_promotion_codegree H f i]
  apply Finset.sum_congr rfl
  intro T _
  by_cases inside : i∈T
  · rw [if_pos inside,if_pos inside,decode_nonempty H f entries support T]
    exact Finset.ne_empty_of_mem inside
  · rw [if_neg inside,if_neg inside]

/-- Unit old-new pairs cap every nonempty actual promotion by one. -/
theorem promotion_le_one (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1)↪Fin v)
    (unit : ∀i : Fin n,H.codegree (f i.castSucc) (f (Fin.last n))=1)
    (T : Finset (Fin n)) (nonempty : T.Nonempty) : promotion H f T≤1 := by
  obtain ⟨i,inside⟩ := nonempty
  have bound := count_le_codegree H f (promoted T) i.castSucc (Fin.last n)
    ((castSucc_mem_promoted T i).mpr inside) (Finset.mem_insert_self _ _)
  simpa only [unit] using bound
end Aris4Math.ThirtyFour.TwentyFourUnitPromotionBase
