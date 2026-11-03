import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset32
abbrev K := Fin 5
def reference : List (Fin 5) := [1, 4]
def word : K → List (Fin 5) := ![
  [1, 4],
  [0, 0, 1, 4],
  [1, 0, 0, 4],
  [1, 1, 3, 4],
  [2, 4, 1, 4]]
def globalWordIndex : K → Nat := ![15, 165, 285, 325, 515]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 3, 2, 3, 4, 2, 1, 1, 0, 4, 2, 3, 1, 0, 1, 3, 2, 4, 1, 0, 1, 3, 2, 4, 4, 2, 3, 2, 4, 3, 2, 3, 4, 0, 1, 1, 3, 4, 2, 1, 1, 0, 4, 3, 2, 1, 1, 0, 4, 3, 2, 3, 4, 2, 3, 2, 4, 4, 2, 3, 1, 0, 1, 2, 3, 4, 0, 1, 1, 2, 4, 3]
def alphaCode : Fin 81 → Nat := ![0, 51, 66, 9, 30, 73, 18, 38, 60, 12, 29, 73, 18, 42, 55, 6, 48, 7, 24, 38, 55, 3, 5, 69, 9, 29, 75, 21, 4, 60, 2, 46, 66, 15, 28, 72, 2, 48, 63, 11, 28, 78, 2, 42, 57, 11, 33, 72, 24, 39, 6, 3, 46, 63, 15, 30, 8, 21, 36, 56, 1, 51, 65, 19, 36, 57, 6, 45, 65, 12, 3, 78, 1, 45, 69, 1, 33, 75, 19, 39, 56]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset32

namespace FullCoset33
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 3]
def word : K → List (Fin 5) := ![
  [2, 3],
  [0, 0, 2, 3],
  [1, 3, 2, 3],
  [2, 0, 0, 3],
  [2, 3, 2, 4]]
def globalWordIndex : K → Nat := ![19, 169, 369, 409, 495]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![9, 18, 18, 9],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 3, 0, 3, 3, 3, 0, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 0, 3, 3, 3, 0, 3, 3, 3, 0, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 4, 1, 1, 2, 4, 4, 1, 2, 2, 1, 4, 4, 2, 1, 1, 4, 2, 0, 3, 3, 3, 0, 3, 3, 3, 0]
def alphaCode : Fin 81 → Nat := ![0, 36, 72, 20, 5, 65, 10, 46, 7, 6, 33, 66, 3, 51, 56, 4, 48, 69, 3, 51, 57, 8, 48, 69, 6, 28, 66, 12, 33, 58, 6, 30, 78, 15, 29, 75, 1, 37, 73, 18, 3, 63, 11, 47, 8, 15, 34, 75, 12, 33, 54, 5, 30, 78, 24, 35, 57, 21, 42, 55, 3, 39, 60, 21, 42, 59, 7, 39, 60, 24, 27, 57, 2, 38, 74, 19, 4, 64, 9, 45, 6]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset33

namespace FullCoset34
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 2]
def word : K → List (Fin 5) := ![
  [2, 2],
  [0, 0, 2, 2],
  [1, 3, 2, 2],
  [2, 0, 0, 2],
  [3, 1, 2, 2]]
def globalWordIndex : K → Nat := ![18, 168, 368, 408, 568]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![9, 18, 18, 9],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 2, 1, 4, 2, 4, 1, 2, 1, 4, 2, 4, 1, 0, 3, 3, 2, 4, 1, 0, 3, 3, 2, 1, 4, 2, 4, 1, 0, 3, 3, 2, 1, 4, 0, 3, 3, 2, 1, 4, 2, 4, 1, 2, 1, 4, 2, 4, 1, 0, 3, 3, 2, 1, 4, 2, 4, 1, 0, 3, 3, 2, 4, 1, 0, 3, 3, 2, 1, 4, 0, 3, 3, 2, 1, 4, 2, 4, 1]
def alphaCode : Fin 81 → Nat := ![0, 20, 10, 42, 39, 48, 75, 69, 78, 6, 3, 12, 39, 33, 42, 8, 73, 63, 3, 24, 6, 4, 45, 38, 78, 75, 57, 21, 15, 24, 3, 47, 37, 69, 66, 75, 2, 19, 9, 33, 30, 39, 66, 60, 69, 24, 21, 3, 30, 51, 33, 7, 72, 65, 15, 12, 21, 48, 42, 51, 6, 74, 64, 12, 6, 15, 5, 46, 36, 60, 57, 66, 1, 18, 11, 51, 48, 30, 57, 78, 60]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset34

namespace FullCoset35
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 1]
def word : K → List (Fin 5) := ![
  [2, 1],
  [0, 0, 2, 1],
  [1, 3, 2, 1],
  [2, 0, 0, 1],
  [2, 1, 0, 0]]
def globalWordIndex : K → Nat := ![17, 167, 367, 407, 431]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![9, 18, 18, 9],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 2, 2, 3, 1, 4, 3, 4, 1, 4, 1, 3, 2, 2, 0, 1, 4, 3, 4, 3, 1, 1, 3, 4, 2, 0, 2, 4, 1, 3, 2, 2, 0, 1, 4, 3, 4, 3, 1, 1, 3, 4, 2, 0, 2, 0, 2, 2, 3, 1, 4, 3, 4, 1, 4, 3, 1, 1, 3, 4, 2, 0, 2, 0, 2, 2, 3, 1, 4, 3, 4, 1, 4, 1, 3, 2, 2, 0, 1, 4, 3]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 9, 42, 57, 18, 33, 75, 3, 48, 72, 21, 42, 6, 15, 27, 63, 6, 36, 69, 21, 45, 54, 15, 3, 75, 4, 30, 73, 3, 51, 7, 24, 28, 64, 7, 37, 78, 3, 46, 55, 24, 4, 57, 1, 30, 78, 10, 51, 58, 19, 34, 57, 8, 38, 60, 12, 47, 56, 6, 5, 66, 2, 39, 60, 11, 33, 59, 20, 35, 66, 5, 39, 74, 12, 33, 8, 6, 29, 65]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset35

end DegreeDiameter.Portfolio.F3Graph15552
