import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row8
open F4Graph3840
def wordData : Array Nat := #[26, 48, 10, 63, 0, 32, 8, 54, 53, 24, 0, 23, 0, 22, 25, 12, 60, 0, 37, 34, 61, 0, 51, 35, 50, 21, 41, 13, 40, 42]
def inversePool : Array (Array Nat) := #[#[0, 0, 1, 0, 1, 2, 1, 1, 0], #[2, 3, 0, 0, 3, 0, 3, 1, 1], #[1, 0, 3, 3, 0, 0, 3, 1, 0], #[1, 0, 0, 3, 2, 0, 2, 2, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 3, 0, 1, 2, 3, 1, 1, 1], #[2, 0, 1, 3, 0, 3, 0, 1, 1], #[3, 2, 0, 1, 2, 0, 3, 2, 1], #[2, 3, 0, 1, 0, 0, 2, 3, 1], #[0, 3, 2, 0, 0, 1, 1, 3, 3], #[0, 3, 1, 0, 0, 1, 1, 1, 2], #[0, 3, 3, 0, 2, 1, 1, 0, 0], #[0, 3, 3, 0, 2, 1, 1, 3, 0], #[1, 0, 2, 0, 0, 1, 0, 1, 0], #[0, 2, 0, 2, 1, 0, 2, 1, 1], #[3, 0, 2, 3, 0, 1, 3, 1, 2], #[1, 3, 2, 1, 0, 1, 1, 3, 3], #[1, 0, 1, 3, 1, 2, 3, 0, 2], #[0, 1, 0, 1, 2, 0, 1, 2, 1], #[3, 1, 0, 1, 3, 0, 0, 0, 1], #[3, 1, 2, 3, 3, 0, 0, 0, 1], #[1, 3, 0, 3, 1, 0, 3, 2, 1], #[0, 2, 1, 0, 3, 1, 1, 3, 2], #[2, 1, 3, 3, 3, 0, 3, 3, 1], #[0, 0, 3, 3, 0, 2, 0, 1, 0], #[3, 1, 2, 2, 0, 2, 2, 0, 3], #[2, 3, 1, 0, 3, 3, 2, 0, 3]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 10, 4, 11, 12, 13, 14, 15, 16, 17, 18, 4, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 226, 129, 67, 389, 242, 145, 83, 390, 194, 161, 99, 391, 210, 177, 115, 392, 65, 243, 130, 393, 81, 227, 146, 394, 97, 211, 162, 395, 113, 195, 178, 396, 131, 66, 209, 397, 147, 82, 193, 398, 163, 98, 241, 399, 179, 114, 225], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 226, 242, 194, 210, 129, 145, 161, 177, 3, 19, 35, 51, 392, 393, 394, 395, 1, 17, 33, 49, 243, 227, 211, 195, 130, 146, 162, 178, 396, 397, 398, 399, 131, 147, 163, 179, 2, 18, 34, 50, 209, 193, 241, 225], #[0, 260, 264, 268, 226, 389, 67, 1, 243, 2, 394, 65, 209, 66, 3, 399, 388, 242, 17, 83, 261, 16, 269, 265, 82, 193, 398, 19, 18, 227, 81, 395, 392, 97, 211, 34, 35, 397, 241, 98, 266, 270, 32, 262, 99, 33, 194, 391, 396, 51, 114, 225, 113, 393, 50, 195, 49, 115, 390, 210, 271, 267, 263, 48], #[0, 67, 65, 66, 324, 453, 179, 3, 328, 1, 458, 145, 332, 162, 2, 463, 16, 83, 81, 82, 325, 452, 163, 19, 329, 17, 459, 129, 333, 178, 18, 462, 32, 99, 97, 98, 326, 455, 147, 35, 330, 33, 456, 177, 334, 130, 34, 461, 48, 115, 113, 114, 327, 454, 131, 51, 331, 49, 457, 161, 335, 146, 50, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row8
