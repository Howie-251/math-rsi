import DegreeDiameter.Portfolio.F9Graph56862Field
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def controllerData : Array (Array Nat) := #[#[2, 24, 26, 52, 31, 62], #[3, 25, 27, 53, 32, 63], #[4, 0, 28, 54, 33, 64], #[5, 1, 29, 55, 34, 65], #[6, 2, 30, 56, 35, 66], #[7, 3, 31, 57, 36, 67], #[8, 4, 32, 58, 37, 68], #[9, 5, 33, 59, 38, 69], #[10, 6, 34, 60, 39, 70], #[11, 7, 35, 61, 40, 71], #[12, 8, 36, 62, 41, 72], #[13, 9, 37, 63, 42, 73], #[14, 10, 38, 64, 43, 74], #[15, 11, 39, 65, 44, 75], #[16, 12, 40, 66, 45, 76], #[17, 13, 41, 67, 46, 77], #[18, 14, 42, 68, 47, 52], #[19, 15, 43, 69, 48, 53], #[20, 16, 44, 70, 49, 54], #[21, 17, 45, 71, 50, 55], #[22, 18, 46, 72, 51, 56], #[23, 19, 47, 73, 26, 57], #[24, 20, 48, 74, 27, 58], #[25, 21, 49, 75, 28, 59], #[0, 22, 50, 76, 29, 60], #[1, 23, 51, 77, 30, 61], #[58, 61, 52, 0, 21, 39], #[59, 62, 53, 1, 22, 40], #[60, 63, 54, 2, 23, 41], #[61, 64, 55, 3, 24, 42], #[62, 65, 56, 4, 25, 43], #[63, 66, 57, 5, 0, 44], #[64, 67, 58, 6, 1, 45], #[65, 68, 59, 7, 2, 46], #[66, 69, 60, 8, 3, 47], #[67, 70, 61, 9, 4, 48], #[68, 71, 62, 10, 5, 49], #[69, 72, 63, 11, 6, 50], #[70, 73, 64, 12, 7, 51], #[71, 74, 65, 13, 8, 26], #[72, 75, 66, 14, 9, 27], #[73, 76, 67, 15, 10, 28], #[74, 77, 68, 16, 11, 29], #[75, 52, 69, 17, 12, 30], #[76, 53, 70, 18, 13, 31], #[77, 54, 71, 19, 14, 32], #[52, 55, 72, 20, 15, 33], #[53, 56, 73, 21, 16, 34], #[54, 57, 74, 22, 17, 35], #[55, 58, 75, 23, 18, 36], #[56, 59, 76, 24, 19, 37], #[57, 60, 77, 25, 20, 38], #[43, 46, 0, 26, 65, 16], #[44, 47, 1, 27, 66, 17], #[45, 48, 2, 28, 67, 18], #[46, 49, 3, 29, 68, 19], #[47, 50, 4, 30, 69, 20], #[48, 51, 5, 31, 70, 21], #[49, 26, 6, 32, 71, 22], #[50, 27, 7, 33, 72, 23], #[51, 28, 8, 34, 73, 24], #[26, 29, 9, 35, 74, 25], #[27, 30, 10, 36, 75, 0], #[28, 31, 11, 37, 76, 1], #[29, 32, 12, 38, 77, 2], #[30, 33, 13, 39, 52, 3], #[31, 34, 14, 40, 53, 4], #[32, 35, 15, 41, 54, 5], #[33, 36, 16, 42, 55, 6], #[34, 37, 17, 43, 56, 7], #[35, 38, 18, 44, 57, 8], #[36, 39, 19, 45, 58, 9], #[37, 40, 20, 46, 59, 10], #[38, 41, 21, 47, 60, 11], #[39, 42, 22, 48, 61, 12], #[40, 43, 23, 49, 62, 13], #[41, 44, 24, 50, 63, 14], #[42, 45, 25, 51, 64, 15]]
def chartData : Array (Array Nat) := #[#[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 4, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 6], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 4, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7], #[0, 1, 2, 3, 5, 7]]
def controller (a : Fin 78) (p : Fin 6) : Fin 78 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 % 78, Nat.mod_lt _ (by decide)⟩
def inversePort : Fin 6 → Fin 6 := ![1,0,3,2,4,5]
def matrixPool : Fin 8 → Mat := ![![![F.c0, F.c0, F.c1], ![F.c4, F.c0, F.c0], ![F.c0, F.c1, F.c0]], ![![F.c0, F.c5, F.c0], ![F.c0, F.c0, F.c1], ![F.c1, F.c0, F.c0]], ![![F.c1, F.c0, F.c0], ![F.c1, F.c6, F.c4], ![F.c7, F.c6, F.c6]], ![![F.c1, F.c0, F.c0], ![F.c3, F.c4, F.c2], ![F.c5, F.c8, F.c4]], ![![F.c1, F.c0, F.c0], ![F.c6, F.c6, F.c4], ![F.c8, F.c2, F.c3]], ![![F.c1, F.c0, F.c0], ![F.c1, F.c5, F.c3], ![F.c4, F.c4, F.c7]], ![![F.c1, F.c0, F.c0], ![F.c3, F.c4, F.c4], ![F.c3, F.c5, F.c8]], ![![F.c1, F.c0, F.c0], ![F.c2, F.c3, F.c3], ![F.c5, F.c2, F.c6]]]
def chart (a : Fin 78) (p : Fin 6) : Fin 8 :=
  ⟨(chartData.getD a.val #[]).getD p.val 0 % 8, Nat.mod_lt _ (by decide)⟩
def matrix (a : Fin 78) (p : Fin 6) : Mat := matrixPool (chart a p)
def direction : Fin 6 → Vec := ![![F.c0, F.c0, F.c1], ![F.c1, F.c0, F.c0], ![F.c1, F.c1, F.c1], ![F.c1, F.c2, F.c1], ![F.c1, F.c3, F.c2], ![F.c1, F.c6, F.c2]]
def encodeVec (x : Vec) : Fin 729 :=
  ⟨F.code (x 0) + 9 * F.code (x 1) + 81 * F.code (x 2), by
    have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
    omega⟩
def decodeVec (x : Fin 729) : Vec := fun i => F.ofCode (x.val / 9 ^ i.val % 9)

theorem decodeVec_encodeVec (x : Vec) : decodeVec (encodeVec x) = x := by
  have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
  funext i
  fin_cases i
  all_goals simp only [decodeVec, encodeVec, Fin.val_zero, Fin.val_one, Fin.val_two,
    pow_zero, pow_one, show 9 ^ 2 = 81 from rfl, Nat.div_one]
  · rw [show (F.code (x 0) + 9 * F.code (x 1) + 81 * F.code (x 2)) % 9 = F.code (x 0) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 9 * F.code (x 1) + 81 * F.code (x 2)) / 9 % 9 = F.code (x 1) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 9 * F.code (x 1) + 81 * F.code (x 2)) / 81 % 9 = F.code (x 2) by omega]
    exact F.ofCode_code _

theorem encodeVec_decodeVec (x : Fin 729) : encodeVec (decodeVec x) = x := by revert x; decide

def stepVec (a : Fin 78) (p : Fin 6) (t : F) (x : Vec) : Vec :=
  act (matrix a p) x + t • direction (inversePort p)
def fiberStep (a : Fin 78) (p : Fin 6) (t : F) (x : Fin 729) : Fin 729 :=
  encodeVec (stepVec a p t (decodeVec x))
def controllerOf (u : Fin 56862) : Fin 78 := ⟨u.val / 729, by omega⟩
def fiberOf (u : Fin 56862) : Fin 729 := ⟨u.val % 729, Nat.mod_lt _ (by decide)⟩
def liftAt (a : Fin 78) (x : Fin 729) : Fin 56862 :=
  ⟨729 * a.val + x.val, by have ha := a.isLt; have hx := x.isLt; omega⟩
def forward (u : Fin 56862) (p : Fin 6) (t : F) : Fin 56862 :=
  liftAt (controller (controllerOf u) p) (fiberStep (controllerOf u) p t (fiberOf u))

/-- Symmetrization of the exact generated edge relation, with loops excluded. -/
def graph : SimpleGraph (Fin 56862) where
  Adj u v := u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u))
  symm := by intro u v h; exact ⟨Ne.symm h.1, h.2.elim Or.inr Or.inl⟩
  loopless := by intro u h; exact h.1 rfl

instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u)))
  infer_instance

theorem controller_reverse : ∀ (a : Fin 78) (p : Fin 6),
  controller (controller a p) (inversePort p) = a := by decide
theorem controller_no_loops : ∀ (a : Fin 78) (p : Fin 6), controller a p ≠ a := by decide
theorem inversePort_involution : ∀ p, inversePort (inversePort p) = p := by decide

theorem controllerOf_liftAt (a : Fin 78) (x : Fin 729) : controllerOf (liftAt a x) = a := by
  apply Fin.ext
  change (729*a.val+x.val)/729=a.val
  have hx:=x.isLt
  omega

theorem fiberOf_liftAt (a : Fin 78) (x : Fin 729) : fiberOf (liftAt a x) = x := by
  apply Fin.ext
  change (729*a.val+x.val)%729=x.val
  have hx:=x.isLt
  omega

theorem liftAt_parts (u : Fin 56862) : liftAt (controllerOf u) (fiberOf u) = u := by
  apply Fin.ext
  change 729*(u.val/729)+u.val%729=u.val
  omega

theorem forward_liftAt (a : Fin 78) (x : Fin 729) (p : Fin 6) (t : F) :
  forward (liftAt a x) p t = liftAt (controller a p) (fiberStep a p t x) := by
  simp only [forward, controllerOf_liftAt, fiberOf_liftAt]

theorem forward_ne_self (u : Fin 56862) (p : Fin 6) (t : F) : forward u p t ≠ u := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward, controllerOf_liftAt] at hc
  exact controller_no_loops (controllerOf u) p hc

theorem forward_adj (u : Fin 56862) (p : Fin 6) (t : F) : graph.Adj u (forward u p t) :=
  ⟨Ne.symm (forward_ne_self u p t), Or.inl ⟨p,t,rfl⟩⟩

#print axioms forward_adj
end DegreeDiameter.Portfolio.F9Graph56862
