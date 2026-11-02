import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row22
open F4Graph3840
def wordData : Array Nat := #[2, 51, 41, 8, 39, 54, 0, 28, 38, 0, 53, 60, 10, 42, 21, 15, 63, 3, 9, 13, 25, 0, 40, 22, 34, 61, 12, 32, 0, 48]
def inversePool : Array (Array Nat) := #[#[2, 0, 3, 3, 0, 2, 1, 1, 2], #[1, 2, 0, 2, 0, 0, 1, 2, 1], #[2, 3, 1, 1, 1, 0, 1, 1, 1], #[3, 0, 1, 2, 0, 1, 2, 1, 1], #[3, 2, 1, 1, 2, 3, 2, 1, 2], #[2, 2, 0, 1, 2, 0, 2, 2, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 3, 1, 0, 0, 1, 1, 2, 3], #[3, 0, 3, 2, 2, 0, 3, 0, 2], #[1, 3, 0, 2, 2, 0, 3, 2, 1], #[1, 3, 0, 2, 0, 0, 2, 0, 1], #[2, 0, 0, 1, 0, 2, 2, 1, 2], #[2, 1, 3, 2, 0, 2, 0, 1, 0], #[0, 3, 2, 0, 1, 2, 1, 3, 2], #[2, 0, 3, 2, 0, 2, 2, 1, 3], #[0, 1, 0, 2, 1, 0, 2, 0, 1], #[1, 0, 3, 3, 0, 1, 0, 1, 0], #[2, 0, 3, 1, 0, 1, 0, 1, 3], #[3, 0, 1, 1, 0, 3, 0, 1, 0], #[0, 2, 0, 0, 2, 1, 1, 0, 1], #[1, 3, 2, 1, 2, 3, 1, 2, 2], #[0, 1, 2, 0, 2, 1, 1, 3, 1], #[1, 3, 2, 0, 2, 2, 1, 3, 3], #[0, 2, 0, 2, 1, 0, 2, 1, 1], #[1, 0, 2, 2, 0, 1, 2, 1, 3], #[3, 3, 0, 1, 2, 3, 0, 0, 1], #[0, 3, 0, 3, 2, 0, 0, 0, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 6, 20, 21, 22, 23, 24, 25, 6, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 67, 130, 209, 389, 83, 146, 193, 390, 99, 162, 241, 391, 115, 178, 225, 392, 226, 65, 131, 393, 242, 81, 147, 394, 194, 97, 163, 395, 210, 113, 179, 396, 129, 243, 66, 397, 145, 227, 82, 398, 161, 211, 98, 399, 177, 195, 114], #[0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 388, 389, 390, 391, 453, 452, 455, 454, 129, 145, 161, 177, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 1, 243, 66, 328, 67, 2, 209, 332, 226, 65, 3, 17, 325, 82, 227, 261, 16, 269, 265, 242, 333, 19, 81, 83, 329, 193, 18, 34, 241, 330, 99, 97, 35, 334, 194, 266, 270, 32, 262, 211, 98, 326, 33, 51, 113, 210, 335, 225, 50, 115, 331, 114, 195, 49, 327, 271, 267, 263, 48], #[0, 1, 2, 3, 324, 453, 65, 145, 328, 162, 458, 66, 332, 67, 179, 463, 16, 17, 18, 19, 325, 452, 81, 129, 329, 178, 459, 82, 333, 83, 163, 462, 32, 33, 34, 35, 326, 455, 97, 177, 330, 130, 456, 98, 334, 99, 147, 461, 48, 49, 50, 51, 327, 454, 113, 161, 331, 146, 457, 114, 335, 115, 131, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row22
