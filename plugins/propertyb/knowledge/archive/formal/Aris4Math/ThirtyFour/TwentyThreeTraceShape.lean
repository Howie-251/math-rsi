import Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting
import Aris4Math.ThirtyFour.LockRelabel

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
