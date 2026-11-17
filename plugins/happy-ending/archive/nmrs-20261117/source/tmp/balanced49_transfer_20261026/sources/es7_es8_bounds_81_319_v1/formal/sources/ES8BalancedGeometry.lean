import ES8CycleValidation

namespace ES8BalancedGeometry
open ES8 ES8Domains ES8ActualRanks ES8BalancedCatalog ES8Geometry ES8CycleRows ES8CycleData

/-- Actual real points in increasing x order and in general position. -/
structure Configuration (n : Nat) where
  point : Fin n → Point
  xOrder : StrictMono (fun i => (point i).1)
  generalPosition : ∀ u v w : Fin n, u < v → v < w → orient (point u) (point v) (point w) ≠ 0

noncomputable def Configuration.cup {n} (c : Configuration n) (u v w : Nat) : Bool := by
  classical
  exact if h : u < n ∧ v < n ∧ w < n then
    decide (0 < orient (c.point ⟨u,h.1⟩) (c.point ⟨v,h.2.1⟩) (c.point ⟨w,h.2.2⟩)) else false

theorem Configuration.cup_sign {n} (c : Configuration n) (u v w : Fin n) :
    c.cup u v w=true ↔ 0 < orient (c.point u) (c.point v) (c.point w) := by
  classical
  simp [Configuration.cup,u.isLt,v.isLt,w.isLt]

noncomputable def model {n} (c : Configuration n) (caps : Avoids n c.cup false 7)
    (cups : Avoids n c.cup true 7) : Model n table where
  index := fun v => (ownerIndex n c.cup caps cups v).val
  injective := fun _ _ h => ownerIndex_injective n c.cup caps cups (Fin.ext h)
  bounded := fun v => (ownerIndex n c.cup caps cups v).isLt
  point := c.point
  cup := c.cup
  label := labels c.cup
  growth := labels_increasing n c.cup
  pairs := fun u v huv => actual_pair_fits n c.cup caps cups u v huv _
    (ES8CycleValidation.domain_checked _ _ (ownerIndex n c.cup caps cups u).isLt (ownerIndex n c.cup caps cups v).isLt)
  signs := fun u v w _ _ => c.cup_sign u v w
  nonzero := c.generalPosition

/-- The complete balanced geometric population bound. No capacity-row hypothesis
is assumed: every literal row is discharged by the checked geometric validator. -/
theorem balanced_bound (n : Nat) (c : Configuration n)
    (noCap : ¬ (colorConfig c.cup true).HasNCap 7 (Finset.range n))
    (noCup : ¬ (colorConfig c.cup true).HasNCup 7 (Finset.range n))
    (noOctagon : ¬ HasConvexOctagon (Set.range c.point)) : n ≤ 193 := by
  let caps := avoids_of_no_cap n 7 c.cup noCap
  let cups := avoids_of_no_cup n 7 c.cup noCup
  let m := model c caps cups
  apply size_when_rows_hold n c.cup caps cups
  intro j hj
  have geometric := checked_row_sound m (Complete.row Certificates.Balanced.rows j)
    (cycles.getD j []) (ES8CycleValidation.cycle_checked j hj) noOctagon
  exact geometric

#print axioms balanced_bound
end ES8BalancedGeometry
