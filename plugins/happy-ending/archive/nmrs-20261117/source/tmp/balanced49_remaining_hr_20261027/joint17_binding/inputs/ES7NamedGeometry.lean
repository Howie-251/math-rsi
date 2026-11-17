import ES7UnorderedColor

namespace ES7NamedGeometry
open ES8ActualRanks ES8BalancedGeometry ES7ActualState ES7BalancedEndpoints ES7PathSemantics

theorem ending_length_first {cup b u v k} (p : EndingPath cup b u v k) : k ≤ u+2 := by
  cases p with
  | pair uv => omega
  | step prior uv turn => have bound := ES8ActualRanks.length_bounds prior; omega

theorem rank_first_bound (cup : Nat→Nat→Nat→Bool) (b : Bool) (uv : u < v) : rank cup b u v ≤ u+2 :=
  ending_length_first (rank_attained cup b u v uv)

theorem initial_label (cup : Nat→Nat→Nat→Bool) (v : Nat) (positive : 0 < v) : label cup 0 v=(1,1) := by
  have a := rank_first_bound cup true positive
  have b := rank_first_bound cup false positive
  have al := (length_bounds (rank_attained cup true 0 v positive)).1
  have bl := (length_bounds (rank_attained cup false 0 v positive)).1
  apply Prod.ext <;> simp only [label] <;> omega

theorem incoming_zero (cup : Nat→Nat→Nat→Bool) (q : Label) : ¬Incoming cup 0 q := by
  rintro ⟨_,_,u,order,_⟩; omega

theorem incoming_one (cup : Nat→Nat→Nat→Bool) (q : Label) : Incoming cup 1 q ↔ q=(1,1) := by
  constructor
  · rintro ⟨pos1,pos2,u,uv,below⟩
    have eq : u=0 := by omega
    subst u
    rw [initial_label cup 1 (by omega)] at below
    apply Prod.ext <;> simp only [Below] at below <;> dsimp <;> omega
  · rintro rfl
    exact ⟨by omega,by omega,0,by omega,by rw [initial_label cup 1 (by omega)]; exact ⟨le_rfl,le_rfl⟩⟩

structure Model (c : Configuration n) (N : Nat) (states : Nat→Finset Label) where
  active : Finset Nat
  active_bound : ∀ i∈active, i < N
  owner : Nat→Nat
  owner_bound : ∀ i∈active, owner i < n
  key : Nat→Nat
  key_injective : Set.InjOn key (Set.Iio N)
  actual_order : ∀ i∈active, ∀ j∈active, key i < key j ↔ owner i < owner j
  actual_state : ∀ i∈active, ∀ q, q∈states i ↔ Incoming c.cup (owner i) q
  inclusion_order : ∀ i j, i < N → j < N → states i ⊂ states j → key i < key j
  noSix : NoSix c.cup (Finset.range n)
  noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)

variable {n N : Nat} {c : Configuration n} {states : Nat→Finset Label}

def Pair (m : Model c N states) (i j : Nat) (q : Label) : Prop :=
  i∈m.active ∧ j∈m.active ∧ m.key i < m.key j ∧ label c.cup (m.owner i) (m.owner j)=q

def NamedPath (m : Model c N states) (b : Bool) (k s i j : Nat) : Prop :=
  s∈m.active ∧ i∈m.active ∧ j∈m.active ∧ m.key s < m.key i ∧ m.key i < m.key j ∧
    Path c.cup b (m.owner s) (m.owner i) (m.owner j) k

def NamedEndpoint (m : Model c N states) (b : Bool) (k s j : Nat) : Prop :=
  s∈m.active ∧ j∈m.active ∧ Endpoint c.cup b (m.owner s) (m.owner j) k

noncomputable def Cup (m : Model c N states) (i j k : Nat) : Bool := ES7UnorderedColor.color c.cup (m.owner i) (m.owner j) (m.owner k)

theorem cup_ordered (m : Model c N states) (hi : i∈m.active) (hj : j∈m.active) (hk : k∈m.active)
    (ij : m.key i < m.key j) (jk : m.key j < m.key k) : Cup m i j k=c.cup (m.owner i) (m.owner j) (m.owner k) :=
  ES7UnorderedColor.ordered _ ((m.actual_order i hi j hj).mp ij) ((m.actual_order j hj k hk).mp jk)

theorem pair_exists (m : Model c N states) (hi : i∈m.active) (hj : j∈m.active)
    (ij : m.key i < m.key j) : ∃ q∈states j\states i, Pair m i j q := by
  have order := (m.actual_order i hi j hj).mp ij
  have diff := label_difference c.cup (m.owner i) (m.owner j) order
  refine ⟨label c.cup (m.owner i) (m.owner j),Finset.mem_sdiff.mpr ⟨?_,?_⟩,hi,hj,ij,rfl⟩
  · exact (m.actual_state j hj _).mpr diff.1
  · intro mem; exact diff.2 ((m.actual_state i hi _).mp mem)

theorem pair_forward (m : Model c N states) (p : Pair m i j a) (q : Pair m j k b) :
    (Cup m i j k=true → a.1 < b.1) ∧ (Cup m i j k=false → a.2 < b.2) := by
  obtain ⟨hi,hj,ij,eq⟩ := p
  obtain ⟨_,hk,jk,eq'⟩ := q
  rw [cup_ordered m hi hj hk ij jk]
  have growth := label_growth c.cup (m.owner i) (m.owner j) (m.owner k)
    ((m.actual_order i hi j hj).mp ij) ((m.actual_order j hj k hk).mp jk)
  simpa only [eq,eq'] using growth

theorem owner_zero (m : Model c N states) (hi : i∈m.active) (empty : states i=∅) : m.owner i=0 := by
  by_contra h
  have positive : 0 < m.owner i := by omega
  have mem := (m.actual_state i hi _).mpr (label_difference c.cup 0 (m.owner i) positive).1
  rw [empty] at mem
  exact Finset.notMem_empty _ mem

theorem owner_one (m : Model c N states) (hi : i∈m.active) (singleton : states i={(1,1)}) : m.owner i=1 := by
  apply incoming_injective c.cup
  funext q
  apply propext
  rw [←m.actual_state i hi q,singleton,Finset.mem_singleton,incoming_one]

theorem pair_first (m : Model c N states) (p : Pair m i j q) (empty : states i=∅) : q=(1,1) := by
  obtain ⟨hi,hj,ij,eq⟩ := p
  have zero := owner_zero m hi empty
  have ord := (m.actual_order i hi j hj).mp ij
  rw [zero] at ord eq
  exact eq.symm.trans (initial_label c.cup (m.owner j) ord)

theorem pair_second (m : Model c N states) (p : Pair m i j q) (singleton : states i={(1,1)}) : q.1 ≤ 2 ∧ q.2 ≤ 2 := by
  obtain ⟨hi,hj,ij,eq⟩ := p
  have one := owner_one m hi singleton
  have ord := (m.actual_order i hi j hj).mp ij
  have a := rank_first_bound c.cup true ord
  have b := rank_first_bound c.cup false ord
  rw [←eq]
  simp only [label]
  omega

def maxLength (states : Nat→Finset Label) (b : Bool) (i : Nat) : Nat :=
  (states i).sup (fun q => if b then q.1 else q.2)+1

theorem ending_bound (m : Model c N states) (hj : j∈m.active)
    (ep : EndingPath c.cup b a (m.owner j) k) : k ≤ maxLength states b j := by
  have ord := (length_bounds ep).2.2
  have mem := (m.actual_state j hj _).mpr (label_difference c.cup a (m.owner j) ord).1
  have upper := Finset.le_sup (f:=fun q : Label => if b then q.1 else q.2) mem
  have lower := rank_ge ep
  have positive := (length_bounds ep).1
  cases b <;> simp only [maxLength,Bool.false_eq_true,if_false,if_true,label] at upper ⊢ <;> omega

def PairAllowed (states : Nat→Finset Label) (i j : Nat) := ¬states j⊆states i
def PathAllowed (N : Nat) (states : Nat→Finset Label) (b : Bool) (k s i j : Nat) : Prop :=
  s < N ∧ i < N ∧ j < N ∧ PairAllowed states s i ∧ PairAllowed states i j ∧ PairAllowed states s j ∧
  3 ≤ k ∧ k ≤ 5 ∧ k ≤ maxLength states b i+1 ∧ k ≤ maxLength states b j
instance (states : Nat→Finset Label) (i j : Nat) : Decidable (PairAllowed states i j) := by unfold PairAllowed; infer_instance
instance (N states b k s i j) : Decidable (PathAllowed N states b k s i j) := by unfold PathAllowed; infer_instance

theorem pair_allowed (m : Model c N states) (hi : i∈m.active) (hj : j∈m.active)
    (ij : m.key i < m.key j) : PairAllowed states i j := by
  obtain ⟨q,hq,_⟩ := pair_exists m hi hj ij
  exact fun sub => (Finset.mem_sdiff.mp hq).2 (sub (Finset.mem_sdiff.mp hq).1)

theorem path_allowed (m : Model c N states) (lo : 3 ≤ k) (path : NamedPath m b k s i j) :
    PathAllowed N states b k s i j := by
  obtain ⟨hs,hi,hj,si,ij,p⟩ := path
  have ep := ES7OrderedPaths.selected_path_rank p
  have upper := ES7BalancedAmbient.rank_le_five c m.noSix b (length_bounds ep).2.2 (m.owner_bound j hj)
  have lower := rank_ge ep
  refine ⟨m.active_bound s hs,m.active_bound i hi,m.active_bound j hj,
    pair_allowed m hs hi si,pair_allowed m hi hj ij,pair_allowed m hs hj (si.trans ij),lo,
    by omega,?_,ending_bound m hj ep⟩
  cases ep with
  | pair ord => omega
  | step prior ord turn => have bound := ending_bound m hi prior; omega

theorem path_bound (m : Model c N states) (path : NamedPath m b k s i j) : k ≤ maxLength states b j := by
  obtain ⟨hs,hi,hj,si,ij,p⟩ := path
  have ep := ES7OrderedPaths.selected_path_rank p
  have ord := (length_bounds ep).2.2
  have mem := (m.actual_state j hj _).mpr (label_difference c.cup (m.owner i) (m.owner j) ord).1
  have upper := Finset.le_sup (f:=fun q : Label => if b then q.1 else q.2) mem
  have lower := rank_ge ep
  have positive := (length_bounds ep).1
  cases b <;> simp only [maxLength,Bool.false_eq_true,if_false,if_true,label] at upper ⊢ <;> omega

theorem path_maximum (m : Model c N states) (path : NamedPath m b 6 s i j) : False := by
  exact ES7OrderedPaths.ending_forbidden (m.noSix b) (m.owner_bound j path.2.2.1)
    (ES7OrderedPaths.selected_path_rank path.2.2.2.2.2)

theorem path_endpoint (m : Model c N states) (path : NamedPath m b k s i j) : NamedEndpoint m b k s j :=
  ⟨path.1,path.2.2.1,i |> m.owner,path.2.2.2.2.2⟩

theorem path_base (m : Model c N states) (hs : s∈m.active) (hi : i∈m.active) (hj : j∈m.active)
    (si : m.key s < m.key i) (ij : m.key i < m.key j) (turn : Cup m s i j=b) : NamedPath m b 3 s i j := by
  refine ⟨hs,hi,hj,si,ij,ES7PathSemantics.path_three c.cup b _ _ _
    ((m.actual_order s hs i hi).mp si) ((m.actual_order i hi j hj).mp ij) ?_⟩
  simpa only [cup_ordered m hs hi hj si ij] using turn

theorem path_step (m : Model c N states) (path : NamedPath m b k s h i)
    (hj : j∈m.active) (ij : m.key i < m.key j) (turn : Cup m h i j=b) : NamedPath m b (k+1) s i j := by
  obtain ⟨hs,hh,hi,sh,hi',p⟩ := path
  refine ⟨hs,hi,hj,sh.trans hi',ij,ES7PathSemantics.path_extension c.cup b _ _ _ _ k p
    ((m.actual_order i hi j hj).mp ij) ?_⟩
  simpa only [cup_ordered m hh hi hj hi' ij] using turn

theorem endpoint_exclusion (m : Model c N states) (a b : Nat) (ha : 2 ≤ a) (hb : 2 ≤ b) (total : a+b=9)
    (cup : NamedEndpoint m true a s j) (cap : NamedEndpoint m false b s j) : False := by
  exact m.noGon (ES7OrderedPaths.weak_heptagon c (m.owner_bound j cup.2.1) ha hb total cup.2.2 cap.2.2)

end ES7NamedGeometry
