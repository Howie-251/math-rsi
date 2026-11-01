import Aris4Math.ThirtyThree.TwentyFourSelection

/-! Redirecting a four-low-lock full trace to the single-triple case or a
full five-low edge with at most one exceptional pair. -/
namespace Aris4Math.ThirtyThree.TwentyFourQuadRedirect

open TwentyFourSelection
variable {V : Type*} [Fintype V] [DecidableEq V]

def TripleLocks (H : Simple5Hypergraph V) : Prop :=
  ∃ S : Finset V, S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
    ∃ B ⊆ S, B.card = 3 ∧
      H.multiTraces S = insert B ((S.powersetCard 2).filter fun P => ¬ P ⊆ B)

def FullFiveLocks (H : Simple5Hypergraph V) : Prop :=
  ∃ E ∈ H.edges, (∀ x ∈ E, H.degree x = 6) ∧
    (H.UnitCodegrees E ∨
      ∃ a ∈ E, ∃ b ∈ E, a ≠ b ∧ H.codegree a b = 2 ∧
        ∀ u ∈ E, ∀ v ∈ E, u ≠ v →
          ({u,v} : Finset V) ≠ {a,b} → H.codegree u v = 1)

theorem triple_of_low_outside (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (S : Finset V)
    (four : S.card = 4) (degrees : ∀ x ∈ S, H.degree x = 6)
    (unit : H.UnitCodegrees S) (E : Finset V) (edge : E ∈ H.edges) (sub : S ⊆ E)
    (z : V) (dz : H.degree z = 6) (outside : z ∉ E) : TripleLocks H := by
  let C := S \ H.badPartners z
  have csize : 3 ≤ C.card := by
    have hs := Finset.card_le_card_sdiff_add_card (s := S) (t := H.badPartners z)
    have hb := H.badPartners_card_le_one_of_twenty_four cover vertices dz
    dsimp [C]
    omega
  obtain ⟨A,subA,three⟩ := Finset.exists_subset_card_eq csize
  have asub : A ⊆ S := subA.trans Finset.sdiff_subset
  have anot : z ∉ A := fun hz => outside (sub (asub hz))
  have good (a : V) (ha : a ∈ A) : a ≠ z ∧ H.codegree z a = 1 := by
    have az : a ≠ z := by intro eq; subst a; exact anot ha
    have nb : a ∉ H.badPartners z := (Finset.mem_sdiff.mp (subA ha)).2
    apply (H.mem_goodPartners cover z a).mp
    apply Finset.mem_sdiff.mpr
    exact ⟨Finset.mem_univ _,by simpa only [Finset.mem_insert,not_or] using And.intro az nb⟩
  let T := insert z A
  have tcard : T.card = 4 := by dsimp [T]; rw [Finset.card_insert_of_notMem anot,three]
  have tdegrees (x : V) (hx : x ∈ T) : H.degree x = 6 := by
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact dz
    · exact degrees x (asub hx)
  have tunit : H.UnitCodegrees T := by
    intro x hx y hy xy
    rcases Finset.mem_insert.mp hx with rfl | hxA
    · rcases Finset.mem_insert.mp hy with rfl | hyA
      · exact False.elim (xy rfl)
      · exact (good y hyA).2
    · rcases Finset.mem_insert.mp hy with hyz | hyA
      · subst y
        rw [H.codegree_comm]
        exact (good x hxA).2
      · exact unit x (asub hxA) y (asub hyA) xy
  have trace : E ∩ T = A := by
    ext x
    constructor
    · rintro hx
      obtain ⟨xe,xt⟩ := Finset.mem_inter.mp hx
      rcases Finset.mem_insert.mp xt with rfl | xa
      · exact False.elim (outside xe)
      · exact xa
    · intro xa
      exact Finset.mem_inter.mpr ⟨sub (asub xa),Finset.mem_insert_of_mem xa⟩
  have block : A ∈ H.multiTraces T :=
    (H.mem_multiTraces T A).mpr ⟨⟨E,edge,trace⟩,by omega⟩
  rcases H.classify_four_lock_traces T tunit tcard with pairs | triple | full
  · rw [pairs] at block
    have := (Finset.mem_powersetCard.mp block).2
    omega
  · exact ⟨T,tcard,tdegrees,tunit,triple⟩
  · rw [full] at block
    have eqAT := Finset.mem_singleton.mp block
    have hc := congrArg Finset.card eqAT
    omega

/-- A full five-low edge containing four unit locks has at most one bad pair.
The exceptional-pair conclusion gives all remaining actual codegrees. -/
theorem full_five_of_all_low_inside (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (many : 5 ≤ H.sixVertices.card)
    (S : Finset V) (four : S.card = 4) (unit : H.UnitCodegrees S)
    (E : Finset V) (edge : E ∈ H.edges) (sub : S ⊆ E)
    (inside : H.sixVertices ⊆ E) : FullFiveLocks H := by
  have ecard := H.five_uniform E edge
  have lows : H.sixVertices = E :=
    Finset.eq_of_subset_of_card_le inside (by omega)
  have degrees (x : V) (hx : x ∈ E) : H.degree x = 6 := by
    rw [← lows] at hx
    exact (Finset.mem_filter.mp hx).2
  refine ⟨E,edge,degrees,?_⟩
  by_cases eunit : H.UnitCodegrees E
  · exact Or.inl eunit
  · right
    have outsideCard : (E \ S).card ≤ 1 := by
      rw [Finset.card_sdiff_of_subset sub,ecard,four]
    have outside_unique (u w : V) (hu : u ∈ E) (hw : w ∈ E)
        (uns : u ∉ S) (wns : w ∉ S) : u = w :=
      Finset.card_le_one.mp outsideCard u (Finset.mem_sdiff.mpr ⟨hu,uns⟩)
        w (Finset.mem_sdiff.mpr ⟨hw,wns⟩)
    have handle (w a : V) (hw : w ∈ E) (ha : a ∈ E) (wa : w ≠ a)
        (wns : w ∉ S) (bad : 2 ≤ H.codegree w a) :
        H.codegree w a = 2 ∧
        ∀ u ∈ E, ∀ v ∈ E, u ≠ v →
          ({u,v} : Finset V) ≠ {w,a} → H.codegree u v = 1 := by
      have upper := six_codegree_le_two H cover vertices (degrees w hw) wa
      refine ⟨by omega, ?_⟩
      intro u hu v hv uv notpair
      by_cases us : u ∈ S
      · by_cases vs : v ∈ S
        · exact unit u us v vs uv
        · have vw := outside_unique v w hv hw vs wns
          subst v
          have ua : u ≠ a := by
            intro eq
            subst u
            exact notpair (by ext q; simp [or_comm])
          rw [H.codegree_comm]
          exact unit_of_other_bad H cover vertices (degrees w hw) wa bad uv.symm ua.symm
      · have uw := outside_unique u w hu hw us wns
        subst u
        have va : v ≠ a := by intro eq; subst v; exact notpair rfl
        exact unit_of_other_bad H cover vertices (degrees w hw) wa bad uv va.symm
    obtain ⟨a,ha,b,hb,ab,bad⟩ := exists_bad_of_not_unit H cover E eunit
    by_cases as : a ∈ S
    · have bn : b ∉ S := by
        intro bs
        have h := unit a as b bs ab
        omega
      have badba : 2 ≤ H.codegree b a := by simpa [H.codegree_comm] using bad
      exact ⟨b,hb,a,ha,ab.symm,handle b a hb ha ab.symm bn badba⟩
    · exact ⟨a,ha,b,hb,ab,handle a b ha hb ab as bad⟩

/-- The full-four trace can always be redirected using the actual low set. -/
theorem redirect_full_four (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (many : 5 ≤ H.sixVertices.card)
    (S : Finset V) (four : S.card = 4) (degrees : ∀ x ∈ S, H.degree x = 6)
    (unit : H.UnitCodegrees S) (full : H.multiTraces S = {S}) :
    TripleLocks H ∨ FullFiveLocks H := by
  have block : S ∈ H.multiTraces S := by rw [full]; simp
  obtain ⟨⟨E,edge,trace⟩,_⟩ := (H.mem_multiTraces S S).mp block
  have sub : S ⊆ E := by rw [← trace]; exact Finset.inter_subset_left
  by_cases inside : H.sixVertices ⊆ E
  · exact Or.inr (full_five_of_all_low_inside H cover vertices many S four unit E edge sub inside)
  · obtain ⟨z,hz,outside⟩ := Finset.not_subset.mp inside
    have dz : H.degree z = 6 := (Finset.mem_filter.mp hz).2
    exact Or.inl (triple_of_low_outside H cover vertices S four degrees unit E edge sub z dz outside)

/-- The at-least-five-low branch has only pair, triple, full-five and
five-two-matching inputs. In particular a four-point full trace is not left
as an unhandled probability case. -/
theorem selected_low_branch (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (many : 5 ≤ H.sixVertices.card) :
    (∃ S : Finset V, S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧
      H.UnitCodegrees S ∧ H.multiTraces S = S.powersetCard 2) ∨
    TripleLocks H ∨ FullFiveLocks H ∨ FiveMatchingLocks H := by
  rcases four_unit_or_five_matching H cover vertices many with ⟨S,four,degrees,unit⟩ | matching
  · rcases H.classify_four_lock_traces S unit four with pairs | triple | full
    · exact Or.inl ⟨S,four,degrees,unit,pairs⟩
    · exact Or.inr (Or.inl ⟨S,four,degrees,unit,triple⟩)
    · rcases redirect_full_four H cover vertices many S four degrees unit full with triple | fullfive
      · exact Or.inr (Or.inl triple)
      · exact Or.inr (Or.inr (Or.inl fullfive))
  · exact Or.inr (Or.inr (Or.inr matching))

theorem selected_of_twenty_four (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    (∃ S : Finset V, S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧
      H.UnitCodegrees S ∧ H.multiTraces S = S.powersetCard 2) ∨
    TripleLocks H ∨ FullFiveLocks H ∨ FiveMatchingLocks H ∨ MixedLocks H := by
  rcases five_six_or_many_seven H cover edges vertices with low | high
  · rcases selected_low_branch H cover vertices low with pairs | triple | full | matching
    · exact Or.inl pairs
    · exact Or.inr (Or.inl triple)
    · exact Or.inr (Or.inr (Or.inl full))
    · exact Or.inr (Or.inr (Or.inr (Or.inl matching)))
  · exact Or.inr (Or.inr (Or.inr (Or.inr
      (mixed_locks_of_many_sevens H cover edges vertices (by omega)))))

end Aris4Math.ThirtyThree.TwentyFourQuadRedirect

#print axioms Aris4Math.ThirtyThree.TwentyFourQuadRedirect.selected_of_twenty_four
