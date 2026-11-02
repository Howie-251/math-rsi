import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset24
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
end FullCoset24

namespace FullCoset25
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
end FullCoset25

namespace FullCoset26
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
end FullCoset26

namespace FullCoset27
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
end FullCoset27

end DegreeDiameter.Portfolio.F3Graph15552
