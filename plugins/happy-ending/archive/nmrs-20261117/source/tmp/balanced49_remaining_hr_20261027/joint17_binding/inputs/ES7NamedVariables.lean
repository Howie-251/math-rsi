import ES7NamedCounting

namespace ES7NamedVariables
open ES7NamedGeometry ES7ActualState ES8BalancedGeometry ES7ClauseLogic

inductive Variable where
  | active (i : Nat)
  | order (i j : Nat)
  | color (i j k : Nat)
  | pair (i j x y : Nat)
  | path (b : Bool) (k s i j : Nat)
  | endpoints (b : Bool) (k s j : Nat)
  | counter (xs : List Nat) (k : Nat)
  deriving DecidableEq, Repr

def meaning (m : Model c N states) : Variable→Prop
  | .active i => i∈m.active
  | .order i j => m.key i < m.key j
  | .color i j k => Cup m i j k=true
  | .pair i j x y => Pair m i j (x,y)
  | .path b k s i j => NamedPath m b k s i j
  | .endpoints b k s j => NamedEndpoint m b k s j
  | .counter xs k => k ≤ ES7NamedCounting.count m.active xs

def yes (v : Variable) : Atom Variable := .literal v true
def no (v : Variable) : Atom Variable := .literal v false

def before (states : Nat→Finset Label) (i j : Nat) : Atom Variable :=
  if states i⊂states j then .constant true else
  if states j⊂states i then .constant false else
  if i < j then yes (.order i j) else no (.order j i)

def color (b : Bool) (i j k : Nat) : Atom Variable :=
  .literal (.color (ES7UnorderedColor.low i j k) (ES7UnorderedColor.middle i j k) (ES7UnorderedColor.high i j k)) b

def path (N : Nat) (states : Nat→Finset Label) (b : Bool) (k s i j : Nat) : Atom Variable :=
  if PathAllowed N states b k s i j then yes (.path b k s i j) else .constant false

def counter (xs : List Nat) (k : Nat) : Atom Variable :=
  if k=0 then .constant true else if xs=[] then .constant false else yes (.counter xs k)

theorem yes_spec (m : Model c N states) (v : Variable) : (yes v).Holds (meaning m) ↔ meaning m v := Iff.rfl
theorem no_spec (m : Model c N states) (v : Variable) : (no v).Holds (meaning m) ↔ ¬meaning m v := Iff.rfl

theorem before_spec (m : Model c N states) (ih : i < N) (jh : j < N) (ne : i≠j) :
    (before states i j).Holds (meaning m) ↔ m.key i < m.key j := by
  have keyne : m.key i≠m.key j := fun eq => ne (m.key_injective ih jh eq)
  unfold before
  split
  next sub => simpa [Atom.Holds] using (m.inclusion_order i j ih jh sub)
  next notSub =>
    split
    next sub =>
      have reverse := m.inclusion_order j i jh ih sub
      simp only [Atom.Holds,Bool.false_eq_true,false_iff]
      omega
    next notReverse =>
      split
      next ij => rfl
      next ji => simp only [no_spec,meaning]; omega

theorem color_spec (m : Model c N states) (b i j k)
    (ne : i≠j ∧ j≠k ∧ i≠k) : (color b i j k).Holds (meaning m) ↔ Cup m i j k=b := by
  have eq := ES7UnorderedColor.sorted_names c.cup m.owner i j k ne
  cases b <;> simp only [color,Atom.Holds,Bool.false_eq_true,if_false,if_true,meaning,Cup,eq] <;> simp

theorem counter_spec (m : Model c N states) (xs : List Nat) (k : Nat) :
    (counter xs k).Holds (meaning m) ↔ k ≤ ES7NamedCounting.count m.active xs := by
  unfold counter
  split
  next h => subst k; simp [Atom.Holds]
  next h =>
    split
    next hx => subst xs; simp [ES7NamedCounting.count,Atom.Holds,h]
    next hx => rfl

theorem path_holds (m : Model c N states) (lo : 3 ≤ k) (h : NamedPath m b k s i j) :
    (path N states b k s i j).Holds (meaning m) := by
  simp only [path,if_pos (path_allowed m lo h),yes_spec,meaning]
  exact h

end ES7NamedVariables
