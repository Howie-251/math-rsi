import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row29
open F4Graph3840
def wordData : Array Nat := #[40, 61, 39, 50, 12, 0, 21, 60, 41, 0, 48, 35, 34, 28, 0, 0, 54, 13, 0, 24, 42, 29, 22, 25, 26, 31, 32, 37, 9, 53]
def inversePool : Array (Array Nat) := #[#[0, 1, 1, 1, 3, 2, 1, 3, 3], #[1, 0, 0, 2, 2, 0, 2, 2, 1], #[2, 1, 3, 0, 3, 3, 2, 1, 2], #[1, 2, 0, 1, 1, 0, 3, 1, 1], #[2, 0, 2, 2, 0, 3, 3, 1, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 0, 3, 0, 1, 2, 1, 0, 3], #[2, 0, 0, 2, 2, 0, 2, 2, 1], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[2, 0, 1, 1, 0, 2, 2, 1, 1], #[2, 0, 0, 1, 1, 0, 3, 0, 1], #[3, 1, 2, 2, 1, 3, 3, 1, 3], #[1, 3, 2, 3, 0, 3, 3, 2, 0], #[0, 3, 1, 0, 3, 3, 1, 2, 3], #[1, 2, 0, 2, 1, 0, 1, 2, 1], #[3, 0, 1, 1, 0, 3, 2, 1, 3], #[0, 2, 1, 0, 1, 2, 1, 1, 2], #[2, 1, 3, 2, 0, 2, 0, 1, 0], #[0, 2, 0, 0, 2, 1, 1, 2, 0], #[0, 2, 3, 0, 0, 2, 1, 1, 2], #[0, 2, 1, 0, 1, 2, 1, 0, 1], #[0, 1, 3, 0, 3, 3, 1, 3, 3], #[0, 3, 1, 0, 1, 0, 1, 2, 3], #[1, 2, 3, 0, 1, 1, 2, 3, 0], #[1, 2, 3, 3, 3, 0, 2, 3, 0], #[1, 0, 2, 3, 0, 2, 2, 1, 0], #[1, 3, 0, 2, 2, 0, 2, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 5, 14, 15, 5, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 209, 226, 243, 1, 193, 242, 227, 2, 241, 194, 211, 3, 225, 210, 195, 388, 453, 129, 65, 389, 452, 145, 81, 390, 455, 161, 97, 391, 454, 177, 113, 392, 66, 458, 130, 393, 82, 459, 146, 394, 98, 456, 162, 395, 114, 457, 178, 396, 131, 67, 463, 397, 147, 83, 462, 398, 163, 99, 461, 399, 179, 115, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 129, 145, 161, 177, 3, 19, 35, 51, 226, 242, 194, 210, 392, 393, 394, 395, 243, 227, 211, 195, 130, 146, 162, 178, 1, 17, 33, 49, 396, 397, 398, 399, 2, 18, 34, 50, 209, 193, 241, 225, 131, 147, 163, 179], #[0, 260, 264, 268, 2, 389, 67, 209, 3, 226, 394, 65, 1, 66, 243, 399, 388, 18, 193, 83, 261, 16, 269, 265, 82, 17, 398, 227, 242, 19, 81, 395, 392, 97, 35, 194, 211, 397, 33, 98, 266, 270, 32, 262, 99, 241, 34, 391, 396, 195, 114, 49, 113, 393, 210, 51, 225, 115, 390, 50, 271, 267, 263, 48], #[0, 260, 264, 268, 2, 453, 67, 145, 3, 162, 458, 65, 1, 66, 179, 463, 16, 261, 265, 269, 18, 452, 83, 129, 19, 178, 459, 81, 17, 82, 163, 462, 32, 262, 266, 270, 34, 455, 99, 177, 35, 130, 456, 97, 33, 98, 147, 461, 48, 263, 267, 271, 50, 454, 115, 161, 51, 146, 457, 113, 49, 114, 131, 460]]

def controllerWord (b : Fin 30) : Fin 64 := ⟨wordData.getD b.val 0 % 64,Nat.mod_lt _ (by decide)⟩
def wordP0 (w : Fin 64) : Fin 4 := ⟨w.val%4,Nat.mod_lt _ (by decide)⟩
def wordP1 (w : Fin 64) : Fin 4 := ⟨w.val/4%4,Nat.mod_lt _ (by decide)⟩
def wordP2 (w : Fin 64) : Fin 4 := ⟨w.val/16%4,Nat.mod_lt _ (by decide)⟩
def nbInverse (b : Fin 30) : Mat := fun i j =>
  F.ofCode ((inversePool.getD (inverseIndex.getD b.val 0) #[]).getD (i.val*3+j.val) 0)
def nbNoise (b : Fin 30) (d : Vec) : Vec := act (nbInverse b) d
def adjacentDecoder (p : Fin 4) (d : Fin 64) : Nat := (adjacentData.getD p.val #[]).getD d.val 0
def adjBefore (p : Fin 4) (d : Fin 64) : Prop := adjacentDecoder p d < 256
instance (p : Fin 4) (d : Fin 64) : Decidable (adjBefore p d) := inferInstanceAs (Decidable (_ < _))
def adjQ (p : Fin 4) (d : Fin 64) : Fin 4 := ⟨adjacentDecoder p d/64%4,Nat.mod_lt _ (by decide)⟩
def adjNoise (p : Fin 4) (d : Fin 64) : Vec := decodeVec ⟨adjacentDecoder p d%64,Nat.mod_lt _ (by decide)⟩
def adjP0 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then adjQ p d else p
def adjP1 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then inversePort (adjQ p d) else adjQ p d
def adjP2 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then p else inversePort (adjQ p d)
end DegreeDiameter.Portfolio.F4Graph1920.Row29
