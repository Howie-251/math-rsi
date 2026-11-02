import DegreeDiameter.Portfolio.F5Graph3750
import Mathlib.Tactic.FinCases

namespace DegreeDiameter.Portfolio.F5Graph3750
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000

def ofCoordinates (c : Fin 3 → Nat) : Fin 125 :=
  ⟨c 0 % 5 + 5 * (c 1 % 5) + 25 * (c 2 % 5), by
    have h0 := Nat.mod_lt (c 0) (by decide : 0 < 5)
    have h1 := Nat.mod_lt (c 1) (by decide : 0 < 5)
    have h2 := Nat.mod_lt (c 2) (by decide : 0 < 5)
    omega⟩

theorem coordinate_ofCoordinates (c : Fin 3 → Nat) (i : Fin 3) :
    coordinate (ofCoordinates c) i = c i % 5 := by
  have h0 := Nat.mod_lt (c 0) (by decide : 0 < 5)
  have h1 := Nat.mod_lt (c 1) (by decide : 0 < 5)
  have h2 := Nat.mod_lt (c 2) (by decide : 0 < 5)
  fin_cases i
  · change ((c 0 % 5 + 5 * (c 1 % 5) + 25 * (c 2 % 5)) / 1) % 5 = c 0 % 5
    omega
  · change ((c 0 % 5 + 5 * (c 1 % 5) + 25 * (c 2 % 5)) / 5) % 5 = c 1 % 5
    omega
  · change ((c 0 % 5 + 5 * (c 1 % 5) + 25 * (c 2 % 5)) / 25) % 5 = c 2 % 5
    omega

theorem code_decompose (x : Fin 125) :
    coordinate x 0 + 5 * coordinate x 1 + 25 * coordinate x 2 = x.val := by
  have hx := x.isLt
  simp only [coordinate, Fin.val_zero, Fin.val_one, Fin.val_two,
    pow_zero, pow_one, show 5 ^ 2 = 25 from rfl, Nat.div_one]
  omega

theorem fiber_ext {x y : Fin 125} (h : ∀ i, coordinate x i = coordinate y i) : x = y := by
  apply Fin.ext
  have hx := code_decompose x
  have hy := code_decompose y
  rw [h 0, h 1, h 2] at hx
  omega

def addFiber (x y : Fin 125) : Fin 125 := ofCoordinates fun i => coordinate x i + coordinate y i

def subFiber (y x : Fin 125) : Fin 125 := ofCoordinates fun i => coordinate y i + 5 - coordinate x i

theorem coordinate_add (x y : Fin 125) (i : Fin 3) :
    coordinate (addFiber x y) i = (coordinate x i + coordinate y i) % 5 :=
  coordinate_ofCoordinates _ _

theorem coordinate_sub (y x : Fin 125) (i : Fin 3) :
    coordinate (subFiber y x) i = (coordinate y i + 5 - coordinate x i) % 5 :=
  coordinate_ofCoordinates _ _

theorem add_sub_cancel (x y : Fin 125) : addFiber x (subFiber y x) = y := by
  apply fiber_ext
  intro i
  rw [coordinate_add, coordinate_sub]
  have hx : coordinate x i < 5 := Nat.mod_lt _ (by decide)
  have hy : coordinate y i < 5 := Nat.mod_lt _ (by decide)
  omega

theorem coordinate_fiberStep (p : Fin 4) (t : Fin 5) (x : Fin 125) (i : Fin 3) :
    coordinate (fiberStep p t x) i = stepCoordinate p t x i := by
  have h0 : stepCoordinate p t x 0 < 5 := Nat.mod_lt _ (by decide)
  have h1 : stepCoordinate p t x 1 < 5 := Nat.mod_lt _ (by decide)
  have h2 : stepCoordinate p t x 2 < 5 := Nat.mod_lt _ (by decide)
  fin_cases i
  · change ((stepCoordinate p t x 0 + 5 * stepCoordinate p t x 1 +
       25 * stepCoordinate p t x 2) / 1) % 5 = stepCoordinate p t x 0
    omega
  · change ((stepCoordinate p t x 0 + 5 * stepCoordinate p t x 1 +
       25 * stepCoordinate p t x 2) / 5) % 5 = stepCoordinate p t x 1
    omega
  · change ((stepCoordinate p t x 0 + 5 * stepCoordinate p t x 1 +
       25 * stepCoordinate p t x 2) / 25) % 5 = stepCoordinate p t x 2
    omega

theorem fiberStep_add (p : Fin 4) (t : Fin 5) (x y : Fin 125) :
    fiberStep p t (addFiber x y) =
      addFiber (fiberStep p 0 x) (fiberStep p t y) := by
  apply fiber_ext
  intro i
  rw [coordinate_fiberStep, coordinate_add, coordinate_fiberStep, coordinate_fiberStep]
  simp only [stepCoordinate, coordinate_add]
  fin_cases p <;> fin_cases i
  · change (0 * ((coordinate x 0 + coordinate y 0) % 5) + 2 * ((coordinate x 1 + coordinate y 1) % 5) + 4 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((0 * coordinate x 0 + 2 * coordinate x 1 + 4 * coordinate x 2) % 5 + (0 * coordinate y 0 + 2 * coordinate y 1 + 4 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (1 * ((coordinate x 0 + coordinate y 0) % 5) + 0 * ((coordinate x 1 + coordinate y 1) % 5) + 0 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((1 * coordinate x 0 + 0 * coordinate x 1 + 0 * coordinate x 2) % 5 + (1 * coordinate y 0 + 0 * coordinate y 1 + 0 * coordinate y 2 + t.val * 1) % 5) % 5
    omega
  · change (0 * ((coordinate x 0 + coordinate y 0) % 5) + 1 * ((coordinate x 1 + coordinate y 1) % 5) + 3 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((0 * coordinate x 0 + 1 * coordinate x 1 + 3 * coordinate x 2) % 5 + (0 * coordinate y 0 + 1 * coordinate y 1 + 3 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (0 * ((coordinate x 0 + coordinate y 0) % 5) + 1 * ((coordinate x 1 + coordinate y 1) % 5) + 0 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((0 * coordinate x 0 + 1 * coordinate x 1 + 0 * coordinate x 2) % 5 + (0 * coordinate y 0 + 1 * coordinate y 1 + 0 * coordinate y 2 + t.val * 1) % 5) % 5
    omega
  · change (4 * ((coordinate x 0 + coordinate y 0) % 5) + 0 * ((coordinate x 1 + coordinate y 1) % 5) + 3 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((4 * coordinate x 0 + 0 * coordinate x 1 + 3 * coordinate x 2) % 5 + (4 * coordinate y 0 + 0 * coordinate y 1 + 3 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (2 * ((coordinate x 0 + coordinate y 0) % 5) + 0 * ((coordinate x 1 + coordinate y 1) % 5) + 1 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((2 * coordinate x 0 + 0 * coordinate x 1 + 1 * coordinate x 2) % 5 + (2 * coordinate y 0 + 0 * coordinate y 1 + 1 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (2 * ((coordinate x 0 + coordinate y 0) % 5) + 3 * ((coordinate x 1 + coordinate y 1) % 5) + 1 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((2 * coordinate x 0 + 3 * coordinate x 1 + 1 * coordinate x 2) % 5 + (2 * coordinate y 0 + 3 * coordinate y 1 + 1 * coordinate y 2 + t.val * 1) % 5) % 5
    omega
  · change (0 * ((coordinate x 0 + coordinate y 0) % 5) + 4 * ((coordinate x 1 + coordinate y 1) % 5) + 1 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((0 * coordinate x 0 + 4 * coordinate x 1 + 1 * coordinate x 2) % 5 + (0 * coordinate y 0 + 4 * coordinate y 1 + 1 * coordinate y 2 + t.val * 1) % 5) % 5
    omega
  · change (1 * ((coordinate x 0 + coordinate y 0) % 5) + 0 * ((coordinate x 1 + coordinate y 1) % 5) + 1 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((1 * coordinate x 0 + 0 * coordinate x 1 + 1 * coordinate x 2) % 5 + (1 * coordinate y 0 + 0 * coordinate y 1 + 1 * coordinate y 2 + t.val * 1) % 5) % 5
    omega
  · change (2 * ((coordinate x 0 + coordinate y 0) % 5) + 1 * ((coordinate x 1 + coordinate y 1) % 5) + 2 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((2 * coordinate x 0 + 1 * coordinate x 1 + 2 * coordinate x 2) % 5 + (2 * coordinate y 0 + 1 * coordinate y 1 + 2 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (3 * ((coordinate x 0 + coordinate y 0) % 5) + 3 * ((coordinate x 1 + coordinate y 1) % 5) + 4 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 0) % 5 =
      ((3 * coordinate x 0 + 3 * coordinate x 1 + 4 * coordinate x 2) % 5 + (3 * coordinate y 0 + 3 * coordinate y 1 + 4 * coordinate y 2 + t.val * 0) % 5) % 5
    omega
  · change (3 * ((coordinate x 0 + coordinate y 0) % 5) + 4 * ((coordinate x 1 + coordinate y 1) % 5) + 4 * ((coordinate x 2 + coordinate y 2) % 5) + t.val * 1) % 5 =
      ((3 * coordinate x 0 + 4 * coordinate x 1 + 4 * coordinate x 2) % 5 + (3 * coordinate y 0 + 4 * coordinate y 1 + 4 * coordinate y 2 + t.val * 1) % 5) % 5
    omega

#print axioms add_sub_cancel
#print axioms fiberStep_add
end DegreeDiameter.Portfolio.F5Graph3750
