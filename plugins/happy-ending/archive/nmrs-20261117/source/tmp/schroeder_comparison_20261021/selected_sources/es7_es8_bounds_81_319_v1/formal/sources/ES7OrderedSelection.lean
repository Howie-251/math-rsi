import ES7Terminal20Data
import ES7BalancedPopulations

namespace ES7OrderedSelection
open ES8ActualRanks ES8BalancedGeometry ES7BalancedEndpoints ES7Geometry

noncomputable def reindex (c : Configuration n) (f : Fin k ↪o Fin n) : Configuration k where
  point := c.point ∘ f
  xOrder := c.xOrder.comp f.strictMono
  generalPosition := fun a b d ab bd => c.generalPosition _ _ _ (f.strictMono ab) (f.strictMono bd)

def enumerate (f : Fin k ↪o Fin n) (i : Nat) : Nat :=
  if h : i < k then (f ⟨i,h⟩).val else 0

theorem enumerate_bound (f : Fin k ↪o Fin n) (hi : i < k) : enumerate f i < n := by
  simp only [enumerate,dif_pos hi]
  exact (f ⟨i,hi⟩).isLt

theorem enumerate_order (f : Fin k ↪o Fin n) (ij : i < j) (hj : j < k) :
    enumerate f i < enumerate f j := by
  simp only [enumerate,dif_pos hj,dif_pos (show i < k by omega)]
  exact f.strictMono ij

theorem cup_eq (c : Configuration n) (f : Fin k ↪o Fin n) (a b d : Nat)
    (ha : a < k) (hb : b < k) (hd : d < k) :
    (reindex c f).cup a b d=c.cup (enumerate f a) (enumerate f b) (enumerate f d) := by
  simp [Configuration.cup,ha,hb,hd,enumerate,reindex]

theorem cup_map (c : Configuration n) (f : Fin k ↪o Fin n) (b : Bool) (xs : List Nat)
    (inside : xs.In (Finset.range k)) (chain : (colorConfig (reindex c f).cup b).Cup xs) :
    (colorConfig c.cup b).Cup (xs.map (enumerate f)) := by
  constructor
  · apply List.Pairwise.isChain
    apply List.pairwise_map.mpr
    exact chain.1.pairwise.imp_of_mem (fun {a d} _ hd ad => enumerate_order f ad (Finset.mem_range.mp (inside d hd)))
  · apply ES8Subset.chain3_map _ _ (enumerate f) xs _ chain.2
    intro a ha d hd e he h
    change c.cup (enumerate f a) (enumerate f d) (enumerate f e)=b
    rw [←cup_eq c f a d e (Finset.mem_range.mp (inside a ha))
      (Finset.mem_range.mp (inside d hd)) (Finset.mem_range.mp (inside e he))]
    exact h

theorem noSix_reindex (c : Configuration n) (f : Fin k ↪o Fin n)
    (noSix : NoSix c.cup (Finset.range n)) : NoSix (reindex c f).cup (Finset.range k) := by
  intro b h
  obtain ⟨xs,⟨chain,len⟩,inside⟩ := h
  apply noSix b
  refine ⟨xs.map (enumerate f),⟨cup_map c f b xs inside chain,by simpa using len⟩,?_⟩
  intro a ha
  obtain ⟨i,hi,rfl⟩ := List.mem_map.mp ha
  exact Finset.mem_range.mpr (enumerate_bound f (Finset.mem_range.mp (inside i hi)))

theorem noGon_reindex (c : Configuration n) (f : Fin k ↪o Fin n)
    (noGon : ¬HasConvexHeptagon (Set.range c.point)) :
    ¬HasConvexHeptagon (Set.range (reindex c f).point) := by
  intro h
  apply noGon
  apply ES7Subset.heptagon_mono _ _ ?_ h
  rintro p ⟨i,rfl⟩
  exact ⟨f i,rfl⟩

noncomputable def selected (S : Finset (Fin n)) (card : S.card=20)
    (a b d e : Fin n) (i : Fin 24) : Fin n :=
  if h : i.val < 20 then S.orderEmbOfFin card ⟨i.val,h⟩
  else if i.val=20 then a else if i.val=21 then b else if i.val=22 then d else e

theorem selected_strict (S : Finset (Fin n)) (card : S.card=20)
    (a b d e : Fin n) (ua : S.orderEmbOfFin card 19 < a)
    (ab : a < b) (bd : b < d) (de : d < e) : StrictMono (selected S card a b d e) := by
  apply Fin.strictMono_iff_lt_succ.mpr
  intro i
  by_cases hi : i.val < 19
  · simp only [selected,Fin.val_castSucc,Fin.val_succ,dif_pos (show i.val < 20 by omega),
      dif_pos (show i.val+1 < 20 by omega)]
    exact (S.orderEmbOfFin card).strictMono (by change i.val < i.val+1; omega)
  · have lo : 19 ≤ i.val := by omega
    have high := i.isLt
    interval_cases h : i.val <;> simp_all [selected]

noncomputable def selection (S : Finset (Fin n)) (card : S.card=20)
    (a b d e : Fin n) (ua : S.orderEmbOfFin card 19 < a)
    (ab : a < b) (bd : b < d) (de : d < e) : Fin 24 ↪o Fin n :=
  OrderEmbedding.ofStrictMono _ (selected_strict S card a b d e ua ab bd de)

/-- The selected twenty core points and the four extra vertices come from one
actual cup at the last core point; all induced ranks are recomputed. -/
theorem terminal_twenty_impossible (c : Configuration n) (S : Finset (Fin n))
    (card : S.card=20) (noSix : NoSix c.cup (Finset.range n))
    (noGon : ¬HasConvexHeptagon (Set.range c.point))
    (core : ∀ b, ¬(colorConfig c.cup b).HasNCup 5 (ES8Subset.natSet S))
    (starts : StartsFive c.cup true (Finset.range n) (S.orderEmbOfFin card 19).val) : False := by
  classical
  let u := S.orderEmbOfFin card 19
  obtain ⟨a,b,d,e,chain,inside⟩ := starts
  have an : a < n := Finset.mem_range.mp (inside a (by simp))
  have bn : b < n := Finset.mem_range.mp (inside b (by simp))
  have dn : d < n := Finset.mem_range.mp (inside d (by simp))
  have en : e < n := Finset.mem_range.mp (inside e (by simp))
  have order := chain
  simp only [Config.Cup.cons3,Config.Cup.pair,colorConfig] at order
  let f := selection S card ⟨a,an⟩ ⟨b,bn⟩ ⟨d,dn⟩ ⟨e,en⟩ order.1 order.2.2.1 order.2.2.2.2.1 order.2.2.2.2.2.2
  apply ES7Terminal20Data.impossible (reindex c f)
  refine ⟨noSix_reindex c f noSix,noGon_reindex c f noGon,?_,?_⟩
  · intro color h
    obtain ⟨xs,⟨cup,len⟩,xin⟩ := h
    have all : xs.In (Finset.range 24) := fun i hi => Finset.mem_range.mpr (by have := Finset.mem_range.mp (xin i hi); omega)
    apply core color
    refine ⟨xs.map (enumerate f),⟨cup_map c f color xs all cup,by simpa using len⟩,?_⟩
    intro i hi
    obtain ⟨j,hj,rfl⟩ := List.mem_map.mp hi
    have jm := Finset.mem_range.mp (xin j hj)
    have j24 : j < 24 := by omega
    simp only [enumerate,dif_pos j24,f,selection,OrderEmbedding.coe_ofStrictMono,selected,dif_pos jm]
    exact Finset.mem_image.mpr ⟨_,S.orderEmbOfFin_mem card ⟨j,jm⟩,rfl⟩
  · intro i j k mi ij jk kn
    have mem : ∀ z, 19≤z → z < 24 → enumerate f z∈[u.val,a,b,d,e] := by
      intro z lo hi
      interval_cases z <;> simp [enumerate,f,selection,selected,u]
    have sign := ES8BaekGeometry.cup_list_all c _ inside chain
      (enumerate f i) (mem i mi (by omega))
      (enumerate f j) (mem j (by omega) (by omega))
      (enumerate f k) (mem k (by omega) kn)
      (enumerate_order f ij (by omega)) (enumerate_order f jk kn)
    rw [cup_eq c f i j k (by omega) (by omega) kn]
    exact (ES8BaekGeometry.cup_sign c _ _ _ (enumerate_bound f (by omega))
      (enumerate_bound f (by omega)) (enumerate_bound f kn)).mpr sign

/-- Any twenty actual five-cup starters contain an internal five-cup. -/
theorem twenty_starters_have_internal_cup (c : Configuration n) (S : Finset (Fin n))
    (card : S.card=20) (subset : S⊆ES7BalancedEndpoints.starters c true)
    (noSix : NoSix c.cup (Finset.range n))
    (noGon : ¬HasConvexHeptagon (Set.range c.point)) :
    (colorConfig c.cup true).HasNCup 5 (ES8Subset.natSet S) := by
  classical
  by_contra noCup
  apply terminal_twenty_impossible c S card noSix noGon
  · intro b
    cases b with
    | true => exact noCup
    | false =>
      have noCap := ES7BalancedPopulations.starter_no_opposite_five c true noSix
      intro h
      apply noCap
      obtain ⟨xs,hxs,inside⟩ := h
      refine ⟨xs,hxs,?_⟩
      intro a ha
      obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp (inside a ha)
      exact Finset.mem_image.mpr ⟨i,subset hi,rfl⟩
  · exact (mem_starters c true _).mp (subset (S.orderEmbOfFin_mem card 19))

end ES7OrderedSelection
