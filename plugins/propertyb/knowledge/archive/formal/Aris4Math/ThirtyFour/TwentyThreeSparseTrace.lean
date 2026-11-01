import Aris4Math.ThirtyFour.TwentyThreeTraceShape
import Aris4Math.ThirtyFour.LockProjection

/-! Exact sparse weighted traces. Repeated projected keys retain multiplicity.
The finite support, rather than the entire powerset, computes positive moments. -/
namespace Aris4Math.ThirtyFour.TwentyThreeSparseTrace
open scoped BigOperators
open LockProjection
variable {n m : ℕ}
abbrev TraceList (n : ℕ) := List (Finset (Fin n) × ℕ)

def counts : TraceList n → Finset (Fin n) → ℕ
  | [], _ => 0
  | (S,k)::rest, T => (if T=S then k else 0)+counts rest T

def support (xs : TraceList n) : Finset (Finset (Fin n)) :=
  (xs.map Prod.fst).toFinset

theorem counts_zero_of_absent (xs : TraceList n) (T : Finset (Fin n))
    (absent : T∉support xs) : counts xs T=0 := by
  induction xs with
  | nil => rfl
  | cons e rest ih =>
    have ne : T≠e.1 := by simpa [support] using (fun h => absent (by simp [support,h]))
    have absent' : T∉support rest := by
      intro h;exact absent (by simp only [support,List.map_cons,List.toFinset_cons,Finset.mem_insert];exact Or.inr h)
    simp only [counts,if_neg ne,zero_add,ih absent']

def projected (g : Fin m ↪ Fin n) (xs : TraceList n) : TraceList m :=
  xs.map (fun e => (project g e.1,e.2))

theorem projected_counts (g : Fin m ↪ Fin n) (xs : TraceList n)
    (T : Finset (Fin m)) :
    counts (projected g xs) T =
      ∑ U : Finset (Fin n), if project g U=T then counts xs U else 0 := by
  induction xs with
  | nil => simp [projected,counts]
  | cons e rest ih =>
    change (if T=project g e.1 then e.2 else 0)+counts (projected g rest) T =
      ∑ U : Finset (Fin n), if project g U=T then
        ((if U=e.1 then e.2 else 0)+counts rest U) else 0
    have split : (∑ U : Finset (Fin n), if project g U=T then
        ((if U=e.1 then e.2 else 0)+counts rest U) else 0) =
        (∑ U : Finset (Fin n), if project g U=T then (if U=e.1 then e.2 else 0) else 0)+
        (∑ U : Finset (Fin n), if project g U=T then counts rest U else 0) := by
      rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro U _
      by_cases h : project g U=T <;> simp [h]
    rw [split,←ih]
    congr 1
    symm
    calc
      _ = (if project g e.1=T then e.2 else 0) := by
        rw [Finset.sum_eq_single e.1]
        · simp
        · intro U _ ne
          by_cases h : project g U=T <;> simp [h,ne]
        · simp
      _ = _ := by simp [eq_comm]

def moment (xs : TraceList n) (k p : ℕ) : ℕ :=
  ∑ T ∈ (support xs).filter (fun T => T.card=k), counts xs T ^ (p+1)

theorem moment_eq (xs : TraceList n) (k p : ℕ) :
    moment xs k p = TwentyThreeTraceShape.cardMoment (counts xs) k (p+1) := by
  unfold moment TwentyThreeTraceShape.cardMoment
  simp only [Finset.sum_filter]
  apply Finset.sum_subset (Finset.subset_univ _)
  intro T _ absent
  rw [counts_zero_of_absent xs T absent]
  simp

theorem moment_zero_eq_cardMass (xs : TraceList n) (k : ℕ) :
    moment xs k 0 = TwentyThreeTraceShape.cardMass (counts xs) k := by
  rw [moment_eq]
  simp only [TwentyThreeTraceShape.cardMoment,TwentyThreeTraceShape.cardMass,
    Nat.zero_add,pow_one]

end Aris4Math.ThirtyFour.TwentyThreeSparseTrace
#print axioms Aris4Math.ThirtyFour.TwentyThreeSparseTrace.projected_counts
#print axioms Aris4Math.ThirtyFour.TwentyThreeSparseTrace.moment_eq
