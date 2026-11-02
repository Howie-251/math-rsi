import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row17
open F4Graph3840
def wordData : Array Nat := #[12, 0, 29, 0, 24, 42, 53, 0, 21, 15, 63, 38, 41, 13, 31, 48, 35, 61, 22, 40, 32, 26, 37, 50, 0, 2, 0, 60, 28, 9]
def inversePool : Array (Array Nat) := #[#[1, 0, 1, 2, 0, 3, 2, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 2, 3, 0, 0, 1, 1, 2, 3], #[0, 1, 3, 0, 1, 2, 1, 1, 2], #[1, 3, 2, 1, 2, 3, 0, 1, 0], #[3, 2, 0, 0, 3, 0, 1, 3, 1], #[2, 0, 2, 1, 0, 2, 2, 1, 2], #[0, 1, 3, 0, 1, 2, 1, 1, 3], #[1, 0, 2, 2, 0, 0, 3, 1, 1], #[2, 3, 0, 2, 1, 0, 0, 2, 1], #[3, 2, 1, 0, 3, 3, 3, 2, 0], #[0, 1, 1, 2, 0, 2, 2, 0, 3], #[3, 0, 1, 2, 0, 1, 2, 1, 3], #[0, 2, 3, 0, 0, 2, 1, 2, 3], #[2, 3, 0, 0, 3, 0, 3, 1, 1], #[2, 1, 3, 1, 0, 1, 1, 3, 3], #[1, 3, 0, 0, 1, 0, 0, 1, 1], #[0, 2, 1, 0, 1, 0, 1, 1, 3], #[3, 1, 2, 2, 1, 3, 2, 1, 2], #[1, 2, 3, 2, 0, 2, 2, 3, 0], #[0, 1, 2, 0, 3, 3, 1, 3, 3], #[0, 1, 1, 1, 2, 3, 0, 2, 3], #[0, 3, 0, 3, 2, 0, 0, 3, 1], #[2, 0, 3, 0, 0, 2, 0, 1, 0], #[1, 2, 0, 2, 0, 0, 2, 0, 1], #[0, 1, 3, 0, 1, 0, 1, 1, 3], #[2, 0, 0, 2, 0, 1, 0, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 23, 1, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 131, 129, 130, 1, 147, 145, 146, 2, 163, 161, 162, 3, 179, 177, 178, 388, 453, 243, 67, 389, 452, 227, 83, 390, 455, 211, 99, 391, 454, 195, 115, 392, 65, 458, 209, 393, 81, 459, 193, 394, 97, 456, 241, 395, 113, 457, 225, 396, 226, 66, 463, 397, 242, 82, 462, 398, 194, 98, 461, 399, 210, 114, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 243, 227, 211, 195, 130, 146, 162, 178, 1, 17, 33, 49, 392, 393, 394, 395, 2, 18, 34, 50, 209, 193, 241, 225, 131, 147, 163, 179, 396, 397, 398, 399, 129, 145, 161, 177, 3, 19, 35, 51, 226, 242, 194, 210], #[0, 260, 264, 268, 226, 389, 67, 1, 243, 2, 394, 65, 209, 66, 3, 399, 388, 242, 17, 83, 261, 16, 269, 265, 82, 193, 398, 19, 18, 227, 81, 395, 392, 97, 211, 34, 35, 397, 241, 98, 266, 270, 32, 262, 99, 33, 194, 391, 396, 51, 114, 225, 113, 393, 50, 195, 49, 115, 390, 210, 271, 267, 263, 48], #[0, 162, 179, 145, 324, 453, 2, 66, 328, 67, 458, 3, 332, 1, 65, 463, 16, 178, 163, 129, 325, 452, 18, 82, 329, 83, 459, 19, 333, 17, 81, 462, 32, 130, 147, 177, 326, 455, 34, 98, 330, 99, 456, 35, 334, 33, 97, 461, 48, 146, 131, 161, 327, 454, 50, 114, 331, 115, 457, 51, 335, 49, 113, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row17
