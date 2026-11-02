import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row23
open F4Graph3840
def wordData : Array Nat := #[61, 13, 22, 60, 40, 55, 41, 50, 39, 31, 24, 0, 0, 0, 34, 28, 21, 37, 29, 53, 0, 8, 48, 32, 35, 42, 9, 26, 0, 12]
def inversePool : Array (Array Nat) := #[#[3, 2, 0, 3, 3, 0, 3, 3, 1], #[3, 0, 1, 0, 0, 1, 2, 1, 3], #[0, 0, 2, 0, 1, 0, 1, 0, 3], #[1, 0, 0, 0, 2, 0, 0, 2, 1], #[2, 0, 2, 0, 2, 2, 0, 2, 3], #[3, 3, 0, 0, 3, 0, 1, 1, 1], #[2, 1, 3, 1, 2, 3, 1, 2, 2], #[2, 3, 0, 1, 1, 0, 0, 0, 1], #[3, 0, 3, 1, 2, 3, 1, 0, 0], #[0, 1, 2, 0, 1, 3, 1, 0, 0], #[0, 3, 3, 0, 1, 3, 1, 0, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 3, 1, 1, 0, 1, 0, 0, 1], #[0, 3, 1, 0, 2, 1, 1, 2, 3], #[0, 1, 2, 0, 1, 1, 1, 1, 2], #[3, 3, 0, 1, 2, 3, 1, 1, 1], #[0, 1, 2, 0, 2, 1, 1, 2, 3], #[0, 2, 0, 1, 1, 0, 0, 3, 1], #[3, 0, 1, 0, 0, 1, 3, 1, 1], #[1, 0, 1, 1, 0, 3, 2, 1, 0], #[2, 3, 0, 2, 2, 0, 3, 1, 1], #[1, 2, 3, 3, 3, 0, 2, 3, 0], #[3, 2, 1, 1, 1, 0, 0, 0, 1], #[2, 1, 3, 3, 3, 0, 1, 2, 2], #[1, 0, 0, 2, 0, 1, 2, 1, 1], #[0, 0, 2, 0, 2, 1, 1, 2, 3], #[1, 0, 2, 2, 0, 1, 1, 1, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 11, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 226, 453, 131, 65, 242, 452, 147, 81, 194, 455, 163, 97, 210, 454, 179, 113, 243, 66, 458, 129, 227, 82, 459, 145, 211, 98, 456, 161, 195, 114, 457, 177, 209, 130, 67, 463, 193, 146, 83, 462, 241, 162, 99, 461, 225, 178, 115, 460], #[0, 16, 32, 48, 129, 145, 161, 177, 130, 146, 162, 178, 131, 147, 163, 179, 388, 389, 390, 391, 453, 452, 455, 454, 1, 17, 33, 49, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 2, 18, 34, 50, 396, 397, 398, 399, 3, 19, 35, 51, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 2, 389, 67, 209, 3, 226, 394, 65, 1, 66, 243, 399, 388, 18, 193, 83, 261, 16, 269, 265, 82, 17, 398, 227, 242, 19, 81, 395, 392, 97, 35, 194, 211, 397, 33, 98, 266, 270, 32, 262, 99, 241, 34, 391, 396, 195, 114, 49, 113, 393, 210, 51, 225, 115, 390, 50, 271, 267, 263, 48], #[0, 162, 179, 145, 324, 453, 2, 66, 328, 67, 458, 3, 332, 1, 65, 463, 16, 178, 163, 129, 325, 452, 18, 82, 329, 83, 459, 19, 333, 17, 81, 462, 32, 130, 147, 177, 326, 455, 34, 98, 330, 99, 456, 35, 334, 33, 97, 461, 48, 146, 131, 161, 327, 454, 50, 114, 331, 115, 457, 51, 335, 49, 113, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row23
