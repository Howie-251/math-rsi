import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow0
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow1
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow2
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow3
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow4
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow5
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow6
import DegreeDiameter.Portfolio.F3Graph15552FullEndpointRow7
import DegreeDiameter.Portfolio.F3Graph15552FullSymmetry
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem all_pair_conditions : ∀r b,pairCondition r b :=
  Fin.cases endpoint_row0 (Fin.cases endpoint_row1 (Fin.cases endpoint_row2
    (Fin.cases endpoint_row3 (Fin.cases endpoint_row4 (Fin.cases endpoint_row5
      (Fin.cases endpoint_row6 (Fin.cases endpoint_row7 (fun i => Fin.elim0 i))))))))
theorem pair_bound (r : Fin 8) (b : Fin 192) : PairBound (FullSymmetry.representatives r) b := by
  have h := all_pair_conditions r b
  cases hd : pairDescriptor r b with
  | inl k =>
      have hc : routeController (FullSymmetry.representatives r) (rankWord k)=b := by
        simpa only [pairCondition,hd] using h
      exact rankBound _ _ k hc
  | inr g =>
      have hc : (cosetPackage g).condition (FullSymmetry.representatives r) b := by
        simpa only [pairCondition,hd] using h
      exact (cosetPackage g).bound _ _ hc
theorem representative_rows (r : Fin 8) : FullSymmetry.RepresentativeRowBound r := by
  intro x v
  have h : ∃w : graph.Walk (liftAt (FullSymmetry.representatives r) x)
      (liftAt (controllerOf v) (fiberOf v)),w.length≤4 := pair_bound r (controllerOf v) x (fiberOf v)
  exact (liftAt_parts v) ▸ h
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
namespace DegreeDiameter.Portfolio.F3Graph15552
theorem diameterAtMost_four : DiameterAtMost graph 4 :=
  FullSymmetry.diameterAtMost_of_representatives FullKernel.representative_rows
#print axioms diameterAtMost_four
end DegreeDiameter.Portfolio.F3Graph15552
