import DegreeDiameter.Portfolio.F3Graph15552Definitions
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

theorem vec_basis (x : Vec) :
    x=x 0 • basisVec 0+x 1 • basisVec 1+x 2 • basisVec 2+x 3 • basisVec 3 := by
  funext i
  fin_cases i <;> simp [basisVec]
theorem act_add (A : Mat) (x y : Vec) : act A (x+y)=act A x+act A y := by
  funext i
  simp only [act,Pi.add_apply,mul_add]
  abel
theorem act_smul (A : Mat) (t : F) (x : Vec) : act A (t • x)=t • act A x := by
  funext i
  simp only [act,Pi.smul_apply,smul_eq_mul]
  ring
theorem act_sub (A : Mat) (x y : Vec) : act A (x-y)=act A x-act A y := by
  funext i
  simp only [act,Pi.sub_apply,mul_sub]
  ring
def combine (d : Fin 4 → Vec) (x : Vec) : Vec :=
  x 0 • d 0+x 1 • d 1+x 2 • d 2+x 3 • d 3
theorem act_basis (A : Mat) (x : Vec) : act A x=
    x 0 • act A (basisVec 0)+x 1 • act A (basisVec 1)+
      x 2 • act A (basisVec 2)+x 3 • act A (basisVec 3) := by
  conv_lhs => rw [vec_basis x]
  simp only [act_add,act_smul]
theorem act_combine (A : Mat) (d : Fin 4 → Vec) (x : Vec) :
    act A (combine d x)=x 0 • act A (d 0)+x 1 • act A (d 1)+
      x 2 • act A (d 2)+x 3 • act A (d 3) := by
  simp only [combine,act_add,act_smul]

/-- Offsets need not lie in the noise image.  Their difference is retained
in the coset-cover equation rather than being silently discarded. -/
theorem affine_coset_solve (M Mr N : Mat) (cw cr x y alpha : Vec)
    (d : Fin 4 → Vec)
    (hcol : ∀j,act M (basisVec j)=act Mr (basisVec j)+act N (d j))
    (hcover : act N alpha=(y-act Mr x-cr)-(cw-cr)) :
    act M x+cw+act N (alpha-combine d x)=y := by
  have hc : act M x=act Mr x+act N (combine d x) := by
    rw [act_basis M x,act_basis Mr x,act_combine]
    rw [hcol 0,hcol 1,hcol 2,hcol 3]
    funext i
    simp only [Pi.add_apply,Pi.smul_apply,smul_eq_mul]
    ring
  rw [hc,act_sub,hcover]
  abel

def noiseShift (q : Vec) : Vec := fun i => q ⟨(i.val+1)%4,Nat.mod_lt _ (by decide)⟩
theorem noiseShift_add (q r : Vec) : noiseShift (q+r)=noiseShift q+noiseShift r := rfl
theorem noiseShift_smul (t : F) (q : Vec) : noiseShift (t • q)=t • noiseShift q := rfl
theorem noiseShift_zero : noiseShift (0:Vec)=0 := rfl
theorem stepVec_eq (p : Fin 5) (t : F) (x : Vec) :
    stepVec p t x=act (matrix p) x+t • direction p := by
  simp only [stepVec,constant_zero,add_zero]
theorem stepVec_joint_add (p : Fin 5) (t s : F) (x y : Vec) :
    stepVec p (t+s) (x+y)=stepVec p t x+stepVec p s y := by
  funext i
  simp only [stepVec_eq,act_add,Pi.add_apply,Pi.smul_apply,smul_eq_mul]
  ring
theorem stepVec_joint_smul (p : Fin 5) (t s : F) (x : Vec) :
    stepVec p (t*s) (t • x)=t • stepVec p s x := by
  funext i
  simp only [stepVec_eq,act_smul,Pi.add_apply,Pi.smul_apply,smul_eq_mul]
  ring
theorem stepVec_zero_zero (p : Fin 5) : stepVec p 0 0=0 := by
  funext i
  simp [stepVec_eq,act]

def routeVec : List (Fin 5) → Vec → Vec → Vec
  | [],_,x => x
  | p::ps,q,x => routeVec ps (noiseShift q) (stepVec p (q 0) x)
theorem routeVec_add (ps : List (Fin 5)) (q r x y : Vec) :
    routeVec ps (q+r) (x+y)=routeVec ps q x+routeVec ps r y := by
  induction ps generalizing q r x y with
  | nil => rfl
  | cons p ps ih =>
      simp only [routeVec,Pi.add_apply,stepVec_joint_add,noiseShift_add]
      exact ih _ _ _ _
theorem routeVec_smul (ps : List (Fin 5)) (t : F) (q x : Vec) :
    routeVec ps (t • q) (t • x)=t • routeVec ps q x := by
  induction ps generalizing q x with
  | nil => rfl
  | cons p ps ih =>
      simp only [routeVec,Pi.smul_apply,smul_eq_mul,stepVec_joint_smul,noiseShift_smul]
      exact ih _ _
theorem routeVec_zero_zero (ps : List (Fin 5)) : routeVec ps 0 0=0 := by
  induction ps with
  | nil => rfl
  | cons p ps ih =>
      simp only [routeVec,Pi.zero_apply,noiseShift_zero,stepVec_zero_zero,ih]
theorem route_before_add (ps : List (Fin 5)) (x y : Vec) :
    routeVec ps 0 (x+y)=routeVec ps 0 x+routeVec ps 0 y := by
  simpa only [zero_add] using routeVec_add ps 0 0 x y
theorem route_before_smul (ps : List (Fin 5)) (t : F) (x : Vec) :
    routeVec ps 0 (t • x)=t • routeVec ps 0 x := by
  simpa only [smul_zero] using routeVec_smul ps t 0 x
theorem route_noise_add (ps : List (Fin 5)) (q r : Vec) :
    routeVec ps (q+r) 0=routeVec ps q 0+routeVec ps r 0 := by
  simpa only [zero_add] using routeVec_add ps q r 0 0
theorem route_noise_smul (ps : List (Fin 5)) (t : F) (q : Vec) :
    routeVec ps (t • q) 0=t • routeVec ps q 0 := by
  simpa only [smul_zero] using routeVec_smul ps t q 0
theorem route_noise_neg (ps : List (Fin 5)) (q : Vec) :
    routeVec ps (-q) 0= -routeVec ps q 0 := by
  have h : routeVec ps q 0+routeVec ps (-q) 0=0 := by
    rw [← route_noise_add,add_neg_cancel,routeVec_zero_zero]
  calc
    routeVec ps (-q) 0=(routeVec ps q 0+routeVec ps (-q) 0)-routeVec ps q 0 := by abel
    _ = -routeVec ps q 0 := by rw [h,zero_sub]
theorem route_noise_sub (ps : List (Fin 5)) (q r : Vec) :
    routeVec ps (q-r) 0=routeVec ps q 0-routeVec ps r 0 := by
  simp only [sub_eq_add_neg,route_noise_add,route_noise_neg]
theorem route_decompose (ps : List (Fin 5)) (q x : Vec) :
    routeVec ps q x=routeVec ps 0 x+routeVec ps q 0 := by
  simpa only [zero_add,add_zero] using routeVec_add ps 0 q x 0
theorem route_before_basis (ps : List (Fin 5)) (x : Vec) : routeVec ps 0 x=
    x 0 • routeVec ps 0 (basisVec 0)+x 1 • routeVec ps 0 (basisVec 1)+
    x 2 • routeVec ps 0 (basisVec 2)+x 3 • routeVec ps 0 (basisVec 3) := by
  conv_lhs => rw [vec_basis x]
  simp only [route_before_add,route_before_smul]
theorem route_noise_combine (ps : List (Fin 5)) (d : Fin 4 → Vec) (x : Vec) :
    routeVec ps (combine d x) 0=x 0 • routeVec ps (d 0) 0+x 1 • routeVec ps (d 1) 0+
      x 2 • routeVec ps (d 2) 0+x 3 • routeVec ps (d 3) 0 := by
  simp only [combine,route_noise_add,route_noise_smul]

theorem column_translation (reference word : List (Fin 5)) (d : Fin 4 → Vec)
    (hcol : ∀j,routeVec word 0 (basisVec j)=
      routeVec reference 0 (basisVec j)+routeVec word (d j) 0) (x : Vec) :
    routeVec word 0 x=routeVec reference 0 x+routeVec word (combine d x) 0 := by
  rw [route_before_basis word x,route_before_basis reference x,route_noise_combine]
  rw [hcol 0,hcol 1,hcol 2,hcol 3]
  funext i
  simp only [Pi.add_apply,Pi.smul_apply,smul_eq_mul]
  ring

theorem coset_solution {K : Type*} (reference : List (Fin 5)) (word : K → List (Fin 5))
    (column : K → Fin 4 → Vec) (choice : Fin 81 → K) (alpha : Fin 81 → Vec)
    (hcol : ∀k j,routeVec (word k) 0 (basisVec j)=
      routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0)
    (hcover : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z)
    (x y : Vec) : ∃k q,routeVec (word k) q x=y := by
  let z := encodeVec (y-routeVec reference 0 x)
  let k := choice z
  refine ⟨k,alpha z-combine (column k) x,?_⟩
  rw [route_decompose,route_noise_sub,column_translation reference (word k) (column k) (hcol k) x]
  have hc : routeVec (word k) (alpha z) 0=y-routeVec reference 0 x := by
    simpa only [k,z,decodeVec_encodeVec] using hcover z
  rw [hc]
  abel
theorem inverse_basis_solution (word : List (Fin 5)) (inverseBasis : Fin 4 → Vec)
    (h : ∀j,routeVec word (inverseBasis j) 0=basisVec j) (x y : Vec) :
    ∃q,routeVec word q x=y := by
  let z := y-routeVec word 0 x
  have hz : routeVec word (combine inverseBasis z) 0=z := by
    rw [route_noise_combine,h 0,h 1,h 2,h 3]
    exact (vec_basis z).symm
  refine ⟨combine inverseBasis z,?_⟩
  rw [route_decompose,hz]
  dsimp [z]
  abel
#print axioms affine_coset_solve
#print axioms coset_solution
#print axioms inverse_basis_solution
end DegreeDiameter.Portfolio.F3Graph15552
