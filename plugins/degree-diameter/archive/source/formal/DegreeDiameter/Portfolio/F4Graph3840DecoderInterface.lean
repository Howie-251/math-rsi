import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
namespace DegreeDiameter.Portfolio.F4Graph3840
theorem noise_decode_of_basis (a b : Fin 60)
    (h : ∀ j, routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b (basisVec j)) 0 = basisVec j) (d : Vec) :
  routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0 = d := by
  have heq := additive_ext
    (fun d => routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0) id
    (by intro x y; dsimp only; unfold nbNoise; rw [act_add,route_noise_add]) (by intros; rfl)
    (by intro t x; dsimp only; unfold nbNoise; rw [act_smul,route_noise_smul]) (by intros; rfl)
    h
  exact congrFun heq d

theorem adjacent_controller (a : Fin 60) (p : Fin 5) (d : Fin 64) :
  routeController a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) = controller a p := by
  unfold adjP0 adjP1 adjP2
  split_ifs <;> simp only [routeController,controller_reverse]

theorem adjacent_center (a : Fin 60) (p : Fin 5) (d : Fin 64) (x : Vec) :
  routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) 0 x = stepVec a p 0 x := by
  unfold adjP0 adjP1 adjP2
  split_ifs
  · exact route_before_center a p (adjQ a p d) x
  · exact route_after_center a p (adjQ a p d) x

#print axioms noise_decode_of_basis
#print axioms adjacent_center
end DegreeDiameter.Portfolio.F4Graph3840
