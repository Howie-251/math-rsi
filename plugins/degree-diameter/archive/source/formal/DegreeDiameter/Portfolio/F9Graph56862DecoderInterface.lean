import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem noise_decode_of_basis (a b : Fin 78)
    (h : ∀ j, routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b (basisVec j)) 0 = basisVec j) (d : Vec) :
  routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0 = d := by
  have heq := additive_ext
    (fun d => routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0) id
    (by intro x y; dsimp only; unfold nbNoise; rw [act_add,route_noise_add]) (by intros; rfl)
    (by intro t x; dsimp only; unfold nbNoise; rw [act_smul,route_noise_smul]) (by intros; rfl)
    h
  exact congrFun heq d
theorem adjacent_controller (a : Fin 78) (p : Fin 6) (d : Fin 729) :
  routeController a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) = controller a p := by
  unfold adjP0 adjP1 adjP2
  split_ifs <;> simp only [routeController,controller_reverse]
theorem adjacent_center (a : Fin 78) (p : Fin 6) (d : Fin 729) (x : Vec) :
  routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) 0 x = stepVec a p 0 x := by
  unfold adjP0 adjP1 adjP2
  split_ifs
  · exact route_before_center a p (adjQ a p d) x
  · exact route_after_center a p (adjQ a p d) x
theorem before_noise (a : Fin 78) (p q : Fin 6) (s t : F) :
  routeVec a q (inversePort q) p ![0,s,t] 0 =
    s • act (matrix a p) (direction q) + t • direction (inversePort p) := by
  simp [routeVec,stepVec,act_zero,controller_reverse,inversePort_involution,act_smul]
theorem after_noise (a : Fin 78) (p q : Fin 6) (s t : F) :
  routeVec a p q (inversePort q) ![t,0,s] 0 =
    s • direction q + t • direction (inversePort p) := by
  simp [routeVec,stepVec,act_zero,inversePort_involution,act_reverse,add_comm]
theorem chart_target_valid : ∀ (a : Fin 78) (p : Fin 6),
  chartTarget (chart a p) = inversePort p := by decide +kernel
end DegreeDiameter.Portfolio.F9Graph56862
