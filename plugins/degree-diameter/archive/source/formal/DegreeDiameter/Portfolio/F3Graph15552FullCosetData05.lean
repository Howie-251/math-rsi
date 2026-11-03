import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset28
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
end FullCoset28

namespace FullCoset29
abbrev K := Fin 5
def reference : List (Fin 5) := [1, 0]
def word : K → List (Fin 5) := ![
  [1, 0],
  [0, 0, 1, 0],
  [1, 0, 1, 3],
  [1, 0, 4, 2],
  [1, 2, 4, 0]]
def globalWordIndex : K → Nat := ![11, 161, 289, 303, 351]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![54, 54, 0, 54],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 4, 3, 2, 4, 2, 3, 2, 4, 3, 3, 4, 2, 1, 0, 1, 2, 3, 4, 1, 1, 0, 3, 2, 4, 1, 1, 0, 3, 2, 4, 2, 3, 4, 4, 3, 2, 4, 2, 3, 0, 1, 1, 3, 4, 2, 1, 0, 1, 2, 4, 3, 1, 0, 1, 2, 4, 3, 3, 4, 2, 3, 2, 4, 2, 3, 4, 1, 1, 0, 4, 2, 3, 0, 1, 1, 4, 3, 2]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 18, 32, 55, 9, 29, 61, 4, 45, 8, 28, 36, 59, 15, 3, 75, 8, 4, 63, 21, 42, 6, 56, 34, 72, 3, 51, 7, 27, 35, 55, 6, 59, 73, 1, 3, 56, 19, 27, 35, 1, 30, 78, 2, 46, 57, 24, 4, 57, 5, 28, 60, 6, 5, 66, 3, 38, 34, 54, 29, 58, 1, 33, 65, 7, 30, 56, 12, 33, 8, 2, 28, 6, 2, 39, 60, 11, 58, 54]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset29

namespace FullCoset30
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
end FullCoset30

namespace FullCoset31
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
end FullCoset31

end DegreeDiameter.Portfolio.F3Graph15552
