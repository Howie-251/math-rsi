import Aris4Math.ThirtyFour.CachedSparseApplication

/-! The total-count obligation is discharged from the actual table, rather
than recomputed for every degree coloring. -/
namespace Aris4Math.ThirtyFour.CachedActualValidity
open scoped BigOperators
open Aris4Math.TypeCounting

theorem table_count_sum {α : Type*} [DecidableEq α] (E : Finset α)
    (classify : α → List ℕ) (p : Numeric.Profile)
    (table : TableRealization E classify p) :
    (p.types.map Numeric.EdgeType.count).foldl (·+·) 0=E.card := by
  have h := sum_by_table E classify p table (fun _ => (1 : ℚ))
  simp only [Finset.sum_const,Finset.card_eq_sum_ones,nsmul_eq_mul,mul_one,
    qsum_eq_sum] at h
  rw [← List.sum_eq_foldl]
  have cast : ((p.types.map Numeric.EdgeType.count).sum : ℚ)=E.card := by
    simpa only [Nat.cast_list_sum,List.map_map,Function.comp_def] using h.symm
  exact_mod_cast cast

theorem valid_of_table {α : Type*} [DecidableEq α] (E : Finset α)
    (classify : α → List ℕ) (p : Numeric.Profile)
    (table : TableRealization E classify p)
    (positions : p.positions.Nodup ∧ p.positions.Pairwise (·<·) ∧
      p.positions.all (fun k => 1≤k && k≤p.v)=true)
    (types : p.types.all (fun t => t.locks.Nodup && t.locks.Pairwise (·<·) &&
      t.locks.all (·∈p.positions) && t.locks.length≤5 &&
      5-t.locks.length≤Numeric.freeCount p && 0<t.count)=true)
    (centers : p.correctionCenters=[])
    (cap : p.emptyPairCap=none) : Numeric.validProfile p E.card := by
  exact ⟨positions.1,positions.2.1,positions.2.2,table.unique,types,
    table_count_sum E classify p table,by simp [centers],Or.inl cap⟩

end Aris4Math.ThirtyFour.CachedActualValidity
