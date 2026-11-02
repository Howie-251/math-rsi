import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row16
open F4Graph3840
def wordData : Array Nat := #[63, 40, 48, 24, 9, 2, 0, 0, 26, 12, 60, 0, 3, 25, 28, 53, 32, 39, 31, 55, 37, 54, 42, 0, 8, 13, 0, 34, 38, 50]
def inversePool : Array (Array Nat) := #[#[3, 2, 0, 3, 3, 0, 0, 1, 1], #[1, 0, 1, 0, 2, 2, 0, 2, 3], #[3, 3, 0, 1, 0, 0, 3, 3, 1], #[0, 3, 3, 0, 2, 1, 1, 0, 3], #[1, 0, 3, 2, 0, 3, 3, 1, 0], #[2, 0, 3, 3, 0, 2, 1, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 3, 3, 0, 1, 2, 1, 0, 3], #[1, 0, 2, 3, 0, 2, 2, 1, 3], #[1, 2, 0, 3, 3, 0, 3, 3, 1], #[2, 0, 1, 1, 0, 2, 2, 1, 1], #[0, 2, 1, 0, 3, 3, 1, 2, 0], #[0, 3, 1, 0, 2, 1, 1, 3, 1], #[2, 1, 0, 0, 1, 0, 1, 3, 1], #[3, 2, 1, 1, 0, 1, 3, 2, 0], #[2, 2, 0, 1, 2, 3, 2, 2, 1], #[0, 2, 3, 0, 0, 2, 1, 1, 2], #[0, 2, 0, 1, 0, 0, 0, 2, 1], #[2, 0, 2, 1, 2, 3, 1, 0, 0], #[0, 2, 0, 1, 0, 0, 0, 0, 1], #[3, 2, 1, 1, 2, 3, 2, 0, 3], #[1, 0, 0, 2, 0, 1, 3, 1, 0], #[1, 0, 2, 3, 0, 2, 2, 1, 0], #[2, 0, 1, 2, 0, 3, 2, 1, 1], #[1, 1, 0, 0, 3, 3, 1, 1, 1], #[2, 2, 0, 1, 0, 1, 0, 0, 1], #[0, 2, 0, 3, 2, 0, 0, 2, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 6, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 209, 453, 130, 67, 193, 452, 146, 83, 241, 455, 162, 99, 225, 454, 178, 115, 226, 65, 458, 131, 242, 81, 459, 147, 194, 97, 456, 163, 210, 113, 457, 179, 243, 129, 66, 463, 227, 145, 82, 462, 211, 161, 98, 461, 195, 177, 114, 460], #[0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 388, 389, 390, 391, 453, 452, 455, 454, 129, 145, 161, 177, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 3, 66, 209, 328, 226, 1, 67, 332, 65, 243, 2, 19, 325, 193, 82, 261, 16, 269, 265, 81, 333, 18, 227, 242, 329, 83, 17, 33, 99, 330, 194, 211, 34, 334, 97, 266, 270, 32, 262, 98, 241, 326, 35, 50, 195, 113, 335, 115, 49, 210, 331, 225, 114, 51, 327, 271, 267, 263, 48], #[0, 65, 66, 67, 324, 453, 1, 145, 328, 162, 458, 2, 332, 3, 179, 463, 16, 81, 82, 83, 325, 452, 17, 129, 329, 178, 459, 18, 333, 19, 163, 462, 32, 97, 98, 99, 326, 455, 33, 177, 330, 130, 456, 34, 334, 35, 147, 461, 48, 113, 114, 115, 327, 454, 49, 161, 331, 146, 457, 50, 335, 51, 131, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row16
