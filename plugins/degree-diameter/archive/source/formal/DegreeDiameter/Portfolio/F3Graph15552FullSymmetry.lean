import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryCertificate0
import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryCertificate1
import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryCoverage
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

def generatorEquiv : Fin 2 → Equiv.Perm (Fin 192) := ![
  { toFun := gen0, invFun := inv0, left_inv := gen0_left_inverse, right_inv := gen0_right_inverse },
  { toFun := gen1, invFun := inv1, left_inv := gen1_left_inverse, right_inv := gen1_right_inverse }]
theorem generatorEquiv_apply (i : Fin 2) (a : Fin 192) : generatorEquiv i a=generator i a := by
  fin_cases i <;> rfl
theorem generatorEquiv_commutes (i : Fin 2) (a : Fin 192) (p : Fin 5) :
    generatorEquiv i (controller a p)=controller (generatorEquiv i a) p := by
  fin_cases i
  · exact gen0_commutes a p
  · exact gen1_commutes a p
def wordEquiv : List (Fin 2) → Equiv.Perm (Fin 192)
  | [] => Equiv.refl _
  | i::is => (generatorEquiv i).trans (wordEquiv is)
theorem wordEquiv_apply (word : List (Fin 2)) (a : Fin 192) :
    wordEquiv word a=wordController a word := by
  induction word generalizing a with
  | nil => rfl
  | cons i is ih =>
      change wordEquiv is (generatorEquiv i a)=wordController (generator i a) is
      rw [ih,generatorEquiv_apply]
theorem wordEquiv_commutes (word : List (Fin 2)) (a : Fin 192) (p : Fin 5) :
    wordEquiv word (controller a p)=controller (wordEquiv word a) p := by
  induction word generalizing a with
  | nil => rfl
  | cons i is ih =>
      change wordEquiv is (generatorEquiv i (controller a p))=
        controller (wordEquiv is (generatorEquiv i a)) p
      rw [generatorEquiv_commutes,ih]

def relabelEquiv (sigma : Equiv.Perm (Fin 192)) : Equiv.Perm (Fin 15552) where
  toFun u := liftAt (sigma (controllerOf u)) (fiberOf u)
  invFun u := liftAt (sigma.symm (controllerOf u)) (fiberOf u)
  left_inv := by
    intro u
    simp only [controllerOf_liftAt,fiberOf_liftAt,Equiv.symm_apply_apply,liftAt_parts]
  right_inv := by
    intro u
    simp only [controllerOf_liftAt,fiberOf_liftAt,Equiv.apply_symm_apply,liftAt_parts]
theorem relabel_liftAt (sigma : Equiv.Perm (Fin 192)) (a : Fin 192) (x : Fin 81) :
    relabelEquiv sigma (liftAt a x)=liftAt (sigma a) x := by
  change liftAt (sigma (controllerOf (liftAt a x))) (fiberOf (liftAt a x))=liftAt (sigma a) x
  rw [controllerOf_liftAt,fiberOf_liftAt]
theorem relabel_controllerOf (sigma : Equiv.Perm (Fin 192)) (u : Fin 15552) :
    controllerOf (relabelEquiv sigma u)=sigma (controllerOf u) :=
  controllerOf_liftAt _ _
theorem relabel_fiberOf (sigma : Equiv.Perm (Fin 192)) (u : Fin 15552) :
    fiberOf (relabelEquiv sigma u)=fiberOf u := fiberOf_liftAt _ _
theorem relabel_forward (sigma : Equiv.Perm (Fin 192))
    (hcomm : ∀a p,sigma (controller a p)=controller (sigma a) p)
    (u : Fin 15552) (p : Fin 5) (t : F) :
    relabelEquiv sigma (forward u p t)=forward (relabelEquiv sigma u) p t := by
  simp only [forward,relabel_liftAt,relabel_controllerOf,relabel_fiberOf,hcomm]
def relabelHom (sigma : Equiv.Perm (Fin 192))
    (hcomm : ∀a p,sigma (controller a p)=controller (sigma a) p) : graph →g graph where
  toFun := relabelEquiv sigma
  map_rel' := by
    intro u v h
    refine ⟨fun he => h.1 ((relabelEquiv sigma).injective he),?_⟩
    rcases h.2 with ⟨p,t,hf⟩|⟨p,t,hf⟩
    · left
      refine ⟨p,t,?_⟩
      rw [← relabel_forward sigma hcomm,hf]
    · right
      refine ⟨p,t,?_⟩
      rw [← relabel_forward sigma hcomm,hf]

def RepresentativeRowBound (i : Fin 8) : Prop := ∀(x : Fin 81)(v : Fin 15552),
  ∃w : graph.Walk (liftAt (representatives i) x) v,w.length≤4
theorem diameterAtMost_of_representatives (rows : ∀i,RepresentativeRowBound i) :
    DiameterAtMost graph 4 := by
  intro u v
  let a := controllerOf u
  let i := representativeIndex a
  let word := transportWord a
  let sigma := wordEquiv word
  have hc : ∀c p,sigma (controller c p)=controller (sigma c) p := wordEquiv_commutes word
  obtain ⟨w,hw⟩ := rows i (fiberOf u) ((relabelEquiv sigma).symm v)
  have hm : ∃q : graph.Walk
      (relabelEquiv sigma (liftAt (representatives i) (fiberOf u)))
      (relabelEquiv sigma ((relabelEquiv sigma).symm v)),q.length≤4 :=
    ⟨w.map (relabelHom sigma hc),by simpa only [SimpleGraph.Walk.length_map] using hw⟩
  have hcov : sigma (representatives i)=a := by
    change wordEquiv (transportWord a) (representatives (representativeIndex a))=a
    rw [wordEquiv_apply]
    exact controller_coverage a
  have hs : relabelEquiv sigma (liftAt (representatives i) (fiberOf u))=u := by
    rw [relabel_liftAt,hcov]
    exact liftAt_parts u
  have ht : relabelEquiv sigma ((relabelEquiv sigma).symm v)=v :=
    (relabelEquiv sigma).apply_symm_apply v
  have hm' : ∃q : graph.Walk u
      (relabelEquiv sigma ((relabelEquiv sigma).symm v)),q.length≤4 := hs ▸ hm
  exact ht ▸ hm'
#print axioms diameterAtMost_of_representatives
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
