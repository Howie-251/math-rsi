import Aris4Math.ThirtyFour.TwentyThreeSparseTrace

/-! Relabeling invariants for mixed low/high locks. Rooted second moments
retain incidence correlations discarded by the unrooted trace spectrum. -/
namespace Aris4Math.ThirtyFour.TwentyThreeRoleMoments
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
variable {n v : ℕ}

def lowCard (r : ℕ) (T : Finset (Fin n)) := (T.filter fun i => i.val<r).card
def highCard (r : ℕ) (T : Finset (Fin n)) := T.card-lowCard r T
def SameRole (r : ℕ) (σ : Equiv.Perm (Fin n)) := ∀ i, (σ i).val<r ↔ i.val<r

theorem lowCard_map (r : ℕ) (σ : Equiv.Perm (Fin n)) (roles : SameRole r σ)
    (T : Finset (Fin n)) : lowCard r (T.map σ.toEmbedding)=lowCard r T := by
  unfold lowCard
  rw [Finset.filter_map,Finset.card_map]
  congr 1
  apply Finset.filter_congr
  intro i _
  exact roles i

theorem highCard_map (r : ℕ) (σ : Equiv.Perm (Fin n)) (roles : SameRole r σ)
    (T : Finset (Fin n)) : highCard r (T.map σ.toEmbedding)=highCard r T := by
  simp only [highCard,Finset.card_map,lowCard_map r σ roles]

def moment (μ : Finset (Fin n)→ℕ) (r a b p : ℕ) :=
  ∑ T : Finset (Fin n), if lowCard r T=a ∧ highCard r T=b then μ T^(p+1) else 0

def rootMass (μ : Finset (Fin n)→ℕ) (r a b : ℕ) (i : Fin n) :=
  ∑ T : Finset (Fin n), if lowCard r T=a ∧ highCard r T=b ∧ i∈T then μ T else 0

def rootMoment (μ : Finset (Fin n)→ℕ) (r a b : ℕ) (low : Bool) :=
  ∑ i : Fin n, if decide (i.val<r)=low then (rootMass μ r a b i)^2 else 0

theorem moment_map (μ : Finset (Fin n)→ℕ) (r a b p : ℕ)
    (σ : Equiv.Perm (Fin n)) (roles : SameRole r σ) :
    moment (fun T => μ (T.map σ.toEmbedding)) r a b p=moment μ r a b p := by
  unfold moment
  apply Fintype.sum_equiv σ.finsetCongr
  intro T
  simp only [Equiv.finsetCongr_apply,lowCard_map r σ roles,highCard_map r σ roles]

theorem rootMass_map (μ : Finset (Fin n)→ℕ) (r a b : ℕ)
    (σ : Equiv.Perm (Fin n)) (roles : SameRole r σ) (i : Fin n) :
    rootMass (fun T => μ (T.map σ.toEmbedding)) r a b i=rootMass μ r a b (σ i) := by
  unfold rootMass
  apply Fintype.sum_equiv σ.finsetCongr
  intro T
  simp only [Equiv.finsetCongr_apply,lowCard_map r σ roles,highCard_map r σ roles,
    Finset.mem_map_equiv,Equiv.symm_apply_apply]

theorem rootMoment_map (μ : Finset (Fin n)→ℕ) (r a b : ℕ) (low : Bool)
    (σ : Equiv.Perm (Fin n)) (roles : SameRole r σ) :
    rootMoment (fun T => μ (T.map σ.toEmbedding)) r a b low=rootMoment μ r a b low := by
  unfold rootMoment
  apply Fintype.sum_equiv σ
  intro i
  rw [rootMass_map μ r a b σ roles i]
  simp only [roles i]

theorem moment_of_relabelled_counts (H : Simple5Hypergraph (Fin v))
    (f : Fin n↪Fin v) (σ : Equiv.Perm (Fin n)) (μ : Finset (Fin n)→ℕ)
    (r a b p : ℕ) (roles : SameRole r σ)
    (actual : ∀ T, count H (σ.toEmbedding.trans f) T=μ T) :
    moment (count H f) r a b p=moment μ r a b p := by
  have equality : μ=fun T => count H f (T.map σ.toEmbedding) := by
    funext T
    rw [←LockRelabel.count_comp_perm,actual]
  rw [equality,moment_map (count H f) r a b p σ roles]

theorem rootMoment_of_relabelled_counts (H : Simple5Hypergraph (Fin v))
    (f : Fin n↪Fin v) (σ : Equiv.Perm (Fin n)) (μ : Finset (Fin n)→ℕ)
    (r a b : ℕ) (low : Bool) (roles : SameRole r σ)
    (actual : ∀ T, count H (σ.toEmbedding.trans f) T=μ T) :
    rootMoment (count H f) r a b low=rootMoment μ r a b low := by
  have equality : μ=fun T => count H f (T.map σ.toEmbedding) := by
    funext T
    rw [←LockRelabel.count_comp_perm,actual]
  rw [equality,rootMoment_map (count H f) r a b low σ roles]

open TwentyThreeSparseTrace

def sparseMoment (xs : TraceList n) (r a b p : ℕ) :=
  ∑ T∈support xs, if lowCard r T=a ∧ highCard r T=b then counts xs T^(p+1) else 0

theorem sparseMoment_eq (xs : TraceList n) (r a b p : ℕ) :
    sparseMoment xs r a b p=moment (counts xs) r a b p := by
  unfold sparseMoment moment
  apply Finset.sum_subset (Finset.subset_univ _)
  intro T _ absent
  rw [counts_zero_of_absent xs T absent]
  simp

def sparseRootMass (xs : TraceList n) (r a b : ℕ) (i : Fin n) :=
  ∑ T∈support xs, if lowCard r T=a ∧ highCard r T=b ∧ i∈T then counts xs T else 0

theorem sparseRootMass_eq (xs : TraceList n) (r a b : ℕ) (i : Fin n) :
    sparseRootMass xs r a b i=rootMass (counts xs) r a b i := by
  unfold sparseRootMass rootMass
  apply Finset.sum_subset (Finset.subset_univ _)
  intro T _ absent
  rw [counts_zero_of_absent xs T absent]
  simp

def sparseRootMoment (xs : TraceList n) (r a b : ℕ) (low : Bool) :=
  ∑ i : Fin n, if decide (i.val<r)=low then (sparseRootMass xs r a b i)^2 else 0

theorem sparseRootMoment_eq (xs : TraceList n) (r a b : ℕ) (low : Bool) :
    sparseRootMoment xs r a b low=rootMoment (counts xs) r a b low := by
  simp only [sparseRootMoment,rootMoment,sparseRootMass_eq]

end Aris4Math.ThirtyFour.TwentyThreeRoleMoments
#print axioms Aris4Math.ThirtyFour.TwentyThreeRoleMoments.moment_of_relabelled_counts
#print axioms Aris4Math.ThirtyFour.TwentyThreeRoleMoments.rootMoment_of_relabelled_counts
#print axioms Aris4Math.ThirtyFour.TwentyThreeRoleMoments.sparseRootMoment_eq
