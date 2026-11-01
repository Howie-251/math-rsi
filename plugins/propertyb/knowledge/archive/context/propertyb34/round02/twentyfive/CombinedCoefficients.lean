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


/-! Common coefficients for all nine-lock 25-point profiles. The unused free
geometry a=16 is retained to keep the indexing uniform. B uses the same endpoint
table at the right count. These tables contain no trace multiplicities. -/
namespace Aris4Math.ThirtyFour.CachedCoefficients16
open CachedRows
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def index (locked : Bool) (a : Fin 17) : Fin 34 :=
  ⟨(if locked then 17 else 0)+a.val, by split_ifs <;> omega⟩
def edgeTable : Fin 34 → Fin 6 → ℚ := ![![(0/1),(1/16),(0/1),(0/1),(0/1),(0/1)],![(0/1),(1/16),(1/120),(0/1),(0/1),(0/1)],![(0/1),(1/16),(1/60),(1/560),(0/1),(0/1)],![(0/1),(1/16),(1/40),(3/560),(1/1820),(0/1)],![(0/1),(1/16),(1/30),(3/280),(1/455),(1/4368)],![(0/1),(1/16),(1/24),(1/56),(1/182),(5/4368)],![(0/1),(1/16),(1/20),(3/112),(1/91),(5/1456)],![(0/1),(1/16),(7/120),(3/80),(1/52),(5/624)],![(0/1),(1/16),(1/15),(1/20),(2/65),(5/312)],![(0/1),(1/16),(3/40),(9/140),(3/65),(3/104)],![(0/1),(1/16),(1/12),(9/112),(6/91),(5/104)],![(0/1),(1/16),(11/120),(11/112),(33/364),(55/728)],![(0/1),(1/16),(1/10),(33/280),(11/91),(165/1456)],![(0/1),(1/16),(13/120),(39/280),(11/70),(55/336)],![(0/1),(1/16),(7/60),(13/80),(1/5),(11/48)],![(0/1),(1/16),(1/8),(3/16),(1/4),(5/16)],![(0/1),(1/16),(2/15),(3/14),(4/13),(5/12)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/1),(1/8),(1/120),(0/1),(0/1),(0/1)],![(1/1),(3/16),(1/40),(1/560),(0/1),(0/1)],![(1/1),(1/4),(1/20),(1/140),(1/1820),(0/1)],![(1/1),(5/16),(1/12),(1/56),(1/364),(1/4368)],![(1/1),(3/8),(1/8),(1/28),(3/364),(1/728)],![(1/1),(7/16),(7/40),(1/16),(1/52),(1/208)],![(1/1),(1/2),(7/30),(1/10),(1/26),(1/78)],![(1/1),(9/16),(3/10),(3/20),(9/130),(3/104)],![(1/1),(5/8),(3/8),(3/14),(3/26),(3/52)],![(1/1),(11/16),(11/24),(33/112),(33/182),(11/104)],![(1/1),(3/4),(11/20),(11/28),(99/364),(33/182)],![(1/1),(13/16),(13/20),(143/280),(11/28),(33/112)],![(1/1),(7/8),(91/120),(13/20),(11/20),(11/24)],![(1/1),(15/16),(7/8),(13/16),(3/4),(11/16)],![(1/1),(1/1),(1/1),(1/1),(1/1),(1/1)]]
def pairTable : Fin 34 → Fin 6 → Fin 6 → ℚ := ![![![(1/16),(1/16),(15/256),(7/128),(13/256),(3/64)],![(1/16),(1/16),(1/16),(1/16),(1/16),(1/16)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(7/128),(91/1920),(13/320),(11/320)],![(1/16),(1/16),(7/120),(13/240),(1/20),(11/240)],![(1/240),(1/240),(1/240),(1/240),(1/240),(1/240)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(13/256),(13/320),(143/4480),(11/448)],![(1/16),(1/16),(13/240),(13/280),(11/280),(11/336)],![(1/120),(1/120),(13/1680),(1/140),(11/1680),(1/168)],![(1/1680),(1/1680),(1/1680),(1/1680),(1/1680),(1/1680)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(3/64),(11/320),(11/448),(99/5824)],![(1/16),(1/16),(1/20),(11/280),(11/364),(33/1456)],![(1/80),(1/80),(3/280),(33/3640),(11/1456),(9/1456)],![(1/560),(1/560),(3/1820),(11/7280),(1/728),(9/7280)],![(1/7280),(1/7280),(1/7280),(1/7280),(1/7280),(1/7280)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(11/256),(11/384),(33/1792),(33/2912)],![(1/16),(1/16),(11/240),(11/336),(33/1456),(11/728)],![(1/60),(1/60),(11/840),(11/1092),(11/1456),(1/182)],![(1/280),(1/280),(11/3640),(11/4368),(3/1456),(3/1820)],![(1/1820),(1/1820),(11/21840),(1/2184),(3/7280),(1/2730)],![(1/21840),(1/21840),(1/21840),(1/21840),(1/21840),(1/21840)]],![![(1/16),(1/16),(5/128),(3/128),(3/224),(3/416)],![(1/16),(1/16),(1/24),(3/112),(3/182),(1/104)],![(1/48),(1/48),(5/336),(15/1456),(5/728),(5/1144)],![(1/168),(1/168),(5/1092),(5/1456),(5/2002),(1/572)],![(1/728),(1/728),(5/4368),(15/16016),(3/4004),(1/1716)],![(1/4368),(1/4368),(5/24024),(3/16016),(1/6006),(1/6864)]],![![(1/16),(1/16),(9/256),(3/160),(3/320),(9/2080)],![(1/16),(1/16),(3/80),(3/140),(3/260),(3/520)],![(1/40),(1/40),(9/560),(9/910),(3/520),(9/2860)],![(1/112),(1/112),(9/1456),(3/728),(3/1144),(9/5720)],![(1/364),(1/364),(3/1456),(3/2002),(3/2860),(1/1430)],![(1/1456),(1/1456),(9/16016),(9/20020),(1/2860),(3/11440)]],![![(1/16),(1/16),(1/32),(7/480),(1/160),(1/416)],![(1/16),(1/16),(1/30),(1/60),(1/130),(1/312)],![(7/240),(7/240),(1/60),(7/780),(7/1560),(7/3432)],![(1/80),(1/80),(1/130),(7/1560),(7/2860),(7/5720)],![(1/208),(1/208),(1/312),(7/3432),(7/5720),(7/10296)],![(1/624),(1/624),(1/858),(7/8580),(7/12870),(7/20592)]],![![(1/16),(1/16),(7/256),(7/640),(1/256),(1/832)],![(1/16),(1/16),(7/240),(1/80),(1/208),(1/624)],![(1/30),(1/30),(1/60),(1/130),(1/312),(1/858)],![(1/60),(1/60),(7/780),(7/1560),(7/3432),(7/8580)],![(1/130),(1/130),(7/1560),(7/2860),(7/5720),(7/12870)],![(1/312),(1/312),(7/3432),(7/5720),(7/10296),(7/20592)]],![![(1/16),(1/16),(3/128),(1/128),(1/448),(3/5824)],![(1/16),(1/16),(1/40),(1/112),(1/364),(1/1456)],![(3/80),(3/80),(9/560),(9/1456),(3/1456),(9/16016)],![(3/140),(3/140),(9/910),(3/728),(3/2002),(9/20020)],![(3/260),(3/260),(3/520),(3/1144),(3/2860),(1/2860)],![(3/520),(3/520),(9/2860),(9/5720),(1/1430),(3/11440)]],![![(1/16),(1/16),(5/256),(1/192),(1/896),(1/5824)],![(1/16),(1/16),(1/48),(1/168),(1/728),(1/4368)],![(1/24),(1/24),(5/336),(5/1092),(5/4368),(5/24024)],![(3/112),(3/112),(15/1456),(5/1456),(15/16016),(3/16016)],![(3/182),(3/182),(5/728),(5/2002),(3/4004),(1/6006)],![(1/104),(1/104),(5/1144),(1/572),(1/1716),(1/6864)]],![![(1/16),(1/16),(1/64),(1/320),(1/2240),(1/29120)],![(1/16),(1/16),(1/60),(1/280),(1/1820),(1/21840)],![(11/240),(11/240),(11/840),(11/3640),(11/21840),(1/21840)],![(11/336),(11/336),(11/1092),(11/4368),(1/2184),(1/21840)],![(33/1456),(33/1456),(11/1456),(3/1456),(3/7280),(1/21840)],![(11/728),(11/728),(1/182),(3/1820),(1/2730),(1/21840)]],![![(1/16),(1/16),(3/256),(1/640),(1/8960),(0/1)],![(1/16),(1/16),(1/80),(1/560),(1/7280),(0/1)],![(1/20),(1/20),(3/280),(3/1820),(1/7280),(0/1)],![(11/280),(11/280),(33/3640),(11/7280),(1/7280),(0/1)],![(11/364),(11/364),(11/1456),(1/728),(1/7280),(0/1)],![(33/1456),(33/1456),(9/1456),(9/7280),(1/7280),(0/1)]],![![(1/16),(1/16),(1/128),(1/1920),(0/1),(0/1)],![(1/16),(1/16),(1/120),(1/1680),(0/1),(0/1)],![(13/240),(13/240),(13/1680),(1/1680),(0/1),(0/1)],![(13/280),(13/280),(1/140),(1/1680),(0/1),(0/1)],![(11/280),(11/280),(11/1680),(1/1680),(0/1),(0/1)],![(11/336),(11/336),(1/168),(1/1680),(0/1),(0/1)]],![![(1/16),(1/16),(1/256),(0/1),(0/1),(0/1)],![(1/16),(1/16),(1/240),(0/1),(0/1),(0/1)],![(7/120),(7/120),(1/240),(0/1),(0/1),(0/1)],![(13/240),(13/240),(1/240),(0/1),(0/1),(0/1)],![(1/20),(1/20),(1/240),(0/1),(0/1),(0/1)],![(11/240),(11/240),(1/240),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)]],![![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(1/15),(1/15),(0/1),(0/1),(0/1),(0/1)],![(1/14),(1/14),(0/1),(0/1),(0/1),(0/1)],![(1/13),(1/13),(0/1),(0/1),(0/1),(0/1)],![(1/12),(1/12),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(1/1),(1/1),(1/1),(1/1),(1/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(15/16),(7/8),(13/16),(3/4),(11/16)],![(1/16),(1/16),(1/16),(1/16),(1/16),(1/16)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(7/8),(91/120),(13/20),(11/20),(11/24)],![(1/8),(7/60),(13/120),(1/10),(11/120),(1/12)],![(1/120),(1/120),(1/120),(1/120),(1/120),(1/120)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(13/16),(13/20),(143/280),(11/28),(33/112)],![(3/16),(13/80),(39/280),(33/280),(11/112),(9/112)],![(1/40),(13/560),(3/140),(11/560),(1/56),(9/560)],![(1/560),(1/560),(1/560),(1/560),(1/560),(1/560)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(3/4),(11/20),(11/28),(99/364),(33/182)],![(1/4),(1/5),(11/70),(11/91),(33/364),(6/91)],![(1/20),(3/70),(33/910),(11/364),(9/364),(9/455)],![(1/140),(3/455),(11/1820),(1/182),(9/1820),(2/455)],![(1/1820),(1/1820),(1/1820),(1/1820),(1/1820),(1/1820)],![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(11/16),(11/24),(33/112),(33/182),(11/104)],![(5/16),(11/48),(55/336),(165/1456),(55/728),(5/104)],![(1/12),(11/168),(55/1092),(55/1456),(5/182),(1/52)],![(1/56),(11/728),(55/4368),(15/1456),(3/364),(1/156)],![(1/364),(11/4368),(5/2184),(3/1456),(1/546),(1/624)],![(1/4368),(1/4368),(1/4368),(1/4368),(1/4368),(1/4368)]],![![(1/1),(5/8),(3/8),(3/14),(3/26),(3/52)],![(3/8),(1/4),(9/56),(9/91),(3/52),(9/286)],![(1/8),(5/56),(45/728),(15/364),(15/572),(9/572)],![(1/28),(5/182),(15/728),(15/1001),(3/286),(1/143)],![(3/364),(5/728),(45/8008),(9/2002),(1/286),(3/1144)],![(1/728),(5/4004),(9/8008),(1/1001),(1/1144),(3/4004)]],![![(1/1),(9/16),(3/10),(3/20),(9/130),(3/104)],![(7/16),(21/80),(3/20),(21/260),(21/520),(21/1144)],![(7/40),(9/80),(9/130),(21/520),(63/2860),(63/5720)],![(1/16),(9/208),(3/104),(21/1144),(63/5720),(7/1144)],![(1/52),(3/208),(3/286),(21/2860),(7/1430),(7/2288)],![(1/208),(9/2288),(9/2860),(7/2860),(21/11440),(3/2288)]],![![(1/1),(1/2),(7/30),(1/10),(1/26),(1/78)],![(1/2),(4/15),(2/15),(4/65),(1/39),(4/429)],![(7/30),(2/15),(14/195),(7/195),(7/429),(14/2145)],![(1/10),(4/65),(7/195),(14/715),(7/715),(28/6435)],![(1/26),(1/39),(7/429),(7/715),(7/1287),(7/2574)],![(1/78),(4/429),(14/2145),(28/6435),(7/2574),(2/1287)]],![![(1/1),(7/16),(7/40),(1/16),(1/52),(1/208)],![(9/16),(21/80),(9/80),(9/208),(3/208),(9/2288)],![(3/10),(3/20),(9/130),(3/104),(3/286),(9/2860)],![(3/20),(21/260),(21/520),(21/1144),(21/2860),(7/2860)],![(9/130),(21/520),(63/2860),(63/5720),(7/1430),(21/11440)],![(3/104),(21/1144),(63/5720),(7/1144),(7/2288),(3/2288)]],![![(1/1),(3/8),(1/8),(1/28),(3/364),(1/728)],![(5/8),(1/4),(5/56),(5/182),(5/728),(5/4004)],![(3/8),(9/56),(45/728),(15/728),(45/8008),(9/8008)],![(3/14),(9/91),(15/364),(15/1001),(9/2002),(1/1001)],![(3/26),(3/52),(15/572),(3/286),(1/286),(1/1144)],![(3/52),(9/286),(9/572),(1/143),(3/1144),(3/4004)]],![![(1/1),(5/16),(1/12),(1/56),(1/364),(1/4368)],![(11/16),(11/48),(11/168),(11/728),(11/4368),(1/4368)],![(11/24),(55/336),(55/1092),(55/4368),(5/2184),(1/4368)],![(33/112),(165/1456),(55/1456),(15/1456),(3/1456),(1/4368)],![(33/182),(55/728),(5/182),(3/364),(1/546),(1/4368)],![(11/104),(5/104),(1/52),(1/156),(1/624),(1/4368)]],![![(1/1),(1/4),(1/20),(1/140),(1/1820),(0/1)],![(3/4),(1/5),(3/70),(3/455),(1/1820),(0/1)],![(11/20),(11/70),(33/910),(11/1820),(1/1820),(0/1)],![(11/28),(11/91),(11/364),(1/182),(1/1820),(0/1)],![(99/364),(33/364),(9/364),(9/1820),(1/1820),(0/1)],![(33/182),(6/91),(9/455),(2/455),(1/1820),(0/1)]],![![(1/1),(3/16),(1/40),(1/560),(0/1),(0/1)],![(13/16),(13/80),(13/560),(1/560),(0/1),(0/1)],![(13/20),(39/280),(3/140),(1/560),(0/1),(0/1)],![(143/280),(33/280),(11/560),(1/560),(0/1),(0/1)],![(11/28),(11/112),(1/56),(1/560),(0/1),(0/1)],![(33/112),(9/112),(9/560),(1/560),(0/1),(0/1)]],![![(1/1),(1/8),(1/120),(0/1),(0/1),(0/1)],![(7/8),(7/60),(1/120),(0/1),(0/1),(0/1)],![(91/120),(13/120),(1/120),(0/1),(0/1),(0/1)],![(13/20),(1/10),(1/120),(0/1),(0/1),(0/1)],![(11/20),(11/120),(1/120),(0/1),(0/1),(0/1)],![(11/24),(1/12),(1/120),(0/1),(0/1),(0/1)]],![![(1/1),(1/16),(0/1),(0/1),(0/1),(0/1)],![(15/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(7/8),(1/16),(0/1),(0/1),(0/1),(0/1)],![(13/16),(1/16),(0/1),(0/1),(0/1),(0/1)],![(3/4),(1/16),(0/1),(0/1),(0/1),(0/1)],![(11/16),(1/16),(0/1),(0/1),(0/1),(0/1)]],![![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)],![(1/1),(0/1),(0/1),(0/1),(0/1),(0/1)]]]

theorem edgeTable_eq : ∀ (locked : Bool) (a : Fin 17) (r : Fin 6),
    edgeCoeff 16 a.val locked r = edgeTable (index locked a) r := by decide +kernel

theorem pairTable_eq : ∀ (locked : Bool) (a : Fin 17) (r q : Fin 6),
    pairCoeff 16 a.val ((if locked then 16 else 15)-a.val) locked r q =
      pairTable (index locked a) r q := by decide +kernel
end Aris4Math.ThirtyFour.CachedCoefficients16
#print axioms Aris4Math.ThirtyFour.CachedCoefficients16.edgeTable_eq
#print axioms Aris4Math.ThirtyFour.CachedCoefficients16.pairTable_eq
