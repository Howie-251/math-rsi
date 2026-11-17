import ES7ClosureCorePaths
namespace ES7FiniteRanks
open ES7ActualState ES8ActualRanks

/-- Executable longest ending-path rank. Its recursion ranges over every
actual predecessor, not over a selected or favourable subset. -/
def rankCode (cup : Nat→Nat→Nat→Bool) (b : Bool) (u v : Nat) : Nat :=
  max 2 ((Finset.range u).sup fun t=>if h : t < u then (if cup t u v=b then rankCode cup b t u+1 else 0) else 0)
termination_by u

theorem rankCode_eq (cup : Nat→Nat→Nat→Bool) (b : Bool) (u v : Nat) (uv : u < v) :
    rankCode cup b u v=rank cup b u v := by
  induction u using Nat.strong_induction_on generalizing v with
  | h u ih =>
    rw [rankCode]
    have lower := (length_bounds (rank_attained cup b u v uv)).1
    apply Nat.le_antisymm
    · apply max_le lower
      apply Finset.sup_le
      intro t ht
      have tu := Finset.mem_range.mp ht
      rw [dif_pos tu]
      split
      next same => rw [ih t tu u tu]; exact Nat.succ_le_of_lt (rank_growth cup b t u v tu uv same)
      next diff => exact Nat.zero_le _
    · by_cases small : rank cup b u v=2
      · rw [small]; exact le_max_left _ _
      · obtain ⟨t,tu,same,eq⟩ := rank_predecessor cup b u v uv (by omega)
        have bound := Finset.le_sup (s:=Finset.range u)
          (f:=fun t=>if h : t < u then (if cup t u v=b then rankCode cup b t u+1 else 0) else 0) (Finset.mem_range.mpr tu)
        rw [dif_pos tu,if_pos same,ih t tu u tu,eq] at bound
        exact bound.trans (le_max_right _ _)

def labelCode (cup : Nat→Nat→Nat→Bool) (u v : Nat) : Label :=
  (rankCode cup true u v-1,rankCode cup false u v-1)

theorem labelCode_eq (cup : Nat→Nat→Nat→Bool) (u v : Nat) (uv : u < v) :
    labelCode cup u v=label cup u v := by
  simp only [labelCode,label,rankCode_eq cup true u v uv,rankCode_eq cup false u v uv]

def down (q : Label) : Finset Label := (Finset.Icc 1 q.1)×ˢ(Finset.Icc 1 q.2)
def stateCode (cup : Nat→Nat→Nat→Bool) (v : Nat) : Finset Label :=
  (Finset.range v).biUnion (fun u=>down (labelCode cup u v))

theorem stateCode_spec (cup : Nat→Nat→Nat→Bool) (v : Nat) (q : Label) :
    q∈stateCode cup v ↔ Incoming cup v q := by
  simp only [stateCode,Finset.mem_biUnion,Finset.mem_range,down,Finset.mem_product,Finset.mem_Icc,Incoming,Below]
  constructor
  · rintro ⟨u,uv,⟨p1,b1⟩,⟨p2,b2⟩⟩
    rw [labelCode_eq cup u v uv] at b1 b2
    exact ⟨p1,p2,u,uv,b1,b2⟩
  · rintro ⟨p1,p2,u,uv,b1,b2⟩
    exact ⟨u,uv,by rw [labelCode_eq cup u v uv]; exact ⟨⟨p1,b1⟩,⟨p2,b2⟩⟩⟩

theorem rankCode_congr (cup cap : Nat→Nat→Nat→Bool) (b : Bool) (u v : Nat) (uv : u < v)
    (agree : ∀a d e,a < d → d < e → e ≤ v → cup a d e=cap a d e) :
    rankCode cup b u v=rankCode cap b u v := by
  induction u using Nat.strong_induction_on generalizing v with
  | h u ih =>
    rw [rankCode,rankCode]
    congr 1
    apply Finset.sup_congr rfl
    intro t ht
    have tu := Finset.mem_range.mp ht
    rw [dif_pos tu,dif_pos tu,agree t u v tu uv le_rfl]
    by_cases same : cap t u v=b
    · rw [if_pos same,if_pos same,ih t tu u tu (fun a d e ad de eu=>agree a d e ad de (eu.trans (le_of_lt uv)))]
    · simp [same]

theorem stateCode_congr (cup cap : Nat→Nat→Nat→Bool) (v : Nat)
    (agree : ∀a d e,a < d → d < e → e ≤ v → cup a d e=cap a d e) :
    stateCode cup v=stateCode cap v := by
  apply Finset.biUnion_congr rfl
  intro u hu
  have uv := Finset.mem_range.mp hu
  congr 1
  simp only [labelCode,rankCode_congr cup cap true u v uv agree,rankCode_congr cup cap false u v uv agree]
end ES7FiniteRanks
