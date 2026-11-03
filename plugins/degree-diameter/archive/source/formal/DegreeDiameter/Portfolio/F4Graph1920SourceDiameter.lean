import DegreeDiameter.Portfolio.F4Graph1920Row0Walks
import DegreeDiameter.Portfolio.F4Graph1920Row1Walks
import DegreeDiameter.Portfolio.F4Graph1920Row2Walks
import DegreeDiameter.Portfolio.F4Graph1920Row3Walks
import DegreeDiameter.Portfolio.F4Graph1920Row4Walks
import DegreeDiameter.Portfolio.F4Graph1920Row5Walks
import DegreeDiameter.Portfolio.F4Graph1920Row6Walks
import DegreeDiameter.Portfolio.F4Graph1920Row7Walks
import DegreeDiameter.Portfolio.F4Graph1920Row8Walks
import DegreeDiameter.Portfolio.F4Graph1920Row9Walks
import DegreeDiameter.Portfolio.F4Graph1920Row10Walks
import DegreeDiameter.Portfolio.F4Graph1920Row11Walks
import DegreeDiameter.Portfolio.F4Graph1920Row12Walks
import DegreeDiameter.Portfolio.F4Graph1920Row13Walks
import DegreeDiameter.Portfolio.F4Graph1920Row14Walks
import DegreeDiameter.Portfolio.F4Graph1920Row15Walks
import DegreeDiameter.Portfolio.F4Graph1920Row16Walks
import DegreeDiameter.Portfolio.F4Graph1920Row17Walks
import DegreeDiameter.Portfolio.F4Graph1920Row18Walks
import DegreeDiameter.Portfolio.F4Graph1920Row19Walks
import DegreeDiameter.Portfolio.F4Graph1920Row20Walks
import DegreeDiameter.Portfolio.F4Graph1920Row21Walks
import DegreeDiameter.Portfolio.F4Graph1920Row22Walks
import DegreeDiameter.Portfolio.F4Graph1920Row23Walks
import DegreeDiameter.Portfolio.F4Graph1920Row24Walks
import DegreeDiameter.Portfolio.F4Graph1920Row25Walks
import DegreeDiameter.Portfolio.F4Graph1920Row26Walks
import DegreeDiameter.Portfolio.F4Graph1920Row27Walks
import DegreeDiameter.Portfolio.F4Graph1920Row28Walks
import DegreeDiameter.Portfolio.F4Graph1920Row29Walks
namespace DegreeDiameter.Portfolio.F4Graph1920
def CompleteRow (a : Fin 30) : Prop := ∀(x : Fin 64)(v : Fin 1920),
  ∃w:graph.Walk (liftAt a x) v,w.length≤3
theorem all_controller_rows : ∀a,CompleteRow a :=
  (Fin.cases Row0.row0_full_walk_bound (Fin.cases Row1.row1_full_walk_bound (Fin.cases Row2.row2_full_walk_bound (Fin.cases Row3.row3_full_walk_bound (Fin.cases Row4.row4_full_walk_bound (Fin.cases Row5.row5_full_walk_bound (Fin.cases Row6.row6_full_walk_bound (Fin.cases Row7.row7_full_walk_bound (Fin.cases Row8.row8_full_walk_bound (Fin.cases Row9.row9_full_walk_bound (Fin.cases Row10.row10_full_walk_bound (Fin.cases Row11.row11_full_walk_bound (Fin.cases Row12.row12_full_walk_bound (Fin.cases Row13.row13_full_walk_bound (Fin.cases Row14.row14_full_walk_bound (Fin.cases Row15.row15_full_walk_bound (Fin.cases Row16.row16_full_walk_bound (Fin.cases Row17.row17_full_walk_bound (Fin.cases Row18.row18_full_walk_bound (Fin.cases Row19.row19_full_walk_bound (Fin.cases Row20.row20_full_walk_bound (Fin.cases Row21.row21_full_walk_bound (Fin.cases Row22.row22_full_walk_bound (Fin.cases Row23.row23_full_walk_bound (Fin.cases Row24.row24_full_walk_bound (Fin.cases Row25.row25_full_walk_bound (Fin.cases Row26.row26_full_walk_bound (Fin.cases Row27.row27_full_walk_bound (Fin.cases Row28.row28_full_walk_bound (Fin.cases Row29.row29_full_walk_bound (fun a : Fin 0 => Fin.elim0 a)))))))))))))))))))))))))))))))
theorem diameterAtMost_three : DiameterAtMost graph 3 := by
  intro u v
  have h := all_controller_rows (controllerOf u) (fiberOf u) v
  change (∃w:graph.Walk (liftAt (controllerOf u) (fiberOf u)) v,w.length≤3) at h
  exact (liftAt_parts u) ▸ h
#print axioms diameterAtMost_three
end DegreeDiameter.Portfolio.F4Graph1920
