import Aris4Math.ThirtyThree.TwentyThreeColoredSelection
import Mathlib.Data.Finset.Max

/-!
The four-part defect-one selection used when the unique six-degree vertex is
unit-codegree to every seven-degree vertex. The partition is obtained by
minimizing monochromatic edges, without enumerating graphs.
-/
namespace Aris4Math.ThirtyThree.TwentyThreeDefectSelection

open scoped BigOperators
open TwentyThreeColoredSelection TwentyThreeSelection
variable {V : Type*} [Fintype V] [DecidableEq V]

def colorNeighbors (R : V → V → Prop) [DecidableRel R]
    (color : V → Fin 4) (x : V) (k : Fin 4) : Finset V :=
  Finset.univ.filter fun y => R x y ∧ color y = k

def weight (R : V → V → Prop) [DecidableRel R]
    (color : V → Fin 4) (x y : V) : ℕ :=
  if R x y ∧ color x = color y then 1 else 0

def energy (R : V → V → Prop) [DecidableRel R] (color : V → Fin 4) : ℕ :=
  ∑ x : V, ∑ y : V, weight R color x y

def restEnergy (R : V → V → Prop) [DecidableRel R] (color : V → Fin 4) (x : V) : ℕ :=
  ∑ u ∈ Finset.univ.erase x, ∑ v ∈ Finset.univ.erase x, weight R color u v

omit [Fintype V] [DecidableEq V] in
theorem weight_symm (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) (color : V → Fin 4) (x y : V) :
    weight R color x y = weight R color y x := by
  have h : R x y ↔ R y x := ⟨symmetric x y,symmetric y x⟩
  simp only [weight,h,eq_comm]

omit [DecidableEq V] in
theorem row_sum (R : V → V → Prop) [DecidableRel R]
    (color : V → Fin 4) (x : V) :
    (∑ y : V, weight R color x y) = (colorNeighbors R color x (color x)).card := by
  simp [weight,colorNeighbors,eq_comm]

theorem energy_at_vertex (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) (irreflexive : ∀ x, ¬ R x x)
    (color : V → Fin 4) (x : V) :
    energy R color = restEnergy R color x +
      2 * (colorNeighbors R color x (color x)).card := by
  have zero : weight R color x x = 0 := by simp [weight,irreflexive x]
  have rowErase := Finset.sum_erase_add (s := Finset.univ)
    (fun y => weight R color x y) (Finset.mem_univ x)
  dsimp only at rowErase
  rw [zero,Nat.add_zero,row_sum] at rowErase
  have column : (∑ u ∈ Finset.univ.erase x, weight R color u x) =
      (colorNeighbors R color x (color x)).card := by
    calc
      _ = ∑ u ∈ Finset.univ.erase x, weight R color x u :=
        Finset.sum_congr rfl (fun u _ => weight_symm R symmetric color u x)
      _ = _ := rowErase
  have outer := Finset.sum_erase_add (s := Finset.univ)
    (fun u => ∑ v : V, weight R color u v) (Finset.mem_univ x)
  dsimp only at outer
  have inner : (∑ u ∈ Finset.univ.erase x, ∑ v : V, weight R color u v) =
      restEnergy R color x + ∑ u ∈ Finset.univ.erase x, weight R color u x := by
    calc
      _ = ∑ u ∈ Finset.univ.erase x,
          ((∑ v ∈ Finset.univ.erase x, weight R color u v) + weight R color u x) := by
        apply Finset.sum_congr rfl
        intro u _
        exact (Finset.sum_erase_add (s := Finset.univ)
          (fun v => weight R color u v) (Finset.mem_univ x)).symm
      _ = _ := Finset.sum_add_distrib
  rw [inner,column,row_sum] at outer
  change restEnergy R color x + (colorNeighbors R color x (color x)).card +
    (colorNeighbors R color x (color x)).card = energy R color at outer
  omega

theorem restEnergy_update (R : V → V → Prop) [DecidableRel R]
    (color : V → Fin 4) (x : V) (k : Fin 4) :
    restEnergy R (Function.update color x k) x = restEnergy R color x := by
  apply Finset.sum_congr rfl
  intro u hu
  apply Finset.sum_congr rfl
  intro v hv
  have ux := (Finset.mem_erase.mp hu).1
  have vx := (Finset.mem_erase.mp hv).1
  simp [weight,Function.update_of_ne ux,Function.update_of_ne vx]

theorem colorNeighbors_update (R : V → V → Prop) [DecidableRel R]
    (irreflexive : ∀ x, ¬ R x x) (color : V → Fin 4) (x : V) (k : Fin 4) :
    colorNeighbors R (Function.update color x k) x k = colorNeighbors R color x k := by
  ext y
  by_cases same : y = x
  · subst y
    simp [colorNeighbors,irreflexive]
  · simp [colorNeighbors,Function.update_of_ne same]

/-- Moving a vertex changes exactly the two orientations of its incident
monochromatic edges. Both neighborhood counts refer to the original coloring. -/
theorem energy_update_balance (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) (irreflexive : ∀ x, ¬ R x x)
    (color : V → Fin 4) (x : V) (k : Fin 4) :
    energy R (Function.update color x k) + 2 * (colorNeighbors R color x (color x)).card =
      energy R color + 2 * (colorNeighbors R color x k).card := by
  rw [energy_at_vertex R symmetric irreflexive (Function.update color x k) x,
    energy_at_vertex R symmetric irreflexive color x,Function.update_self,
    restEnergy_update,colorNeighbors_update R irreflexive]
  omega

omit [DecidableEq V] in
theorem colorNeighbors_sum (R : V → V → Prop) [DecidableRel R]
    (color : V → Fin 4) (x : V) :
    (∑ k : Fin 4, (colorNeighbors R color x k).card) = (neighbors R x).card := by
  simpa [colorNeighbors,neighbors,Finset.filter_filter] using
    Finset.sum_card_fiberwise_eq_card_filter (neighbors R x) Finset.univ color

/-- A minimum-monochromatic-edge partition of a graph of maximum degree six
into four labelled classes has at most one same-class neighbor at each vertex. -/
theorem exists_four_part_defect_one (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) (irreflexive : ∀ x, ¬ R x x)
    (maximum : ∀ x, (neighbors R x).card ≤ 6) :
    ∃ color : V → Fin 4, ∀ x, (colorNeighbors R color x (color x)).card ≤ 1 := by
  classical
  obtain ⟨color,_,minimal⟩ := Finset.exists_min_image (Finset.univ : Finset (V → Fin 4))
    (energy R) ⟨fun _ => 0,Finset.mem_univ _⟩
  refine ⟨color,?_⟩
  intro x
  have each (k : Fin 4) : (colorNeighbors R color x (color x)).card ≤
      (colorNeighbors R color x k).card := by
    have compare := minimal (Function.update color x k) (Finset.mem_univ _)
    have balance := energy_update_balance R symmetric irreflexive color x k
    omega
  have hsum := Finset.sum_le_sum (s := Finset.univ) (fun k _ => each k)
  rw [colorNeighbors_sum R color x] at hsum
  have hmax := maximum x
  simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul] at hsum
  omega

/-- Among at least seventeen vertices, one defect-one class contains five
vertices. Restricting to those five preserves the internal degree bound. -/
theorem exists_five_with_degree_le_one (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) (irreflexive : ∀ x, ¬ R x x)
    (maximum : ∀ x, (neighbors R x).card ≤ 6) (many : 17 ≤ Fintype.card V) :
    ∃ T : Finset V, T.card = 5 ∧ ∀ x ∈ T, (T.filter (R x)).card ≤ 1 := by
  obtain ⟨color,defect⟩ := exists_four_part_defect_one R symmetric irreflexive maximum
  have total : (∑ k : Fin 4, (Finset.univ.filter fun x => color x = k).card) =
      Fintype.card V := by
    simpa using Finset.sum_card_fiberwise_eq_card_filter (Finset.univ : Finset V)
      (Finset.univ : Finset (Fin 4)) color
  have large : ∃ k : Fin 4, 5 ≤ (Finset.univ.filter fun x => color x = k).card := by
    by_contra no
    have small (k : Fin 4) : (Finset.univ.filter fun x => color x = k).card ≤ 4 := by
      have h : ¬ 5 ≤ (Finset.univ.filter fun x => color x = k).card := fun h => no ⟨k,h⟩
      omega
    have hsum := Finset.sum_le_sum (s := Finset.univ) (fun k _ => small k)
    rw [total] at hsum
    simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul] at hsum
    omega
  obtain ⟨k,hk⟩ := large
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq hk
  refine ⟨T,card,?_⟩
  intro x hx
  have cx : color x = k := (Finset.mem_filter.mp (sub hx)).2
  have inside : T.filter (R x) ⊆ colorNeighbors R color x (color x) := by
    intro y hy
    obtain ⟨hy,hxy⟩ := Finset.mem_filter.mp hy
    have cy : color y = k := (Finset.mem_filter.mp (sub hy)).2
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ y,hxy,cy.trans cx.symm⟩
  exact (Finset.card_le_card inside).trans (defect x)

/-- Apply the partition to the actual bad-codegree relation on seven-degree
vertices. The chosen five original vertices induce a matching of bad pairs. -/
theorem exists_five_high_matching (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 17 ≤ (sevenVertices H).card) :
    ∃ f : Fin 5 → V, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
      ∀ i, (Finset.univ.filter fun j : Fin 5 =>
        j ≠ i ∧ 2 ≤ H.codegree (f i) (f j)).card ≤ 1 := by
  classical
  let S := sevenVertices H
  let R : ↥S → ↥S → Prop := fun a b => a ≠ b ∧ 2 ≤ H.codegree a.val b.val
  have symmetric (a b : ↥S) (h : R a b) : R b a :=
    ⟨h.1.symm,by simpa only [H.codegree_comm b.val a.val] using h.2⟩
  have irreflexive (a : ↥S) : ¬ R a a := fun h => h.1 rfl
  have maximum (a : ↥S) : (neighbors R a).card ≤ 6 := by
    have sub : (neighbors R a).image Subtype.val ⊆ H.badPartners a.val := by
      intro z hz
      obtain ⟨b,hb,rfl⟩ := Finset.mem_image.mp hz
      have related := (mem_neighbors R a b).mp hb
      apply Finset.mem_filter.mpr
      refine ⟨Finset.mem_erase.mpr ⟨?_,Finset.mem_univ b.val⟩,related.2⟩
      intro eq
      exact related.1 (Subtype.ext eq.symm)
    have h := Finset.card_le_card sub
    rw [Finset.card_image_of_injective _ Subtype.val_injective] at h
    exact h.trans (seven_badPartners_le_six H cover vertices
      ((mem_sevenVertices H a.val).mp a.property))
  have size : 17 ≤ Fintype.card ↥S := by
    rw [Fintype.card_coe]
    exact many
  obtain ⟨T,Tcard,Tdefect⟩ := exists_five_with_degree_le_one R symmetric irreflexive maximum size
  obtain ⟨g,ginj,inside⟩ := exists_indexed_subset T (n := 5) (by omega)
  let f : Fin 5 → V := fun i => (g i).val
  refine ⟨f,Subtype.val_injective.comp ginj,?_,?_⟩
  · intro i
    exact (mem_sevenVertices H (f i)).mp (g i).property
  · intro i
    let B := Finset.univ.filter fun j : Fin 5 => j ≠ i ∧ 2 ≤ H.codegree (f i) (f j)
    have sub : B.image g ⊆ T.filter (R (g i)) := by
      intro z hz
      obtain ⟨j,hj,rfl⟩ := Finset.mem_image.mp hz
      obtain ⟨_,ji,hbad⟩ := Finset.mem_filter.mp hj
      exact Finset.mem_filter.mpr ⟨inside j,fun h => ji (ginj h.symm),hbad⟩
    have h := Finset.card_le_card sub
    rw [Finset.card_image_of_injective B ginj] at h
    exact h.trans (Tdefect (g i) (inside i))

/-- Five selected high vertices together with an actual six-degree vertex
unit to all sevens yield the six locks of the all-unit-low candidate. -/
theorem exists_six_locks_low_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 17 ≤ (sevenVertices H).card)
    (x : V) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1) :
    ∃ f : Fin 6 → V, Function.Injective f ∧ f 5 = x ∧
      (∀ i, H.degree (f i) = if i.val < 5 then 7 else 6) ∧
      (∀ i : Fin 5, H.codegree x (f i.castSucc) = 1) ∧
      (∀ i : Fin 5, (Finset.univ.filter fun j : Fin 5 =>
        j ≠ i ∧ 2 ≤ H.codegree (f i.castSucc) (f j.castSucc)).card ≤ 1) := by
  obtain ⟨g,ginj,degree,matching⟩ := exists_five_high_matching H cover vertices many
  let f : Fin 6 → V := Fin.append g (fun _ : Fin 1 => x)
  have finj : Function.Injective f := by
    apply Fin.append_injective_iff.mpr
    refine ⟨ginj,?_,?_⟩
    · intro i j _
      exact Subsingleton.elim i j
    · intro i j same
      have di := degree i
      change g i = x at same
      rw [same,dx] at di
      omega
  have left (i : Fin 5) : f i.castSucc = g i := by
    fin_cases i <;> rfl
  refine ⟨f,finj,rfl,?_,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,Fin.append] <;> first | exact degree _ | exact dx
  · intro i
    rw [left]
    exact unit (g i) (degree i)
  · intro i
    simpa only [left] using matching i

theorem exists_six_locks_low_unit_of_count (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 33)
    (vertices : Fintype.card V = 23) (count : H.sixVertices.card = 1)
    (x : V) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1) :
    ∃ f : Fin 6 → V, Function.Injective f ∧ f 5 = x ∧
      (∀ i, H.degree (f i) = if i.val < 5 then 7 else 6) ∧
      (∀ i : Fin 5, H.codegree x (f i.castSucc) = 1) ∧
      (∀ i : Fin 5, (Finset.univ.filter fun j : Fin 5 =>
        j ≠ i ∧ 2 ≤ H.codegree (f i.castSucc) (f j.castSucc)).card ≤ 1) := by
  have budget := six_seven_budget H cover edges vertices
  exact exists_six_locks_low_unit H cover vertices (by omega) x dx unit

/-- Before applying the six-lock matching table, a codegree-three pair of
high vertices can be extended to the actual five-lock exclusion pattern. -/
theorem exists_mixed_five_of_high_three (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (many : 17 ≤ (sevenVertices H).card)
    (x y z : V) (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (unit : ∀ a, H.degree a = 7 → H.codegree x a = 1)
    (yz : y ≠ z) (cyz : H.codegree y z = 3) :
    ∃ f : Fin 5 → V, Function.Injective f ∧ f 0 = x ∧
      (∀ i, H.degree (f i) = if i = 0 then 6 else 7) ∧
      H.codegree (f 1) (f 2) = 3 ∧
      (∀ i j, i < j → ¬ (i = 1 ∧ j = 2) → ¬ (i = 3 ∧ j = 4) →
        H.codegree (f i) (f j) = 1) := by
  let A := insert y (H.badPartners y)
  let B := insert z (H.badPartners z)
  let P := sevenVertices H \ (A ∪ B)
  have A7 : A.card ≤ 7 := by
    have hb := seven_badPartners_le_six H cover vertices dy
    have hi := Finset.card_insert_le y (H.badPartners y)
    dsimp [A]
    omega
  have B7 : B.card ≤ 7 := by
    have hb := seven_badPartners_le_six H cover vertices dz
    have hi := Finset.card_insert_le z (H.badPartners z)
    dsimp [B]
    omega
  have Psize : 1 < P.card := by
    have hu := Finset.card_union_le A B
    have budget := Finset.card_le_card_sdiff_add_card (s := sevenVertices H) (t := A ∪ B)
    change (sevenVertices H).card ≤ P.card + (A ∪ B).card at budget
    omega
  have degreeP (a : V) (ha : a ∈ P) : H.degree a = 7 :=
    (mem_sevenVertices H a).mp (Finset.mem_sdiff.mp ha).1
  have goodY (a : V) (ha : a ∈ P) : a ≠ y ∧ H.codegree y a = 1 := by
    have good : a ∈ H.goodPartners y := Finset.mem_sdiff.mpr
      ⟨Finset.mem_univ a,fun h => (Finset.mem_sdiff.mp ha).2 (Finset.mem_union_left B h)⟩
    exact (H.mem_goodPartners cover y a).mp good
  have goodZ (a : V) (ha : a ∈ P) : a ≠ z ∧ H.codegree z a = 1 := by
    have good : a ∈ H.goodPartners z := Finset.mem_sdiff.mpr
      ⟨Finset.mem_univ a,fun h => (Finset.mem_sdiff.mp ha).2 (Finset.mem_union_right A h)⟩
    exact (H.mem_goodPartners cover z a).mp good
  obtain ⟨u,hu,v,hv,uv⟩ := Finset.one_lt_card.mp Psize
  have du := degreeP u hu
  have dv := degreeP v hv
  obtain ⟨uy,cyu⟩ := goodY u hu
  obtain ⟨vy,cyv⟩ := goodY v hv
  obtain ⟨uz,czu⟩ := goodZ u hu
  obtain ⟨vz,czv⟩ := goodZ v hv
  have lowNe (a : V) (da : H.degree a = 7) : x ≠ a := by
    intro eq
    rw [eq,da] at dx
    omega
  have xy := lowNe y dy
  have xz := lowNe z dz
  have xu := lowNe u du
  have xv := lowNe v dv
  have cxy := unit y dy
  have cxz := unit z dz
  have cxu := unit u du
  have cxv := unit v dv
  let f : Fin 5 → V := ![x,y,z,u,v]
  have finj : Function.Injective f := by
    intro i j heq
    fin_cases i <;> fin_cases j <;>
      simp [f,xy,xy.symm,xz,xz.symm,xu,xu.symm,xv,xv.symm,
        yz,yz.symm,uy,uy.symm,vy,vy.symm,uz,uz.symm,vz,vz.symm,uv,uv.symm] at heq <;> rfl
  refine ⟨f,finj,rfl,?_,cyz,?_⟩
  · intro i
    fin_cases i <;> simp [f,dx,dy,dz,du,dv]
  · intro i j hij h12 h34
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;>
      simp [Fin.ext_iff] at h12 <;> simp [Fin.ext_iff] at h34 <;>
      first | exact cxy | exact cxz | exact cxu | exact cxv |
        exact cyu | exact cyv | exact czu | exact czv

end Aris4Math.ThirtyThree.TwentyThreeDefectSelection

#print axioms Aris4Math.ThirtyThree.TwentyThreeDefectSelection.energy_update_balance
#print axioms Aris4Math.ThirtyThree.TwentyThreeDefectSelection.exists_five_with_degree_le_one
#print axioms Aris4Math.ThirtyThree.TwentyThreeDefectSelection.exists_six_locks_low_unit_of_count
#print axioms Aris4Math.ThirtyThree.TwentyThreeDefectSelection.exists_mixed_five_of_high_three
