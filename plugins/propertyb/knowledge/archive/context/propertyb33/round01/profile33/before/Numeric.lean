import Mathlib.Data.List.Sort
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-! Closed arithmetic obligations for the Property B proof.
This module does not assert that an arbitrary hypergraph admits any profile.
The types below store actual locked POSITIONS (one-based), not vertex labels.
All proofs are checked by the Lean kernel; no native evaluator is used. -/

namespace Aris4Math.Numeric
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Fast binomial computation, propositionally equal to `Nat.choose` for all inputs. -/
def binom := Nat.fast_choose

theorem binom_eq_choose (n k : Nat) : binom n k = Nat.choose n k := by
  exact (congrFun (congrFun Nat.choose_eq_fast_choose n) k).symm

structure EdgeType where
  locks : List Nat
  count : Nat
  deriving DecidableEq, Repr

structure Profile where
  v : Nat
  positions : List Nat
  types : List EdgeType
  emptyPairCap : Option Nat := none
  correctionCenters : List Nat := []
  deriving Repr

def qsum (xs : List Rat) : Rat := xs.foldl (· + ·) 0

def freeCount (p : Profile) : Nat := p.v - p.positions.length

def leftCount (p : Profile) (k : Nat) : Nat :=
  k - 1 - (p.positions.filter (· < k)).length

def rightCount (p : Profile) (k : Nat) : Nat :=
  p.v - k - (p.positions.filter (k < ·)).length

/-- P2a/P2b, including compatibility before evaluating fractions. -/
def edgeWeight (p : Profile) (t : EdgeType) (k : Nat) (last : Bool) : Rat :=
  let N := freeCount p
  let r := 5 - t.locks.length
  let fits := fun j => if last then j < k else k < j
  let slots := if last then leftCount p k else rightCount p k
  if k ∈ p.positions then
    if k ∈ t.locks ∧ (t.locks.filter (· != k)).all fits then
      (binom slots r : Rat) / binom N r
    else 0
  else
    if 1 ≤ r ∧ t.locks.all fits then
      ((r * binom slots (r - 1) : Nat) : Rat) / (N * binom (N - 1) (r - 1) : Nat)
    else 0

/-- P3/P4: fixed ordered pair weight; there is no extra r*q factor. -/
def pairWeight (p : Profile) (t u : EdgeType) (k : Nat) : Rat :=
  let N := freeCount p
  let r := 5 - t.locks.length
  let q := 5 - u.locks.length
  let a := leftCount p k
  let b := rightCount p k
  if k ∈ p.positions then
    if t.locks.filter (· ∈ u.locks) = [k] ∧
        (t.locks.filter (· != k)).all (· < k) ∧
        (u.locks.filter (· != k)).all (k < ·) ∧ r + q ≤ N then
      ((binom a r * binom b q : Nat) : Rat) / (binom N r * binom (N - r) q : Nat)
    else 0
  else
    if 1 ≤ r ∧ 1 ≤ q ∧ t.locks.all (· ∉ u.locks) ∧
        t.locks.all (· < k) ∧ u.locks.all (k < ·) ∧ r + q - 1 ≤ N then
      ((binom a (r - 1) * binom b (q - 1) : Nat) : Rat) /
        (N * binom (N - 1) (r - 1) * binom (N - r) (q - 1) : Nat)
    else 0

def pairCount (p : Profile) (t u : EdgeType) : Nat :=
  let m := t.count * (u.count - if t.locks = u.locks then 1 else 0)
  if t.locks = [] ∧ u.locks = [] then p.emptyPairCap.getD m else m

def boundA (p : Profile) (k : Nat) : Rat :=
  qsum (p.types.map fun t => (t.count : Rat) * edgeWeight p t k true)

def boundB (p : Profile) (k : Nat) : Rat :=
  qsum (p.types.map fun t => (t.count : Rat) * edgeWeight p t k false)

def boundC (p : Profile) (k : Nat) : Rat :=
  qsum (p.types.flatMap fun t => p.types.map fun u =>
    (pairCount p t u : Rat) * pairWeight p t u k)

/-- All distinct unordered pair slots at k, weighted by BOTH directions. -/
def linkSlots (p : Profile) (k : Nat) : List Rat :=
  let ts := p.types.filter fun t => k ∈ t.locks
  ts.zipIdx |>.flatMap fun (t,i) =>
    (ts.drop i).flatMap fun u =>
      let capacity := if t.locks = u.locks then binom t.count 2 else t.count * u.count
      List.replicate capacity (pairWeight p t u k + pairWeight p u t k)

def linkDegree (p : Profile) (k : Nat) : Nat :=
  ((p.types.filter fun t => k ∈ t.locks).map EdgeType.count).foldl (· + ·) 0

/-- Numerical P8 input; its applicability to a hypergraph is a separate theorem. -/
def linkQLower (p : Profile) (k : Nat) : Nat :=
  (4 * linkDegree p k - (p.v - 1) + 2) / 3

/-- Sum of the cheapest q unordered slots, allowing zero weights. -/
def deduction (p : Profile) (k : Nat) : Rat :=
  if k ∈ p.correctionCenters then
    qsum (((linkSlots p k).insertionSort (· ≤ ·)).take (linkQLower p k))
  else 0

/-- P7: change C first and only THEN take the minimum. -/
def positionBound (p : Profile) (k : Nat) : Rat :=
  min (boundA p k) (min (boundB p k) (boundC p k - deduction p k))

def totalBound (p : Profile) : Rat :=
  qsum ((List.range p.v).map fun i => positionBound p (i + 1))

/-- Inputs used here satisfy the elementary profile well-formedness constraints.
This checks only data; it is not the structural existence theorem. -/
def validProfile (p : Profile) : Prop :=
  p.positions.Nodup ∧ p.positions.Pairwise (· < ·) ∧
  (p.positions.all fun k => 1 ≤ k && k ≤ p.v) ∧
  (p.types.map EdgeType.locks).Nodup ∧
  (p.types.all fun t => t.locks.Nodup && t.locks.Pairwise (· < ·) &&
    t.locks.all (· ∈ p.positions) &&
    t.locks.length ≤ 5 && 5 - t.locks.length ≤ freeCount p && 0 < t.count) ∧
  (p.types.map EdgeType.count).foldl (· + ·) 0 = 32 ∧
  (p.correctionCenters.all (· ∈ p.positions)) ∧
  (p.emptyPairCap = none ∨
    p.positions = [] ∧ p.types = [⟨[], 32⟩] ∧ p.emptyPairCap.getD 992 ≤ 992)

-- BEGIN GENERATED CLOSED CERTIFICATES
/- Static inputs correspond to results/reproduced_bounds.json.
Expected fractions are conclusions proved by kernel reduction,
never hypotheses. Both unused diagnostic profiles are retained. -/

-- v19: masks/counts {'0': 32}
def v19 : Profile :=
  ⟨19, [], [⟨[], 32⟩], none, []⟩
theorem v19_valid : validProfile v19 := by unfold validProfile; decide +kernel
theorem v19_value : totalBound v19 = (222656 / 230945 : Rat) := by
  decide +kernel
#print axioms v19_value
theorem v19_lt_one : totalBound v19 < 1 := by
  rw [v19_value]
  norm_num

-- v20: masks/counts {'0': 32}
def v20 : Profile :=
  ⟨20, [], [⟨[], 32⟩], some 948, []⟩
theorem v20_valid : validProfile v20 := by unfold validProfile; decide +kernel
theorem v20_value : totalBound v20 = (20874 / 20995 : Rat) := by
  decide +kernel
#print axioms v20_value
theorem v20_lt_one : totalBound v20 < 1 := by
  rw [v20_value]
  norm_num

-- v21_d5: masks/counts {'0': 27, '1': 5}
def v21_d5 : Profile :=
  ⟨21, [11], [⟨[], 27⟩, ⟨[11], 5⟩], none, []⟩
theorem v21_d5_valid : validProfile v21_d5 := by unfold validProfile; decide +kernel
theorem v21_d5_value : totalBound v21_d5 = (483 / 494 : Rat) := by
  decide +kernel
#print axioms v21_d5_value
theorem v21_d5_lt_one : totalBound v21_d5 < 1 := by
  rw [v21_d5_value]
  norm_num

-- v21_d6: masks/counts {'0': 26, '1': 6}
def v21_d6 : Profile :=
  ⟨21, [11], [⟨[], 26⟩, ⟨[11], 6⟩], none, []⟩
theorem v21_d6_valid : validProfile v21_d6 := by unfold validProfile; decide +kernel
theorem v21_d6_value : totalBound v21_d6 = (4179 / 4199 : Rat) := by
  decide +kernel
#print axioms v21_d6_value
theorem v21_d6_lt_one : totalBound v21_d6 < 1 := by
  rw [v21_d6_value]
  norm_num

-- v21_d7: masks/counts {'0': 25, '1': 7}
def v21_d7 : Profile :=
  ⟨21, [11], [⟨[], 25⟩, ⟨[11], 7⟩], none, [11]⟩
theorem v21_d7_valid : validProfile v21_d7 := by unfold validProfile; decide +kernel
theorem v21_d7_value : totalBound v21_d7 = (8337 / 8398 : Rat) := by
  decide +kernel
#print axioms v21_d7_value
theorem v21_d7_base_value : totalBound { v21_d7 with correctionCenters := [] } = (8589 / 8398 : Rat) := by
  decide +kernel
theorem v21_d7_link_11 :
    linkQLower v21_d7 11 = 3 ∧
    3 ≤ (linkSlots v21_d7 11).length ∧
    deduction v21_d7 11 = (126 / 4199 : Rat) ∧
    0 ≤ deduction v21_d7 11 ∧ deduction v21_d7 11 ≤ boundC v21_d7 11 := by
  decide +kernel
theorem v21_d7_lt_one : totalBound v21_d7 < 1 := by
  rw [v21_d7_value]
  norm_num

-- v22_66: masks/counts {'0': 21, '1': 5, '2': 5, '3': 1}
def v22_66 : Profile :=
  ⟨22, [11, 12], [⟨[], 21⟩, ⟨[11], 5⟩, ⟨[12], 5⟩, ⟨[11, 12], 1⟩], none, []⟩
theorem v22_66_valid : validProfile v22_66 := by unfold validProfile; decide +kernel
theorem v22_66_value : totalBound v22_66 = (8193 / 8398 : Rat) := by
  decide +kernel
#print axioms v22_66_value
theorem v22_66_lt_one : totalBound v22_66 < 1 := by
  rw [v22_66_value]
  norm_num

-- v22_67: masks/counts {'0': 20, '1': 5, '2': 6, '3': 1}
def v22_67 : Profile :=
  ⟨22, [11, 12], [⟨[], 20⟩, ⟨[11], 5⟩, ⟨[12], 6⟩, ⟨[11, 12], 1⟩], none, [12]⟩
theorem v22_67_valid : validProfile v22_67 := by unfold validProfile; decide +kernel
theorem v22_67_value : totalBound v22_67 = (4092 / 4199 : Rat) := by
  decide +kernel
#print axioms v22_67_value
theorem v22_67_base_value : totalBound { v22_67 with correctionCenters := [] } = (4209 / 4199 : Rat) := by
  decide +kernel
theorem v22_67_link_12 :
    linkQLower v22_67 12 = 3 ∧
    3 ≤ (linkSlots v22_67 12).length ∧
    deduction v22_67 12 = (9 / 323 : Rat) ∧
    0 ≤ deduction v22_67 12 ∧ deduction v22_67 12 ≤ boundC v22_67 12 := by
  decide +kernel
theorem v22_67_lt_one : totalBound v22_67 < 1 := by
  rw [v22_67_value]
  norm_num

-- v22_77: masks/counts {'0': 19, '1': 6, '2': 6, '3': 1}
def v22_77 : Profile :=
  ⟨22, [11, 12], [⟨[], 19⟩, ⟨[11], 6⟩, ⟨[12], 6⟩, ⟨[11, 12], 1⟩], none, [11, 12]⟩
theorem v22_77_valid : validProfile v22_77 := by unfold validProfile; decide +kernel
theorem v22_77_value : totalBound v22_77 = (8175 / 8398 : Rat) := by
  decide +kernel
#print axioms v22_77_value
theorem v22_77_base_value : totalBound { v22_77 with correctionCenters := [] } = (8643 / 8398 : Rat) := by
  decide +kernel
theorem v22_77_link_11 :
    linkQLower v22_77 11 = 3 ∧
    3 ≤ (linkSlots v22_77 11).length ∧
    deduction v22_77 11 = (9 / 323 : Rat) ∧
    0 ≤ deduction v22_77 11 ∧ deduction v22_77 11 ≤ boundC v22_77 11 := by
  decide +kernel
theorem v22_77_link_12 :
    linkQLower v22_77 12 = 3 ∧
    3 ≤ (linkSlots v22_77 12).length ∧
    deduction v22_77 12 = (9 / 323 : Rat) ∧
    0 ≤ deduction v22_77 12 ∧ deduction v22_77 12 ≤ boundC v22_77 12 := by
  decide +kernel
theorem v22_77_lt_one : totalBound v22_77 < 1 := by
  rw [v22_77_value]
  norm_num

-- v23_66: masks/counts {'0': 21, '1': 5, '2': 5, '3': 1}
def v23_66 : Profile :=
  ⟨23, [11, 12], [⟨[], 21⟩, ⟨[11], 5⟩, ⟨[12], 5⟩, ⟨[11, 12], 1⟩], none, [11, 12]⟩
theorem v23_66_valid : validProfile v23_66 := by unfold validProfile; decide +kernel
theorem v23_66_value : totalBound v23_66 = (117203 / 117572 : Rat) := by
  decide +kernel
#print axioms v23_66_value
theorem v23_66_base_value : totalBound { v23_66 with correctionCenters := [] } = (29837 / 29393 : Rat) := by
  decide +kernel
theorem v23_66_link_11 :
    linkQLower v23_66 11 = 1 ∧
    1 ≤ (linkSlots v23_66 11).length ∧
    deduction v23_66 11 = (11 / 1292 : Rat) ∧
    0 ≤ deduction v23_66 11 ∧ deduction v23_66 11 ≤ boundC v23_66 11 := by
  decide +kernel
theorem v23_66_link_12 :
    linkQLower v23_66 12 = 1 ∧
    1 ≤ (linkSlots v23_66 12).length ∧
    deduction v23_66 12 = (22 / 2261 : Rat) ∧
    0 ≤ deduction v23_66 12 ∧ deduction v23_66 12 ≤ boundC v23_66 12 := by
  decide +kernel
theorem v23_66_lt_one : totalBound v23_66 < 1 := by
  rw [v23_66_value]
  norm_num

-- v23_67: masks/counts {'0': 20, '1': 5, '2': 6, '3': 1}
def v23_67 : Profile :=
  ⟨23, [11, 12], [⟨[], 20⟩, ⟨[11], 5⟩, ⟨[12], 6⟩, ⟨[11, 12], 1⟩], none, []⟩
theorem v23_67_valid : validProfile v23_67 := by unfold validProfile; decide +kernel
theorem v23_67_value : totalBound v23_67 = (122609 / 117572 : Rat) := by
  decide +kernel
#print axioms v23_67_value
theorem v23_67_gt_one : totalBound v23_67 > 1 := by
  rw [v23_67_value]
  norm_num

-- v23_677: masks/counts {'0': 15, '1': 4, '2': 5, '4': 5, '3': 1, '5': 1, '6': 1}
def v23_677 : Profile :=
  ⟨23, [11, 12, 13], [⟨[], 15⟩, ⟨[11], 4⟩, ⟨[12], 5⟩, ⟨[13], 5⟩, ⟨[11, 12], 1⟩, ⟨[11, 13], 1⟩, ⟨[12, 13], 1⟩], none, [12, 13]⟩
theorem v23_677_valid : validProfile v23_677 := by unfold validProfile; decide +kernel
theorem v23_677_value : totalBound v23_677 = (645 / 646 : Rat) := by
  decide +kernel
#print axioms v23_677_value
theorem v23_677_base_value : totalBound { v23_677 with correctionCenters := [] } = (39 / 38 : Rat) := by
  decide +kernel
theorem v23_677_link_12 :
    linkQLower v23_677 12 = 2 ∧
    2 ≤ (linkSlots v23_677 12).length ∧
    deduction v23_677 12 = (6 / 323 : Rat) ∧
    0 ≤ deduction v23_677 12 ∧ deduction v23_677 12 ≤ boundC v23_677 12 := by
  decide +kernel
theorem v23_677_link_13 :
    linkQLower v23_677 13 = 2 ∧
    2 ≤ (linkSlots v23_677 13).length ∧
    deduction v23_677 13 = (3 / 323 : Rat) ∧
    0 ≤ deduction v23_677 13 ∧ deduction v23_677 13 ≤ boundC v23_677 13 := by
  decide +kernel
theorem v23_677_lt_one : totalBound v23_677 < 1 := by
  rw [v23_677_value]
  norm_num

-- v24_K4-1: masks/counts {'0': 14, '1': 3, '2': 3, '4': 3, '8': 3, '3': 1, '5': 1, '9': 1, '6': 1, '10': 1, '12': 1}
def v24_K4_1 : Profile :=
  ⟨24, [11, 12, 13, 14], [⟨[], 14⟩, ⟨[11], 3⟩, ⟨[12], 3⟩, ⟨[13], 3⟩, ⟨[14], 3⟩, ⟨[11, 12], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 13], 1⟩, ⟨[12, 14], 1⟩, ⟨[13, 14], 1⟩], none, []⟩
theorem v24_K4_1_valid : validProfile v24_K4_1 := by unfold validProfile; decide +kernel
theorem v24_K4_1_value : totalBound v24_K4_1 = (243 / 247 : Rat) := by
  decide +kernel
#print axioms v24_K4_1_value
theorem v24_K4_1_lt_one : totalBound v24_K4_1 < 1 := by
  rw [v24_K4_1_value]
  norm_num

-- v24_K4-2: masks/counts {'0': 13, '1': 4, '2': 4, '4': 4, '8': 3, '7': 1, '9': 1, '10': 1, '12': 1}
def v24_K4_2 : Profile :=
  ⟨24, [11, 12, 13, 14], [⟨[], 13⟩, ⟨[11], 4⟩, ⟨[12], 4⟩, ⟨[13], 4⟩, ⟨[14], 3⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 14], 1⟩, ⟨[13, 14], 1⟩], none, []⟩
theorem v24_K4_2_valid : validProfile v24_K4_2 := by unfold validProfile; decide +kernel
theorem v24_K4_2_value : totalBound v24_K4_2 = (16671 / 16796 : Rat) := by
  decide +kernel
#print axioms v24_K4_2_value
theorem v24_K4_2_lt_one : totalBound v24_K4_2 < 1 := by
  rw [v24_K4_2_value]
  norm_num

-- v24_K4-3: masks/counts {'0': 11, '1': 5, '2': 5, '4': 5, '8': 5, '15': 1}
def v24_K4_3 : Profile :=
  ⟨24, [11, 12, 13, 14], [⟨[], 11⟩, ⟨[11], 5⟩, ⟨[12], 5⟩, ⟨[13], 5⟩, ⟨[14], 5⟩, ⟨[11, 12, 13, 14], 1⟩], none, []⟩
theorem v24_K4_3_valid : validProfile v24_K4_3 := by unfold validProfile; decide +kernel
theorem v24_K4_3_value : totalBound v24_K4_3 = (8323 / 8398 : Rat) := by
  decide +kernel
#print axioms v24_K4_3_value
theorem v24_K4_3_lt_one : totalBound v24_K4_3 < 1 := by
  rw [v24_K4_3_value]
  norm_num

-- v25_K6-1: masks/counts {'0': 11, '1': 1, '2': 1, '4': 1, '8': 1, '16': 1, '32': 1, '3': 1, '5': 1, '9': 1, '17': 1, '33': 1, '6': 1, '10': 1, '18': 1, '34': 1, '12': 1, '20': 1, '36': 1, '24': 1, '40': 1, '48': 1}
def v25_K6_1 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 11⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 1⟩, ⟨[15], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[11, 12], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 13], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
theorem v25_K6_1_valid : validProfile v25_K6_1 := by unfold validProfile; decide +kernel
theorem v25_K6_1_value : totalBound v25_K6_1 = (4188 / 4199 : Rat) := by
  decide +kernel
#print axioms v25_K6_1_value
theorem v25_K6_1_lt_one : totalBound v25_K6_1 < 1 := by
  rw [v25_K6_1_value]
  norm_num

-- v25_K6-2: masks/counts {'0': 10, '1': 2, '2': 2, '4': 2, '8': 1, '16': 1, '32': 1, '7': 1, '9': 1, '17': 1, '33': 1, '10': 1, '18': 1, '34': 1, '12': 1, '20': 1, '36': 1, '24': 1, '40': 1, '48': 1}
def v25_K6_2 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 10⟩, ⟨[10], 2⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 1⟩, ⟨[14], 1⟩, ⟨[15], 1⟩, ⟨[10, 11, 12], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 13], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
theorem v25_K6_2_valid : validProfile v25_K6_2 := by unfold validProfile; decide +kernel
theorem v25_K6_2_value : totalBound v25_K6_2 = (4170 / 4199 : Rat) := by
  decide +kernel
#print axioms v25_K6_2_value
theorem v25_K6_2_lt_one : totalBound v25_K6_2 < 1 := by
  rw [v25_K6_2_value]
  norm_num

-- v25_K6-3: masks/counts {'0': 9, '1': 2, '2': 2, '4': 2, '8': 3, '16': 2, '32': 1, '3': 1, '5': 1, '25': 1, '33': 1, '14': 1, '18': 1, '34': 1, '20': 1, '36': 1, '40': 1, '48': 1}
def v25_K6_3 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 9⟩, ⟨[10], 2⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 3⟩, ⟨[14], 2⟩, ⟨[15], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
theorem v25_K6_3_valid : validProfile v25_K6_3 := by unfold validProfile; decide +kernel
theorem v25_K6_3_value : totalBound v25_K6_3 = (8297 / 8398 : Rat) := by
  decide +kernel
#print axioms v25_K6_3_value
theorem v25_K6_3_lt_one : totalBound v25_K6_3 < 1 := by
  rw [v25_K6_3_value]
  norm_num

-- v25_K6-4: masks/counts {'0': 9, '1': 2, '2': 2, '4': 2, '8': 2, '16': 2, '32': 2, '3': 1, '5': 1, '9': 1, '49': 1, '14': 1, '18': 1, '34': 1, '20': 1, '36': 1, '24': 1, '40': 1}
def v25_K6_4 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 9⟩, ⟨[10], 2⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 2⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩], none, []⟩
theorem v25_K6_4_valid : validProfile v25_K6_4 := by unfold validProfile; decide +kernel
theorem v25_K6_4_value : totalBound v25_K6_4 = (8405 / 8398 : Rat) := by
  decide +kernel
#print axioms v25_K6_4_value
theorem v25_K6_4_gt_one : totalBound v25_K6_4 > 1 := by
  rw [v25_K6_4_value]
  norm_num

-- v25_K6-5: masks/counts {'0': 8, '1': 2, '2': 3, '4': 2, '8': 3, '16': 3, '32': 2, '3': 1, '5': 1, '25': 1, '33': 1, '14': 1, '50': 1, '20': 1, '36': 1, '40': 1}
def v25_K6_5 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 8⟩, ⟨[10], 2⟩, ⟨[11], 3⟩, ⟨[12], 2⟩, ⟨[13], 3⟩, ⟨[14], 3⟩, ⟨[15], 2⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14, 15], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 15], 1⟩], none, []⟩
theorem v25_K6_5_valid : validProfile v25_K6_5 := by unfold validProfile; decide +kernel
theorem v25_K6_5_value : totalBound v25_K6_5 = (8249 / 8398 : Rat) := by
  decide +kernel
#print axioms v25_K6_5_value
theorem v25_K6_5_lt_one : totalBound v25_K6_5 < 1 := by
  rw [v25_K6_5_value]
  norm_num

-- v25_K6-6: masks/counts {'0': 7, '1': 3, '2': 3, '4': 3, '8': 3, '16': 3, '32': 3, '11': 1, '5': 1, '49': 1, '22': 1, '34': 1, '44': 1, '24': 1}
def v25_K6_6 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 7⟩, ⟨[10], 3⟩, ⟨[11], 3⟩, ⟨[12], 3⟩, ⟨[13], 3⟩, ⟨[14], 3⟩, ⟨[15], 3⟩, ⟨[10, 11, 13], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[11, 12, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 13, 15], 1⟩, ⟨[13, 14], 1⟩], none, []⟩
theorem v25_K6_6_valid : validProfile v25_K6_6 := by unfold validProfile; decide +kernel
theorem v25_K6_6_value : totalBound v25_K6_6 = (243 / 247 : Rat) := by
  decide +kernel
#print axioms v25_K6_6_value
theorem v25_K6_6_lt_one : totalBound v25_K6_6 < 1 := by
  rw [v25_K6_6_value]
  norm_num

-- v25_K6-7: masks/counts {'0': 8, '1': 3, '2': 3, '4': 3, '8': 1, '16': 1, '32': 3, '39': 1, '9': 1, '17': 1, '10': 1, '18': 1, '12': 1, '20': 1, '24': 1, '40': 1, '48': 1}
def v25_K6_7 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 8⟩, ⟨[10], 3⟩, ⟨[11], 3⟩, ⟨[12], 3⟩, ⟨[13], 1⟩, ⟨[14], 1⟩, ⟨[15], 3⟩, ⟨[10, 11, 12, 15], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 14], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 13], 1⟩, ⟨[12, 14], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
theorem v25_K6_7_valid : validProfile v25_K6_7 := by unfold validProfile; decide +kernel
theorem v25_K6_7_value : totalBound v25_K6_7 = (4050 / 4199 : Rat) := by
  decide +kernel
#print axioms v25_K6_7_value
theorem v25_K6_7_lt_one : totalBound v25_K6_7 < 1 := by
  rw [v25_K6_7_value]
  norm_num

-- v25_K6-8: masks/counts {'0': 7, '1': 3, '2': 2, '4': 2, '8': 4, '16': 3, '32': 3, '3': 1, '5': 1, '57': 1, '14': 1, '18': 1, '34': 1, '20': 1, '36': 1}
def v25_K6_8 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 7⟩, ⟨[10], 3⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 4⟩, ⟨[14], 3⟩, ⟨[15], 3⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13, 14, 15], 1⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 15], 1⟩], none, []⟩
theorem v25_K6_8_valid : validProfile v25_K6_8 := by unfold validProfile; decide +kernel
theorem v25_K6_8_value : totalBound v25_K6_8 = (8105 / 8398 : Rat) := by
  decide +kernel
#print axioms v25_K6_8_value
theorem v25_K6_8_lt_one : totalBound v25_K6_8 < 1 := by
  rw [v25_K6_8_value]
  norm_num

-- v25_K6-9: masks/counts {'0': 5, '1': 4, '2': 4, '4': 4, '8': 4, '16': 1, '32': 4, '47': 1, '17': 1, '18': 1, '20': 1, '24': 1, '48': 1}
def v25_K6_9 : Profile :=
  ⟨25, [10, 11, 12, 13, 14, 15], [⟨[], 5⟩, ⟨[10], 4⟩, ⟨[11], 4⟩, ⟨[12], 4⟩, ⟨[13], 4⟩, ⟨[14], 1⟩, ⟨[15], 4⟩, ⟨[10, 11, 12, 13, 15], 1⟩, ⟨[10, 14], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 14], 1⟩, ⟨[13, 14], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
theorem v25_K6_9_valid : validProfile v25_K6_9 := by unfold validProfile; decide +kernel
theorem v25_K6_9_value : totalBound v25_K6_9 = (7685 / 8398 : Rat) := by
  decide +kernel
#print axioms v25_K6_9_value
theorem v25_K6_9_lt_one : totalBound v25_K6_9 < 1 := by
  rw [v25_K6_9_value]
  norm_num

/-- The twenty-one profiles actually used by the proof. -/
def successfulProfiles : List Profile := [v19, v20, v21_d5, v21_d6, v21_d7, v22_66, v22_67, v22_77, v23_66, v23_677, v24_K4_1, v24_K4_2, v24_K4_3, v25_K6_1, v25_K6_2, v25_K6_3, v25_K6_5, v25_K6_6, v25_K6_7, v25_K6_8, v25_K6_9]
theorem all_successful_values : ∀ p ∈ successfulProfiles, totalBound p < 1 := by
  intro p hp
  simp only [successfulProfiles, List.mem_cons, List.not_mem_nil, or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact v19_lt_one
  · exact v20_lt_one
  · exact v21_d5_lt_one
  · exact v21_d6_lt_one
  · exact v21_d7_lt_one
  · exact v22_66_lt_one
  · exact v22_67_lt_one
  · exact v22_77_lt_one
  · exact v23_66_lt_one
  · exact v23_677_lt_one
  · exact v24_K4_1_lt_one
  · exact v24_K4_2_lt_one
  · exact v24_K4_3_lt_one
  · exact v25_K6_1_lt_one
  · exact v25_K6_2_lt_one
  · exact v25_K6_3_lt_one
  · exact v25_K6_5_lt_one
  · exact v25_K6_6_lt_one
  · exact v25_K6_7_lt_one
  · exact v25_K6_8_lt_one
  · exact v25_K6_9_lt_one
#print axioms all_successful_values
#print axioms binom_eq_choose
-- END GENERATED CLOSED CERTIFICATES
end Aris4Math.Numeric
