import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset11
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
end FullCoset11

namespace FullCoset12
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 1]
def word : K → List (Fin 5) := ![
  [4, 1],
  [0, 0, 4, 1],
  [1, 3, 4, 1],
  [4, 1, 0, 0],
  [4, 1, 4, 2]]
def globalWordIndex : K → Nat := ![27, 177, 377, 681, 703]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![27, 27, 27, 54]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 2, 1, 4, 4, 0, 2, 3, 1, 3, 1, 2, 2, 1, 3, 4, 0, 4, 3, 2, 1, 4, 4, 0, 2, 3, 1, 3, 1, 2, 2, 1, 3, 4, 0, 4, 0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 1, 2, 2, 1, 3, 4, 0, 4, 0, 4, 4, 1, 2, 3, 1, 3, 2, 3, 2, 1, 4, 4, 0, 2, 3, 1]
def alphaCode : Fin 81 → Nat := ![0, 5, 7, 24, 51, 57, 12, 33, 66, 3, 39, 66, 29, 31, 6, 24, 27, 78, 6, 51, 78, 12, 39, 54, 55, 3, 62, 4, 48, 75, 27, 32, 7, 6, 28, 60, 7, 33, 60, 21, 48, 55, 56, 4, 60, 1, 3, 8, 6, 33, 58, 21, 34, 75, 8, 42, 69, 3, 30, 56, 54, 5, 61, 2, 4, 6, 15, 42, 59, 3, 35, 57, 5, 30, 57, 28, 30, 8, 15, 29, 69]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset12

namespace FullCoset13
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
end FullCoset13

namespace FullCoset14
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
end FullCoset14

end DegreeDiameter.Portfolio.F3Graph15552
