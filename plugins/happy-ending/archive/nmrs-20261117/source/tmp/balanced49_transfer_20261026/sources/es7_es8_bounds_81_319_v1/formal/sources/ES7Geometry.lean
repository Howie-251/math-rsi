import ES8Final

namespace ES7Geometry
open ES8Geometry ES8BalancedGeometry ES8ActualRanks ES8BaekGeometry ES8BoundaryGeometry

def HasConvexHeptagon (S : Set Point) : Prop :=
  ∃ T : Finset Point, T.card=7 ∧ (↑T : Set Point)⊆S ∧ ConvexPosition (↑T : Set Point)

theorem heptagon_of_cyclic (p : Nat → Point) (positive : CyclicPositive 7 p)
    (S : Set Point) (inside : ∀ i, i < 7 → p i ∈ S) : HasConvexHeptagon S := by
  classical
  let T := (Finset.range 7).image p
  have inj : Set.InjOn p (↑(Finset.range 7) : Set Nat) := by
    intro i hi j hj equal
    have hi' : i < 7 := by simpa using hi
    have hj' : j < 7 := by simpa using hj
    by_cases h : i=j
    · exact h
    · by_cases hij : i < j
      · exact False.elim (cyclic_points_distinct 7 (by omega) p positive i j hi' hj' hij equal)
      · exact False.elim (cyclic_points_distinct 7 (by omega) p positive j i hj' hi' (by omega) equal.symm)
  have card : T.card=7 := by
    dsimp [T]
    rw [Finset.card_image_of_injOn inj]
    simp
  have seteq : (↑T : Set Point) = {v | ∃ i, i < 7 ∧ p i=v} := by
    ext v
    simp [T]
  refine ⟨T,card,?_,?_⟩
  · intro v hv
    rw [seteq] at hv
    obtain ⟨i,hi,rfl⟩ := hv
    exact inside i hi
  · rw [seteq]
    exact cyclic_positive_convex_position 7 (by omega) p positive


theorem boundary_heptagon {k l} (b : Boundary k l) (seven : k+l+2=7)
    (S : Set Point) (inside : b.points⊆S) : HasConvexHeptagon S := by
  refine ⟨b.finite,?_,?_,?_⟩
  · rw [b.card,seven]
  · rw [b.finite_coe]; exact inside
  · rw [b.finite_coe]; exact boundary_convex_position b

theorem hasNGon_heptagon {n} (c : Configuration n)
    (gon : (colorConfig c.cup true).HasNGon 7 (Finset.range n)) :
    HasConvexHeptagon (Set.range c.point) := by
  obtain ⟨xs,ys,hgon,xi,yi⟩ := gon
  let k := xs.length-2
  let l := ys.length-2
  have hx : xs.length=k+2 := by have := hgon.1.1; dsimp [k]; omega
  have hy : ys.length=l+2 := by have := hgon.1.2.2.1; dsimp [l]; omega
  apply boundary_heptagon (boundaryOfGon c xs ys k l hx hy xi yi hgon.1)
  · have := hgon.2; omega
  · exact boundaryOfGon_inside c xs ys k l hx hy xi yi hgon.1

theorem hasNCup_heptagon {n} (c : Configuration n)
    (cup : (colorConfig c.cup true).HasNCup 7 (Finset.range n)) :
    HasConvexHeptagon (Set.range c.point) := by
  obtain ⟨xs,⟨chain,len⟩,inside⟩ := cup
  let arc := cupArc c xs 5 len inside chain
  let p : Nat→Point := fun i=>if hi : i<7 then arc.point ⟨i,hi⟩ else (0,0)
  apply heptagon_of_cyclic p
  · intro i j k hij hjk hk
    have hi : i<7 := by omega
    have hj : j<7 := by omega
    simp only [p,dif_pos hi,dif_pos hj,dif_pos hk]
    exact arc.positive _ _ _ hij hjk
  · intro i hi
    simp only [p,dif_pos hi]
    change pointAt c (xs.get ⟨i,by omega⟩)∈Set.range c.point
    have bound := Finset.mem_range.mp (inside _ (xs.get_mem ⟨i,by omega⟩))
    exact ⟨⟨_,bound⟩,(pointAt_eq c _ bound).symm⟩


#print axioms hasNGon_heptagon
#print axioms hasNCup_heptagon
end ES7Geometry
