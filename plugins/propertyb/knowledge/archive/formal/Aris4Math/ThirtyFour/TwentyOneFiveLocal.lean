import Aris4Math.ThirtyFour.TwentyOneFiveStructure
import Aris4Math.ThirtyFour.TwentyOneFiveClassification
import Aris4Math.ThirtyFour.QuadIncidence

set_option simprocs false

namespace Aris4Math.ThirtyFour.TwentyOneFiveLocal
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices high_inventory highPairSum)
open Aris4Math.ThirtyFour.TwentyOneFiveClassification (Kind degrees Assumptions Residue)

variable (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
  (size : H.edges.card=34) (noB : ¬ PropertyB H)
include cover size noB

theorem residue (f : Fin 4 ↪ Fin 21) (kind : Kind)
    (hd : ∀ j, H.degree (f j)=degrees kind j)
    (ass : Assumptions kind (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j))) :
    Residue kind (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  have dx : H.degree (f 0)=5 := by have h := hd 0; fin_cases kind <;> simpa [degrees] using h
  have other (j : Fin 3) : H.degree (f j.succ)=7 ∨ H.degree (f j.succ)=8 := by
    rw [hd]; fin_cases kind <;> fin_cases j <;> decide
  have unit := ThirtyThree.TwentyOneStructure.all_unit_of_degree_five H cover (by simp) (f 0) dx
  have u (j : Fin 3) : H.codegree (f 0) (f j.succ)=1 := unit _ (f.injective.ne (by fin_cases j <;> decide))
  have pair (i j : Fin 3) (ij : i ≠ j) : H.codegree (f i.succ) (f j.succ) ≤ 2 := by
    have ne := f.injective.ne (Fin.succ_injective 3 |>.ne ij)
    rcases other i with di | di <;> rcases other j with dj | dj
    · exact le_of_eq (TwentyOneFiveStructure.seven_pair H cover size (f 0) dx noB _ _ di dj ne).1
    · exact TwentyOneFiveStructure.high_pair H cover size (f 0) dx noB _ _ (Or.inl di) dj ne
    · rw [H.codegree_comm]
      exact TwentyOneFiveStructure.high_pair H cover size (f 0) dx noB _ _ (Or.inl dj) di (Ne.symm ne)
    · exact TwentyOneFiveStructure.high_pair H cover size (f 0) dx noB _ _ (Or.inr di) dj ne
  apply TwentyOneFiveClassification.residual_of_not_propertyB H size noB f kind hd u _ cover ass
  intro j
  have u0 := u 0; have u1 := u 1; have u2 := u 2
  have p01 := pair 0 1 (by decide); have p02 := pair 0 2 (by decide); have p12 := pair 1 2 (by decide)
  fin_cases j
  · change H.codegree (f 0) (f 1) ≤ 2
    change H.codegree (f 0) (f 1)=1 at u0
    omega
  · change H.codegree (f 0) (f 2) ≤ 2
    change H.codegree (f 0) (f 2)=1 at u1
    omega
  · change H.codegree (f 0) (f 3) ≤ 2
    change H.codegree (f 0) (f 3)=1 at u2
    omega
  · exact p01
  · exact p02
  · exact p12

omit cover size noB in
theorem common_quad (f : Fin 4 ↪ Fin 21) (e : Finset (Fin 21)) (he : e ∈ H.edges)
    (common : ∀ j, f j ∈ e) : 1 ≤ count H f (highLabels 4) := by
  have sig : lockSignature f e=highLabels 4 := by
    have all : highLabels 4=Finset.univ := by decide
    rw [all]
    ext j
    simp [lockSignature,common]
  exact Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩

omit cover size noB in
theorem triple_common (x y z : Fin 21) (positive : 1 ≤ tripleCodegree H x y z) :
    ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e ∧ z ∈ e := by
  obtain ⟨e,he⟩ := Finset.one_le_card.mp positive
  exact ⟨e,(Finset.mem_filter.mp he).1,(Finset.mem_filter.mp he).2⟩

omit size noB in
theorem no_triple_outside (x y z : Fin 21) (dx : H.degree x=5) (xy : x ≠ y)
    (e : Finset (Fin 21)) (he : e ∈ H.edges) (xe : x ∈ e) (ye : y ∈ e)
    (ze : z ∉ e) : tripleCodegree H x y z=0 := by
  apply ThirtyThree.TwentyOnePairAssembly.tripleCodegree_zero
  intro f hf hxyz
  have unit := ThirtyThree.TwentyOneStructure.all_unit_of_degree_five H cover (by simp) x dx y xy
  have eq := H.edge_unique_of_codegree_one unit hf he hxyz.1 hxyz.2.1 xe ye
  exact ze (eq ▸ hxyz.2.2)

end Aris4Math.ThirtyFour.TwentyOneFiveLocal
