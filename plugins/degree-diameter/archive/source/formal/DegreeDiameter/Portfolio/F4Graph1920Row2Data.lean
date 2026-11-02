import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row2
open F4Graph3840
def wordData : Array Nat := #[0, 0, 37, 28, 51, 25, 42, 32, 61, 53, 13, 0, 2, 34, 9, 41, 22, 8, 0, 31, 21, 24, 15, 48, 12, 0, 10, 55, 50, 35]
def inversePool : Array (Array Nat) := #[#[0, 0, 0, 0, 0, 0, 0, 0, 0], #[1, 3, 2, 0, 3, 3, 1, 3, 3], #[0, 3, 1, 0, 2, 1, 1, 1, 2], #[1, 0, 0, 1, 1, 0, 3, 0, 1], #[0, 3, 2, 0, 2, 3, 1, 3, 0], #[1, 3, 2, 1, 2, 3, 0, 1, 0], #[1, 2, 3, 1, 3, 2, 2, 3, 0], #[3, 2, 0, 0, 1, 0, 0, 1, 1], #[3, 3, 0, 0, 1, 0, 3, 3, 1], #[1, 0, 3, 1, 0, 0, 1, 1, 3], #[1, 0, 3, 0, 0, 1, 1, 1, 3], #[1, 2, 3, 3, 2, 1, 3, 1, 3], #[0, 0, 3, 1, 0, 3, 1, 1, 0], #[1, 3, 2, 0, 1, 1, 0, 1, 0], #[0, 3, 1, 0, 2, 0, 1, 2, 3], #[1, 0, 1, 1, 0, 3, 3, 1, 1], #[0, 1, 1, 0, 0, 3, 1, 2, 2], #[0, 2, 1, 0, 3, 1, 1, 1, 3], #[0, 2, 3, 0, 2, 1, 1, 1, 0], #[3, 0, 1, 3, 0, 0, 2, 1, 3], #[0, 1, 0, 3, 0, 0, 0, 2, 1], #[0, 0, 2, 3, 0, 2, 0, 1, 3], #[1, 0, 2, 2, 0, 1, 1, 1, 2], #[2, 0, 0, 0, 0, 1, 0, 1, 1], #[2, 1, 0, 1, 0, 0, 1, 3, 1], #[1, 3, 0, 0, 2, 0, 3, 2, 1], #[0, 2, 2, 3, 2, 1, 0, 1, 0]]
def inverseIndex : Array Nat := #[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 65, 66, 67, 1, 81, 82, 83, 2, 97, 98, 99, 3, 113, 114, 115, 388, 453, 129, 209, 389, 452, 145, 193, 390, 455, 161, 241, 391, 454, 177, 225, 392, 226, 458, 130, 393, 242, 459, 146, 394, 194, 456, 162, 395, 210, 457, 178, 396, 131, 243, 463, 397, 147, 227, 462, 398, 163, 211, 461, 399, 179, 195, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 209, 193, 241, 225, 453, 452, 455, 454, 130, 146, 162, 178, 3, 19, 35, 51, 226, 242, 194, 210, 1, 17, 33, 49, 458, 459, 456, 457, 131, 147, 163, 179, 243, 227, 211, 195, 129, 145, 161, 177, 2, 18, 34, 50, 463, 462, 461, 460], #[0, 260, 264, 268, 209, 389, 66, 3, 226, 1, 394, 67, 243, 65, 2, 399, 388, 193, 19, 82, 261, 16, 269, 265, 81, 227, 398, 18, 17, 242, 83, 395, 392, 99, 194, 33, 34, 397, 211, 97, 266, 270, 32, 262, 98, 35, 241, 391, 396, 50, 113, 195, 115, 393, 49, 210, 51, 114, 390, 225, 271, 267, 263, 48], #[0, 260, 264, 268, 2, 453, 67, 145, 3, 162, 458, 65, 1, 66, 179, 463, 16, 261, 265, 269, 18, 452, 83, 129, 19, 178, 459, 81, 17, 82, 163, 462, 32, 262, 266, 270, 34, 455, 99, 177, 35, 130, 456, 97, 33, 98, 147, 461, 48, 263, 267, 271, 50, 454, 115, 161, 51, 146, 457, 113, 49, 114, 131, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row2
