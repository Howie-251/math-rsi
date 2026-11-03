import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row3
open F4Graph3840
def wordData : Array Nat := #[55, 0, 24, 40, 37, 0, 22, 35, 42, 25, 32, 12, 53, 8, 2, 13, 28, 0, 50, 60, 48, 0, 29, 26, 15, 3, 63, 0, 41, 54]
def inversePool : Array (Array Nat) := #[#[3, 0, 0, 2, 2, 0, 3, 0, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 2, 1, 0, 0, 1, 1, 3, 3], #[2, 1, 3, 2, 0, 2, 2, 0, 3], #[1, 3, 2, 1, 2, 3, 1, 3, 3], #[0, 0, 1, 0, 1, 3, 1, 0, 0], #[1, 2, 3, 1, 3, 2, 3, 1, 3], #[1, 3, 2, 3, 3, 0, 2, 0, 3], #[0, 1, 3, 0, 0, 1, 1, 0, 1], #[0, 1, 1, 1, 2, 3, 0, 2, 3], #[2, 0, 3, 2, 0, 1, 3, 1, 1], #[2, 1, 0, 2, 2, 0, 2, 1, 1], #[3, 0, 0, 2, 0, 1, 0, 1, 1], #[1, 0, 3, 0, 0, 1, 0, 1, 0], #[3, 0, 1, 0, 0, 1, 3, 1, 1], #[0, 3, 3, 0, 2, 3, 1, 2, 2], #[1, 2, 0, 2, 0, 0, 1, 2, 1], #[1, 3, 0, 3, 3, 0, 3, 3, 1], #[2, 3, 0, 2, 2, 0, 3, 1, 1], #[0, 2, 1, 0, 2, 3, 1, 3, 2], #[0, 3, 2, 0, 2, 0, 1, 1, 2], #[0, 0, 3, 3, 0, 1, 0, 1, 2], #[3, 0, 1, 2, 0, 1, 3, 1, 1], #[0, 1, 0, 2, 3, 0, 2, 2, 1], #[2, 0, 1, 0, 0, 3, 2, 1, 1], #[2, 3, 1, 1, 1, 0, 1, 1, 1], #[3, 2, 0, 0, 3, 0, 3, 2, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 16, 17, 18, 1, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 226, 129, 67, 389, 242, 145, 83, 390, 194, 161, 99, 391, 210, 177, 115, 392, 65, 243, 130, 393, 81, 227, 146, 394, 97, 211, 162, 395, 113, 195, 178, 396, 131, 66, 209, 397, 147, 82, 193, 398, 163, 98, 241, 399, 179, 114, 225], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 129, 145, 161, 177, 453, 452, 455, 454, 226, 242, 194, 210, 3, 19, 35, 51, 130, 146, 162, 178, 1, 17, 33, 49, 458, 459, 456, 457, 243, 227, 211, 195, 131, 147, 163, 179, 209, 193, 241, 225, 2, 18, 34, 50, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 67, 2, 209, 328, 226, 65, 3, 332, 1, 243, 66, 83, 325, 193, 18, 261, 16, 269, 265, 17, 333, 82, 227, 242, 329, 19, 81, 97, 35, 330, 194, 211, 98, 334, 33, 266, 270, 32, 262, 34, 241, 326, 99, 114, 195, 49, 335, 51, 113, 210, 331, 225, 50, 115, 327, 271, 267, 263, 48], #[0, 260, 264, 268, 162, 453, 67, 1, 179, 2, 458, 65, 145, 66, 3, 463, 16, 261, 265, 269, 178, 452, 83, 17, 163, 18, 459, 81, 129, 82, 19, 462, 32, 262, 266, 270, 130, 455, 99, 33, 147, 34, 456, 97, 177, 98, 35, 461, 48, 263, 267, 271, 146, 454, 115, 49, 131, 50, 457, 113, 161, 114, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row3
