import Aris4Math.ThirtyThree.TwentyFourFourLowData

/-! Exact local certificates for four degree-six unit locks with one triple. -/
namespace Aris4Math.ThirtyThree.TwentyFourTripleLowData
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open Aris4Math.ThirtyThree.TwentyFourFourLowData (positions)
open scoped BigOperators

def counts (T : Finset (Fin 4)) : ℕ :=
  recovered 33 (fun _ => 6) (fun _ => 1) ![1,0,0,0,0] T

def p (i : Fin 12) : Numeric.Profile :=
  pruneZero ⟨24, executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, counts T⟩), none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Fin 12) : p i =
    profile (positions i) counts (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 12 → Numeric.Profile := ![⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[12],4⟩,⟨[13],4⟩,⟨[11,12,13],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩],none,[11,12,13,14]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[12],4⟩,⟨[14],4⟩,⟨[11,12,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[13,14],1⟩],none,[11,12,14,13]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[13],4⟩,⟨[12],4⟩,⟨[11,12,13],1⟩,⟨[14],3⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩],none,[11,13,12,14]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[13],4⟩,⟨[14],4⟩,⟨[11,13,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[12,14],1⟩],none,[11,13,14,12]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[14],4⟩,⟨[12],4⟩,⟨[11,12,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[13,14],1⟩,⟨[12,13],1⟩],none,[11,14,12,13]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[11],4⟩,⟨[14],4⟩,⟨[13],4⟩,⟨[11,13,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[12,13],1⟩],none,[11,14,13,12]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[11],4⟩,⟨[13],4⟩,⟨[11,12,13],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩],none,[12,11,13,14]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[11],4⟩,⟨[14],4⟩,⟨[11,12,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[13,14],1⟩],none,[12,11,14,13]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[13],4⟩,⟨[11],4⟩,⟨[11,12,13],1⟩,⟨[14],3⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11,14],1⟩],none,[12,13,11,14]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[13],4⟩,⟨[14],4⟩,⟨[12,13,14],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩],none,[12,13,14,11]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[14],4⟩,⟨[11],4⟩,⟨[11,12,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[11,13],1⟩],none,[12,14,11,13]⟩,⟨24,[11,12,13,14],[⟨[],14⟩,⟨[12],4⟩,⟨[14],4⟩,⟨[13],4⟩,⟨[12,13,14],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[11,14],1⟩,⟨[11,13],1⟩],none,[12,14,13,11]⟩]
theorem p_eq_computed (i : Fin 12) : p i = computed i := by fin_cases i <;> rfl

def slotFirst : Fin 4 → Fin 7 → Finset (Fin 4) := ![![{0},{0},{0},{0,1,2},{0,1,2},{0,1,2},{0,1,2}],![{1},{1},{1},{0,1,2},{0,1,2},{0,1,2},{0,1,2}],![{2},{2},{2},{0,1,2},{0,1,2},{0,1,2},{0,1,2}],![{3},{3},{3},{3},{0,3},{0,3},{1,3}]]
def slotSecond : Fin 4 → Fin 7 → Finset (Fin 4) := ![![{0},{0,1,2},{0,3},{0,3},{0,3},{0,3},{0,3}],![{1},{0,1,2},{1,3},{1,3},{1,3},{1,3},{1,3}],![{2},{0,1,2},{2,3},{2,3},{2,3},{2,3},{2,3}],![{3},{0,3},{1,3},{2,3},{1,3},{2,3},{2,3}]]
def weightNumer : Fin 12 → Fin 4 → Fin 7 → ℕ := ![![![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,273,156,585,585,585,585],![168,156,156,156,0,0,0]],![![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,156,156,156,0,312,312]],![![168,273,156,0,0,0,0],![168,273,156,585,585,585,585],![168,0,156,0,0,0,0],![168,156,156,156,0,0,0]],![![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,156,156,156,312,312,0]],![![168,273,156,0,0,0,0],![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,156,156,156,312,0,312]],![![168,273,156,0,0,0,0],![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,156,156,156,312,312,0]],![![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,273,156,585,585,585,585],![168,156,156,156,0,0,0]],![![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,273,156,0,0,0,0],![168,156,156,156,0,312,312]],![![168,0,156,0,0,0,0],![168,273,156,585,585,585,585],![168,273,156,0,0,0,0],![168,156,156,156,0,0,0]],![![168,273,156,585,585,585,585],![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,156,156,156,0,0,0]],![![168,0,156,0,0,0,0],![168,273,156,0,0,0,0],![168,273,156,0,0,0,0],![168,156,156,156,312,0,312]],![![168,273,156,585,585,585,585],![168,273,156,0,0,0,0],![168,0,156,0,0,0,0],![168,156,156,156,0,0,0]]]
def baseNumer : Fin 12 → ℕ := ![17217,17256,17217,17256,17256,17256,17217,17256,17217,17217,17256,17217]

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
    slotWeight i j s = (weightNumer i j s : ℚ)/16796 := by
  simp only [slotWeight,p_eq_computed]
  decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem baseline : ∀ i : Fin 12, Numeric.validProfile (p i) 33 ∧
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)))) =
        (baseNumer i : ℚ)/16796 ∧
    ∀ j : Fin 4, min (Numeric.boundA (p i) ((positions i j).val+1))
      (min (Numeric.boundB (p i) ((positions i j).val+1))
        (Numeric.boundC (p i) ((positions i j).val+1))) =
      Numeric.boundC (p i) ((positions i j).val+1) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- The seven-slot padding repeats three existing slots at the first three
centers, so it covers the original 4^3*7 domain without extra assumptions. -/
theorem order_covers : ∀ s : Fin 4 → Fin 7, ∃ i : Fin 12,
    baseNumer i < 16796 + ∑ j : Fin 4, weightNumer i j (s j) := by decide +kernel

end Aris4Math.ThirtyThree.TwentyFourTripleLowData
#print axioms Aris4Math.ThirtyThree.TwentyFourTripleLowData.slotWeight_eq
#print axioms Aris4Math.ThirtyThree.TwentyFourTripleLowData.baseline
#print axioms Aris4Math.ThirtyThree.TwentyFourTripleLowData.order_covers
