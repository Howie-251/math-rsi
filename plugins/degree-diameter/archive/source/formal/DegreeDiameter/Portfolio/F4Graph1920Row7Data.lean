import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row7
open F4Graph3840
def wordData : Array Nat := #[9, 22, 60, 39, 3, 13, 29, 38, 50, 42, 2, 0, 15, 0, 35, 8, 0, 32, 34, 48, 53, 40, 24, 54, 41, 0, 28, 0, 63, 61]
def inversePool : Array (Array Nat) := #[#[1, 0, 3, 2, 0, 3, 2, 1, 3], #[0, 2, 3, 0, 3, 2, 1, 1, 2], #[3, 2, 0, 2, 3, 0, 2, 3, 1], #[1, 2, 3, 3, 3, 0, 1, 2, 2], #[3, 0, 1, 1, 0, 1, 1, 1, 2], #[1, 0, 1, 2, 0, 3, 3, 1, 3], #[0, 2, 3, 0, 0, 1, 1, 2, 3], #[2, 1, 3, 3, 3, 0, 2, 1, 2], #[3, 3, 0, 0, 3, 0, 2, 2, 1], #[3, 2, 1, 1, 2, 3, 2, 0, 3], #[2, 0, 0, 0, 0, 1, 3, 1, 0], #[1, 0, 3, 1, 0, 2, 1, 1, 3], #[3, 0, 1, 0, 0, 3, 2, 1, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 1, 2, 3, 3, 0, 2, 3, 0], #[2, 0, 1, 0, 0, 1, 2, 1, 0], #[1, 2, 3, 3, 3, 0, 2, 3, 0], #[3, 0, 3, 1, 1, 0, 2, 0, 3], #[2, 3, 0, 3, 0, 0, 3, 1, 1], #[2, 1, 0, 0, 1, 0, 1, 3, 1], #[2, 3, 1, 3, 3, 0, 3, 3, 1], #[0, 0, 2, 0, 2, 3, 1, 2, 2], #[2, 1, 0, 0, 3, 0, 2, 1, 1], #[3, 1, 2, 3, 2, 1, 3, 2, 0], #[0, 3, 1, 0, 1, 3, 1, 0, 0], #[0, 2, 0, 2, 2, 0, 2, 0, 1], #[2, 3, 0, 1, 1, 0, 1, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 13, 16, 17, 18, 19, 20, 21, 22, 23, 13, 24, 13, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 65, 66, 67, 1, 81, 82, 83, 2, 97, 98, 99, 3, 113, 114, 115, 388, 453, 129, 209, 389, 452, 145, 193, 390, 455, 161, 241, 391, 454, 177, 225, 392, 226, 458, 130, 393, 242, 459, 146, 394, 194, 456, 162, 395, 210, 457, 178, 396, 131, 243, 463, 397, 147, 227, 462, 398, 163, 211, 461, 399, 179, 195, 460], #[0, 16, 32, 48, 226, 242, 194, 210, 243, 227, 211, 195, 209, 193, 241, 225, 388, 389, 390, 391, 453, 452, 455, 454, 2, 18, 34, 50, 130, 146, 162, 178, 392, 393, 394, 395, 131, 147, 163, 179, 458, 459, 456, 457, 3, 19, 35, 51, 396, 397, 398, 399, 1, 17, 33, 49, 129, 145, 161, 177, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 67, 2, 209, 328, 226, 65, 3, 332, 1, 243, 66, 83, 325, 193, 18, 261, 16, 269, 265, 17, 333, 82, 227, 242, 329, 19, 81, 97, 35, 330, 194, 211, 98, 334, 33, 266, 270, 32, 262, 34, 241, 326, 99, 114, 195, 49, 335, 51, 113, 210, 331, 225, 50, 115, 327, 271, 267, 263, 48], #[0, 260, 264, 268, 324, 1, 179, 66, 328, 67, 2, 145, 332, 162, 65, 3, 16, 261, 265, 269, 325, 17, 163, 82, 329, 83, 18, 129, 333, 178, 81, 19, 32, 262, 266, 270, 326, 33, 147, 98, 330, 99, 34, 177, 334, 130, 97, 35, 48, 263, 267, 271, 327, 49, 131, 114, 331, 115, 50, 161, 335, 146, 113, 51]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row7
