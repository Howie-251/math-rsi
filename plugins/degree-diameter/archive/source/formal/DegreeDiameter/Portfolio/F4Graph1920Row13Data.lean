import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row13
open F4Graph3840
def wordData : Array Nat := #[53, 0, 55, 29, 10, 41, 34, 0, 48, 40, 0, 37, 31, 60, 42, 54, 12, 9, 32, 8, 38, 25, 63, 0, 13, 0, 61, 28, 3, 24]
def inversePool : Array (Array Nat) := #[#[2, 0, 0, 1, 2, 0, 0, 0, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 3, 0, 1, 1, 0, 0, 0, 1], #[0, 1, 2, 0, 2, 1, 1, 3, 1], #[3, 0, 2, 1, 0, 1, 0, 1, 2], #[1, 3, 2, 2, 0, 2, 2, 0, 3], #[2, 3, 1, 1, 0, 1, 2, 3, 0], #[3, 3, 0, 0, 3, 0, 1, 1, 1], #[3, 2, 1, 3, 3, 0, 3, 3, 1], #[3, 0, 0, 2, 0, 1, 2, 1, 0], #[2, 1, 3, 3, 1, 2, 0, 0, 1], #[0, 2, 3, 0, 0, 3, 1, 0, 0], #[2, 3, 0, 2, 0, 0, 2, 0, 1], #[1, 3, 2, 3, 3, 0, 2, 0, 3], #[1, 3, 0, 0, 1, 0, 0, 0, 1], #[3, 0, 1, 0, 0, 1, 2, 1, 3], #[3, 0, 3, 1, 0, 3, 2, 1, 0], #[2, 0, 2, 2, 1, 3, 3, 0, 2], #[3, 0, 3, 2, 2, 0, 0, 0, 1], #[0, 3, 1, 0, 2, 1, 1, 0, 2], #[0, 2, 0, 1, 1, 0, 1, 3, 1], #[0, 0, 1, 3, 0, 2, 0, 1, 1], #[0, 1, 0, 2, 0, 0, 2, 0, 1], #[0, 3, 2, 0, 2, 3, 1, 1, 3], #[2, 0, 1, 0, 0, 3, 1, 1, 3], #[0, 2, 3, 0, 1, 1, 1, 0, 3]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 16, 18, 19, 20, 1, 21, 1, 22, 23, 24, 25]
def adjacentData : Array (Array Nat) := #[#[0, 226, 243, 209, 1, 242, 227, 193, 2, 194, 211, 241, 3, 210, 195, 225, 388, 453, 66, 130, 389, 452, 82, 146, 390, 455, 98, 162, 391, 454, 114, 178, 392, 131, 458, 67, 393, 147, 459, 83, 394, 163, 456, 99, 395, 179, 457, 115, 396, 65, 129, 463, 397, 81, 145, 462, 398, 97, 161, 461, 399, 113, 177, 460], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 129, 145, 161, 177, 3, 19, 35, 51, 226, 242, 194, 210, 392, 393, 394, 395, 243, 227, 211, 195, 130, 146, 162, 178, 1, 17, 33, 49, 396, 397, 398, 399, 2, 18, 34, 50, 209, 193, 241, 225, 131, 147, 163, 179], #[0, 209, 226, 243, 324, 389, 65, 1, 328, 2, 394, 66, 332, 67, 3, 399, 388, 325, 17, 81, 193, 16, 227, 242, 83, 333, 398, 19, 18, 329, 82, 395, 392, 98, 330, 34, 35, 397, 334, 99, 194, 211, 32, 241, 97, 33, 326, 391, 396, 51, 115, 335, 114, 393, 50, 331, 49, 113, 390, 327, 195, 210, 225, 48], #[0, 67, 65, 66, 324, 453, 179, 3, 328, 1, 458, 145, 332, 162, 2, 463, 16, 83, 81, 82, 325, 452, 163, 19, 329, 17, 459, 129, 333, 178, 18, 462, 32, 99, 97, 98, 326, 455, 147, 35, 330, 33, 456, 177, 334, 130, 34, 461, 48, 115, 113, 114, 327, 454, 131, 51, 331, 49, 457, 161, 335, 146, 50, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row13
