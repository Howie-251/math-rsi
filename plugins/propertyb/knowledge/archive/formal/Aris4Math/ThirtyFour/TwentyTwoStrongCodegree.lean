import Aris4Math.ThirtyFour.TwentyTwoStrongCoverage
import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyThreeSelection
namespace Aris4Math.ThirtyFour.TwentyTwoStrongCodegree
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt
open Aris4Math.ThirtyThree.TripleProfiles
open Aris4Math.ThirtyThree.TwentyThreeSelection (sevenVertices mem_sevenVertices)
open NineteenPairs
set_option maxHeartbeats 0
set_option maxRecDepth 100000

theorem pair_certificates : ∀ l : Fin 8, 4≤l.val →
    Numeric.validProfile (pairProfile 22 1 13 7 7 l.val []) 34 ∧
    Numeric.totalBound (pairProfile 22 1 13 7 7 l.val [])<1 := by
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_pair (H : Simple5Hypergraph (Fin 22)) (size : H.edges.card=34)
    (x y : Fin 22) (xy : x≠y) (dx : H.degree x=7) (dy : H.degree y=7)
    (high : 4≤H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at upper
  obtain ⟨valid,strict⟩ := pair_certificates ⟨H.codegree x y,by omega⟩ high
  have real := realizes_pair_profile H size (by decide : 1≤1) (by decide : 1<13)
    (by decide : 13≤22) x y xy [] (by simpa only [dx,dy] using valid)
  apply ProfileApplication.propertyB_of_uncorrected_profile H (twoVertices x y xy)
    (positionsAt 22 1 13 (by decide) (by decide) (by decide))
    (pairProfile 22 1 13 (H.degree x) (H.degree y) (H.codegree x y) []) real rfl rfl
  simpa only [dx,dy] using strict

/-- An actual degree-seven pair is small, after the proved strict branches. -/
theorem codegree_le (H : Simple5Hypergraph (Fin 22)) (cover : H.PairCovering)
    (size : H.edges.card=34) (many : 3≤(sevenVertices H).card) (noB : ¬PropertyB H)
    (x y : Fin 22) (xy : x≠y) (dx : H.degree x=7) (dy : H.degree y=7) :
    H.codegree x y≤2 := by
  have upper (a b : Fin 22) (ab : a≠b) (da : H.degree a=7) (db : H.degree b=7) :
      H.codegree a b≤3 := by
    by_contra h
    exact noB (propertyB_of_pair H size a b ab da db (by omega))
  have ux := upper x y xy dx dy
  by_contra fail
  have high : H.codegree x y=3 := by omega
  have exists_third : ∃ z∈sevenVertices H, z≠x ∧ z≠y := by
    by_contra! h
    have sub : sevenVertices H⊆({x,y} : Finset (Fin 22)) := by
      intro z hz
      by_cases zx : z=x
      · simp [zx]
      · simp [h z hz zx]
    have bound := (Finset.card_le_card sub).trans Finset.card_le_two
    omega
  obtain ⟨z,hz,zx,zy⟩ := exists_third
  have dz := (mem_sevenVertices H z).mp hz
  let f := threeVertices x y z xy zx.symm zy.symm
  have degrees : ∀ j, H.degree (f j)=7 := by
    intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
  apply noB
  exact TwentyTwoStrongCoverage.propertyB_of_triple H cover size f degrees
    (fun i j ij => upper (f i) (f j) (f.injective.ne ij) (degrees i) (degrees j)) high
end Aris4Math.ThirtyFour.TwentyTwoStrongCodegree
#print axioms Aris4Math.ThirtyFour.TwentyTwoStrongCodegree.codegree_le
