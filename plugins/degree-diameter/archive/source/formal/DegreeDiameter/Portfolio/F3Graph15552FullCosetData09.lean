import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset44
abbrev K := Fin 6
def reference : List (Fin 5) := [4, 4]
def word : K → List (Fin 5) := ![
  [4, 4],
  [4, 4, 0],
  [0, 0, 4, 4],
  [1, 3, 4, 4],
  [4, 3, 1, 4],
  [4, 4, 3, 1]]
def globalWordIndex : K → Nat := ![30, 151, 180, 380, 740, 772]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 5, 5, 1, 3, 4, 1, 4, 3, 2, 1, 3, 0, 1, 5, 2, 1, 4, 2, 3, 1, 2, 4, 1, 0, 5, 1, 3, 1, 2, 4, 1, 2, 5, 1, 0, 5, 5, 0, 3, 4, 1, 4, 3, 1, 1, 3, 2, 1, 5, 0, 1, 4, 2, 3, 2, 1, 5, 0, 1, 4, 2, 1, 1, 2, 3, 1, 2, 4, 1, 0, 5, 5, 0, 5, 4, 1, 3, 3, 1, 4]
def alphaCode : Fin 81 → Nat := ![0, 29, 55, 6, 30, 73, 3, 38, 60, 12, 15, 78, 2, 12, 54, 6, 9, 63, 24, 39, 21, 3, 45, 18, 1, 27, 24, 21, 10, 60, 1, 16, 66, 7, 13, 8, 6, 35, 7, 12, 29, 22, 18, 42, 19, 4, 33, 75, 1, 34, 6, 7, 46, 69, 15, 30, 20, 5, 4, 26, 2, 51, 23, 8, 42, 57, 5, 48, 65, 2, 3, 59, 3, 5, 58, 9, 11, 75, 24, 17, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset44

namespace FullCoset45
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
end FullCoset45

namespace FullCoset46
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
end FullCoset46

namespace FullCoset47
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
end FullCoset47

end DegreeDiameter.Portfolio.F3Graph15552
