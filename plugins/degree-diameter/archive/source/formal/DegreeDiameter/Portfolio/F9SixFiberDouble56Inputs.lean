import DegreeDiameter.Portfolio.F9SixFiberDouble56Definitions
import DegreeDiameter.Portfolio.F9PlaneClone55Inputs
namespace DegreeDiameter.Portfolio.F9SixFiberDouble56
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem selected_charts_same_zero : ∀ (i : Fin 6) (p : Fin 6),
    chart (chosenFiber i) p = chart 0 p := by decide +kernel
theorem controller_targets_injective : Function.Injective
    (fun ip : Fin 6 × Fin 6 => controller (chosenFiber ip.1) ip.2) := by decide +kernel

def sourcePlaneMap (a : Fin 78) (p : Fin 6) (x : Vec) : Vec :=
  stepVec a p (x 2) (F9PlaneClone55.plane x)

theorem sourcePlaneMap_injective (a : Fin 78) (p : Fin 6) : Function.Injective (sourcePlaneMap a p) := by
  intro x y h
  have hr := congrArg (act (matrix (controller a p) (inversePort p))) h
  simp only [sourcePlaneMap,stepVec,act_add,act_smul,act_reverse,inverse_direction] at hr
  have hz := congrArg (act (matrix 0 p)) hr
  have hd := inverse_direction (controller 0 p) (inversePort p)
  simp only [controller_reverse,inversePort_involution] at hd
  apply F9PlaneClone55.pinMap_injective p
  simpa only [F9PlaneClone55.pinMap,stepVec,act_add,act_smul,hd] using hz

theorem forward_planeCenter {I : Type*} (fibers : I → Fin 78)
    (i : I × Fin 81) (p : Fin 6) (t : F) :
    forward (planeCenter fibers i) p t =
      liftAt (controller (fibers i.1) p)
        (encodeVec (sourcePlaneMap (fibers i.1) p (F9PlaneClone55.parameters i.2 t))) := by
  simp only [planeCenter,forward_liftAt,fiberStep,decodeVec_encodeVec,
    sourcePlaneMap,F9PlaneClone55.plane_parameters_zero]
  rfl

/-- Existing single-plane inverse maps plus a controller target injection distinguish all owners. -/
theorem common_plane_pin_index_unique {I : Type*} (fibers : I → Fin 78)
    (ht : Function.Injective (fun ip : I × Fin 6 => controller (fibers ip.1) ip.2))
    (w : Fin 56862) (i j : I × Fin 81)
    (hi : F9Graph56862.graph.Adj w (planeCenter fibers i))
    (hj : F9Graph56862.graph.Adj w (planeCenter fibers j)) : i = j := by
  obtain ⟨p,s,hp⟩ := (adj_iff_forward _ _).mp (F9Graph56862.graph.symm hi)
  obtain ⟨q,t,hq⟩ := (adj_iff_forward _ _).mp (F9Graph56862.graph.symm hj)
  have heq : forward (planeCenter fibers i) p s = forward (planeCenter fibers j) q t := hp.trans hq.symm
  have htarget := congrArg controllerOf heq
  simp only [forward_planeCenter fibers,controllerOf_liftAt] at htarget
  have hpair : (i.1,p) = (j.1,q) := ht htarget
  have hfirst : i.1 = j.1 := congrArg (fun z : I × Fin 6 => z.1) hpair
  have hpq : p = q := congrArg (fun z : I × Fin 6 => z.2) hpair
  subst q
  have hf := congrArg (fun v => decodeVec (fiberOf v)) heq
  simp only [forward_planeCenter fibers,fiberOf_liftAt,decodeVec_encodeVec] at hf
  have hfibers : fibers i.1 = fibers j.1 := congrArg fibers hfirst
  rw [← hfibers] at hf
  have hsecond := F9PlaneClone55.parameters_index_unique i.2 j.2 s t
    (sourcePlaneMap_injective (fibers i.1) p hf)
  exact Prod.ext hfirst hsecond

theorem common_base_pin_index_unique (w : Fin 56862) (i j : BaseIndex)
    (hi : F9Graph56862.graph.Adj w (baseCenter i))
    (hj : F9Graph56862.graph.Adj w (baseCenter j)) : i = j := by
  apply basePair.injective
  exact common_plane_pin_index_unique chosenFiber controller_targets_injective
    w (basePair i) (basePair j) hi hj
theorem base_load_le_one (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph baseCenter w ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_base_pin_index_unique w x.val y.val x.property y.property
theorem load_le_two (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph center w ≤ 2 := by
  have hbase : ∀ x y : {b : BaseIndex // F9Graph56862.graph.Adj w (baseCenter b)}, x = y :=
    Fintype.card_le_one_iff.mp (base_load_le_one w)
  let copyIndex : {k : CloneIndex // F9Graph56862.graph.Adj w (center k)} → Fin 2 := fun k => (clonePair k.val).1
  have hinj : Function.Injective copyIndex := by
    intro x y hcopy
    have hbaseval : (clonePair x.val).2 = (clonePair y.val).2 :=
      congrArg Subtype.val (hbase ⟨(clonePair x.val).2,x.property⟩ ⟨(clonePair y.val).2,y.property⟩)
    apply Subtype.ext
    apply clonePair.injective
    exact Prod.ext hcopy hbaseval
  have h := Fintype.card_le_of_injective copyIndex hinj
  simpa only [Fintype.card_fin] using h
#print axioms common_plane_pin_index_unique
#print axioms sourcePlaneMap_injective
#print axioms base_load_le_one
#print axioms load_le_two
end DegreeDiameter.Portfolio.F9SixFiberDouble56
