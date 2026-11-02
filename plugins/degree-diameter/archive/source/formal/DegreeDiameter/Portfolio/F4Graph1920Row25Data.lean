import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row25
open F4Graph3840
def wordData : Array Nat := #[42, 31, 8, 37, 0, 22, 35, 0, 0, 2, 28, 29, 13, 0, 0, 38, 9, 53, 54, 26, 39, 12, 10, 63, 48, 41, 34, 25, 61, 40]
def inversePool : Array (Array Nat) := #[#[0, 3, 3, 1, 3, 2, 1, 0, 0], #[0, 2, 2, 0, 0, 1, 1, 3, 3], #[3, 0, 2, 2, 0, 3, 2, 1, 3], #[2, 3, 1, 3, 3, 0, 3, 1, 3], #[0, 0, 0, 0, 0, 0, 0, 0, 0], #[0, 1, 2, 0, 0, 3, 1, 3, 1], #[3, 1, 2, 3, 3, 0, 3, 1, 3], #[2, 0, 1, 1, 0, 2, 0, 1, 0], #[1, 0, 3, 0, 0, 1, 3, 1, 2], #[0, 2, 3, 0, 1, 3, 1, 3, 1], #[0, 0, 1, 0, 1, 2, 1, 0, 2], #[3, 0, 1, 3, 0, 2, 3, 1, 1], #[3, 0, 3, 2, 2, 0, 1, 0, 0], #[1, 0, 3, 0, 0, 1, 3, 1, 3], #[1, 2, 0, 1, 0, 0, 2, 3, 1], #[2, 0, 0, 0, 2, 0, 3, 0, 1], #[0, 3, 2, 0, 2, 0, 1, 2, 0], #[1, 0, 1, 1, 2, 3, 3, 0, 2], #[2, 0, 3, 1, 0, 3, 3, 1, 1], #[1, 0, 3, 1, 0, 2, 3, 1, 3], #[3, 1, 0, 1, 1, 0, 2, 0, 1], #[2, 1, 0, 3, 1, 0, 2, 1, 1], #[1, 3, 2, 0, 1, 1, 0, 1, 0], #[2, 3, 1, 2, 2, 0, 1, 2, 2], #[0, 0, 3, 0, 2, 3, 1, 2, 0], #[0, 3, 0, 2, 2, 0, 2, 2, 1], #[3, 1, 2, 0, 3, 3, 0, 3, 2]]
def inverseIndex : Array Nat := #[0, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10, 11, 4, 4, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
def adjacentData : Array (Array Nat) := #[#[0, 260, 264, 268, 1, 261, 265, 269, 2, 262, 266, 270, 3, 263, 267, 271, 388, 129, 67, 226, 389, 145, 83, 242, 390, 161, 99, 194, 391, 177, 115, 210, 392, 243, 130, 65, 393, 227, 146, 81, 394, 211, 162, 97, 395, 195, 178, 113, 396, 66, 209, 131, 397, 82, 193, 147, 398, 98, 241, 163, 399, 114, 225, 179], #[0, 16, 32, 48, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 388, 389, 390, 391, 3, 19, 35, 51, 130, 146, 162, 178, 209, 193, 241, 225, 392, 393, 394, 395, 226, 242, 194, 210, 1, 17, 33, 49, 131, 147, 163, 179, 396, 397, 398, 399, 129, 145, 161, 177, 243, 227, 211, 195, 2, 18, 34, 50], #[0, 260, 264, 268, 324, 3, 66, 209, 328, 226, 1, 67, 332, 65, 243, 2, 19, 325, 193, 82, 261, 16, 269, 265, 81, 333, 18, 227, 242, 329, 83, 17, 33, 99, 330, 194, 211, 34, 334, 97, 266, 270, 32, 262, 98, 241, 326, 35, 50, 195, 113, 335, 115, 49, 210, 331, 225, 114, 51, 327, 271, 267, 263, 48], #[0, 260, 264, 268, 162, 453, 67, 1, 179, 2, 458, 65, 145, 66, 3, 463, 16, 261, 265, 269, 178, 452, 83, 17, 163, 18, 459, 81, 129, 82, 19, 462, 32, 262, 266, 270, 130, 455, 99, 33, 147, 34, 456, 97, 177, 98, 35, 461, 48, 263, 267, 271, 146, 454, 115, 49, 131, 50, 457, 113, 161, 114, 51, 460]]

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
end DegreeDiameter.Portfolio.F4Graph1920.Row25
