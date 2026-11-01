import Aris4Math.ThirtyThree.TwentyThreeClusterMoments
import Aris4Math.ThirtyThree.TwentyTwoSelection

/-! Actual lock selection from the codegree-two cluster partition on 23 points. -/
namespace Aris4Math.ThirtyThree.TwentyThreeClusterSelection

open scoped BigOperators
open TwentyThreeSelection TwentyTwoSelection TwentyThreeClusterMoments
variable {V : Type*} [Fintype V] [DecidableEq V]

def clusters (H : Simple5Hypergraph V) (S : Finset V) : Finset (Finset V) :=
  S.image (cluster H S)

theorem cluster_card_le_seven (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (S : Finset V) (a : V) (da : H.degree a = 7) :
    (cluster H S a).card ≤ 7 := by
  have sub : cluster H S a ⊆ insert a (H.badPartners a) := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact Finset.mem_insert_self _ _
    · obtain ⟨_,za,az⟩ := Finset.mem_filter.mp hz
      exact Finset.mem_insert_of_mem (Finset.mem_filter.mpr ⟨by simp [za], by omega⟩)
  have h := Finset.card_le_card sub
  have hi := Finset.card_insert_le a (H.badPartners a)
  have hb := seven_badPartners_le_six H cover vertices da
  omega

theorem cluster_eq_of_mem (H : Simple5Hypergraph V) (S : Finset V)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1)
    {a b : V} (ha : a ∈ S) (hb : b ∈ cluster H S a) :
    cluster H S b = cluster H S a := by
  have sub := cluster_subset H S a ha
  obtain ⟨clique,cross⟩ := cluster_relations H S a ha range noPath
  ext z
  constructor
  · intro hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact hb
    · obtain ⟨hzS,zb,bz⟩ := Finset.mem_filter.mp hz
      by_contra out
      have one := cross b hb z hzS out
      omega
  · intro hz
    by_cases zb : z = b
    · subst z
      exact Finset.mem_insert_self _ _
    · exact Finset.mem_insert_of_mem (Finset.mem_filter.mpr
        ⟨sub hz,zb,clique b hb z hz (Ne.symm zb)⟩)

theorem clusters_disjoint (H : Simple5Hypergraph V) (S : Finset V)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1)
    {A B : Finset V} (hA : A ∈ clusters H S) (hB : B ∈ clusters H S) (ne : A ≠ B) :
    Disjoint A B := by
  obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp hA
  obtain ⟨b,hb,rfl⟩ := Finset.mem_image.mp hB
  apply Finset.disjoint_left.mpr
  intro z hza hzb
  exact ne ((cluster_eq_of_mem H S range noPath ha hza).symm.trans
    (cluster_eq_of_mem H S range noPath hb hzb))

theorem clusters_cover (H : Simple5Hypergraph V) (S : Finset V) :
    (clusters H S).biUnion id = S := by
  ext x
  constructor
  · intro hx
    obtain ⟨A,hA,hx⟩ := Finset.mem_biUnion.mp hx
    obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp hA
    exact cluster_subset H S a ha hx
  · intro hx
    exact Finset.mem_biUnion.mpr ⟨cluster H S x, Finset.mem_image.mpr ⟨x,hx,rfl⟩,
      Finset.mem_insert_self _ _⟩

theorem clusters_facts (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (S : Finset V)
    (degrees : ∀ x ∈ S, H.degree x = 7)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1)
    {A : Finset V} (hA : A ∈ clusters H S) :
    A.Nonempty ∧ A ⊆ S ∧ A.card ≤ 7 ∧
      (∀ x ∈ A, ∀ y ∈ A, x ≠ y → H.codegree x y = 2) ∧
      (∀ x ∈ A, ∀ y ∈ S, y ∉ A → H.codegree x y = 1) := by
  obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp hA
  exact ⟨⟨a,Finset.mem_insert_self _ _⟩,cluster_subset H S a ha,
    cluster_card_le_seven H cover vertices S a (degrees a ha),
    cluster_relations H S a ha range noPath⟩

theorem exists_retained_pair (A e : Finset V) (size : 2 ≤ A.card) :
    ∃ P : Finset V, P ⊆ A ∧ P.card = 2 ∧ min (e ∩ A).card 2 ≤ (e ∩ P).card := by
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq (min_le_left (e ∩ A).card 2)
  have subA : T ⊆ A := sub.trans Finset.inter_subset_right
  obtain ⟨P,TP,PA,pcard⟩ := Finset.exists_subsuperset_card_eq subA
    (by rw [card]; exact min_le_right _ _) size
  refine ⟨P,PA,pcard,?_⟩
  rw [←card]
  exact Finset.card_le_card (fun x hx => Finset.mem_inter.mpr
    ⟨(Finset.mem_inter.mp (sub hx)).1,TP hx⟩)

def FiveCase (H : Simple5Hypergraph V) : Prop :=
  ∃ f : Fin 5 → V, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
    H.codegree (f 0) (f 1) ≤ 2 ∧
    ∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → H.codegree (f i) (f j) = 1

def SixCase (H : Simple5Hypergraph V) : Prop :=
  ∃ f : Fin 6 → V, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
    (∀ i j, i < j → H.codegree (f i) (f j) = if i.val / 2 = j.val / 2 then 2 else 1) ∧
    ∃ e ∈ H.edges, 4 ≤ (e ∩ Finset.univ.image f).card

theorem indexed_image_eq {n : ℕ} (P : Finset V) (f : Fin n → V)
    (inj : Function.Injective f) (inside : ∀ i, f i ∈ P) (card : P.card = n) :
    Finset.univ.image f = P := by
  apply Finset.eq_of_subset_of_card_le
  · intro x hx
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
    exact inside i
  · rw [Finset.card_image_of_injective _ inj, Finset.card_univ, Fintype.card_fin,card]

theorem indexed_trace_card {n : ℕ} (f : Fin n → V) (inj : Function.Injective f)
    (e : Finset V) :
    (Finset.univ.filter fun i => f i ∈ e).card = (e ∩ Finset.univ.image f).card := by
  have image : (Finset.univ.filter fun i => f i ∈ e).image f = e ∩ Finset.univ.image f := by
    ext x
    simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_inter]
    constructor
    · rintro ⟨i,hi,rfl⟩
      exact ⟨hi,i,rfl⟩
    · rintro ⟨he,i,rfl⟩
      exact ⟨i,he,rfl⟩
  rw [←image, Finset.card_image_of_injective _ inj]

set_option maxHeartbeats 800000 in
/-- Choose two actual vertices per clique, retaining the moment witness edge. -/
theorem six_of_three_cliques (H : Simple5Hypergraph V) (A B C : Finset V)
    (ab : Disjoint A B) (ac : Disjoint A C) (bc : Disjoint B C)
    (degrees : ∀ x ∈ A ∪ B ∪ C, H.degree x = 7)
    (aa : ∀ x ∈ A, ∀ y ∈ A, x ≠ y → H.codegree x y = 2)
    (bb : ∀ x ∈ B, ∀ y ∈ B, x ≠ y → H.codegree x y = 2)
    (cc : ∀ x ∈ C, ∀ y ∈ C, x ≠ y → H.codegree x y = 2)
    (crossAB : ∀ x ∈ A, ∀ y ∈ B, H.codegree x y = 1)
    (crossAC : ∀ x ∈ A, ∀ y ∈ C, H.codegree x y = 1)
    (crossBC : ∀ x ∈ B, ∀ y ∈ C, H.codegree x y = 1)
    (ha : 5 ≤ A.card ∧ A.card ≤ 7) (hb : 5 ≤ B.card ∧ B.card ≤ 7)
    (hc : 5 ≤ C.card ∧ C.card ≤ 7) (many : 19 ≤ A.card+B.card+C.card) : SixCase H := by
  obtain ⟨e,he,large⟩ := exists_large_clipped_trace H A B C ab ac bc degrees aa bb cc
    crossAB crossAC crossBC ha hb hc many
  obtain ⟨P,PA,Pcard,Pe⟩ := exists_retained_pair A e (by omega)
  obtain ⟨Q,QB,Qcard,Qe⟩ := exists_retained_pair B e (by omega)
  obtain ⟨R,RC,Rcard,Re⟩ := exists_retained_pair C e (by omega)
  obtain ⟨p,pinj,pmem⟩ := exists_indexed_subset P (show 2 ≤ P.card by omega)
  obtain ⟨q,qinj,qmem⟩ := exists_indexed_subset Q (show 2 ≤ Q.card by omega)
  obtain ⟨r,rinj,rmem⟩ := exists_indexed_subset R (show 2 ≤ R.card by omega)
  have pa (i : Fin 2) := PA (pmem i)
  have qb (i : Fin 2) := QB (qmem i)
  have rc (i : Fin 2) := RC (rmem i)
  have pq (i j : Fin 2) : p i ≠ q j := by
    intro eq
    exact Finset.disjoint_left.mp ab (pa i) (eq.symm ▸ qb j)
  have pr (i j : Fin 2) : p i ≠ r j := by
    intro eq
    exact Finset.disjoint_left.mp ac (pa i) (eq.symm ▸ rc j)
  have qr (i j : Fin 2) : q i ≠ r j := by
    intro eq
    exact Finset.disjoint_left.mp bc (qb i) (eq.symm ▸ rc j)
  let f : Fin 6 → V := Fin.append p (Fin.append q r)
  have finj : Function.Injective f := by
    apply Fin.append_injective_iff.mpr
    refine ⟨pinj,Fin.append_injective_iff.mpr ⟨qinj,rinj,qr⟩,?_⟩
    intro i j
    fin_cases j <;> first | exact pq i _ | exact pr i _
  refine ⟨f,finj,?_,?_,e,he,?_⟩
  · intro i
    fin_cases i <;> first
      | exact degrees _ (Finset.mem_union_left _ (Finset.mem_union_left _ (pa _)))
      | exact degrees _ (Finset.mem_union_left _ (Finset.mem_union_right _ (qb _)))
      | exact degrees _ (Finset.mem_union_right _ (rc _))
  · have pp := aa _ (pa 0) _ (pa 1) (fun h => by have := pinj h; contradiction)
    have qq := bb _ (qb 0) _ (qb 1) (fun h => by have := qinj h; contradiction)
    have rr := cc _ (rc 0) _ (rc 1) (fun h => by have := rinj h; contradiction)
    intro i j hij
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;> norm_num <;>
      first | exact pp | exact qq | exact rr |
        exact crossAB _ (pa _) _ (qb _) | exact crossAC _ (pa _) _ (rc _) |
        exact crossBC _ (qb _) _ (rc _)
  · have subP : P ⊆ Finset.univ.image f := by
      rw [← indexed_image_eq P p pinj pmem Pcard]
      intro x hx
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
      exact Finset.mem_image.mpr ⟨Fin.castAdd 4 i,Finset.mem_univ _,by simp [f]⟩
    have subQ : Q ⊆ Finset.univ.image f := by
      rw [← indexed_image_eq Q q qinj qmem Qcard]
      intro x hx
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
      exact Finset.mem_image.mpr ⟨Fin.natAdd 2 (Fin.castAdd 2 i),Finset.mem_univ _,by simp [f]⟩
    have subR : R ⊆ Finset.univ.image f := by
      rw [← indexed_image_eq R r rinj rmem Rcard]
      intro x hx
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
      exact Finset.mem_image.mpr ⟨Fin.natAdd 2 (Fin.natAdd 2 i),Finset.mem_univ _,by
        fin_cases i <;> rfl⟩
    have ePQ : Disjoint (e ∩ P) (e ∩ Q) := ab.mono
      (Finset.inter_subset_right.trans PA) (Finset.inter_subset_right.trans QB)
    have ePR : Disjoint (e ∩ P) (e ∩ R) := ac.mono
      (Finset.inter_subset_right.trans PA) (Finset.inter_subset_right.trans RC)
    have eQR : Disjoint (e ∩ Q) (e ∩ R) := bc.mono
      (Finset.inter_subset_right.trans QB) (Finset.inter_subset_right.trans RC)
    have sub : (e ∩ P) ∪ (e ∩ Q) ∪ (e ∩ R) ⊆ e ∩ Finset.univ.image f := by
      apply Finset.union_subset
      · apply Finset.union_subset
        · exact Finset.inter_subset_inter_left subP
        · exact Finset.inter_subset_inter_left subQ
      · exact Finset.inter_subset_inter_left subR
    have count := Finset.card_le_card sub
    rw [Finset.card_union_of_disjoint (Finset.disjoint_union_left.mpr ⟨ePR,eQR⟩),
      Finset.card_union_of_disjoint ePQ] at count
    omega

theorem five_of_many_clusters (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (S : Finset V) (many : 19 ≤ S.card)
    (degrees : ∀ x ∈ S, H.degree x = 7)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1)
    (parts : 4 ≤ (clusters H S).card) : FiveCase H := by
  have facts {A : Finset V} (hA : A ∈ clusters H S) :=
    clusters_facts H cover vertices S degrees range noPath hA
  have disj {A B : Finset V} (hA : A ∈ clusters H S) (hB : B ∈ clusters H S)
      (ne : A ≠ B) := clusters_disjoint H S range noPath hA hB ne
  by_cases large : ∃ A ∈ clusters H S, 2 ≤ A.card
  · obtain ⟨A,hA,big⟩ := large
    have other : 3 ≤ ((clusters H S).erase A).card := by
      rw [Finset.card_erase_of_mem hA]
      omega
    obtain ⟨Cs,Cinj,Cmem⟩ := exists_indexed_subset ((clusters H S).erase A) other
    have cmem (i : Fin 3) := (Finset.mem_erase.mp (Cmem i)).2
    have cne (i : Fin 3) := (Finset.mem_erase.mp (Cmem i)).1
    have pick (i : Fin 3) : ∃ x, x ∈ Cs i := (facts (cmem i)).1
    choose p pmem using pick
    obtain ⟨q,qinj,qmem⟩ := exists_indexed_subset A big
    have qp (i : Fin 2) (j : Fin 3) : q i ≠ p j := by
      intro eq
      exact Finset.disjoint_left.mp (disj hA (cmem j) (Ne.symm (cne j)))
        (qmem i) (eq.symm ▸ pmem j)
    have pinj : Function.Injective p := by
      intro i j eq
      by_contra ne
      exact Finset.disjoint_left.mp (disj (cmem i) (cmem j) (fun h => ne (Cinj h)))
        (pmem i) (eq.symm ▸ pmem j)
    have unitQP (i : Fin 2) (j : Fin 3) : H.codegree (q i) (p j) = 1 := by
      apply (facts hA).2.2.2.2 (q i) (qmem i) (p j) ((facts (cmem j)).2.1 (pmem j))
      intro hi
      exact Finset.disjoint_left.mp (disj hA (cmem j) (Ne.symm (cne j))) hi (pmem j)
    have unitPP (i j : Fin 3) (ne : i ≠ j) : H.codegree (p i) (p j) = 1 := by
      apply (facts (cmem i)).2.2.2.2 (p i) (pmem i) (p j) ((facts (cmem j)).2.1 (pmem j))
      intro hi
      exact Finset.disjoint_left.mp (disj (cmem i) (cmem j) (fun h => ne (Cinj h))) hi (pmem j)
    let f : Fin 5 → V := Fin.append q p
    refine ⟨f,Fin.append_injective_iff.mpr ⟨qinj,pinj,qp⟩,?_,?_,?_⟩
    · intro i
      fin_cases i <;> first
        | exact degrees _ ((facts hA).2.1 (qmem _))
        | exact degrees _ ((facts (cmem _)).2.1 (pmem _))
    · exact (range _ ((facts hA).2.1 (qmem 0)) _ ((facts hA).2.1 (qmem 1))
        (fun h => by have := qinj h; contradiction)).2
    · intro i j hij h01
      fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;>
        simp [Fin.ext_iff] at h01 <;> first
        | exact unitQP _ _
        | exact unitPP _ _ (by decide)
  · have singleton (A : Finset V) (hA : A ∈ clusters H S) : A.card ≤ 1 := by
      have : ¬2 ≤ A.card := fun h => large ⟨A,hA,h⟩
      omega
    have unit (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (ne : x ≠ y) :
        H.codegree x y = 1 := by
      let A := cluster H S x
      have hA : A ∈ clusters H S := Finset.mem_image.mpr ⟨x,hx,rfl⟩
      have xA : x ∈ A := Finset.mem_insert_self _ _
      apply (facts hA).2.2.2.2 x xA y hy
      intro yA
      have lower : 2 ≤ A.card := Finset.one_lt_card.mpr ⟨x,xA,y,yA,ne⟩
      have upper := singleton A hA
      omega
    obtain ⟨f,inj,inside⟩ := exists_indexed_subset S (show 5 ≤ S.card by omega)
    refine ⟨f,inj,fun i => degrees _ (inside i),?_,?_⟩
    · rw [unit _ (inside 0) _ (inside 1) (fun h => by have := inj h; contradiction)]
      omega
    · intro i j hij _
      exact unit _ (inside i) _ (inside j) (fun h => (ne_of_lt hij) (inj h))

/-- The remaining cluster branch produces actual five locks, or actual six
locks whose three double pairs form a matching and which meet an edge at least
four times. No desired lock configuration is assumed. -/
theorem cluster_selection (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (S : Finset V) (many : 19 ≤ S.card)
    (degrees : ∀ x ∈ S, H.degree x = 7)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1) :
    FiveCase H ∨ SixCase H := by
  by_cases parts : 4 ≤ (clusters H S).card
  · exact Or.inl (five_of_many_clusters H cover vertices S many degrees range noPath parts)
  · have facts {A : Finset V} (hA : A ∈ clusters H S) :=
      clusters_facts H cover vertices S degrees range noPath hA
    have size : S.card ≤ 7*(clusters H S).card := by
      calc
        S.card = ((clusters H S).biUnion id).card := by rw [clusters_cover]
        _ ≤ ∑ A ∈ clusters H S, A.card := Finset.card_biUnion_le
        _ ≤ ∑ _A ∈ clusters H S, 7 := Finset.sum_le_sum (fun A hA => (facts hA).2.2.1)
        _ = _ := by simp [Nat.mul_comm]
    have card : (clusters H S).card = 3 := by omega
    let equiv : ↥(clusters H S) ≃ Fin 3 := Fintype.equivFinOfCardEq (by simpa using card)
    let C : Fin 3 → Finset V := fun i => (equiv.symm i).val
    have mem (i : Fin 3) : C i ∈ clusters H S := (equiv.symm i).property
    have inj : Function.Injective C := Subtype.val_injective.comp equiv.symm.injective
    have onto (A : Finset V) (hA : A ∈ clusters H S) : ∃ i, C i = A := by
      refine ⟨equiv ⟨A,hA⟩,?_⟩
      simp [C]
    have union : C 0 ∪ C 1 ∪ C 2 = S := by
      ext x
      constructor
      · intro hx
        rcases Finset.mem_union.mp hx with hx | hx
        · rcases Finset.mem_union.mp hx with hx | hx
          · exact (facts (mem 0)).2.1 hx
          · exact (facts (mem 1)).2.1 hx
        · exact (facts (mem 2)).2.1 hx
      · intro hx
        have hxu : x ∈ (clusters H S).biUnion id := by rw [clusters_cover]; exact hx
        obtain ⟨A,hA,hxA⟩ := Finset.mem_biUnion.mp hxu
        obtain ⟨i,rfl⟩ := onto A hA
        fin_cases i
        · exact Finset.mem_union_left _ (Finset.mem_union_left _ hxA)
        · exact Finset.mem_union_left _ (Finset.mem_union_right _ hxA)
        · exact Finset.mem_union_right _ hxA
    have disj (i j : Fin 3) (ne : i ≠ j) : Disjoint (C i) (C j) :=
      clusters_disjoint H S range noPath (mem i) (mem j) (fun h => ne (inj h))
    have d01 := disj 0 1 (by decide)
    have d02 := disj 0 2 (by decide)
    have d12 := disj 1 2 (by decide)
    have total : (C 0).card + (C 1).card + (C 2).card = S.card := by
      rw [←union, Finset.card_union_of_disjoint (Finset.disjoint_union_left.mpr ⟨d02,d12⟩),
        Finset.card_union_of_disjoint d01]
    have sizes (i : Fin 3) : 5 ≤ (C i).card ∧ (C i).card ≤ 7 := by
      have h0 := (facts (mem 0)).2.2.1
      have h1 := (facts (mem 1)).2.2.1
      have h2 := (facts (mem 2)).2.2.1
      fin_cases i
      · change 5 ≤ (C 0).card ∧ (C 0).card ≤ 7
        omega
      · change 5 ≤ (C 1).card ∧ (C 1).card ≤ 7
        omega
      · change 5 ≤ (C 2).card ∧ (C 2).card ≤ 7
        omega
    have clique (i : Fin 3) := (facts (mem i)).2.2.2.1
    have cross (i j : Fin 3) (ne : i ≠ j) (x : V) (hx : x ∈ C i)
        (y : V) (hy : y ∈ C j) : H.codegree x y = 1 := by
      apply (facts (mem i)).2.2.2.2 x hx y ((facts (mem j)).2.1 hy)
      intro hi
      exact Finset.disjoint_left.mp (disj i j ne) hi hy
    apply Or.inr
    exact six_of_three_cliques H (C 0) (C 1) (C 2) d01 d02 d12
      (by rw [union]; exact degrees) (clique 0) (clique 1) (clique 2)
      (cross 0 1 (by decide)) (cross 0 2 (by decide)) (cross 1 2 (by decide))
      (sizes 0) (sizes 1) (sizes 2) (by omega)

/-- The r=0 degree count supplies the large seven-degree set automatically.
The high-pair and induced-path exclusions remain explicit graph hypotheses. -/
theorem cluster_selection_of_no_sixes (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (edges : H.edges.card = 33)
    (count : H.sixVertices.card = 0)
    (upper : ∀ x, H.degree x = 7 → ∀ y, H.degree y = 7 → x ≠ y → H.codegree x y ≤ 2)
    (noPath : ∀ x, H.degree x = 7 → ∀ y, H.degree y = 7 → ∀ z, H.degree z = 7 →
      x ≠ y → x ≠ z → y ≠ z → H.codegree x y = 2 → H.codegree x z = 2 →
      H.codegree y z ≠ 1) : FiveCase H ∨ SixCase H := by
  have budget := six_seven_budget H cover edges vertices
  have degree (x : V) (hx : x ∈ sevenVertices H) := (mem_sevenVertices H x).mp hx
  exact cluster_selection H cover vertices (sevenVertices H) (by omega) degree
    (fun x hx y hy ne => ⟨H.one_le_codegree cover ne,upper x (degree x hx) y (degree y hy) ne⟩)
    (fun x hx y hy z hz => noPath x (degree x hx) y (degree y hy) z (degree z hz))

end Aris4Math.ThirtyThree.TwentyThreeClusterSelection
