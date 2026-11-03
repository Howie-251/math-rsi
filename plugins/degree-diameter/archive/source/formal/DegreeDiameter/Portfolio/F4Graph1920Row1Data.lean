import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row1
open F4Graph3840
def wordData : Array Nat := #[21, 34, 0, 0, 0, 39, 54, 48, 22, 61, 35, 28, 42, 0, 32, 26, 8, 0, 13, 63, 51, 23, 38, 9, 2, 40, 25, 24, 60, 37]
def inversePool : Array (Array Nat) := #[#[0, 3, 2, 0, 1, 2, 1, 3, 2], #[2, 3, 1, 1, 1, 0, 1, 2, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 0, 1, 1, 0, 1, 3, 1, 1], #[1, 2, 3, 3, 3, 0, 3, 1, 3], #[1, 3, 0, 3, 1, 0, 3, 2, 1], #[3, 1, 0, 1, 1, 0, 2, 3, 1], #[0, 3, 2, 0, 2, 0, 1, 3, 2], #[3, 1, 0, 3, 2, 0, 3, 2, 1], #[0, 3, 3, 1, 2, 3, 0, 0, 1], #[0, 0, 3, 0, 1, 2, 1, 0, 0], #[0, 1, 1, 2, 3, 1, 2, 2, 1], #[0, 2, 0, 0, 0, 1, 1, 0, 1], #[1, 0, 3, 0, 0, 1, 2, 1, 0], #[1, 0, 3, 1, 0, 1, 0, 1, 0], #[2, 1, 0, 2, 0, 0, 0, 1, 1], #[3, 1, 0, 1, 3, 0, 0, 0, 1], #[0, 3, 2, 0, 1, 0, 1, 3, 2], #[0, 1, 1, 1, 3, 2, 0, 3, 2], #[2, 0, 3, 1, 0, 0, 3, 1, 3], #[1, 0, 3, 1, 0, 0, 3, 1, 2], #[3, 2, 1, 2, 0, 2, 2, 0, 3], #[0, 2, 2, 0, 1, 3, 1, 2, 0], #[0, 0, 1, 0, 2, 3, 1, 2, 2], #[0, 1, 0, 2, 3, 0, 2, 3, 1], #[3, 2, 1, 0, 3, 3, 1, 3, 3]]
def inverseIndex : Array Nat := #[0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 4, 12, 13, 2, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 209, 453, 130, 67, 193, 452, 146, 83, 241, 455, 162, 99, 225, 454, 178, 115, 226, 65, 458, 131, 242, 81, 459, 147, 194, 97, 456, 163, 210, 113, 457, 179, 243, 129, 66, 463, 227, 145, 82, 462, 211, 161, 98, 461, 195, 177, 114, 460], #[0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 388, 389, 390, 391, 453, 452, 455, 454, 129, 145, 161, 177, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 67, 2, 209, 328, 226, 65, 3, 332, 1, 243, 66, 83, 325, 193, 18, 261, 16, 269, 265, 17, 333, 82, 227, 242, 329, 19, 81, 97, 35, 330, 194, 211, 98, 334, 33, 266, 270, 32, 262, 34, 241, 326, 99, 114, 195, 49, 335, 51, 113, 210, 331, 225, 50, 115, 327, 271, 267, 263, 48], #[0, 260, 264, 268, 324, 67, 2, 145, 328, 162, 65, 3, 332, 1, 179, 66, 16, 261, 265, 269, 325, 83, 18, 129, 329, 178, 81, 19, 333, 17, 163, 82, 32, 262, 266, 270, 326, 99, 34, 177, 330, 130, 97, 35, 334, 33, 147, 98, 48, 263, 267, 271, 327, 115, 50, 161, 331, 146, 113, 51, 335, 49, 131, 114]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row1
