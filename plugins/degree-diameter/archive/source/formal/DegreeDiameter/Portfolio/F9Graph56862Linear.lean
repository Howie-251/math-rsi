import DegreeDiameter.Portfolio.F9Graph56862Routes
namespace DegreeDiameter.Portfolio.F9Graph56862

theorem stepVec_joint_add (a : Fin 78) (p : Fin 6) (s t : F) (x y : Vec) :
  stepVec a p (s+t) (x+y) = stepVec a p s x + stepVec a p t y := by
  simp only [stepVec,act_add,add_smul]
  abel

theorem stepVec_joint_smul (a : Fin 78) (p : Fin 6) (s t : F) (x : Vec) :
  stepVec a p (s*t) (s • x) = s • stepVec a p t x := by
  simp only [stepVec,act_smul,smul_add,smul_smul]

theorem route_noise_add (a : Fin 78) (p q r : Fin 6) (n m : Vec) :
  routeVec a p q r (n+m) 0 = routeVec a p q r n 0 + routeVec a p q r m 0 := by
  have hzero : (0 : Vec) = 0+0 := by simp
  conv_lhs => rw [hzero]
  simp only [routeVec,Pi.add_apply,stepVec_joint_add]

theorem route_noise_smul (a : Fin 78) (p q r : Fin 6) (t : F) (n : Vec) :
  routeVec a p q r (t • n) 0 = t • routeVec a p q r n 0 := by
  have hzero : (0 : Vec) = t • 0 := by simp
  conv_lhs => rw [hzero]
  simp only [routeVec,Pi.smul_apply,smul_eq_mul,stepVec_joint_smul]

theorem stepVec_reverse_zero (a : Fin 78) (p : Fin 6) (x : Vec) :
  stepVec (controller a p) (inversePort p) 0 (stepVec a p 0 x) = x := by
  simpa only [neg_zero] using stepVec_reverse a p 0 x

theorem route_before_center (a : Fin 78) (p q : Fin 6) (x : Vec) :
  routeVec a q (inversePort q) p 0 x = stepVec a p 0 x := by
  simp only [routeVec,Pi.zero_apply,controller_reverse,stepVec_reverse_zero]

theorem route_after_center (a : Fin 78) (p q : Fin 6) (x : Vec) :
  routeVec a p q (inversePort q) 0 x = stepVec a p 0 x := by
  simp only [routeVec,Pi.zero_apply,stepVec_reverse_zero]
end DegreeDiameter.Portfolio.F9Graph56862
