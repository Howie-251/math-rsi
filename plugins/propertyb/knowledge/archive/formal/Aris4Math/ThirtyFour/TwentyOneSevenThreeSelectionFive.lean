import Aris4Math.ThirtyFour.TwentyOneSevenThreeSelection

/-! Package the actual selected triple and repeated eight-degree pair as five
real distinct locks, retaining all codegree conditions needed by the catalogue. -/
namespace Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionFive
open TwentyOneSevenSelection TwentyOneSevenThreeSelection

/-- This applies to any pair sharing a unit seven-center, not just the pair
chosen by weighted pigeonhole. It is also used for every residual projection. -/
theorem pair_eq_two (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (many : 13≤(eights H).card)
    (x u v : Fin 21) (dx : H.degree x=7) (hu : u∈eights H) (hv : v∈eights H)
    (ne : u≠v) (xu : H.codegree x u=1) (xv : H.codegree x v=1) : H.codegree u v=2 := by
  have budget := unit_eights_budget H cover x dx
  have enough : 3≤(unitEights H x).card := by omega
  exact (unit_eights_structure H cover size noB x dx enough).1
    u (Finset.mem_filter.mpr ⟨hu,xu⟩) v (Finset.mem_filter.mpr ⟨hv,xv⟩) ne

theorem internal_bounds (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀ i,H.degree (f i)=7) : ∀ i j,i≠j→H.codegree (f i) (f j)≤2 := by
  have ds : ∀ i,H.degree (f i)=(![7,7,7] : Fin 3→ℕ) i := by
    intro i;fin_cases i <;> exact degrees _
  obtain ⟨h01,h02,h12⟩ := TwentyOneSevenTriples.residual777 H cover size noB f ds
  intro i j ne
  fin_cases i <;> fin_cases j
  all_goals first
    | exact False.elim (ne rfl)
    | exact h01
    | exact h02
    | exact h12
    | exact (H.codegree_comm _ _).trans_le h01
    | exact (H.codegree_comm _ _).trans_le h02
    | exact (H.codegree_comm _ _).trans_le h12

def first (i : Fin 3) : Fin 5 := i.castSucc.castSucc

theorem package (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀ i,H.degree (f i)=7)
    (u v : Fin 21) (hu : u∈eights H) (hv : v∈eights H) (uv : u≠v)
    (same : ∀ i,H.codegree (f i) u=H.codegree (f i) v)
    (unit : ∃ i,H.codegree (f i) u=1) (double : H.codegree u v=2) :
    ∃ g : Fin 5↪Fin 21,(∀ i,H.degree (g i)=(![7,7,7,8,8] : Fin 5→ℕ) i) ∧
      (∀ i,H.codegree (g (first i)) (g 3)=H.codegree (g (first i)) (g 4)) ∧
      (∃ i,H.codegree (g (first i)) (g 3)=1) ∧ H.codegree (g 3) (g 4)=2 ∧
      (∀ i j,i≠j→H.codegree (g i) (g j)≤2) := by
  have du : H.degree u=8 := (Finset.mem_filter.mp hu).2
  have dv : H.degree v=8 := (Finset.mem_filter.mp hv).2
  have uOutside : u∉Set.range f := by
    rintro ⟨i,eq⟩
    exact eight_apart H (f i) u (degrees i) hu eq
  let g4 : Fin 4↪Fin 21 := ⟨Fin.snoc f u,Fin.snoc_injective_of_injective f.injective uOutside⟩
  have vOutside : v∉Set.range g4 := by
    rintro ⟨i,eq⟩
    refine Fin.lastCases ?_ (fun j => ?_) i eq
    · change u=v→False
      exact uv
    · simpa [g4] using eight_apart H (f j) v (degrees j) hv
  let g : Fin 5↪Fin 21 := ⟨Fin.snoc g4 v,Fin.snoc_injective_of_injective g4.injective vOutside⟩
  have old (i : Fin 3) : g (first i)=f i := by simp [g,g4,first]
  have gu : g 3=u := by simp [g,g4,Fin.snoc]
  have gv : g 4=v := by simp [g,g4,Fin.snoc]
  have dg : ∀ i,H.degree (g i)=(![7,7,7,8,8] : Fin 5→ℕ) i := by
    intro i
    fin_cases i
    · exact degrees 0
    · exact degrees 1
    · exact degrees 2
    · exact du
    · exact dv
  have core := internal_bounds H cover size noB f degrees
  have cross := cross_bounds H cover size noB f degrees
  have h01 : H.codegree (g 0) (g 1)≤2 := core 0 1 (by decide)
  have h02 : H.codegree (g 0) (g 2)≤2 := core 0 2 (by decide)
  have h12 : H.codegree (g 1) (g 2)≤2 := core 1 2 (by decide)
  have h03 : H.codegree (g 0) (g 3)≤2 := (cross 0 u hu).2
  have h04 : H.codegree (g 0) (g 4)≤2 := (cross 0 v hv).2
  have h13 : H.codegree (g 1) (g 3)≤2 := (cross 1 u hu).2
  have h14 : H.codegree (g 1) (g 4)≤2 := (cross 1 v hv).2
  have h23 : H.codegree (g 2) (g 3)≤2 := (cross 2 u hu).2
  have h24 : H.codegree (g 2) (g 4)≤2 := (cross 2 v hv).2
  have h34 : H.codegree (g 3) (g 4)≤2 := double.le
  refine ⟨g,dg,?_,?_,double,?_⟩
  · intro i
    rw [old,gu,gv]
    exact same i
  · obtain ⟨i,hi⟩ := unit
    exact ⟨i,by rw [old,gu];exact hi⟩
  · intro i j ne
    fin_cases i <;> fin_cases j
    all_goals first
      | exact False.elim (ne rfl)
      | assumption
      | exact (H.codegree_comm _ _).trans_le h01
      | exact (H.codegree_comm _ _).trans_le h02
      | exact (H.codegree_comm _ _).trans_le h12
      | exact (H.codegree_comm _ _).trans_le h03
      | exact (H.codegree_comm _ _).trans_le h04
      | exact (H.codegree_comm _ _).trans_le h13
      | exact (H.codegree_comm _ _).trans_le h14
      | exact (H.codegree_comm _ _).trans_le h23
      | exact (H.codegree_comm _ _).trans_le h24
      | exact (H.codegree_comm _ _).trans_le h34

theorem select_five (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x,7≤H.degree x) (noB : ¬PropertyB H)
    (three : (sevens H).card=3) :
    ∃ g : Fin 5↪Fin 21,(∀ i,H.degree (g i)=(![7,7,7,8,8] : Fin 5→ℕ) i) ∧
      (∀ i,H.codegree (g (first i)) (g 3)=H.codegree (g (first i)) (g 4)) ∧
      (∃ i,H.codegree (g (first i)) (g 3)=1) ∧ H.codegree (g 3) (g 4)=2 ∧
      (∀ i j,i≠j→H.codegree (g i) (g j)≤2) := by
  obtain ⟨f,degrees,_,u,hu,v,hv,ne,same,unit,double⟩ := select H cover size minimum noB three
  exact package H cover size noB f degrees u v hu hv ne same unit double

end Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionFive
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionFive.select_five
