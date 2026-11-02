import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset95
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 3]
def word : K → List (Fin 5) := ![
  [2, 3],
  [2, 3, 0],
  [1, 3, 2, 3],
  [2, 0, 0, 3],
  [2, 3, 2, 4]]
def globalWordIndex : K → Nat := ![19, 96, 369, 409, 495]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 3, 0, 3],
  ![6, 0, 0, 0],
  ![9, 18, 18, 9],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 3, 0, 3, 3, 3, 0, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 0, 3, 3, 3, 0, 3, 3, 3, 0, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 0, 3, 3, 3, 0, 3, 3, 3, 0]
def alphaCode : Fin 81 → Nat := ![0, 36, 72, 20, 5, 65, 10, 46, 7, 6, 33, 26, 4, 51, 56, 4, 9, 69, 3, 13, 57, 8, 48, 18, 8, 28, 66, 12, 14, 58, 6, 30, 19, 6, 29, 75, 1, 37, 73, 18, 3, 63, 11, 47, 8, 15, 34, 24, 5, 33, 54, 5, 10, 78, 24, 35, 25, 3, 42, 55, 3, 11, 60, 21, 12, 59, 7, 39, 20, 7, 27, 57, 2, 38, 74, 19, 4, 64, 9, 45, 6]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset95

namespace FullCoset96
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 4]
def word : K → List (Fin 5) := ![
  [4, 4],
  [0, 0, 4, 4],
  [1, 3, 4, 4],
  [4, 3, 1, 4],
  [4, 4, 3, 1]]
def globalWordIndex : K → Nat := ![30, 180, 380, 740, 772]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 1, 2, 3, 1, 3, 2, 1, 3, 2, 0, 4, 4, 1, 2, 3, 1, 2, 3, 1, 3, 2, 0, 4, 4, 2, 3, 1, 3, 2, 1, 4, 4, 0, 4, 4, 0, 2, 3, 1, 3, 2, 1, 3, 2, 1, 4, 4, 0, 2, 3, 1, 2, 1, 3, 4, 0, 4, 3, 1, 2, 3, 1, 2, 2, 1, 3, 4, 0, 4, 4, 0, 4, 3, 1, 2, 2, 1, 3]
def alphaCode : Fin 81 → Nat := ![0, 29, 55, 15, 30, 73, 21, 38, 60, 12, 28, 78, 2, 28, 54, 6, 48, 63, 24, 39, 56, 3, 45, 69, 1, 27, 56, 21, 36, 60, 1, 51, 66, 7, 33, 8, 6, 35, 7, 12, 29, 78, 18, 42, 57, 11, 33, 75, 8, 34, 6, 3, 46, 69, 15, 30, 72, 5, 4, 57, 2, 51, 66, 19, 42, 57, 6, 48, 65, 4, 3, 59, 3, 5, 58, 9, 33, 75, 24, 39, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset96

end DegreeDiameter.Portfolio.F3Graph15552
