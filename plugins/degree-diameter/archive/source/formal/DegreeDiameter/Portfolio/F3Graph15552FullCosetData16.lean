import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset74
abbrev K := Fin 12
def reference : List (Fin 5) := [3]
def word : K → List (Fin 5) := ![
  [3],
  [3, 0],
  [0, 0, 3],
  [1, 3, 3],
  [2, 4, 3],
  [3, 2, 4],
  [3, 3, 1],
  [4, 2, 3],
  [0, 0, 3, 0],
  [1, 0, 3, 3],
  [1, 3, 3, 0],
  [4, 2, 3, 0]]
def globalWordIndex : K → Nat := ![4, 21, 34, 74, 104, 120, 122, 144, 171, 299, 371, 721]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 1, 2, 2],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 6, 0, 0],
  ![6, 9, 18, 18],
  ![15, 12, 0, 0],
  ![6, 9, 18, 18],
  ![0, 15, 18, 18]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 2, 2, 10, 7, 9, 10, 9, 7, 4, 5, 9, 11, 3, 6, 8, 1, 8, 4, 9, 5, 8, 8, 1, 11, 6, 3, 3, 11, 6, 5, 4, 9, 1, 8, 8, 7, 10, 9, 2, 0, 2, 9, 10, 7, 8, 8, 1, 9, 4, 5, 6, 11, 3, 3, 6, 11, 1, 8, 8, 5, 9, 4, 8, 1, 8, 6, 3, 11, 9, 5, 4, 7, 9, 10, 9, 7, 10, 2, 2, 0]
def alphaCode : Fin 81 → Nat := ![0, 12, 24, 6, 15, 57, 3, 33, 21, 3, 11, 69, 12, 12, 18, 24, 3, 66, 6, 48, 19, 12, 51, 6, 24, 9, 24, 6, 42, 19, 2, 15, 75, 2, 30, 69, 3, 48, 60, 6, 1, 21, 3, 51, 24, 3, 42, 8, 15, 12, 18, 1, 30, 21, 3, 11, 75, 1, 48, 60, 1, 42, 21, 6, 4, 75, 2, 15, 60, 21, 9, 24, 6, 30, 69, 6, 12, 66, 3, 15, 2]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset74

namespace FullCoset75
abbrev K := Fin 5
def reference : List (Fin 5) := [1, 2]
def word : K → List (Fin 5) := ![
  [1, 2],
  [0, 0, 1, 2],
  [1, 0, 0, 2],
  [1, 1, 3, 2],
  [1, 2, 1, 3]]
def globalWordIndex : K → Nat := ![13, 163, 283, 323, 339]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![27, 54, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4, 3, 2, 1, 3, 1, 2, 0, 4, 4]
def alphaCode : Fin 81 → Nat := ![0, 34, 59, 38, 38, 51, 73, 66, 73, 2, 33, 58, 28, 28, 42, 63, 57, 63, 1, 35, 57, 45, 45, 33, 56, 75, 56, 19, 12, 19, 3, 28, 62, 65, 65, 78, 9, 3, 9, 5, 27, 61, 55, 55, 69, 2, 21, 2, 4, 29, 60, 72, 72, 60, 11, 11, 24, 46, 39, 46, 6, 31, 56, 1, 1, 15, 36, 30, 36, 8, 30, 55, 18, 18, 6, 29, 48, 29, 7, 32, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset75

namespace FullCoset76
abbrev K := Fin 5
def reference : List (Fin 5) := [3, 2]
def word : K → List (Fin 5) := ![
  [3, 2],
  [3, 0, 2],
  [0, 0, 3, 2],
  [3, 2, 1, 3],
  [3, 3, 1, 2]]
def globalWordIndex : K → Nat := ![23, 108, 173, 589, 613]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 1, 2, 2],
  ![6, 0, 0, 0],
  ![0, 27, 54, 54],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 4, 3, 2, 4, 2, 3, 4, 3, 2, 4, 2, 3, 0, 1, 1, 4, 2, 3, 0, 1, 1, 4, 3, 2, 4, 2, 3, 0, 1, 1, 4, 3, 2, 0, 1, 1, 4, 3, 2, 4, 2, 3, 4, 3, 2, 4, 2, 3, 0, 1, 1, 4, 3, 2, 4, 2, 3, 0, 1, 1, 4, 2, 3, 0, 1, 1, 4, 3, 2, 0, 1, 1, 4, 3, 2, 4, 2, 3]
def alphaCode : Fin 81 → Nat := ![0, 2, 1, 38, 29, 30, 73, 60, 55, 18, 33, 12, 29, 42, 62, 7, 22, 21, 9, 24, 57, 5, 15, 17, 55, 31, 75, 19, 6, 58, 3, 11, 10, 65, 32, 57, 1, 4, 3, 45, 27, 39, 56, 69, 56, 1, 34, 21, 36, 51, 60, 8, 24, 26, 11, 35, 3, 46, 33, 61, 6, 20, 19, 2, 15, 59, 4, 13, 12, 72, 30, 66, 2, 6, 8, 28, 28, 48, 63, 78, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset76

namespace FullCoset77
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
end FullCoset77

end DegreeDiameter.Portfolio.F3Graph15552
