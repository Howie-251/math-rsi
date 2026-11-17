import ES7JointCatalog

namespace ES7JointRealization
open ES7NamedGeometry ES7ActualState ES7BalancedEndpoints ES7BalancedAmbient ES8BalancedGeometry

def grid : Finset Label := (Finset.Icc 1 4)×ˢ(Finset.Icc 1 4)
noncomputable def incoming (cup : Nat→Nat→Nat→Bool) (v : Nat) : Finset Label := by
  classical
  exact grid.filter (Incoming cup v)

theorem incoming_bound (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (vn : v < n) (h : Incoming c.cup v q) : q∈grid := by
  obtain ⟨p1,p2,u,uv,below⟩ := h
  have a := rank_le_five c noSix true uv vn
  have b := rank_le_five c noSix false uv vn
  simp only [grid,Finset.mem_product,Finset.mem_Icc]
  simp only [Below,label] at below
  exact ⟨⟨p1,by omega⟩,⟨p2,by omega⟩⟩

theorem mem_incoming (c : Configuration n) (noSix : NoSix c.cup (Finset.range n)) (vn : v < n) :
    q∈incoming c.cup v ↔ Incoming c.cup v q := by
  classical
  simp only [incoming,Finset.mem_filter]
  exact ⟨And.right,fun h=>⟨incoming_bound c noSix vn h,h⟩⟩

theorem incoming_subset_order (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (un : u < n) (vn : v < n) (sub : incoming c.cup u⊆incoming c.cup v) : u ≤ v := by
  by_contra h
  have vu : v < u := by omega
  have diff := label_difference c.cup v u vu
  exact diff.2 ((mem_incoming c noSix vn).mp (sub ((mem_incoming c noSix un).mpr diff.1)))

theorem incoming_inj (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (un : u < n) (vn : v < n) (eq : incoming c.cup u=incoming c.cup v) : u=v := by
  exact Nat.le_antisymm (incoming_subset_order c noSix un vn eq.subset)
    (incoming_subset_order c noSix vn un eq.symm.subset)

noncomputable def available (c : Configuration n) (states : Nat→Finset Label) : Finset Nat := by
  classical
  exact (Finset.range 40).filter (fun i=>∃v < n,incoming c.cup v=states i)

noncomputable def owner (c : Configuration n) (states : Nat→Finset Label) (i : Nat) : Nat :=
  if h : ∃v < n,incoming c.cup v=states i then Classical.choose h else 0

theorem owner_spec (c : Configuration n) (states : Nat→Finset Label) (h : i∈available c states) :
    owner c states i < n ∧ incoming c.cup (owner c states i)=states i := by
  classical
  have ex := (Finset.mem_filter.mp h).2
  unfold owner
  rw [dif_pos ex]
  exact Classical.choose_spec ex

noncomputable def cut (c : Configuration n) (states : Nat→Finset Label) (i : Nat) : Nat := by
  classical
  exact (Finset.range n).sup (fun v=>if incoming c.cup v⊆states i then v+1 else 0)

noncomputable def key (c : Configuration n) (states : Nat→Finset Label) (i : Nat) : Nat :=
  680*cut c states i+40*(states i).card+i

theorem cut_mono (c : Configuration n) (states : Nat→Finset Label) (sub : states i⊆states j) :
    cut c states i ≤ cut c states j := by
  classical
  apply Finset.sup_le
  intro v hv
  by_cases present : incoming c.cup v⊆states i
  · have also := present.trans sub
    have h := Finset.le_sup (s:=Finset.range n) (f:=fun v=>if incoming c.cup v⊆states j then v+1 else 0) hv
    simpa [cut,present,also] using h
  · simp [present]

theorem cut_actual (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (states : Nat→Finset Label) (vn : v < n) (eq : incoming c.cup v=states i) : cut c states i=v+1 := by
  classical
  apply Nat.le_antisymm
  · apply Finset.sup_le
    intro u hu
    split
    next sub =>
      rw [←eq] at sub
      exact Nat.add_le_add_right (incoming_subset_order c noSix (Finset.mem_range.mp hu) vn sub) 1
    next missing => omega
  · have h := Finset.le_sup (s:=Finset.range n) (f:=fun u=>if incoming c.cup u⊆states i then u+1 else 0) (Finset.mem_range.mpr vn)
    simpa [cut,eq] using h

theorem key_inj (c : Configuration n) (states : Nat→Finset Label) : Set.InjOn (key c states) (Set.Iio 40) := by
  intro i ih j jh eq
  have h := congrArg (·%40) eq
  dsimp only [key] at h
  change i < 40 at ih
  change j < 40 at jh
  omega

theorem key_inclusion (c : Configuration n) (states : Nat→Finset Label)
    (ih : i < 40) (jh : j < 40) (sub : states i⊂states j) : key c states i < key c states j := by
  have a := cut_mono c states sub.subset
  have b := Finset.card_lt_card sub
  unfold key
  omega

theorem key_actual (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (states : Nat→Finset Label) (inj : Set.InjOn states (Set.Iio 40)) (size : ∀i < 40,(states i).card ≤ 16)
    (hi : i∈available c states) (hj : j∈available c states) :
    key c states i < key c states j ↔ owner c states i < owner c states j := by
  classical
  have si := owner_spec c states hi
  have sj := owner_spec c states hj
  have ki := cut_actual c noSix states si.1 si.2
  have kj := cut_actual c noSix states sj.1 sj.2
  have ib : i < 40 := Finset.mem_range.mp (Finset.mem_filter.mp hi).1
  have jb : j < 40 := Finset.mem_range.mp (Finset.mem_filter.mp hj).1
  have ci := size i ib
  have cj := size j jb
  constructor
  · intro lt
    by_contra bad
    by_cases eq : owner c states i=owner c states j
    · have st : states i=states j := by rw [←si.2,←sj.2,eq]
      have ij := inj ib jb st
      subst j
      exact (lt_irrefl _ lt)
    · unfold key at lt
      omega
  · intro lt
    unfold key
    omega

noncomputable def realize (c : Configuration n) (noSix : NoSix c.cup (Finset.range n))
    (noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point))
    (states : Nat→Finset Label) (inj : Set.InjOn states (Set.Iio 40))
    (size : ∀i < 40,(states i).card ≤ 16) (active : Finset Nat)
    (sub : active⊆available c states) : Model c 40 states where
  active := active
  active_bound := by
    classical
    exact fun i hi=>Finset.mem_range.mp (Finset.mem_filter.mp (sub hi)).1
  owner := owner c states
  owner_bound := fun i hi=>(owner_spec c states (sub hi)).1
  key := key c states
  key_injective := key_inj c states
  actual_order := fun i hi j hj=>key_actual c noSix states inj size (sub hi) (sub hj)
  actual_state := by
    intro i hi q
    have spec := owner_spec c states (sub hi)
    rw [←spec.2]
    exact mem_incoming c noSix spec.1
  inclusion_order := fun i j ih jh=>key_inclusion c states ih jh
  noSix := noSix
  noGon := noGon

end ES7JointRealization
