import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row18
open F4Graph3840
def wordData : Array Nat := #[0, 9, 0, 32, 0, 10, 26, 55, 3, 60, 31, 41, 38, 23, 39, 22, 40, 48, 12, 29, 28, 15, 13, 8, 37, 50, 24, 53, 21, 0]
def inversePool : Array (Array Nat) := #[#[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 0, 2, 0, 0, 1, 3, 1, 3], #[3, 3, 0, 1, 2, 3, 0, 0, 1], #[3, 0, 2, 1, 0, 1, 0, 1, 2], #[0, 2, 1, 0, 2, 0, 1, 2, 0], #[2, 1, 0, 0, 1, 0, 1, 3, 1], #[1, 0, 3, 1, 0, 2, 1, 1, 3], #[2, 3, 0, 2, 0, 0, 2, 0, 1], #[0, 1, 2, 0, 0, 1, 1, 1, 2], #[2, 0, 2, 1, 1, 0, 1, 1, 1], #[1, 2, 3, 3, 3, 0, 3, 1, 3], #[0, 1, 1, 0, 1, 2, 1, 1, 1], #[3, 3, 0, 1, 2, 3, 2, 2, 1], #[0, 3, 2, 0, 0, 3, 1, 1, 3], #[2, 3, 1, 0, 2, 2, 0, 2, 3], #[3, 3, 0, 1, 2, 0, 0, 0, 1], #[2, 0, 1, 1, 0, 1, 1, 1, 3], #[0, 3, 3, 0, 1, 2, 1, 3, 3], #[0, 1, 2, 0, 2, 1, 1, 2, 3], #[3, 0, 1, 2, 0, 2, 2, 1, 3], #[1, 0, 2, 0, 0, 1, 1, 1, 2], #[1, 0, 2, 1, 0, 0, 0, 1, 2], #[1, 1, 0, 3, 2, 1, 2, 2, 1], #[2, 1, 0, 0, 2, 0, 0, 0, 1], #[0, 2, 2, 0, 1, 3, 1, 0, 2], #[1, 3, 0, 2, 2, 0, 2, 1, 1], #[0, 3, 0, 0, 2, 1, 1, 3, 0]]
def inverseIndex : Array Nat := #[0, 1, 0, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 0]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 129, 67, 226, 389, 145, 83, 242, 390, 161, 99, 194, 391, 177, 115, 210, 392, 243, 130, 65, 393, 227, 146, 81, 394, 211, 162, 97, 395, 195, 178, 113, 396, 66, 209, 131, 397, 82, 193, 147, 398, 98, 241, 163, 399, 114, 225, 179], #[0, 16, 32, 48, 209, 193, 241, 225, 226, 242, 194, 210, 243, 227, 211, 195, 388, 389, 390, 391, 453, 452, 455, 454, 129, 145, 161, 177, 1, 17, 33, 49, 392, 393, 394, 395, 2, 18, 34, 50, 458, 459, 456, 457, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 3, 19, 35, 51, 463, 462, 461, 460], #[0, 67, 65, 66, 324, 389, 243, 3, 328, 1, 394, 209, 332, 226, 2, 399, 388, 325, 19, 227, 83, 16, 82, 81, 242, 333, 398, 18, 17, 329, 193, 395, 392, 241, 330, 33, 34, 397, 334, 194, 97, 98, 32, 99, 211, 35, 326, 391, 396, 50, 210, 335, 225, 393, 49, 331, 51, 195, 390, 327, 114, 113, 115, 48], #[0, 260, 264, 268, 65, 453, 162, 3, 66, 1, 458, 179, 67, 145, 2, 463, 16, 261, 265, 269, 81, 452, 178, 19, 82, 17, 459, 163, 83, 129, 18, 462, 32, 262, 266, 270, 97, 455, 130, 35, 98, 33, 456, 147, 99, 177, 34, 461, 48, 263, 267, 271, 113, 454, 146, 51, 114, 49, 457, 131, 115, 161, 50, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row18
