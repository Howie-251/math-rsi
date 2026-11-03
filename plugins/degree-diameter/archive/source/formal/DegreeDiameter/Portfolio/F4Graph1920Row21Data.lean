import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row21
open F4Graph3840
def wordData : Array Nat := #[38, 32, 28, 0, 21, 61, 0, 31, 0, 23, 9, 63, 26, 12, 54, 24, 50, 60, 41, 37, 10, 34, 0, 29, 0, 25, 48, 35, 13, 8]
def inversePool : Array (Array Nat) := #[#[2, 1, 3, 3, 3, 0, 2, 1, 2], #[1, 2, 3, 3, 2, 1, 2, 3, 0], #[0, 2, 3, 0, 0, 1, 1, 3, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 3, 1, 0, 0, 1, 1, 3, 1], #[3, 2, 0, 2, 0, 0, 2, 0, 1], #[0, 2, 3, 0, 2, 2, 1, 0, 0], #[0, 0, 2, 0, 1, 2, 1, 0, 3], #[3, 0, 1, 1, 0, 0, 3, 1, 3], #[2, 1, 0, 3, 3, 0, 1, 2, 1], #[0, 1, 3, 0, 3, 3, 1, 0, 1], #[2, 0, 3, 2, 0, 1, 1, 1, 2], #[3, 0, 0, 2, 1, 0, 3, 0, 1], #[0, 3, 0, 0, 2, 1, 1, 3, 1], #[1, 3, 0, 2, 3, 0, 1, 3, 1], #[2, 1, 0, 2, 0, 0, 2, 0, 1], #[2, 3, 1, 0, 2, 2, 0, 2, 3], #[2, 1, 3, 1, 0, 1, 3, 2, 0], #[3, 0, 2, 2, 0, 0, 3, 1, 3], #[2, 0, 2, 0, 1, 1, 2, 0, 3], #[0, 3, 3, 0, 1, 2, 1, 1, 1], #[2, 0, 1, 0, 0, 3, 2, 1, 1], #[0, 2, 0, 0, 2, 1, 1, 0, 1], #[3, 2, 0, 3, 0, 0, 1, 3, 1], #[2, 2, 0, 1, 2, 3, 2, 2, 1], #[0, 0, 2, 3, 0, 2, 0, 1, 2], #[3, 0, 0, 2, 0, 1, 3, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 3, 6, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 3, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 129, 453, 226, 67, 145, 452, 242, 83, 161, 455, 194, 99, 177, 454, 210, 115, 130, 65, 458, 243, 146, 81, 459, 227, 162, 97, 456, 211, 178, 113, 457, 195, 131, 209, 66, 463, 147, 193, 82, 462, 163, 241, 98, 461, 179, 225, 114, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 243, 227, 211, 195, 130, 146, 162, 178, 1, 17, 33, 49, 392, 393, 394, 395, 2, 18, 34, 50, 209, 193, 241, 225, 131, 147, 163, 179, 396, 397, 398, 399, 129, 145, 161, 177, 3, 19, 35, 51, 226, 242, 194, 210], #[0, 1, 2, 3, 324, 389, 65, 209, 328, 226, 394, 66, 332, 67, 243, 399, 388, 325, 193, 81, 17, 16, 19, 18, 83, 333, 398, 227, 242, 329, 82, 395, 392, 98, 330, 194, 211, 397, 334, 99, 34, 35, 32, 33, 97, 241, 326, 391, 396, 195, 115, 335, 114, 393, 210, 331, 225, 113, 390, 327, 51, 50, 49, 48], #[0, 260, 264, 268, 65, 453, 162, 3, 66, 1, 458, 179, 67, 145, 2, 463, 16, 261, 265, 269, 81, 452, 178, 19, 82, 17, 459, 163, 83, 129, 18, 462, 32, 262, 266, 270, 97, 455, 130, 35, 98, 33, 456, 147, 99, 177, 34, 461, 48, 263, 267, 271, 113, 454, 146, 51, 114, 49, 457, 131, 115, 161, 50, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row21
