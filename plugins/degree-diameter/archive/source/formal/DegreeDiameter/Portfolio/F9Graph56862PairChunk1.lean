import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.F9Graph56862Models
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem pair_check_chunk_1 : ∀ (j : Fin 13) (b : Fin 78),
    let a := (finProdFinEquiv (m:=6) (n:=13)) ((1 : Fin 6),j)
    (¬∃ p, controller a p = b) → PairCheck a b := by decide +kernel
#print axioms pair_check_chunk_1
end DegreeDiameter.Portfolio.F9Graph56862
