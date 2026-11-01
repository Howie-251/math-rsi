import Aris4Math.ThirtyFour.LocalProfiles
import Mathlib.Tactic.Ring.Basic

/-! Exact compression of uncorrected A/B/C rows by residual edge size.
Quota penalties are intentionally left at their existing type-pair interface. -/
namespace Aris4Math.ThirtyFour.CachedRows
open scoped BigOperators
open Aris4Math.TypeCounting
open Numeric

def residual (t : EdgeType) : Fin 6 := ⟨5-t.locks.length, by omega⟩

def compatible (p : Profile) (t : EdgeType) (k : ℕ) (last : Bool) : Prop :=
  if k ∈ p.positions then
    k ∈ t.locks ∧ (t.locks.filter (· != k)).all (fun j => if last then j < k else k < j)
  else
    1 ≤ (residual t).val ∧ t.locks.all (fun j => if last then j < k else k < j)
instance (p : Profile) (t : EdgeType) (k : ℕ) (last : Bool) :
    Decidable (compatible p t k last) := by unfold compatible; infer_instance

/-- The geometric input contains only free counts, side counts and pivot status. -/
def edgeCoeff (N a : ℕ) (locked : Bool) (r : Fin 6) : ℚ :=
  if locked then (binom a r.val : ℚ) / binom N r.val
  else ((r.val * binom a (r.val-1) : ℕ) : ℚ) /
    (N * binom (N-1) (r.val-1) : ℕ)

def pairCoeff (N a b : ℕ) (locked : Bool) (r q : Fin 6) : ℚ :=
  if locked then
    if r.val+q.val ≤ N then
      ((binom a r.val * binom b q.val : ℕ) : ℚ) /
        (binom N r.val * binom (N-r.val) q.val : ℕ)
    else 0
  else
    if r.val+q.val-1 ≤ N then
      ((binom a (r.val-1) * binom b (q.val-1) : ℕ) : ℚ) /
        (N * binom (N-1) (r.val-1) * binom (N-r.val) (q.val-1) : ℕ)
    else 0

def aCoeff (p : Profile) (k : ℕ) (last : Bool) : Fin 6 → ℚ :=
  edgeCoeff (freeCount p) (if last then leftCount p k else rightCount p k)
    (decide (k ∈ p.positions))
def cCoeff (p : Profile) (k : ℕ) : Fin 6 → Fin 6 → ℚ :=
  pairCoeff (freeCount p) (leftCount p k) (rightCount p k)
    (decide (k ∈ p.positions))

theorem edgeWeight_factor (p : Profile) (t : EdgeType) (k : ℕ) (last : Bool) :
    edgeWeight p t k last = if compatible p t k last then aCoeff p k last (residual t) else 0 := by
  cases last <;> by_cases h : k ∈ p.positions <;>
    simp [edgeWeight, compatible, aCoeff, edgeCoeff, residual, h]

private theorem locked_pair_iff (t u : List ℕ) (k : ℕ) (hn : t.Nodup) :
    (t.filter (· ∈ u) = [k] ∧
      (t.filter (· != k)).all (· < k) ∧ (u.filter (· != k)).all (k < ·)) ↔
    ((k ∈ t ∧ (t.filter (· != k)).all (· < k)) ∧
      (k ∈ u ∧ (u.filter (· != k)).all (k < ·))) := by
  constructor
  · rintro ⟨inter, left, right⟩
    have h : k ∈ t.filter (· ∈ u) := by rw [inter]; simp
    have hku := List.mem_filter.mp h
    exact ⟨⟨hku.1,left⟩,⟨of_decide_eq_true hku.2,right⟩⟩
  · rintro ⟨⟨kt,left⟩,⟨ku,right⟩⟩
    refine ⟨?_,left,right⟩
    apply List.Perm.eq_singleton
    apply (List.perm_ext_iff_of_nodup (hn.filter _) (List.nodup_singleton _)).mpr
    intro x
    simp only [List.mem_filter, decide_eq_true_eq, List.mem_singleton]
    constructor
    · rintro ⟨xt,xu⟩
      by_contra ne
      have l : x < k := of_decide_eq_true (List.all_eq_true.mp left x (by simp [xt,ne]))
      have r : k < x := of_decide_eq_true (List.all_eq_true.mp right x (by simp [xu,ne]))
      omega
    · rintro rfl; exact ⟨kt,ku⟩

private theorem free_disjoint (t u : List ℕ) (k : ℕ)
    (left : t.all (· < k)) (right : u.all (k < ·)) : t.all (· ∉ u) := by
  apply List.all_eq_true.mpr
  intro x hx
  apply decide_eq_true
  intro hu
  have l := of_decide_eq_true (List.all_eq_true.mp left x hx)
  have r := of_decide_eq_true (List.all_eq_true.mp right x hu)
  omega

theorem pairWeight_factor (p : Profile) (t u : EdgeType) (k : ℕ)
    (hn : t.locks.Nodup) :
    pairWeight p t u k =
      if compatible p t k true ∧ compatible p u k false
      then cCoeff p k (residual t) (residual u) else 0 := by
  by_cases locked : k ∈ p.positions
  · simp only [pairWeight, compatible, cCoeff, pairCoeff, residual, locked,
      decide_true, Bool.false_eq_true, ↓reduceIte]
    have eq := locked_pair_iff t.locks u.locks k hn
    split_ifs <;> first | rfl | (exfalso; tauto)
  · simp only [pairWeight, compatible, cCoeff, pairCoeff, residual, locked,
      decide_false, Bool.false_eq_true, ↓reduceIte]
    have disj := free_disjoint t.locks u.locks k
    split_ifs <;> first | rfl | (exfalso; tauto)

/-- Six exact multiplicity buckets; the two sides use the same type table. -/
def mass (p : Profile) (k : ℕ) (last : Bool) (r : Fin 6) : ℚ :=
  ∑ t ∈ p.types.toFinset,
    if residual t = r ∧ compatible p t k last then (t.count : ℚ) else 0

def cachedA (p : Profile) (k : ℕ) (last : Bool) : ℚ :=
  ∑ r : Fin 6, mass p k last r * aCoeff p k last r

def cachedDiagonal (p : Profile) (k : ℕ) : ℚ :=
  ∑ t ∈ p.types.toFinset,
    if compatible p t k true ∧ compatible p t k false
    then (t.count : ℚ) * cCoeff p k (residual t) (residual t) else 0

def cachedC (p : Profile) (k : ℕ) : ℚ :=
  (∑ r : Fin 6, ∑ q : Fin 6, mass p k true r * mass p k false q * cCoeff p k r q)
    - cachedDiagonal p k

private theorem weighted_group {α : Type*} [DecidableEq α]
    (S : Finset α) (g : α → Fin 6) (w : α → ℚ) (C : Fin 6 → ℚ) :
    (∑ t ∈ S, w t * C (g t)) =
      ∑ r : Fin 6, (∑ t ∈ S, if g t = r then w t else 0) * C r := by
  simp_rw [Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  simp only [ite_mul, zero_mul]
  simp

private theorem weighted_group₂ {α : Type*} [DecidableEq α]
    (S : Finset α) (g : α → Fin 6) (w z : α → ℚ) (C : Fin 6 → Fin 6 → ℚ) :
    (∑ t ∈ S, ∑ u ∈ S, w t * z u * C (g t) (g u)) =
      ∑ r : Fin 6, ∑ q : Fin 6,
        (∑ t ∈ S, if g t = r then w t else 0) *
        (∑ u ∈ S, if g u = q then z u else 0) * C r q := by
  simp_rw [mul_assoc, ← Finset.mul_sum]
  rw [weighted_group S g w (fun r => ∑ u ∈ S, z u * C r (g u))]
  apply Finset.sum_congr rfl
  intro r hr
  rw [weighted_group S g z (C r)]

private theorem pairCount_cast (p : Profile) (nocap : p.emptyPairCap = none)
    (unique : (p.types.map EdgeType.locks).Nodup)
    (t u : EdgeType) (ht : t ∈ p.types) (hu : u ∈ p.types) :
    (pairCount p t u : ℚ) = (t.count : ℚ)*(u.count : ℚ) -
      if t=u then (t.count : ℚ) else 0 := by
  have eq : t.locks=u.locks ↔ t=u :=
    ⟨List.inj_on_of_nodup_map unique ht hu, fun h => congrArg EdgeType.locks h⟩
  simp only [pairCount,nocap,Option.getD_none,ite_self,eq]
  by_cases h : t=u
  · subst u
    cases hcount : t.count with
    | zero => simp
    | succ n => simp; ring1
  · simp [h]

private theorem types_nodup (p : Profile) (unique : (p.types.map EdgeType.locks).Nodup) :
    p.types.Nodup := List.Nodup.of_map _ unique

theorem boundAB_eq (p : Profile) (k : ℕ)
    (unique : (p.types.map EdgeType.locks).Nodup) (last : Bool) :
    (if last then boundA p k else boundB p k) = cachedA p k last := by
  have start : (if last then boundA p k else boundB p k) =
      ∑ t ∈ p.types.toFinset, (t.count : ℚ)*edgeWeight p t k last := by
    cases last <;> simp only [Bool.false_eq_true, ↓reduceIte, boundA,boundB,qsum_eq_sum]
    all_goals exact (List.sum_toFinset _ (types_nodup p unique)).symm
  rw [start]
  simp_rw [edgeWeight_factor]
  calc
    _ = ∑ t ∈ p.types.toFinset,
      (if compatible p t k last then (t.count : ℚ) else 0) * aCoeff p k last (residual t) := by
      apply Finset.sum_congr rfl
      intro t ht
      split_ifs <;> simp
    _ = _ := by
      rw [weighted_group]
      simp only [cachedA,mass,ite_and]

private theorem subtract_diagonal {α : Type*} [DecidableEq α] (S : Finset α)
    (w : α → ℚ) (F : α → α → ℚ) :
    (∑ t ∈ S, ∑ u ∈ S, (w t*w u - if t=u then w t else 0)*F t u) =
      (∑ t ∈ S, ∑ u ∈ S, w t*w u*F t u) - ∑ t ∈ S, w t*F t t := by
  simp_rw [sub_mul,Finset.sum_sub_distrib]
  congr 1
  apply Finset.sum_congr rfl
  intro t ht
  simp only [ite_mul,zero_mul]
  simp [ht]

private theorem sum_flatMap_map {α β : Type*} (xs : List α) (ys : List β)
    (f : α → β → ℚ) :
    (xs.flatMap fun t => ys.map (f t)).sum =
      (xs.map fun t => (ys.map (f t)).sum).sum := by
  induction xs with
  | nil => simp
  | cons a xs ih => simp only [List.flatMap_cons,List.sum_append,List.map_cons,List.sum_cons,ih]

theorem boundC_eq (p : Profile) (k : ℕ)
    (unique : (p.types.map EdgeType.locks).Nodup)
    (nodup : ∀ t ∈ p.types, t.locks.Nodup) (nocap : p.emptyPairCap=none) :
    boundC p k = cachedC p k := by
  have start : boundC p k = ∑ t ∈ p.types.toFinset, ∑ u ∈ p.types.toFinset,
      (pairCount p t u : ℚ)*pairWeight p t u k := by
    rw [boundC,qsum_eq_sum,sum_flatMap_map]
    simp_rw [← List.sum_toFinset _ (types_nodup p unique)]
  rw [start]
  calc
    _ = ∑ t ∈ p.types.toFinset, ∑ u ∈ p.types.toFinset,
        ((t.count : ℚ)*(u.count : ℚ) - if t=u then (t.count : ℚ) else 0)*pairWeight p t u k := by
      apply Finset.sum_congr rfl
      intro t ht
      apply Finset.sum_congr rfl
      intro u hu
      rw [pairCount_cast p nocap unique t u (List.mem_toFinset.mp ht) (List.mem_toFinset.mp hu)]
    _ = (∑ t ∈ p.types.toFinset, ∑ u ∈ p.types.toFinset,
        (t.count : ℚ)*(u.count : ℚ)*pairWeight p t u k) -
        ∑ t ∈ p.types.toFinset, (t.count : ℚ)*pairWeight p t t k :=
      subtract_diagonal _ _ _
    _ = cachedC p k := by
      unfold cachedC
      congr 1
      · calc
          _ = ∑ t ∈ p.types.toFinset, ∑ u ∈ p.types.toFinset,
              (if compatible p t k true then (t.count : ℚ) else 0)*
              (if compatible p u k false then (u.count : ℚ) else 0)*
              cCoeff p k (residual t) (residual u) := by
            apply Finset.sum_congr rfl
            intro t ht
            apply Finset.sum_congr rfl
            intro u hu
            rw [pairWeight_factor p t u k (nodup t (List.mem_toFinset.mp ht))]
            split_ifs <;> simp_all
          _ = _ := by
            rw [weighted_group₂]
            simp only [mass,ite_and]
      · unfold cachedDiagonal
        apply Finset.sum_congr rfl
        intro t ht
        rw [pairWeight_factor p t t k (nodup t (List.mem_toFinset.mp ht))]
        split_ifs <;> simp

/-- All three rows are connected to the existing actual-event interface. -/
theorem rows_eq (p : Profile) (m k : ℕ) (valid : validProfile p m)
    (nocap : p.emptyPairCap=none) :
    boundA p k = cachedA p k true ∧ boundB p k = cachedA p k false ∧
      boundC p k = cachedC p k := by
  refine ⟨boundAB_eq p k valid.2.2.2.1 true,
    boundAB_eq p k valid.2.2.2.1 false, boundC_eq p k valid.2.2.2.1 ?_ nocap⟩
  intro t ht
  have h := List.all_eq_true.mp valid.2.2.2.2.1 t ht
  simp only [Bool.and_eq_true,decide_eq_true_eq] at h
  exact h.1.1.1.1.1

/-- The only trace eligible on both sides is the pivot trace. -/
def pivotTrace (p : Profile) (k : ℕ) : List ℕ := if k ∈ p.positions then [k] else []

theorem diagonal_compatible_iff (p : Profile) (t : EdgeType) (k : ℕ)
    (hn : t.locks.Nodup) :
    (compatible p t k true ∧ compatible p t k false) ↔ t.locks=pivotTrace p k := by
  by_cases hk : k ∈ p.positions
  · simp only [compatible,pivotTrace,hk,↓reduceIte,Bool.false_eq_true]
    constructor
    · rintro ⟨⟨kt,l⟩,⟨_,r⟩⟩
      apply List.Perm.eq_singleton
      apply (List.perm_ext_iff_of_nodup hn (List.nodup_singleton _)).mpr
      intro x
      simp only [List.mem_singleton]
      constructor
      · intro hx
        by_contra ne
        have left := of_decide_eq_true (List.all_eq_true.mp l x (by simp [hx,ne]))
        have right := of_decide_eq_true (List.all_eq_true.mp r x (by simp [hx,ne]))
        omega
      · rintro rfl; exact kt
    · intro ht; simp [ht]
  · simp only [compatible,pivotTrace,hk,↓reduceIte,Bool.false_eq_true]
    constructor
    · rintro ⟨⟨_,l⟩,⟨_,r⟩⟩
      apply List.eq_nil_iff_forall_not_mem.mpr
      intro x hx
      have left := of_decide_eq_true (List.all_eq_true.mp l x hx)
      have right := of_decide_eq_true (List.all_eq_true.mp r x hx)
      omega
    · intro ht; simp [ht,residual]

/-- Zero-count pruning and ordered-pair diagonal subtraction are both exact. -/
theorem cachedDiagonal_eq (p : Profile) (k : ℕ)
    (nodup : ∀ t ∈ p.types, t.locks.Nodup) :
    cachedDiagonal p k =
      (∑ t ∈ p.types.toFinset, if t.locks=pivotTrace p k then (t.count : ℚ) else 0)*
      cCoeff p k (residual ⟨pivotTrace p k,0⟩) (residual ⟨pivotTrace p k,0⟩) := by
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro t ht
  simp only [diagonal_compatible_iff p t k (nodup t (List.mem_toFinset.mp ht))]
  by_cases eq : t.locks=pivotTrace p k
  · simp [eq,residual]
  · simp [eq]

def cachedTotal (p : Profile) : ℚ :=
  ∑ k : Fin p.v, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))

theorem propertyB_of_cached (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v) (p : Profile) (m : ℕ)
    (real : RealizesProfile H vertices positions p m) (nocap : p.emptyPairCap=none)
    (strict : (∑ k : Fin v, min (cachedA p (k.val+1) true)
      (min (cachedA p (k.val+1) false) (cachedC p (k.val+1))))<1) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H vertices positions
    (fun k => cachedA p (k.val+1) true) (fun k => cachedA p (k.val+1) false)
    (fun k => cachedC p (k.val+1))
  · intro k
    rw [← (rows_eq p m (k.val+1) real.valid nocap).1]
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions p real k true)
  · intro k
    rw [← (rows_eq p m (k.val+1) real.valid nocap).2.1]
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions p real k false)
  · intro k
    rw [← (rows_eq p m (k.val+1) real.valid nocap).2.2]
    exact ProfileApplication.critical_sum_le H vertices positions p real nocap k
  · exact strict

/-- An actual-hypergraph entry: all realization data are constructed from the
complete trace labels and their actual counts. -/
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup) (all : ∀ T,T∈labels)
    (μ : Finset (Fin n) → ℕ)
    (counts : ∀ T,ThirtyThree.MultiLockRecovery.count H vertices T=μ T)
    (valid : validProfile (ThirtyThree.MultiLockRecovery.profile labels positions μ []) m)
    (strict : (∑ k : Fin v,
      min (cachedA (ThirtyThree.MultiLockRecovery.profile labels positions μ []) (k.val+1) true)
      (min (cachedA (ThirtyThree.MultiLockRecovery.profile labels positions μ []) (k.val+1) false)
        (cachedC (ThirtyThree.MultiLockRecovery.profile labels positions μ []) (k.val+1))))<1) : PropertyB H := by
  exact propertyB_of_cached H vertices positions _ m
    (LocalProfiles.realizes H vertices positions labels nodup all μ counts [] valid) rfl strict

end Aris4Math.ThirtyFour.CachedRows

#print axioms Aris4Math.ThirtyFour.CachedRows.rows_eq
#print axioms Aris4Math.ThirtyFour.CachedRows.cachedDiagonal_eq
#print axioms Aris4Math.ThirtyFour.CachedRows.propertyB_of_counts



/-! Sparse profiles cover all actual edges through positive actual multiplicities.
A complete powerset listing is unnecessary. -/
namespace Aris4Math.ThirtyFour.CachedSparseApplication
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

/-- Every actual edge has positive multiplicity at its own trace. -/
theorem self_count_pos (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (e : Finset (Fin v)) (he : e ∈ H.edges) :
    0 < count H vertices (lockSignature vertices e) := by
  unfold count multiplicity fiber
  apply Finset.card_pos.mpr
  exact ⟨e, by simp [he]⟩

/-- The support condition replaces complete powerset enumeration. It is not an
extra condition on H: finite certificate data discharge it at every caller. -/
theorem realizes_sparse (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup)
    (μ : Finset (Fin n) → ℕ) (support : ∀ T, μ T ≠ 0 → T ∈ labels)
    (counts : ∀ T,count H vertices T=μ T)
    (centers : List ℕ) (valid : Numeric.validProfile (rawProfile labels positions μ centers) m) :
    RealizesProfile H vertices positions (rawProfile labels positions μ centers) m := by
  refine ⟨rfl, valid, ?_, ?_⟩
  · simp [rawProfile,canonicalType]
  · constructor
    · simpa only [rawProfile,List.map_map,Function.comp_def] using
        nodup.map (canonicalType_injective positions)
    · intro e he
      have hc : μ (lockSignature vertices e) ≠ 0 := by
        rw [← counts]; exact ne_of_gt (self_count_pos H vertices e he)
      have hs := support _ hc
      change canonicalType positions (lockSignature vertices e) ∈
        (labels.map fun T => (⟨canonicalType positions T,μ T⟩ : Numeric.EdgeType)).map Numeric.EdgeType.locks
      simp only [List.map_map,List.mem_map]
      exact ⟨_,hs,rfl⟩
    · intro t ht
      obtain ⟨T,_,rfl⟩ := List.mem_map.mp ht
      exact (position_fiber_count H vertices positions T).trans (counts T)

theorem propertyB_of_sparse_counts (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup)
    (μ : Finset (Fin n) → ℕ) (support : ∀ T, μ T ≠ 0 → T ∈ labels)
    (counts : ∀ T,count H vertices T=μ T)
    (valid : Numeric.validProfile (rawProfile labels positions μ []) m)
    (strict : (∑ k : Fin v,
      min (CachedRows.cachedA (rawProfile labels positions μ []) (k.val+1) true)
      (min (CachedRows.cachedA (rawProfile labels positions μ []) (k.val+1) false)
        (CachedRows.cachedC (rawProfile labels positions μ []) (k.val+1))))<1) : PropertyB H := by
  exact CachedRows.propertyB_of_cached H vertices positions _ m
    (realizes_sparse H vertices positions labels nodup μ support counts [] valid) rfl strict
end Aris4Math.ThirtyFour.CachedSparseApplication
#print axioms Aris4Math.ThirtyFour.CachedSparseApplication.propertyB_of_sparse_counts

namespace Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
/- Saved q=5 bare witness 4423, with the smallest successful margin in that
bare batch. This theorem closes this actual trace input, not all 25-point H. -/
def positions : Fin 9 ↪ Fin 25 :=
  ⟨fun j => ⟨j.val+8,by omega⟩, fun i j h => Fin.ext (by
    have := congrArg Fin.val h; simp only at this; omega)⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,4},{2,4},{3,4},{5},{0,1,2,3,5},{6},{0,6},{3,6},{5,6},{7},{0,7},{2,7},{5,7},{1,4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then ( if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={0,1,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={1,4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile :=
  ⟨25,executableType positions Finset.univ,
    labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[9],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[9,10,11,12,14],1⟩,⟨[15],2⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[9,16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[9,17],1⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,17],1⟩,⟨[12,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel

theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (12869/12870 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (vertices : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H vertices T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H vertices positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot
#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot.propertyB_of_counts
