import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fin.VecNotation

/-! Literal Fin3750 binding of the 2026-10-29 full-F5 construction.
This file defines the concrete graph and verifies small controller/root certificates.
It does not assert the global diameter or regularity theorem. -/
namespace DegreeDiameter.Portfolio.F5Graph3750

set_option maxRecDepth 3000
set_option maxHeartbeats 4000000

def controller : Fin 30 → Fin 4 → Fin 30 := ![![18, 20, 2, 9], ![13, 2, 3, 17], ![1, 18, 11, 0], ![17, 21, 5, 1], ![10, 25, 18, 8], ![29, 15, 12, 3], ![15, 22, 21, 16], ![16, 27, 25, 13], ![21, 10, 4, 12], ![22, 19, 0, 14], ![8, 4, 19, 24], ![23, 26, 16, 2], ![28, 23, 8, 5], ![25, 1, 7, 23], ![19, 29, 9, 25], ![5, 6, 27, 29], ![26, 7, 6, 11], ![24, 3, 1, 26], ![2, 0, 29, 4], ![9, 14, 26, 10], ![0, 28, 24, 27], ![3, 8, 22, 6], ![6, 9, 28, 21], ![12, 11, 13, 28], ![27, 17, 10, 20], ![4, 13, 14, 7], ![11, 16, 17, 19], ![7, 24, 20, 15], ![20, 12, 23, 22], ![14, 5, 15, 18]]

def inversePort : Fin 4 → Fin 4 := ![1, 0, 3, 2]

def matrix : Fin 4 → Fin 3 → Fin 3 → Nat := ![![![0, 2, 4], ![1, 0, 0], ![0, 1, 3]], ![![0, 1, 0], ![4, 0, 3], ![2, 0, 1]], ![![2, 3, 1], ![0, 4, 1], ![1, 0, 1]], ![![2, 1, 2], ![3, 3, 4], ![3, 4, 4]]]

def direction : Fin 4 → Fin 3 → Nat := ![![1, 0, 0], ![0, 1, 0], ![0, 0, 1], ![1, 1, 1]]

def coordinate (x : Fin 125) (i : Fin 3) : Nat :=
  (x.val / 5 ^ i.val) % 5

def stepCoordinate (p : Fin 4) (t : Fin 5) (x : Fin 125) (i : Fin 3) : Nat :=
  (matrix p i 0 * coordinate x 0 + matrix p i 1 * coordinate x 1 +
   matrix p i 2 * coordinate x 2 + t.val * direction (inversePort p) i) % 5

def fiberStep (p : Fin 4) (t : Fin 5) (x : Fin 125) : Fin 125 :=
  ⟨stepCoordinate p t x 0 + 5 * stepCoordinate p t x 1 +
      25 * stepCoordinate p t x 2, by
    have h0 : stepCoordinate p t x 0 < 5 := Nat.mod_lt _ (by decide)
    have h1 : stepCoordinate p t x 1 < 5 := Nat.mod_lt _ (by decide)
    have h2 : stepCoordinate p t x 2 < 5 := Nat.mod_lt _ (by decide)
    omega⟩

def controllerOf (u : Fin 3750) : Fin 30 := ⟨u.val / 125, by omega⟩
def fiberOf (u : Fin 3750) : Fin 125 := ⟨u.val % 125, Nat.mod_lt _ (by decide)⟩

def forward (u : Fin 3750) (p : Fin 4) (t : Fin 5) : Fin 3750 :=
  ⟨125 * (controller (controllerOf u) p).val + (fiberStep p t (fiberOf u)).val, by
    have hc := (controller (controllerOf u) p).isLt
    have hf := (fiberStep p t (fiberOf u)).isLt
    omega⟩

/-- Explicit symmetrized line-relation graph with self-loops excluded. -/
def graph : SimpleGraph (Fin 3750) where
  Adj u v := u ≠ v ∧
    ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u))
  symm := by
    intro u v h
    exact ⟨Ne.symm h.1, h.2.elim Or.inr Or.inl⟩
  loopless := by
    intro u h
    exact h.1 rfl

/-- Kernel-checked 120-entry reverse-port binding for the literal controller. -/
theorem controller_reverse : ∀ (a : Fin 30) (p : Fin 4),
    controller (controller a p) (inversePort p) = a := by decide

theorem controller_no_loops : ∀ (a : Fin 30) (p : Fin 4),
    controller a p ≠ a := by decide

theorem controller_distinct_ports : ∀ (a : Fin 30) (p q : Fin 4),
    controller a p = controller a q → p = q := by decide

/-- Exactly twenty distinct forward neighbors for the actual root label zero. -/
def rootForwardNeighbors : Finset (Fin 3750) :=
  (Finset.univ.product Finset.univ).image fun pt : Fin 4 × Fin 5 => forward 0 pt.1 pt.2

theorem root_forward_count : rootForwardNeighbors.card = 20 := by decide

theorem root_forward_not_self : ∀ (p : Fin 4) (t : Fin 5), forward 0 p t ≠ 0 := by decide

theorem root_forward_adj (p : Fin 4) (t : Fin 5) : graph.Adj 0 (forward 0 p t) := by
  exact ⟨Ne.symm (root_forward_not_self p t), Or.inl ⟨p, t, rfl⟩⟩

def negNoise (t : Fin 5) : Fin 5 := ⟨(5 - t.val) % 5, Nat.mod_lt _ (by decide)⟩

/-- The only new exhaustive check has 4*5*125=2500 inputs. -/
theorem fiberStep_reverse : ∀ (p : Fin 4) (t : Fin 5) (x : Fin 125),
    fiberStep (inversePort p) (negNoise t) (fiberStep p t x) = x := by decide

theorem controllerOf_forward (u : Fin 3750) (p : Fin 4) (t : Fin 5) :
    controllerOf (forward u p t) = controller (controllerOf u) p := by
  apply Fin.ext
  change (125 * (controller (controllerOf u) p).val +
    (fiberStep p t (fiberOf u)).val) / 125 = (controller (controllerOf u) p).val
  have hf := (fiberStep p t (fiberOf u)).isLt
  omega

theorem fiberOf_forward (u : Fin 3750) (p : Fin 4) (t : Fin 5) :
    fiberOf (forward u p t) = fiberStep p t (fiberOf u) := by
  apply Fin.ext
  change (125 * (controller (controllerOf u) p).val +
    (fiberStep p t (fiberOf u)).val) % 125 = (fiberStep p t (fiberOf u)).val
  have hf := (fiberStep p t (fiberOf u)).isLt
  omega

theorem forward_reverse (u : Fin 3750) (p : Fin 4) (t : Fin 5) :
    forward (forward u p t) (inversePort p) (negNoise t) = u := by
  apply Fin.ext
  change 125 * (controller (controllerOf (forward u p t)) (inversePort p)).val +
    (fiberStep (inversePort p) (negNoise t) (fiberOf (forward u p t))).val = u.val
  rw [controllerOf_forward, fiberOf_forward, controller_reverse, fiberStep_reverse]
  simp only [controllerOf, fiberOf]
  omega

theorem forward_ne_self (u : Fin 3750) (p : Fin 4) (t : Fin 5) : forward u p t ≠ u := by
  intro h
  have hc := congrArg controllerOf h
  rw [controllerOf_forward] at hc
  exact controller_no_loops (controllerOf u) p hc

theorem adj_iff_forward (u v : Fin 3750) :
    graph.Adj u v ↔ ∃ (p : Fin 4) (t : Fin 5), forward u p t = v := by
  constructor
  · rintro ⟨_, h⟩
    rcases h with h | ⟨p, t, h⟩
    · exact h
    · refine ⟨inversePort p, negNoise t, ?_⟩
      rw [← h]
      exact forward_reverse v p t
  · rintro ⟨p, t, h⟩
    refine ⟨?_, Or.inl ⟨p, t, h⟩⟩
    intro heq
    exact forward_ne_self u p t (h.trans heq.symm)

instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u ≠ v ∧
    ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u)))
  infer_instance

theorem neighborFinset_eq_forward (u : Fin 3750) :
    graph.neighborFinset u =
      (Finset.univ.product Finset.univ).image
        (fun pt : Fin 4 × Fin 5 => forward u pt.1 pt.2) := by
  ext v
  simp only [SimpleGraph.mem_neighborFinset, adj_iff_forward, Finset.mem_image]
  constructor
  · rintro ⟨p, t, h⟩
    exact ⟨(p, t), by simp, h⟩
  · rintro ⟨pt, _, h⟩
    exact ⟨pt.1, pt.2, h⟩

theorem degree_le_twenty (u : Fin 3750) : graph.degree u ≤ 20 := by
  rw [← SimpleGraph.card_neighborFinset_eq_degree, neighborFinset_eq_forward]
  calc
    _ ≤ (Finset.univ.product (Finset.univ : Finset (Fin 5))).card := Finset.card_image_le
    _ = 20 := by decide

#print axioms controller_reverse
#print axioms root_forward_count
#print axioms root_forward_adj
#print axioms fiberStep_reverse
#print axioms degree_le_twenty

end DegreeDiameter.Portfolio.F5Graph3750
