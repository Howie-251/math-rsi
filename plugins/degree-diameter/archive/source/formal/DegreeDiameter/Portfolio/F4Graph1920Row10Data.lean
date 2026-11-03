import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row10
open F4Graph3840
def wordData : Array Nat := #[25, 39, 9, 0, 0, 60, 48, 53, 0, 38, 8, 10, 61, 21, 37, 51, 26, 42, 40, 0, 35, 13, 32, 28, 0, 24, 55, 63, 31, 41]
def inversePool : Array (Array Nat) := #[#[0, 0, 1, 0, 1, 3, 1, 1, 1], #[1, 3, 2, 1, 2, 3, 2, 1, 2], #[2, 0, 1, 2, 0, 3, 0, 1, 2], #[1, 0, 3, 1, 0, 0, 1, 1, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[1, 3, 0, 3, 3, 0, 3, 3, 1], #[2, 0, 0, 1, 1, 0, 3, 0, 1], #[1, 3, 0, 3, 3, 0, 2, 1, 1], #[3, 1, 2, 3, 0, 3, 1, 2, 2], #[2, 0, 3, 1, 0, 0, 0, 1, 2], #[3, 0, 3, 1, 0, 2, 0, 1, 3], #[2, 3, 0, 2, 0, 0, 2, 0, 1], #[0, 2, 2, 0, 1, 2, 1, 2, 2], #[3, 3, 0, 1, 2, 3, 1, 1, 1], #[3, 1, 0, 3, 2, 0, 0, 0, 1], #[0, 1, 3, 0, 3, 0, 1, 3, 0], #[1, 3, 2, 3, 3, 0, 2, 0, 3], #[3, 1, 2, 3, 3, 0, 3, 3, 1], #[3, 1, 2, 2, 0, 2, 0, 0, 1], #[1, 0, 2, 1, 0, 3, 1, 1, 2], #[1, 2, 3, 0, 1, 1, 2, 3, 0], #[0, 2, 2, 0, 1, 2, 1, 0, 0], #[0, 2, 0, 0, 2, 1, 1, 1, 1], #[2, 3, 0, 1, 0, 0, 3, 1, 1], #[3, 1, 0, 0, 3, 0, 3, 2, 1], #[0, 2, 1, 0, 3, 1, 1, 0, 0], #[1, 2, 3, 1, 1, 0, 1, 1, 1]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 7, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 4, 18, 19, 20, 21, 4, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 243, 130, 65, 389, 227, 146, 81, 390, 211, 162, 97, 391, 195, 178, 113, 392, 66, 209, 131, 393, 82, 193, 147, 394, 98, 241, 163, 395, 114, 225, 179, 396, 129, 67, 226, 397, 145, 83, 242, 398, 161, 99, 194, 399, 177, 115, 210], #[0, 16, 32, 48, 129, 145, 161, 177, 130, 146, 162, 178, 131, 147, 163, 179, 388, 389, 390, 391, 453, 452, 455, 454, 1, 17, 33, 49, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 458, 459, 456, 457, 2, 18, 34, 50, 396, 397, 398, 399, 3, 19, 35, 51, 243, 227, 211, 195, 463, 462, 461, 460], #[0, 260, 264, 268, 65, 389, 226, 3, 66, 1, 394, 243, 67, 209, 2, 399, 388, 81, 19, 242, 261, 16, 269, 265, 193, 83, 398, 18, 17, 82, 227, 395, 392, 211, 98, 33, 34, 397, 99, 241, 266, 270, 32, 262, 194, 35, 97, 391, 396, 50, 225, 115, 195, 393, 49, 114, 51, 210, 390, 113, 271, 267, 263, 48], #[0, 260, 264, 268, 1, 453, 162, 67, 2, 65, 458, 179, 3, 145, 66, 463, 16, 261, 265, 269, 17, 452, 178, 83, 18, 81, 459, 163, 19, 129, 82, 462, 32, 262, 266, 270, 33, 455, 130, 99, 34, 97, 456, 147, 35, 177, 98, 461, 48, 263, 267, 271, 49, 454, 146, 115, 50, 113, 457, 131, 51, 161, 114, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row10
