import DegreeDiameter.Portfolio.F9Graph56862Models
import DegreeDiameter.Portfolio.F9Graph56862DecoderInterface
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem route_model_noise (a : Fin 78) (p q r : Fin 6) (n : Vec) :
    routeVec a p q r n 0 =
      act (matrixPool (chart (controller (controller a p) q) r))
        (act (matrixPool (chart (controller a p) q)) (n 0 • direction (inversePort p)) +
          n 1 • direction (chartTarget (chart (controller a p) q))) +
        n 2 • direction (chartTarget (chart (controller (controller a p) q) r)) := by
  simp [routeVec,stepVec,act_zero,matrix,chart_target_valid]
theorem basis_of_pair_and_model (a b : Fin 78) (j : Fin 3)
    (hp : PairCheck a b)
    (hm : modelNoise (modelIndex a b) (act (modelInverse (modelIndex a b)) (basisVec j)) = basisVec j) :
    routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b))
      (nbNoise a b (basisVec j)) 0 = basisVec j := by
  rcases hp with ⟨_,hidx,hfirst,hsecond,hthird⟩
  have hinv : nbInverse a b = modelInverse (modelIndex a b) := by
    funext i k
    simp only [nbInverse,modelInverse,hidx]
  rw [route_model_noise]
  simpa only [modelNoise,nbNoise,hinv,hfirst,hsecond,hthird] using hm
#print axioms basis_of_pair_and_model
end DegreeDiameter.Portfolio.F9Graph56862
