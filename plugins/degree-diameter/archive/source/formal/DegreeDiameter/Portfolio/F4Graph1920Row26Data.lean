import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row26
open F4Graph3840
def wordData : Array Nat := #[35, 12, 61, 42, 31, 38, 40, 24, 15, 39, 34, 0, 0, 53, 51, 9, 0, 0, 28, 0, 50, 22, 25, 13, 63, 37, 8, 2, 48, 23]
def inversePool : Array (Array Nat) := #[#[2, 3, 1, 1, 3, 2, 3, 1, 3], #[1, 0, 2, 0, 0, 1, 1, 1, 2], #[1, 3, 0, 3, 0, 0, 3, 0, 1], #[3, 2, 1, 0, 1, 1, 3, 3, 1], #[0, 0, 1, 0, 1, 3, 1, 0, 3], #[3, 1, 2, 0, 2, 2, 1, 2, 2], #[3, 2, 1, 2, 0, 2, 2, 0, 3], #[0, 1, 3, 0, 0, 1, 1, 2, 0], #[2, 0, 3, 0, 0, 2, 2, 1, 3], #[1, 2, 3, 0, 1, 1, 3, 1, 3], #[0, 2, 2, 1, 0, 1, 0, 3, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[3, 0, 2, 1, 0, 2, 0, 1, 0], #[1, 1, 0, 3, 2, 0, 0, 0, 1], #[2, 1, 0, 2, 2, 0, 3, 2, 1], #[3, 0, 2, 0, 0, 1, 1, 1, 2], #[0, 3, 1, 0, 2, 1, 1, 3, 1], #[1, 2, 0, 2, 2, 0, 2, 3, 1], #[0, 1, 3, 0, 0, 3, 1, 2, 1], #[0, 0, 1, 0, 2, 3, 1, 2, 1], #[2, 0, 1, 1, 0, 0, 3, 1, 2], #[2, 3, 0, 2, 1, 0, 0, 2, 1], #[1, 2, 3, 3, 3, 0, 0, 0, 1], #[3, 0, 0, 2, 0, 1, 1, 1, 1], #[2, 0, 1, 2, 0, 2, 1, 1, 3], #[2, 1, 0, 0, 2, 0, 2, 1, 1], #[0, 2, 2, 0, 3, 2, 1, 2, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 11, 11, 16, 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 243, 130, 65, 389, 227, 146, 81, 390, 211, 162, 97, 391, 195, 178, 113, 392, 66, 209, 131, 393, 82, 193, 147, 394, 98, 241, 163, 395, 114, 225, 179, 396, 129, 67, 226, 397, 145, 83, 242, 398, 161, 99, 194, 399, 177, 115, 210], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 129, 145, 161, 177, 3, 19, 35, 51, 226, 242, 194, 210, 392, 393, 394, 395, 243, 227, 211, 195, 130, 146, 162, 178, 1, 17, 33, 49, 396, 397, 398, 399, 2, 18, 34, 50, 209, 193, 241, 225, 131, 147, 163, 179], #[0, 260, 264, 268, 324, 3, 66, 209, 328, 226, 1, 67, 332, 65, 243, 2, 19, 325, 193, 82, 261, 16, 269, 265, 81, 333, 18, 227, 242, 329, 83, 17, 33, 99, 330, 194, 211, 34, 334, 97, 266, 270, 32, 262, 98, 241, 326, 35, 50, 195, 113, 335, 115, 49, 210, 331, 225, 114, 51, 327, 271, 267, 263, 48], #[0, 1, 2, 3, 324, 453, 65, 145, 328, 162, 458, 66, 332, 67, 179, 463, 16, 17, 18, 19, 325, 452, 81, 129, 329, 178, 459, 82, 333, 83, 163, 462, 32, 33, 34, 35, 326, 455, 97, 177, 330, 130, 456, 98, 334, 99, 147, 461, 48, 49, 50, 51, 327, 454, 113, 161, 331, 146, 457, 114, 335, 115, 131, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row26
