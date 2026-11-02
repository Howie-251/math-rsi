import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row12
open F4Graph3840
def wordData : Array Nat := #[0, 63, 53, 2, 22, 0, 12, 41, 0, 28, 10, 24, 8, 40, 3, 35, 37, 15, 42, 38, 13, 60, 61, 0, 32, 9, 21, 48, 0, 55]
def inversePool : Array (Array Nat) := #[#[2, 0, 3, 1, 0, 1, 3, 1, 1], #[3, 0, 0, 2, 2, 0, 1, 2, 1], #[3, 1, 0, 2, 0, 0, 3, 1, 1], #[3, 0, 2, 2, 0, 2, 2, 1, 1], #[0, 2, 3, 0, 2, 2, 1, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[1, 0, 2, 3, 0, 3, 2, 1, 3], #[0, 2, 2, 1, 2, 3, 1, 2, 2], #[0, 3, 1, 0, 0, 1, 1, 3, 1], #[1, 0, 2, 0, 0, 2, 1, 1, 0], #[0, 1, 3, 0, 1, 2, 1, 2, 0], #[3, 0, 0, 3, 0, 2, 0, 1, 2], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[2, 0, 1, 1, 0, 2, 2, 1, 1], #[1, 2, 3, 2, 0, 2, 3, 1, 3], #[3, 0, 3, 2, 1, 3, 3, 0, 2], #[1, 0, 2, 0, 0, 1, 0, 1, 0], #[1, 2, 3, 0, 2, 2, 1, 0, 0], #[3, 2, 1, 2, 2, 0, 2, 1, 2], #[0, 0, 2, 1, 0, 2, 0, 1, 2], #[2, 1, 0, 2, 0, 0, 2, 0, 1], #[0, 3, 0, 1, 1, 0, 1, 1, 1], #[2, 1, 3, 1, 1, 0, 2, 1, 2], #[0, 0, 3, 2, 0, 3, 2, 1, 3], #[0, 1, 3, 0, 3, 1, 1, 2, 1], #[0, 1, 0, 3, 3, 0, 0, 1, 1], #[2, 1, 0, 1, 0, 0, 1, 3, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 5, 22, 23, 24, 25, 5, 26]
def adjacentData : Array (Array Nat) := #[#[0, 131, 129, 130, 1, 147, 145, 146, 2, 163, 161, 162, 3, 179, 177, 178, 388, 453, 243, 67, 389, 452, 227, 83, 390, 455, 211, 99, 391, 454, 195, 115, 392, 65, 458, 209, 393, 81, 459, 193, 394, 97, 456, 241, 395, 113, 457, 225, 396, 226, 66, 463, 397, 242, 82, 462, 398, 194, 98, 461, 399, 210, 114, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 131, 147, 163, 179, 2, 18, 34, 50, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 129, 145, 161, 177, 3, 19, 35, 51, 396, 397, 398, 399, 1, 17, 33, 49, 243, 227, 211, 195, 130, 146, 162, 178], #[0, 260, 264, 268, 2, 389, 67, 209, 3, 226, 394, 65, 1, 66, 243, 399, 388, 18, 193, 83, 261, 16, 269, 265, 82, 17, 398, 227, 242, 19, 81, 395, 392, 97, 35, 194, 211, 397, 33, 98, 266, 270, 32, 262, 99, 241, 34, 391, 396, 195, 114, 49, 113, 393, 210, 51, 225, 115, 390, 50, 271, 267, 263, 48], #[0, 260, 264, 268, 324, 3, 66, 145, 328, 162, 1, 67, 332, 65, 179, 2, 16, 261, 265, 269, 325, 19, 82, 129, 329, 178, 17, 83, 333, 81, 163, 18, 32, 262, 266, 270, 326, 35, 98, 177, 330, 130, 33, 99, 334, 97, 147, 34, 48, 263, 267, 271, 327, 51, 114, 161, 331, 146, 49, 115, 335, 113, 131, 50]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row12
