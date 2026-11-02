import DegreeDiameter.Portfolio.F4Graph3840Routes
namespace DegreeDiameter.Portfolio.F4Graph3840

theorem stepVec_joint_add (a : Fin 60) (p : Fin 5) (s t : F) (x y : Vec) :
  stepVec a p (s+t) (x+y) = stepVec a p s x + stepVec a p t y := by
  simp only [stepVec,act_add,add_smul]
  abel

theorem stepVec_joint_smul (a : Fin 60) (p : Fin 5) (s t : F) (x : Vec) :
  stepVec a p (s*t) (s • x) = s • stepVec a p t x := by
  simp only [stepVec,act_smul,smul_add,smul_smul]

theorem route_noise_add (a : Fin 60) (p q r : Fin 5) (n m : Vec) :
  routeVec a p q r (n+m) 0 = routeVec a p q r n 0 + routeVec a p q r m 0 := by
  have hzero : (0 : Vec) = 0+0 := by simp
  conv_lhs => rw [hzero]
  simp only [routeVec,Pi.add_apply,stepVec_joint_add]

theorem route_noise_smul (a : Fin 60) (p q r : Fin 5) (t : F) (n : Vec) :
  routeVec a p q r (t • n) 0 = t • routeVec a p q r n 0 := by
  have hzero : (0 : Vec) = t • 0 := by simp
  conv_lhs => rw [hzero]
  simp only [routeVec,Pi.smul_apply,smul_eq_mul,stepVec_joint_smul]

theorem route_before_center (a : Fin 60) (p q : Fin 5) (x : Vec) :
  routeVec a q (inversePort q) p 0 x = stepVec a p 0 x := by
  simp only [routeVec,Pi.zero_apply,controller_reverse,stepVec_reverse]

theorem route_after_center (a : Fin 60) (p q : Fin 5) (x : Vec) :
  routeVec a p q (inversePort q) 0 x = stepVec a p 0 x := by
  simp only [routeVec,Pi.zero_apply,stepVec_reverse]
end DegreeDiameter.Portfolio.F4Graph3840
