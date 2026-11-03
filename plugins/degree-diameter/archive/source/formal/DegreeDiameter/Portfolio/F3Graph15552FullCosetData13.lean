import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset61
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 0]
def word : K → List (Fin 5) := ![
  [2, 0],
  [0, 0, 2, 0],
  [2, 0, 1, 3],
  [2, 0, 3, 1],
  [2, 3, 1, 0]]
def globalWordIndex : K → Nat := ![16, 166, 414, 422, 486]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![9, 18, 18, 9]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 3, 2, 4, 4, 2, 3, 1, 0, 1, 3, 4, 2, 1, 1, 0, 4, 3, 2, 2, 3, 4, 0, 1, 1, 2, 4, 3, 1, 0, 1, 3, 2, 4, 4, 2, 3, 4, 3, 2, 3, 4, 2, 1, 1, 0, 2, 4, 3, 2, 3, 4, 0, 1, 1, 4, 2, 3, 1, 0, 1, 3, 2, 4, 1, 1, 0, 4, 3, 2, 3, 4, 2]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 8, 46, 57, 4, 33, 65, 6, 29, 73, 11, 34, 54, 15, 3, 75, 3, 38, 55, 21, 42, 6, 19, 27, 59, 5, 34, 63, 1, 30, 78, 6, 47, 58, 24, 4, 57, 7, 27, 74, 9, 35, 55, 20, 28, 57, 4, 36, 56, 3, 51, 7, 7, 45, 59, 3, 35, 64, 2, 39, 60, 10, 33, 56, 6, 5, 66, 8, 28, 72, 12, 33, 8, 18, 29, 58, 5, 37, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset61

namespace FullCoset62
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
end FullCoset62

namespace FullCoset63
abbrev K := Fin 6
def reference : List (Fin 5) := [3, 4]
def word : K → List (Fin 5) := ![
  [3, 4],
  [3, 4, 0],
  [0, 0, 3, 4],
  [1, 3, 3, 4],
  [3, 3, 1, 4],
  [3, 4, 0, 0]]
def globalWordIndex : K → Nat := ![25, 126, 175, 375, 615, 631]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 2, 2, 1, 5, 4, 1, 4, 5, 3, 1, 5, 0, 1, 2, 3, 1, 4, 3, 5, 1, 3, 4, 1, 0, 2, 1, 5, 1, 3, 4, 1, 3, 2, 1, 0, 2, 2, 0, 5, 4, 1, 4, 5, 1, 1, 5, 3, 1, 2, 0, 1, 4, 3, 5, 3, 1, 2, 0, 1, 4, 3, 1, 1, 3, 5, 1, 3, 4, 1, 0, 2, 2, 0, 2, 4, 1, 5, 5, 1, 4]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 6, 28, 73, 3, 38, 56, 12, 15, 55, 2, 12, 60, 6, 9, 63, 24, 29, 21, 3, 45, 18, 1, 30, 24, 6, 10, 60, 1, 16, 66, 12, 13, 8, 3, 51, 7, 8, 29, 22, 18, 33, 19, 4, 35, 75, 1, 42, 6, 7, 46, 69, 3, 30, 20, 24, 4, 26, 2, 51, 23, 8, 42, 58, 5, 48, 65, 2, 3, 75, 6, 5, 66, 9, 11, 57, 4, 17, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset63

namespace FullCoset64
abbrev K := Fin 5
def reference : List (Fin 5) := [0, 2]
def word : K → List (Fin 5) := ![
  [0, 2],
  [0, 1, 3, 2],
  [0, 2, 1, 3],
  [0, 2, 3, 1],
  [0, 3, 1, 2]]
def globalWordIndex : K → Nat := ![8, 198, 214, 222, 238]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 27, 27, 54],
  ![0, 27, 27, 54],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 3, 4, 2, 3, 2, 4, 4, 2, 3, 2, 4, 3, 1, 1, 0, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 4, 0, 1, 1, 3, 4, 2, 1, 1, 0, 4, 2, 3, 2, 4, 3, 2, 3, 4, 4, 3, 2, 1, 0, 1, 3, 4, 2, 3, 2, 4, 0, 1, 1, 2, 4, 3, 1, 1, 0, 4, 2, 3, 1, 0, 1, 2, 3, 4, 4, 3, 2]
def alphaCode : Fin 81 → Nat := ![0, 2, 1, 7, 38, 56, 5, 28, 73, 18, 33, 59, 8, 29, 54, 63, 65, 7, 9, 34, 57, 45, 5, 46, 4, 27, 55, 8, 31, 19, 3, 29, 28, 1, 65, 59, 9, 11, 1, 45, 27, 62, 2, 56, 57, 7, 30, 1, 36, 28, 60, 72, 8, 73, 4, 11, 62, 2, 34, 46, 6, 56, 55, 5, 2, 60, 36, 38, 4, 72, 30, 56, 18, 2, 19, 1, 33, 28, 63, 31, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset64

end DegreeDiameter.Portfolio.F3Graph15552
