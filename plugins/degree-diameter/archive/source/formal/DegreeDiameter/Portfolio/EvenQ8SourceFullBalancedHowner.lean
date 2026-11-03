import DegreeDiameter.Portfolio.EvenQ8SourceFullData
namespace DegreeDiameter.Portfolio.EvenQ8SourceFull
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Balanced
open DegreeDiameter.Portfolio.EvenQ8Source.Balanced
open DegreeDiameter.Portfolio.EvenQ8Source
def restrictedHelper (j : Fin 64) : Helper := ⟨j.val,by omega⟩
theorem howner_certificate : ∀ (j : Fin 64) (i : Fin 9),
    spreadOwner (linePoint (spread (restrictedHelper j)) i) = restrictedHelper j := by decide
theorem howner : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  intro p j h
  by_cases hj : j.val < 64
  · let small : Fin 64 := ⟨j.val,hj⟩
    have he : restrictedHelper small = j := Fin.ext rfl
    obtain ⟨i,hi⟩ := h
    rw [←hi]
    have hc := howner_certificate small i
    rw [he] at hc
    exact hc.symm
  · have he : j = lastSpread := by
      apply Fin.ext
      change j.val = 64
      have := j.isLt
      omega
    subst j
    exact representative_howner p h
#print axioms howner
end Balanced
end DegreeDiameter.Portfolio.EvenQ8SourceFull
