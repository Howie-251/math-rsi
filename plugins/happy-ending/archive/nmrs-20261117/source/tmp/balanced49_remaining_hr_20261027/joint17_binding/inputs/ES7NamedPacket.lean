import ES7NamedRules
import ES7PacketSemantics

set_option linter.unusedSimpArgs false
namespace ES7NamedPacket
open ES7NamedGeometry ES7NamedVariables ES7ActualState ES8BalancedGeometry ES7ClauseLogic

def triples (a b c d : Nat) : List (Nat×Nat×Nat) := [(a,b,c),(a,b,d),(a,c,d),(b,c,d)]
def packetColor (a b c d i : Nat) (v : Bool) : Atom Variable :=
  let t := (triples a b c d)[i]?.getD (a,b,c)
  color v t.1 t.2.1 t.2.2

theorem four_bool (x y z w v : Bool)
    (h : (x=true ∨ y=false ∨ z=true) ∧ (x=false ∨ y=true ∨ z=false) ∧
      (x=true ∨ z=false ∨ w=true) ∧ (x=false ∨ z=true ∨ w=false))
    (i j k : Nat) (ij : i < j) (jk : j < k) (kh : k < 4)
    (hi : [x,y,z,w][i]?.getD false=v) (hk : [x,y,z,w][k]?.getD false=v) :
    [x,y,z,w][j]?.getD false=v := by
  have ih : i < 4 := by omega
  have jh : j < 4 := by omega
  interval_cases i <;> interval_cases j <;> interval_cases k <;> try omega
  all_goals cases x <;> cases y <;> cases z <;> cases w <;> cases v <;> simp_all

theorem packet_color_spec (m : Model c N states) (a b d e : Nat)
    (aa : a∈m.active) (bb : b∈m.active) (dd : d∈m.active) (ee : e∈m.active)
    (ab : m.key a < m.key b) (bd : m.key b < m.key d) (de : m.key d < m.key e)
    (i : Nat) (ih : i < 4) (v : Bool) :
    (packetColor a b d e i v).Holds (meaning m) ↔
      [c.cup (m.owner a) (m.owner b) (m.owner d),
       c.cup (m.owner a) (m.owner b) (m.owner e),
       c.cup (m.owner a) (m.owner d) (m.owner e),
       c.cup (m.owner b) (m.owner d) (m.owner e)][i]?.getD false=v := by
  have neab : a≠b := by intro h; subst b; omega
  have nebd : b≠d := by intro h; subst d; omega
  have nede : d≠e := by intro h; subst e; omega
  have nead : a≠d := by intro h; subst d; omega
  have neae : a≠e := by intro h; subst e; omega
  have nebe : b≠e := by intro h; subst e; omega
  interval_cases i
  · simpa [packetColor,triples,cup_ordered m aa bb dd ab bd] using color_spec m v a b d ⟨neab,nebd,nead⟩
  · simpa [packetColor,triples,cup_ordered m aa bb ee ab (bd.trans de)] using color_spec m v a b e ⟨neab,nebe,neae⟩
  · simpa [packetColor,triples,cup_ordered m aa dd ee (ab.trans bd) de] using color_spec m v a d e ⟨nead,nede,neae⟩
  · simpa [packetColor,triples,cup_ordered m bb dd ee bd de] using color_spec m v b d e ⟨nebd,nede,nebe⟩

def guards (states : Nat→Finset Label) (a b c d i k : Nat) (v : Bool) :=
  [yes (.active a),yes (.active b),yes (.active c),yes (.active d),
   before states a b,before states b c,before states c d,
   packetColor a b c d i v,packetColor a b c d k v]
def clause (states : Nat→Finset Label) (a b c d i j k : Nat) (v : Bool) :=
  (guards states a b c d i k v).map Atom.neg++[packetColor a b c d j v]

theorem sound (m : Model c N states) (a b d e i j k : Nat) (v : Bool)
    (valid : ES7NamedRules.boundedDistinct N [a,b,d,e]) (ij : i < j) (jk : j < k) (kh : k < 4) :
    Satisfied (meaning m) (clause states a b d e i j k v) := by
  classical
  apply guarded_sound
  intro all
  have aa : a∈m.active := all (yes (.active a)) (by simp [guards])
  have bb : b∈m.active := all (yes (.active b)) (by simp [guards])
  have dd : d∈m.active := all (yes (.active d)) (by simp [guards])
  have ee : e∈m.active := all (yes (.active e)) (by simp [guards])
  have bounds := valid.1
  have ne : a≠b ∧ b≠d ∧ d≠e := by
    have h := valid.2
    simp only [List.nodup_cons,List.mem_cons,List.mem_singleton,List.not_mem_nil,not_false_eq_true,and_true,not_or] at h
    tauto
  have ab := (before_spec m (bounds a (by simp)) (bounds b (by simp)) ne.1).mp (all _ (by simp [guards]))
  have bd := (before_spec m (bounds b (by simp)) (bounds d (by simp)) ne.2.1).mp (all _ (by simp [guards]))
  have de := (before_spec m (bounds d (by simp)) (bounds e (by simp)) ne.2.2).mp (all _ (by simp [guards]))
  have geom := ES7PacketSemantics.packet_clauses c
    ((m.actual_order a aa b bb).mp ab) ((m.actual_order b bb d dd).mp bd)
    ((m.actual_order d dd e ee).mp de) (m.owner_bound e ee)
  have first := (packet_color_spec m a b d e aa bb dd ee ab bd de i (by omega) v).mp (all _ (by simp [guards]))
  have last := (packet_color_spec m a b d e aa bb dd ee ab bd de k kh v).mp (all _ (by simp [guards]))
  exact ⟨_,by simp,(packet_color_spec m a b d e aa bb dd ee ab bd de j (by omega) v).mpr
    (four_bool _ _ _ _ v geom i j k ij jk kh first last)⟩
end ES7NamedPacket
