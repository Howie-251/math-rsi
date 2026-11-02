import DegreeDiameter.Portfolio.F4Graph1920Routes

namespace DegreeDiameter.Portfolio.F4Graph1920.Clone2016
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

/-- The 24 target controller layers identify the selected source layer and
port.  Default values at the six unused layers are immaterial. -/
def targetLayer : Fin 30 → Fin 6 := ![4, 1, 0, 2, 0, 1, 5, 5, 0, 0, 0, 5, 2, 3, 4, 2, 3, 1, 0, 4, 0, 1, 4, 0, 0, 3, 5, 3, 0, 2]
def targetPort : Fin 30 → Fin 4 := ![2, 3, 2, 3, 0, 2, 2, 1, 0, 3, 0, 3, 2, 3, 3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0]

theorem targetLayer_forward : ∀ (i : Fin 6) (p : Fin 4),
    targetLayer (controller (layer i) p) = i := by decide

theorem targetPort_forward : ∀ (i : Fin 6) (p : Fin 4),
    targetPort (controller (layer i) p) = p := by decide

/-- Normal111 for the actual characteristic-two transverse plane. -/
def pinNormal (x : Vec) : F := x 0 + x 1 + x 2

theorem pinNormal_add (x y : Vec) : pinNormal (x+y) = pinNormal x + pinNormal y := by
  simp only [pinNormal, Pi.add_apply]
  abel

theorem pinNormal_smul (t : F) (x : Vec) : pinNormal (t • x) = t * pinNormal x := by
  simp only [pinNormal, Pi.smul_apply, smul_eq_mul]
  ring

theorem pinNormal_plane (a b : Fin 4) : pinNormal (planeVec a b) = 0 := by
  change (F.ofCode a.val + F.ofCode b.val) +
    (F.ofCode a.val + F.ofCode b.val) = 0
  exact add_neg_cancel _

/-- Four actual direction values, not a field-law or old rank recheck. -/
theorem pinNormal_direction : ∀ p : Fin 4, pinNormal (direction p) = 1 := by decide

def pinProject (p : Fin 4) (z : Vec) : Vec := z + pinNormal z • direction p

/-- Symbolic in the plane coordinates and noise: no1536-coordinate table. -/
theorem pinProject_plane_noise (p : Fin 4) (a b : Fin 4) (t : F) :
    pinProject p (planeVec a b + t • direction p) = planeVec a b := by
  simp only [pinProject, pinNormal_add, pinNormal_plane, pinNormal_smul,
    pinNormal_direction, zero_add, mul_one]
  rw [add_assoc, ← add_smul]
  have ht : t+t=0 := add_neg_cancel t
  rw [ht, zero_smul, add_zero]

def cloneBlock (j : Fin 96) : Fin 6 := ⟨j.val/16, by have h:=j.isLt; omega⟩
def cloneA (j : Fin 96) : Fin 4 := ⟨j.val/4%4,Nat.mod_lt _ (by decide)⟩
def cloneB (j : Fin 96) : Fin 4 := ⟨j.val%4,Nat.mod_lt _ (by decide)⟩

theorem center_eq_parts (j : Fin 96) : center j =
    liftAt (layer (cloneBlock j)) (encodeVec (planeVec (cloneA j) (cloneB j))) := rfl

def makeIndex (i : Fin 6) (a b : F) : Fin 96 :=
  ⟨16*i.val+4*F.code a+F.code b, by
    have hi:=i.isLt; have ha:=F.code_lt a; have hb:=F.code_lt b
    omega⟩

theorem makeIndex_reassemble (j : Fin 96) :
    makeIndex (cloneBlock j) ((planeVec (cloneA j) (cloneB j)) 0)
      ((planeVec (cloneA j) (cloneB j)) 1) = j := by
  apply Fin.ext
  change 16*(cloneBlock j).val + 4*F.code (F.ofCode (cloneA j).val) +
    F.code (F.ofCode (cloneB j).val) = j.val
  rw [F.code_ofCode (cloneA j), F.code_ofCode (cloneB j)]
  simp only [cloneBlock,cloneA,cloneB]
  have hj:=j.isLt
  omega

/-- Use the inherited true reverse matrix, then remove the one noise
coordinate by the transverse-plane normal. -/
def pinCoordinates (v : Fin 1920) : Vec :=
  pinProject (targetPort (controllerOf v))
    (act (matrix (controllerOf v) (inversePort (targetPort (controllerOf v))))
      (decodeVec (fiberOf v)))

def pinOwner (v : Fin 1920) : Fin 96 :=
  makeIndex (targetLayer (controllerOf v)) ((pinCoordinates v) 0) ((pinCoordinates v) 1)

theorem pinOwner_forward (j : Fin 96) (p : Fin 4) (t : F) :
    pinOwner (forward (center j) p t) = j := by
  let i := cloneBlock j
  let a := cloneA j
  let b := cloneB j
  have hcenter : center j = liftAt (layer i) (encodeVec (planeVec a b)) := rfl
  have hc : controllerOf (forward (center j) p t) = controller (layer i) p := by
    rw [hcenter, forward_liftAt, controllerOf_liftAt]
  have hf : decodeVec (fiberOf (forward (center j) p t)) =
      stepVec (layer i) p t (planeVec a b) := by
    rw [hcenter, forward_liftAt, fiberOf_liftAt]
    simp only [fiberStep, decodeVec_encodeVec]
  have hi : targetLayer (controllerOf (forward (center j) p t)) = i := by
    simp only [hc, targetLayer_forward]
  have hcoordinates : pinCoordinates (forward (center j) p t) = planeVec a b := by
    simp only [pinCoordinates, hc, targetPort_forward, hf]
    simp only [stepVec, act_add, act_smul, act_reverse, inverse_direction]
    exact pinProject_plane_noise p a b t
  calc
    pinOwner (forward (center j) p t) =
        makeIndex i ((planeVec a b) 0) ((planeVec a b) 1) := by
          simp only [pinOwner, hi, hcoordinates]
    _ = j := makeIndex_reassemble j

theorem common_pin_index_unique (v : Fin 1920) (i j : Fin 96)
    (hi : F4Graph1920.graph.Adj v (center i))
    (hj : F4Graph1920.graph.Adj v (center j)) : i = j := by
  obtain ⟨p,s,hp⟩ := (adj_iff_forward _ _).mp (F4Graph1920.graph.symm hi)
  obtain ⟨q,t,hq⟩ := (adj_iff_forward _ _).mp (F4Graph1920.graph.symm hj)
  have h := congrArg pinOwner (hp.trans hq.symm)
  simpa only [pinOwner_forward] using h

theorem load_le_one (v : Fin 1920) :
    FullNeighborhoodClones.load F4Graph1920.graph center v ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_pin_index_unique v x.val y.val x.property y.property

#print axioms pinOwner_forward
#print axioms load_le_one
end DegreeDiameter.Portfolio.F4Graph1920.Clone2016
