import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.F9Graph56862Models
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem model_basis_chunk_0 : ∀ (j : Fin 13) (i : Fin 3),
    let k := (finProdFinEquiv (m:=13) (n:=13)) ((0 : Fin 13),j)
    modelNoise k (act (modelInverse k) (basisVec i)) = basisVec i := by decide +kernel
#print axioms model_basis_chunk_0
end DegreeDiameter.Portfolio.F9Graph56862
