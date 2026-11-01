import Aris4Math.ThirtyThree.TwentyThreeDefectSelection

/-!
Actual high-degree lock selection for the no-six-degree branch on 23 vertices.
Known internal codegree excess is charged before choosing outside unit neighbors.
-/
namespace Aris4Math.ThirtyThree.TwentyThreeHighSelection

open scoped BigOperators
open TwentyThreeSelection
variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Charge all known internal excess before counting remaining bad neighbors. -/
theorem seven_outside_bad_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (x : V) (degree : H.degree x = 7)
    (T : Finset V) (apart : x ∉ T) :
    (H.badPartners x \ T).card + (∑ y ∈ T, (H.codegree x y - 1)) ≤ 6 := by
  let A := H.badPartners x \ T
  have disjoint : Disjoint A T := Finset.sdiff_disjoint
  have sub : A ∪ T ⊆ Finset.univ.erase x := by
    intro y hy
    rcases Finset.mem_union.mp hy with hA | hT
    · exact (Finset.mem_filter.mp (Finset.mem_sdiff.mp hA).1).1
    · exact Finset.mem_erase.mpr ⟨fun h => apart (h ▸ hT),Finset.mem_univ y⟩
  have lower : A.card ≤ ∑ y ∈ A, (H.codegree x y - 1) := by
    calc
      _ = ∑ _y ∈ A, (1 : ℕ) := by simp
      _ ≤ _ := by
        apply Finset.sum_le_sum
        intro y hy
        have hbad := (Finset.mem_filter.mp (Finset.mem_sdiff.mp hy).1).2
        omega
  have sumBound := Finset.sum_le_sum_of_subset sub (f := fun y => H.codegree x y - 1)
  rw [Finset.sum_union disjoint,H.sum_codegree_excess cover x,vertices,degree] at sumBound
  change A.card + (∑ y ∈ T, (H.codegree x y - 1)) ≤ 6
  omega

theorem high_three_bad_erase_le_four (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) {x y : V} (degree : H.degree x = 7)
    (xy : x ≠ y) (codegree : H.codegree x y = 3) :
    ((H.badPartners x).erase y).card ≤ 4 := by
  have h := seven_outside_bad_budget H cover vertices x degree {y} (by simpa using xy)
  simpa [Finset.sdiff_singleton_eq_erase,codegree] using h

/-- Two degree-seven vertices of codegree three have nine high vertices
unit to both. This spends their two units of mutual excess first. -/
theorem high_three_unit_pool (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 19 ≤ (sevenVertices H).card)
    (x y : V) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (xy : x ≠ y) (codegree : H.codegree x y = 3) :
    ∃ P : Finset V, 9 ≤ P.card ∧ ∀ a ∈ P,
      H.degree a = 7 ∧ a ≠ x ∧ a ≠ y ∧
        H.codegree x a = 1 ∧ H.codegree y a = 1 := by
  let A := (H.badPartners x).erase y
  let B := (H.badPartners y).erase x
  let F := insert x (insert y (A ∪ B))
  let P := sevenVertices H \ F
  have A4 : A.card ≤ 4 := high_three_bad_erase_le_four H cover vertices dx xy codegree
  have B4 : B.card ≤ 4 := high_three_bad_erase_le_four H cover vertices dy xy.symm
    ((H.codegree_comm y x).trans codegree)
  have F10 : F.card ≤ 10 := by
    have hu := Finset.card_union_le A B
    have hy := Finset.card_insert_le y (A ∪ B)
    have hx := Finset.card_insert_le x (insert y (A ∪ B))
    dsimp [F]
    omega
  have P9 : 9 ≤ P.card := by
    have h := Finset.card_le_card_sdiff_add_card (s := sevenVertices H) (t := F)
    change (sevenVertices H).card ≤ P.card + F.card at h
    omega
  refine ⟨P,P9,?_⟩
  intro a ha
  obtain ⟨ha7,haF⟩ := Finset.mem_sdiff.mp ha
  have da : H.degree a = 7 := (mem_sevenVertices H a).mp ha7
  have ax : a ≠ x := fun h => haF (h ▸ Finset.mem_insert_self x _)
  have ay : a ≠ y := fun h => haF
    (h ▸ Finset.mem_insert_of_mem (Finset.mem_insert_self y _))
  have anotx : a ∉ H.badPartners x := by
    intro h
    exact haF (Finset.mem_insert_of_mem (Finset.mem_insert_of_mem
      (Finset.mem_union_left B (Finset.mem_erase.mpr ⟨ay,h⟩))))
  have anoty : a ∉ H.badPartners y := by
    intro h
    exact haF (Finset.mem_insert_of_mem (Finset.mem_insert_of_mem
      (Finset.mem_union_right A (Finset.mem_erase.mpr ⟨ax,h⟩))))
  have goodx : a ∈ H.goodPartners x := Finset.mem_sdiff.mpr
    ⟨Finset.mem_univ a,by simpa only [Finset.mem_insert,not_or] using And.intro ax anotx⟩
  have goody : a ∈ H.goodPartners y := Finset.mem_sdiff.mpr
    ⟨Finset.mem_univ a,by simpa only [Finset.mem_insert,not_or] using And.intro ay anoty⟩
  exact ⟨da,ax,ay,((H.mem_goodPartners cover x a).mp goodx).2,
    ((H.mem_goodPartners cover y a).mp goody).2⟩

/-- The actual four high locks used to rule out a codegree-three pair. -/
theorem exists_four_high_of_three (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 19 ≤ (sevenVertices H).card)
    (x y : V) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (xy : x ≠ y) (codegree : H.codegree x y = 3) :
    ∃ f : Fin 4 → V, Function.Injective f ∧ f 0 = x ∧ f 1 = y ∧
      (∀ i, H.degree (f i) = 7) ∧ H.codegree (f 0) (f 1) = 3 ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → H.codegree (f i) (f j) = 1) := by
  obtain ⟨P,P9,facts⟩ := high_three_unit_pool H cover vertices many x y dx dy xy codegree
  obtain ⟨u,hu,_v,_hv,w,hw,_,uw,_,cuw,_⟩ :=
    exists_three_sevens_two_unit H cover vertices P (fun a ha => (facts a ha).1) P9
  obtain ⟨du,ux,uy,cxu,cyu⟩ := facts u hu
  obtain ⟨dw,wx,wy,cxw,cyw⟩ := facts w hw
  let f : Fin 4 → V := ![x,y,u,w]
  have finj : Function.Injective f := by
    intro i j heq
    fin_cases i <;> fin_cases j <;>
      simp [f,xy,xy.symm,ux,ux.symm,uy,uy.symm,wx,wx.symm,wy,wy.symm,uw,uw.symm] at heq <;> rfl
  refine ⟨f,finj,rfl,rfl,?_,codegree,?_⟩
  · intro i
    fin_cases i <;> simp [f,dx,dy,du,dw]
  · intro i j hij h01
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;>
      simp [Fin.ext_iff] at h01 <;>
      first | exact cxu | exact cxw | exact cyu | exact cyw | exact cuw

/-- An induced high-degree path spends four internal bad adjacencies. Its
outside bad-neighbor union therefore excludes at most fourteen high points. -/
theorem high_path_unit_pool (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 19 ≤ (sevenVertices H).card)
    (x y z : V) (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 1)
    (cyz : H.codegree y z = 2) :
    ∃ P : Finset V, 2 ≤ P.card ∧ ∀ a ∈ P,
      H.degree a = 7 ∧ a ≠ x ∧ a ≠ y ∧ a ≠ z ∧
        H.codegree x a = 1 ∧ H.codegree y a = 1 ∧ H.codegree z a = 1 := by
  let A := H.badPartners x \ {y,z}
  let B := H.badPartners y \ {x,z}
  let C := H.badPartners z \ {x,y}
  let F := insert x (insert y (insert z ((A ∪ B) ∪ C)))
  let P := sevenVertices H \ F
  have A5 : A.card ≤ 5 := by
    have h := seven_outside_bad_budget H cover vertices x dx {y,z} (by simp [xy,xz])
    simpa [Finset.sum_insert,Finset.sum_singleton,yz,cxy,cxz] using h
  have B4 : B.card ≤ 4 := by
    have h := seven_outside_bad_budget H cover vertices y dy {x,z} (by simp [xy.symm,yz])
    have cyx : H.codegree y x = 2 := (H.codegree_comm y x).trans cxy
    simpa [Finset.sum_insert,Finset.sum_singleton,xz,cyx,cyz] using h
  have C5 : C.card ≤ 5 := by
    have h := seven_outside_bad_budget H cover vertices z dz {x,y} (by simp [xz.symm,yz.symm])
    have czx : H.codegree z x = 1 := (H.codegree_comm z x).trans cxz
    have czy : H.codegree z y = 2 := (H.codegree_comm z y).trans cyz
    simpa [Finset.sum_insert,Finset.sum_singleton,xy,czx,czy] using h
  have F17 : F.card ≤ 17 := by
    have hAB := Finset.card_union_le A B
    have hABC := Finset.card_union_le (A ∪ B) C
    have hz := Finset.card_insert_le z ((A ∪ B) ∪ C)
    have hy := Finset.card_insert_le y (insert z ((A ∪ B) ∪ C))
    have hx := Finset.card_insert_le x (insert y (insert z ((A ∪ B) ∪ C)))
    dsimp [F]
    omega
  have P2 : 2 ≤ P.card := by
    have h := Finset.card_le_card_sdiff_add_card (s := sevenVertices H) (t := F)
    change (sevenVertices H).card ≤ P.card + F.card at h
    omega
  refine ⟨P,P2,?_⟩
  intro a ha
  obtain ⟨ha7,haF⟩ := Finset.mem_sdiff.mp ha
  have da : H.degree a = 7 := (mem_sevenVertices H a).mp ha7
  have outside : a ≠ x ∧ a ≠ y ∧ a ≠ z ∧ a ∉ (A ∪ B) ∪ C := by
    simpa only [F,Finset.mem_insert,not_or,and_assoc] using haF
  obtain ⟨ax,ay,az,notABC⟩ := outside
  have anotx : a ∉ H.badPartners x := by
    intro h
    exact notABC (Finset.mem_union_left C (Finset.mem_union_left B
      (Finset.mem_sdiff.mpr ⟨h,by simp [ay,az]⟩)))
  have anoty : a ∉ H.badPartners y := by
    intro h
    exact notABC (Finset.mem_union_left C (Finset.mem_union_right A
      (Finset.mem_sdiff.mpr ⟨h,by simp [ax,az]⟩)))
  have anotz : a ∉ H.badPartners z := by
    intro h
    exact notABC (Finset.mem_union_right (A ∪ B)
      (Finset.mem_sdiff.mpr ⟨h,by simp [ax,ay]⟩))
  have good (p : V) (ap : a ≠ p) (notbad : a ∉ H.badPartners p) : H.codegree p a = 1 := by
    have h : a ∈ H.goodPartners p := Finset.mem_sdiff.mpr
      ⟨Finset.mem_univ a,by simpa only [Finset.mem_insert,not_or] using And.intro ap notbad⟩
    exact ((H.mem_goodPartners cover p a).mp h).2
  exact ⟨da,ax,ay,az,good x ax anotx,good y ay anoty,good z az anotz⟩

/-- The five high locks produced by an actual induced codegree-two path.
The final pair 34 is left for the high-pair exclusion or the 1/2 table. -/
theorem exists_five_high_of_path (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 19 ≤ (sevenVertices H).card)
    (x y z : V) (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 1)
    (cyz : H.codegree y z = 2) :
    ∃ f : Fin 5 → V, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
      H.codegree (f 0) (f 1) = 2 ∧ H.codegree (f 1) (f 2) = 2 ∧
      H.codegree (f 0) (f 2) = 1 ∧
      (∀ i j, i.val < 3 → 3 ≤ j.val → H.codegree (f i) (f j) = 1) := by
  obtain ⟨P,P2,facts⟩ := high_path_unit_pool H cover vertices many
    x y z dx dy dz xy xz yz cxy cxz cyz
  obtain ⟨u,hu,v,hv,uv⟩ := Finset.one_lt_card.mp (show 1 < P.card by omega)
  obtain ⟨du,ux,uy,uz,cxu,cyu,czu⟩ := facts u hu
  obtain ⟨dv,vx,vy,vz,cxv,cyv,czv⟩ := facts v hv
  let f : Fin 5 → V := ![x,y,z,u,v]
  have finj : Function.Injective f := by
    intro i j heq
    fin_cases i <;> fin_cases j <;>
      simp [f,xy,xy.symm,xz,xz.symm,yz,yz.symm,ux,ux.symm,uy,uy.symm,uz,uz.symm,
        vx,vx.symm,vy,vy.symm,vz,vz.symm,uv,uv.symm] at heq <;> rfl
  refine ⟨f,finj,?_,cxy,cyz,cxz,?_⟩
  · intro i
    fin_cases i <;> simp [f,dx,dy,dz,du,dv]
  · intro i j hi hj
    fin_cases i <;> fin_cases j <;> norm_num at hi <;> norm_num at hj <;>
      first | exact cxu | exact cxv | exact cyu | exact cyv | exact czu | exact czv

end Aris4Math.ThirtyThree.TwentyThreeHighSelection

#print axioms Aris4Math.ThirtyThree.TwentyThreeHighSelection.exists_four_high_of_three
#print axioms Aris4Math.ThirtyThree.TwentyThreeHighSelection.exists_five_high_of_path
