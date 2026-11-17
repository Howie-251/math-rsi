import ES7JointCatalogProof
import ES7Joint17Data
import ES7BalancedEquality

namespace ES7JointPopulations
open ES7NamedGeometry ES7ActualState ES7BalancedEndpoints ES7BalancedAmbient ES8BalancedGeometry
open ES7JointRealization ES7JointCatalog ES7JointCatalogProof ES7JointRules ES7BalancedEquality

theorem state_height_four_iff_ends (c : Configuration n)
    (noSix : NoSix c.cup (Finset.range n)) (v : Fin n) :
    Incoming c.cup v.val (1,4) ↔ EndsFive c.cup false (Finset.range n) v.val := by
  constructor
  · rintro ⟨_,_,u,uv,below⟩
    have upper := rank_le_five c noSix false uv v.isLt
    have eq : ES8ActualRanks.rank c.cup false u v.val=5 := by simp only [Below,label] at below; omega
    have path := ES8ActualRanks.rank_attained c.cup false u v.val uv
    rw [eq] at path
    exact end_of_path v.isLt path
  · rintro ⟨a,d,e,u,chain,inside⟩
    have path := ES8SlopePartition.ending_of_cup c.cup false [a,d,e] u v.val chain
    have len : ES8ActualRanks.EndingPath c.cup false u v.val 5 := by simpa using path
    have uv := (ES8ActualRanks.length_bounds len).2.2
    have lower := ES8ActualRanks.rank_ge len
    have pos := label_positive c.cup u v.val uv
    refine ⟨by omega,by omega,u,uv,pos.1,?_⟩
    simp only [label]; omega

theorem low_of_L (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50))
    (v : Fin 50) (hv : v∈L c) : Low (incoming c.cup v.val) := by
  obtain ⟨a,b⟩ := Finset.mem_inter.mp hv
  constructor
  · intro h
    have e := (state_width_four_iff_ends c noSix v).mp ((mem_incoming c noSix v.isLt).mp h)
    exact no_opposite_junction c.cup _ noSix false v.val e ((mem_starters c false v).mp b)
  · intro h
    have e := (state_height_four_iff_ends c noSix v).mp ((mem_incoming c noSix v.isLt).mp h)
    exact no_opposite_junction c.cup _ noSix true v.val e ((mem_starters c true v).mp a)

theorem high_of_R (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50))
    (v : Fin 50) (hv : v∈R c) : High (incoming c.cup v.val) := by
  obtain ⟨a,b⟩ := Finset.mem_inter.mp hv
  exact ⟨(mem_incoming c noSix v.isLt).mpr ((state_width_four_iff_ends c noSix v).mpr ((mem_enders c true v).mp a)),
    (mem_incoming c noSix v.isLt).mpr ((state_height_four_iff_ends c noSix v).mpr ((mem_enders c false v).mp b))⟩

noncomputable def index (cup : Nat→Nat→Nat→Bool) (v : Nat) : Nat := by
  classical
  exact if h : ∃i < 40,states i=incoming cup v then Classical.choose h else 0

theorem index_spec (cup : Nat→Nat→Nat→Bool) (v : Nat)
    (h : Low (incoming cup v) ∨ High (incoming cup v)) : index cup v < 40 ∧ states (index cup v)=incoming cup v := by
  have ex : ∃i < 40,states i=incoming cup v := by
    rcases h with low|high
    · obtain ⟨i,hi,eq⟩ := low_name cup v low
      exact ⟨i,by omega,eq⟩
    · obtain ⟨i,_,hi,eq⟩ := high_name cup v high
      exact ⟨i,hi,eq⟩
  unfold index
  rw [dif_pos ex]
  exact Classical.choose_spec ex

theorem index_low (cup : Nat→Nat→Nat→Bool) (v : Nat) (h : Low (incoming cup v)) : index cup v < 20 := by
  obtain ⟨i,hi,eq⟩ := low_name cup v h
  have spec := index_spec cup v (Or.inl h)
  have same := ES7JointCatalogProof.injective spec.1 (by omega : i < 40) (spec.2.trans eq.symm)
  omega

theorem index_high (cup : Nat→Nat→Nat→Bool) (v : Nat) (h : High (incoming cup v)) : 20 ≤ index cup v := by
  obtain ⟨i,lo,hi,eq⟩ := high_name cup v h
  have spec := index_spec cup v (Or.inr h)
  have same := ES7JointCatalogProof.injective spec.1 hi (spec.2.trans eq.symm)
  omega

noncomputable def lowAvailable (c : Configuration n) := available c states ∩ Finset.range 20
noncomputable def highAvailable (c : Configuration n) := available c states ∩ Finset.Ico 20 40

theorem low_population (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50)) :
    (L c).card ≤ (lowAvailable c).card := by
  classical
  apply Finset.card_le_card_of_injOn (fun v : Fin 50=>index c.cup v.val)
  · intro v hv
    have low := low_of_L c noSix v hv
    have spec := index_spec c.cup v.val (Or.inl low)
    exact Finset.mem_inter.mpr ⟨Finset.mem_filter.mpr ⟨Finset.mem_range.mpr spec.1,v.val,v.isLt,spec.2.symm⟩,
      Finset.mem_range.mpr (index_low c.cup v.val low)⟩
  · intro u hu v hv eq
    apply Fin.ext
    have a := index_spec c.cup u.val (Or.inl (low_of_L c noSix u hu))
    have b := index_spec c.cup v.val (Or.inl (low_of_L c noSix v hv))
    exact incoming_inj c noSix u.isLt v.isLt (a.2.symm.trans ((congrArg states eq).trans b.2))

theorem high_population (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50)) :
    (R c).card ≤ (highAvailable c).card := by
  classical
  apply Finset.card_le_card_of_injOn (fun v : Fin 50=>index c.cup v.val)
  · intro v hv
    have high := high_of_R c noSix v hv
    have spec := index_spec c.cup v.val (Or.inr high)
    exact Finset.mem_inter.mpr ⟨Finset.mem_filter.mpr ⟨Finset.mem_range.mpr spec.1,v.val,v.isLt,spec.2.symm⟩,
      Finset.mem_Ico.mpr ⟨index_high c.cup v.val high,spec.1⟩⟩
  · intro u hu v hv eq
    apply Fin.ext
    have a := index_spec c.cup u.val (Or.inr (high_of_R c noSix u hu))
    have b := index_spec c.cup v.val (Or.inr (high_of_R c noSix v hv))
    exact incoming_inj c noSix u.isLt v.isLt (a.2.symm.trans ((congrArg states eq).trans b.2))

theorem first_two_available (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50)) :
    ({0,1} : Finset Nat)⊆lowAvailable c := by
  classical
  intro i hi
  simp only [Finset.mem_insert,Finset.mem_singleton] at hi
  rcases hi with rfl|rfl
  · apply Finset.mem_inter.mpr
    refine ⟨Finset.mem_filter.mpr ⟨by simp,0,by omega,?_⟩,by simp⟩
    rw [catalog_checked.2.2.2.1]
    ext q
    simp only [Finset.notMem_empty,iff_false]
    intro h
    exact incoming_zero c.cup q ((mem_incoming c noSix (by omega : 0 < 50)).mp h)
  · apply Finset.mem_inter.mpr
    refine ⟨Finset.mem_filter.mpr ⟨by simp,1,by omega,?_⟩,by simp⟩
    rw [catalog_checked.2.2.2.2]
    ext q
    rw [mem_incoming c noSix (by omega : 1 < 50),incoming_one,Finset.mem_singleton]

theorem joint_seventeen_impossible (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point))
    (lo : 17 ≤ (L c).card) (hi : 17 ≤ (R c).card) : False := by
  classical
  obtain ⟨low,firsts,lowSub,lowCard⟩ := Finset.exists_subsuperset_card_eq
    (first_two_available c noSix) (by decide : ({0,1} : Finset Nat).card ≤ 17)
    (lo.trans (low_population c noSix))
  obtain ⟨high,highSub,highCard⟩ := Finset.exists_subset_card_eq (hi.trans (high_population c noSix))
  have sub : low∪high⊆available c states := by
    intro i h
    rcases Finset.mem_union.mp h with hl|hh
    · exact (Finset.mem_inter.mp (lowSub hl)).1
    · exact (Finset.mem_inter.mp (highSub hh)).1
  let m := realize c noSix noH states ES7JointCatalogProof.injective ES7JointCatalogProof.size (low∪high) sub
  apply ES7Joint17Data.impossible m
  constructor
  · change ES7NamedCounting.count (low∪high) lowNames=17
    rw [ES7NamedCounting.count_nodup_card _ _ (by decide : lowNames.Nodup)]
    have eq : lowNames.toFinset∩(low∪high)=low := by
      ext i
      have lowBound : i∈low → i < 20 := fun h=>Finset.mem_range.mp (Finset.mem_inter.mp (lowSub h)).2
      have highBound : i∈high → 20 ≤ i := fun h=>(Finset.mem_Ico.mp (Finset.mem_inter.mp (highSub h)).2).1
      simp only [lowNames,List.toFinset_range,Finset.mem_inter,Finset.mem_union,Finset.mem_range]
      constructor
      · rintro ⟨ib,hl|hh⟩
        · exact hl
        · have := highBound hh; omega
      · intro hl; exact ⟨lowBound hl,Or.inl hl⟩
    rw [eq,lowCard]
  · change ES7NamedCounting.count (low∪high) highNames=17
    rw [ES7NamedCounting.count_nodup_card _ _ (by decide : highNames.Nodup)]
    have namesEq : highNames.toFinset=Finset.Ico 20 40 := by decide
    have eq : highNames.toFinset∩(low∪high)=high := by
      rw [namesEq]
      ext i
      have lowBound : i∈low → i < 20 := fun h=>Finset.mem_range.mp (Finset.mem_inter.mp (lowSub h)).2
      have highBound : i∈high → 20 ≤ i ∧ i < 40 := fun h=>Finset.mem_Ico.mp (Finset.mem_inter.mp (highSub h)).2
      simp only [Finset.mem_inter,Finset.mem_union,Finset.mem_Ico]
      constructor
      · rintro ⟨⟨ib,ih⟩,hl|hh⟩
        · have := lowBound hl; omega
        · exact hh
      · intro hh; exact ⟨highBound hh,Or.inr hh⟩
    rw [eq,highCard]
  · exact Finset.mem_union_left high (firsts (by simp))
  · exact Finset.mem_union_left high (firsts (by simp))

theorem through_range (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)) :
    9 ≤ (X c).card ∧ (X c).card ≤ 13 := by
  obtain ⟨t,ht,x,y,l,r⟩ := four_populations c noSix noH
  constructor
  · by_contra h
    have lo : 17 ≤ (L c).card := by omega
    have hi : 17 ≤ (R c).card := by omega
    exact joint_seventeen_impossible c noSix noH lo hi
  · exact ES7ThroughSelection.through_population_le_thirteen c noSix noH

#print axioms joint_seventeen_impossible
#print axioms through_range
end ES7JointPopulations
