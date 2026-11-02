import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row4
open F4Graph3840
def wordData : Array Nat := #[50, 21, 38, 3, 32, 26, 51, 37, 0, 8, 0, 34, 48, 61, 10, 42, 13, 28, 0, 9, 60, 0, 35, 31, 55, 0, 40, 12, 15, 25]
def inversePool : Array (Array Nat) := #[#[1, 2, 0, 0, 3, 0, 3, 1, 1], #[0, 1, 2, 0, 1, 1, 1, 2, 3], #[3, 2, 1, 3, 1, 2, 0, 0, 1], #[2, 0, 1, 1, 0, 0, 3, 1, 2], #[2, 3, 1, 3, 2, 1, 2, 3, 0], #[0, 1, 3, 0, 3, 0, 1, 0, 2], #[2, 0, 0, 0, 1, 0, 2, 0, 1], #[3, 2, 1, 1, 2, 3, 1, 3, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 0, 0, 3, 0, 2, 3, 1, 2], #[2, 3, 1, 0, 2, 2, 1, 2, 2], #[0, 2, 0, 3, 0, 0, 0, 2, 1], #[1, 2, 0, 0, 3, 0, 0, 3, 1], #[0, 0, 3, 1, 0, 0, 1, 1, 1], #[3, 2, 1, 0, 1, 1, 3, 3, 1], #[1, 0, 2, 0, 0, 1, 3, 1, 1], #[0, 1, 2, 0, 2, 0, 1, 2, 3], #[1, 0, 1, 1, 0, 3, 3, 1, 1], #[0, 2, 0, 1, 0, 0, 1, 0, 1], #[1, 0, 3, 3, 0, 1, 3, 1, 2], #[3, 1, 2, 0, 1, 1, 3, 1, 3], #[0, 1, 1, 0, 0, 3, 1, 2, 2], #[1, 3, 2, 1, 2, 3, 1, 2, 2], #[0, 0, 2, 3, 0, 2, 0, 1, 2], #[0, 0, 2, 3, 0, 0, 0, 1, 1], #[0, 1, 2, 0, 1, 1, 1, 3, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 10, 11, 12, 13, 14, 15, 16, 8, 17, 18, 19, 20, 21, 6, 8, 22, 23, 24, 25]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 65, 453, 226, 131, 81, 452, 242, 147, 97, 455, 194, 163, 113, 454, 210, 179, 66, 129, 458, 243, 82, 145, 459, 227, 98, 161, 456, 211, 114, 177, 457, 195, 67, 209, 130, 463, 83, 193, 146, 462, 99, 241, 162, 461, 115, 225, 178, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 209, 193, 241, 225, 453, 452, 455, 454, 130, 146, 162, 178, 3, 19, 35, 51, 226, 242, 194, 210, 1, 17, 33, 49, 458, 459, 456, 457, 131, 147, 163, 179, 243, 227, 211, 195, 129, 145, 161, 177, 2, 18, 34, 50, 463, 462, 461, 460], #[0, 260, 264, 268, 65, 389, 226, 3, 66, 1, 394, 243, 67, 209, 2, 399, 388, 81, 19, 242, 261, 16, 269, 265, 193, 83, 398, 18, 17, 82, 227, 395, 392, 211, 98, 33, 34, 397, 99, 241, 266, 270, 32, 262, 194, 35, 97, 391, 396, 50, 225, 115, 195, 393, 49, 114, 51, 210, 390, 113, 271, 267, 263, 48], #[0, 260, 264, 268, 324, 67, 2, 145, 328, 162, 65, 3, 332, 1, 179, 66, 16, 261, 265, 269, 325, 83, 18, 129, 329, 178, 81, 19, 333, 17, 163, 82, 32, 262, 266, 270, 326, 99, 34, 177, 330, 130, 97, 35, 334, 33, 147, 98, 48, 263, 267, 271, 327, 115, 50, 161, 331, 146, 113, 51, 335, 49, 131, 114]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row4
