import DegreeDiameter.Portfolio.F3Graph15552Routes

/- Existing complete coset certificates copied as data only; no coverage is recomputed. -/
namespace DegreeDiameter.Portfolio.F3Graph15552

namespace FullCoset36
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
end FullCoset36

namespace FullCoset37
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
end FullCoset37

namespace FullCoset38
abbrev K := Fin 5
def reference : List (Fin 5) := [4, 3]
def word : K → List (Fin 5) := ![
  [4, 3],
  [4, 3, 0],
  [1, 3, 4, 3],
  [4, 0, 0, 3],
  [4, 1, 3, 3]]
def globalWordIndex : K → Nat := ![29, 146, 379, 659, 699]
def columnCode : K → Fin 4 → Nat := ![
  ![0, 0, 0, 0],
  ![3, 6, 6, 3],
  ![6, 0, 0, 0],
  ![0, 0, 0, 0],
  ![0, 0, 0, 0]]
def column (k : K) (j : Fin 4) : Vec :=
  decodeVec ⟨columnCode k j % 81, Nat.mod_lt _ (by decide)⟩
def choice : Fin 81 → K := ![0, 3, 3, 2, 4, 1, 2, 1, 4, 0, 3, 3, 2, 4, 1, 2, 1, 4, 0, 3, 3, 2, 4, 1, 2, 1, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 2, 1, 3, 0, 3, 1, 2, 4, 4, 1, 2, 1, 4, 2, 3, 3, 0, 4, 1, 2, 1, 4, 2, 3, 3, 0, 4, 1, 2, 1, 4, 2, 3, 3, 0]
def alphaCode : Fin 81 → Nat := ![0, 36, 72, 12, 29, 22, 24, 17, 55, 1, 46, 55, 21, 36, 26, 6, 9, 65, 2, 29, 65, 3, 46, 18, 15, 13, 72, 18, 42, 19, 11, 5, 56, 6, 30, 73, 1, 51, 23, 18, 3, 63, 1, 39, 56, 11, 33, 24, 1, 4, 73, 5, 48, 63, 9, 11, 75, 3, 38, 60, 19, 28, 7, 19, 12, 57, 7, 45, 69, 2, 38, 8, 2, 16, 66, 2, 28, 78, 9, 45, 6]
def alpha (z : Fin 81) : Vec :=
  decodeVec ⟨alphaCode z % 81, Nat.mod_lt _ (by decide)⟩
end FullCoset38

namespace FullCoset39
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
end FullCoset39

end DegreeDiameter.Portfolio.F3Graph15552
