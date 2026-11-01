import Aris4Math.ThirtyThree.TwentyTwoStructure
import Mathlib.Data.Finset.Card

/-! Complete actual lock selection on 22 vertices. The codegree-two relation
is handled directly on the finite seven-degree set, without a graph encoding. -/
namespace Aris4Math.ThirtyThree.TwentyTwoSelection

open scoped BigOperators
variable {V : Type*} [Fintype V] [DecidableEq V]

def PairCase (H : Simple5Hypergraph V) (x y : V) : Prop :=
  (H.degree x = 6 ∧ (H.degree y = 6 ∨ H.degree y = 7) ∧ H.codegree x y = 1) ∨
  (H.degree x = 7 ∧ H.degree y = 7 ∧ 3 ≤ H.codegree x y)

def TripleCase (H : Simple5Hypergraph V) (x y z : V) : Prop :=
  H.degree x = 7 ∧ H.degree y = 7 ∧ H.degree z = 7 ∧
  H.codegree x y = 2 ∧ H.codegree x z = 2 ∧ H.codegree y z = 1

def QuadCase (H : Simple5Hypergraph V) (x y z w : V) : Prop :=
  H.degree x = 7 ∧ H.degree y = 7 ∧ H.degree z = 7 ∧ H.degree w = 7 ∧
  ((H.codegree x y = 2 ∧ H.codegree x z = 2 ∧ H.codegree y z = 2 ∧
    H.codegree x w = 1 ∧ H.codegree y w = 1 ∧ H.codegree z w = 1) ∨
   (H.codegree x y = 2 ∧ H.codegree x z = 1 ∧ H.codegree x w = 1 ∧
    H.codegree y z = 1 ∧ H.codegree y w = 1 ∧ H.codegree z w = 1) ∨
   (H.codegree x y = 1 ∧ H.codegree x z = 1 ∧ H.codegree x w = 1 ∧
    H.codegree y z = 1 ∧ H.codegree y w = 1 ∧ H.codegree z w = 1 ∧
    ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e ∧ z ∈ e))

def Selected (H : Simple5Hypergraph V) : Prop :=
  (∃ x y, x ≠ y ∧ PairCase H x y) ∨
  (∃ x y z, x ≠ y ∧ x ≠ z ∧ y ≠ z ∧ TripleCase H x y z) ∨
  (∃ x y z w, x ≠ y ∧ x ≠ z ∧ x ≠ w ∧ y ≠ z ∧ y ≠ w ∧ z ≠ w ∧
    QuadCase H x y z w)

/-- The neighborhood of a, together with a itself. -/
def cluster (H : Simple5Hypergraph V) (S : Finset V) (a : V) : Finset V :=
  insert a (S.filter fun z => z ≠ a ∧ H.codegree a z = 2)

theorem cluster_subset (H : Simple5Hypergraph V) (S : Finset V) (a : V) (ha : a ∈ S) :
    cluster H S a ⊆ S := by
  intro z hz
  rcases Finset.mem_insert.mp hz with rfl | hz
  · exact ha
  · exact (Finset.mem_filter.mp hz).1

theorem cluster_card_le_eight (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 22) (S : Finset V) (a : V) (da : H.degree a = 7) :
    (cluster H S a).card ≤ 8 := by
  have sub : cluster H S a ⊆ insert a (H.badPartners a) := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact Finset.mem_insert_self _ _
    · obtain ⟨_,za,az⟩ := Finset.mem_filter.mp hz
      apply Finset.mem_insert_of_mem
      exact Finset.mem_filter.mpr ⟨by simp [za],by omega⟩
  have hs := Finset.card_le_card sub
  have hi := Finset.card_insert_le a (H.badPartners a)
  have hb := H.badPartners_card_le_excess cover a
  rw [vertices,da] at hb
  omega

/-- Without an induced three-point path, the closed neighborhood is a clique
and every codegree to its complement in S equals one. -/
theorem cluster_relations (H : Simple5Hypergraph V) (S : Finset V) (a : V)
    (ha : a ∈ S)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1) :
    (∀ x ∈ cluster H S a, ∀ y ∈ cluster H S a, x ≠ y → H.codegree x y = 2) ∧
    (∀ x ∈ cluster H S a, ∀ y ∈ S, y ∉ cluster H S a → H.codegree x y = 1) := by
  have trans (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (z : V) (hz : z ∈ S)
      (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
      (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 2) : H.codegree y z = 2 := by
    have hr := range y hy z hz yz
    have hn := noPath x hx y hy z hz xy xz yz cxy cxz
    omega
  have aself : a ∈ cluster H S a := Finset.mem_insert_self _ _
  have csub := cluster_subset H S a ha
  constructor
  · intro x hx y hy xy
    rcases Finset.mem_insert.mp hx with rfl | hx
    · obtain ⟨_,_,cy⟩ := Finset.mem_filter.mp (Finset.mem_insert.mp hy |>.resolve_left (Ne.symm xy))
      exact cy
    · obtain ⟨hxS,xa,cax⟩ := Finset.mem_filter.mp hx
      rcases Finset.mem_insert.mp hy with rfl | hy
      · exact (H.codegree_comm x _).trans cax
      · obtain ⟨hyS,ya,cay⟩ := Finset.mem_filter.mp hy
        exact trans a ha x hxS y hyS (Ne.symm xa) (Ne.symm ya) xy cax cay
  · intro x hx y hy hyout
    have ya : y ≠ a := fun h => hyout (h ▸ aself)
    have cay_ne : H.codegree a y ≠ 2 := fun h => hyout
      (Finset.mem_insert_of_mem (Finset.mem_filter.mpr ⟨hy,ya,h⟩))
    have cay : H.codegree a y = 1 := by
      have hr := range a ha y hy (Ne.symm ya)
      omega
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact cay
    · obtain ⟨hxS,xa,cax⟩ := Finset.mem_filter.mp hx
      have xy : x ≠ y := fun h => hyout (h ▸ Finset.mem_insert_of_mem
        (Finset.mem_filter.mpr ⟨hxS,xa,cax⟩))
      have hr := range x hxS y hy xy
      by_contra hn
      have cxy : H.codegree x y = 2 := by omega
      have cxa := (H.codegree_comm x _).trans cax
      have two := trans x hxS a ha y hy xa xy (Ne.symm ya) cxa cxy
      omega

theorem selected_of_cluster_edge (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 22) (S : Finset V) (many : 11 ≤ S.card)
    (degrees : ∀ x ∈ S, H.degree x = 7)
    (range : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → 1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2)
    (noPath : ∀ x ∈ S, ∀ y ∈ S, ∀ z ∈ S, x ≠ y → x ≠ z → y ≠ z →
      H.codegree x y = 2 → H.codegree x z = 2 → H.codegree y z ≠ 1)
    (a : V) (ha : a ∈ S) (b : V) (hb : b ∈ S) (ab : a ≠ b)
    (cab : H.codegree a b = 2) : Selected H := by
  let C := cluster H S a
  have aC : a ∈ C := Finset.mem_insert_self _ _
  have bC : b ∈ C := Finset.mem_insert_of_mem (Finset.mem_filter.mpr ⟨hb,Ne.symm ab,cab⟩)
  have Csub : C ⊆ S := cluster_subset H S a ha
  have Csize : C.card ≤ 8 := cluster_card_le_eight H cover vertices S a (degrees a ha)
  obtain ⟨clique,cross⟩ := cluster_relations H S a ha range noPath
  change (∀ x ∈ C, ∀ y ∈ C, x ≠ y → H.codegree x y = 2) at clique
  change (∀ x ∈ C, ∀ y ∈ S, y ∉ C → H.codegree x y = 1) at cross
  have distinct (x : V) (hx : x ∈ C) (y : V) (hy : y ∉ C) : x ≠ y := by
    intro h
    exact hy (h ▸ hx)
  by_cases big : 3 ≤ C.card
  · have bErase : b ∈ C.erase a := Finset.mem_erase.mpr ⟨Ne.symm ab,bC⟩
    have csize : 0 < ((C.erase a).erase b).card := by
      rw [Finset.card_erase_of_mem bErase,Finset.card_erase_of_mem aC]
      omega
    obtain ⟨c,hc⟩ := Finset.card_pos.mp csize
    obtain ⟨cb,hc1⟩ := Finset.mem_erase.mp hc
    obtain ⟨ca,cC⟩ := Finset.mem_erase.mp hc1
    have osize := Finset.card_le_card_sdiff_add_card (s := S) (t := C)
    obtain ⟨d,hd⟩ := Finset.card_pos.mp (show 0 < (S \ C).card by omega)
    obtain ⟨dS,dC⟩ := Finset.mem_sdiff.mp hd
    refine Or.inr (Or.inr ⟨a,b,c,d,ab,Ne.symm ca,distinct a aC d dC,
      Ne.symm cb,distinct b bC d dC,distinct c cC d dC,
      degrees a ha,degrees b hb,degrees c (Csub cC),degrees d dS,Or.inl ?_⟩)
    exact ⟨cab,clique a aC c cC (Ne.symm ca),clique b bC c cC (Ne.symm cb),
      cross a aC d dS dC,cross b bC d dS dC,cross c cC d dS dC⟩
  · let O := S \ C
    have osize : 9 ≤ O.card := by
      have h := Finset.card_le_card_sdiff_add_card (s := S) (t := C)
      dsimp [O]
      omega
    obtain ⟨c,hc⟩ := Finset.card_pos.mp (show 0 < O.card by omega)
    obtain ⟨cS,cC⟩ := Finset.mem_sdiff.mp hc
    let B := insert c (H.badPartners c)
    have bsize : B.card ≤ 8 := by
      have hbad := H.badPartners_card_le_excess cover c
      rw [vertices,degrees c cS] at hbad
      have hi := Finset.card_insert_le c (H.badPartners c)
      dsimp [B]
      omega
    have dsize := Finset.card_le_card_sdiff_add_card (s := O) (t := B)
    obtain ⟨d,hd⟩ := Finset.card_pos.mp (show 0 < (O \ B).card by omega)
    obtain ⟨dO,dB⟩ := Finset.mem_sdiff.mp hd
    obtain ⟨dS,dC⟩ := Finset.mem_sdiff.mp dO
    have good : d ∈ H.goodPartners c := Finset.mem_sdiff.mpr ⟨Finset.mem_univ d,dB⟩
    obtain ⟨dc,ccd⟩ := (H.mem_goodPartners cover c d).mp good
    refine Or.inr (Or.inr ⟨a,b,c,d,ab,distinct a aC c cC,distinct a aC d dC,
      distinct b bC c cC,distinct b bC d dC,Ne.symm dc,
      degrees a ha,degrees b hb,degrees c cS,degrees d dS,Or.inr (Or.inl ?_)⟩)
    exact ⟨cab,cross a aC c cS cC,cross a aC d dS dC,
      cross b bC c cS cC,cross b bC d dS dC,ccd⟩

theorem selected_of_unit_sevens (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (S : Finset V) (many : 11 ≤ S.card) (degrees : ∀ x ∈ S, H.degree x = 7)
    (unit : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → H.codegree x y = 1) : Selected H := by
  obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
  let I := H.edges.filter fun e => x ∈ e
  have icard : I.card = 7 := degrees x hx
  have large : ∃ e ∈ I, 3 ≤ (e ∩ S).card := by
    by_contra hn
    have small (e : Finset V) (he : e ∈ I) : ((e ∩ S).erase x).card ≤ 1 := by
      have xe : x ∈ e := (Finset.mem_filter.mp he).2
      have inS : x ∈ e ∩ S := Finset.mem_inter.mpr ⟨xe,hx⟩
      have : ¬ 3 ≤ (e ∩ S).card := fun h => hn ⟨e,he,h⟩
      rw [Finset.card_erase_of_mem inS]
      omega
    have covered : S.erase x ⊆ I.biUnion (fun e => (e ∩ S).erase x) := by
      intro y hy
      obtain ⟨yx,hyS⟩ := Finset.mem_erase.mp hy
      obtain ⟨e,he,xe,ye⟩ := cover x y (Ne.symm yx)
      exact Finset.mem_biUnion.mpr ⟨e,Finset.mem_filter.mpr ⟨he,xe⟩,
        Finset.mem_erase.mpr ⟨yx,Finset.mem_inter.mpr ⟨ye,hyS⟩⟩⟩
    have h1 := Finset.card_le_card covered
    have h2 := Finset.card_biUnion_le (s := I) (t := fun e => (e ∩ S).erase x)
    have h3 := Finset.sum_le_sum (s := I) small
    have h4 : (∑ e ∈ I, (1 : ℕ)) = 7 := by simp [icard]
    rw [h4] at h3
    rw [Finset.card_erase_of_mem hx] at h1
    omega
  obtain ⟨e,he,three⟩ := large
  obtain ⟨heH,xe⟩ := Finset.mem_filter.mp he
  have hxT : x ∈ e ∩ S := Finset.mem_inter.mpr ⟨xe,hx⟩
  have size : 1 < ((e ∩ S).erase x).card := by
    rw [Finset.card_erase_of_mem hxT]
    omega
  obtain ⟨y,hy,z,hz,yz⟩ := Finset.one_lt_card.mp size
  obtain ⟨yx,hyT⟩ := Finset.mem_erase.mp hy
  obtain ⟨zx,hzT⟩ := Finset.mem_erase.mp hz
  obtain ⟨ye,hyS⟩ := Finset.mem_inter.mp hyT
  obtain ⟨ze,hzS⟩ := Finset.mem_inter.mp hzT
  have bcard : ({x,y,z} : Finset V).card = 3 := by simp [Ne.symm yx,Ne.symm zx,yz]
  have hdiff := Finset.card_le_card_sdiff_add_card (s := S) (t := {x,y,z})
  obtain ⟨w,hw⟩ := Finset.card_pos.mp (show 0 < (S \ {x,y,z}).card by omega)
  obtain ⟨hwS,hwB⟩ := Finset.mem_sdiff.mp hw
  have wx : w ≠ x := fun h => hwB (by simp [h])
  have wy : w ≠ y := fun h => hwB (by simp [h])
  have wz : w ≠ z := fun h => hwB (by simp [h])
  refine Or.inr (Or.inr ⟨x,y,z,w,Ne.symm yx,Ne.symm zx,Ne.symm wx,yz,Ne.symm wy,Ne.symm wz,
    degrees x hx,degrees y hyS,degrees z hzS,degrees w hwS,Or.inr (Or.inr ?_)⟩)
  exact ⟨unit x hx y hyS (Ne.symm yx),unit x hx z hzS (Ne.symm zx),unit x hx w hwS (Ne.symm wx),
    unit y hyS z hzS yz,unit y hyS w hwS (Ne.symm wy),unit z hzS w hwS (Ne.symm wz),e,heH,xe,ye,ze⟩

theorem selected_of_min_seven (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 22)
    (minimum : ∀ x, 7 ≤ H.degree x) : Selected H := by
  let S := Finset.univ.filter fun x => H.degree x = 7
  have degrees (x : V) (hx : x ∈ S) : H.degree x = 7 := (Finset.mem_filter.mp hx).2
  have many : 11 ≤ S.card := by
    have each (x : V) : 8 ≤ H.degree x + if H.degree x = 7 then 1 else 0 := by
      have := minimum x
      split_ifs <;> omega
    have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
    have hs : 8 * Fintype.card V ≤ 165 + S.card := by
      simpa [Finset.sum_add_distrib, H.sum_degrees, edges, S, Nat.mul_comm] using h
    rw [vertices] at hs
    omega
  by_cases high : ∃ x ∈ S, ∃ y ∈ S, x ≠ y ∧ 3 ≤ H.codegree x y
  · obtain ⟨x,hx,y,hy,ne,hc⟩ := high
    exact Or.inl ⟨x,y,ne,Or.inr ⟨degrees x hx,degrees y hy,hc⟩⟩
  have range (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (xy : x ≠ y) :
      1 ≤ H.codegree x y ∧ H.codegree x y ≤ 2 := by
    have lo := H.one_le_codegree cover xy
    have no : ¬ 3 ≤ H.codegree x y := fun h => high ⟨x,hx,y,hy,xy,h⟩
    omega
  by_cases path : ∃ x ∈ S, ∃ y ∈ S, ∃ z ∈ S, x ≠ y ∧ x ≠ z ∧ y ≠ z ∧
      H.codegree x y = 2 ∧ H.codegree x z = 2 ∧ H.codegree y z = 1
  · obtain ⟨x,hx,y,hy,z,hz,xy,xz,yz,cxy,cxz,cyz⟩ := path
    exact Or.inr (Or.inl ⟨x,y,z,xy,xz,yz,degrees x hx,degrees y hy,degrees z hz,cxy,cxz,cyz⟩)
  have noPath (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (z : V) (hz : z ∈ S)
      (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
      (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 2) : H.codegree y z ≠ 1 := by
    intro cyz
    exact path ⟨x,hx,y,hy,z,hz,xy,xz,yz,cxy,cxz,cyz⟩
  by_cases edge : ∃ a ∈ S, ∃ b ∈ S, a ≠ b ∧ H.codegree a b = 2
  · obtain ⟨a,ha,b,hb,ab,cab⟩ := edge
    exact selected_of_cluster_edge H cover vertices S many degrees range noPath a ha b hb ab cab
  have unit (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (xy : x ≠ y) : H.codegree x y = 1 := by
    have hr := range x hx y hy xy
    have no : H.codegree x y ≠ 2 := fun h => edge ⟨x,hx,y,hy,xy,h⟩
    omega
  exact selected_of_unit_sevens H cover S many degrees unit

/-- All actual 22-vertex pair-covering 33-edge inputs admit one of the complete
low-pair, high-pair, induced-path, or three specified four-lock configurations. -/
theorem exists_locks_of_twenty_two (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 22) : Selected H := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices] at h
    omega
  by_cases six : ∃ x, H.degree x = 6
  · obtain ⟨x,dx⟩ := six
    have good := H.goodPartners_budget cover x
    rw [vertices,dx] at good
    have partner : ∃ y ∈ H.goodPartners x, H.degree y ≤ 7 := by
      by_contra hn
      have high (y : V) (hy : y ∈ H.goodPartners x) : 6 + 2 ≤ H.degree y := by
        have no : ¬ H.degree y ≤ 7 := fun h => hn ⟨y,hy,h⟩
        omega
      have budget := H.subset_degree_budget (H.goodPartners x) 6 2 minimum high
      rw [vertices,edges] at budget
      omega
    obtain ⟨y,hy,dy⟩ := partner
    obtain ⟨yx,cxy⟩ := (H.mem_goodPartners cover x y).mp hy
    have lower := minimum y
    exact Or.inl ⟨x,y,Ne.symm yx,Or.inl ⟨dx,by omega,cxy⟩⟩
  have min7 (x : V) : 7 ≤ H.degree x := by
    have := minimum x
    have no : H.degree x ≠ 6 := fun h => six ⟨x,h⟩
    omega
  exact selected_of_min_seven H cover edges vertices min7

end Aris4Math.ThirtyThree.TwentyTwoSelection

#print axioms Aris4Math.ThirtyThree.TwentyTwoSelection.exists_locks_of_twenty_two

