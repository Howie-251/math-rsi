import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row0
open F4Graph3840
def wordData : Array Nat := #[48, 0, 0, 34, 54, 24, 3, 13, 60, 0, 12, 32, 21, 2, 23, 40, 42, 25, 0, 15, 0, 51, 53, 10, 29, 63, 39, 9, 35, 31]
def inversePool : Array (Array Nat) := #[#[1, 2, 0, 0, 3, 0, 2, 3, 1], #[0, 0, 3, 1, 0, 2, 0, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[1, 1, 0, 0, 3, 3, 1, 1, 1], #[2, 1, 0, 1, 0, 0, 2, 1, 1], #[0, 2, 1, 0, 2, 3, 1, 2, 3], #[3, 0, 3, 1, 0, 2, 1, 1, 1], #[3, 0, 1, 3, 0, 3, 3, 1, 1], #[2, 1, 0, 3, 3, 0, 3, 3, 1], #[2, 0, 1, 1, 0, 0, 0, 1, 0], #[1, 2, 3, 2, 1, 3, 2, 3, 0], #[0, 2, 0, 0, 1, 2, 1, 0, 0], #[2, 0, 1, 1, 0, 0, 1, 1, 3], #[0, 1, 3, 0, 1, 2, 1, 2, 1], #[2, 1, 3, 2, 0, 2, 2, 0, 3], #[3, 1, 2, 1, 0, 1, 2, 1, 2], #[0, 3, 2, 0, 2, 0, 1, 1, 2], #[1, 0, 2, 0, 0, 1, 1, 1, 2], #[2, 3, 0, 2, 2, 0, 2, 3, 1], #[1, 3, 0, 0, 1, 0, 1, 3, 1], #[3, 0, 1, 2, 0, 1, 1, 1, 0], #[0, 1, 2, 0, 2, 0, 1, 2, 3], #[0, 1, 0, 2, 1, 0, 2, 0, 1], #[0, 3, 3, 1, 2, 3, 0, 1, 0], #[3, 0, 1, 3, 0, 2, 0, 1, 3], #[2, 1, 3, 1, 1, 0, 2, 1, 2], #[0, 3, 2, 0, 2, 3, 1, 2, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 2, 9, 10, 11, 12, 13, 14, 15, 16, 2, 17, 2, 18, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 65, 243, 130, 389, 81, 227, 146, 390, 97, 211, 162, 391, 113, 195, 178, 392, 131, 66, 209, 393, 147, 82, 193, 394, 163, 98, 241, 395, 179, 114, 225, 396, 226, 129, 67, 397, 242, 145, 83, 398, 194, 161, 99, 399, 210, 177, 115], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 209, 193, 241, 225, 453, 452, 455, 454, 130, 146, 162, 178, 3, 19, 35, 51, 226, 242, 194, 210, 1, 17, 33, 49, 458, 459, 456, 457, 131, 147, 163, 179, 243, 227, 211, 195, 129, 145, 161, 177, 2, 18, 34, 50, 463, 462, 461, 460], #[0, 67, 65, 66, 324, 389, 243, 3, 328, 1, 394, 209, 332, 226, 2, 399, 388, 325, 19, 227, 83, 16, 82, 81, 242, 333, 398, 18, 17, 329, 193, 395, 392, 241, 330, 33, 34, 397, 334, 194, 97, 98, 32, 99, 211, 35, 326, 391, 396, 50, 210, 335, 225, 393, 49, 331, 51, 195, 390, 327, 114, 113, 115, 48], #[0, 260, 264, 268, 324, 1, 179, 66, 328, 67, 2, 145, 332, 162, 65, 3, 16, 261, 265, 269, 325, 17, 163, 82, 329, 83, 18, 129, 333, 178, 81, 19, 32, 262, 266, 270, 326, 33, 147, 98, 330, 99, 34, 177, 334, 130, 97, 35, 48, 263, 267, 271, 327, 49, 131, 114, 331, 115, 50, 161, 335, 146, 113, 51]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row0
