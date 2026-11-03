import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row11
open F4Graph3840
def wordData : Array Nat := #[23, 24, 0, 25, 55, 48, 37, 40, 32, 63, 61, 53, 28, 54, 29, 10, 0, 51, 15, 50, 12, 42, 60, 0, 9, 8, 0, 22, 0, 39]
def inversePool : Array (Array Nat) := #[#[0, 2, 1, 0, 1, 2, 1, 2, 1], #[0, 1, 3, 0, 2, 3, 1, 0, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 2, 2, 0, 2, 1, 1, 1, 2], #[1, 3, 0, 2, 2, 0, 3, 2, 1], #[3, 1, 0, 0, 2, 0, 3, 1, 1], #[1, 1, 0, 1, 2, 3, 2, 2, 1], #[0, 1, 1, 1, 1, 0, 1, 1, 1], #[2, 3, 1, 2, 0, 2, 2, 3, 0], #[1, 2, 0, 1, 1, 0, 0, 3, 1], #[3, 1, 0, 2, 1, 0, 2, 1, 1], #[1, 2, 0, 2, 2, 0, 2, 3, 1], #[0, 3, 1, 0, 2, 0, 1, 2, 3], #[3, 3, 0, 3, 2, 0, 3, 3, 1], #[0, 1, 2, 0, 2, 1, 1, 0, 0], #[1, 0, 3, 1, 0, 2, 3, 1, 3], #[1, 1, 0, 0, 3, 0, 1, 1, 1], #[3, 0, 2, 2, 0, 3, 2, 1, 1], #[1, 2, 0, 0, 1, 0, 1, 2, 1], #[0, 0, 2, 1, 0, 2, 0, 1, 3], #[2, 3, 1, 2, 1, 3, 0, 2, 3], #[0, 1, 0, 1, 0, 0, 1, 0, 1], #[2, 0, 3, 3, 0, 2, 0, 1, 3], #[0, 0, 1, 2, 0, 3, 2, 1, 0], #[0, 2, 3, 0, 0, 2, 1, 1, 2], #[3, 0, 2, 0, 0, 3, 2, 1, 1], #[3, 2, 1, 0, 3, 3, 2, 1, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 16, 17, 18, 19, 20, 21, 2, 22, 23, 2, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 65, 453, 226, 131, 81, 452, 242, 147, 97, 455, 194, 163, 113, 454, 210, 179, 66, 129, 458, 243, 82, 145, 459, 227, 98, 161, 456, 211, 114, 177, 457, 195, 67, 209, 130, 463, 83, 193, 146, 462, 99, 241, 162, 461, 115, 225, 178, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 226, 242, 194, 210, 129, 145, 161, 177, 3, 19, 35, 51, 392, 393, 394, 395, 1, 17, 33, 49, 243, 227, 211, 195, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 2, 18, 34, 50, 209, 193, 241, 225], #[0, 260, 264, 268, 1, 389, 226, 67, 2, 65, 394, 243, 3, 209, 66, 399, 388, 17, 83, 242, 261, 16, 269, 265, 193, 19, 398, 82, 81, 18, 227, 395, 392, 211, 34, 97, 98, 397, 35, 241, 266, 270, 32, 262, 194, 99, 33, 391, 396, 114, 225, 51, 195, 393, 113, 50, 115, 210, 390, 49, 271, 267, 263, 48], #[0, 260, 264, 268, 324, 65, 3, 162, 328, 179, 66, 1, 332, 2, 145, 67, 16, 261, 265, 269, 325, 81, 19, 178, 329, 163, 82, 17, 333, 18, 129, 83, 32, 262, 266, 270, 326, 97, 35, 130, 330, 147, 98, 33, 334, 34, 177, 99, 48, 263, 267, 271, 327, 113, 51, 146, 331, 131, 114, 49, 335, 50, 161, 115]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row11
