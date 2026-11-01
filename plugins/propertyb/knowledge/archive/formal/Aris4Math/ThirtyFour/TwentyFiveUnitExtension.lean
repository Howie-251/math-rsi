import Aris4Math.ThirtyFour.PromotionReconstruction
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.K6Classification

/-! Complete extension of actual unit-lock traces. Only disjoint old blocks
can be promoted through the new lock. The recursion below follows these
actual decisions, so its local catalogue does not omit an actual hypergraph. -/
namespace Aris4Math.ThirtyFour.TwentyFiveUnitExtension

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionReconstruction
open Aris4Math.K6Classification

variable {n v : ℕ}

def Unit (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v) : Prop :=
  ∀ i j, i ≠ j → H.codegree (f i) (f j) = 1

def blocks (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v) :
    Finset (Finset (Fin n)) :=
  Finset.univ.filter fun T => 2 ≤ T.card ∧ 0 < count H f T

def large (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v) :
    Finset (Finset (Fin n)) := largeBlocks (blocks H f)

@[simp] theorem mem_blocks (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (T : Finset (Fin n)) : T ∈ blocks H f ↔ 2 ≤ T.card ∧ 0 < count H f T := by
  simp [blocks]

@[simp] theorem mem_large (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (T : Finset (Fin n)) : T ∈ large H f ↔ 3 ≤ T.card ∧ 0 < count H f T := by
  simp only [large, largeBlocks, Finset.mem_filter, mem_blocks]
  omega

theorem count_le_one (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (unit : Unit H f) (T : Finset (Fin n)) (two : 2 ≤ T.card) : count H f T ≤ 1 := by
  obtain ⟨i, hi, j, hj, ne⟩ := Finset.one_lt_card.mp (show 1 < T.card by omega)
  exact (count_le_codegree H f T i j hi hj).trans_eq (unit i j ne)

theorem blocks_linear (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (unit : Unit H f) : BlockClassification.Linear (blocks H f) := by
  intro T hT U hU ne
  by_contra small
  obtain ⟨i, hi, j, hj, ij⟩ := Finset.one_lt_card.mp (show 1 < (T ∩ U).card by omega)
  obtain ⟨e, he⟩ := Finset.card_pos.mp (mem_blocks H f T |>.mp hT).2
  obtain ⟨a, ha⟩ := Finset.card_pos.mp (mem_blocks H f U |>.mp hU).2
  obtain ⟨heH, heT⟩ := Finset.mem_filter.mp he
  obtain ⟨haH, haU⟩ := Finset.mem_filter.mp ha
  have eq := H.edges_eq_of_codegree_one (unit i j ij) heH haH
    ((mem_lockSignature f e i).mp (heT.symm ▸ (Finset.mem_inter.mp hi).1))
    ((mem_lockSignature f e j).mp (heT.symm ▸ (Finset.mem_inter.mp hj).1))
    ((mem_lockSignature f a i).mp (haU.symm ▸ (Finset.mem_inter.mp hi).2))
    ((mem_lockSignature f a j).mp (haU.symm ▸ (Finset.mem_inter.mp hj).2))
  exact ne (heT.symm.trans ((congrArg (lockSignature f) eq).trans haU))

theorem blocks_recovered (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (unit : Unit H f) : blocks H f = pairCompletion (large H f) := by
  apply recover_pairs
  · intro T hT
    exact (mem_blocks H f T |>.mp hT).1
  · exact blocks_linear H f unit
  · intro P card
    obtain ⟨i, j, ne, rfl⟩ := Finset.card_eq_two.mp card
    have pos : 0 < H.codegree (f i) (f j) := by rw [unit i j ne]; decide
    obtain ⟨e, he⟩ := Finset.card_pos.mp pos
    obtain ⟨heH, hi, hj⟩ := Finset.mem_filter.mp he
    have hi' := (mem_lockSignature f e i).mpr hi
    have hj' := (mem_lockSignature f e j).mpr hj
    have sub : ({i,j} : Finset (Fin n)) ⊆ lockSignature f e :=
      Finset.insert_subset hi' (Finset.singleton_subset_iff.mpr hj')
    refine ⟨lockSignature f e, (mem_blocks H f _).mpr ⟨?_, ?_⟩, sub⟩
    · have le := Finset.card_le_card sub
      simpa [ne] using le
    · apply Finset.card_pos.mpr
      exact ⟨e, Finset.mem_filter.mpr ⟨heH, rfl⟩⟩

theorem blocks_size (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    {T : Finset (Fin n)} (mem : T ∈ blocks H f) : T.card ≤ 5 := by
  by_contra h
  have zero := count_eq_zero_of_large H f T (by omega)
  have pos := (mem_blocks H f T |>.mp mem).2
  omega

theorem unit_restrict (H : Simple5Hypergraph (Fin v)) (f : Fin (n+1) ↪ Fin v)
    (unit : Unit H f) : Unit H (restrict f) := by
  intro i j ne
  exact unit i.castSucc j.castSucc (by simpa using ne)

/-- Old blocks of size at least two actually promoted through the new lock. -/
def selected (H : Simple5Hypergraph (Fin v)) (f : Fin (n+1) ↪ Fin v) :
    Finset (Finset (Fin n)) :=
  Finset.univ.filter fun T => 2 ≤ T.card ∧ 0 < promotion H f T

@[simp] theorem mem_selected (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (T : Finset (Fin n)) :
    T ∈ selected H f ↔ 2 ≤ T.card ∧ 0 < promotion H f T := by simp [selected]

theorem selected_candidate (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) {T : Finset (Fin n)} (mem : T ∈ selected H f) :
    T ∈ blocks H (restrict f) ∧ T.card ≤ 4 := by
  obtain ⟨two, pos⟩ := (mem_selected H f T).mp mem
  have le := promotion_le_old H f T
  refine ⟨(mem_blocks H (restrict f) T).mpr ⟨two, by omega⟩, ?_⟩
  by_contra h
  have zero := promotion_eq_zero_of_large H f T (by omega)
  omega

theorem selected_disjoint (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (unit : Unit H f) :
    ∀ T ∈ selected H f, ∀ U ∈ selected H f, T ≠ U → Disjoint T U := by
  intro T hT U hU ne
  apply Finset.disjoint_left.mpr
  intro i hi hj
  obtain ⟨e, he⟩ := Finset.card_pos.mp ((mem_selected H f T).mp hT).2
  obtain ⟨a, ha⟩ := Finset.card_pos.mp ((mem_selected H f U).mp hU).2
  obtain ⟨heH, heT⟩ := Finset.mem_filter.mp he
  obtain ⟨haH, haU⟩ := Finset.mem_filter.mp ha
  obtain ⟨heOld, heLast⟩ := (signature_with_iff f e T).mp heT
  obtain ⟨haOld, haLast⟩ := (signature_with_iff f a U).mp haU
  have eq := H.edges_eq_of_codegree_one (unit i.castSucc (Fin.last n) (Fin.castSucc_ne_last i))
    heH haH ((mem_lockSignature (restrict f) e i).mp (heOld.symm ▸ hi)) heLast
    ((mem_lockSignature (restrict f) a i).mp (haOld.symm ▸ hj)) haLast
  exact ne (heOld.symm.trans ((congrArg (lockSignature (restrict f)) eq).trans haOld))

def extend (big chosen : Finset (Finset (Fin n))) : Finset (Finset (Fin (n+1))) :=
  ((big \ chosen).image fun T => T.map Fin.castSuccEmb) ∪ chosen.image promoted

theorem actual_extend (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (unit : Unit H f) :
    large H f = extend (large H (restrict f)) (selected H f) := by
  ext U
  by_cases present : Fin.last n ∈ U
  · have form := with_last U present
    have card : U.card = (oldTrace U).card + 1 := by
      calc U.card = (promoted (oldTrace U)).card := congrArg Finset.card form
           _ = _ := by rw [promoted, Finset.card_insert_of_notMem (last_notMem_map _), Finset.card_map]
    have count : count H f U = promotion H f (oldTrace U) :=
      congrArg (count H f) form
    have notOld : ∀ T : Finset (Fin n), T.map Fin.castSuccEmb ≠ U := by
      intro T same
      exact last_notMem_map T (same.symm ▸ present)
    simp only [mem_large, extend, Finset.mem_union, Finset.mem_image]
    constructor
    · intro h
      right
      refine ⟨oldTrace U, (mem_selected H f _).mpr ⟨by omega, ?_⟩, form.symm⟩
      simpa only [count] using h.2
    · rintro (⟨T, _, same⟩ | ⟨T, hT, same⟩)
      · exact (notOld T same).elim
      · subst U
        obtain ⟨two, pos⟩ := (mem_selected H f T).mp hT
        refine ⟨?_, pos⟩
        rw [promoted, Finset.card_insert_of_notMem (last_notMem_map _), Finset.card_map]
        omega
  · have form := without_last U present
    have card : U.card = (oldTrace U).card :=
      (congrArg Finset.card form).trans (Finset.card_map _)
    have count := count_split H f (oldTrace U)
    rw [← form] at count
    have notNew : ∀ T : Finset (Fin n), promoted T ≠ U := by
      intro T same
      apply present
      rw [← same]
      exact Finset.mem_insert_self _ _
    simp only [mem_large, extend, Finset.mem_union, Finset.mem_image]
    constructor
    · intro h
      have bound := count_le_one H (restrict f) (unit_restrict H f unit) (oldTrace U) (by omega)
      left
      refine ⟨oldTrace U, Finset.mem_sdiff.mpr ⟨(mem_large H (restrict f) _).mpr ⟨by omega, by omega⟩, ?_⟩, form.symm⟩
      intro sel
      have pos := ((mem_selected H f _).mp sel).2
      omega
    · rintro (⟨T, hT, same⟩ | ⟨T, _, same⟩)
      · subst U
        obtain ⟨big, notSel⟩ := Finset.mem_sdiff.mp hT
        obtain ⟨three, pos⟩ := (mem_large H (restrict f) T).mp big
        have zero : promotion H f T = 0 := by
          have := (mem_selected H f T).not.mp notSel
          omega
        rw [Finset.card_map]
        have split := count_split H f T
        exact ⟨three, by omega⟩
      · exact (notNew T same).elim

/-- Enumerate only pairwise disjoint promoted old blocks. -/
def choices (candidates : List (Finset (Fin n))) (chosen : Finset (Finset (Fin n))) :
    List (Finset (Finset (Fin n))) :=
  match candidates with
  | [] => [chosen]
  | T :: rest => choices rest chosen ++
      if ∀ U ∈ chosen, T ≠ U → Disjoint T U then choices rest (insert T chosen) else []

theorem choices_complete (candidates : List (Finset (Fin n)))
    (chosen target : Finset (Finset (Fin n))) (contained : chosen ⊆ target)
    (remaining : target ⊆ chosen ∪ candidates.toFinset)
    (disjoint : ∀ T ∈ target, ∀ U ∈ target, T ≠ U → Disjoint T U) :
    target ∈ choices candidates chosen := by
  induction candidates generalizing chosen with
  | nil =>
    have eq : target = chosen := Finset.Subset.antisymm (by simpa using remaining) contained
    simp [choices, eq]
  | cons T rest ih =>
    by_cases mem : T ∈ target
    · have compatible : ∀ U ∈ chosen, T ≠ U → Disjoint T U := by
        intro U hU ne
        exact disjoint T mem U (contained hU) ne
      have remaining' : target ⊆ insert T chosen ∪ rest.toFinset := by
        intro U hU
        have := remaining hU
        simp only [List.toFinset_cons, Finset.mem_union, Finset.mem_insert] at this ⊢
        tauto
      have occurs := ih (insert T chosen) (Finset.insert_subset mem contained) remaining'
      simp only [choices, if_pos compatible, List.mem_append]
      exact Or.inr occurs
    · have remaining' : target ⊆ chosen ∪ rest.toFinset := by
        intro U hU
        have := remaining hU
        simp only [List.toFinset_cons, Finset.mem_union, Finset.mem_insert] at this ⊢
        rcases this with old | eq | rest
        · exact Or.inl old
        · exact (mem (eq ▸ hU)).elim
        · exact Or.inr rest
      exact List.mem_append_left _ (ih chosen contained remaining')

theorem actual_selected_in_choices (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (unit : Unit H f)
    (candidates : List (Finset (Fin n)))
    (covers : ∀ T ∈ pairCompletion (large H (restrict f)), T.card ≤ 4 → T ∈ candidates) :
    selected H f ∈ choices candidates ∅ := by
  apply choices_complete candidates ∅ (selected H f) (Finset.empty_subset _) ?_
    (selected_disjoint H f unit)
  intro T hT
  obtain ⟨mem, small⟩ := selected_candidate H f hT
  rw [blocks_recovered H (restrict f) (unit_restrict H f unit)] at mem
  simpa using covers T mem small

end Aris4Math.ThirtyFour.TwentyFiveUnitExtension

#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitExtension.actual_extend
#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitExtension.actual_selected_in_choices
