import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset87
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 1]
def word : K → List (Fin 5) := ![
  [4, 1],
  [4, 0, 1],
  [1, 3, 4, 1],
  [4, 1, 0, 0],
  [4, 1, 4, 2]]
def globalWordIndex : K → Nat := ![27, 132, 377, 681, 703]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![27, 27, 27, 54]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 2, 1, 4, 4, 0, 2, 3, 1, 3, 1, 2, 2, 1, 3, 4, 0, 4, 3, 2, 1, 4, 4, 0, 2, 3, 1, 3, 1, 2, 2, 1, 3, 4, 0, 4, 0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 1, 2, 2, 1, 3, 4, 0, 4, 0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 2, 1, 4, 4, 0, 2, 3, 1]
def alphaCode : Fin 81 → Nat := ![0, 5, 7, 3, 51, 57, 6, 33, 66, 3, 39, 24, 29, 31, 6, 24, 27, 21, 6, 12, 78, 12, 15, 54, 55, 3, 62, 4, 48, 22, 27, 32, 7, 6, 28, 19, 7, 10, 60, 21, 13, 55, 56, 4, 60, 1, 3, 8, 1, 33, 58, 4, 34, 75, 8, 17, 69, 3, 11, 56, 54, 5, 61, 2, 4, 6, 8, 42, 59, 2, 35, 57, 5, 30, 20, 28, 30, 8, 15, 29, 26]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset87

namespace FullCoset88
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
end FullCoset88

namespace FullCoset89
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 4]
def word : K → List (Fin 5) := ![
  [4, 4],
  [4, 0, 4],
  [1, 3, 4, 4],
  [4, 3, 1, 4],
  [4, 4, 3, 1]]
def globalWordIndex : K → Nat := ![30, 135, 380, 740, 772]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![2, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 1, 2, 3, 1, 3, 2, 1, 3, 2, 0, 4, 4, 1, 2, 3, 1, 2, 3, 1, 3, 2, 0, 4, 4, 2, 3, 1, 3, 2, 1, 4, 4, 0, 4, 4, 0, 2, 3, 1, 3, 2, 1, 3, 2, 1, 4, 4, 0, 2, 3, 1, 2, 1, 3, 4, 0, 4, 3, 1, 2, 3, 1, 2, 2, 1, 3, 4, 0, 4, 4, 0, 4, 3, 1, 2, 2, 1, 3]
def alphaCode : Fin 81 → Nat := ![0, 29, 55, 3, 30, 73, 6, 38, 60, 4, 28, 78, 2, 28, 54, 1, 48, 63, 8, 39, 56, 2, 45, 69, 1, 27, 56, 21, 36, 19, 1, 51, 22, 7, 33, 8, 6, 35, 7, 12, 29, 26, 18, 42, 20, 11, 33, 24, 8, 34, 6, 3, 46, 21, 15, 11, 72, 5, 4, 57, 2, 17, 66, 19, 12, 57, 6, 15, 65, 4, 3, 59, 3, 5, 58, 9, 10, 75, 24, 13, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset89

namespace FullCoset90
abbrev K := Fin 5
def reference : List (Fin 5) := [0, 4]
def word : K → List (Fin 5) := ![
  [0, 4],
  [0, 4, 0],
  [0, 1, 3, 4],
  [0, 3, 1, 4],
  [3, 1, 0, 4]]
def globalWordIndex : K → Nat := ![10, 51, 200, 240, 560]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 0, 4, 4, 0, 4, 4, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 3, 2, 1, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 4, 0, 4, 4, 0, 4, 4, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 0, 4, 4, 0, 4, 4, 0, 4, 3, 2, 1, 3, 2, 1, 3, 2, 1]
def alphaCode : Fin 81 → Nat := ![0, 51, 66, 1, 33, 75, 2, 42, 57, 11, 15, 73, 18, 12, 56, 1, 9, 63, 19, 38, 21, 2, 45, 18, 9, 28, 24, 1, 36, 55, 7, 46, 65, 4, 29, 72, 1, 16, 63, 11, 13, 73, 18, 10, 56, 15, 30, 8, 24, 39, 6, 6, 48, 7, 2, 29, 72, 8, 36, 55, 5, 46, 65, 21, 4, 60, 3, 5, 69, 12, 3, 78, 2, 45, 23, 9, 28, 20, 19, 38, 26]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset90

end DegreeDiameter.Portfolio.F3Graph15552
