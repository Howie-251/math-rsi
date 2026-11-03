import DegreeDiameter.Portfolio.F4PlaneBlockClonesDefinitions
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

theorem form_add (x y : Vec) : form (x+y) = form x + form y := by
  simp only [form,Pi.add_apply]
  ring

theorem form_smul (t : F) (x : Vec) : form (t • x) = t * form x := by
  simp only [form,Pi.smul_apply,smul_eq_mul]
  ring

theorem form_step (a : Fin 60) (p : Fin 5) (t : F) (x : Vec) :
  form (stepVec a p t x) = form (act (matrix a p) x) + t * form (direction (inversePort p)) := by
  rw [stepVec,form_add,form_smul]

theorem direction_transverse : ∀ p : Fin 5, form (direction p) ≠ 0 := by decide +kernel

theorem mul_cancel_nonzero : ∀ (d t s : F), d ≠ 0 → t*d=s*d → t=s := by decide +kernel

theorem step_plane_noise_unique (a : Fin 60) (p : Fin 5) (x : Vec) (t s : F)
  (ht : form (stepVec a p t x) = 0) (hs : form (stepVec a p s x) = 0) : t=s := by
  have h := ht.trans hs.symm
  rw [form_step,form_step] at h
  exact mul_cancel_nonzero _ _ _ (direction_transverse _) (add_left_cancel h)

theorem plane_member : ∀ i : Fin 16, form (decodeVec (planeCode i)) = 0 := by decide +kernel

theorem planeCode_injective : Function.Injective planeCode := by decide +kernel

theorem controller_ports_injective : ∀ (a : Fin 60) (p q : Fin 5),
  controller a p = controller a q → p=q := by decide +kernel

/-- A source vertex has at most one neighbor among the16centers of any fixed plane block. -/
theorem plane_neighbor_unique (v : Fin 3840) (a : Fin 60) (i j : Fin 16)
    (hi : F4Graph3840.graph.Adj v (liftAt a (planeCode i)))
    (hj : F4Graph3840.graph.Adj v (liftAt a (planeCode j))) : i=j := by
  obtain ⟨p,t,hp⟩ := (adj_iff_forward _ _).mp hi
  obtain ⟨q,s,hq⟩ := (adj_iff_forward _ _).mp hj
  have hpc := congrArg controllerOf hp
  have hqc := congrArg controllerOf hq
  simp only [forward,controllerOf_liftAt] at hpc hqc
  have hpq := controller_ports_injective (controllerOf v) p q (hpc.trans hqc.symm)
  subst q
  have hpf := congrArg fiberOf hp
  have hqf := congrArg fiberOf hq
  simp only [forward,fiberOf_liftAt,fiberStep] at hpf hqf
  have hpv := congrArg decodeVec hpf
  have hqv := congrArg decodeVec hqf
  simp only [decodeVec_encodeVec] at hpv hqv
  have ht : form (stepVec (controllerOf v) p t (decodeVec (fiberOf v))) = 0 := by rw [hpv]; exact plane_member i
  have hs : form (stepVec (controllerOf v) p s (decodeVec (fiberOf v))) = 0 := by rw [hqv]; exact plane_member j
  have hts := step_plane_noise_unique _ _ _ _ _ ht hs
  subst s
  apply planeCode_injective
  exact hpf.symm.trans hqf

#print axioms plane_neighbor_unique
end DegreeDiameter.Portfolio.F4PlaneBlockClones
