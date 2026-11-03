import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row9
open F4Graph3840
def wordData : Array Nat := #[0, 10, 2, 12, 29, 23, 60, 63, 28, 37, 51, 42, 24, 31, 0, 0, 25, 41, 26, 0, 8, 32, 0, 40, 61, 53, 35, 54, 22, 21]
def inversePool : Array (Array Nat) := #[#[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 0, 2, 3, 0, 3, 2, 1, 0], #[1, 0, 2, 0, 0, 3, 3, 1, 1], #[1, 0, 0, 2, 0, 1, 2, 1, 0], #[0, 0, 1, 0, 1, 2, 1, 0, 2], #[0, 3, 1, 0, 1, 1, 1, 1, 2], #[1, 2, 0, 3, 3, 0, 3, 3, 1], #[3, 0, 0, 0, 2, 0, 3, 2, 1], #[0, 3, 1, 0, 2, 1, 1, 3, 1], #[2, 3, 1, 0, 1, 1, 2, 3, 0], #[2, 0, 0, 0, 1, 0, 2, 0, 1], #[1, 0, 1, 1, 1, 0, 0, 1, 0], #[0, 2, 1, 0, 2, 0, 1, 3, 3], #[0, 2, 3, 0, 1, 0, 1, 0, 0], #[0, 0, 3, 1, 0, 2, 0, 1, 1], #[0, 3, 2, 0, 2, 3, 1, 2, 3], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[0, 2, 0, 0, 0, 1, 1, 1, 1], #[2, 0, 1, 1, 0, 2, 2, 1, 0], #[3, 0, 3, 2, 1, 3, 1, 0, 0], #[2, 1, 3, 2, 0, 2, 2, 0, 3], #[1, 2, 0, 3, 3, 0, 1, 2, 1], #[3, 1, 2, 0, 1, 1, 3, 1, 3], #[3, 2, 0, 0, 3, 0, 3, 2, 1], #[0, 1, 0, 0, 3, 1, 1, 0, 0], #[0, 1, 1, 0, 3, 2, 1, 3, 3]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15, 16, 17, 0, 18, 19, 0, 20, 6, 21, 22, 23, 24, 25]
def adjacentData : Array (Array Nat) := #[#[0, 65, 66, 67, 1, 81, 82, 83, 2, 97, 98, 99, 3, 113, 114, 115, 388, 453, 129, 209, 389, 452, 145, 193, 390, 455, 161, 241, 391, 454, 177, 225, 392, 226, 458, 130, 393, 242, 459, 146, 394, 194, 456, 162, 395, 210, 457, 178, 396, 131, 243, 463, 397, 147, 227, 462, 398, 163, 211, 461, 399, 179, 195, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 131, 147, 163, 179, 2, 18, 34, 50, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 129, 145, 161, 177, 3, 19, 35, 51, 396, 397, 398, 399, 1, 17, 33, 49, 243, 227, 211, 195, 130, 146, 162, 178], #[0, 209, 226, 243, 324, 389, 65, 1, 328, 2, 394, 66, 332, 67, 3, 399, 388, 325, 17, 81, 193, 16, 227, 242, 83, 333, 398, 19, 18, 329, 82, 395, 392, 98, 330, 34, 35, 397, 334, 99, 194, 211, 32, 241, 97, 33, 326, 391, 396, 51, 115, 335, 114, 393, 50, 331, 49, 113, 390, 327, 195, 210, 225, 48], #[0, 260, 264, 268, 1, 453, 162, 67, 2, 65, 458, 179, 3, 145, 66, 463, 16, 261, 265, 269, 17, 452, 178, 83, 18, 81, 459, 163, 19, 129, 82, 462, 32, 262, 266, 270, 33, 455, 130, 99, 34, 97, 456, 147, 35, 177, 98, 461, 48, 263, 267, 271, 49, 454, 146, 115, 50, 113, 457, 131, 51, 161, 114, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row9
