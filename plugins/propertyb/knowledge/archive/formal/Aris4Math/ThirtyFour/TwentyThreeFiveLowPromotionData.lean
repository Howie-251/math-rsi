import Aris4Math.ThirtyFour.TwentyThreeFourLowClassified
import Aris4Math.ThirtyFour.TwentyThreeTraceShape
import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
import Aris4Math.ThirtyFour.TwentyThreeSparseTrace
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockProjection LockExtension PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
abbrev OldCase := TwentyThreeFourLowClassified.Residue
abbrev NewCase := Fin 12
abbrev NewPerm := Fin 32
def oldCounts := TwentyThreeFourLowClassified.residualCounts
def μ : NewCase → Finset (Fin 5) → ℕ := ![(fun T => if T=∅ then 12 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={1,2,4} then 1 else if T={0,3,4} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={2,3,4} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else 0),(fun T => if T=∅ then 14 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else 0),(fun T => if T=∅ then 12 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 4 else if T={1,2,3} then 1 else if T={4} then 4 else if T={1,2,4} then 1 else if T={0,3,4} then 1 else 0),(fun T => if T=∅ then 11 else if T={0} then 2 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={4} then 4 else if T={0,4} then 1 else if T={1,2,3,4} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={4} then 5 else if T={0,1,2,3,4} then 1 else 0),(fun T => if T=∅ then 12 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={4} then 4 else if T={0,3,4} then 1 else if T={1,2,3,4} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 4 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={3,4} then 1 else if T={1,2,3,4} then 1 else 0),(fun T => if T=∅ then 14 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else 0),(fun T => if T=∅ then 11 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 4 else if T={4} then 4 else if T={0,3,4} then 1 else if T={1,2,3,4} then 1 else 0)]
def entries : OldCase → List (Finset (Fin 4) × ℕ) := ![[({0},3),({1},3),({0,1},1),({2},3),({0,2},1),({1,2},1),({3},3),({0,3},1),({1,3},1),({2,3},1)],[({0},3),({1},4),({0,1},1),({2},4),({0,2},1),({3},4),({0,3},1),({1,2,3},1)],[({0},5),({1},5),({2},5),({3},5),({0,1,2,3},1)],[({0},3),({1},3),({0,1},1),({2},3),({0,2},1),({1,2},1),({3},4),({0,3},1),({1,2,3},1)],[({0},4),({1},4),({0,1},1),({2},4),({3},4),({0,2,3},1),({1,2,3},1)],[({0},2),({1},2),({0,1},1),({2},2),({0,2},1),({1,2},2),({3},2),({0,3},2),({1,3},1),({2,3},1)],[({0},2),({1},3),({0,1},1),({2},3),({0,2},1),({1,2},1),({3},3),({0,3},2),({1,2,3},1)],[({0},4),({1},4),({0,1},1),({2},4),({3},4),({2,3},1),({0,1,2,3},1)]]
def newPermFn : NewPerm → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,2,4,3],![0,1,3,2,4],![0,1,3,4,2],![0,1,4,2,3],![0,2,1,3,4],![0,2,3,1,4],![0,2,3,4,1],![0,3,1,2,4],![0,3,4,1,2],![0,4,1,2,3],![1,0,2,3,4],![1,0,3,2,4],![1,0,4,2,3],![1,2,0,3,4],![1,2,0,4,3],![1,2,3,0,4],![1,3,0,2,4],![2,0,1,3,4],![2,0,3,1,4],![2,0,4,1,3],![2,1,0,4,3],![2,1,3,0,4],![2,3,0,1,4],![3,0,1,2,4],![3,0,2,1,4],![3,0,4,1,2],![3,1,2,0,4],![4,0,1,2,3],![4,0,2,3,1],![4,1,2,3,0],![4,2,3,0,1]]
theorem newPermFn_injective : ∀ p, Function.Injective (newPermFn p) := by decide +kernel
noncomputable def newPerm (p : NewPerm) : Equiv.Perm (Fin 5) :=
  Equiv.ofBijective (newPermFn p) ⟨newPermFn_injective p,Finite.surjective_of_injective (newPermFn_injective p)⟩
def expected : OldCase → Fin 5 → Fin 2 → ℕ := ![![![16,256],![12,36],![6,6],![0,0],![0,0]],![![15,225],![15,57],![3,3],![1,1],![0,0]],![![13,169],![20,100],![0,0],![0,0],![1,1]],![![16,256],![13,43],![4,4],![1,1],![0,0]],![![15,225],![16,64],![1,1],![2,2],![0,0]],![![18,324],![8,16],![8,12],![0,0],![0,0]],![![17,289],![11,31],![5,7],![1,1],![0,0]],![![15,225],![16,64],![2,2],![0,0],![1,1]]]
theorem expected_correct : ∀ r (k : Fin 5) (p : Fin 2),
    TwentyThreeTraceShape.cardMoment (oldCounts r) k (p.val+1)=expected r k p := by decide +kernel

def OldResidual (c : Finset (Fin 4) → ℕ) : Prop :=
  ∃ r : OldCase, ∀ k : Fin 5, ∀ p : Fin 2, TwentyThreeTraceShape.cardMoment c k (p.val+1)=expected r k p
noncomputable instance (c : Finset (Fin 4) → ℕ) : Decidable (OldResidual c) := by
  unfold OldResidual
  infer_instance

def deletion (x : Fin 5) : Fin 4 ↪ Fin 5 := x.succAboveEmb

def projected (x : Fin 5) (c : Finset (Fin 5) → ℕ) (T : Finset (Fin 4)) :=
  ∑ U : Finset (Fin 5), if project (deletion x) U=T then c U else 0

def vector (c : OldCase) (values : List ℕ) := BoundedAllocations.decode (entries c) values

def newCounts (c : OldCase) (values : List ℕ) := extend (oldCounts c) (vector c values) 6

def code (c : OldCase) (values : List ℕ) : ℕ := c.val+8*(values.foldl (fun a x => 7*a+x) 0)
abbrev Witness := Fin 5 × NewCase × NewPerm
def rowCovered (c : OldCase) (values : List ℕ) (w : Witness) : Prop :=
  TwentyThreeLowPromotionBase.Feasible (newCounts c values) →
  OldResidual (projected w.1 (newCounts c values)) →
  ∀ T, newCounts c values (T.map (newPerm w.2.2).toEmbedding)=μ w.2.1 T
noncomputable instance (c : OldCase) (values : List ℕ) (w : Witness) : Decidable (rowCovered c values w) := by
  unfold rowCovered
  infer_instance

def covered (c : OldCase) (values : List ℕ) : Prop := ∃ w : Witness, rowCovered c values w

inductive Reason where
  | zeroPair (i j : Fin 5)
  | excess (i : Fin 5)
  | projection (x : Fin 5) (traces : TwentyThreeSparseTrace.TraceList 5)
  | matched (q : NewCase) (p : NewPerm)

def catalogue (c : OldCase) := BoundedAllocations.enumerate
  TwentyThreeLowPromotionBase.incidenceCost (entries c) TwentyThreeLowPromotionBase.incidenceCap
def SparseResidual (xs : TwentyThreeSparseTrace.TraceList 4) : Prop := ∃ r : OldCase, ∀ k : Fin 5, ∀ p : Fin 2, TwentyThreeSparseTrace.moment xs k p=expected r k p
noncomputable instance (xs : TwentyThreeSparseTrace.TraceList 4) : Decidable (SparseResidual xs) := by
  unfold SparseResidual
  infer_instance

theorem sparseResidual_of_old (xs : TwentyThreeSparseTrace.TraceList 4)
    (h : OldResidual (TwentyThreeSparseTrace.counts xs)) : SparseResidual xs := by
  obtain ⟨r,h⟩ := h
  refine ⟨r,?_⟩
  intro k p
  rw [TwentyThreeSparseTrace.moment_eq]
  exact h k p

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

end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
