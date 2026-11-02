import DegreeDiameter.Portfolio.F9PlaneClone55Definitions

namespace DegreeDiameter.Portfolio.F9PlaneClone55
open F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

def pinInverse : Fin 6 → Mat := ![![![F.c0, F.c5, F.c0], ![F.c0, F.c0, F.c1], ![F.c1, F.c2, F.c0]], ![![F.c0, F.c5, F.c0], ![F.c4, F.c0, F.c0], ![F.c0, F.c7, F.c1]], ![![F.c7, F.c5, F.c7], ![F.c0, F.c6, F.c6], ![F.c3, F.c7, F.c5]], ![![F.c2, F.c2, F.c2], ![F.c0, F.c7, F.c5], ![F.c2, F.c1, F.c1]], ![![F.c1, F.c6, F.c2], ![F.c1, F.c3, F.c0], ![F.c0, F.c3, F.c1]], ![![F.c5, F.c8, F.c7], ![F.c6, F.c8, F.c2], ![F.c8, F.c4, F.c5]]]

theorem plane_add (x y : Vec) : plane (x+y) = plane x + plane y := by
  funext i
  fin_cases i <;> simp [plane,mul_add]

theorem plane_smul (t : F) (x : Vec) : plane (t • x) = t • plane x := by
  funext i
  fin_cases i <;> simp [plane,smul_eq_mul,mul_left_comm]

theorem pinMap_add (p : Fin 6) (x y : Vec) : pinMap p (x+y) = pinMap p x + pinMap p y := by
  simp only [pinMap,Pi.add_apply,plane_add,stepVec_joint_add]

theorem pinMap_smul (p : Fin 6) (t : F) (x : Vec) : pinMap p (t • x) = t • pinMap p x := by
  simp only [pinMap,Pi.smul_apply,smul_eq_mul,plane_smul,stepVec_joint_smul]

/-- Eighteen basis checks, not4374 coordinate checks. -/
theorem pinInverse_basis : ∀ (p : Fin 6) (j : Fin 3),
    act (pinInverse p) (pinMap p (basisVec j)) = basisVec j := by decide +kernel

theorem pinInverse_left (p : Fin 6) (x : Vec) : act (pinInverse p) (pinMap p x) = x := by
  have h := additive_ext (fun x => act (pinInverse p) (pinMap p x)) id
    (by intro x y; dsimp only; rw [pinMap_add,act_add]) (by intros; rfl)
    (by intro t x; dsimp only; rw [pinMap_smul,act_smul]) (by intros; rfl)
    (pinInverse_basis p)
  exact congrFun h x

theorem pinMap_injective (p : Fin 6) : Function.Injective (pinMap p) := by
  intro x y h
  have h' := congrArg (act (pinInverse p)) h
  simpa only [pinInverse_left] using h'

theorem controller_zero_injective : Function.Injective (controller 0) := by decide +kernel

theorem plane_parameters_zero (i : CloneIndex) (t : F) :
    plane (parameters i t) = plane (parameters i 0) := rfl

theorem forward_center (i : CloneIndex) (p : Fin 6) (t : F) :
    forward (center i) p t = liftAt (controller 0 p) (encodeVec (pinMap p (parameters i t))) := by
  simp only [center,forward_liftAt,fiberStep,decodeVec_encodeVec,pinMap,
    plane_parameters_zero]
  rfl

theorem parameters_index_unique (i j : CloneIndex) (s t : F)
    (h : parameters i s = parameters j t) : i = j := by
  have ha := congrArg (fun x : Vec => F.code (x 0)) h
  have hb := congrArg (fun x : Vec => F.code (x 1)) h
  change F.code (F.ofCode (clonePair i).1.val) = F.code (F.ofCode (clonePair j).1.val) at ha
  change F.code (F.ofCode (clonePair i).2.val) = F.code (F.ofCode (clonePair j).2.val) at hb
  simp only [F.code_ofCode] at ha hb
  apply clonePair.injective
  exact Prod.ext (Fin.ext ha) (Fin.ext hb)

theorem common_pin_index_unique (w : Fin 56862) (i j : CloneIndex)
    (hi : F9Graph56862.graph.Adj w (center i))
    (hj : F9Graph56862.graph.Adj w (center j)) : i = j := by
  obtain ⟨p,s,hp⟩ := (adj_iff_forward _ _).mp (F9Graph56862.graph.symm hi)
  obtain ⟨q,t,hq⟩ := (adj_iff_forward _ _).mp (F9Graph56862.graph.symm hj)
  have heq : forward (center i) p s = forward (center j) q t := hp.trans hq.symm
  have hc := congrArg controllerOf heq
  simp only [forward_center,controllerOf_liftAt] at hc
  have hpq : p = q := controller_zero_injective hc
  subst q
  have hf := congrArg (fun v => decodeVec (fiberOf v)) heq
  simp only [forward_center,fiberOf_liftAt,decodeVec_encodeVec] at hf
  exact parameters_index_unique i j s t (pinMap_injective p hf)

theorem load_le_one (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph center w ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_pin_index_unique w x.val y.val x.property y.property

#print axioms pinInverse_basis
#print axioms pinInverse_left
#print axioms load_le_one
end DegreeDiameter.Portfolio.F9PlaneClone55
