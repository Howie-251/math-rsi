import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row5
open F4Graph3840
def wordData : Array Nat := #[28, 35, 12, 0, 60, 8, 24, 9, 23, 32, 26, 22, 0, 38, 13, 0, 53, 63, 61, 0, 41, 37, 50, 34, 25, 48, 51, 40, 54, 0]
def inversePool : Array (Array Nat) := #[#[0, 2, 3, 0, 1, 3, 1, 3, 1], #[3, 1, 2, 3, 2, 1, 3, 1, 3], #[3, 0, 3, 2, 0, 3, 2, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 1, 0, 3, 3, 0, 3, 3, 1], #[2, 0, 1, 2, 0, 3, 3, 1, 0], #[0, 2, 1, 0, 0, 1, 1, 3, 3], #[3, 0, 2, 3, 0, 3, 0, 1, 1], #[0, 2, 1, 0, 1, 2, 1, 0, 0], #[0, 2, 2, 1, 2, 3, 0, 2, 3], #[0, 3, 3, 0, 2, 0, 1, 2, 0], #[0, 1, 2, 0, 1, 3, 1, 3, 1], #[3, 0, 3, 2, 2, 0, 3, 0, 2], #[3, 0, 1, 1, 0, 3, 3, 1, 1], #[2, 3, 0, 2, 1, 0, 0, 0, 1], #[3, 2, 0, 0, 1, 0, 3, 3, 1], #[1, 3, 0, 0, 1, 0, 0, 1, 1], #[1, 0, 3, 3, 0, 1, 3, 1, 2], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[2, 1, 3, 1, 0, 1, 0, 0, 1], #[1, 2, 0, 2, 2, 0, 2, 3, 1], #[2, 3, 1, 1, 0, 1, 3, 1, 3], #[0, 3, 2, 0, 2, 0, 1, 0, 1], #[1, 3, 0, 3, 0, 0, 1, 3, 1], #[3, 2, 0, 1, 1, 0, 3, 2, 1], #[2, 1, 3, 2, 0, 2, 2, 0, 3], #[1, 2, 0, 2, 1, 0, 1, 2, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 12, 13, 3, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 3]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 209, 453, 130, 67, 193, 452, 146, 83, 241, 455, 162, 99, 225, 454, 178, 115, 226, 65, 458, 131, 242, 81, 459, 147, 194, 97, 456, 163, 210, 113, 457, 179, 243, 129, 66, 463, 227, 145, 82, 462, 211, 161, 98, 461, 195, 177, 114, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 209, 193, 241, 225, 453, 452, 455, 454, 130, 146, 162, 178, 3, 19, 35, 51, 226, 242, 194, 210, 1, 17, 33, 49, 458, 459, 456, 457, 131, 147, 163, 179, 243, 227, 211, 195, 129, 145, 161, 177, 2, 18, 34, 50, 463, 462, 461, 460], #[0, 226, 243, 209, 324, 389, 2, 66, 328, 67, 394, 3, 332, 1, 65, 399, 388, 325, 82, 18, 242, 16, 193, 227, 17, 333, 398, 81, 83, 329, 19, 395, 392, 35, 330, 99, 97, 397, 334, 33, 211, 241, 32, 194, 34, 98, 326, 391, 396, 113, 49, 335, 51, 393, 115, 331, 114, 50, 390, 327, 225, 195, 210, 48], #[0, 260, 264, 268, 162, 453, 67, 1, 179, 2, 458, 65, 145, 66, 3, 463, 16, 261, 265, 269, 178, 452, 83, 17, 163, 18, 459, 81, 129, 82, 19, 462, 32, 262, 266, 270, 130, 455, 99, 33, 147, 34, 456, 97, 177, 98, 35, 461, 48, 263, 267, 271, 146, 454, 115, 49, 131, 50, 457, 113, 161, 114, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row5
