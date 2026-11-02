import DegreeDiameter.Portfolio.F3Graph15552Routes
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def pivot : Fin 5 → Fin 4 := ![0,0,1,0,0]
theorem direction_pivot : ∀p,direction p (pivot p)=1 := by decide +kernel
theorem inverse_basis : ∀p j,
    act (matrix (inverseType p)) (act (matrix p) (basisVec j))=
      basisVec j-(basisVec j) (pivot (inverseType p)) • direction (inverseType p) := by decide +kernel
theorem inverse_direction : ∀p,act (matrix (inverseType p)) (direction p)=0 := by decide +kernel
theorem linear_map_ext (f g : Vec → Vec)
    (fadd : ∀x y,f (x+y)=f x+f y) (gadd : ∀x y,g (x+y)=g x+g y)
    (fsmul : ∀(t : F) x,f (t • x)=t • f x) (gsmul : ∀(t : F) x,g (t • x)=t • g x)
    (hbasis : ∀j,f (basisVec j)=g (basisVec j)) (x : Vec) : f x=g x := by
  conv_lhs => rw [vec_basis x]
  conv_rhs => rw [vec_basis x]
  simp only [fadd,gadd,fsmul,gsmul,hbasis]
theorem inverse_action (p : Fin 5) (x : Vec) :
    act (matrix (inverseType p)) (act (matrix p) x)=
      x-x (pivot (inverseType p)) • direction (inverseType p) := by
  refine linear_map_ext
    (fun u => act (matrix (inverseType p)) (act (matrix p) u))
    (fun u => u-u (pivot (inverseType p)) • direction (inverseType p))
    ?_ ?_ ?_ ?_ (inverse_basis p) x
  · intro u v
    simp only [act_add]
  · intro u v
    funext i
    simp only [Pi.add_apply,Pi.sub_apply,Pi.smul_apply,smul_eq_mul]
    ring
  · intro t u
    simp only [act_smul]
  · intro t u
    funext i
    simp only [Pi.add_apply,Pi.sub_apply,Pi.smul_apply,smul_eq_mul]
    ring
theorem stepVec_reverse (p : Fin 5) (t : F) (x : Vec) :
    stepVec (inverseType p) (x (pivot (inverseType p))) (stepVec p t x)=x := by
  rw [stepVec_eq,stepVec_eq,act_add,act_smul,inverse_action,inverse_direction]
  funext i
  simp only [Pi.add_apply,Pi.sub_apply,Pi.smul_apply,Pi.zero_apply,smul_eq_mul,mul_zero]
  ring
theorem forward_reverse_liftAt (a : Fin 192) (x : Vec) (p : Fin 5) (t : F) :
    forward (forward (liftAt a (encodeVec x)) p t) (inverseType p)
      (x (pivot (inverseType p)))=liftAt a (encodeVec x) := by
  rw [forward_liftAt,forward_liftAt,controller_reverse_type,stepVec_reverse]
theorem forward_reverse (u : Fin 15552) (p : Fin 5) (t : F) :
    forward (forward u p t) (inverseType p)
      ((decodeVec (fiberOf u)) (pivot (inverseType p)))=u := by
  simpa only [encodeVec_decodeVec,liftAt_parts] using
    forward_reverse_liftAt (controllerOf u) (decodeVec (fiberOf u)) p t
theorem adj_iff_forward (u v : Fin 15552) :
    graph.Adj u v ↔ u≠v ∧ ∃p t,forward u p t=v := by
  constructor
  · rintro ⟨hne,hf|hr⟩
    · exact ⟨hne,hf⟩
    · obtain ⟨p,t,hp⟩ := hr
      have hrev := forward_reverse v p t
      rw [hp] at hrev
      exact ⟨hne,inverseType p,(decodeVec (fiberOf v)) (pivot (inverseType p)),hrev⟩
  · rintro ⟨hne,p,t,hp⟩
    exact ⟨hne,Or.inl ⟨p,t,hp⟩⟩
theorem degree_le_fifteen (u : Fin 15552) : graph.degree u≤15 := by
  rw [← SimpleGraph.card_neighborFinset_eq_degree]
  calc
    (graph.neighborFinset u).card ≤
        (Finset.univ.image (fun pt : Fin 5 × F => forward u pt.1 pt.2)).card := by
      apply Finset.card_le_card
      intro v hv
      have ha : graph.Adj u v := by simpa only [SimpleGraph.mem_neighborFinset] using hv
      obtain ⟨_,p,t,hp⟩ := (adj_iff_forward u v).mp ha
      exact Finset.mem_image.mpr ⟨(p,t),Finset.mem_univ _,hp⟩
    _ ≤ (Finset.univ : Finset (Fin 5 × F)).card := Finset.card_image_le
    _ = 15 := by decide +kernel
theorem forward_noise_injective (u : Fin 15552) (p : Fin 5) (t s : F)
    (h : forward u p t=forward u p s) : t=s := by
  have hc := congrArg (fun v => decodeVec (fiberOf v) (pivot p)) h
  simp only [forward,fiberOf_liftAt,decodeVec_encodeVec,stepVec_eq,
    Pi.add_apply,Pi.smul_apply,smul_eq_mul,direction_pivot,mul_one] at hc
  exact add_left_cancel hc
theorem source_no_isolated (u : Fin 15552) : ∃v,graph.Adj u v := by
  classical
  by_cases h : u≠forward u 0 0
  · exact ⟨forward u 0 0,forward_adj_of_ne u 0 0 h⟩
  · have heq : u=forward u 0 0 := Classical.not_not.mp h
    refine ⟨forward u 0 1,forward_adj_of_ne u 0 1 ?_⟩
    intro h1
    have hz : (0 : F)=1 := forward_noise_injective u 0 0 1 (heq.symm.trans h1)
    exact zero_ne_one hz
#print axioms degree_le_fifteen
#print axioms source_no_isolated
#print axioms inverse_action
end DegreeDiameter.Portfolio.F3Graph15552
