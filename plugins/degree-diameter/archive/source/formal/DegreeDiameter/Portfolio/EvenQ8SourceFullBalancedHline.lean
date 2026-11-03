import DegreeDiameter.Portfolio.EvenQ8SourceFullData
namespace DegreeDiameter.Portfolio.EvenQ8SourceFull
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Balanced
open DegreeDiameter.Portfolio.EvenQ8Source.Balanced
open DegreeDiameter.Portfolio.EvenQ8Source
def restrictedLine (l : Fin 584) : Line := ⟨l.val,by omega⟩
theorem hline_certificate : ∀ (l : Fin 584) (i : Fin 9),
    pointLine (linePoint (restrictedLine l) i) (coverSlot (restrictedLine l) i) = restrictedLine l := by decide
theorem hline : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  intro p l h
  by_cases hl : l.val < 584
  · let small : Fin 584 := ⟨l.val,hl⟩
    have he : restrictedLine small = l := Fin.ext rfl
    obtain ⟨i,hi⟩ := h
    refine ⟨coverSlot l i,?_⟩
    rw [←hi]
    have hc := hline_certificate small i
    rw [he] at hc
    exact hc
  · have he : l = lastLine := by
      apply Fin.ext
      change l.val = 584
      have := l.isLt
      omega
    subst l
    exact representative_hline p h
#print axioms hline
end Balanced
end DegreeDiameter.Portfolio.EvenQ8SourceFull
