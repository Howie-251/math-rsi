import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row27
open F4Graph3840
def wordData : Array Nat := #[13, 28, 34, 21, 8, 31, 32, 0, 9, 50, 42, 48, 22, 24, 15, 0, 55, 26, 2, 41, 0, 39, 54, 60, 0, 12, 53, 61, 29, 3]
def inversePool : Array (Array Nat) := #[#[1, 0, 1, 2, 0, 3, 3, 1, 3], #[0, 3, 3, 0, 2, 3, 1, 2, 2], #[0, 2, 2, 3, 0, 3, 0, 1, 0], #[0, 3, 2, 0, 1, 2, 1, 0, 0], #[2, 0, 1, 2, 0, 3, 1, 1, 1], #[0, 2, 2, 0, 0, 1, 1, 3, 3], #[1, 2, 3, 3, 3, 0, 0, 0, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 0, 3, 2, 0, 1, 3, 1, 0], #[3, 2, 0, 0, 2, 0, 2, 1, 1], #[1, 3, 2, 2, 0, 2, 3, 3, 1], #[0, 1, 0, 1, 2, 0, 0, 0, 1], #[0, 3, 0, 0, 2, 2, 1, 3, 0], #[0, 1, 3, 0, 3, 3, 1, 1, 2], #[3, 0, 1, 2, 0, 2, 2, 1, 3], #[3, 1, 0, 1, 0, 0, 3, 1, 1], #[0, 1, 3, 0, 3, 3, 1, 0, 1], #[2, 0, 2, 1, 0, 0, 3, 1, 3], #[1, 2, 3, 3, 3, 0, 3, 3, 1], #[1, 3, 2, 1, 0, 1, 1, 3, 3], #[3, 2, 0, 0, 1, 0, 2, 1, 1], #[3, 1, 0, 1, 1, 0, 1, 1, 1], #[3, 0, 2, 2, 0, 3, 1, 1, 3], #[3, 1, 0, 0, 2, 0, 2, 3, 1], #[2, 3, 0, 1, 1, 0, 1, 1, 1], #[0, 3, 2, 0, 1, 0, 1, 3, 2], #[2, 0, 1, 3, 0, 1, 2, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 7, 15, 16, 17, 18, 7, 19, 20, 21, 7, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 67, 130, 209, 389, 83, 146, 193, 390, 99, 162, 241, 391, 115, 178, 225, 392, 226, 65, 131, 393, 242, 81, 147, 394, 194, 97, 163, 395, 210, 113, 179, 396, 129, 243, 66, 397, 145, 227, 82, 398, 161, 211, 98, 399, 177, 195, 114], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 2, 18, 34, 50, 453, 452, 455, 454, 131, 147, 163, 179, 209, 193, 241, 225, 3, 19, 35, 51, 226, 242, 194, 210, 458, 459, 456, 457, 129, 145, 161, 177, 1, 17, 33, 49, 130, 146, 162, 178, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 2, 389, 67, 209, 3, 226, 394, 65, 1, 66, 243, 399, 388, 18, 193, 83, 261, 16, 269, 265, 82, 17, 398, 227, 242, 19, 81, 395, 392, 97, 35, 194, 211, 397, 33, 98, 266, 270, 32, 262, 99, 241, 34, 391, 396, 195, 114, 49, 113, 393, 210, 51, 225, 115, 390, 50, 271, 267, 263, 48], #[0, 260, 264, 268, 162, 453, 67, 1, 179, 2, 458, 65, 145, 66, 3, 463, 16, 261, 265, 269, 178, 452, 83, 17, 163, 18, 459, 81, 129, 82, 19, 462, 32, 262, 266, 270, 130, 455, 99, 33, 147, 34, 456, 97, 177, 98, 35, 461, 48, 263, 267, 271, 146, 454, 115, 49, 131, 50, 457, 113, 161, 114, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row27
