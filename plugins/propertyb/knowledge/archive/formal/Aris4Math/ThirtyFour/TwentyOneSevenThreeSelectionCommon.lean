import Aris4Math.ThirtyFour.TwentyOneSevenThreeSelection

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
