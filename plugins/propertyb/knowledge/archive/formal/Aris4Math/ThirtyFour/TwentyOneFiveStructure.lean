import Aris4Math.ThirtyFour.TwentyOneFiveTriples
import Aris4Math.ThirtyThree.TwentyOneStructure
import Aris4Math.ThirtyFour.Incidence

namespace Aris4Math.ThirtyFour.TwentyOneFiveStructure
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles
open Aris4Math.ThirtyThree.TwentyOneStructure (all_unit_of_degree_five degree_budget_two)

theorem pair_inventory {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (x y z : Fin v) (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z) :
    H.codegree x y + H.codegree y z ≤ H.degree y + tripleCodegree H x y z := by
  let f := threeVertices x y z xy xz yz
  have hd := sum_degree_counts H f 1
  have ha := sum_codegree_counts H f 0 1
  have hb := sum_codegree_counts H f 1 2
  rw [Aris4Math.TripleLockProfiles.label_univ] at hd ha hb
  simp +decide only [Finset.filter_insert,Finset.filter_singleton,Finset.sum_insert,
    Finset.sum_singleton,Finset.mem_insert,Finset.mem_singleton,if_true,if_false] at hd ha hb
  have ht := triple_count_eq H f
  change count H f {0,1,2}=tripleCodegree H x y z at ht
  change _=H.degree y at hd
  change _=H.codegree x y at ha
  change _=H.codegree y z at hb
  omega

variable (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
  (size : H.edges.card=34) (x : Fin 21) (dx : H.degree x=5)
include cover size dx

theorem other_low (low : ∃ y, y ≠ x ∧ H.degree y ≤ 6) : PropertyB H := by
  classical
  obtain ⟨y0,y0x,dy0⟩ := low
  obtain ⟨y,hy,least⟩ := (Finset.univ.erase x).exists_min_image H.degree ⟨y0,by simp [y0x]⟩
  have yx := (Finset.mem_erase.mp hy).1
  have dy6 : H.degree y ≤ 6 := (least y0 (by simp [y0x])).trans dy0
  have dy5 : 5 ≤ H.degree y := by
    have bound := H.pairCovering_degree_bound cover y
    simp only [Fintype.card_fin] at bound; omega
  let S := (Finset.univ.erase x).erase y
  have spos : 0<S.card := by simp [S,Finset.card_erase_of_mem hy]
  obtain ⟨z,hz,leastz⟩ := S.exists_min_image H.degree (Finset.card_pos.mp spos)
  obtain ⟨zy,hz'⟩ := Finset.mem_erase.mp hz
  have zx := (Finset.mem_erase.mp hz').1
  have dyz := least z hz'
  have dz8 : H.degree z ≤ 8 := by
    by_contra hn
    have bud := degree_budget_two H x y (Ne.symm yx) 9 (fun w wx wy => by
      have h := leastz w (by simp [S,wx,wy]); omega)
    simp only [Fintype.card_fin,size,dx] at bud
    omega
  have unit := all_unit_of_degree_five H cover (by simp) x dx
  have a := unit y (Ne.symm yx)
  have b := unit z (Ne.symm zx)
  have cl := H.one_le_codegree cover (Ne.symm zy)
  have cu := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H y z
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  rw [a] at ta
  have inv := pair_inventory H x y z (Ne.symm yx) (Ne.symm zx) (Ne.symm zy)
  rw [a] at inv
  have five (dd : H.degree y=5) : H.codegree y z=1 :=
    all_unit_of_degree_five H cover (by simp) y dd z (Ne.symm zy)
  have suitable := TwentyOneFiveTriples.low_coverage
    ⟨H.degree y,by omega⟩ ⟨H.degree z,by omega⟩ ⟨H.codegree y z,by omega⟩
    ⟨tripleCodegree H x y z,by omega⟩ dy5 dy6 dyz cl cu inv five
  exact TwentyOneFiveTriples.propertyB_of_suitable H cover size x y z
    (Ne.symm yx) (Ne.symm zx) (Ne.symm zy) dx a b suitable

theorem seven_pair (noB : ¬ PropertyB H) (y z : Fin 21)
    (dy : H.degree y=7) (dz : H.degree z=7) (yz : y ≠ z) :
    H.codegree y z=2 ∧ tripleCodegree H x y z=1 := by
  have xy : x ≠ y := by intro eq; rw [eq,dy] at dx; omega
  have xz : x ≠ z := by intro eq; rw [eq,dz] at dx; omega
  have unit := all_unit_of_degree_five H cover (by simp) x dx
  have a := unit y xy; have b := unit z xz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  rw [a] at ta
  have cl := H.one_le_codegree cover yz
  have cu := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H y z
  rw [dy] at cu
  have inv := pair_inventory H x y z xy xz yz
  rw [a,dy] at inv
  rcases TwentyOneFiveTriples.seven_coverage ⟨H.codegree y z,by omega⟩
      ⟨tripleCodegree H x y z,by omega⟩ cl inv with residual | suitable
  · exact residual
  · apply False.elim; apply noB
    apply TwentyOneFiveTriples.propertyB_of_suitable H cover size x y z xy xz yz dx a b
    simpa only [dy,dz] using suitable

theorem high_pair (noB : ¬ PropertyB H) (y z : Fin 21)
    (dy : H.degree y=7 ∨ H.degree y=8) (dz : H.degree z=8) (yz : y ≠ z) :
    H.codegree y z ≤ 2 := by
  have xy : x ≠ y := by intro eq; rw [← eq,dx] at dy; omega
  have xz : x ≠ z := by intro eq; rw [eq,dz] at dx; omega
  have unit := all_unit_of_degree_five H cover (by simp) x dx
  have a := unit y xy; have b := unit z xz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  rw [a] at ta
  have inv := pair_inventory H x y z xy xz yz
  rw [a] at inv
  have cu := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H y z
  by_contra hn
  have high : 3 ≤ H.codegree y z := by omega
  apply noB
  apply TwentyOneFiveTriples.propertyB_of_suitable H cover size x y z xy xz yz dx a b
  rcases dy with dy | dy
  · rw [dy,dz]
    rw [dy] at cu inv
    exact TwentyOneFiveTriples.mixed_high ⟨H.codegree y z,by omega⟩
      ⟨tripleCodegree H x y z,by omega⟩ high inv
  · rw [dy,dz]
    rw [dy] at cu inv
    exact TwentyOneFiveTriples.eight_high ⟨H.codegree y z,by omega⟩
      ⟨tripleCodegree H x y z,by omega⟩ high inv

omit cover size x dx in
def sevens : Finset (Fin 21) := Finset.univ.filter (fun y => H.degree y=7)
omit cover size x dx in
def eights : Finset (Fin 21) := Finset.univ.filter (fun y => H.degree y=8)
omit cover size x dx in
theorem mem_sevens (y : Fin 21) : y ∈ sevens H ↔ H.degree y=7 := by simp [sevens]
omit cover size x dx in
theorem mem_eights (y : Fin 21) : y ∈ eights H ↔ H.degree y=8 := by simp [eights]

theorem eights_budget (minimum : ∀ y, y ≠ x → 7 ≤ H.degree y) :
    15 ≤ 2*(sevens H).card+(eights H).card := by
  have each (y : Fin 21) : 9 ≤ H.degree y + (if y=x then 4 else 0) +
      (if y ∈ sevens H then 2 else 0) + (if y ∈ eights H then 1 else 0) := by
    by_cases eq : y=x
    · simp [eq,dx,sevens,eights]
    have lo := minimum y eq
    by_cases seven : H.degree y=7
    · simp [eq,seven,sevens,eights]
    by_cases eight : H.degree y=8
    · simp [eq,eight,sevens,eights]
    simp only [mem_sevens,mem_eights,eq,seven,eight,if_false,add_zero]; omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun y _ => each y)
  have bud : 189 ≤ 170+4+2*(sevens H).card+(eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,Nat.mul_comm] using sum
  omega

end Aris4Math.ThirtyFour.TwentyOneFiveStructure
#print axioms Aris4Math.ThirtyFour.TwentyOneFiveStructure.other_low
