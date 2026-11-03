import DegreeDiameter.Portfolio.F9Graph56862MatrixCertificate
import Mathlib.Algebra.Module.Pi

namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

theorem act_zero (A : Mat) : act A 0 = 0 := by funext i; simp [act]
theorem stepVec_zero (a : Fin 78) (p : Fin 6) (x : Vec) : stepVec a p 0 x = act (matrix a p) x := by
  simp [stepVec]

theorem stepVec_add (a : Fin 78) (p : Fin 6) (t : F) (x y : Vec) :
  stepVec a p t (x+y) = stepVec a p 0 x + stepVec a p t y := by
  simp only [stepVec, act_add, zero_smul, add_zero]
  abel

theorem act_reverse (a : Fin 78) (p : Fin 6) (x : Vec) :
  act (matrix (controller a p) (inversePort p)) (act (matrix a p) x) = x := by
  have h := additive_ext
    (fun x => act (matrix (controller a p) (inversePort p)) (act (matrix a p) x)) id
    (by intro x y; dsimp only; rw [act_add, act_add]) (by intros; rfl)
    (by intro t x; dsimp only; rw [act_smul, act_smul]) (by intros; rfl)
    (inverse_basis a p)
  exact congrFun h x

theorem stepVec_reverse (a : Fin 78) (p : Fin 6) (t : F) (x : Vec) :
  stepVec (controller a p) (inversePort p) (-t) (stepVec a p t x) = x := by
  simp only [stepVec, act_add, act_smul, act_reverse, inverse_direction, inversePort_involution]
  simp only [neg_smul]
  abel

theorem fiberStep_reverse (a : Fin 78) (p : Fin 6) (t : F) (x : Fin 729) :
  fiberStep (controller a p) (inversePort p) (-t) (fiberStep a p t x) = x := by
  simp only [fiberStep, decodeVec_encodeVec, stepVec_reverse, encodeVec_decodeVec]

theorem forward_reverse (u : Fin 56862) (p : Fin 6) (t : F) :
  forward (forward u p t) (inversePort p) (-t) = u := by
  simp only [forward, controllerOf_liftAt, fiberOf_liftAt, controller_reverse, fiberStep_reverse, liftAt_parts]

theorem adj_iff_forward (u v : Fin 56862) :
  graph.Adj u v ↔ ∃ (p : Fin 6) (t : F), forward u p t = v := by
  constructor
  · rintro ⟨_, h⟩
    rcases h with h | ⟨p,t,h⟩
    · exact h
    · refine ⟨inversePort p,-t,?_⟩
      rw [← h]
      exact forward_reverse v p t
  · rintro ⟨p,t,h⟩
    refine ⟨?_,Or.inl ⟨p,t,h⟩⟩
    intro heq
    exact forward_ne_self u p t (h.trans heq.symm)

theorem neighborFinset_eq_forward (u : Fin 56862) :
  graph.neighborFinset u = (Finset.univ.product Finset.univ).image (fun pt : Fin 6 × F => forward u pt.1 pt.2) := by
  ext v
  simp only [SimpleGraph.mem_neighborFinset, adj_iff_forward, Finset.mem_image]
  constructor
  · rintro ⟨p,t,h⟩; exact ⟨(p,t),by simp,h⟩
  · rintro ⟨pt,_,h⟩; exact ⟨pt.1,pt.2,h⟩

theorem degree_le_fifty_four (u : Fin 56862) : graph.degree u ≤ 54 := by
  rw [← SimpleGraph.card_neighborFinset_eq_degree, neighborFinset_eq_forward]
  calc
    _ ≤ (Finset.univ.product (Finset.univ : Finset F)).card := Finset.card_image_le
    _ = 54 := by decide

def routeController (a : Fin 78) (p q r : Fin 6) : Fin 78 := controller (controller (controller a p) q) r

def routeVec (a : Fin 78) (p q r : Fin 6) (n x : Vec) : Vec :=
  stepVec (controller (controller a p) q) r (n 2)
    (stepVec (controller a p) q (n 1) (stepVec a p (n 0) x))

theorem route_affine (a : Fin 78) (p q r : Fin 6) (n x : Vec) :
  routeVec a p q r n x = routeVec a p q r 0 x + routeVec a p q r n 0 := by
  have h : x + (0 : Vec) = x := add_zero x
  conv_lhs => rw [← h]
  simp only [routeVec, Pi.zero_apply, stepVec_add]

def routeForward (u : Fin 56862) (p q r : Fin 6) (n : Vec) : Fin 56862 :=
  forward (forward (forward u p (n 0)) q (n 1)) r (n 2)

theorem routeForward_parts (u : Fin 56862) (p q r : Fin 6) (n : Vec) :
  routeForward u p q r n = liftAt (routeController (controllerOf u) p q r)
    (encodeVec (routeVec (controllerOf u) p q r n (decodeVec (fiberOf u)))) := by
  simp only [routeForward, forward, controllerOf_liftAt, fiberOf_liftAt,
    fiberStep, decodeVec_encodeVec, routeVec, routeController]

def walkThree (u : Fin 56862) (p q r : Fin 6) (n : Vec) : graph.Walk u (routeForward u p q r n) :=
  SimpleGraph.Walk.cons (forward_adj _ _ _)
    (SimpleGraph.Walk.cons (forward_adj _ _ _)
      (SimpleGraph.Walk.cons (forward_adj _ _ _) SimpleGraph.Walk.nil))

theorem bounded_walk_of_route (u v : Fin 56862) (p q r : Fin 6) (n : Vec)
  (hc : routeController (controllerOf u) p q r = controllerOf v)
  (hf : routeVec (controllerOf u) p q r n (decodeVec (fiberOf u)) = decodeVec (fiberOf v)) :
  ∃ w : graph.Walk u v, w.length ≤ 3 := by
  have hend : routeForward u p q r n = v := by
    rw [routeForward_parts,hc,hf,encodeVec_decodeVec,liftAt_parts]
  rw [← hend]
  exact ⟨walkThree u p q r n, by change 3 ≤ 3; decide⟩

#print axioms degree_le_fifty_four
#print axioms bounded_walk_of_route
end DegreeDiameter.Portfolio.F9Graph56862
