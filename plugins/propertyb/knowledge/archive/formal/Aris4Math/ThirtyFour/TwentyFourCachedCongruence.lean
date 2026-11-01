import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourCachedCongruence
open CachedRows

/-- Cached exact rows ignore the ordering of the type list and the list of
correction centers. This permits one probability computation for many labels. -/
theorem rows (p q : Numeric.Profile)
    (v : p.v=q.v) (positions : p.positions=q.positions)
    (types : p.types.toFinset=q.types.toFinset) (k : ℕ) :
    (∀b,cachedA p k b=cachedA q k b) ∧ cachedC p k=cachedC q k := by
  have compat (t : Numeric.EdgeType) (b : Bool) : compatible p t k b ↔ compatible q t k b := by
    simp only [compatible,positions]
  have ac (b : Bool) : aCoeff p k b=aCoeff q k b := by
    simp only [aCoeff,Numeric.freeCount,Numeric.leftCount,Numeric.rightCount,v,positions]
  have cc : cCoeff p k=cCoeff q k := by
    simp only [cCoeff,Numeric.freeCount,Numeric.leftCount,Numeric.rightCount,v,positions]
  have mm (b : Bool) (r : Fin 6) : mass p k b r=mass q k b r := by
    simp only [mass,types,compat]
  simp only [cachedA,cachedC,cachedDiagonal,types,mm,ac,cc,compat]
  exact ⟨fun _=>True.intro,True.intro⟩
end Aris4Math.ThirtyFour.TwentyFourCachedCongruence
