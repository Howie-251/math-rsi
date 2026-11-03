import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset78
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
end FullCoset78

namespace FullCoset79
abbrev K := Fin 6
def reference : List (Fin 5) := [1, 4]
def word : K → List (Fin 5) := ![
  [1, 4],
  [1, 4, 0],
  [0, 0, 1, 4],
  [1, 0, 0, 4],
  [1, 1, 3, 4],
  [2, 4, 1, 4]]
def globalWordIndex : K → Nat := ![15, 76, 165, 285, 325, 515]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 0, 2, 4, 3, 5, 5, 3, 4, 3, 5, 4, 3, 4, 5, 0, 2, 2, 4, 5, 3, 2, 2, 0, 5, 4, 3, 2, 2, 0, 5, 4, 3, 4, 5, 3, 4, 3, 5, 5, 3, 4, 2, 0, 2, 3, 4, 5, 0, 2, 2, 3, 5, 4]
def alphaCode : Fin 81 → Nat := ![0, 16, 23, 6, 13, 20, 3, 10, 26, 2, 15, 22, 8, 12, 19, 5, 9, 7, 1, 17, 21, 7, 5, 18, 4, 11, 24, 21, 4, 60, 2, 46, 66, 15, 28, 72, 2, 48, 63, 11, 28, 78, 2, 42, 57, 11, 33, 72, 24, 39, 6, 3, 46, 63, 15, 30, 8, 21, 36, 56, 1, 51, 65, 19, 36, 57, 6, 45, 65, 12, 3, 78, 1, 45, 69, 1, 33, 75, 19, 39, 56]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset79

namespace FullCoset80
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
end FullCoset80

namespace FullCoset81
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
end FullCoset81

end DegreeDiameter.Portfolio.F3Graph15552
