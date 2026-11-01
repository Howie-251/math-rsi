import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalogData
import Aris4Math.ThirtyThree.TwentyThreeDefectSelection

/-! Actual normalization of the matching among five high locks, with the low lock fixed. -/
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection
open TwentyThreeLowUnitSixCatalogData (degreeData pairDegree permutation)
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def first : Fin 10 → Fin 6 := ![0,0,0,0,1,1,1,2,2,3]
def second : Fin 10 → Fin 6 := ![1,2,3,4,2,3,4,3,4,4]
def related (h : Fin 10 → Bool) (i j : Fin 6) : ℕ :=
  if ∃ a : Fin 10, ((first a = i ∧ second a = j) ∨
      (first a = j ∧ second a = i)) ∧ h a = true then 2 else 1

def IsMatching (h : Fin 10 → Bool) : Prop :=
  ∀ i : Fin 5, (Finset.univ.filter fun j : Fin 5 =>
    j ≠ i ∧ related h i.castSucc j.castSucc = 2).card ≤ 1

def matching : Fin 26 → Fin 10 → Bool := ![![false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,false],![false,false,false,false,true,false,false,false,false,false],![false,false,true,false,true,false,false,false,false,false],![false,false,false,true,true,false,false,false,false,false],![false,false,false,false,false,true,false,false,false,false],![false,true,false,false,false,true,false,false,false,false],![false,false,false,true,false,true,false,false,false,false],![false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,false,true,false,false,false],![false,false,true,false,false,false,true,false,false,false],![false,false,false,false,false,false,false,true,false,false],![true,false,false,false,false,false,false,true,false,false],![false,false,false,true,false,false,false,true,false,false],![false,false,false,false,false,false,true,true,false,false],![false,false,false,false,false,false,false,false,true,false],![true,false,false,false,false,false,false,false,true,false],![false,false,true,false,false,false,false,false,true,false],![false,false,false,false,false,true,false,false,true,false],![false,false,false,false,false,false,false,false,false,true],![true,false,false,false,false,false,false,false,false,true],![false,true,false,false,false,false,false,false,false,true],![false,false,false,false,true,false,false,false,false,true]]
def edgeNumber : Fin 26 → Fin 3 := ![0,1,1,1,1,1,2,2,1,2,2,1,2,2,1,2,2,2,1,2,2,2,1,2,2,2]
def order : Fin 26 → Fin 120 := ![0,0,6,12,18,30,12,18,36,6,19,42,7,13,60,0,21,45,66,1,15,39,90,3,9,33]

/-- Complete coverage of all ten-bit graphs of maximum degree one. -/
theorem matching_complete : ∀ h : Fin 10 → Bool, IsMatching h →
    ∃ k : Fin 26, h = matching k := by
  unfold IsMatching
  decide +kernel

theorem normalized : ∀ k : Fin 26, ∀ i j : Fin 6, i ≠ j →
    related (matching k) (permutation (order k) i) (permutation (order k) j) =
      pairDegree (edgeNumber k) i j := by decide +kernel

theorem permutation_degrees : ∀ r : Fin 120, ∀ i : Fin 6,
    degreeData (permutation r i) = degreeData i := by decide +kernel

theorem endpoints : ∀ a, first a ≠ 5 ∧ second a ≠ 5 ∧ first a ≠ second a := by
  decide +kernel

theorem pair_supported : ∀ i j : Fin 6, i ≠ 5 → j ≠ 5 → i ≠ j →
    ∃ a : Fin 10, (first a = i ∧ second a = j) ∨
      (first a = j ∧ second a = i) := by decide +kernel

/-- The bit graph is computed from actual codegrees of the selected locks. -/
def actualBits (H : Simple5Hypergraph (Fin 23)) (f : Fin 6 → Fin 23) : Fin 10 → Bool :=
  fun a => decide (H.codegree (f (first a)) (f (second a)) = 2)

theorem actual_related (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 6 → Fin 23) (inj : Function.Injective f)
    (degrees : ∀ i, H.degree (f i) = degreeData i)
    (unit : ∀ i : Fin 6, i ≠ 5 → H.codegree (f 5) (f i) = 1)
    (upper : ∀ y z, y ≠ z → H.degree y = 7 → H.degree z = 7 → H.codegree y z ≤ 2)
    (i j : Fin 6) (ij : i ≠ j) :
    H.codegree (f i) (f j) = related (actualBits H f) i j := by
  have bits : ∀ a, actualBits H f a = true ↔ H.codegree (f (first a)) (f (second a)) = 2 :=
    fun a => by simp [actualBits]
  by_cases i5 : i = 5
  · subst i
    rw [unit j (Ne.symm ij)]
    unfold related
    have no : ¬ ∃ a, ((first a = 5 ∧ second a = j) ∨
        (first a = j ∧ second a = 5)) ∧ actualBits H f a = true := by
      rintro ⟨a,ha,_⟩
      rcases ha with ⟨h,_⟩ | ⟨_,h⟩
      · exact (endpoints a).1 h
      · exact (endpoints a).2.1 h
    simp [no]
  by_cases j5 : j = 5
  · subst j
    rw [H.codegree_comm,unit i i5]
    unfold related
    have no : ¬ ∃ a, ((first a = i ∧ second a = 5) ∨
        (first a = 5 ∧ second a = i)) ∧ actualBits H f a = true := by
      rintro ⟨a,ha,_⟩
      rcases ha with ⟨_,h⟩ | ⟨h,_⟩
      · exact (endpoints a).2.1 h
      · exact (endpoints a).1 h
    simp [no]
  have di : H.degree (f i) = 7 := by simpa [degreeData,i5] using degrees i
  have dj : H.degree (f j) = 7 := by simpa [degreeData,j5] using degrees j
  have lo := H.one_le_codegree cover (inj.ne ij)
  have hi := upper (f i) (f j) (inj.ne ij) di dj
  have eq : (∃ a, ((first a = i ∧ second a = j) ∨
      (first a = j ∧ second a = i)) ∧ actualBits H f a = true) ↔
      H.codegree (f i) (f j) = 2 := by
    constructor
    · rintro ⟨a,ha,hbit⟩
      have co := (bits a).mp hbit
      rcases ha with ⟨h1,h2⟩ | ⟨h1,h2⟩
      · simpa only [h1,h2] using co
      · simpa only [h1,h2,H.codegree_comm (f j) (f i)] using co
    · intro co
      obtain ⟨a,ha⟩ := pair_supported i j i5 j5 ij
      refine ⟨a,ha,(bits a).mpr ?_⟩
      rcases ha with ⟨h1,h2⟩ | ⟨h1,h2⟩
      · simpa only [h1,h2] using co
      · simpa only [h1,h2,H.codegree_comm (f j) (f i)] using co
  simp only [related,eq]
  split <;> omega

/-- Actual six locks with canonical zero-, one-, or two-edge high matching. -/
theorem exists_locks (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count : H.sixVertices.card = 1) (x : Fin 23) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1)
    (upper : ∀ y z, y ≠ z → H.degree y = 7 → H.degree z = 7 → H.codegree y z ≤ 2) :
    ∃ e : Fin 3, ∃ w : Fin 6 ↪ Fin 23,
      (∀ i, H.degree (w i) = degreeData i) ∧
      (∀ i j, i ≠ j → H.codegree (w i) (w j) = pairDegree e i j) := by
  obtain ⟨f,inj,fx,df,uf,matching_bound⟩ :=
    TwentyThreeDefectSelection.exists_six_locks_low_unit_of_count H cover edges33
      (by decide) count x dx unit
  have degrees (i : Fin 6) : H.degree (f i) = degreeData i := by
    rw [df]
    fin_cases i <;> rfl
  have units (i : Fin 6) (i5 : i ≠ 5) : H.codegree (f 5) (f i) = 1 := by
    rw [fx]
    exact unit (f i) (by simpa [degreeData,i5] using degrees i)
  have actual := actual_related H cover f inj degrees units upper
  have ismatching : IsMatching (actualBits H f) := by
    intro i
    apply le_trans (Finset.card_le_card ?_) (matching_bound i)
    intro j hj
    simp only [Finset.mem_filter,Finset.mem_univ,true_and] at hj ⊢
    refine ⟨hj.1,?_⟩
    have ij : i.castSucc ≠ j.castSucc := by
      intro eq
      exact hj.1 (Fin.castSucc_injective _ eq).symm
    rw [actual i.castSucc j.castSucc ij,hj.2]
  obtain ⟨k,hk⟩ := matching_complete (actualBits H f) ismatching
  let σ := permutation (order k)
  let w : Fin 6 ↪ Fin 23 := σ.toEmbedding.trans ⟨f,inj⟩
  refine ⟨edgeNumber k,w,?_,?_⟩
  · intro i
    change H.degree (f (σ i)) = _
    rw [degrees]
    exact permutation_degrees (order k) i
  · intro i j ij
    change H.codegree (f (σ i)) (f (σ j)) = _
    rw [actual (σ i) (σ j) (σ.injective.ne ij),hk]
    exact normalized k i j ij

end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection
