import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset52
abbrev K := Fin 5
def reference : List (Fin 5) := [2, 1]
def word : K → List (Fin 5) := ![
  [2, 1],
  [2, 0, 1],
  [0, 0, 2, 1],
  [1, 3, 2, 1],
  [2, 1, 0, 0]]
def globalWordIndex : K → Nat := ![17, 82, 167, 367, 431]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 6, 0, 3],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 1, 2, 4, 1, 4, 2, 4, 2, 1, 3, 3, 0, 2, 4, 1, 4, 1, 2, 2, 1, 4, 3, 0, 3, 4, 2, 1, 3, 3, 0, 2, 4, 1, 4, 1, 2, 2, 1, 4, 3, 0, 3, 0, 3, 3, 1, 2, 4, 1, 4, 2, 4, 1, 2, 2, 1, 4, 3, 0, 3, 0, 3, 3, 1, 2, 4, 1, 4, 2, 4, 2, 1, 3, 3, 0, 2, 4, 1]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 3, 42, 57, 6, 33, 75, 3, 48, 24, 21, 42, 6, 15, 27, 21, 6, 12, 69, 21, 15, 54, 15, 3, 75, 4, 30, 25, 3, 51, 7, 24, 28, 22, 7, 13, 78, 3, 16, 55, 24, 4, 57, 1, 30, 78, 4, 51, 58, 7, 34, 57, 8, 14, 60, 12, 17, 56, 6, 5, 66, 2, 39, 60, 5, 33, 59, 8, 35, 66, 5, 39, 26, 12, 33, 8, 6, 29, 23]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset52

namespace FullCoset54
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
end FullCoset54

namespace FullCoset55
abbrev K := Fin 5
def reference : List (Fin 5) := [3, 2]
def word : K → List (Fin 5) := ![
  [3, 2],
  [0, 0, 3, 2],
  [1, 3, 3, 2],
  [3, 2, 1, 3],
  [3, 3, 1, 2]]
def globalWordIndex : K → Nat := ![23, 173, 373, 589, 613]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 27, 54, 54],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 2, 2, 4, 3, 1, 4, 1, 3, 4, 3, 1, 4, 1, 3, 0, 2, 2, 4, 1, 3, 0, 2, 2, 4, 3, 1, 4, 1, 3, 0, 2, 2, 4, 3, 1, 0, 2, 2, 4, 3, 1, 4, 1, 3, 4, 3, 1, 4, 1, 3, 0, 2, 2, 4, 3, 1, 4, 1, 3, 0, 2, 2, 4, 1, 3, 0, 2, 2, 4, 3, 1, 0, 2, 2, 4, 3, 1, 4, 1, 3]
def alphaCode : Fin 81 → Nat := ![0, 12, 24, 38, 29, 30, 73, 60, 55, 18, 33, 12, 29, 42, 62, 7, 75, 60, 9, 24, 57, 5, 30, 42, 55, 31, 75, 19, 6, 58, 3, 39, 51, 65, 32, 57, 1, 21, 6, 45, 27, 39, 56, 69, 56, 1, 34, 21, 36, 51, 60, 8, 57, 69, 11, 35, 3, 46, 33, 61, 6, 66, 78, 2, 15, 59, 4, 48, 33, 72, 30, 66, 2, 3, 15, 28, 28, 48, 63, 78, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset55

namespace FullCoset56
abbrev K := Fin 5
def reference : List (Fin 5) := [3, 0]
def word : K → List (Fin 5) := ![
  [3, 0],
  [0, 0, 3, 0],
  [1, 3, 3, 0],
  [2, 4, 3, 0],
  [4, 2, 3, 0]]
def globalWordIndex : K → Nat := ![21, 171, 371, 521, 721]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 6, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 3, 2, 4, 4, 2, 3, 1, 0, 1, 3, 4, 2, 1, 1, 0, 4, 3, 2, 2, 4, 3, 2, 3, 4, 0, 1, 1, 4, 2, 3, 1, 0, 1, 3, 2, 4, 1, 1, 0, 4, 3, 2, 3, 4, 2, 2, 3, 4, 0, 1, 1, 2, 4, 3, 1, 0, 1, 3, 2, 4, 4, 2, 3, 4, 3, 2, 3, 4, 2, 1, 1, 0]
def alphaCode : Fin 81 → Nat := ![0, 39, 78, 6, 51, 66, 3, 51, 66, 12, 33, 78, 12, 30, 78, 24, 3, 66, 24, 39, 57, 12, 51, 6, 24, 39, 60, 24, 42, 57, 21, 42, 57, 2, 30, 69, 3, 48, 69, 15, 5, 57, 3, 51, 69, 3, 42, 8, 15, 30, 78, 15, 30, 75, 12, 33, 75, 1, 48, 60, 15, 33, 75, 6, 4, 75, 21, 42, 60, 21, 39, 60, 6, 48, 69, 6, 48, 66, 21, 33, 7]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset56

end DegreeDiameter.Portfolio.F3Graph15552
