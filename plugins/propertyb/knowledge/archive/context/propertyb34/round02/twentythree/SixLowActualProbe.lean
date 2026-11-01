import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
import Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting

/-! Actual lock counts determine the original-edge trace shape. This bridge
retains multiplicity, including distinct edges with identical traces. -/
namespace Aris4Math.ThirtyFour.TwentyThreeTraceShape
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyThreeSevenLowCounting

theorem signature_image {n v : ℕ} (f : Fin n ↪ Fin v) (e : Finset (Fin v)) :
    (lockSignature f e).image f = e ∩ Finset.univ.image f := by
  ext x
  constructor
  · intro hx
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hx
    exact Finset.mem_inter.mpr ⟨(mem_lockSignature f e i).mp hi,
      Finset.mem_image.mpr ⟨i,Finset.mem_univ i,rfl⟩⟩
  · intro hx
    obtain ⟨he,hr⟩ := Finset.mem_inter.mp hx
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hr
    exact Finset.mem_image.mpr ⟨i,(mem_lockSignature f e i).mpr he,rfl⟩

theorem signature_card {n v : ℕ} (f : Fin n ↪ Fin v) (e : Finset (Fin v)) :
    (lockSignature f e).card = (e ∩ Finset.univ.image f).card := by
  rw [← signature_image,Finset.card_image_of_injective _ f.injective]

/-- Exact actual counts imply the required original-edge trace statement. -/
theorem shape_of_counts {n v : ℕ} (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (μ : Finset (Fin n) → ℕ)
    (small : ∀ T, 0 < μ T → T.card ≤ 3)
    (triples : (∑ T ∈ Finset.univ.filter (fun T : Finset (Fin n) => T.card=3), μ T)=2)
    (actual : ∀ T, count H f T=μ T) :
    TwoTripleTraceShape H (Finset.univ.image f) := by
  constructor
  · intro e he
    have positive : 0 < count H f (lockSignature f e) := by
      apply Finset.card_pos.mpr
      exact ⟨e,Finset.mem_filter.mpr ⟨he,rfl⟩⟩
    rw [actual] at positive
    rw [← signature_card]
    exact small _ positive
  · have totals := sum_counts H f (Finset.univ.filter fun T : Finset (Fin n) => T.card=3)
    simp only [Finset.mem_filter,Finset.mem_univ,true_and,signature_card] at totals
    rw [← totals]
    simp_rw [actual]
    exact triples

/-- The total number of original edges having a given trace size. -/
def cardMass {n : ℕ} (μ : Finset (Fin n) → ℕ) (k : ℕ) : ℕ :=
  ∑ T ∈ Finset.univ.filter (fun T : Finset (Fin n) => T.card=k), μ T

theorem cardMass_actual {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (f : Fin n ↪ Fin v) (k : ℕ) :
    cardMass (count H f) k =
      (H.edges.filter (fun e => (lockSignature f e).card=k)).card := by
  simpa only [cardMass,Finset.mem_filter,Finset.mem_univ,true_and] using
    sum_counts H f (Finset.univ.filter fun T : Finset (Fin n) => T.card=k)

/-- Relabeling preserves the size spectrum on the same original edges. -/
theorem cardMass_relabel {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (f : Fin n ↪ Fin v) (σ : Equiv.Perm (Fin n)) (k : ℕ) :
    cardMass (count H (σ.toEmbedding.trans f)) k = cardMass (count H f) k := by
  rw [cardMass_actual,cardMass_actual]
  congr 1
  apply Finset.filter_congr
  intro e he
  have same := congrArg Finset.card (LockRelabel.signature_comp_perm f σ e)
  simp only [Finset.card_map] at same
  rw [same]

/-- A classified inventory implies its size spectrum without retaining
any canonical permutation as an extra premise. -/
theorem cardMass_of_relabelled_counts {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (f : Fin n ↪ Fin v) (σ : Equiv.Perm (Fin n)) (μ : Finset (Fin n) → ℕ)
    (actual : ∀ T, count H (σ.toEmbedding.trans f) T=μ T) (k : ℕ) :
    cardMass (count H f) k=cardMass μ k := by
  rw [← cardMass_relabel H f σ k]
  simp only [cardMass,actual]

/-- Moments of type multiplicities grouped by trace cardinality. The first
moment is the size spectrum; the second also detects multiplicity clustering. -/
def cardMoment {n : ℕ} (μ : Finset (Fin n) → ℕ) (k p : ℕ) : ℕ :=
  ∑ T ∈ Finset.univ.filter (fun T : Finset (Fin n) => T.card=k), μ T ^ p

theorem cardMoment_map {n : ℕ} (μ : Finset (Fin n) → ℕ)
    (σ : Equiv.Perm (Fin n)) (k p : ℕ) :
    cardMoment (fun T => μ (T.map σ.toEmbedding)) k p=cardMoment μ k p := by
  unfold cardMoment
  simp only [Finset.sum_filter]
  apply Fintype.sum_equiv σ.finsetCongr
  intro T
  simp only [Equiv.finsetCongr_apply,Finset.card_map]

theorem cardMoment_relabel {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (f : Fin n ↪ Fin v) (σ : Equiv.Perm (Fin n)) (k p : ℕ) :
    cardMoment (count H (σ.toEmbedding.trans f)) k p=cardMoment (count H f) k p := by
  have actual : count H (σ.toEmbedding.trans f) =
      fun T => count H f (T.map σ.toEmbedding) := by
    funext T
    exact LockRelabel.count_comp_perm H f σ T
  rw [actual]
  exact cardMoment_map (count H f) σ k p

theorem cardMoment_of_relabelled_counts {n v : ℕ} (H : Simple5Hypergraph (Fin v))
    (f : Fin n ↪ Fin v) (σ : Equiv.Perm (Fin n)) (μ : Finset (Fin n) → ℕ)
    (actual : ∀ T, count H (σ.toEmbedding.trans f) T=μ T) (k p : ℕ) :
    cardMoment (count H f) k p=cardMoment μ k p := by
  rw [← cardMoment_relabel H f σ k p]
  simp only [cardMoment,actual]

end Aris4Math.ThirtyFour.TwentyThreeTraceShape
#print axioms Aris4Math.ThirtyFour.TwentyThreeTraceShape.shape_of_counts

#print axioms Aris4Math.ThirtyFour.TwentyThreeTraceShape.cardMass_of_relabelled_counts

#print axioms Aris4Math.ThirtyFour.TwentyThreeTraceShape.cardMoment_of_relabelled_counts

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
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified
abbrev Residue := Fin 2
def residualCounts : Residue → Finset (Fin 5) → ℕ := ![(fun T => if T=∅ then 12 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={1,2,4} then 1 else if T={0,3,4} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else 0)]
end Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified

namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockProjection LockExtension PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
abbrev OldCase := TwentyThreeFiveLowClassified.Residue
abbrev NewCase := Fin 3
abbrev NewPerm := Fin 13
def oldCounts := TwentyThreeFiveLowClassified.residualCounts
def μ : NewCase → Finset (Fin 6) → ℕ := ![(fun T => if T=∅ then 9 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={2,3} then 1 else if T={4} then 3 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={1,2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else 0),(fun T => if T=∅ then 10 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={4} then 3 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={0,4,5} then 1 else 0),(fun T => if T=∅ then 11 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else 0)]
def entries : OldCase → List (Finset (Fin 5) × ℕ) := ![[({0},3),({1},3),({0,1},1),({2},3),({0,2},1),({3},3),({1,3},1),({2,3},1),({4},4),({1,2,4},1),({0,3,4},1)],[({0},2),({1},2),({0,1},1),({2},3),({0,2},1),({1,2},1),({3},3),({0,3},1),({1,3},1),({4},3),({0,4},1),({1,4},1),({2,3,4},1)]]
def newPermFn : NewPerm → Fin 6 → Fin 6 := ![![0,1,2,3,4,5],![0,1,2,3,5,4],![0,1,2,4,3,5],![0,1,3,2,4,5],![0,1,3,4,2,5],![0,1,4,2,3,5],![0,1,4,3,2,5],![0,1,5,2,3,4],![0,2,1,3,5,4],![0,2,3,4,1,5],![0,2,5,1,3,4],![1,3,5,0,2,4],![2,3,5,0,1,4]]
theorem newPermFn_injective : ∀ p, Function.Injective (newPermFn p) := by decide +kernel
noncomputable def newPerm (p : NewPerm) : Equiv.Perm (Fin 6) :=
  Equiv.ofBijective (newPermFn p) ⟨newPermFn_injective p,Finite.surjective_of_injective (newPermFn_injective p)⟩
def expected : OldCase → Fin 6 → ℕ := ![![12,16,4,2,0,0],![13,13,7,1,0,0]]
theorem expected_correct : ∀ r (k : Fin 6),
    TwentyThreeTraceShape.cardMass (oldCounts r) k=expected r k := by decide +kernel

def OldResidual (c : Finset (Fin 5) → ℕ) : Prop :=
  ∃ r : OldCase, ∀ k : Fin 6, TwentyThreeTraceShape.cardMass c k=expected r k
noncomputable instance (c : Finset (Fin 5) → ℕ) : Decidable (OldResidual c) := by
  unfold OldResidual
  infer_instance

def deletion (x : Fin 6) : Fin 5 ↪ Fin 6 := x.succAboveEmb

def projected (x : Fin 6) (c : Finset (Fin 6) → ℕ) (T : Finset (Fin 5)) :=
  ∑ U : Finset (Fin 6), if project (deletion x) U=T then c U else 0

def vector (c : OldCase) (values : List ℕ) := BoundedAllocations.decode (entries c) values

def newCounts (c : OldCase) (values : List ℕ) := extend (oldCounts c) (vector c values) 6

def code (c : OldCase) (values : List ℕ) : ℕ := c.val+2*(values.foldl (fun a x => 7*a+x) 0)
abbrev Witness := Fin 6 × NewCase × NewPerm
def rowCovered (c : OldCase) (values : List ℕ) (w : Witness) : Prop :=
  TwentyThreeLowPromotionBase.Feasible (newCounts c values) →
  OldResidual (projected w.1 (newCounts c values)) →
  ∀ T, newCounts c values (T.map (newPerm w.2.2).toEmbedding)=μ w.2.1 T
noncomputable instance (c : OldCase) (values : List ℕ) (w : Witness) : Decidable (rowCovered c values w) := by
  unfold rowCovered
  infer_instance

def covered (c : OldCase) (values : List ℕ) : Prop := ∃ w : Witness, rowCovered c values w

inductive Reason where
  | zeroPair (i j : Fin 6)
  | excess (i : Fin 6)
  | projection (x : Fin 6) (traces : TwentyThreeSparseTrace.TraceList 6)
  | matched (q : NewCase) (p : NewPerm)

def catalogue (c : OldCase) := BoundedAllocations.enumerate
  TwentyThreeLowPromotionBase.incidenceCost (entries c) TwentyThreeLowPromotionBase.incidenceCap
def SparseResidual (xs : TwentyThreeSparseTrace.TraceList 5) : Prop := ∃ r : OldCase, ∀ k : Fin 6, TwentyThreeSparseTrace.moment xs k 0=expected r k
noncomputable instance (xs : TwentyThreeSparseTrace.TraceList 5) : Decidable (SparseResidual xs) := by
  unfold SparseResidual
  infer_instance

theorem sparseResidual_of_old (xs : TwentyThreeSparseTrace.TraceList 5)
    (h : OldResidual (TwentyThreeSparseTrace.counts xs)) : SparseResidual xs := by
  obtain ⟨r,h⟩ := h
  refine ⟨r,?_⟩
  intro k
  rw [TwentyThreeSparseTrace.moment_zero_eq_cardMass]
  exact h k

def rowValid (c : OldCase) (values : List ℕ) : Reason → Prop
  | .zeroPair i j => i≠j ∧ TwentyThreeLowPromotionBase.co (newCounts c values) i j=0
  | .excess i => 2 < ∑ j ∈ Finset.univ.erase i,
      (TwentyThreeLowPromotionBase.co (newCounts c values) i j-1)
  | .projection x traces =>
      (∀ T, newCounts c values T=TwentyThreeSparseTrace.counts traces T) ∧
      ¬ SparseResidual (TwentyThreeSparseTrace.projected (deletion x) traces)
  | .matched q p => ∀ T,
      newCounts c values (T.map (newPerm p).toEmbedding)=μ q T
noncomputable instance (c : OldCase) (values : List ℕ) (reason : Reason) :
    Decidable (rowValid c values reason) := by
  cases reason <;> unfold rowValid <;> infer_instance

theorem rowValid_covered (c : OldCase) (values : List ℕ) (reason : Reason)
    (valid : rowValid c values reason) : covered c values := by
  cases reason with
  | zeroPair i j =>
    refine ⟨(0,0,0),?_⟩
    intro feasible _ T
    have pos := feasible.1 i j valid.1
    rw [valid.2] at pos
    omega
  | excess i =>
    refine ⟨(0,0,0),?_⟩
    intro feasible _ T
    have bound := feasible.2 i
    exact (Nat.not_lt_of_ge bound valid).elim
  | projection x traces =>
    refine ⟨(x,0,0),?_⟩
    intro _ old T
    have same : projected x (newCounts c values)=
        TwentyThreeSparseTrace.counts (TwentyThreeSparseTrace.projected (deletion x) traces) := by
      funext U
      rw [TwentyThreeSparseTrace.projected_counts]
      unfold projected
      simp_rw [valid.1]
    have old' : OldResidual (TwentyThreeSparseTrace.counts
        (TwentyThreeSparseTrace.projected (deletion x) traces)) := by
      rwa [← same]
    exact (valid.2 (sparseResidual_of_old _ old')).elim
  | matched q p =>
    exact ⟨(0,q,p),fun _ _ T => valid T⟩

end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog PromotionReconstruction
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000

theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel

theorem entries_values (c : OldCase) (e : Finset (Fin 5) × ℕ) (mem : e∈entries c) :
    e.2=oldCounts c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2=oldCounts c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)

theorem entries_support : ∀ c, ∀ T : Finset (Fin 5),
    T≠∅ → T∉(entries c).map Prod.fst → oldCounts c T=0 := by decide +kernel

variable (checkedOldClassifier : ∀ (H : Simple5Hypergraph (Fin 23)), H.PairCovering →
    H.edges.card=34 → ∀ (f : Fin 5 ↪ Fin 23),
    (∀ i, H.degree (f i)=6) → ¬ PropertyB H →
    ∃ r : TwentyThreeFiveLowClassified.Residue, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeFiveLowClassified.residualCounts r T)
include checkedOldClassifier

theorem old_actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (g : Fin 5 ↪ Fin 23)
    (degrees : ∀ i, H.degree (g i)=6) (notB : ¬ PropertyB H) :
    OldResidual (count H g) := by
  obtain ⟨r, σ, actual⟩ := checkedOldClassifier H cover edges g degrees notB
  refine ⟨r,?_⟩
  intro k
  exact (TwentyThreeTraceShape.cardMass_of_relabelled_counts H g σ (oldCounts r) actual k).trans
    (expected_correct r k)

attribute [local irreducible] covered

theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 6 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (values : List ℕ) (matched : covered c values)
    (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  have feasible := TwentyThreeLowPromotionBase.feasible_actual H cover f degrees
    (newCounts c values) actual
  unfold covered at matched
  obtain ⟨choice,matched⟩ := matched
  have projection : ∀ T, projected choice.1 (newCounts c values) T =
      count H ((deletion choice.1).trans f) T := by
    intro T
    rw [LockProjection.count_comp]
    simp only [projected,actual]
  have old := old_actual checkedOldClassifier H cover edges ((deletion choice.1).trans f)
    (fun i => degrees ((deletion choice.1) i)) notB
  have residual : OldResidual (projected choice.1 (newCounts c values)) := by
    simpa only [show projected choice.1 (newCounts c values)=
      count H ((deletion choice.1).trans f) from funext projection] using old
  unfold rowCovered at matched
  refine ⟨choice.2.1,newPerm choice.2.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched feasible residual T

variable (checkedCoverage : ∀ c values, values∈catalogue c → covered c values)
include checkedCoverage

/-- Complete actual extension from one canonical old inventory. Every
rejected projection is classified on the same original H. -/
theorem actual_extension (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 6 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (old : ∀ T, count H (restrict f) T=oldCounts c T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  let values := (entries c).map (fun e => promotion H f e.1)
  have member : values∈catalogue c := by
    apply TwentyThreeLowPromotionBase.actual_mem H cover f degrees (entries c) (entries_distinct c)
    intro e he
    rw [old,entries_values c e he]
  have prom (T : Finset (Fin 5)) (ne : T≠∅) : vector c values T=promotion H f T := by
    apply decode_nonempty H f (entries c) ?_ T ne
    intro S nonempty absent
    have bound := promotion_le_old H f S
    rw [old,entries_support c S nonempty absent] at bound
    omega
  have actual (T : Finset (Fin 6)) : count H f T=newCounts c values T :=
    extend_actual H f (oldCounts c) (vector c values) 6 old prom (degrees _) T
  exact actual_of_covered checkedOldClassifier H cover edges f degrees notB c values (checkedCoverage c values member) actual

/-- Every original low-lock choice is covered: first normalize its old
subset, then lift that same permutation while fixing the newly added point. -/
theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 6 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨c,σ,hc⟩ := checkedOldClassifier H cover edges (restrict f)
    (fun i => degrees i.castSucc) notB
  let lift := LockLiftRelabel.lift σ
  let g := lift.toEmbedding.trans f
  have old : ∀ T, count H (restrict g) T=oldCounts c T := by
    intro T
    rw [show restrict g=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    exact hc T
  obtain ⟨q,τ,ht⟩ := actual_extension checkedOldClassifier checkedCoverage H cover edges g (fun i => degrees (lift i)) notB c old
  exact ⟨q,τ.trans lift,ht⟩

end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion.actual
