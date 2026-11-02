import DegreeDiameter.Portfolio.F4Graph3840Field
import DegreeDiameter.Portfolio.FullNeighborhoodClones
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.F4Graph1920
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def controllerData : Array (Array Nat) := #[#[18, 20, 2, 9], #[13, 2, 3, 17], #[1, 18, 11, 0], #[17, 21, 5, 1], #[10, 25, 18, 8], #[29, 15, 12, 3], #[15, 22, 21, 16], #[16, 27, 25, 13], #[21, 10, 4, 12], #[22, 19, 0, 14], #[8, 4, 19, 24], #[23, 26, 16, 2], #[28, 23, 8, 5], #[25, 1, 7, 23], #[19, 29, 9, 25], #[5, 6, 27, 29], #[26, 7, 6, 11], #[24, 3, 1, 26], #[2, 0, 29, 4], #[9, 14, 26, 10], #[0, 28, 24, 27], #[3, 8, 22, 6], #[6, 9, 28, 21], #[12, 11, 13, 28], #[27, 17, 10, 20], #[4, 13, 14, 7], #[11, 16, 17, 19], #[7, 24, 20, 15], #[20, 12, 23, 22], #[14, 5, 15, 18]]
def matrixPool : Array (Array Nat) := #[#[0, 1, 2, 1, 0, 0, 0, 1, 3], #[0, 1, 0, 1, 0, 1, 2, 0, 3], #[1, 2, 1, 2, 0, 1, 0, 0, 1], #[1, 2, 3, 1, 3, 2, 0, 0, 1], #[0, 1, 1, 1, 0, 0, 0, 2, 3], #[0, 1, 0, 1, 0, 2, 0, 0, 1], #[1, 2, 1, 3, 2, 1, 0, 0, 1], #[1, 2, 3, 3, 2, 1, 0, 0, 1], #[0, 1, 2, 1, 0, 0, 0, 0, 1], #[1, 1, 1, 2, 3, 1, 0, 0, 1], #[0, 3, 3, 3, 2, 1, 0, 0, 1], #[0, 1, 2, 1, 0, 0, 0, 2, 1], #[0, 1, 0, 1, 0, 0, 2, 0, 1], #[3, 3, 0, 1, 2, 3, 0, 0, 1], #[0, 0, 1, 1, 0, 0, 0, 1, 2], #[1, 0, 1, 2, 1, 1, 0, 0, 1], #[1, 2, 1, 3, 3, 1, 0, 0, 1], #[0, 1, 0, 1, 0, 2, 3, 0, 3], #[1, 2, 3, 3, 3, 0, 0, 0, 1], #[0, 1, 0, 1, 0, 2, 2, 0, 1], #[3, 3, 1, 1, 2, 1, 0, 0, 1], #[1, 2, 3, 2, 0, 2, 0, 0, 1], #[0, 1, 0, 1, 0, 2, 3, 0, 2], #[3, 2, 1, 1, 1, 1, 0, 0, 1], #[0, 1, 1, 1, 2, 3, 0, 0, 1], #[0, 3, 1, 1, 0, 0, 0, 1, 3], #[0, 1, 0, 2, 0, 1, 1, 0, 0], #[0, 1, 1, 1, 2, 1, 0, 0, 1], #[3, 1, 2, 2, 1, 3, 0, 0, 1], #[0, 1, 2, 1, 0, 0, 0, 2, 0], #[0, 3, 1, 3, 2, 1, 0, 0, 1], #[2, 1, 3, 2, 3, 1, 0, 0, 1], #[0, 1, 2, 1, 0, 0, 0, 3, 3], #[0, 1, 0, 3, 0, 1, 2, 0, 1], #[0, 1, 0, 1, 0, 2, 1, 0, 3], #[2, 1, 1, 1, 0, 1, 0, 0, 1], #[0, 3, 1, 1, 0, 0, 0, 2, 1], #[2, 1, 1, 2, 3, 1, 0, 0, 1], #[2, 1, 3, 1, 0, 1, 0, 0, 1], #[0, 1, 0, 3, 0, 1, 1, 0, 3], #[0, 1, 0, 3, 0, 2, 1, 0, 1], #[1, 0, 1, 2, 1, 3, 0, 0, 1], #[0, 3, 3, 1, 0, 0, 0, 1, 2], #[1, 2, 1, 0, 1, 1, 0, 0, 1], #[0, 1, 0, 0, 0, 1, 1, 0, 2], #[1, 2, 1, 1, 3, 1, 0, 0, 1], #[0, 1, 0, 1, 0, 0, 0, 2, 1], #[0, 2, 1, 1, 0, 0, 0, 2, 3], #[1, 2, 3, 0, 1, 1, 0, 0, 1], #[0, 1, 0, 0, 0, 3, 3, 0, 2], #[3, 2, 1, 1, 1, 0, 0, 0, 1], #[0, 1, 0, 2, 0, 1, 2, 0, 3], #[0, 2, 1, 1, 0, 0, 0, 1, 0], #[0, 3, 2, 1, 0, 0, 0, 1, 1]]
def matrixIndex : Array (Array Nat) := #[#[0, 1, 2, 3], #[4, 5, 6, 7], #[8, 1, 9, 10], #[11, 12, 6, 13], #[14, 1, 15, 7], #[4, 1, 16, 13], #[8, 17, 15, 18], #[8, 17, 6, 3], #[11, 19, 20, 21], #[8, 22, 23, 24], #[25, 26, 15, 24], #[14, 19, 27, 28], #[29, 22, 30, 31], #[32, 33, 23, 21], #[11, 34, 35, 18], #[36, 5, 6, 21], #[4, 5, 37, 38], #[29, 39, 20, 18], #[36, 40, 2, 41], #[42, 39, 43, 41], #[36, 44, 45, 21], #[46, 39, 43, 41], #[47, 5, 45, 48], #[42, 26, 30, 18], #[29, 49, 35, 50], #[36, 51, 37, 13], #[25, 33, 37, 48], #[47, 49, 30, 13], #[52, 49, 37, 50], #[53, 33, 30, 10]]
def directionData : Array (Array Nat) := #[#[1, 0, 0], #[0, 1, 0], #[0, 0, 1], #[1, 1, 1]]
def controller (a : Fin 30) (p : Fin 4) : Fin 30 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 % 30, Nat.mod_lt _ (by decide)⟩
def inversePort : Fin 4 → Fin 4 := ![1,0,3,2]
def matrix (a : Fin 30) (p : Fin 4) : Mat := fun i j =>
  F.ofCode ((matrixPool.getD ((matrixIndex.getD a.val #[]).getD p.val 0) #[]).getD (i.val*3+j.val) 0)
def direction (p : Fin 4) : Vec := fun i =>
  F.ofCode ((directionData.getD p.val #[]).getD i.val 0)

def encodeVec (x : Vec) : Fin 64 :=
  ⟨F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2), by
    have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
    omega⟩
def decodeVec (x : Fin 64) : Vec := fun i => F.ofCode (x.val / 4 ^ i.val % 4)

theorem decodeVec_encodeVec (x : Vec) : decodeVec (encodeVec x) = x := by
  have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
  funext i
  fin_cases i
  all_goals simp only [decodeVec, encodeVec, Fin.val_zero, Fin.val_one, Fin.val_two,
    pow_zero, pow_one, show 4 ^ 2 = 16 from rfl, Nat.div_one]
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) % 4 = F.code (x 0) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) / 4 % 4 = F.code (x 1) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) / 16 % 4 = F.code (x 2) by omega]
    exact F.ofCode_code _

theorem encodeVec_decodeVec (x : Fin 64) : encodeVec (decodeVec x) = x := by revert x; decide

def stepVec (a : Fin 30) (p : Fin 4) (t : F) (x : Vec) : Vec :=
  act (matrix a p) x + t • direction (inversePort p)
def fiberStep (a : Fin 30) (p : Fin 4) (t : F) (x : Fin 64) : Fin 64 :=
  encodeVec (stepVec a p t (decodeVec x))
def controllerOf (u : Fin 1920) : Fin 30 := ⟨u.val / 64, by omega⟩
def fiberOf (u : Fin 1920) : Fin 64 := ⟨u.val % 64, Nat.mod_lt _ (by decide)⟩
def liftAt (a : Fin 30) (x : Fin 64) : Fin 1920 :=
  ⟨64 * a.val + x.val, by have ha := a.isLt; have hx := x.isLt; omega⟩
def forward (u : Fin 1920) (p : Fin 4) (t : F) : Fin 1920 :=
  liftAt (controller (controllerOf u) p) (fiberStep (controllerOf u) p t (fiberOf u))

/-- Symmetrization of the exact generated edge relation, with loops excluded. -/
def graph : SimpleGraph (Fin 1920) where
  Adj u v := u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u))
  symm := by intro u v h; exact ⟨Ne.symm h.1, h.2.elim Or.inr Or.inl⟩
  loopless := by intro u h; exact h.1 rfl

instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u)))
  infer_instance

theorem controller_reverse : ∀ (a : Fin 30) (p : Fin 4),
  controller (controller a p) (inversePort p) = a := by decide
theorem controller_no_loops : ∀ (a : Fin 30) (p : Fin 4), controller a p ≠ a := by decide
theorem inversePort_involution : ∀ p, inversePort (inversePort p) = p := by decide

theorem controllerOf_liftAt (a : Fin 30) (x : Fin 64) : controllerOf (liftAt a x) = a := by
  apply Fin.ext
  change (64*a.val+x.val)/64=a.val
  have hx:=x.isLt
  omega

theorem fiberOf_liftAt (a : Fin 30) (x : Fin 64) : fiberOf (liftAt a x) = x := by
  apply Fin.ext
  change (64*a.val+x.val)%64=x.val
  have hx:=x.isLt
  omega

theorem liftAt_parts (u : Fin 1920) : liftAt (controllerOf u) (fiberOf u) = u := by
  apply Fin.ext
  change 64*(u.val/64)+u.val%64=u.val
  omega

theorem forward_liftAt (a : Fin 30) (x : Fin 64) (p : Fin 4) (t : F) :
  forward (liftAt a x) p t = liftAt (controller a p) (fiberStep a p t x) := by
  simp only [forward, controllerOf_liftAt, fiberOf_liftAt]

theorem forward_ne_self (u : Fin 1920) (p : Fin 4) (t : F) : forward u p t ≠ u := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward, controllerOf_liftAt] at hc
  exact controller_no_loops (controllerOf u) p hc

theorem forward_adj (u : Fin 1920) (p : Fin 4) (t : F) : graph.Adj u (forward u p t) :=
  ⟨Ne.symm (forward_ne_self u p t), Or.inl ⟨p,t,rfl⟩⟩

#print axioms forward_adj


def SourceFinalClaim : Prop := Fintype.card (Fin 1920)=1920 ∧
  (∀v,graph.degree v≤16) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
namespace Clone2016
abbrev Vertex := Fin 1920 ⊕ Fin 96
def layer : Fin 6 → Fin 30 := ![0,3,5,7,9,16]
def planeVec (a b : Fin 4) : Vec := ![F.ofCode a.val,F.ofCode b.val,F.ofCode a.val+F.ofCode b.val]
def center (j : Fin 96) : Fin 1920 :=
  liftAt (layer ⟨j.val/16,by have h:=j.isLt;omega⟩)
    (encodeVec (planeVec ⟨j.val/4%4,Nat.mod_lt _ (by decide)⟩ ⟨j.val%4,Nat.mod_lt _ (by decide)⟩))
abbrev graph := FullNeighborhoodClones.graph F4Graph1920.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F4Graph1920.graph center).Adj)
def label : Vertex ≃ Fin 2016 := finSumFinEquiv
theorem label_new (j : Fin 96) : (label (.inr j)).val=1920+j.val := rfl
def FinalClaim : Prop := Fintype.card Vertex=2016 ∧
  (∀v,graph.degree v≤17) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 2016)
end Clone2016
end DegreeDiameter.Portfolio.F4Graph1920
