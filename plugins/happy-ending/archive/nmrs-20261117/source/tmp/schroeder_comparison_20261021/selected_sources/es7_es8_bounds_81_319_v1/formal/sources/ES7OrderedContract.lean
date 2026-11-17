import ES7OrderedPaths

set_option linter.unusedSimpArgs false

namespace ES7OrderedContract
open ES8ActualRanks ES8ResidualRanks ES8BalancedGeometry ES7BalancedEndpoints ES7OrderedPaths

inductive Var where
  | C (i j k : Nat)
  | P (b : Bool) (k s i j : Nat)
  | E (b : Bool) (k s j : Nat)
  | L (b : Bool) (k i j : Nat)
  | R (b : Bool) (k i j : Nat)
  deriving DecidableEq, Repr

def Meaning (c : Configuration n) : Var → Prop
  | .C i j k => c.cup i j k=true
  | .P b k s i j => ES7PathSemantics.Path c.cup b s i j k
  | .E b k s j => ES7PathSemantics.Endpoint c.cup b s j k
  | .L b k i j => EndingPath c.cup b i j k
  | .R b k i j => StartingPath n c.cup b i j k

abbrev Lit := Var × Bool
def Sat (c : Configuration n) (cl : List Lit) : Prop :=
  ∃ v∈cl, if v.2 then Meaning c v.1 else ¬Meaning c v.1
def pos (v : Var) : Lit := (v,true)
def neg (v : Var) : Lit := (v,false)
def turn (b : Bool) (i j k : Nat) : Lit := (.C i j k,b)
def notTurn (b : Bool) (i j k : Nat) : Lit := (.C i j k,!b)
def pathVar (b : Bool) (k s i j : Nat) : Lit :=
  if k=3 then turn b s i j else pos (.P b k s i j)
def notPath (b : Bool) (k s i j : Nat) : Lit :=
  let p := pathVar b k s i j
  (p.1,!p.2)
def rankVar (right : Bool) (b : Bool) (k i j : Nat) : Var :=
  if right then .R b k i j else .L b k i j

theorem turn_spec (c : Configuration n) (b i j k) :
    (if (turn b i j k).2 then Meaning c (turn b i j k).1 else ¬Meaning c (turn b i j k).1) ↔
    c.cup i j k=b := by
  cases b  <;> simp [turn,Meaning]
theorem not_turn_spec (c : Configuration n) (b i j k) :
    (if (notTurn b i j k).2 then Meaning c (notTurn b i j k).1 else ¬Meaning c (notTurn b i j k).1) ↔
    c.cup i j k≠b := by
  cases b  <;> simp [notTurn,Meaning]

theorem path_three_iff (c : Configuration n) (b s i j)
    (si : s < i) (ij : i < j) : ES7PathSemantics.Path c.cup b s i j 3 ↔ c.cup s i j=b := by
  constructor
  · rintro ⟨xs,head,len,chain⟩
    have size : xs.length=1 := by simp only [List.length_append,List.length_cons,List.length_nil] at len; omega
    obtain ⟨a,rfl⟩ := List.length_eq_one_iff.mp size
    have eq : a=s := by simpa using head
    subst a
    exact (Config.Cup.cons3.mp chain).2.1
  · exact ES7PathSemantics.path_three c.cup b s i j si ij

theorem path_spec (c : Configuration n) (b k s i j) (si : s < i) (ij : i < j) :
    (if (pathVar b k s i j).2 then Meaning c (pathVar b k s i j).1 else ¬Meaning c (pathVar b k s i j).1) ↔
    ES7PathSemantics.Path c.cup b s i j k := by
  by_cases h : k=3
  · subst k; simpa only [pathVar,ite_true] using (turn_spec c b s i j).trans (path_three_iff c b s i j si ij).symm
  · simp [pathVar,h,pos,Meaning]
theorem not_path_spec (c : Configuration n) (b k s i j) (si : s < i) (ij : i < j) :
    (if (notPath b k s i j).2 then Meaning c (notPath b k s i j).1 else ¬Meaning c (notPath b k s i j).1) ↔
    ¬ES7PathSemantics.Path c.cup b s i j k := by
  have h := path_spec c b k s i j si ij
  unfold notPath
  cases hp : (pathVar b k s i j).2  <;> simp_all <;> tauto

/-- Eight four-bit words with more than one sign change, in source order. -/
def packetBits : List (List Bool) :=
  [[false,true,false,false],[false,true,false,true],
   [false,true,true,false],[true,false,false,true],
   [true,false,true,false],[true,false,true,true],
   [false,false,true,false],[true,true,false,true]]

inductive Rule where
  | pathExtend (b : Bool) (k s h i j : Nat)
  | pathMax (b : Bool) (s h i j : Nat)
  | endpoint (b : Bool) (k s i j : Nat)
  | weak (a b s j : Nat)
  | packet (i j k l t : Nat)
  | base (right b : Bool) (i j k : Nat)
  | extend (right b : Bool) (len i j k : Nat)
  | maximum (right b : Bool) (i j k : Nat)
  | triple (b : Bool) (left right i j k : Nat)
  | suffix (right b : Bool) (len i j : Nat)
  | pair (b : Bool) (left right i j : Nat)
  | pathRank (b : Bool) (k s i j : Nat)
  | core (b : Bool) (i j : Nat)
  | terminal (i j k : Nat)
  deriving Repr, DecidableEq

def Rule.clause : Rule → List Lit
  | .pathExtend b k s h i j => [notPath b k s h i,notTurn b h i j,pos (.P b (k+1) s i j)]
  | .pathMax b s h i j => [neg (.P b 5 s h i),notTurn b h i j]
  | .endpoint b k s i j => [neg (.P b k s i j),pos (.E b k s j)]
  | .weak a b s j => [neg (.E true a s j),neg (.E false b s j)]
  | .packet i j k l t =>
      ([(.C i j k),(.C i j l),(.C i k l),(.C j k l)]).zip ((packetBits[t]?.getD []).map Bool.not)
  | .base right b i j k => [notTurn b i j k,pos (if right then .R b 3 i j else .L b 3 j k)]
  | .extend right b len i j k =>
      [neg (if right then .R b len j k else .L b len i j),notTurn b i j k,
       pos (if right then .R b (len+1) i j else .L b (len+1) j k)]
  | .maximum right b i j k =>
      [neg (if right then .R b 5 j k else .L b 5 i j),notTurn b i j k]
  | .triple b left right i j k => [notTurn b i j k,neg (.L b left i j),neg (.R b right j k)]
  | .suffix right b len i j => [neg (rankVar right b len i j),pos (rankVar right b (len-1) i j)]
  | .pair b left right i j => [neg (.L b left i j),neg (.R b right i j)]
  | .pathRank b k s i j => [neg (.P b k s i j),pos (.L b k i j)]
  | .core b i j => [neg (.L b 5 i j)]
  | .terminal i j k => [pos (.C i j k)]

/-- Only necessary premises; this is independently checked rather than trusting
the Python generator's loops or family labels. -/
def Rule.Valid (n m : Nat) : Rule → Prop
  | .pathExtend _ k s h i j => 3≤k ∧ k≤4 ∧ s < h ∧ h < i ∧ i < j ∧ j < n
  | .pathMax _ s h i j => s < h ∧ h < i ∧ i < j ∧ j < n
  | .endpoint _ _ s i j => s < i ∧ i < j ∧ j < n
  | .weak a b s j => 2≤a ∧ 2≤b ∧ a+b=9 ∧ s < j ∧ j < n
  | .packet i j k l t => i < j ∧ j < k ∧ k < l ∧ l < n ∧ t < 8
  | .base _ _ i j k => i < j ∧ j < k ∧ k < n
  | .extend _ _ _ i j k => i < j ∧ j < k ∧ k < n
  | .maximum _ _ i j k => i < j ∧ j < k ∧ k < n
  | .triple _ left right i j k => left+right=7 ∧ i < j ∧ j < k ∧ k < n
  | .suffix _ _ len i j => 3≤len ∧ i < j ∧ j < n
  | .pair _ left right i j => left+right=8 ∧ i < j ∧ j < n
  | .pathRank _ _ s i j => s < i ∧ i < j ∧ j < n
  | .core _ i j => i < j ∧ j < m
  | .terminal i j k => m - 1 ≤ i ∧ i < j ∧ j < k ∧ k < n

instance (n m : Nat) (r : Rule) : Decidable (r.Valid n m) := by
  cases r  <;> unfold Rule.Valid  <;> infer_instance

structure Hypotheses (c : Configuration n) (m : Nat) : Prop where
  noSix : NoSix c.cup (Finset.range n)
  noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)
  core : ∀ b, ¬(colorConfig c.cup b).HasNCup 5 (Finset.range m)
  terminal : ∀ i j k, m - 1 ≤ i → i < j → j < k → k < n → c.cup i j k=true

theorem packet_sound (c : Configuration n) (i j k l t : Nat)
    (valid : (Rule.packet i j k l t).Valid n m) : Sat c (Rule.packet i j k l t).clause := by
  obtain ⟨ij,jk,kl,ln,tn⟩ := valid
  have hp := ES7PacketSemantics.packet_clauses c ij jk kl ln
  interval_cases t  <;>
    simp only [Rule.clause,packetBits,List.getElem?_cons_zero,List.getElem?_cons_succ,
      Option.getD_some,List.map_cons,List.map_nil,Bool.not_false,Bool.not_true,List.zip_cons_cons,List.zip_nil_right]  <;>
    simp only [Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left,Prod.fst,Prod.snd,
      Meaning,Bool.false_eq_true,if_false,if_true]  <;>
    cases h1 : c.cup i j k  <;> cases h2 : c.cup i j l  <;>
    cases h3 : c.cup i k l  <;> cases h4 : c.cup j k l  <;> simp_all

theorem sound (c : Configuration n) (m : Nat) (hyp : Hypotheses c m)
    (r : Rule) (valid : r.Valid n m) : Sat c r.clause := by
  classical
  cases r with
  | pathExtend b k s h i j =>
    obtain ⟨lo,hi,sh,hi',ij,jn⟩ := valid
    have extension := ES7PathSemantics.path_extension c.cup b s h i j k
    simp only [Rule.clause,Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left]
    rw [not_path_spec c b k s h i sh hi',not_turn_spec]
    simp only [pos,Prod.fst,Prod.snd,if_true,Meaning]
    have step := fun p turn => extension p ij turn
    tauto
  | pathMax b s h i j =>
    obtain ⟨sh,hi,ij,jn⟩ := valid
    have maximum : ES7PathSemantics.Path c.cup b s h i 5 → c.cup h i j=b → False := by
      intro p turn
      exact ending_forbidden (hyp.noSix b) jn (selected_path_rank (ES7PathSemantics.path_extension c.cup b s h i j 5 p ij turn))
    simp only [Rule.clause,Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left]
    rw [not_turn_spec]
    simp only [neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,Meaning]
    tauto
  | endpoint b k s i j =>
    have h := ES7PathSemantics.path_endpoint c.cup b s i j k
    simpa [Rule.clause,Sat,pos,neg,Meaning] using (imp_iff_not_or.mp h)
  | weak a b s j =>
    obtain ⟨ha,hb,total,sj,jn⟩ := valid
    have h := fun cup cap => hyp.noGon (weak_heptagon c (s:=s) jn ha hb total cup cap)
    simp only [Rule.clause,Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left,
      neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,Meaning]
    tauto
  | packet i j k l t => exact packet_sound c i j k l t valid
  | base right b i j k =>
    obtain ⟨ij,jk,kn⟩ := valid
    have l : c.cup i j k=b → EndingPath c.cup b j k 3 := fun h => .step (.pair ij) jk h
    have rr : c.cup i j k=b → StartingPath n c.cup b i j 3 := fun h => .step (.pair jk kn) ij h
    cases right  <;>
      simp only [Rule.clause,Bool.false_eq_true,if_false,if_true,Sat,List.mem_cons,List.not_mem_nil,
        or_false,exists_eq_or_imp,exists_eq_left]  <;> rw [not_turn_spec]  <;>
      simp only [pos,Prod.fst,Prod.snd,if_true,Meaning]  <;> tauto
  | extend right b len i j k =>
    obtain ⟨ij,jk,kn⟩ := valid
    have l : EndingPath c.cup b i j len → c.cup i j k=b → EndingPath c.cup b j k (len+1) := fun p h => .step p jk h
    have rr : StartingPath n c.cup b j k len → c.cup i j k=b → StartingPath n c.cup b i j (len+1) := fun p h => .step p ij h
    cases right  <;>
      simp only [Rule.clause,Bool.false_eq_true,if_false,if_true,Sat,List.mem_cons,List.not_mem_nil,
        or_false,exists_eq_or_imp,exists_eq_left]  <;> rw [not_turn_spec]  <;>
      simp only [pos,neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,if_true,Meaning]  <;> tauto
  | maximum right b i j k =>
    obtain ⟨ij,jk,kn⟩ := valid
    have l : EndingPath c.cup b i j 5 → c.cup i j k=b → False := fun p h => ending_forbidden (hyp.noSix b) kn (.step p jk h)
    have rr : StartingPath n c.cup b j k 5 → c.cup i j k=b → False := fun p h => starting_forbidden (hyp.noSix b) (.step p ij h)
    cases right  <;>
      simp only [Rule.clause,Bool.false_eq_true,if_false,if_true,Sat,List.mem_cons,List.not_mem_nil,
        or_false,exists_eq_or_imp,exists_eq_left]  <;> rw [not_turn_spec]  <;>
      simp only [neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,Meaning]  <;> tauto
  | triple b left right i j k =>
    obtain ⟨total,ij,jk,kn⟩ := valid
    have h := triple_budget (cup:=c.cup) (color:=b) (u:=i) (v:=j) (w:=k) hyp.noSix total
    simp only [Rule.clause,Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left]
    rw [not_turn_spec]
    simp only [neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,Meaning]
    tauto
  | suffix right b len i j =>
    obtain ⟨lo,ij,jn⟩ := valid
    have l : EndingPath c.cup b i j len → EndingPath c.cup b i j (len-1) := fun p => ending_truncate p _ (by omega) (by omega)
    have rr : StartingPath n c.cup b i j len → StartingPath n c.cup b i j (len-1) := fun p => truncate p _ (by omega) (by omega)
    cases right  <;> simp [Rule.clause,Sat,pos,neg,rankVar,Meaning]  <;> tauto
  | pair b left right i j =>
    obtain ⟨total,ij,jn⟩ := valid
    have h := pair_budget (cup:=c.cup) (color:=b) (u:=i) (v:=j) hyp.noSix total
    simp only [Rule.clause,Sat,List.mem_cons,List.not_mem_nil,or_false,exists_eq_or_imp,exists_eq_left,
      neg,Prod.fst,Prod.snd,Bool.false_eq_true,if_false,Meaning]
    tauto
  | pathRank b k s i j =>
    have h := selected_path_rank (cup:=c.cup) (color:=b) (s:=s) (u:=i) (v:=j) (k:=k)
    simpa [Rule.clause,Sat,pos,neg,Meaning] using (imp_iff_not_or.mp h)
  | core b i j =>
    obtain ⟨ij,jm⟩ := valid
    have h : ¬EndingPath c.cup b i j 5 := fun p => ending_forbidden (hyp.core b) jm p
    simpa [Rule.clause,Sat,neg,Meaning] using h
  | terminal i j k =>
    obtain ⟨mi,ij,jk,kn⟩ := valid
    simpa [Rule.clause,Sat,pos,Meaning] using hyp.terminal i j k mi ij jk kn

end ES7OrderedContract
