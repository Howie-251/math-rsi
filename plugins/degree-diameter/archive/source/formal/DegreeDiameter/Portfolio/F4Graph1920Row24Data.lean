import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row24
open F4Graph3840
def wordData : Array Nat := #[8, 53, 25, 41, 34, 12, 28, 15, 54, 10, 0, 13, 23, 9, 26, 63, 0, 0, 38, 61, 0, 21, 55, 39, 40, 32, 42, 0, 24, 60]
def inversePool : Array (Array Nat) := #[#[2, 0, 1, 2, 0, 3, 3, 1, 0], #[2, 1, 0, 3, 3, 0, 2, 1, 1], #[0, 2, 1, 0, 0, 1, 1, 2, 0], #[1, 3, 2, 0, 1, 1, 0, 1, 0], #[3, 1, 2, 0, 3, 3, 1, 2, 2], #[3, 0, 3, 2, 0, 3, 2, 1, 2], #[0, 2, 3, 0, 0, 1, 1, 3, 1], #[3, 0, 1, 0, 0, 2, 2, 1, 3], #[3, 1, 0, 3, 3, 0, 3, 1, 1], #[3, 0, 0, 0, 0, 2, 0, 1, 2], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 0, 3, 2, 0, 1, 2, 1, 3], #[0, 1, 0, 0, 1, 2, 1, 1, 0], #[1, 0, 0, 2, 0, 1, 1, 1, 1], #[0, 3, 3, 0, 1, 2, 1, 0, 3], #[2, 0, 0, 2, 2, 0, 0, 2, 1], #[0, 0, 3, 1, 0, 2, 0, 1, 1], #[3, 2, 1, 2, 2, 0, 3, 2, 0], #[3, 2, 0, 2, 0, 0, 2, 0, 1], #[0, 2, 1, 0, 1, 0, 1, 1, 3], #[2, 1, 0, 2, 0, 0, 3, 2, 1], #[3, 3, 0, 1, 2, 3, 1, 1, 1], #[2, 3, 1, 2, 0, 2, 2, 0, 3], #[2, 2, 0, 1, 2, 3, 3, 3, 1], #[3, 2, 1, 1, 2, 3, 2, 0, 3], #[0, 1, 2, 0, 1, 0, 1, 3, 3], #[3, 1, 0, 2, 0, 0, 2, 0, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10, 17, 18, 10, 19, 20, 21, 22, 23, 24, 10, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 131, 129, 130, 1, 147, 145, 146, 2, 163, 161, 162, 3, 179, 177, 178, 388, 453, 243, 67, 389, 452, 227, 83, 390, 455, 211, 99, 391, 454, 195, 115, 392, 65, 458, 209, 393, 81, 459, 193, 394, 97, 456, 241, 395, 113, 457, 225, 396, 226, 66, 463, 397, 242, 82, 462, 398, 194, 98, 461, 399, 210, 114, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 2, 18, 34, 50, 453, 452, 455, 454, 131, 147, 163, 179, 209, 193, 241, 225, 3, 19, 35, 51, 226, 242, 194, 210, 458, 459, 456, 457, 129, 145, 161, 177, 1, 17, 33, 49, 130, 146, 162, 178, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 65, 66, 67, 324, 389, 1, 209, 328, 226, 394, 2, 332, 3, 243, 399, 388, 325, 193, 17, 81, 16, 83, 82, 19, 333, 398, 227, 242, 329, 18, 395, 392, 34, 330, 194, 211, 397, 334, 35, 98, 99, 32, 97, 33, 241, 326, 391, 396, 195, 51, 335, 50, 393, 210, 331, 225, 49, 390, 327, 115, 114, 113, 48], #[0, 145, 162, 179, 324, 453, 65, 1, 328, 2, 458, 66, 332, 67, 3, 463, 16, 129, 178, 163, 325, 452, 81, 17, 329, 18, 459, 82, 333, 83, 19, 462, 32, 177, 130, 147, 326, 455, 97, 33, 330, 34, 456, 98, 334, 99, 35, 461, 48, 161, 146, 131, 327, 454, 113, 49, 331, 50, 457, 114, 335, 115, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row24
