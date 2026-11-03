import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row14
open F4Graph3840
def wordData : Array Nat := #[32, 23, 13, 53, 61, 9, 2, 39, 12, 0, 54, 8, 37, 63, 48, 21, 24, 40, 35, 0, 26, 50, 0, 55, 60, 0, 38, 41, 34, 0]
def inversePool : Array (Array Nat) := #[#[2, 3, 1, 1, 3, 2, 2, 3, 0], #[0, 3, 1, 0, 1, 1, 1, 3, 1], #[2, 0, 2, 2, 0, 3, 0, 1, 0], #[3, 2, 0, 0, 1, 0, 1, 3, 1], #[1, 2, 0, 1, 0, 0, 1, 0, 1], #[1, 0, 3, 2, 0, 3, 2, 1, 3], #[3, 0, 3, 2, 0, 1, 2, 1, 2], #[1, 3, 2, 1, 2, 3, 3, 2, 0], #[1, 0, 2, 2, 0, 1, 0, 1, 0], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[1, 3, 0, 1, 0, 0, 1, 3, 1], #[3, 0, 3, 2, 0, 1, 3, 1, 0], #[3, 1, 2, 2, 1, 3, 1, 2, 2], #[3, 1, 0, 0, 3, 0, 3, 2, 1], #[1, 3, 0, 0, 3, 0, 1, 3, 1], #[0, 1, 3, 0, 3, 1, 1, 3, 2], #[0, 2, 1, 0, 2, 3, 1, 0, 2], #[3, 2, 1, 0, 1, 1, 0, 1, 0], #[1, 0, 1, 2, 1, 3, 1, 0, 0], #[0, 1, 0, 0, 3, 1, 1, 2, 1], #[3, 1, 0, 0, 1, 0, 3, 1, 1], #[0, 0, 1, 1, 0, 2, 0, 1, 3], #[2, 1, 0, 1, 0, 0, 1, 3, 1], #[3, 1, 0, 2, 1, 0, 2, 1, 1], #[0, 2, 2, 1, 0, 1, 0, 2, 3], #[3, 2, 1, 3, 3, 0, 3, 3, 1], #[1, 3, 2, 0, 2, 2, 1, 3, 3]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 9, 19, 20, 21, 22, 23, 9, 24, 25, 26, 9]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 226, 129, 67, 389, 242, 145, 83, 390, 194, 161, 99, 391, 210, 177, 115, 392, 65, 243, 130, 393, 81, 227, 146, 394, 97, 211, 162, 395, 113, 195, 178, 396, 131, 66, 209, 397, 147, 82, 193, 398, 163, 98, 241, 399, 179, 114, 225], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 1, 17, 33, 49, 243, 227, 211, 195, 130, 146, 162, 178, 392, 393, 394, 395, 131, 147, 163, 179, 2, 18, 34, 50, 209, 193, 241, 225, 396, 397, 398, 399, 226, 242, 194, 210, 129, 145, 161, 177, 3, 19, 35, 51], #[0, 65, 66, 67, 324, 389, 1, 209, 328, 226, 394, 2, 332, 3, 243, 399, 388, 325, 193, 17, 81, 16, 83, 82, 19, 333, 398, 227, 242, 329, 18, 395, 392, 34, 330, 194, 211, 397, 334, 35, 98, 99, 32, 97, 33, 241, 326, 391, 396, 195, 51, 335, 50, 393, 210, 331, 225, 49, 390, 327, 115, 114, 113, 48], #[0, 162, 179, 145, 324, 453, 2, 66, 328, 67, 458, 3, 332, 1, 65, 463, 16, 178, 163, 129, 325, 452, 18, 82, 329, 83, 459, 19, 333, 17, 81, 462, 32, 130, 147, 177, 326, 455, 34, 98, 330, 99, 456, 35, 334, 33, 97, 461, 48, 146, 131, 161, 327, 454, 50, 114, 331, 115, 457, 51, 335, 49, 113, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row14
