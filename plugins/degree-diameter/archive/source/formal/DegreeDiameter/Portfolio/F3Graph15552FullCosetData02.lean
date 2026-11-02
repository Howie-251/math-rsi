import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset15
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 0]
def word : K → List (Fin 5) := ![
  [4, 0],
  [0, 0, 4, 0],
  [1, 3, 4, 0],
  [3, 1, 4, 0],
  [4, 3, 1, 0]]
def globalWordIndex : K → Nat := ![26, 176, 376, 576, 736]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3, 3, 0, 1, 2, 4, 1, 2, 4, 1, 2, 4, 4, 1, 2, 4, 1, 2, 4, 1, 2, 2, 4, 1, 2, 4, 1, 2, 4, 1, 1, 4, 2, 1, 4, 2, 1, 4, 2, 2, 1, 4, 2, 1, 4, 2, 1, 4, 4, 2, 1, 4, 2, 1, 4, 2, 1]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 2, 39, 60, 1, 30, 78, 6, 5, 66, 24, 4, 57, 15, 3, 75, 3, 51, 7, 21, 42, 6, 12, 33, 8, 3, 30, 63, 21, 48, 56, 12, 39, 73, 2, 48, 75, 19, 39, 66, 9, 30, 57, 12, 46, 66, 3, 36, 57, 21, 29, 75, 6, 45, 60, 24, 38, 78, 15, 28, 69, 24, 51, 65, 15, 42, 55, 6, 33, 72, 1, 42, 69, 18, 33, 60, 11, 51, 78]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset15

namespace FullCoset16
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 3]
def word : K → List (Fin 5) := ![
  [4, 3],
  [0, 0, 4, 3],
  [1, 3, 4, 3],
  [4, 0, 0, 3],
  [4, 1, 3, 3]]
def globalWordIndex : K → Nat := ![29, 179, 379, 659, 699]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 2, 4, 1, 2, 1, 4, 0, 3, 3, 2, 4, 1, 2, 1, 4, 0, 3, 3, 2, 4, 1, 2, 1, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 1, 2, 1, 4, 2, 3, 3, 0, 4, 1, 2, 1, 4, 2, 3, 3, 0, 4, 1, 2, 1, 4, 2, 3, 3, 0]
def alphaCode : Fin 81 → Nat := ![0, 36, 72, 12, 29, 69, 24, 48, 55, 1, 46, 55, 21, 36, 78, 6, 30, 65, 2, 29, 65, 3, 46, 60, 15, 39, 72, 18, 42, 66, 11, 5, 56, 6, 30, 73, 1, 51, 75, 18, 3, 63, 15, 39, 56, 11, 33, 57, 1, 4, 73, 24, 48, 63, 9, 51, 75, 3, 38, 60, 19, 28, 7, 19, 33, 57, 12, 45, 69, 2, 38, 8, 2, 42, 66, 21, 28, 78, 9, 45, 6]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset16

namespace FullCoset17
abbrev K := Fin 5
def reference : List (Fin 5) := [3, 4]
def word : K → List (Fin 5) := ![
  [3, 4],
  [0, 0, 3, 4],
  [1, 3, 3, 4],
  [3, 3, 1, 4],
  [3, 4, 0, 0]]
def globalWordIndex : K → Nat := ![25, 175, 375, 615, 631]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 2, 3, 4, 0, 1, 1, 2, 4, 3, 2, 4, 3, 2, 3, 4, 0, 1, 1, 4, 3, 2, 3, 4, 2, 1, 1, 0, 1, 1, 0, 4, 3, 2, 3, 4, 2, 3, 4, 2, 1, 1, 0, 4, 3, 2, 4, 2, 3, 1, 0, 1, 3, 2, 4, 3, 2, 4, 4, 2, 3, 1, 0, 1, 1, 0, 1, 3, 2, 4, 4, 2, 3]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 15, 28, 73, 21, 38, 56, 12, 28, 55, 2, 39, 60, 6, 27, 63, 24, 29, 56, 3, 45, 54, 1, 30, 78, 6, 36, 60, 1, 34, 66, 12, 33, 8, 3, 51, 7, 8, 29, 78, 18, 33, 57, 11, 35, 75, 21, 42, 6, 7, 46, 69, 3, 30, 72, 24, 4, 57, 2, 51, 59, 19, 42, 58, 5, 48, 65, 15, 3, 75, 6, 5, 66, 9, 33, 57, 4, 39, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset17

namespace FullCoset18
abbrev K := Fin 5
def reference : List (Fin 5) := [1, 4]
def word : K → List (Fin 5) := ![
  [1, 4],
  [0, 1, 4],
  [1, 0, 0, 4],
  [1, 1, 3, 4],
  [2, 4, 1, 4]]
def globalWordIndex : K → Nat := ![15, 40, 285, 325, 515]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![2, 2, 2, 1],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 3, 2, 3, 4, 2, 1, 1, 0, 4, 2, 3, 1, 0, 1, 3, 2, 4, 1, 0, 1, 3, 2, 4, 4, 2, 3, 2, 4, 3, 2, 3, 4, 0, 1, 1, 3, 4, 2, 1, 1, 0, 4, 3, 2, 1, 1, 0, 4, 3, 2, 3, 4, 2, 3, 2, 4, 4, 2, 3, 1, 0, 1, 2, 3, 4, 0, 1, 1, 2, 4, 3]
def alphaCode : Fin 81 → Nat := ![0, 17, 22, 9, 30, 73, 18, 38, 60, 12, 29, 73, 18, 42, 55, 2, 16, 7, 24, 38, 55, 1, 5, 23, 9, 29, 75, 7, 4, 20, 2, 46, 66, 15, 28, 72, 2, 48, 63, 11, 28, 78, 2, 14, 19, 11, 33, 72, 8, 13, 6, 3, 46, 63, 5, 10, 8, 21, 36, 56, 1, 51, 65, 19, 36, 57, 6, 45, 65, 4, 3, 26, 1, 45, 69, 1, 11, 25, 19, 39, 56]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset18

end DegreeDiameter.Portfolio.F3Graph15552
