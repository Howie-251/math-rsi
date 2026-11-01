import Aris4Math.ThirtyFour.BoundedAllocations
namespace Aris4Math.ThirtyFour.ActualAllocations
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
variable {n v : ℕ}

def cost (P T : Finset (Fin n)) : ℕ:=if P⊆T then 1 else 0

/-- Actual trace counts in any nonrepeating local type list satisfy every
ordinary containment capacity. -/
theorem budget (H : Simple5Hypergraph (Fin v)) (f : Fin n↪Fin v)
    (entries : List (Finset (Fin n)×ℕ)) (nodup : (entries.map Prod.fst).Nodup)
    (P : Finset (Fin n)) :
    (entries.map (fun e=>count H f e.1*cost P e.1)).sum ≤ upperCount H f P := by
  classical
  have eq : (entries.map (fun e=>count H f e.1*cost P e.1)).sum =
      ∑T∈(entries.map Prod.fst).toFinset, if P⊆T then count H f T else 0 := by
    rw [List.sum_toFinset _ nodup]
    simp only [List.map_map,cost,mul_ite,mul_one,mul_zero,Function.comp_def]
  rw [eq,←Finset.sum_filter]
  calc
    _ ≤ ∑T∈Finset.univ.filter (fun T=>P⊆T),count H f T :=
      Finset.sum_le_sum_of_subset (by
        intro T hT
        exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,(Finset.mem_filter.mp hT).2⟩)
    _ = upperCount H f P := sum_supers H f P

/-- Input membership follows from actual edge counts, not from a retained
candidate list or a successful search run. -/
theorem mem_enumerate {β : Type*} [Fintype β]
    (H : Simple5Hypergraph (Fin v)) (f : Fin n↪Fin v)
    (entries : List (Finset (Fin n)×ℕ)) (nodup : (entries.map Prod.fst).Nodup)
    (P : β→Finset (Fin n)) (cap : β→ℕ)
    (bounds : ∀e∈entries,count H f e.1≤e.2)
    (capacities : ∀j,upperCount H f (P j)≤cap j) :
    entries.map (fun e=>count H f e.1) ∈
      BoundedAllocations.enumerate (fun T j=>cost (P j) T) entries cap := by
  apply BoundedAllocations.mem_enumerate _ entries cap (count H f) bounds
  intro j
  exact (budget H f entries nodup (P j)).trans (capacities j)

theorem count_le_of_pairs (H : Simple5Hypergraph (Fin v)) (f : Fin n↪Fin v)
    (cap : ℕ) (pairs : ∀i j,i≠j→H.codegree (f i) (f j)≤cap)
    (T : Finset (Fin n)) (large : 2≤T.card) : count H f T≤cap := by
  obtain ⟨i,hi,j,hj,ij⟩:=Finset.one_lt_card.mp (by omega : 1<T.card)
  exact (count_le_codegree H f T i j hi hj).trans (pairs i j ij)
end Aris4Math.ThirtyFour.ActualAllocations
#print axioms Aris4Math.ThirtyFour.ActualAllocations.mem_enumerate
