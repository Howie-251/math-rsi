import ES7ActualState

namespace ES7PacketSemantics
open ES8Geometry ES8BalancedGeometry ES8BaekGeometry ES8ThreeChain

/-- The middle ray's determinant is a positive weighted combination of the two
outer determinants when abscissae are ordered. -/
theorem fan_identity (a b c d : Point) :
    (d.1-a.1)*orient a b c + (b.1-a.1)*orient a c d = (c.1-a.1)*orient a b d := by
  unfold orient
  ring

theorem fan {n} (c : Configuration n) {a b d e : Nat}
    (ab : a<b) (bd : b<d) (de : d<e) (en : e<n) (color : Bool)
    (left : c.cup a b d=color) (right : c.cup a d e=color) : c.cup a b e=color := by
  have an : a<n := by omega
  have bn : b<n := by omega
  have dn : d<n := by omega
  have pos1 := sub_pos.mpr (pointAt_order c an en (by omega : a<e))
  have pos2 := sub_pos.mpr (pointAt_order c an bn ab)
  have pos3 := sub_pos.mpr (pointAt_order c an dn (by omega : a<d))
  have identity := fan_identity (pointAt c a) (pointAt c b) (pointAt c d) (pointAt c e)
  cases color with
  | true =>
    have h1 := (cup_sign c a b d an bn dn).mp left
    have h2 := (cup_sign c a d e an dn en).mp right
    have positive := add_pos (mul_pos pos1 h1) (mul_pos pos2 h2)
    rw [identity] at positive
    exact (cup_sign c a b e an bn en).mpr ((mul_pos_iff_of_pos_left pos3).mp positive)
  | false =>
    have h1 := (cap_sign c a b d an bn dn ab bd).mp (by simp [left])
    have h2 := (cap_sign c a d e an dn en (by omega) de).mp (by simp [right])
    have negative := add_neg (mul_neg_of_pos_of_neg pos1 h1) (mul_neg_of_pos_of_neg pos2 h2)
    rw [identity] at negative
    have sign : orient (pointAt c a) (pointAt c b) (pointAt c e)<0 := by
      by_contra h
      have nn := mul_nonneg (le_of_lt pos3) (le_of_not_gt h)
      linarith
    have result := (cap_sign c a b e an bn en ab (by omega)).mpr sign
    simpa using result

/-- The four packet primitive clauses, with every chronology premise explicit.
The names x,y,z,w refer to abc,abd,acd,bcd in that actual order. -/
theorem packet_clauses {n} (c : Configuration n) {a b d e : Nat}
    (ab : a<b) (bd : b<d) (de : d<e) (en : e<n) :
    (c.cup a b d=true ∨ c.cup a b e=false ∨ c.cup a d e=true) ∧
    (c.cup a b d=false ∨ c.cup a b e=true ∨ c.cup a d e=false) ∧
    (c.cup a b d=true ∨ c.cup a d e=false ∨ c.cup b d e=true) ∧
    (c.cup a b d=false ∨ c.cup a d e=true ∨ c.cup b d e=false) := by
  have f := fan c ab bd de en
  have g := four c ab bd de en
  have ff := f false
  have ft := f true
  have gf := g false
  have gt := g true
  cases h1 : c.cup a b d <;> cases h2 : c.cup a b e <;>
    cases h3 : c.cup a d e <;> cases h4 : c.cup b d e <;> simp_all

#print axioms packet_clauses
end ES7PacketSemantics
