import ES7Through14Data
import ES7TerminalPopulation

namespace ES7ThroughSelection
open ES8BalancedGeometry ES8ActualRanks ES7BalancedEndpoints ES7Geometry ES7OrderedSelection

noncomputable def selected (S : Finset (Fin n)) (card : S.card=14)
    (a b d e p q r s : Fin n) (i : Fin 22) : Fin n :=
  if i.val < 4 then
    if i.val=0 then a else if i.val=1 then b else if i.val=2 then d else e
  else if h : i.val < 18 then S.orderEmbOfFin card ⟨i.val-4,by omega⟩
  else if i.val=18 then p else if i.val=19 then q else if i.val=20 then r else s

theorem selected_strict (S : Finset (Fin n)) (card : S.card=14)
    (a b d e p q r s : Fin n)
    (ab : a < b) (bd : b < d) (de : d < e) (eu : e < S.orderEmbOfFin card 0)
    (vp : S.orderEmbOfFin card 13 < p) (pq : p < q) (qr : q < r) (rs : r < s) :
    StrictMono (selected S card a b d e p q r s) := by
  apply Fin.strictMono_iff_lt_succ.mpr
  intro i
  by_cases lo : i.val < 4
  · interval_cases h : i.val <;> simp_all [selected]
  · by_cases mid : i.val < 17
    · simp only [selected,Fin.val_castSucc,Fin.val_succ,if_neg lo,
        if_neg (show ¬i.val+1 < 4 by omega),dif_pos (show i.val < 18 by omega),
        dif_pos (show i.val+1 < 18 by omega)]
      exact (S.orderEmbOfFin card).strictMono (by change i.val-4 < i.val+1-4; omega)
    · have high := i.isLt
      interval_cases h : i.val <;> simp_all [selected]

noncomputable def selection (S : Finset (Fin n)) (card : S.card=14)
    (a b d e p q r s : Fin n)
    (ab : a < b) (bd : b < d) (de : d < e) (eu : e < S.orderEmbOfFin card 0)
    (vp : S.orderEmbOfFin card 13 < p) (pq : p < q) (qr : q < r) (rs : r < s) : Fin 22 ↪o Fin n :=
  OrderEmbedding.ofStrictMono _ (selected_strict S card a b d e p q r s ab bd de eu vp pq qr rs)

theorem fourteen_impossible (c : Configuration n) (S : Finset (Fin n))
    (card : S.card=14) (sub : S⊆starters c true ∩ enders c true)
    (noSix : NoSix c.cup (Finset.range n))
    (noGon : ¬HasConvexHeptagon (Set.range c.point)) : False := by
  classical
  let u := S.orderEmbOfFin card 0
  let v := S.orderEmbOfFin card 13
  have hu := sub (S.orderEmbOfFin_mem card 0)
  have hv := sub (S.orderEmbOfFin_mem card 13)
  obtain ⟨a,b,d,e,incoming,incomingIn⟩ := (mem_enders c true u).mp (Finset.mem_inter.mp hu).2
  obtain ⟨p,q,r,s,outgoing,outgoingIn⟩ := (mem_starters c true v).mp (Finset.mem_inter.mp hv).1
  have an : a < n := Finset.mem_range.mp (incomingIn a (by simp))
  have bn : b < n := Finset.mem_range.mp (incomingIn b (by simp))
  have dn : d < n := Finset.mem_range.mp (incomingIn d (by simp))
  have en : e < n := Finset.mem_range.mp (incomingIn e (by simp))
  have pn : p < n := Finset.mem_range.mp (outgoingIn p (by simp))
  have qn : q < n := Finset.mem_range.mp (outgoingIn q (by simp))
  have rn : r < n := Finset.mem_range.mp (outgoingIn r (by simp))
  have sn : s < n := Finset.mem_range.mp (outgoingIn s (by simp))
  have inOrder := incoming
  have outOrder := outgoing
  simp only [Config.Cup.cons3,Config.Cup.pair,colorConfig] at inOrder outOrder
  let g := selection S card ⟨a,an⟩ ⟨b,bn⟩ ⟨d,dn⟩ ⟨e,en⟩ ⟨p,pn⟩ ⟨q,qn⟩ ⟨r,rn⟩ ⟨s,sn⟩
    inOrder.1 inOrder.2.2.1 inOrder.2.2.2.2.1 inOrder.2.2.2.2.2.2
    outOrder.1 outOrder.2.2.1 outOrder.2.2.2.2.1 outOrder.2.2.2.2.2.2
  let f := enumerate g
  have bounded : ∀ i, i < 22 → f i < n := fun i hi => enumerate_bound g hi
  have ordered : ∀ i j, i < j → j < 22 → f i < f j := fun i j ij jh => enumerate_order g ij jh
  apply ES7Through14Data.impossible c f
  refine ⟨ordered,bounded,noSix,noGon,?_,?_⟩
  · intro z hz
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hz
    obtain ⟨lo,hi⟩ := Finset.mem_Ico.mp hi
    have mem : (g ⟨i,by omega⟩)∈S := by
      simp only [g,selection,OrderEmbedding.coe_ofStrictMono,selected,if_neg (by omega : ¬i < 4),dif_pos hi]
      exact S.orderEmbOfFin_mem card _
    have both := Finset.mem_inter.mp (sub mem)
    have eq : f i=(g ⟨i,by omega⟩).val := by simp [f,enumerate,show i < 22 by omega]
    rw [eq]
    exact ⟨(mem_starters c true _).mp both.1,(mem_enders c true _).mp both.2⟩
  · intro i j k ij jk kh side
    have transfer (xs : List Nat) (inside : xs.In (Finset.range n))
        (chain : (colorConfig c.cup true).Cup xs)
        (mi : f i∈xs) (mj : f j∈xs) (mk : f k∈xs) : c.cup (f i) (f j) (f k)=true := by
      have sign := ES8BaekGeometry.cup_list_all c xs inside chain _ mi _ mj _ mk
        (ordered i j ij (by omega)) (ordered j k jk kh)
      exact (ES8BaekGeometry.cup_sign c _ _ _ (bounded i (by omega)) (bounded j (by omega)) (bounded k kh)).mpr sign
    rcases side with left|right
    · have mem : ∀ z, z ≤ 4 → f z∈[a,b,d,e,u.val] := by
        intro z zh
        interval_cases z <;> simp [f,enumerate,g,selection,selected,u]
      exact transfer _ incomingIn incoming (mem i (by omega)) (mem j (by omega)) (mem k left)
    · have mem : ∀ z, 17 ≤ z → z < 22 → f z∈[v.val,p,q,r,s] := by
        intro z zl zh
        interval_cases z <;> simp [f,enumerate,g,selection,selected,v]
      exact transfer _ outgoingIn outgoing (mem i right (by omega)) (mem j (by omega) (by omega)) (mem k (by omega) kh)

/-- At most thirteen points can both start and end actual five-cups in one
heptagon-free configuration without six-cups or six-caps. -/
theorem through_population_le_thirteen (c : Configuration n)
    (noSix : NoSix c.cup (Finset.range n))
    (noGon : ¬HasConvexHeptagon (Set.range c.point)) :
    (starters c true ∩ enders c true).card ≤ 13 := by
  classical
  by_contra high
  obtain ⟨S,sub,card⟩ := Finset.exists_subset_card_eq (show 14 ≤ (starters c true ∩ enders c true).card by omega)
  exact fourteen_impossible c S card sub noSix noGon

end ES7ThroughSelection
