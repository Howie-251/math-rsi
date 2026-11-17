import ES7NamedVariables

set_option linter.unusedSimpArgs false
namespace ES7NamedRules
open ES7NamedGeometry ES7NamedVariables ES7ActualState ES8BalancedGeometry ES7ClauseLogic

def boundedDistinct (N : Nat) (xs : List Nat) := (∀ i∈xs,i < N) ∧ xs.Nodup
instance (N : Nat) (xs : List Nat) : Decidable (boundedDistinct N xs) := by unfold boundedDistinct; infer_instance

inductive Schema where
  | order (i j k : Nat)
  | pairActive (i j x y : Nat) (right : Bool)
  | pairOrder (i j x y : Nat)
  | pairChoice (i j : Nat) (qs : List Label)
  | pairUnique (i j x y u v : Nat)
  | firstPair (i j x y : Nat)
  | forward (b : Bool) (i j k x y u v : Nat)
  | endpoint (b : Bool) (k s i j : Nat)
  | pathActive (b : Bool) (k s i j slot : Nat)
  | pathOrder (b : Bool) (k s i j : Nat) (right : Bool)
  | base (b : Bool) (s i j : Nat)
  | growth (b : Bool) (k s h i j : Nat)
  | polygon (a b s j : Nat)
  deriving DecidableEq, Repr

def guards (states : Nat→Finset Label) : Schema→List (Atom Variable)
  | .order i j k => [before states i j,before states j k]
  | .pairActive i j x y _ => [yes (.pair i j x y)]
  | .pairOrder i j x y => [yes (.pair i j x y)]
  | .pairChoice i j _ => [yes (.active i),yes (.active j),before states i j]
  | .pairUnique i j x y u v => [yes (.pair i j x y),yes (.pair i j u v)]
  | .firstPair i j x y => [yes (.pair i j x y)]
  | .forward b i j k x y u v => [yes (.pair i j x y),yes (.pair j k u v),color b i j k]
  | .endpoint b k s i j => [yes (.path b k s i j)]
  | .pathActive b k s i j _ => [yes (.path b k s i j)]
  | .pathOrder b k s i j _ => [yes (.path b k s i j)]
  | .base b s i j => [yes (.active s),yes (.active i),yes (.active j),before states s i,before states i j,color b s i j]
  | .growth b k s h i j => [yes (.path b k s h i),yes (.active j),before states i j,color b h i j]
  | .polygon a b s j => [yes (.endpoints true a s j),yes (.endpoints false b s j)]

def conclusion (N : Nat) (states : Nat→Finset Label) : Schema→List (Atom Variable)
  | .order i _ k => [before states i k]
  | .pairActive i j _ _ right => [yes (.active (if right then j else i))]
  | .pairOrder i j _ _ => [before states i j]
  | .pairChoice i j qs => qs.map (fun q => yes (.pair i j q.1 q.2))
  | .pairUnique .. => []
  | .firstPair .. => []
  | .forward .. => []
  | .endpoint b k s _ j => [yes (.endpoints b k s j)]
  | .pathActive b k s i j slot => [yes (.active (if slot=0 then s else if slot=1 then i else j))]
  | .pathOrder b k s i j right => [if right then before states i j else before states s i]
  | .base b s i j => [path N states b 3 s i j]
  | .growth b k s _ i j => [path N states b (k+1) s i j]
  | .polygon .. => []

def clause (N : Nat) (states : Nat→Finset Label) (r : Schema) : List (Atom Variable) :=
  (guards states r).map Atom.neg++conclusion N states r

def Valid (N : Nat) (states : Nat→Finset Label) : Schema→Prop
  | .order i j k => boundedDistinct N [i,j,k]
  | .pairActive i j _ _ _ => boundedDistinct N [i,j]
  | .pairOrder i j _ _ => boundedDistinct N [i,j]
  | .pairChoice i j qs => boundedDistinct N [i,j] ∧ qs.toFinset = states j\states i
  | .pairUnique i j x y u v => boundedDistinct N [i,j] ∧ (x,y)≠(u,v)
  | .firstPair i j x y => boundedDistinct N [i,j] ∧
      ((states i=∅ ∧ (x,y)≠(1,1)) ∨ (states i={(1,1)} ∧ (2 < x ∨ 2 < y)))
  | .forward b i j k x y u v => boundedDistinct N [i,j,k] ∧ (if b then u ≤ x else v ≤ y)
  | .endpoint b k s i j => boundedDistinct N [s,i,j]
  | .pathActive b k s i j slot => boundedDistinct N [s,i,j] ∧ slot < 3
  | .pathOrder b k s i j _ => boundedDistinct N [s,i,j]
  | .base b s i j => boundedDistinct N [s,i,j]
  | .growth b k s h i j => boundedDistinct N [s,h,i,j] ∧ 3 ≤ k
  | .polygon a b s j => boundedDistinct N [s,j] ∧ 2 ≤ a ∧ 2 ≤ b ∧ a+b=9

instance (N states r) : Decidable (Valid N states r) := by cases r <;> unfold Valid <;> infer_instance

theorem two_valid (h : boundedDistinct N [i,j]) : i < N ∧ j < N ∧ i≠j := by
  simpa [boundedDistinct,List.nodup_cons,and_assoc] using h
theorem three_valid (h : boundedDistinct N [i,j,k]) :
    i < N ∧ j < N ∧ k < N ∧ i≠j ∧ j≠k ∧ i≠k := by
  simp only [boundedDistinct,List.mem_cons,List.mem_singleton,forall_eq_or_imp,forall_eq,
    List.nodup_cons,List.not_mem_nil,not_false_eq_true,and_true,not_or] at h
  tauto

theorem sound (m : Model c N states) (r : Schema) (valid : Valid N states r) :
    Satisfied (meaning m) (clause N states r) := by
  classical
  apply guarded_sound
  intro all
  cases r with
  | order i j k =>
    obtain ⟨ih,jh,kh,ij,jk,ik⟩ := three_valid valid
    have a := (before_spec m ih jh ij).mp (all _ (by simp [guards]))
    have b := (before_spec m jh kh jk).mp (all _ (by simp [guards]))
    exact ⟨_,by simp [conclusion],(before_spec m ih kh ik).mpr (a.trans b)⟩
  | pairActive i j x y right =>
    have p : Pair m i j (x,y) := all (yes (.pair i j x y)) (by simp [guards])
    cases right
    · exact ⟨yes (.active i),by simp [conclusion],p.1⟩
    · exact ⟨yes (.active j),by simp [conclusion],p.2.1⟩
  | pairOrder i j x y =>
    obtain ⟨ih,jh,ij⟩ := two_valid valid
    have p : Pair m i j (x,y) := all (yes (.pair i j x y)) (by simp [guards])
    exact ⟨_,by simp [conclusion],(before_spec m ih jh ij).mpr p.2.2.1⟩
  | pairChoice i j qs =>
    obtain ⟨ih,jh,ij⟩ := two_valid valid.1
    have ai : i∈m.active := all (yes (.active i)) (by simp [guards])
    have aj : j∈m.active := all (yes (.active j)) (by simp [guards])
    have ord := (before_spec m ih jh ij).mp (all _ (by simp [guards]))
    obtain ⟨q,hq,h⟩ := pair_exists m ai aj ord
    exact ⟨yes (.pair i j q.1 q.2),List.mem_map.mpr ⟨q,by rw [← valid.2] at hq; exact List.mem_toFinset.mp hq,rfl⟩,h⟩
  | pairUnique i j x y u v =>
    have p : Pair m i j (x,y) := all (yes (.pair i j x y)) (by simp [guards])
    have q : Pair m i j (u,v) := all (yes (.pair i j u v)) (by simp [guards])
    exact (valid.2 (p.2.2.2.symm.trans q.2.2.2)).elim
  | firstPair i j x y =>
    have p : Pair m i j (x,y) := all (yes (.pair i j x y)) (by simp [guards])
    rcases valid.2 with ⟨empty,bad⟩|⟨singleton,bad⟩
    · exact (bad (pair_first m p empty)).elim
    · have bound := pair_second m p singleton
      rcases bad with bad|bad <;> omega
  | forward b i j k x y u v =>
    obtain ⟨ih,jh,kh,ij,jk,ik⟩ := three_valid valid.1
    have p : Pair m i j (x,y) := all (yes (.pair i j x y)) (by simp [guards])
    have q : Pair m j k (u,v) := all (yes (.pair j k u v)) (by simp [guards])
    have turn := (color_spec m b i j k ⟨ij,jk,ik⟩).mp (all _ (by simp [guards]))
    have grow := pair_forward m p q
    cases b with
    | false => have h := grow.2 turn; have h' := valid.2; simp only [Bool.false_eq_true,if_false] at h'; omega
    | true => have h := grow.1 turn; have h' := valid.2; simp only [if_true] at h'; omega
  | endpoint b k s i j =>
    have p : NamedPath m b k s i j := all (yes (.path b k s i j)) (by simp [guards])
    exact ⟨yes (.endpoints b k s j),by simp [conclusion],path_endpoint m p⟩
  | pathActive b k s i j slot =>
    have p : NamedPath m b k s i j := all (yes (.path b k s i j)) (by simp [guards])
    have sh := valid.2
    interval_cases slot
    · exact ⟨yes (.active s),by simp [conclusion],p.1⟩
    · exact ⟨yes (.active i),by simp [conclusion],p.2.1⟩
    · exact ⟨yes (.active j),by simp [conclusion],p.2.2.1⟩
  | pathOrder b k s i j right =>
    obtain ⟨sh,ih,jh,si,ij,sj⟩ := three_valid valid
    have p : NamedPath m b k s i j := all (yes (.path b k s i j)) (by simp [guards])
    cases right
    · exact ⟨_,by simp [conclusion],(before_spec m sh ih si).mpr p.2.2.2.1⟩
    · exact ⟨_,by simp [conclusion],(before_spec m ih jh ij).mpr p.2.2.2.2.1⟩
  | base b s i j =>
    obtain ⟨sh,ih,jh,si,ij,sj⟩ := three_valid valid
    have hs : s∈m.active := all (yes (.active s)) (by simp [guards])
    have hi : i∈m.active := all (yes (.active i)) (by simp [guards])
    have hj : j∈m.active := all (yes (.active j)) (by simp [guards])
    have ord := (before_spec m sh ih si).mp (all _ (by simp [guards]))
    have ord' := (before_spec m ih jh ij).mp (all _ (by simp [guards]))
    have turn := (color_spec m b s i j ⟨si,ij,sj⟩).mp (all _ (by simp [guards]))
    exact ⟨_,by simp [conclusion],path_holds m (by omega) (path_base m hs hi hj ord ord' turn)⟩
  | growth b k s h i j =>
    have indexes := valid.1.1
    have nd := valid.1.2
    have hh : h < N := indexes h (by simp)
    have ih : i < N := indexes i (by simp)
    have jh : j < N := indexes j (by simp)
    have ne : h≠i ∧ i≠j ∧ h≠j := by
      simp only [List.nodup_cons,List.mem_cons,List.mem_singleton,List.not_mem_nil,not_false_eq_true,and_true,not_or] at nd
      tauto
    have p : NamedPath m b k s h i := all (yes (.path b k s h i)) (by simp [guards])
    have hj : j∈m.active := all (yes (.active j)) (by simp [guards])
    have ord := (before_spec m ih jh ne.2.1).mp (all _ (by simp [guards]))
    have turn := (color_spec m b h i j ne).mp (all _ (by simp [guards]))
    exact ⟨_,by simp [conclusion],path_holds m (by have := valid.2; omega) (path_step m p hj ord turn)⟩
  | polygon a b s j =>
    have cup : NamedEndpoint m true a s j := all (yes (.endpoints true a s j)) (by simp [guards])
    have cap : NamedEndpoint m false b s j := all (yes (.endpoints false b s j)) (by simp [guards])
    exact (endpoint_exclusion m a b valid.2.1 valid.2.2.1 valid.2.2.2 cup cap).elim

end ES7NamedRules
