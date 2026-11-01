import Aris4Math.Structure
import Mathlib.Data.Finset.Max
import Mathlib.Data.Finset.Powerset

/-! Minimum-weight fixed-cardinality subsets and their actual exchange bounds.
The energy counts both orientations; no averaging over graphs is involved. -/
namespace Aris4Math.ThirtyFour.WeightedSubsetSelection

open scoped BigOperators
variable {V : Type*} [DecidableEq V]

def degree (w : V → V → ℕ) (S : Finset V) (x : V) : ℕ := ∑ y ∈ S, w x y
def energy (w : V → V → ℕ) (S : Finset V) : ℕ := ∑ x ∈ S, degree w S x

theorem degree_insert (w : V → V → ℕ) (S : Finset V) (x y : V) (hy : y ∉ S) :
    degree w (insert y S) x = w x y + degree w S x := by
  simp [degree,hy]

theorem energy_insert (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (S : Finset V) (x : V) (hx : x ∉ S) :
    energy w (insert x S) = energy w S + 2 * degree w S x := by
  unfold energy
  rw [Finset.sum_insert hx]
  simp_rw [degree_insert w S _ x hx]
  rw [Finset.sum_add_distrib, zero, Nat.zero_add]
  have column : (∑ y ∈ S, w y x) = degree w S x := by
    exact Finset.sum_congr rfl (fun y _ => symm y x)
  rw [column]
  omega

theorem energy_erase (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (S : Finset V) (x : V) (hx : x ∈ S) :
    energy w S = energy w (S.erase x) + 2 * degree w S x := by
  have h := energy_insert w symm zero (S.erase x) x (Finset.notMem_erase x S)
  rw [Finset.insert_erase hx] at h
  have d : degree w (S.erase x) x = degree w S x := by
    have h := Finset.sum_erase_add (s := S) (fun y => w x y) hx
    simpa [degree,zero] using h
  simpa [d] using h

theorem energy_even (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (S : Finset V) : ∃ k, energy w S = 2*k := by
  induction S using Finset.induction_on with
  | empty => exact ⟨0,by simp [energy]⟩
  | @insert x S hx ih =>
    obtain ⟨k,hk⟩ := ih
    refine ⟨k + degree w S x,?_⟩
    rw [energy_insert w symm zero S x hx,hk]
    omega

theorem swap_balance (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (S : Finset V) (x y : V)
    (hx : x ∈ S) (hy : y ∉ S) :
    energy w (insert y (S.erase x)) + 2*degree w S x + 2*w x y =
      energy w S + 2*degree w S y := by
  have hS := energy_erase w symm zero S x hx
  have hT := energy_insert w symm zero (S.erase x) y
    (fun hm => hy (Finset.mem_of_mem_erase hm))
  have dy := Finset.sum_erase_add (s := S) (fun z => w y z) hx
  change degree w (S.erase x) y + w y x = degree w S y at dy
  rw [symm y x] at dy
  omega

def IsMinimum (w : V → V → ℕ) (L S : Finset V) : Prop :=
  S ⊆ L ∧ ∀ T ⊆ L, T.card = S.card → energy w S ≤ energy w T

theorem exists_minimum (w : V → V → ℕ) (L : Finset V) (k : ℕ)
    (hk : k ≤ L.card) : ∃ S, S.card=k ∧ IsMinimum w L S := by
  classical
  obtain ⟨S,hS,minimal⟩ := Finset.exists_min_image (L.powersetCard k) (energy w)
    (Finset.powersetCard_nonempty.mpr hk)
  obtain ⟨sub,card⟩ := Finset.mem_powersetCard.mp hS
  refine ⟨S,card,sub,?_⟩
  intro T hT hcard
  exact minimal T (Finset.mem_powersetCard.mpr ⟨hT,hcard.trans card⟩)

theorem swap_inequality (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (L S : Finset V) (minimal : IsMinimum w L S)
    (x y : V) (hx : x ∈ S) (hy : y ∈ L \ S) :
    degree w S x + w x y ≤ degree w S y := by
  obtain ⟨hyL,hyS⟩ := Finset.mem_sdiff.mp hy
  have sub : insert y (S.erase x) ⊆ L := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact hyL
    · exact minimal.1 (Finset.mem_of_mem_erase hz)
  have card : (insert y (S.erase x)).card = S.card := by
    rw [Finset.card_insert_of_notMem (fun hz => hyS (Finset.mem_of_mem_erase hz)),
      Finset.card_erase_of_mem hx]
    have positive := Finset.card_pos.mpr ⟨x,hx⟩
    omega
  have min := minimal.2 _ sub card
  have balance := swap_balance w symm zero S x y hx hyS
  omega

theorem degree_split (w : V → V → ℕ) (L S : Finset V) (sub : S ⊆ L) (x : V) :
    degree w S x + degree w (L \ S) x = degree w L x := by
  have disjoint : Disjoint S (L \ S) := Finset.sdiff_disjoint.symm
  have union : S ∪ (L \ S) = L := Finset.union_sdiff_of_subset sub
  simpa [degree,union] using (Finset.sum_union disjoint (f := w x)).symm

/-- Sum all swaps at one actual selected vertex. This is the general form of
(r-7)d_S(x)+2W≤30 for a six-set in weighted maximum degree six. -/
theorem vertex_bound (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (L S : Finset V) (minimal : IsMinimum w L S)
    (D : ℕ) (maximum : ∀ z ∈ L, degree w L z ≤ D)
    (proper : S.card < L.card) (x : V) (hx : x ∈ S) :
    (L.card-(S.card+1))*degree w S x + energy w S ≤ (S.card-1)*D := by
  let B := L \ S
  let cut := ∑ z ∈ S, degree w B z
  have swap := Finset.sum_le_sum (s := B)
    (fun y hy => swap_inequality w symm zero L S minimal x y hx hy)
  have exchange : B.card * degree w S x + degree w B x ≤ cut := by
    have trans : (∑ y ∈ B, degree w S y) = cut := by
      dsimp [degree,cut]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro z hz
      exact Finset.sum_congr rfl (fun y _ => symm y z)
    rw [Finset.sum_add_distrib,trans] at swap
    simpa [degree,Finset.sum_const,nsmul_eq_mul] using swap
  have all : energy w S + cut = ∑ z ∈ S, degree w L z := by
    rw [energy,← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun z _ => degree_split w L S minimal.1 z)
  have rest : (∑ z ∈ S.erase x, degree w L z) ≤ (S.card-1)*D := by
    calc
      _ ≤ ∑ _z ∈ S.erase x, D := Finset.sum_le_sum
        (fun z hz => maximum z (minimal.1 (Finset.mem_of_mem_erase hz)))
      _ = _ := by simp [Finset.card_erase_of_mem hx]
  have split := Finset.sum_erase_add (s := S) (fun z => degree w L z) hx
  have dx := degree_split w L S minimal.1 x
  have cards : B.card+S.card=L.card := Finset.card_sdiff_add_card_eq_card minimal.1
  have positive : 0 < B.card := by omega
  have coeff : L.card-(S.card+1)+1=B.card := by omega
  rw [← coeff,Nat.add_mul] at exchange
  nlinarith

/-- The actual minimizing six-set needed in the 23-vertex branch. Energy is
twice its unordered weight. Summing over all six-subsets is unnecessary:
the vertex bound and parity already give all required integer bounds. -/
theorem exists_six (w : V → V → ℕ) (symm : ∀ x y, w x y = w y x)
    (zero : ∀ x, w x x = 0) (L : Finset V) (large : 14 ≤ L.card)
    (maximum : ∀ z ∈ L, degree w L z ≤ 6) :
    ∃ S, S.card=6 ∧ IsMinimum w L S ∧ energy w S ≤ 12 ∧
      (∀ x ∈ S, degree w S x ≤ 3) ∧
      (∀ x ∈ S, degree w S x=3 → energy w S ≤ 8) := by
  obtain ⟨S,card,minimal⟩ := exists_minimum w L 6 (by omega)
  have each (x : V) (hx : x ∈ S) := vertex_bound w symm zero L S minimal 6
    maximum (by omega) x hx
  have seven : 7 ≤ L.card-7 := by omega
  have maxThree : ∀ x ∈ S, degree w S x ≤ 3 := by
    intro x hx
    have bound := each x hx
    have twice := energy_erase w symm zero S x hx
    have weighted := Nat.mul_le_mul_right (degree w S x) seven
    rw [card] at bound
    norm_num at bound
    nlinarith
  have atThree : ∀ x ∈ S, degree w S x=3 → energy w S ≤ 8 := by
    intro x hx dx
    have bound := each x hx
    obtain ⟨k,hk⟩ := energy_even w symm zero S
    rw [card,dx] at bound
    norm_num at bound
    omega
  refine ⟨S,card,minimal,?_,maxThree,atThree⟩
  by_cases existsThree : ∃ x ∈ S, degree w S x=3
  · obtain ⟨x,hx,dx⟩ := existsThree
    have bound := atThree x hx dx
    omega
  · have bound : ∀ x ∈ S, degree w S x ≤ 2 := by
      intro x hx
      have max := maxThree x hx
      have ne : degree w S x ≠ 3 := fun eq => existsThree ⟨x,hx,eq⟩
      omega
    calc
      energy w S ≤ ∑ _x ∈ S, 2 := Finset.sum_le_sum bound
      _ = 12 := by simp [card]

/-- In the six-set equality case only the saturation of selected vertices is
needed. This avoids identifying the complete weighted graph as two K7s. -/
theorem six_equality_saturation (w : V → V → ℕ)
    (symm : ∀ x y, w x y = w y x) (zero : ∀ x, w x x=0)
    (L S : Finset V) (minimal : IsMinimum w L S) (card : S.card=6)
    (large : 14 ≤ L.card) (maximum : ∀ x ∈ L, degree w L x ≤ 6)
    (internal : ∀ x ∈ S, degree w S x ≤ 2) (equal : energy w S=12) :
    L.card=14 ∧ ∀ x ∈ S, degree w L x=6 := by
  have two : ∀ x ∈ S, degree w S x=2 := by
    apply (Finset.sum_eq_sum_iff_of_le internal).mp
    simpa [energy,card] using equal
  let B := L \ S
  have outside : ∀ y ∈ B, 3 ≤ degree w S y := by
    intro y hy
    by_contra small
    have dy : degree w S y ≤ 2 := by omega
    have noWeight : ∀ x ∈ S, w x y=0 := by
      intro x hx
      have exchange := swap_inequality w symm zero L S minimal x y hx hy
      rw [two x hx] at exchange
      omega
    have empty : degree w S y=0 := by
      apply Finset.sum_eq_zero
      intro x hx
      rw [symm y x,noWeight x hx]
    obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
    have exchange := swap_inequality w symm zero L S minimal x y hx hy
    rw [two x hx,empty] at exchange
    omega
  let cut := ∑ x ∈ S, degree w B x
  have transpose : (∑ y ∈ B, degree w S y)=cut := by
    dsimp [degree,cut]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro x hx
    exact Finset.sum_congr rfl (fun y _ => symm y x)
  have lower : 3*B.card ≤ cut := by
    have bound := Finset.sum_le_sum outside
    rw [transpose] at bound
    simpa [Nat.mul_comm] using bound
  have split : energy w S + cut = ∑ x ∈ S, degree w L x := by
    rw [energy,← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun x _ => degree_split w L S minimal.1 x)
  have upper : (∑ x ∈ S, degree w L x) ≤ 36 := by
    have bound := Finset.sum_le_sum (s := S) (fun x hx => maximum x (minimal.1 hx))
    simpa [card] using bound
  have cards : B.card+S.card=L.card := Finset.card_sdiff_add_card_eq_card minimal.1
  have cardL : L.card=14 := by omega
  have full : (∑ x ∈ S, degree w L x)=36 := by omega
  refine ⟨cardL,?_⟩
  apply (Finset.sum_eq_sum_iff_of_le (fun x hx => maximum x (minimal.1 hx))).mp
  simpa [card] using full

end Aris4Math.ThirtyFour.WeightedSubsetSelection
