import Aris4Math.LowDegree
import Aris4Math.Traces

/-! Actual unit-lock selection at 25 vertices and 34 edges. The tenth lock
is selected together with the first nine whenever the later proof may need it. -/

namespace Aris4Math.ThirtyFour.TwentyFiveSelection

open scoped BigOperators

def sevens (H : Simple5Hypergraph (Fin 25)) : Finset (Fin 25) :=
  Finset.univ.filter fun x => H.degree x=7

def UnitLocks {n : ℕ} (H : Simple5Hypergraph (Fin 25)) (f : Fin n↪Fin 25) : Prop :=
  ∀i j,i≠j→H.codegree (f i) (f j)=1

def MixedLocks (H : Simple5Hypergraph (Fin 25)) (l h : ℕ) : Prop :=
  ∃f : Fin (l+h)↪Fin 25,
    (∀i,H.degree (f i)=if i.val<l then 6 else 7) ∧ UnitLocks H f

def NineLowExtension (H : Simple5Hypergraph (Fin 25)) : Prop :=
  ∃f : Fin 10↪Fin 25,(∀i,i.val<9→H.degree (f i)=6) ∧
    (H.degree (f 9)=6 ∨ H.degree (f 9)=7) ∧ UnitLocks H f

theorem degree_budgets (H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering)
    (size : H.edges.card=34) :
    5≤H.sixVertices.card ∧ 30≤2*H.sixVertices.card+(sevens H).card := by
  have minimum (x : Fin 25) : 6≤H.degree x := by
    have bound := H.pairCovering_degree_bound cover x
    simp only [Fintype.card_fin] at bound
    omega
  have each7 (x : Fin 25) : 7≤H.degree x+(if H.degree x=6 then 1 else 0) := by
    have lower := minimum x
    split_ifs <;> omega
  have each8 (x : Fin 25) : 8≤H.degree x+
      (if H.degree x=6 then 2 else 0)+(if H.degree x=7 then 1 else 0) := by
    have lower := minimum x
    split_ifs <;> omega
  have sum7 := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each7 x)
  have budget7 : 175≤170+H.sixVertices.card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,Simple5Hypergraph.sixVertices] using sum7
  have sumtwo : (∑x : Fin 25,if H.degree x=6 then 2 else 0)=2*H.sixVertices.card := by
    rw [←Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices,Nat.mul_comm]
  have sum8 := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each8 x)
  have budget8 : 200≤170+2*H.sixVertices.card+(sevens H).card := by
    simpa [Finset.sum_add_distrib,sumtwo,H.sum_degrees,size,sevens] using sum8
  omega

/-- Greedy selection with an actual global bound on nonunit partners.
It is consumed below at k=4,2,1 and d=4. -/
theorem unit_subset_of_bad_bound (H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering)
    (k d : ℕ) (S : Finset (Fin 25))
    (maximum : ∀x∈S,(H.badPartners x).card≤d)
    (large : (k-1)*(d+1)<S.card) :
    ∃T⊆S,T.card=k ∧ H.UnitCodegrees T := by
  induction k generalizing S with
  | zero => exact ⟨∅,Finset.empty_subset _,rfl,by simp [Simple5Hypergraph.UnitCodegrees]⟩
  | succ k ih =>
    have positive : 0<S.card := by omega
    obtain ⟨x,hx⟩ := Finset.card_pos.mp positive
    let B := insert x (H.badPartners x)
    let R := S\B
    have small : B.card≤d+1 := by
      have bound := maximum x hx
      have add := Finset.card_insert_le x (H.badPartners x)
      dsimp [B]
      omega
    have sub : R⊆S := Finset.sdiff_subset
    have good (y : Fin 25) (hy : y∈R) : y≠x ∧ H.codegree x y=1 :=
      (H.mem_goodPartners cover x y).mp
        (Finset.mem_sdiff.mpr ⟨Finset.mem_univ _,(Finset.mem_sdiff.mp hy).2⟩)
    by_cases kz : k=0
    · subst k
      refine ⟨{x},Finset.singleton_subset_iff.mpr hx,by simp,?_⟩
      intro a ha b hb ne
      have ax := Finset.mem_singleton.mp ha
      have bx := Finset.mem_singleton.mp hb
      exact (ne (ax.trans bx.symm)).elim
    · have bound := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
      change S.card≤R.card+B.card at bound
      have split : (k-1)*(d+1)+(d+1)=k*(d+1) := by
        calc
          _ = ((k-1)+1)*(d+1) := by simp only [Nat.add_mul,Nat.one_mul]
          _ = _ := by rw [Nat.sub_add_cancel (by omega : 1≤k)]
      have next : (k-1)*(d+1)<R.card := by
        simp only [Nat.add_sub_cancel] at large
        omega
      obtain ⟨T,tSub,tCard,tUnit⟩ := ih R (fun y hy => maximum y (sub hy)) next
      have xnot : x∉T := fun h => (good x (tSub h)).1 rfl
      refine ⟨insert x T,Finset.insert_subset hx (tSub.trans sub),by simp [xnot,tCard],?_⟩
      intro a ha b hb ne
      rcases Finset.mem_insert.mp ha with rfl | haT
      · rcases Finset.mem_insert.mp hb with rfl | hbT
        · exact (ne rfl).elim
        · exact (good b (tSub hbT)).2
      · rcases Finset.mem_insert.mp hb with rfl | hbT
        · rw [H.codegree_comm]
          exact (good a (tSub haT)).2
        · exact tUnit a haT b hbT ne

theorem unit_sevens (H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering)
    (k : ℕ) (large : (k-1)*5<(sevens H).card) :
    ∃T⊆sevens H,T.card=k ∧ H.UnitCodegrees T := by
  apply unit_subset_of_bad_bound H cover k 4 (sevens H) ?_ large
  intro x hx
  have bound := H.badPartners_card_le_excess cover x
  have degree := (Finset.mem_filter.mp hx).2
  simpa [degree] using bound

/-- Indexing a finite actual set, without imposing a canonical label order. -/
theorem index_set (S : Finset (Fin 25)) {n : ℕ} (card : S.card=n) :
    ∃f : Fin n↪Fin 25,∀i,f i∈S := by
  let e : ↥S≃Fin n := Fintype.equivFinOfCardEq (by simpa using card)
  exact ⟨⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩,
    fun i => (e.symm i).property⟩

theorem mixed_locks (H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering)
    (l h : ℕ) (low : l≤H.sixVertices.card)
    (U : Finset (Fin 25)) (uSub : U⊆sevens H) (uCard : U.card=h)
    (uUnit : H.UnitCodegrees U) : MixedLocks H l h := by
  obtain ⟨L,lSub,lCard⟩ := Finset.exists_subset_card_eq low
  have lDegree (x : Fin 25) (hx : x∈L) : H.degree x=6 :=
    (Finset.mem_filter.mp (lSub hx)).2
  have uDegree (x : Fin 25) (hx : x∈U) : H.degree x=7 :=
    (Finset.mem_filter.mp (uSub hx)).2
  obtain ⟨a,ain⟩ := index_set L lCard
  obtain ⟨b,bin⟩ := index_set U uCard
  let f : Fin (l+h)↪Fin 25 := ⟨Fin.append a b,Fin.append_injective_iff.mpr
    ⟨a.injective,b.injective,by
      intro i j eq
      have da := lDegree _ (ain i)
      have db := uDegree _ (bin j)
      rw [eq] at da
      omega⟩⟩
  have parts (i : Fin (l+h)) : (i.val<l ∧ f i∈L) ∨ (l≤i.val ∧ f i∈U) := by
    refine Fin.addCases (fun j => ?_) (fun j => ?_) i
    · left
      exact ⟨j.isLt,by simpa [f] using ain j⟩
    · right
      exact ⟨by simp,by simpa [f] using bin j⟩
  refine ⟨f,?_,?_⟩
  · intro i
    rcases parts i with ⟨lt,inside⟩ | ⟨ge,inside⟩
    · rw [if_pos lt]
      exact lDegree _ inside
    · rw [if_neg (by omega)]
      exact uDegree _ inside
  · intro i j ne
    rcases parts i with ⟨_,inside⟩ | ⟨_,inside⟩
    · exact H.codegree_eq_one_of_twenty_five cover (by simp) (lDegree _ inside) (f.injective.ne ne)
    · rcases parts j with ⟨_,jinside⟩ | ⟨_,jinside⟩
      · rw [H.codegree_comm]
        exact H.codegree_eq_one_of_twenty_five cover (by simp) (lDegree _ jinside)
          (f.injective.ne ne.symm)
      · exact uUnit _ inside _ jinside (f.injective.ne ne)

/-- A single actual selection supplies all three catalogue branches, including
the real tenth lock needed by any nine-lock residue. -/
theorem exists_nine_or_ten_unit_locks (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (size : H.edges.card=34) :
    MixedLocks H 5 4 ∨ MixedLocks H 8 2 ∨ NineLowExtension H := by
  obtain ⟨low,budget⟩ := degree_budgets H cover size
  by_cases few : H.sixVertices.card<8
  · obtain ⟨U,sub,card,unit⟩ := unit_sevens H cover 4 (by omega)
    exact Or.inl (mixed_locks H cover 5 4 low U sub card unit)
  · right
    by_cases eight : H.sixVertices.card=8
    · obtain ⟨U,sub,card,unit⟩ := unit_sevens H cover 2 (by omega)
      exact Or.inl (mixed_locks H cover 8 2 (by omega) U sub card unit)
    · right
      by_cases ten : 10≤H.sixVertices.card
      · obtain ⟨L,sub,card⟩ := Finset.exists_subset_card_eq ten
        obtain ⟨f,inside⟩ := index_set L card
        have degrees (i) : H.degree (f i)=6 := (Finset.mem_filter.mp (sub (inside i))).2
        refine ⟨f,fun i _ => degrees i,Or.inl (degrees 9),?_⟩
        intro i j ne
        exact H.codegree_eq_one_of_twenty_five cover (by simp) (degrees i) (f.injective.ne ne)
      · have nine : H.sixVertices.card=9 := by omega
        obtain ⟨U,sub,card,unit⟩ := unit_sevens H cover 1 (by omega)
        obtain ⟨f,degrees,pairs⟩ := mixed_locks H cover 9 1 (by omega) U sub card unit
        refine ⟨f,?_,Or.inr ?_,pairs⟩
        · intro i hi
          simpa only [if_pos hi] using degrees i
        · simpa using degrees 9

end Aris4Math.ThirtyFour.TwentyFiveSelection

#print axioms Aris4Math.ThirtyFour.TwentyFiveSelection.exists_nine_or_ten_unit_locks
