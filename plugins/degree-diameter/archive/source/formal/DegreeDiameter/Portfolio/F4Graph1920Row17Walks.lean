import DegreeDiameter.Portfolio.F4Graph1920Row17Certificate
namespace DegreeDiameter.Portfolio.F4Graph1920.Row17
open F4Graph3840
theorem noise_decode (b : Fin 30)(h : ¬∃p,controller 17 p=b)(d : Vec) :
    routeVec 17 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b)) (nbNoise b d) 0=d := by
  have heq := additive_ext
    (fun d => routeVec 17 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b)) (nbNoise b d) 0) id
    (by intro x y;dsimp only;unfold nbNoise;rw [act_add,route_noise_add]) (by intros;rfl)
    (by intro t x;dsimp only;unfold nbNoise;rw [act_smul,route_noise_smul]) (by intros;rfl)
    (fun j => nb_basis_row b j h)
  exact congrFun heq d
theorem adjacent_controller (p : Fin 4)(d : Fin 64) :
    routeController 17 (adjP0 p d) (adjP1 p d) (adjP2 p d)=controller 17 p := by
  unfold adjP0 adjP1 adjP2
  split_ifs <;> simp only [routeController,controller_reverse]
theorem adjacent_center (p : Fin 4)(d : Fin 64)(x : Vec) :
    routeVec 17 (adjP0 p d) (adjP1 p d) (adjP2 p d) 0 x=stepVec 17 p 0 x := by
  unfold adjP0 adjP1 adjP2
  split_ifs
  · exact route_before_center 17 p (adjQ p d) x
  · exact route_after_center 17 p (adjQ p d) x
theorem row17_full_walk_bound (x : Fin 64)(v : Fin 1920) :
    ∃w : graph.Walk (liftAt 17 x) v,w.length≤3 := by
  by_cases h : ∃p,controller 17 p=controllerOf v
  · obtain ⟨p,hp⟩ := h
    let d := encodeVec (decodeVec (fiberOf v)-stepVec 17 p 0 (decodeVec x))
    apply bounded_walk_of_route (liftAt 17 x) v (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d)
    · simpa only [controllerOf_liftAt] using (adjacent_controller p d).trans hp
    · simp only [controllerOf_liftAt,fiberOf_liftAt]
      rw [route_affine,adjacent_row,adjacent_center]
      simp only [d,decodeVec_encodeVec]
      abel
  · let b := controllerOf v
    let w := controllerWord b
    let center := routeVec 17 (wordP0 w) (wordP1 w) (wordP2 w) 0 (decodeVec x)
    let d := decodeVec (fiberOf v)-center
    apply bounded_walk_of_route (liftAt 17 x) v (wordP0 w) (wordP1 w) (wordP2 w) (nbNoise b d)
    · simpa only [controllerOf_liftAt] using controller_row b h
    · simp only [controllerOf_liftAt,fiberOf_liftAt]
      rw [route_affine,noise_decode b h]
      change center+(decodeVec (fiberOf v)-center)=decodeVec (fiberOf v)
      abel
#print axioms row17_full_walk_bound
end DegreeDiameter.Portfolio.F4Graph1920.Row17
