import DegreeDiameter.Portfolio.F5Graph3750Routes

namespace DegreeDiameter.Portfolio.F5Graph3750
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000

theorem coordinate_zero (i : Fin 3) : coordinate 0 i = 0 := by simp [coordinate]

theorem add_zero (x : Fin 125) : addFiber x 0 = x := by
  apply fiber_ext
  intro i
  rw [coordinate_add, coordinate_zero, Nat.add_zero]
  exact Nat.mod_eq_of_lt (Nat.mod_lt _ (by decide))

def noiseAt (n : Fin 125) (i : Fin 3) : Fin 5 :=
  ⟨coordinate n i, Nat.mod_lt _ (by decide)⟩

theorem noiseAt_zero (i : Fin 3) : noiseAt 0 i = 0 := by
  apply Fin.ext
  exact coordinate_zero i

def routeFiber (p q r : Fin 4) (n x : Fin 125) : Fin 125 :=
  fiberStep r (noiseAt n 2) (fiberStep q (noiseAt n 1) (fiberStep p (noiseAt n 0) x))

theorem route_add (p q r : Fin 4) (n x y : Fin 125) :
    routeFiber p q r n (addFiber x y) =
      addFiber (routeFiber p q r 0 x) (routeFiber p q r n y) := by
  simp only [routeFiber, noiseAt_zero]
  rw [fiberStep_add, fiberStep_add, fiberStep_add]

theorem route_affine (p q r : Fin 4) (n x : Fin 125) :
    routeFiber p q r n x =
      addFiber (routeFiber p q r 0 x) (routeFiber p q r n 0) := by
  simpa only [add_zero] using route_add p q r n x 0

theorem fiber_zero_reverse (p : Fin 4) (x : Fin 125) :
    fiberStep (inversePort p) 0 (fiberStep p 0 x) = x := by
  have h := fiberStep_reverse p 0 x
  change fiberStep (inversePort p) 0 (fiberStep p 0 x) = x at h
  exact h

theorem route_before_center (p q : Fin 4) (x : Fin 125) :
    routeFiber q (inversePort q) p 0 x = fiberStep p 0 x := by
  simp only [routeFiber, noiseAt_zero, fiber_zero_reverse]

theorem route_after_center (p q : Fin 4) (x : Fin 125) :
    routeFiber p q (inversePort q) 0 x = fiberStep p 0 x := by
  simp only [routeFiber, noiseAt_zero, fiber_zero_reverse]

def liftAt (a : Fin 30) (x : Fin 125) : Fin 3750 :=
  ⟨125 * a.val + x.val, by have ha := a.isLt; have hx := x.isLt; omega⟩

theorem controllerOf_liftAt (a : Fin 30) (x : Fin 125) : controllerOf (liftAt a x) = a := by
  apply Fin.ext
  change (125 * a.val + x.val) / 125 = a.val
  have hx := x.isLt
  omega

theorem fiberOf_liftAt (a : Fin 30) (x : Fin 125) : fiberOf (liftAt a x) = x := by
  apply Fin.ext
  change (125 * a.val + x.val) % 125 = x.val
  have hx := x.isLt
  omega

theorem liftAt_parts (u : Fin 3750) : liftAt (controllerOf u) (fiberOf u) = u := by
  apply Fin.ext
  change 125 * (u.val / 125) + u.val % 125 = u.val
  omega

theorem forward_liftAt (a : Fin 30) (x : Fin 125) (p : Fin 4) (t : Fin 5) :
    forward (liftAt a x) p t = liftAt (controller a p) (fiberStep p t x) := by
  apply Fin.ext
  change 125 * (controller (controllerOf (liftAt a x)) p).val +
    (fiberStep p t (fiberOf (liftAt a x))).val =
    125 * (controller a p).val + (fiberStep p t x).val
  rw [controllerOf_liftAt, fiberOf_liftAt]

def routeForward (u : Fin 3750) (p q r : Fin 4) (n : Fin 125) : Fin 3750 :=
  forward (forward (forward u p (noiseAt n 0)) q (noiseAt n 1)) r (noiseAt n 2)

theorem routeForward_liftAt (a : Fin 30) (x : Fin 125) (p q r : Fin 4) (n : Fin 125) :
    routeForward (liftAt a x) p q r n =
      liftAt (controller (controller (controller a p) q) r) (routeFiber p q r n x) := by
  simp only [routeForward, forward_liftAt, routeFiber]

theorem routeForward_parts (u : Fin 3750) (p q r : Fin 4) (n : Fin 125) :
    routeForward u p q r n =
      liftAt (controller (controller (controller (controllerOf u) p) q) r)
        (routeFiber p q r n (fiberOf u)) := by
  simpa only [liftAt_parts] using routeForward_liftAt (controllerOf u) (fiberOf u) p q r n

def walkThree (u : Fin 3750) (p q r : Fin 4) (n : Fin 125) :
    graph.Walk u (routeForward u p q r n) :=
  SimpleGraph.Walk.cons ((adj_iff_forward _ _).mpr ⟨p, noiseAt n 0, rfl⟩)
    (SimpleGraph.Walk.cons ((adj_iff_forward _ _).mpr ⟨q, noiseAt n 1, rfl⟩)
      (SimpleGraph.Walk.cons ((adj_iff_forward _ _).mpr ⟨r, noiseAt n 2, rfl⟩)
        SimpleGraph.Walk.nil))

theorem walkThree_length (u : Fin 3750) (p q r : Fin 4) (n : Fin 125) :
    (walkThree u p q r n).length = 3 := rfl

theorem bounded_walk_of_route (u v : Fin 3750) (p q r : Fin 4) (n : Fin 125)
    (hc : controller (controller (controller (controllerOf u) p) q) r = controllerOf v)
    (hf : routeFiber p q r n (fiberOf u) = fiberOf v) :
    ∃ w : graph.Walk u v, w.length ≤ 3 := by
  have hend : routeForward u p q r n = v := by
    rw [routeForward_parts, hc, hf, liftAt_parts]
  rw [← hend]
  exact ⟨walkThree u p q r n, by rw [walkThree_length]⟩

#print axioms route_affine
#print axioms bounded_walk_of_route
end DegreeDiameter.Portfolio.F5Graph3750
