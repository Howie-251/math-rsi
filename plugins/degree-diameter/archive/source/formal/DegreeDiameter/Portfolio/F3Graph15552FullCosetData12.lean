import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset57
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
end FullCoset57

namespace FullCoset58
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
end FullCoset58

namespace FullCoset59
abbrev K := Fin 5
def reference : List (Fin 5) := [0, 3]
def word : K → List (Fin 5) := ![
  [0, 3],
  [0, 1, 3, 3],
  [0, 2, 4, 3],
  [0, 3, 0, 0],
  [0, 4, 2, 3]]
def globalWordIndex : K → Nat := ![9, 199, 229, 231, 269]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![18, 0, 9, 18]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 0, 0, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 0, 0, 0, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 4, 4, 4, 4, 4, 4, 0, 0, 0]
def alphaCode : Fin 81 → Nat := ![0, 4, 8, 2, 45, 64, 1, 47, 63, 9, 46, 56, 2, 36, 73, 8, 27, 58, 18, 28, 65, 4, 35, 54, 1, 38, 72, 18, 28, 65, 11, 45, 55, 3, 34, 56, 9, 28, 74, 2, 3, 7, 10, 29, 72, 7, 29, 57, 2, 36, 73, 19, 29, 63, 9, 46, 56, 6, 28, 59, 19, 29, 63, 5, 33, 55, 11, 45, 55, 1, 38, 72, 18, 37, 56, 20, 36, 55, 1, 5, 6]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset59

namespace FullCoset60
abbrev K := Fin 5
def reference : List (Fin 5) := [0, 1]
def word : K → List (Fin 5) := ![
  [0, 1],
  [0, 1, 0, 0],
  [0, 1, 1, 3],
  [0, 1, 2, 4],
  [0, 1, 4, 2]]
def globalWordIndex : K → Nat := ![7, 181, 189, 195, 203]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![27, 54, 27, 27]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 4, 3, 2, 4, 3, 2, 4, 3, 2, 3, 2, 4, 3, 2, 4, 3, 2, 4, 2, 4, 3, 2, 4, 3, 2, 4, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 2, 3, 4, 2, 3, 4, 2, 3, 4, 3, 4, 2, 3, 4, 2, 3, 4, 2]
def alphaCode : Fin 81 → Nat := ![0, 34, 59, 1, 35, 57, 2, 33, 58, 3, 28, 8, 4, 29, 6, 5, 27, 7, 6, 4, 56, 7, 5, 54, 8, 3, 55, 2, 34, 57, 27, 35, 58, 55, 33, 59, 3, 29, 7, 4, 27, 35, 5, 28, 60, 7, 3, 56, 8, 31, 54, 6, 59, 55, 1, 33, 59, 29, 34, 57, 54, 35, 58, 5, 28, 6, 3, 29, 34, 4, 27, 62, 6, 5, 55, 7, 30, 56, 8, 58, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset60

end DegreeDiameter.Portfolio.F3Graph15552
