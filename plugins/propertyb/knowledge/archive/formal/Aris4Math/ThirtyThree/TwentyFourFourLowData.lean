import Aris4Math.ThirtyThree.QuadProfiles

/-! Finite local data for four unit-codegree degree-six locks with only
pair traces at 24 vertices. No hypergraphs are enumerated. -/
namespace Aris4Math.ThirtyThree.TwentyFourFourLowData
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open scoped BigOperators

def positionFn : Fin 12 → Fin 4 → Fin 24 := ![![10,11,12,13],![10,11,13,12],![10,12,11,13],![10,12,13,11],![10,13,11,12],![10,13,12,11],![11,10,12,13],![11,10,13,12],![11,12,10,13],![11,12,13,10],![11,13,10,12],![11,13,12,10]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel

def positions (i : Fin 12) : Fin 4 ↪ Fin 24 := ⟨positionFn i,positionFn_injective i⟩
def counts (T : Finset (Fin 4)) : ℕ := if T.card=0 then 15 else if T.card=1 then 3 else if T.card=2 then 1 else 0

def p (i : Fin 12) : Numeric.Profile :=
  pruneZero ⟨24, executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, counts T⟩), none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Fin 12) : p i =
    profile (positions i) counts (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 12 → Numeric.Profile := ![⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩],none,[11,12,13,14]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[13,14],1⟩],none,[11,12,14,13]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩],none,[11,13,12,14]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[12,14],1⟩],none,[11,13,14,12]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[13,14],1⟩,⟨[12,13],1⟩],none,[11,14,12,13]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[11],3⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[13,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[12,13],1⟩],none,[11,14,13,12]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩],none,[12,11,13,14]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[13,14],1⟩],none,[12,11,14,13]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11,14],1⟩],none,[12,13,11,14]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩],none,[12,13,14,11]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[11,13],1⟩],none,[12,14,11,13]⟩,⟨24,[11,12,13,14],[⟨[],15⟩,⟨[12],3⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,14],1⟩,⟨[11,13],1⟩],none,[12,14,13,11]⟩]
theorem p_eq_computed (i : Fin 12) : p i = computed i := by fin_cases i <;> rfl

def slotFirst : Fin 4 → Fin 7 → Finset (Fin 4) := ![![{0},{0},{0},{0},{0,1},{0,1},{0,2}],![{1},{1},{1},{1},{0,1},{0,1},{1,2}],![{2},{2},{2},{2},{0,2},{0,2},{1,2}],![{3},{3},{3},{3},{0,3},{0,3},{1,3}]]
def slotSecond : Fin 4 → Fin 7 → Finset (Fin 4) := ![![{0},{0,1},{0,2},{0,3},{0,2},{0,3},{0,3}],![{1},{0,1},{1,2},{1,3},{1,2},{1,3},{1,3}],![{2},{0,2},{1,2},{2,3},{1,2},{2,3},{2,3}],![{3},{0,3},{1,3},{2,3},{1,3},{2,3},{2,3}]]
def weightNumer : Fin 12 → Fin 4 → Fin 7 → ℕ := ![![![42,39,39,39,0,0,0],![42,39,39,39,78,78,0],![42,39,39,39,0,78,78],![42,39,39,39,0,0,0]],![![42,39,39,39,0,0,0],![42,39,39,39,78,78,0],![42,39,39,39,0,0,0],![42,39,39,39,0,78,78]],![![42,39,39,39,0,0,0],![42,39,39,39,0,78,78],![42,39,39,39,78,78,0],![42,39,39,39,0,0,0]],![![42,39,39,39,0,0,0],![42,39,39,39,78,0,78],![42,39,39,39,0,0,0],![42,39,39,39,78,78,0]],![![42,39,39,39,0,0,0],![42,39,39,39,0,0,0],![42,39,39,39,78,78,0],![42,39,39,39,78,0,78]],![![42,39,39,39,0,0,0],![42,39,39,39,0,0,0],![42,39,39,39,78,0,78],![42,39,39,39,78,78,0]],![![42,39,39,39,78,78,0],![42,39,39,39,0,0,0],![42,39,39,39,0,78,78],![42,39,39,39,0,0,0]],![![42,39,39,39,78,78,0],![42,39,39,39,0,0,0],![42,39,39,39,0,0,0],![42,39,39,39,0,78,78]],![![42,39,39,39,78,0,78],![42,39,39,39,0,78,78],![42,39,39,39,0,0,0],![42,39,39,39,0,0,0]],![![42,39,39,39,0,78,78],![42,39,39,39,78,0,78],![42,39,39,39,0,0,0],![42,39,39,39,0,0,0]],![![42,39,39,39,78,0,78],![42,39,39,39,0,0,0],![42,39,39,39,0,0,0],![42,39,39,39,78,0,78]],![![42,39,39,39,0,78,78],![42,39,39,39,0,0,0],![42,39,39,39,78,0,78],![42,39,39,39,0,0,0]]]

def slotWeight (i : Fin 12) (j : Fin 4) (s : Fin 7) : ℚ :=
  Numeric.pairWeight (p i)
    ⟨executableType (positions i) (slotFirst j s),0⟩
    ⟨executableType (positions i) (slotSecond j s),0⟩ ((positions i j).val+1) +
  Numeric.pairWeight (p i)
    ⟨executableType (positions i) (slotSecond j s),0⟩
    ⟨executableType (positions i) (slotFirst j s),0⟩ ((positions i j).val+1)

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem slotWeight_eq : ∀ i j s,
    slotWeight i j s = (weightNumer i j s : ℚ)/4199 := by
  simp only [slotWeight,p_eq_computed]
  decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem baseline : ∀ i : Fin 12, Numeric.validProfile (p i) 33 ∧
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)))) = 8535/8398 ∧
    ∀ j : Fin 4, min (Numeric.boundA (p i) ((positions i j).val+1))
      (min (Numeric.boundB (p i) ((positions i j).val+1))
        (Numeric.boundC (p i) ((positions i j).val+1))) =
      Numeric.boundC (p i) ((positions i j).val+1) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- Every tuple of the seven actual bad-pair slots has a usable lock order. -/
theorem order_covers : ∀ s : Fin 4 → Fin 7, ∃ i : Fin 12,
    78 ≤ ∑ j : Fin 4, weightNumer i j (s j) := by decide +kernel

end Aris4Math.ThirtyThree.TwentyFourFourLowData
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLowData.slotWeight_eq
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLowData.baseline
#print axioms Aris4Math.ThirtyThree.TwentyFourFourLowData.order_covers
