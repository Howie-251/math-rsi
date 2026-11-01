import Aris4Math.ThirtyThree.DoubleLockAt
import Aris4Math.ProfileApplication

/-! Eleven actual double-lock cases on twenty vertices. The remaining (8,8)
case requires the separate stronger ordinary-link deletion. -/

namespace Aris4Math.ThirtyThree.TwentyStandard

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.LinkWeightCertificates Aris4Math.LinkDeletion
open Aris4Math.ThirtyThree.DoubleLockAt

/-- Finite degree alternatives obtained by the separate structural selection. -/
def standardDegrees : List (ℕ × ℕ) :=
  [(5,5), (5,6), (5,7), (5,8), (6,6), (6,7), (6,8), (6,9), (7,7), (7,8), (7,9)]

def firstPosition (e : ℕ) : ℕ := if e = 9 then 11 else 10

def profile (d e : ℕ) : Numeric.Profile :=
  profileAt 20 (firstPosition e) (firstPosition e + 1) d e
    [firstPosition e, firstPosition e + 1]

def linkQ (d : ℕ) : ℕ := (4*d - 19 + 2)/3

def leftWeight (e : ℕ) : ℚ := if e = 9 then 70/7293 else 21/2210

def rightWeight (e : ℕ) : ℚ := if e = 9 then 5/663 else 21/2210

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Finite exact arithmetic on eleven profiles: geometry, strict values and
per-unordered-pair lower weights. The real-H connection is proved below. -/
theorem standard_certificates : ∀ de ∈ standardDegrees,
    1 ≤ firstPosition de.2 ∧ firstPosition de.2 + 1 ≤ 20 ∧
    Numeric.validProfile (profile de.1 de.2) 33 ∧
    Numeric.totalBound (profile de.1 de.2) < 1 ∧
    0 ≤ leftWeight de.2 ∧ 0 ≤ rightWeight de.2 ∧
    IncidentWeightBound (profile de.1 de.2) (firstPosition de.2) (leftWeight de.2) ∧
    IncidentWeightBound (profile de.1 de.2) (firstPosition de.2 + 1) (rightWeight de.2) ∧
    Numeric.deduction (profile de.1 de.2) (firstPosition de.2) ≤
      (linkQ de.1 : ℚ) * leftWeight de.2 ∧
    Numeric.deduction (profile de.1 de.2) (firstPosition de.2 + 1) ≤
      (linkQ de.2 : ℚ) * rightWeight de.2 := by
  unfold Numeric.validProfile
  decide +kernel

/-- Any actual codegree-one pair in one of the eleven degree alternatives gives
Property B. All input multiplicities and both link deletions are discharged. -/
theorem propertyB_of_standard_pair (H : Simple5Hypergraph (Fin 20))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 20) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (degrees : (H.degree x, H.degree y) ∈ standardDegrees) : PropertyB H := by
  obtain ⟨ha,hb,hvalid,hstrict,hcl,hcr,hwl,hwr,hdl,hdr⟩ :=
    standard_certificates (H.degree x, H.degree y) degrees
  dsimp only [Prod.fst, Prod.snd] at ha hb hvalid hstrict hcl hcr hwl hwr hdl hdr
  let a := firstPosition (H.degree y)
  have hab : a < a+1 := by omega
  have real := realizes_profile_at H edges33 ha hab hb x y hne codegree1 [a,a+1] hvalid
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (positionsAt 20 a (a+1) ha hab hb)
    (profile (H.degree x) (H.degree y)) real rfl
  · intro j _
    fin_cases j
    · change Numeric.deduction (profile (H.degree x) (H.degree y)) (a-1+1) ≤
          ∑ d ∈ directedBadPairs H x,
            typeWeight (profile (H.degree x) (H.degree y))
              (positionType (twoVertices x y hne) (positionsAt 20 a (a+1) ha hab hb)) (a-1+1) d
      rw [Nat.sub_add_cancel ha]
      apply realized_center_deduction H cover (twoVertices x y hne)
        (positionsAt 20 a (a+1) ha hab hb) (profile (H.degree x) (H.degree y)) real
        0 a (linkQ (H.degree x)) (leftWeight (H.degree y))
      · change a - 1 + 1 = a
        exact Nat.sub_add_cancel ha
      · change linkQ (H.degree x) ≤ (4 * H.degree x - (20-1) + 2)/3
        exact le_rfl
      · exact hcl
      · exact hwl
      · exact hdl
    · change Numeric.deduction (profile (H.degree x) (H.degree y)) (a+1-1+1) ≤
          ∑ d ∈ directedBadPairs H y,
            typeWeight (profile (H.degree x) (H.degree y))
              (positionType (twoVertices x y hne) (positionsAt 20 a (a+1) ha hab hb)) (a+1-1+1) d
      simp only [Nat.add_sub_cancel]
      apply realized_center_deduction H cover (twoVertices x y hne)
        (positionsAt 20 a (a+1) ha hab hb) (profile (H.degree x) (H.degree y)) real
        1 (a+1) (linkQ (H.degree y)) (rightWeight (H.degree y))
      · change a+1 - 1 + 1 = a+1
        omega
      · change linkQ (H.degree y) ≤ (4 * H.degree y - (20-1) + 2)/3
        exact le_rfl
      · exact hcr
      · exact hwr
      · exact hdr
  · exact hstrict

end Aris4Math.ThirtyThree.TwentyStandard

#print axioms Aris4Math.ThirtyThree.TwentyStandard.standard_certificates
#print axioms Aris4Math.ThirtyThree.TwentyStandard.propertyB_of_standard_pair
