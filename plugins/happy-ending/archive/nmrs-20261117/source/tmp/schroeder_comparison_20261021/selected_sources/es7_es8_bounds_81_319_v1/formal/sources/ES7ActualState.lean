import ES7Final

namespace ES7ActualState
open ES8ActualRanks ES8BalancedGeometry ES7Geometry

abbrev Label := Nat × Nat

def Below (q r : Label) : Prop := q.1≤r.1 ∧ q.2≤r.2

/-- Source-specific convention: cup first, cap second. -/
noncomputable def label (cup : Nat→Nat→Nat→Bool) (u v : Nat) : Label :=
  (rank cup true u v-1,rank cup false u v-1)

/-- Actual incoming state, restricted to positive grid coordinates. -/
def Incoming (cup : Nat→Nat→Nat→Bool) (v : Nat) (q : Label) : Prop :=
  1≤q.1 ∧ 1≤q.2 ∧ ∃ u, u<v ∧ Below q (label cup u v)

theorem label_positive (cup : Nat→Nat→Nat→Bool) (u v : Nat) (uv : u<v) :
    1≤(label cup u v).1 ∧ 1≤(label cup u v).2 := by
  have r := (length_bounds (rank_attained cup true u v uv)).1
  have b := (length_bounds (rank_attained cup false u v uv)).1
  simp only [label]; omega

theorem label_growth (cup : Nat→Nat→Nat→Bool) (t u v : Nat) (tu : t<u) (uv : u<v) :
    (cup t u v=true → (label cup t u).1<(label cup u v).1) ∧
    (cup t u v=false → (label cup t u).2<(label cup u v).2) := by
  have r := (length_bounds (rank_attained cup true t u tu)).1
  have b := (length_bounds (rank_attained cup false t u tu)).1
  constructor
  · intro h; have g := rank_growth cup true t u v tu uv h; simp only [label]; omega
  · intro h; have g := rank_growth cup false t u v tu uv h; simp only [label]; omega

theorem label_difference (cup : Nat→Nat→Nat→Bool) (u v : Nat) (uv : u<v) :
    Incoming cup v (label cup u v) ∧ ¬Incoming cup u (label cup u v) := by
  refine ⟨⟨(label_positive cup u v uv).1,(label_positive cup u v uv).2,u,uv,le_rfl,le_rfl⟩,?_⟩
  rintro ⟨_,_,t,tu,h⟩
  have g := label_growth cup t u v tu uv
  cases hc : cup t u v with
  | true => have := g.1 hc; exact (not_le_of_gt this) h.1
  | false => have := g.2 hc; exact (not_le_of_gt this) h.2

theorem incoming_injective (cup : Nat→Nat→Nat→Bool) : Function.Injective (Incoming cup) := by
  intro u v eq
  by_contra ne
  rcases lt_or_gt_of_ne ne with uv | vu
  · have h := label_difference cup u v uv
    exact h.2 (eq ▸ h.1)
  · have h := label_difference cup v u vu
    exact h.2 (eq.symm ▸ h.1)

theorem inclusion_order (cup : Nat→Nat→Nat→Bool) (u v : Nat) (ne : u≠v)
    (sub : ∀ q, Incoming cup u q → Incoming cup v q) : u<v := by
  by_contra h
  have vu : v<u := by omega
  have witness := label_difference cup v u vu
  exact witness.2 (sub _ witness.1)

theorem incoming_downclosed (cup : Nat→Nat→Nat→Bool) {v : Nat} {q r : Label}
    (member : Incoming cup v r) (positive : 1≤q.1 ∧ 1≤q.2) (below : Below q r) :
    Incoming cup v q := by
  obtain ⟨_,_,u,uv,h⟩ := member
  exact ⟨positive.1,positive.2,u,uv,le_trans below.1 h.1,le_trans below.2 h.2⟩

theorem restricted_bounds {n} (c : Configuration n)
    (noCap : ¬(colorConfig c.cup true).HasNCap 5 (Finset.range n))
    (noCup : ¬(colorConfig c.cup true).HasNCup 6 (Finset.range n))
    {u v : Nat} (uv : u<v) (vn : v<n) :
    (label c.cup u v).1≤4 ∧ (label c.cup u v).2≤3 := by
  have r := rank_lt_of_avoids n c.cup true 6 (by omega) (avoids_of_no_cup n 6 c.cup noCup) u v uv vn
  have b := rank_lt_of_avoids n c.cup false 5 (by omega) (avoids_of_no_cap n 5 c.cup noCap) u v uv vn
  simp only [label]; omega

theorem incoming_bounds {n} (c : Configuration n)
    (noCap : ¬(colorConfig c.cup true).HasNCap 5 (Finset.range n))
    (noCup : ¬(colorConfig c.cup true).HasNCup 6 (Finset.range n))
    {v : Nat} (vn : v<n) {q : Label} (member : Incoming c.cup v q) : q.1≤4 ∧ q.2≤3 := by
  obtain ⟨_,_,u,uv,h⟩ := member
  have b := restricted_bounds c noCap noCup uv vn
  exact ⟨le_trans h.1 b.1,le_trans h.2 b.2⟩

/-- A maximal corner is attained by an actual incoming pair. -/
theorem corner_attained (cup : Nat→Nat→Nat→Bool) {v : Nat} {q : Label}
    (member : Incoming cup v q)
    (maximal : ∀ r, Incoming cup v r → Below q r → r=q) :
    ∃ u, u<v ∧ label cup u v=q ∧ ¬Incoming cup u q := by
  obtain ⟨_,_,u,uv,below⟩ := member
  have h := label_difference cup u v uv
  have eq := maximal _ h.1 below
  exact ⟨u,uv,eq,eq ▸ h.2⟩

/-- Maximal pair ranks have a shared, actual predecessor attaining one less.
This is stronger than choosing unrelated threshold witnesses. -/
theorem rank_predecessor (cup : Nat→Nat→Nat→Bool) (color : Bool)
    (u v : Nat) (uv : u<v) (large : 3≤rank cup color u v) :
    ∃ t, t<u ∧ cup t u v=color ∧ rank cup color t u+1=rank cup color u v := by
  have path := rank_attained cup color u v uv
  generalize he : rank cup color u v = r at path large
  cases path with
  | pair h => omega
  | @step t x y l prior stepOrder same =>
    have tu := (length_bounds prior).2.2
    have low := rank_ge prior
    have high := rank_growth cup color t u v tu uv same
    exact ⟨t,tu,same,by omega⟩

/-- A cup-coordinate attainment witness has the exact predecessor label. -/
theorem cup_predecessor (cup : Nat→Nat→Nat→Bool) (u v : Nat) (uv : u<v)
    (large : 2≤(label cup u v).1) :
    ∃ t, t<u ∧ cup t u v=true ∧ (label cup t u).1+1=(label cup u v).1 ∧
      Incoming cup u (label cup t u) ∧ ¬Incoming cup t (label cup t u) := by
  have high : 3≤rank cup true u v := by simp only [label] at large; omega
  obtain ⟨t,tu,col,eq⟩ := rank_predecessor cup true u v uv high
  have low := (length_bounds (rank_attained cup true t u tu)).1
  exact ⟨t,tu,col,by simp only [label]; omega,label_difference cup t u tu⟩

theorem cap_predecessor (cup : Nat→Nat→Nat→Bool) (u v : Nat) (uv : u<v)
    (large : 2≤(label cup u v).2) :
    ∃ t, t<u ∧ cup t u v=false ∧ (label cup t u).2+1=(label cup u v).2 ∧
      Incoming cup u (label cup t u) ∧ ¬Incoming cup t (label cup t u) := by
  have high : 3≤rank cup false u v := by simp only [label] at large; omega
  obtain ⟨t,tu,col,eq⟩ := rank_predecessor cup false u v uv high
  have low := (length_bounds (rank_attained cup false t u tu)).1
  exact ⟨t,tu,col,by simp only [label]; omega,label_difference cup t u tu⟩

#print axioms corner_attained
#print axioms rank_predecessor
#print axioms cup_predecessor
#print axioms cap_predecessor
end ES7ActualState
