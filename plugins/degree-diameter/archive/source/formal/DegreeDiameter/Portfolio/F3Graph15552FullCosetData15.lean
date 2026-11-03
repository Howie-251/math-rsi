import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset70
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
end FullCoset70

namespace FullCoset71
abbrev K := Fin 5
def reference : List (Fin 5) := [0, 4]
def word : K → List (Fin 5) := ![
  [0, 4],
  [0, 1, 3, 4],
  [0, 3, 1, 4],
  [0, 4, 0, 0],
  [3, 1, 0, 4]]
def globalWordIndex : K → Nat := ![10, 200, 240, 256, 560]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 4, 4, 0, 4, 4, 0, 4, 4, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 4, 4, 0, 4, 4, 0, 4, 4, 0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 0, 4, 4, 0, 4, 4, 0, 4, 2, 1, 3, 2, 1, 3, 2, 1, 3]
def alphaCode : Fin 81 → Nat := ![0, 51, 66, 1, 33, 75, 2, 42, 57, 11, 28, 73, 18, 29, 56, 1, 27, 63, 19, 38, 56, 2, 45, 54, 9, 28, 55, 6, 36, 55, 7, 46, 65, 8, 29, 72, 1, 34, 63, 11, 35, 73, 18, 33, 56, 15, 30, 8, 24, 39, 6, 6, 48, 7, 3, 29, 72, 4, 36, 55, 5, 46, 65, 21, 4, 60, 3, 5, 69, 12, 3, 78, 2, 45, 59, 9, 28, 57, 19, 38, 58]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset71

namespace FullCoset72
abbrev K := Fin 5
def reference : List (Fin 5) := [3, 4]
def word : K → List (Fin 5) := ![
  [3, 4],
  [3, 0, 4],
  [0, 0, 3, 4],
  [3, 3, 1, 4],
  [3, 4, 0, 0]]
def globalWordIndex : K → Nat := ![25, 110, 175, 615, 631]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![0, 1, 2, 2],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 2, 2, 1, 4, 3, 1, 3, 4, 1, 3, 4, 0, 2, 2, 1, 4, 3, 1, 4, 3, 1, 3, 4, 0, 2, 2, 4, 3, 1, 3, 4, 1, 2, 2, 0, 2, 2, 0, 4, 3, 1, 3, 4, 1, 3, 4, 1, 2, 2, 0, 4, 3, 1, 4, 1, 3, 2, 0, 2, 3, 1, 4, 3, 1, 4, 4, 1, 3, 2, 0, 2, 2, 0, 2, 3, 1, 4, 4, 1, 3]
def alphaCode : Fin 81 → Nat := ![0, 48, 69, 3, 28, 73, 6, 38, 56, 4, 28, 55, 2, 39, 60, 1, 27, 63, 8, 29, 56, 2, 45, 54, 1, 30, 78, 6, 36, 19, 1, 34, 22, 12, 33, 8, 3, 51, 7, 8, 29, 26, 18, 33, 20, 11, 35, 24, 21, 42, 6, 7, 46, 21, 3, 11, 72, 24, 4, 57, 2, 17, 59, 19, 12, 58, 5, 15, 65, 15, 3, 75, 6, 5, 66, 9, 10, 57, 4, 13, 55]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset72

namespace FullCoset73
abbrev K := Fin 5
def reference : List (Fin 5) := [1, 4]
def word : K → List (Fin 5) := ![
  [1, 4],
  [0, 0, 1, 4],
  [1, 0, 0, 4],
  [1, 1, 3, 4],
  [2, 4, 1, 4]]
def globalWordIndex : K → Nat := ![15, 165, 285, 325, 515]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0],
  ![6, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 3, 2, 3, 4, 2, 1, 1, 0, 4, 2, 3, 1, 0, 1, 3, 2, 4, 1, 0, 1, 3, 2, 4, 4, 2, 3, 2, 4, 3, 2, 3, 4, 0, 1, 1, 3, 4, 2, 1, 1, 0, 4, 3, 2, 1, 1, 0, 4, 3, 2, 3, 4, 2, 3, 2, 4, 4, 2, 3, 1, 0, 1, 2, 3, 4, 0, 1, 1, 2, 4, 3]
def alphaCode : Fin 81 → Nat := ![0, 51, 66, 9, 30, 73, 18, 38, 60, 12, 29, 73, 18, 42, 55, 6, 48, 7, 24, 38, 55, 3, 5, 69, 9, 29, 75, 21, 4, 60, 2, 46, 66, 15, 28, 72, 2, 48, 63, 11, 28, 78, 2, 42, 57, 11, 33, 72, 24, 39, 6, 3, 46, 63, 15, 30, 8, 21, 36, 56, 1, 51, 65, 19, 36, 57, 6, 45, 65, 12, 3, 78, 1, 45, 69, 1, 33, 75, 19, 39, 56]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset73

end DegreeDiameter.Portfolio.F3Graph15552
