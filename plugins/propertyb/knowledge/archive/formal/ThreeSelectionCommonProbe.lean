import Aris4Math.ThirtyFour.TwentyOneSevenSelection
import Aris4Math.ThirtyFour.TwentyOneSevenTriples

/-! Weighted pigeonhole bounds for three actual seven-degree vertices.
The finite constants 12 and 9 count the eight subsets of Fin 3 only. -/
namespace Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights
open scoped BigOperators
variable {α β : Type*} [DecidableEq α] [DecidableEq β] [Fintype β]

theorem weighted_bound (S : Finset α) (pattern : α → β) (weight : β → ℕ)
    (unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y → weight (pattern x)=0) :
    (∑ x∈S,weight (pattern x))≤∑ b : β,weight b := by
  have image : (∑ b∈S.image pattern,weight b)=∑ x∈S,weight (pattern x) :=
    Finset.sum_image_of_pairwise_eq_zero unique
  rw [← image]
  exact Finset.sum_le_sum_of_subset (Finset.subset_univ _)

theorem repeated_of_weight (S : Finset α) (pattern : α → β) (weight : β → ℕ)
    (large : (∑ b : β,weight b)<∑ x∈S,weight (pattern x)) :
    ∃ x∈S,∃ y∈S,x≠y ∧ pattern x=pattern y ∧ 0<weight (pattern x) := by
  by_contra no
  have unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y → weight (pattern x)=0 := by
    intro x hx y hy ne same
    by_contra positive
    exact no ⟨x,hx,y,hy,ne,same,Nat.pos_of_ne_zero positive⟩
  exact (not_lt_of_ge (weighted_bound S pattern weight unique)) large

theorem subsets_weight : (∑ P : Finset (Fin 3),P.card)=12 := by decide +kernel

theorem repeated_nonempty (S : Finset α) (pattern : α → Finset (Fin 3))
    (large : 12<∑ x∈S,(pattern x).card) :
    ∃ x∈S,∃ y∈S,x≠y ∧ pattern x=pattern y ∧ (pattern x).Nonempty := by
  rw [← subsets_weight] at large
  obtain ⟨x,hx,y,hy,ne,same,pos⟩ := repeated_of_weight S pattern Finset.card large
  exact ⟨x,hx,y,hy,ne,same,Finset.card_pos.mp pos⟩

def properWeight (P : Finset (Fin 3)) : ℕ := if P=Finset.univ then 0 else P.card

theorem proper_weight : (∑ P : Finset (Fin 3),properWeight P)=9 := by decide +kernel

theorem full_pattern_bound (S : Finset α) (pattern : α → Finset (Fin 3))
    (unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y →
      (pattern x).Nonempty → pattern x=Finset.univ) :
    (∑ x∈S,(pattern x).card)≤9+3*(S.filter fun x => pattern x=Finset.univ).card := by
  have proper : (∑ x∈S,properWeight (pattern x))≤9 := by
    rw [← proper_weight]
    apply weighted_bound S pattern properWeight
    intro x hx y hy ne same
    by_cases empty : pattern x=∅
    · simp [properWeight,empty]
    · have full := unique x hx y hy ne same (Finset.nonempty_iff_ne_empty.mpr empty)
      simp [properWeight,full]
  have each (x : α) : (pattern x).card=properWeight (pattern x)+
      if pattern x=Finset.univ then 3 else 0 := by
    by_cases full : pattern x=Finset.univ
    · simp [properWeight,full]
    · simp [properWeight,full]
  have totals : (∑ x∈S,(pattern x).card)=(∑ x∈S,properWeight (pattern x))+
      3*(S.filter fun x => pattern x=Finset.univ).card := by
    simp_rw [each,Finset.sum_add_distrib]
    rw [←Finset.sum_filter]
    simp [Nat.mul_comm]
  omega

end Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights.repeated_nonempty
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights.full_pattern_bound

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

/-! Stronger actual budget after the remaining five-lock residues force the
three internal seven-pairs to be double and every repeated nonempty pattern
of eight-degree points to be fully unit. These residue hypotheses are explicit. -/
namespace Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionCommon
open scoped BigOperators
open TwentyOneSevenSelection TwentyOneSevenThreeSelectionWeights
open TwentyOneSevenThreeSelection

theorem excess_le_six (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=7) (dy : H.degree y=7) (dz : H.degree z=7)
    (doubleY : H.codegree x y=2) (doubleZ : H.codegree x z=2) :
    (∑ u∈eights H,(H.codegree x u-1))≤6 := by
  have yn : y∉eights H := by intro hy;have := (Finset.mem_filter.mp hy).2;omega
  have zn : z∉eights H := by intro hz;have := (Finset.mem_filter.mp hz).2;omega
  have yin : y∉insert z (eights H) := by simp only [Finset.mem_insert,not_or];exact ⟨yz,yn⟩
  have sub : insert y (insert z (eights H))⊆Finset.univ.erase x := by
    apply Finset.insert_subset
    · exact Finset.mem_erase.mpr ⟨xy.symm,Finset.mem_univ _⟩
    apply Finset.insert_subset
    · exact Finset.mem_erase.mpr ⟨xz.symm,Finset.mem_univ _⟩
    exact eights_subset_erase H x dx
  have upper : (∑ u∈insert y (insert z (eights H)),(H.codegree x u-1))≤8 := by
    calc
      _ ≤ ∑ u∈Finset.univ.erase x,(H.codegree x u-1) := Finset.sum_le_sum_of_subset sub
      _ = 8 := by rw [H.sum_codegree_excess cover x,dx];norm_num
  rw [Finset.sum_insert yin,Finset.sum_insert zn,doubleY,doubleZ] at upper
  omega

theorem external_excess_le_eighteen (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (f : Fin 3↪Fin 21) (degrees : ∀ i,H.degree (f i)=7)
    (internal : ∀ i j,i≠j→H.codegree (f i) (f j)=2) :
    (∑ u∈eights H,∑ i : Fin 3,(H.codegree (f i) u-1))≤18 := by
  have each (i : Fin 3) : (∑ u∈eights H,(H.codegree (f i) u-1))≤6 := by
    have others : ∀ i : Fin 3,∃ j k : Fin 3,i≠j ∧ i≠k ∧ j≠k := by decide
    obtain ⟨j,k,ij,ik,jk⟩ := others i
    exact excess_le_six H cover (f i) (f j) (f k) (f.injective.ne ij)
      (f.injective.ne ik) (f.injective.ne jk) (degrees i) (degrees j) (degrees k)
      (internal i j ij) (internal i k ik)
  rw [Finset.sum_comm]
  calc
    _ ≤ ∑ i : Fin 3,6 := Finset.sum_le_sum (fun i _ => each i)
    _ = 18 := by decide

def commonUnitEights (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21) : Finset (Fin 21) :=
  (eights H).filter fun u => pattern H f u=Finset.univ

@[simp] theorem mem_commonUnitEights (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (u : Fin 21) : u∈commonUnitEights H f ↔ u∈eights H ∧ ∀ i,H.codegree (f i) u=1 := by
  simp only [commonUnitEights,Finset.mem_filter,Finset.eq_univ_iff_forall,mem_pattern]

theorem four_common (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀ i,H.degree (f i)=7) (many : 13≤(eights H).card)
    (internal : ∀ i j,i≠j→H.codegree (f i) (f j)=2)
    (residues : ∀ u∈eights H,∀ v∈eights H,u≠v →
      (∀ i,H.codegree (f i) u=H.codegree (f i) v) →
      (∃ i,H.codegree (f i) u=1) → ∀ i,H.codegree (f i) u=1) :
    4≤(commonUnitEights H f).card ∧
      (∀ u∈commonUnitEights H f,H.degree u=8 ∧ ∀ i,H.codegree (f i) u=1) ∧
      (∀ u∈commonUnitEights H f,∀ v∈commonUnitEights H f,u≠v→H.codegree u v=2) := by
  have bounds := cross_bounds H cover size noB f degrees
  have total := pattern_total H f bounds
  have excess := external_excess_le_eighteen H cover f degrees internal
  have unique : ∀ u∈eights H,∀ v∈eights H,u≠v → pattern H f u=pattern H f v →
      (pattern H f u).Nonempty → pattern H f u=Finset.univ := by
    intro u hu v hv ne same nonempty
    have eq := same_pattern_codegrees H f u v same (fun i => bounds i u hu) (fun i => bounds i v hv)
    obtain ⟨i,member⟩ := nonempty
    have all := residues u hu v hv ne eq ⟨i,(mem_pattern H f u i).mp member⟩
    apply Finset.eq_univ_iff_forall.mpr
    intro i
    exact (mem_pattern H f u i).mpr (all i)
  have upper := full_pattern_bound (eights H) (pattern H f) unique
  have four : 4≤(commonUnitEights H f).card := by
    change 4≤((eights H).filter fun u => pattern H f u=Finset.univ).card
    omega
  have singleBudget := unit_eights_budget H cover (f 0) (degrees 0)
  have unitMany : 3≤(unitEights H (f 0)).card := by omega
  have structurePairs := (unit_eights_structure H cover size noB (f 0) (degrees 0) unitMany).1
  refine ⟨four,?_,?_⟩
  · intro u hu
    obtain ⟨eight,units⟩ := (mem_commonUnitEights H f u).mp hu
    exact ⟨(Finset.mem_filter.mp eight).2,units⟩
  · intro u hu v hv ne
    obtain ⟨eightU,unitsU⟩ := (mem_commonUnitEights H f u).mp hu
    obtain ⟨eightV,unitsV⟩ := (mem_commonUnitEights H f v).mp hv
    exact structurePairs u (Finset.mem_filter.mpr ⟨eightU,unitsU 0⟩)
      v (Finset.mem_filter.mpr ⟨eightV,unitsV 0⟩) ne

end Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionCommon
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionCommon.four_common
