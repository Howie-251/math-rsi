import Aris4Math.LowDegree
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.IntervalCases

/-! Actual lock selection at 21 vertices and 33 edges.  Degree budgets and
codegree exclusions act on the original hypergraph, without profile hypotheses. -/

namespace Aris4Math.ThirtyThree.TwentyOneStructure

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

def PairCase (H : Simple5Hypergraph V) (x y : V) : Prop :=
  (H.degree x = 5 ∧ 5 ≤ H.degree y ∧ H.degree y ≤ 7 ∧ H.codegree x y = 1) ∨
  (H.degree x = 6 ∧ H.degree y = 6) ∨
  (H.degree x = 6 ∧ H.degree y = 7 ∧ H.codegree x y ≠ 2) ∨
  (H.degree x = 7 ∧ H.degree y = 7 ∧ 3 ≤ H.codegree x y)

def NoTriple (H : Simple5Hypergraph V) (x y z : V) : Prop :=
  ∀ e ∈ H.edges, ¬ (x ∈ e ∧ y ∈ e ∧ z ∈ e)

def TripleCase (H : Simple5Hypergraph V) (x y z : V) : Prop :=
  (H.degree x = 5 ∧ H.degree y = 8 ∧ H.degree z = 8 ∧
    H.codegree x y = 1 ∧ H.codegree x z = 1 ∧ H.codegree y z = 1 ∧ NoTriple H x y z) ∨
  (H.degree x = 6 ∧ H.degree y = 7 ∧ H.degree z = 7 ∧
    H.codegree x y = 2 ∧ H.codegree x z = 2 ∧ H.codegree y z ≤ 2) ∨
  (H.degree x = 6 ∧ H.degree y = 7 ∧ H.degree z = 8 ∧
    H.codegree x y = 2 ∧ H.codegree x z = 1 ∧ H.codegree y z = 1 ∧ NoTriple H x y z) ∨
  (H.degree x = 7 ∧ H.degree y = 7 ∧ H.degree z = 7 ∧
    H.codegree x y ≤ 2 ∧ H.codegree x z ≤ 2 ∧ H.codegree y z ≤ 2)

def Selected (H : Simple5Hypergraph V) : Prop :=
  (∃ x y, x ≠ y ∧ PairCase H x y) ∨
  (∃ x y z, x ≠ y ∧ x ≠ z ∧ y ≠ z ∧ TripleCase H x y z)

theorem degree_budget_one (H : Simple5Hypergraph V) (x : V) (b : ℕ)
    (lower : ∀ z, z ≠ x → b ≤ H.degree z) :
    H.degree x + b * (Fintype.card V - 1) ≤ 5 * H.edges.card := by
  have hl := Finset.sum_le_sum (s := Finset.univ.erase x) (fun z hz =>
    lower z (Finset.mem_erase.mp hz).1)
  have hs := Finset.sum_erase_add (s := Finset.univ) H.degree (Finset.mem_univ x)
  have hc : (Finset.univ.erase x).card = Fintype.card V - 1 := by simp
  simp [hc, Nat.mul_comm] at hl
  rw [H.sum_degrees] at hs
  omega

theorem degree_budget_two (H : Simple5Hypergraph V) (x y : V) (ne : x ≠ y) (b : ℕ)
    (lower : ∀ z, z ≠ x → z ≠ y → b ≤ H.degree z) :
    H.degree x + H.degree y + b * (Fintype.card V - 2) ≤ 5 * H.edges.card := by
  have hy : y ∈ Finset.univ.erase x := by simp [Ne.symm ne]
  have hl := Finset.sum_le_sum (s := (Finset.univ.erase x).erase y) (fun z hz =>
    lower z (Finset.mem_erase.mp (Finset.mem_erase.mp hz).2).1
      (Finset.mem_erase.mp hz).1)
  have hs1 := Finset.sum_erase_add (s := Finset.univ) H.degree (Finset.mem_univ x)
  have hs2 := Finset.sum_erase_add (s := Finset.univ.erase x) H.degree hy
  have hc : ((Finset.univ.erase x).erase y).card = Fintype.card V - 2 := by
    rw [Finset.card_erase_of_mem hy]
    simp [Nat.sub_sub]
  simp [hc, Nat.mul_comm] at hl
  rw [H.sum_degrees] at hs1
  omega

theorem degree_budget_three (H : Simple5Hypergraph V) (x y z : V)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z) (b : ℕ)
    (lower : ∀ w, w ≠ x → w ≠ y → w ≠ z → b ≤ H.degree w) :
    H.degree x + H.degree y + H.degree z + b * (Fintype.card V - 3) ≤
      5 * H.edges.card := by
  have hy : y ∈ Finset.univ.erase x := by simp [Ne.symm xy]
  have hz : z ∈ (Finset.univ.erase x).erase y := by simp [Ne.symm xz, Ne.symm yz]
  have hl := Finset.sum_le_sum (s := ((Finset.univ.erase x).erase y).erase z)
    (fun w hw => lower w
      (Finset.mem_erase.mp (Finset.mem_erase.mp (Finset.mem_erase.mp hw).2).2).1
      (Finset.mem_erase.mp (Finset.mem_erase.mp hw).2).1 (Finset.mem_erase.mp hw).1)
  have hs1 := Finset.sum_erase_add (s := Finset.univ) H.degree (Finset.mem_univ x)
  have hs2 := Finset.sum_erase_add (s := Finset.univ.erase x) H.degree hy
  have hs3 := Finset.sum_erase_add (s := (Finset.univ.erase x).erase y) H.degree hz
  have hc : (((Finset.univ.erase x).erase y).erase z).card = Fintype.card V - 3 := by
    rw [Finset.card_erase_of_mem hz, Finset.card_erase_of_mem hy]
    simp [Nat.sub_sub]
  simp [hc, Nat.mul_comm] at hl
  rw [H.sum_degrees] at hs1
  omega

theorem all_unit_of_degree_five (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 21) (x : V) (dx : H.degree x = 5) :
    ∀ y, x ≠ y → H.codegree x y = 1 := by
  intro y ne
  have hb := H.badPartners_card_le_excess cover x
  rw [vertices, dx] at hb
  have empty : H.badPartners x = ∅ := Finset.card_eq_zero.mp (by omega)
  have good : y ∈ H.goodPartners x := by simp [Simple5Hypergraph.goodPartners, empty, Ne.symm ne]
  exact ((H.mem_goodPartners cover x y).mp good).2

theorem selected_of_degree_five (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 21)
    (minimum : ∀ z, 5 ≤ H.degree z) (x : V) (dx : H.degree x = 5) : Selected H := by
  have unit := all_unit_of_degree_five H cover vertices x dx
  by_cases pair : ∃ y, y ≠ x ∧ H.degree y ≤ 7
  · obtain ⟨y, yx, dy⟩ := pair
    exact Or.inl ⟨x, y, Ne.symm yx, Or.inl ⟨dx, minimum y, dy, unit y (Ne.symm yx)⟩⟩
  have lower (y : V) (yx : y ≠ x) : 8 ≤ H.degree y := by
    have : ¬ H.degree y ≤ 7 := fun h => pair ⟨y,yx,h⟩
    omega
  have exact8 (y : V) (yx : y ≠ x) : H.degree y = 8 := by
    have hb := degree_budget_two H x y (Ne.symm yx) 8 (fun z zx _ => lower z zx)
    rw [edges, vertices, dx] at hb
    have := lower y yx
    omega
  have size : 0 < (Finset.univ.erase x).card := by simp [vertices]
  obtain ⟨y,hy⟩ := Finset.card_pos.mp size
  have yx := (Finset.mem_erase.mp hy).1
  have dy := exact8 y yx
  obtain ⟨e,he,xe,ye⟩ := cover x y (Ne.symm yx)
  have hgood := H.goodPartners_budget cover y
  rw [vertices,dy] at hgood
  have hecard := H.five_uniform e he
  have hdiff := Finset.card_le_card_sdiff_add_card (s := H.goodPartners y) (t := e)
  obtain ⟨z,hz⟩ := Finset.card_pos.mp
    (show 0 < (H.goodPartners y \ e).card by omega)
  obtain ⟨zg,ze⟩ := Finset.mem_sdiff.mp hz
  obtain ⟨zy,cyz⟩ := (H.mem_goodPartners cover y z).mp zg
  have zx : z ≠ x := fun h => ze (h ▸ xe)
  refine Or.inr ⟨x,y,z,Ne.symm yx,Ne.symm zx,Ne.symm zy,Or.inl
    ⟨dx,dy,exact8 z zx,unit y (Ne.symm yx),unit z (Ne.symm zx),cyz,?_⟩⟩
  intro f hf hxyz
  have fe := H.edge_unique_of_codegree_one (unit y (Ne.symm yx)) hf he
    hxyz.1 hxyz.2.1 xe ye
  exact ze (fe ▸ hxyz.2.2)

theorem selected_of_min_seven (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 21)
    (minimum : ∀ z, 7 ≤ H.degree z) : Selected H := by
  let S := Finset.univ.filter fun x => H.degree x = 7
  have size : 3 ≤ S.card := by
    have each (x : V) : 8 ≤ H.degree x + if H.degree x = 7 then 1 else 0 := by
      have := minimum x
      split_ifs <;> omega
    have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
    have hs : 8 * Fintype.card V ≤ 165 + S.card := by
      simpa [Finset.sum_add_distrib, H.sum_degrees, edges, S, Nat.mul_comm] using h
    rw [vertices] at hs
    omega
  by_cases pair : ∃ x ∈ S, ∃ y ∈ S, x ≠ y ∧ 3 ≤ H.codegree x y
  · obtain ⟨x,hx,y,hy,ne,hc⟩ := pair
    exact Or.inl ⟨x,y,ne,Or.inr (Or.inr (Or.inr
      ⟨(Finset.mem_filter.mp hx).2,(Finset.mem_filter.mp hy).2,hc⟩))⟩
  have small (x : V) (hx : x ∈ S) (y : V) (hy : y ∈ S) (ne : x ≠ y) :
      H.codegree x y ≤ 2 := by
    have : ¬ 3 ≤ H.codegree x y := fun h => pair ⟨x,hx,y,hy,ne,h⟩
    omega
  obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
  have size1 : 2 ≤ (S.erase x).card := by rw [Finset.card_erase_of_mem hx]; omega
  obtain ⟨y,hy⟩ := Finset.card_pos.mp (show 0 < (S.erase x).card by omega)
  obtain ⟨yx,hyS⟩ := Finset.mem_erase.mp hy
  have size2 : 1 ≤ ((S.erase x).erase y).card := by
    rw [Finset.card_erase_of_mem hy]; omega
  obtain ⟨z,hz⟩ := Finset.card_pos.mp (by omega : 0 < ((S.erase x).erase y).card)
  obtain ⟨zy,hz1⟩ := Finset.mem_erase.mp hz
  obtain ⟨zx,hzS⟩ := Finset.mem_erase.mp hz1
  exact Or.inr ⟨x,y,z,Ne.symm yx,Ne.symm zx,Ne.symm zy,
    Or.inr (Or.inr (Or.inr ⟨(Finset.mem_filter.mp hx).2,
      (Finset.mem_filter.mp hyS).2,(Finset.mem_filter.mp hzS).2,
      small x hx y hyS (Ne.symm yx),small x hx z hzS (Ne.symm zx),
      small y hyS z hzS (Ne.symm zy)⟩))⟩

/-- Points other than the selected pair that share an edge with both. -/
def pairRemainders (H : Simple5Hypergraph V) (x y : V) : Finset V :=
  (H.edges.filter fun e => x ∈ e ∧ y ∈ e).biUnion fun e => (e.erase x).erase y

theorem pairRemainders_card_le (H : Simple5Hypergraph V) (x y : V) (xy : x ≠ y) :
    (pairRemainders H x y).card ≤ 3 * H.codegree x y := by
  have h := Finset.card_biUnion_le (s := H.edges.filter fun e => x ∈ e ∧ y ∈ e)
    (t := fun e => (e.erase x).erase y)
  have hc (e : Finset V) (he : e ∈ H.edges.filter fun e => x ∈ e ∧ y ∈ e) :
      ((e.erase x).erase y).card = 3 := by
    obtain ⟨he,xe,ye⟩ := Finset.mem_filter.mp he
    rw [Finset.card_erase_of_mem (by simp [ye,Ne.symm xy]),
      Finset.card_erase_of_mem xe, H.five_uniform e he]
  have hs : (∑ e ∈ H.edges.filter (fun e => x ∈ e ∧ y ∈ e), ((e.erase x).erase y).card) =
      3 * H.codegree x y := by
    rw [Finset.sum_congr rfl hc]
    simp [Simple5Hypergraph.codegree, Nat.mul_comm]
  exact h.trans_eq hs

theorem noTriple_of_not_pairRemainders (H : Simple5Hypergraph V) (x y z : V)
    (xz : x ≠ z) (yz : y ≠ z) (absent : z ∉ pairRemainders H x y) : NoTriple H x y z := by
  intro e he xyz
  exact absent (Finset.mem_biUnion.mpr ⟨e,Finset.mem_filter.mpr ⟨he,xyz.1,xyz.2.1⟩,
    by simp [xyz.2.2,Ne.symm xz,Ne.symm yz]⟩)

theorem selected_of_unique_six (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 21)
    (x : V) (dx : H.degree x = 6)
    (other : ∀ y, y ≠ x → 7 ≤ H.degree y) : Selected H := by
  have seven : ∃ y, y ≠ x ∧ H.degree y = 7 := by
    by_contra hn
    have lower (y : V) (yx : y ≠ x) : 8 ≤ H.degree y := by
      have := other y yx
      have : H.degree y ≠ 7 := fun h => hn ⟨y,yx,h⟩
      omega
    have hb := degree_budget_one H x 8 lower
    rw [dx,vertices,edges] at hb
    omega
  by_cases pair : ∃ y, y ≠ x ∧ H.degree y = 7 ∧ H.codegree x y ≠ 2
  · obtain ⟨y,yx,dy,cxy⟩ := pair
    exact Or.inl ⟨x,y,Ne.symm yx,Or.inr (Or.inr (Or.inl ⟨dx,dy,cxy⟩))⟩
  have codeg2 (y : V) (yx : y ≠ x) (dy : H.degree y = 7) : H.codegree x y = 2 := by
    by_contra hn
    exact pair ⟨y,yx,dy,hn⟩
  obtain ⟨y,yx,dy⟩ := seven
  have cxy := codeg2 y yx dy
  by_cases second : ∃ z, z ≠ x ∧ z ≠ y ∧ H.degree z = 7
  · obtain ⟨z,zx,zy,dz⟩ := second
    by_cases high : 3 ≤ H.codegree y z
    · exact Or.inl ⟨y,z,Ne.symm zy,Or.inr (Or.inr (Or.inr ⟨dy,dz,high⟩))⟩
    · exact Or.inr ⟨x,y,z,Ne.symm yx,Ne.symm zx,Ne.symm zy,
        Or.inr (Or.inl ⟨dx,dy,dz,cxy,codeg2 z zx dz,by omega⟩)⟩
  have lower8 (z : V) (zx : z ≠ x) (zy : z ≠ y) : 8 ≤ H.degree z := by
    have := other z zx
    have : H.degree z ≠ 7 := fun h => second ⟨z,zx,zy,h⟩
    omega
  have exact8 (z : V) (zx : z ≠ x) (zy : z ≠ y) : H.degree z = 8 := by
    have hb := degree_budget_three H x y z (Ne.symm yx) (Ne.symm zx) (Ne.symm zy)
      8 (fun w wx wy _ => lower8 w wx wy)
    rw [dx,dy,vertices,edges] at hb
    have := lower8 z zx zy
    omega
  let B := H.badPartners x ∪ pairRemainders H x y
  have bsize : B.card ≤ 10 := by
    have bad := H.badPartners_card_le_excess cover x
    rw [vertices,dx] at bad
    have remainder := pairRemainders_card_le H x y (Ne.symm yx)
    rw [cxy] at remainder
    have hu := Finset.card_union_le (H.badPartners x) (pairRemainders H x y)
    dsimp [B]
    omega
  have good := H.goodPartners_budget cover y
  rw [vertices,dy] at good
  have diff := Finset.card_le_card_sdiff_add_card (s := H.goodPartners y) (t := B)
  obtain ⟨z,hz⟩ := Finset.card_pos.mp (show 0 < (H.goodPartners y \ B).card by omega)
  obtain ⟨zg,zB⟩ := Finset.mem_sdiff.mp hz
  obtain ⟨zy,cyz⟩ := (H.mem_goodPartners cover y z).mp zg
  have zx : z ≠ x := by
    intro heq
    have cyx := H.codegree_comm y x
    rw [heq] at cyz
    omega
  have zbad : z ∉ H.badPartners x := fun h => zB (Finset.mem_union_left _ h)
  have zgood : z ∈ H.goodPartners x := by
    simp only [Simple5Hypergraph.goodPartners, Finset.mem_sdiff, Finset.mem_univ,
      true_and, Finset.mem_insert, not_or]
    exact ⟨zx,zbad⟩
  have cxz := ((H.mem_goodPartners cover x z).mp zgood).2
  have zrem : z ∉ pairRemainders H x y := fun h => zB (Finset.mem_union_right _ h)
  exact Or.inr ⟨x,y,z,Ne.symm yx,Ne.symm zx,Ne.symm zy,
    Or.inr (Or.inr (Or.inl ⟨dx,dy,exact8 z zx zy,cxy,cxz,cyz,
      noTriple_of_not_pairRemainders H x y z (Ne.symm zx) (Ne.symm zy) zrem⟩))⟩

theorem exists_locks_of_twenty_one (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 21) : Selected H := by
  have minimum (x : V) : 5 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices] at h
    omega
  by_cases five : ∃ x, H.degree x = 5
  · obtain ⟨x,dx⟩ := five
    exact selected_of_degree_five H cover edges vertices minimum x dx
  have min6 (x : V) : 6 ≤ H.degree x := by
    have := minimum x
    have : H.degree x ≠ 5 := fun h => five ⟨x,h⟩
    omega
  by_cases six : ∃ x, H.degree x = 6
  · obtain ⟨x,dx⟩ := six
    by_cases another : ∃ y, y ≠ x ∧ H.degree y = 6
    · obtain ⟨y,yx,dy⟩ := another
      exact Or.inl ⟨x,y,Ne.symm yx,Or.inr (Or.inl ⟨dx,dy⟩)⟩
    have other (y : V) (yx : y ≠ x) : 7 ≤ H.degree y := by
      have := min6 y
      have : H.degree y ≠ 6 := fun h => another ⟨y,yx,h⟩
      omega
    exact selected_of_unique_six H cover edges vertices x dx other
  have min7 (x : V) : 7 ≤ H.degree x := by
    have := min6 x
    have : H.degree x ≠ 6 := fun h => six ⟨x,h⟩
    omega
  exact selected_of_min_seven H cover edges vertices min7

end Aris4Math.ThirtyThree.TwentyOneStructure

#print axioms Aris4Math.ThirtyThree.TwentyOneStructure.exists_locks_of_twenty_one

