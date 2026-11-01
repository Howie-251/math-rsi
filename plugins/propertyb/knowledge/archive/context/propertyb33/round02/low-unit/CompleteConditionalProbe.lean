import Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection

namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitComplete

theorem propertyB_of_low_unit
    (representation : ∀ H : Simple5Hypergraph (Fin 23), H.edges.card = 33 →
      ∀ vertices : Fin 6 ↪ Fin 23, ∀ e : Fin 3,
      (∀ i, H.degree (vertices i) = TwentyThreeLowUnitSixCatalogData.degreeData i) →
      (∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = TwentyThreeLowUnitSixCatalogData.pairDegree e i j) →
      ∃ c : TwentyThreeLowUnitSixCatalogData.Case, ∃ w : Fin 6 ↪ Fin 23,
        ∀ T, MultiLockRecovery.count H w T = TwentyThreeLowUnitSixCatalogData.counts c T)
    (finalCounts : ∀ H : Simple5Hypergraph (Fin 23), ∀ w : Fin 6 ↪ Fin 23,
      ∀ c : TwentyThreeLowUnitSixCatalogData.Case,
      (∀ T, MultiLockRecovery.count H w T = TwentyThreeLowUnitSixCatalogData.counts c T) → PropertyB H)
    (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count : H.sixVertices.card = 1) (x : Fin 23) (dx : H.degree x = 6)
    (unit : ∀ y, H.degree y = 7 → H.codegree x y = 1) : PropertyB H := by
  classical
  have budget := TwentyThreeSelection.six_seven_budget H cover edges33 (by decide)
  have many : 17 ≤ (TwentyThreeSelection.sevenVertices H).card := by omega
  by_cases high : ∃ y z : Fin 23, H.degree y = 7 ∧ H.degree z = 7 ∧
      y ≠ z ∧ 3 ≤ H.codegree y z
  · obtain ⟨y,z,dy,dz,yz,cyz⟩ := high
    exact TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair
      H cover edges33 many x y z dx dy dz unit yz cyz
  have upper (y z : Fin 23) (dy : H.degree y = 7) (dz : H.degree z = 7)
      (yz : y ≠ z) : H.codegree y z ≤ 2 := by
    by_contra hn
    exact high ⟨y,z,dy,dz,yz,by omega⟩
  obtain ⟨e,w,degrees,pairs⟩ :=
    TwentyThreeLowUnitSixSelection.exists_locks H cover edges33 count x dx unit
      (fun y z yz dy dz => upper y z dy dz yz)
  obtain ⟨c,v,actual⟩ :=
    representation H edges33 w e degrees pairs
  exact finalCounts H v c actual

end Aris4Math.ThirtyThree.TwentyThreeLowUnitComplete
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitComplete.propertyB_of_low_unit
