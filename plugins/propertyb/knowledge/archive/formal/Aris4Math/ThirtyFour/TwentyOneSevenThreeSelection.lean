import Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights
import Aris4Math.ThirtyFour.TwentyOneSevenTriples

/-! Actual selections for exactly three seven-degree vertices. This module
supplies structural inputs; it does not assert that the r=3 branch is closed. -/
namespace Aris4Math.ThirtyFour.TwentyOneSevenThreeSelection
open scoped BigOperators
open TwentyOneSevenSelection TwentyOneSevenThreeSelectionWeights
open Aris4Math.ThirtyThree.TripleProfiles (threeVertices)

def pattern (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21) (u : Fin 21) : Finset (Fin 3) :=
  Finset.univ.filter fun i => H.codegree (f i) u=1

@[simp] theorem mem_pattern (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (u : Fin 21) (i : Fin 3) : i∈pattern H f u ↔ H.codegree (f i) u=1 := by
  simp [pattern]

theorem eight_apart (H : Simple5Hypergraph (Fin 21)) (x u : Fin 21)
    (dx : H.degree x=7) (hu : u∈eights H) : x≠u := by
  have du : H.degree u=8 := (Finset.mem_filter.mp hu).2
  intro eq
  rw [eq] at dx
  omega

theorem cross_bounds (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀ i,H.degree (f i)=7) :
    ∀ i,∀ u∈eights H,1≤H.codegree (f i) u ∧ H.codegree (f i) u≤2 := by
  intro i u hu
  have other : ∀ i : Fin 3,∃ j : Fin 3,i≠j := by decide
  obtain ⟨j,ij⟩ := other i
  have iu := eight_apart H (f i) u (degrees i) hu
  have ju := eight_apart H (f j) u (degrees j) hu
  let t := threeVertices (f i) (f j) u (f.injective.ne ij) iu ju
  have du : H.degree u=8 := (Finset.mem_filter.mp hu).2
  have ds : ∀ k,H.degree (t k)=(![7,7,8] : Fin 3→ℕ) k := by
    intro k
    fin_cases k <;> simp [t,threeVertices,degrees,du]
  exact ⟨H.one_le_codegree cover iu,(TwentyOneSevenTriples.residual778 H cover size noB t ds).2.1⟩

theorem pattern_partition (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (u : Fin 21) (bounds : ∀ i,1≤H.codegree (f i) u ∧ H.codegree (f i) u≤2) :
    (pattern H f u).card+(∑ i : Fin 3,(H.codegree (f i) u-1))=3 := by
  have each (i : Fin 3) : (if H.codegree (f i) u=1 then 1 else 0)+
      (H.codegree (f i) u-1)=1 := by
    have bound := bounds i
    split_ifs <;> omega
  calc
    _ = ∑ i : Fin 3,((if H.codegree (f i) u=1 then 1 else 0)+(H.codegree (f i) u-1)) := by
      simp only [pattern,Finset.card_eq_sum_ones,Finset.sum_filter,Finset.sum_add_distrib]
    _ = 3 := by simp_rw [each];decide

theorem external_excess_le_twenty_four (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (f : Fin 3↪Fin 21) (degrees : ∀ i,H.degree (f i)=7) :
    (∑ u∈eights H,∑ i : Fin 3,(H.codegree (f i) u-1))≤24 := by
  have each (i : Fin 3) : (∑ u∈eights H,(H.codegree (f i) u-1))≤8 := by
    calc
      _ ≤ ∑ u∈Finset.univ.erase (f i),(H.codegree (f i) u-1) :=
        Finset.sum_le_sum_of_subset (eights_subset_erase H (f i) (degrees i))
      _ = 8 := by rw [H.sum_codegree_excess cover (f i),degrees i];norm_num
  rw [Finset.sum_comm]
  calc
    _ ≤ ∑ i : Fin 3,8 := Finset.sum_le_sum (fun i _ => each i)
    _ = 24 := by decide

theorem pattern_total (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (bounds : ∀ i,∀ u∈eights H,1≤H.codegree (f i) u ∧ H.codegree (f i) u≤2) :
    (∑ u∈eights H,(pattern H f u).card)+
      (∑ u∈eights H,∑ i : Fin 3,(H.codegree (f i) u-1))=3*(eights H).card := by
  rw [←Finset.sum_add_distrib]
  calc
    _ = ∑ u∈eights H,3 := Finset.sum_congr rfl (fun u hu => pattern_partition H f u (fun i => bounds i u hu))
    _ = _ := by simp [Nat.mul_comm]

theorem same_pattern_codegrees (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (u v : Fin 21) (same : pattern H f u=pattern H f v)
    (bu : ∀ i,1≤H.codegree (f i) u ∧ H.codegree (f i) u≤2)
    (bv : ∀ i,1≤H.codegree (f i) v ∧ H.codegree (f i) v≤2) :
    ∀ i,H.codegree (f i) u=H.codegree (f i) v := by
  intro i
  have iff : H.codegree (f i) u=1 ↔ H.codegree (f i) v=1 := by
    rw [←mem_pattern,←mem_pattern,same]
  have lo := bu i
  have hi := bv i
  omega

/-- The repeated eight-degree vertices actually have mutual codegree exactly
2: the common seven-degree center has at least five unit eight-neighbors. -/
theorem matching_eights (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀ i,H.degree (f i)=7) (many : 13≤(eights H).card) :
    ∃ u∈eights H,∃ v∈eights H,u≠v ∧
      (∀ i,H.codegree (f i) u=H.codegree (f i) v) ∧
      (∃ i,H.codegree (f i) u=1) ∧ H.codegree u v=2 := by
  have bounds := cross_bounds H cover size noB f degrees
  have total := pattern_total H f bounds
  have excess := external_excess_le_twenty_four H cover f degrees
  have large : 12<∑ u∈eights H,(pattern H f u).card := by omega
  obtain ⟨u,hu,v,hv,ne,same,i,member⟩ := repeated_nonempty (eights H) (pattern H f) large
  have unitU : H.codegree (f i) u=1 := (mem_pattern H f u i).mp member
  have matched := same_pattern_codegrees H f u v same (fun i => bounds i u hu) (fun i => bounds i v hv)
  have unitV : H.codegree (f i) v=1 := (matched i).symm.trans unitU
  have budget := unit_eights_budget H cover (f i) (degrees i)
  have enough : 3≤(unitEights H (f i)).card := by omega
  have pairStructure := (unit_eights_structure H cover size noB (f i) (degrees i) enough).1
  exact ⟨u,hu,v,hv,ne,matched,⟨i,unitU⟩,
    pairStructure u (Finset.mem_filter.mpr ⟨hu,unitU⟩) v (Finset.mem_filter.mpr ⟨hv,unitV⟩) ne⟩

/-- Start with the original exactly-three-sevens hypothesis, rather than an
assumed local embedding or a supplied low-degree pattern. -/
theorem select (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x,7≤H.degree x) (noB : ¬PropertyB H)
    (three : (sevens H).card=3) :
    ∃ f : Fin 3↪Fin 21,(∀ i,H.degree (f i)=7) ∧
      (∀ i,∀ u∈eights H,1≤H.codegree (f i) u ∧ H.codegree (f i) u≤2) ∧
      ∃ u∈eights H,∃ v∈eights H,u≠v ∧
        (∀ i,H.codegree (f i) u=H.codegree (f i) v) ∧
        (∃ i,H.codegree (f i) u=1) ∧ H.codegree u v=2 := by
  classical
  let S := sevens H
  let e : ↥S ≃ Fin 3 := Fintype.equivFinOfCardEq (by simpa [S] using three)
  let f : Fin 3↪Fin 21 := ⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩
  have degrees (i : Fin 3) : H.degree (f i)=7 := (Finset.mem_filter.mp (e.symm i).property).2
  have budget := degree_count_budget H size minimum
  rw [three] at budget
  exact ⟨f,degrees,cross_bounds H cover size noB f degrees,
    matching_eights H cover size noB f degrees (by omega)⟩

end Aris4Math.ThirtyFour.TwentyOneSevenThreeSelection
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelection.select
