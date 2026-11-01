import Aris4Math.ThirtyThree.FiveProfiles

/-! Two exact profiles for a full edge of five degree-six locks, with zero
or one exceptional internal pair. Their uncorrected bounds already suffice. -/
namespace Aris4Math.ThirtyThree.TwentyFourFullFiveData
open FiveProfiles
open TripleProfiles (pruneZero)

def positionFn : Fin 2 → Fin 5 → Fin 24 := ![![9,10,11,12,13],![9,13,10,11,12]]
theorem positionFn_injective : ∀ k, Function.Injective (positionFn k) := by decide +kernel
def positions (k : Fin 2) : Fin 5 ↪ Fin 24 := ⟨positionFn k,positionFn_injective k⟩

def low (k : Fin 2) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then 6 else
  if k = 1 ∧ T = {0,1} then 2 else 1

def high (T : Finset (Fin 5)) : ℕ := if T = Finset.univ then 1 else 0

def counts (k : Fin 2) (T : Finset (Fin 5)) : ℕ :=
  if T = Finset.univ then 1 else
  if T = ∅ then if k = 0 then 7 else 8 else
  if T.card = 1 then if k = 1 ∧ T ⊆ {0,1} then 4 else 5 else
  if k = 1 ∧ T = {0,1} then 1 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovered_eq : ∀ k T, MultiLockRecovery.recovered (low k) high T = counts k T := by
  decide +kernel

def p (k : Fin 2) : Numeric.Profile :=
  pruneZero ⟨24,executableType (positions k) Finset.univ,
    labels.map (fun T => ⟨executableType (positions k) T,counts k T⟩),none,[]⟩
theorem p_eq (k : Fin 2) : p k = profile (positions k) (counts k) [] := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 2 → Numeric.Profile := ![
  ⟨24,[10,11,12,13,14],[⟨[],7⟩,⟨[10],5⟩,⟨[11],5⟩,⟨[12],5⟩,
    ⟨[13],5⟩,⟨[14],5⟩,⟨[10,11,12,13,14],1⟩],none,[]⟩,
  ⟨24,[10,11,12,13,14],[⟨[],8⟩,⟨[10],4⟩,⟨[14],4⟩,⟨[10,14],1⟩,
    ⟨[11],5⟩,⟨[12],5⟩,⟨[13],5⟩,⟨[10,11,12,13,14],1⟩],none,[]⟩]

theorem p_eq_computed (k : Fin 2) : p k = computed k := by fin_cases k <;> rfl

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem certificates : ∀ k : Fin 2, Numeric.validProfile (p k) 33 ∧
    Numeric.totalBound (p k) < 1 ∧ (p k).emptyPairCap = none ∧
    (p k).correctionCenters = [] := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem exact_bounds : Numeric.totalBound (p 0) = (8071:ℚ)/8398 ∧
    Numeric.totalBound (p 1) = (224:ℚ)/247 := by
  simp only [p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyThree.TwentyFourFullFiveData
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFiveData.recovered_eq
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFiveData.certificates
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFiveData.exact_bounds
