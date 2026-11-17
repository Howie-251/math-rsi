import ES7CorePaths
import ES7AmbientRemap

set_option linter.unusedSimpArgs false
namespace ES7ThroughMeaning
open ES8BalancedGeometry ES8ActualRanks ES8ResidualRanks ES7BalancedEndpoints
open ES7OrderedContract ES7AmbientRemap ES7CorePaths

def coreSet (f : Nat→Nat) : Finset Nat := (Finset.Ico 4 18).image f

structure Model (c : Configuration n) (f : Nat→Nat) : Prop where
  ordered : ∀ a b, a < b → b < 22 → f a < f b
  bounded : ∀ a, a < 22 → f a < n
  noSix : NoSix c.cup (Finset.range n)
  noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)
  through : Through c.cup (Finset.range n) (coreSet f)
  cups : ∀ i j k, i < j → j < k → k < 22 → (k ≤ 4 ∨ 17 ≤ i) → c.cup (f i) (f j) (f k)=true

variable {n : Nat} {c : Configuration n} {f : Nat→Nat}

theorem core_mem (f : Nat→Nat) (lo : 4 ≤ i) (hi : i < 18) : f i∈coreSet f :=
  Finset.mem_image.mpr ⟨i,Finset.mem_Ico.mpr ⟨lo,hi⟩,rfl⟩

theorem core_bounded (m : Model c f) : coreSet f⊆Finset.range n := by
  intro v hv
  obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hv
  exact Finset.mem_range.mpr (m.bounded i (by have := Finset.mem_Ico.mp hi; omega))

theorem order_reflect (m : Model c f) (ai : a < 22) (bi : b < 22)
    (h : f a < f b) : a < b := by
  by_contra contra
  rcases lt_or_eq_of_le (le_of_not_gt contra) with ba|eq
  · have bad := m.ordered b a ba ai; omega
  · subst a; omega

inductive Variable where
  | ambient (v : Var)
  | core (right b : Bool) (k i j : Nat)
  | witness (right b : Bool) (k i j t : Nat)
  deriving DecidableEq, Repr

def CoreRank (cup : Nat→Nat→Nat→Bool) (f : Nat→Nat) (right b : Bool) (k i j : Nat) : Prop :=
  if right then Start cup b (coreSet f) (f i) (f j) k else End cup b (coreSet f) (f i) (f j) k

def predecessor (cup : Nat→Nat→Nat→Bool) (f : Nat→Nat) (right b : Bool) (k i j t : Nat) : Prop :=
  if right then CoreRank cup f right b (k-1) j t else CoreRank cup f right b (k-1) t i

def turnValue (cup : Nat→Nat→Nat→Bool) (f : Nat→Nat) (right b : Bool) (i j t : Nat) : Prop :=
  if right then cup (f i) (f j) (f t)=b else cup (f t) (f i) (f j)=b

def meaning (c : Configuration n) (f : Nat→Nat) : Variable→Prop
  | .ambient v => Meaning c (variableMap f v)
  | .core right b k i j => CoreRank c.cup f right b k i j
  | .witness right b k i j t => predecessor c.cup f right b k i j t ∧ turnValue c.cup f right b i j t

abbrev Literal := Variable×Bool
def positive (v : Variable) : Literal := (v,true)
def negative (v : Variable) : Literal := (v,false)
def color (b : Bool) (i j k : Nat) : Literal := (.ambient (.C i j k),b)
def notColor (b : Bool) (i j k : Nat) : Literal := (.ambient (.C i j k),!b)
def preVar (r b : Bool) (k i j t : Nat) : Variable :=
  if r then .core r b (k-1) j t else .core r b (k-1) t i
def witnessLit (r b : Bool) (k i j t : Nat) : Literal :=
  if k=3 then (if r then color b i j t else color b t i j)
  else positive (.witness r b k i j t)
def negLit (v : Literal) : Literal := (v.1,!v.2)
def predecessors (r : Bool) (i j : Nat) : List Nat :=
  (List.range 18).filter (fun t => decide (4 ≤ t ∧ if r then j < t else t < i))

def LitTrue (c : Configuration n) (f : Nat→Nat) (v : Literal) : Prop :=
  if v.2 then meaning c f v.1 else ¬meaning c f v.1
def Satisfied (c : Configuration n) (f : Nat→Nat) (cl : List Literal) : Prop := ∃v∈cl,LitTrue c f v

theorem color_spec (c : Configuration n) (f : Nat→Nat) (b i j k) :
    LitTrue c f (color b i j k) ↔ c.cup (f i) (f j) (f k)=b := by
  cases b <;> simp [LitTrue,color,meaning,Meaning,variableMap]
theorem neg_spec (c : Configuration n) (f : Nat→Nat) (v : Literal) :
    LitTrue c f (negLit v) ↔ ¬LitTrue c f v := by
  classical
  rcases v with ⟨v,b⟩
  cases b <;> simp [LitTrue,negLit]
theorem pos_spec (c : Configuration n) (f : Nat→Nat) (v : Variable) :
    LitTrue c f (positive v) ↔ meaning c f v := by simp [LitTrue,positive]
theorem negative_spec (c : Configuration n) (f : Nat→Nat) (v : Variable) :
    LitTrue c f (negative v) ↔ ¬meaning c f v := by simp [LitTrue,negative]

def PairValid (i j : Nat) : Prop := 4 ≤ i ∧ i < j ∧ j < 18
def RankValid (b : Bool) (k i j : Nat) : Prop := PairValid i j ∧ 3 ≤ k ∧ k ≤ (if b then 5 else 3)
def PreValid (r : Bool) (i j t : Nat) : Prop := PairValid i j ∧ 4 ≤ t ∧ t < 18 ∧ (if r then j < t else t < i)
instance (i j) : Decidable (PairValid i j) := inferInstanceAs (Decidable (4 ≤ i ∧ i < j ∧ j < 18))
instance (b k i j) : Decidable (RankValid b k i j) := inferInstanceAs (Decidable (PairValid i j ∧ 3 ≤ k ∧ k ≤ (if b then 5 else 3)))
instance (r i j t) : Decidable (PreValid r i j t) := inferInstanceAs (Decidable (PairValid i j ∧ 4 ≤ t ∧ t < 18 ∧ (if r then j < t else t < i)))

theorem predecessor_mem (r : Bool) (i j t : Nat) : t∈predecessors r i j ↔ 4 ≤ t ∧ t < 18 ∧ (if r then j < t else t < i) := by
  simp [predecessors,and_assoc,and_left_comm,and_comm]

theorem rank_base (m : Model c f) (r b : Bool) (valid : PairValid i j) : CoreRank c.cup f r b 2 i j := by
  obtain ⟨lo,ij,hi⟩ := valid
  have ord := m.ordered i j ij (by omega)
  have im := core_mem f lo (by omega)
  have jm := core_mem f (by omega) hi
  cases r <;> exact .pair im jm ord

theorem rank_step (m : Model c f) (r b : Bool) (k i j t : Nat)
    (valid : PreValid r i j t)
    (pre : predecessor c.cup f r b k i j t) (turn : turnValue c.cup f r b i j t)
    (lo : 3 ≤ k) : CoreRank c.cup f r b k i j := by
  obtain ⟨⟨il,ij,jh⟩,tl,th,ord⟩ := valid
  have eq : k-1+1=k := by omega
  cases r with
  | false => simpa only [eq,CoreRank,Bool.false_eq_true,if_false] using End.step pre (core_mem f (by omega) jh) (m.ordered i j ij (by omega)) turn
  | true => simpa only [eq,CoreRank,if_true] using Start.step pre (core_mem f il (by omega)) (m.ordered i j ij (by omega)) turn

theorem witness_forward (m : Model c f) (r b : Bool) (k i j t : Nat)
    (valid : PreValid r i j t) (lo : 3 ≤ k)
    (h : LitTrue c f (witnessLit r b k i j t)) : CoreRank c.cup f r b k i j := by
  by_cases eq : k=3
  · subst k
    have turn : turnValue c.cup f r b i j t := by
      cases r <;> simpa only [witnessLit,ite_true,Bool.false_eq_true,if_false,if_true,color_spec,turnValue] using h
    apply rank_step m r b 3 i j t valid _ turn (by omega)
    obtain ⟨⟨il,ij,jh⟩,tl,th,ord⟩ := valid
    cases r with
    | false => exact rank_base m false b ⟨tl,ord,by omega⟩
    | true => exact rank_base m true b ⟨by omega,ord,th⟩
  · have hp : predecessor c.cup f r b k i j t ∧ turnValue c.cup f r b i j t := by
      simpa only [witnessLit,if_neg eq,pos_spec,meaning] using h
    exact rank_step m r b k i j t valid hp.1 hp.2 lo

theorem rank_attain (m : Model c f) (r b : Bool) (k i j : Nat)
    (valid : RankValid b k i j) (h : CoreRank c.cup f r b k i j) :
    ∃ t∈predecessors r i j, LitTrue c f (witnessLit r b k i j t) := by
  obtain ⟨pair,lo,hi⟩ := valid
  have ih : i < 22 := by have := pair.2; omega
  have jh : j < 22 := by have := pair.2; omega
  have attained : ∃ t∈coreSet f, (if r then f j < t else t < f i) ∧
      (if r then Start c.cup b (coreSet f) (f j) t (k-1) else End c.cup b (coreSet f) t (f i) (k-1)) ∧
      (if r then c.cup (f i) (f j) t=b else c.cup t (f i) (f j)=b) := by
    cases r with
    | false => exact end_attain h lo
    | true => exact start_attain h lo
  obtain ⟨value,member,ord,prior,turn⟩ := attained
  obtain ⟨t,ht,rfl⟩ := Finset.mem_image.mp member
  obtain ⟨tl,th⟩ := Finset.mem_Ico.mp ht
  have relative : if r then j < t else t < i := by
    cases r with
    | false => exact order_reflect m (by omega) ih ord
    | true => exact order_reflect m jh (by omega) ord
  refine ⟨t,(predecessor_mem r i j t).mpr ⟨tl,th,relative⟩,?_⟩
  by_cases eq : k=3
  · subst k
    cases r <;> simpa only [witnessLit,ite_true,Bool.false_eq_true,if_false,if_true,color_spec] using turn
  · simp only [witnessLit,if_neg eq,pos_spec,meaning]
    constructor
    · cases r <;> exact prior
    · exact turn

theorem rank_nesting (r b : Bool) (k i j : Nat) (lo : 3 ≤ k)
    (h : CoreRank cup f r b k i j) : CoreRank cup f r b (k-1) i j := by
  cases r with
  | false => exact end_truncate h _ (by omega) (by omega)
  | true => exact start_truncate h _ (by omega) (by omega)

theorem ambient_extension (m : Model c f) (r b : Bool) (k i j : Nat)
    (valid : RankValid b k i j) (h : CoreRank c.cup f r b k i j) :
    Meaning c (variableMap f (rankVar r b (k+(if b then 0 else 1)) i j)) := by
  cases b with
  | true =>
    cases r with
    | false => exact end_ambient h
    | true => exact start_ambient (core_bounded m) h
  | false =>
    have eq : k=3 := by have := valid.2; simp only [Bool.false_eq_true,if_false] at this; omega
    subst k
    cases r with
    | false => exact cap_three_left m.noSix (core_bounded m) m.through h
    | true => exact cap_three_right m.noSix (core_bounded m) m.through h

theorem pair_extension (m : Model c f) (r : Bool) (i j : Nat) (valid : PairValid i j) :
    Meaning c (variableMap f (rankVar r false 3 i j)) := by
  obtain ⟨lo,ij,hi⟩ := valid
  have im := core_mem f lo (by omega)
  have jm := core_mem f (by omega) hi
  have ord := m.ordered i j ij (by omega)
  cases r with
  | false => exact cap_pair_left m.noSix (core_bounded m) m.through im jm ord
  | true => exact cap_pair_right m.noSix (core_bounded m) m.through im jm ord

theorem core_maximum (m : Model c f) (r b : Bool) (i j k : Nat)
    (valid : 4 ≤ i ∧ i < j ∧ j < k ∧ k < 18)
    (p : CoreRank c.cup f r b (if b then 5 else 3) (if r then j else i) (if r then k else j))
    (turn : c.cup (f i) (f j) (f k)=b) : False := by
  obtain ⟨lo,ij,jk,kh⟩ := valid
  have im := core_mem f lo (by omega)
  have km := core_mem f (by omega) kh
  have fij := m.ordered i j ij (by omega)
  have fjk := m.ordered j k jk (by omega)
  cases b <;> cases r
  · exact end_maximum m.noSix (core_bounded m) m.through (End.step p km fjk turn)
  · exact start_maximum m.noSix (core_bounded m) m.through (Start.step p im fij turn)
  · exact end_maximum m.noSix (core_bounded m) m.through (End.step p km fjk turn)
  · exact start_maximum m.noSix (core_bounded m) m.through (Start.step p im fij turn)

end ES7ThroughMeaning
