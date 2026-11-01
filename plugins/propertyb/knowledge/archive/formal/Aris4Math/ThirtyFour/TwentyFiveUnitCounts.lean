import Aris4Math.ThirtyFour.TwentyFiveUnitExtension
import Aris4Math.TraceRecovery

/-! Recover all actual trace counts, with individually prescribed lock degrees,
from the complete unit block family. This also supplies the feasibility bounds
used to discard impossible canonical families. -/
namespace Aris4Math.ThirtyFour.TwentyFiveUnitCounts

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.TwentyFiveUnitExtension
open Aris4Math.TraceRecovery
open Aris4Math.K6Classification

variable {n v : ℕ}

def inventory (m : ℕ) (degree : Fin n → ℕ) (B : Finset (Finset (Fin n)))
    (T : Finset (Fin n)) : ℕ :=
  if T=∅ then m-B.card-∑ i : Fin n, (degree i-(B.filter fun U => i∈U).card)
  else if T.card=1 then ∑ i∈T, (degree i-(B.filter fun U => i∈U).card)
  else if T∈B then 1 else 0

def Feasible (m : ℕ) (degree : Fin n → ℕ) (B : Finset (Finset (Fin n))) : Prop :=
  (∀ i, (B.filter fun U => i∈U).card ≤ degree i) ∧
    B.card+(∑ i : Fin n, (degree i-(B.filter fun U => i∈U).card)) ≤ m

instance (m : ℕ) (degree : Fin n → ℕ) (B : Finset (Finset (Fin n))) :
    Decidable (Feasible m degree B) := by unfold Feasible; infer_instance

theorem labeled_blocks_eq (H : Simple5Hypergraph (Fin v)) (W : Finset (Fin v))
    (label : ↥W ≃ Fin n) :
    (H.multiTraces W).image (labelBlock W label)=blocks H (lockVertices W label) := by
  ext T
  rw [← unlabel_mem_blocks, H.mem_multiTraces, unlabel_card, mem_blocks]
  change (∃ e∈H.edges, e∩W=unlabel W label T) ∧ 2≤T.card ↔
    2≤T.card ∧ 0<(H.edges.filter fun e => lockedLabels (lockVertices W label) e=T).card
  rw [Finset.card_pos]
  simp only [Finset.Nonempty, Finset.mem_filter, labels_eq_iff_trace]
  tauto

theorem labeled_inventory (H : Simple5Hypergraph (Fin v)) (W : Finset (Fin v))
    (label : ↥W ≃ Fin n) (unit : H.UnitCodegrees W) (degree : Fin n → ℕ)
    (degrees : ∀ i, H.degree (lockVertices W label i)=degree i) :
    (∀ T, count H (lockVertices W label) T=
      inventory H.edges.card degree ((H.multiTraces W).image (labelBlock W label)) T) ∧
    Feasible H.edges.card degree ((H.multiTraces W).image (labelBlock W label)) := by
  let B := (H.multiTraces W).image (labelBlock W label)
  have split (i : Fin n) :
      H.typeCount W (unlabel W label {i})+(B.filter fun U => i∈U).card=degree i := by
    rw [show B=(H.multiTraces W).image (labelBlock W label) from rfl, labeled_incidence_card]
    have h := H.singleton_typeCount_add_blocks W unit (label.symm i).property
    rw [← degrees i]
    simpa only [unlabel, Finset.map_singleton] using h
  have singles (i : Fin n) : H.typeCount W (unlabel W label {i})=
      degree i-(B.filter fun U => i∈U).card := by have := split i; omega
  have partition := H.typeCount_partition W unit
  rw [singleton_sum_labels H W label, ← labeled_blocks_card H W label] at partition
  change H.typeCount W ∅+(∑ i : Fin n, H.typeCount W (unlabel W label {i}))+B.card=H.edges.card at partition
  simp_rw [singles] at partition
  constructor
  · intro T
    change (H.edges.filter (fun e => lockedLabels (lockVertices W label) e=T)).card=_
    rw [labeled_fiber_card]
    by_cases empty : T=∅
    · subst T
      simp only [inventory, if_pos rfl, unlabel, Finset.map_empty]
      change H.typeCount W ∅=H.edges.card-B.card-∑ i : Fin n, (degree i-(B.filter fun U => i∈U).card)
      omega
    by_cases one : T.card=1
    · obtain ⟨i, rfl⟩ := Finset.card_eq_one.mp one
      simpa only [inventory, Finset.singleton_ne_empty, if_false, Finset.card_singleton,
        if_pos rfl, Finset.sum_singleton] using singles i
    · have two : 2≤(unlabel W label T).card := by
        rw [unlabel_card]
        have pos := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr empty)
        omega
      rw [H.typeCount_large W _ unit two]
      simp only [unlabel_mem_blocks, inventory, if_neg empty, if_neg one]
  · constructor
    · intro i
      change (B.filter fun U => i∈U).card≤degree i
      have := split i
      omega
    · change B.card+(∑ i : Fin n, (degree i-(B.filter fun U => i∈U).card))≤H.edges.card
      omega

/-- Actual arbitrary embeddings are identified with their image, so the old
trace recovery theorem applies without any extra labeling assumption. -/
theorem actual_inventory (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (unit : Unit H f) (degree : Fin n → ℕ) (degrees : ∀ i, H.degree (f i)=degree i) :
    (∀ T, count H f T=inventory H.edges.card degree (pairCompletion (large H f)) T) ∧
      Feasible H.edges.card degree (pairCompletion (large H f)) := by
  let W := Finset.univ.map f
  let toW : Fin n → ↥W := fun i => ⟨f i, Finset.mem_map.mpr ⟨i,Finset.mem_univ _,rfl⟩⟩
  have inj : Function.Injective toW := fun i j h => f.injective (congrArg Subtype.val h)
  have surj : Function.Surjective toW := by
    intro x
    obtain ⟨i, _, eq⟩ := Finset.mem_map.mp x.property
    exact ⟨i, Subtype.ext eq⟩
  let e := Equiv.ofBijective toW ⟨inj,surj⟩
  have vertices : lockVertices W e.symm=f := by
    apply Function.Embedding.ext
    intro i
    rfl
  have unitW : H.UnitCodegrees W := by
    intro x hx y hy ne
    obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hx
    obtain ⟨j, _, rfl⟩ := Finset.mem_map.mp hy
    exact unit i j (fun eq => ne (congrArg f eq))
  have deg : ∀ i, H.degree (lockVertices W e.symm i)=degree i := by
    rw [vertices]
    exact degrees
  have h := labeled_inventory H W e.symm unitW degree deg
  rw [labeled_blocks_eq, vertices, blocks_recovered H f unit] at h
  exact h

end Aris4Math.ThirtyFour.TwentyFiveUnitCounts

#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitCounts.actual_inventory
