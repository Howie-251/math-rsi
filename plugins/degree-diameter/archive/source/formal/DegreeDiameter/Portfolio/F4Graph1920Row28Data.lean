import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row28
open F4Graph3840
def wordData : Array Nat := #[39, 26, 32, 15, 41, 50, 63, 42, 31, 48, 40, 21, 0, 37, 55, 60, 38, 24, 0, 23, 0, 9, 0, 0, 28, 10, 22, 8, 53, 13]
def inversePool : Array (Array Nat) := #[#[3, 2, 1, 1, 2, 3, 3, 2, 0], #[0, 1, 3, 0, 3, 0, 1, 3, 0], #[0, 1, 1, 3, 2, 1, 0, 2, 3], #[1, 0, 0, 3, 0, 1, 3, 1, 0], #[3, 0, 3, 1, 2, 3, 1, 2, 2], #[2, 3, 0, 0, 2, 0, 1, 2, 1], #[2, 3, 0, 2, 1, 0, 0, 2, 1], #[0, 3, 3, 1, 3, 2, 1, 0, 0], #[0, 2, 3, 0, 0, 2, 1, 2, 3], #[3, 2, 0, 0, 2, 0, 1, 3, 1], #[1, 3, 2, 2, 0, 2, 2, 0, 3], #[0, 2, 3, 0, 0, 1, 1, 2, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 0, 2, 1, 2, 3, 1, 0, 0], #[2, 0, 0, 0, 1, 0, 2, 0, 1], #[1, 0, 0, 3, 2, 0, 3, 2, 1], #[2, 0, 2, 0, 1, 1, 2, 0, 3], #[0, 2, 1, 0, 2, 0, 1, 3, 3], #[3, 0, 3, 3, 0, 2, 2, 1, 2], #[0, 1, 2, 0, 3, 3, 1, 2, 3], #[3, 0, 3, 1, 0, 3, 1, 1, 3], #[0, 3, 1, 0, 2, 0, 1, 0, 0], #[0, 0, 2, 2, 0, 1, 2, 1, 2], #[0, 1, 3, 0, 2, 2, 1, 3, 2], #[1, 0, 2, 3, 0, 2, 1, 1, 1], #[1, 2, 0, 1, 0, 0, 3, 1, 1], #[2, 0, 3, 2, 0, 1, 3, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 12, 20, 12, 12, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 129, 130, 131, 1, 145, 146, 147, 2, 161, 162, 163, 3, 177, 178, 179, 388, 453, 65, 209, 389, 452, 81, 193, 390, 455, 97, 241, 391, 454, 113, 225, 392, 226, 458, 66, 393, 242, 459, 82, 394, 194, 456, 98, 395, 210, 457, 114, 396, 67, 243, 463, 397, 83, 227, 462, 398, 99, 211, 461, 399, 115, 195, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 2, 18, 34, 50, 453, 452, 455, 454, 131, 147, 163, 179, 209, 193, 241, 225, 3, 19, 35, 51, 226, 242, 194, 210, 458, 459, 456, 457, 129, 145, 161, 177, 1, 17, 33, 49, 130, 146, 162, 178, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 324, 3, 66, 209, 328, 226, 1, 67, 332, 65, 243, 2, 19, 325, 193, 82, 261, 16, 269, 265, 81, 333, 18, 227, 242, 329, 83, 17, 33, 99, 330, 194, 211, 34, 334, 97, 266, 270, 32, 262, 98, 241, 326, 35, 50, 195, 113, 335, 115, 49, 210, 331, 225, 114, 51, 327, 271, 267, 263, 48], #[0, 145, 162, 179, 324, 453, 65, 1, 328, 2, 458, 66, 332, 67, 3, 463, 16, 129, 178, 163, 325, 452, 81, 17, 329, 18, 459, 82, 333, 83, 19, 462, 32, 177, 130, 147, 326, 455, 97, 33, 330, 34, 456, 98, 334, 99, 35, 461, 48, 161, 146, 131, 327, 454, 113, 49, 331, 50, 457, 114, 335, 115, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row28
