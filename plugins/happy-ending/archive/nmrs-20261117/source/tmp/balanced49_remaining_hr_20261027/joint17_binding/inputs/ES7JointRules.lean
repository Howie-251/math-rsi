import ES7NamedPacket

namespace ES7JointRules
open ES7NamedGeometry ES7NamedVariables ES7ActualState ES8BalancedGeometry ES7ClauseLogic

def lowNames : List Nat := List.range 20
def highNames : List Nat := (List.range 20).map (20+·)

structure Hypotheses (m : Model c 40 states) : Prop where
  low : ES7NamedCounting.count m.active lowNames=17
  high : ES7NamedCounting.count m.active highNames=17
  first : 0∈m.active
  second : 1∈m.active

inductive Schema where
  | named (r : ES7NamedRules.Schema)
  | packet (a b c d i j k : Nat) (v : Bool)
  | counter (xs : List Nat) (i k part : Nat)
  | population (high : Bool) (upper : Bool)
  | mandatory (i : Nat)
  deriving DecidableEq, Repr

def clause (states : Nat→Finset Label) : Schema→List (Atom Variable)
  | .named r => ES7NamedRules.clause 40 states r
  | .packet a b c d i j k v => ES7NamedPacket.clause states a b c d i j k v
  | .counter xs i k part =>
    let q := counter (xs++[i]) k
    let prev := counter xs k
    let below := counter xs (k-1)
    match part with
    | 0 => [q.neg,prev,below]
    | 1 => [q.neg,prev,yes (.active i)]
    | 2 => [prev.neg,q]
    | _ => [below.neg,no (.active i),q]
  | .population high upper =>
    let xs := if high then highNames else lowNames
    [if upper then (counter xs 18).neg else counter xs 17]
  | .mandatory i => [yes (.active i)]

def Valid (states : Nat→Finset Label) : Schema→Prop
  | .named r => ES7NamedRules.Valid 40 states r
  | .packet a b c d i j k _ => ES7NamedRules.boundedDistinct 40 [a,b,c,d] ∧ i < j ∧ j < k ∧ k < 4
  | .counter _ _ k part => 1 ≤ k ∧ part < 4
  | .population .. => True
  | .mandatory i => i=0 ∨ i=1
instance (states r) : Decidable (Valid states r) := by cases r <;> unfold Valid <;> infer_instance

theorem counter_sound (m : Model c N states) (xs : List Nat) (i k part : Nat)
    (positive : 1 ≤ k) (ph : part < 4) :
    Satisfied (meaning m) (clause states (.counter xs i k part)) := by
  have h := ES7NamedCounting.threshold_recurrence m.active xs i k positive
  have a := counter_spec m (xs++[i]) k
  have b := counter_spec m xs k
  have d := counter_spec m xs (k-1)
  interval_cases part
  all_goals simp only [clause,Satisfied,List.mem_cons,List.mem_singleton,exists_eq_or_imp,
    neg_holds,yes_spec,no_spec,meaning,a,b,d,List.not_mem_nil,false_and,exists_false,or_false,exists_eq_left]
  · exact h.1
  · exact h.2.1
  · exact h.2.2.1
  · exact h.2.2.2

theorem sound (m : Model c 40 states) (h : Hypotheses m) (r : Schema) (valid : Valid states r) :
    Satisfied (meaning m) (clause states r) := by
  classical
  cases r with
  | named r => exact ES7NamedRules.sound m r valid
  | packet a b d e i j k v => exact ES7NamedPacket.sound m a b d e i j k v valid.1 valid.2.1 valid.2.2.1 valid.2.2.2
  | counter xs i k part => exact counter_sound m xs i k part valid.1 valid.2
  | mandatory i =>
    rcases valid with rfl|rfl
    · exact ⟨yes (.active 0),by simp [clause],h.first⟩
    · exact ⟨yes (.active 1),by simp [clause],h.second⟩
  | population high upper =>
    cases high <;> cases upper
    all_goals simp only [clause,Bool.false_eq_true,if_false,if_true,Satisfied,
      List.mem_singleton,exists_eq_left,neg_holds,counter_spec]
    all_goals simp [h.low,h.high]
end ES7JointRules
