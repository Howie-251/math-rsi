import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row15
open F4Graph3840
def wordData : Array Nat := #[10, 60, 15, 9, 63, 0, 0, 29, 40, 21, 38, 61, 39, 50, 0, 32, 2, 12, 48, 3, 54, 28, 41, 24, 42, 34, 13, 0, 8, 0]
def inversePool : Array (Array Nat) := #[#[3, 0, 2, 1, 0, 1, 0, 1, 2], #[2, 0, 0, 0, 2, 0, 0, 2, 1], #[1, 0, 1, 3, 0, 2, 3, 1, 3], #[2, 0, 3, 2, 0, 1, 0, 1, 2], #[2, 3, 0, 2, 1, 0, 0, 2, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 1, 2, 0, 0, 1, 1, 3, 1], #[3, 2, 1, 0, 1, 1, 0, 1, 0], #[0, 0, 2, 0, 1, 2, 1, 0, 2], #[2, 3, 1, 2, 2, 0, 2, 3, 0], #[3, 2, 0, 3, 3, 0, 3, 3, 1], #[2, 3, 1, 2, 1, 3, 2, 3, 0], #[2, 1, 0, 1, 1, 0, 2, 1, 1], #[3, 0, 2, 1, 0, 2, 3, 1, 2], #[1, 2, 3, 2, 0, 2, 2, 3, 0], #[0, 0, 1, 1, 0, 3, 0, 1, 3], #[2, 0, 3, 1, 0, 3, 1, 1, 2], #[2, 3, 0, 1, 1, 0, 3, 1, 1], #[1, 0, 3, 3, 0, 1, 2, 1, 1], #[3, 2, 0, 1, 2, 0, 3, 2, 1], #[0, 2, 0, 0, 2, 1, 1, 3, 0], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[0, 1, 3, 0, 1, 2, 1, 2, 0], #[1, 2, 3, 1, 1, 0, 0, 3, 2], #[1, 1, 0, 0, 3, 3, 1, 1, 1], #[1, 0, 2, 2, 0, 1, 1, 1, 2], #[1, 0, 2, 3, 0, 2, 1, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 26, 5]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 129, 67, 226, 389, 145, 83, 242, 390, 161, 99, 194, 391, 177, 115, 210, 392, 243, 130, 65, 393, 227, 146, 81, 394, 211, 162, 97, 395, 195, 178, 113, 396, 66, 209, 131, 397, 82, 193, 147, 398, 98, 241, 163, 399, 114, 225, 179], #[0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 388, 389, 390, 391, 453, 452, 455, 454, 129, 145, 161, 177, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 67, 2, 209, 328, 226, 65, 3, 332, 1, 243, 66, 83, 325, 193, 18, 261, 16, 269, 265, 17, 333, 82, 227, 242, 329, 19, 81, 97, 35, 330, 194, 211, 98, 334, 33, 266, 270, 32, 262, 34, 241, 326, 99, 114, 195, 49, 335, 51, 113, 210, 331, 225, 50, 115, 327, 271, 267, 263, 48], #[0, 67, 65, 66, 324, 453, 179, 3, 328, 1, 458, 145, 332, 162, 2, 463, 16, 83, 81, 82, 325, 452, 163, 19, 329, 17, 459, 129, 333, 178, 18, 462, 32, 99, 97, 98, 326, 455, 147, 35, 330, 33, 456, 177, 334, 130, 34, 461, 48, 115, 113, 114, 327, 454, 131, 51, 331, 49, 457, 161, 335, 146, 50, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row15
