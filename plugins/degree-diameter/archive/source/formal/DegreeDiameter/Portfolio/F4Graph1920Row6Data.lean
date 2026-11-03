import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row6
open F4Graph3840
def wordData : Array Nat := #[37, 50, 63, 48, 38, 28, 61, 8, 29, 26, 22, 3, 32, 55, 53, 0, 0, 2, 60, 51, 9, 0, 0, 15, 24, 39, 31, 23, 42, 0]
def inversePool : Array (Array Nat) := #[#[1, 3, 2, 1, 2, 3, 0, 0, 1], #[3, 1, 0, 2, 0, 0, 2, 3, 1], #[2, 1, 0, 2, 3, 0, 0, 2, 1], #[1, 2, 0, 1, 1, 0, 2, 3, 1], #[2, 1, 3, 3, 3, 0, 3, 2, 0], #[0, 3, 3, 0, 2, 3, 1, 0, 0], #[3, 1, 0, 2, 1, 0, 2, 1, 1], #[1, 0, 3, 3, 0, 3, 1, 1, 2], #[0, 1, 2, 0, 2, 1, 1, 0, 0], #[0, 2, 1, 0, 2, 0, 1, 2, 0], #[0, 3, 2, 0, 0, 3, 1, 1, 3], #[3, 0, 2, 1, 0, 2, 3, 1, 2], #[3, 2, 1, 2, 3, 1, 1, 3, 3], #[2, 2, 0, 1, 0, 0, 2, 2, 1], #[1, 0, 0, 2, 1, 0, 0, 0, 1], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[2, 0, 1, 1, 0, 0, 2, 1, 1], #[2, 1, 0, 2, 0, 0, 2, 0, 1], #[3, 1, 0, 2, 2, 0, 2, 3, 1], #[1, 0, 3, 1, 0, 2, 0, 1, 1], #[2, 0, 1, 3, 0, 1, 1, 1, 3], #[0, 2, 1, 0, 2, 0, 1, 1, 2], #[3, 1, 2, 3, 3, 0, 3, 1, 3], #[0, 1, 2, 0, 0, 1, 1, 1, 2], #[0, 2, 3, 0, 2, 1, 1, 3, 1], #[1, 2, 3, 1, 1, 0, 0, 3, 2], #[1, 0, 3, 3, 0, 1, 3, 1, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 15, 15, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 65, 66, 67, 1, 81, 82, 83, 2, 97, 98, 99, 3, 113, 114, 115, 388, 453, 129, 209, 389, 452, 145, 193, 390, 455, 161, 241, 391, 454, 177, 225, 392, 226, 458, 130, 393, 242, 459, 146, 394, 194, 456, 162, 395, 210, 457, 178, 396, 131, 243, 463, 397, 147, 227, 462, 398, 163, 211, 461, 399, 179, 195, 460], #[0, 16, 32, 48, 226, 242, 194, 210, 243, 227, 211, 195, 209, 193, 241, 225, 388, 389, 390, 391, 453, 452, 455, 454, 2, 18, 34, 50, 130, 146, 162, 178, 392, 393, 394, 395, 131, 147, 163, 179, 458, 459, 456, 457, 3, 19, 35, 51, 396, 397, 398, 399, 1, 17, 33, 49, 129, 145, 161, 177, 463, 462, 461, 460], #[0, 260, 264, 268, 65, 389, 226, 3, 66, 1, 394, 243, 67, 209, 2, 399, 388, 81, 19, 242, 261, 16, 269, 265, 193, 83, 398, 18, 17, 82, 227, 395, 392, 211, 98, 33, 34, 397, 99, 241, 266, 270, 32, 262, 194, 35, 97, 391, 396, 50, 225, 115, 195, 393, 49, 114, 51, 210, 390, 113, 271, 267, 263, 48], #[0, 162, 179, 145, 324, 453, 2, 66, 328, 67, 458, 3, 332, 1, 65, 463, 16, 178, 163, 129, 325, 452, 18, 82, 329, 83, 459, 19, 333, 17, 81, 462, 32, 130, 147, 177, 326, 455, 34, 98, 330, 99, 456, 35, 334, 33, 97, 461, 48, 146, 131, 161, 327, 454, 50, 114, 331, 115, 457, 51, 335, 49, 113, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row6
