import Aris4Math.LowDegree
import Aris4Math.ThirtyThree.TripleProfiles

/-! The actual unit-codegree graph at 21 vertices. Local classification
consequences imply a graph contradiction; no graph enumeration is used. -/

namespace Aris4Math.ThirtyFour.TwentyOneEightGraph

open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)

def Unit (H : Simple5Hypergraph (Fin 21)) (x y : Fin 21) : Prop :=
  x ≠ y ∧ H.codegree x y=1

instance (H : Simple5Hypergraph (Fin 21)) : DecidableRel (Unit H) :=
  fun x y => by unfold Unit; infer_instance

theorem unit_symm (H : Simple5Hypergraph (Fin 21)) : Symmetric (Unit H) := by
  intro x y h
  exact ⟨h.1.symm,by rw [H.codegree_comm]; exact h.2⟩

theorem unit_irrefl (H : Simple5Hypergraph (Fin 21)) : Irreflexive (Unit H) :=
  fun x h => h.1 rfl

def neighbors (H : Simple5Hypergraph (Fin 21)) (L : Finset (Fin 21))
    (x : Fin 21) : Finset (Fin 21) := L.filter (Unit H x)

/-- Four local consequences to be supplied by the actual triple, quadruple,
and claw-extension classifications. Cycle and claw fields concern real edges. -/
structure Rules (H : Simple5Hypergraph (Fin 21)) (L : Finset (Fin 21)) : Prop where
  triangle : ∀ x ∈ L, ∀ a ∈ L, ∀ b ∈ L,
    Unit H x a → Unit H x b → ¬ Unit H a b
  pathIsolate : ∀ x ∈ L, ∀ a ∈ L, ∀ b ∈ L, ∀ z ∈ L,
    a ≠ b → x ≠ z → a ≠ z → b ≠ z →
    Unit H x a → Unit H x b → ¬ Unit H x z → ¬ Unit H a z → ¬ Unit H b z → False
  cycle : ∀ x ∈ L, ∀ z ∈ L, ∀ a ∈ L, ∀ b ∈ L,
    x ≠ z → a ≠ b → Unit H x a → Unit H x b → Unit H z a → Unit H z b →
    ¬ Unit H x z → ¬ Unit H a b →
    ∃ e ∈ H.edges, x ∈ e ∧ z ∈ e ∧ a ∈ e ∧ b ∈ e
  claw : ∀ x ∈ L, ∀ a ∈ L, ∀ b ∈ L, ∀ c ∈ L,
    a ≠ b → a ≠ c → b ≠ c →
    Unit H x a → Unit H x b → Unit H x c →
    ¬ Unit H a b → ¬ Unit H a c → ¬ Unit H b c →
    ∀ e ∈ H.edges, x ∈ e → a ∈ e → b ∈ e → c ∈ e → False

/-- The two actual C4 edges agree on a unit pair, producing a forbidden
common edge on the claw. Hence there cannot be three common neighbors. -/
theorem no_three_common_neighbors (H : Simple5Hypergraph (Fin 21))
    (L : Finset (Fin 21)) (rules : Rules H L)
    (x z a b c : Fin 21) (hx : x ∈ L) (hz : z ∈ L)
    (ha : a ∈ L) (hb : b ∈ L) (hc : c ∈ L)
    (xz : x ≠ z) (ab : a ≠ b) (ac : a ≠ c) (bc : b ≠ c)
    (xa : Unit H x a) (xb : Unit H x b) (xc : Unit H x c)
    (za : Unit H z a) (zb : Unit H z b) (zc : Unit H z c) : False := by
  have nxz := rules.triangle a ha x hx z hz (unit_symm H xa) (unit_symm H za)
  have nab := rules.triangle x hx a ha b hb xa xb
  have nac := rules.triangle x hx a ha c hc xa xc
  have nbc := rules.triangle x hx b hb c hc xb xc
  obtain ⟨e,he,xe,ze,ae,be⟩ := rules.cycle x hx z hz a ha b hb xz ab xa xb za zb nxz nab
  obtain ⟨f,hf,xf,zf,af,cf⟩ := rules.cycle x hx z hz a ha c hc xz ac xa xc za zc nxz nac
  have eq := H.edge_unique_of_codegree_one xa.2 hf he xf af xe ae
  have ce : c ∈ e := eq ▸ cf
  exact rules.claw x hx a ha b hb c hc ab ac bc xa xb xc nab nac nbc e he xe ae be ce

/-- Three neighbors already suffice for universality once the path-isolate
and three-common-neighbor configurations are excluded. -/
theorem universal_of_three (H : Simple5Hypergraph (Fin 21))
    (L : Finset (Fin 21)) (rules : Rules H L) (x : Fin 21) (hx : x ∈ L)
    (large : 3 ≤ (neighbors H L x).card) :
    ∀ z ∈ L, x ≠ z → Unit H x z := by
  obtain ⟨a,b,c,ha,hb,hc,ab,ac,bc⟩ :=
    Finset.two_lt_card_iff.mp (show 2 < (neighbors H L x).card by omega)
  obtain ⟨ha,xa⟩ := Finset.mem_filter.mp ha
  obtain ⟨hb,xb⟩ := Finset.mem_filter.mp hb
  obtain ⟨hc,xc⟩ := Finset.mem_filter.mp hc
  have nab := rules.triangle x hx a ha b hb xa xb
  have nac := rules.triangle x hx a ha c hc xa xc
  have nbc := rules.triangle x hx b hb c hc xb xc
  intro z hz xz
  by_contra nxz
  have az : a ≠ z := by intro eq; exact nxz (eq ▸ xa)
  have bz : b ≠ z := by intro eq; exact nxz (eq ▸ xb)
  have cz : c ≠ z := by intro eq; exact nxz (eq ▸ xc)
  have miss (v : Fin 21) (h : ¬ Unit H z v) : ¬ Unit H v z :=
    fun hv => h (unit_symm H hv)
  by_cases za : Unit H z a
  · by_cases zb : Unit H z b
    · by_cases zc : Unit H z c
      · exact no_three_common_neighbors H L rules x z a b c hx hz ha hb hc xz ab ac bc
          xa xb xc za zb zc
      · exact rules.pathIsolate z hz a ha b hb c hc ab cz.symm ac bc za zb zc nac nbc
    · by_cases zc : Unit H z c
      · exact rules.pathIsolate z hz a ha c hc b hb ac bz.symm ab bc.symm za zc zb nab
          (fun h => nbc (unit_symm H h))
      · exact rules.pathIsolate x hx b hb c hc z hz bc xz bz cz xb xc nxz (miss b zb) (miss c zc)
  · by_cases zb : Unit H z b
    · by_cases zc : Unit H z c
      · exact rules.pathIsolate z hz b hb c hc a ha bc az.symm ab.symm ac.symm zb zc za
          (fun h => nab (unit_symm H h)) (fun h => nac (unit_symm H h))
      · exact rules.pathIsolate x hx a ha c hc z hz ac xz az cz xa xc nxz (miss a za) (miss c zc)
    · exact rules.pathIsolate x hx a ha b hb z hz ab xz az bz xa xb nxz (miss a za) (miss b zb)

theorem contradiction (H : Simple5Hypergraph (Fin 21)) (L : Finset (Fin 21))
    (nonempty : L.Nonempty) (minimum : ∀ x ∈ L, 6 ≤ (neighbors H L x).card)
    (rules : Rules H L) : False := by
  obtain ⟨x,hx⟩ := nonempty
  have large := minimum x hx
  have universal := universal_of_three H L rules x hx (by omega)
  obtain ⟨a,ha⟩ := Finset.card_pos.mp (show 0 < (neighbors H L x).card by omega)
  obtain ⟨ha,xa⟩ := Finset.mem_filter.mp ha
  have sub : neighbors H L a ⊆ ({x} : Finset (Fin 21)) := by
    intro y hy
    obtain ⟨hy,ay⟩ := Finset.mem_filter.mp hy
    apply Finset.mem_singleton.mpr
    by_contra yx
    exact rules.triangle x hx a ha y hy xa (universal y hy (Ne.symm yx)) ay
  have small := Finset.card_le_card sub
  have largeA := minimum a ha
  simp only [Finset.card_singleton] at small
  omega

def eights (H : Simple5Hypergraph (Fin 21)) : Finset (Fin 21) :=
  Finset.univ.filter fun x => H.degree x=8

theorem eights_at_least_nineteen (H : Simple5Hypergraph (Fin 21))
    (size : H.edges.card=34) (minimum : ∀ x, 8 ≤ H.degree x) : 19 ≤ (eights H).card := by
  have each (x : Fin 21) : 9 ≤ H.degree x+(if H.degree x=8 then 1 else 0) := by
    have lower := minimum x
    split_ifs <;> omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have bound : 189 ≤ 170+(eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,eights] using sum
  omega

/-- The actual excess budget leaves at least six unit neighbors within the
degree-eight set; no local probability classification is used here. -/
theorem neighbors_at_least_six (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (minimum : ∀ x, 8 ≤ H.degree x)
    (x : Fin 21) (hx : x ∈ eights H) : 6 ≤ (neighbors H (eights H) x).card := by
  have dx : H.degree x=8 := (Finset.mem_filter.mp hx).2
  have large := eights_at_least_nineteen H size minimum
  have bad := H.badPartners_card_le_excess cover x
  have bad12 : (H.badPartners x).card ≤ 12 := by simpa [dx] using bad
  let S := ((eights H).erase x) \ H.badPartners x
  have sub : S ⊆ neighbors H (eights H) x := by
    intro y hy
    obtain ⟨hy,notbad⟩ := Finset.mem_sdiff.mp hy
    obtain ⟨yx,hy⟩ := Finset.mem_erase.mp hy
    have positive := H.one_le_codegree cover yx.symm
    have codegree : H.codegree x y=1 := by
      by_contra ne
      apply notbad
      exact Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨yx,Finset.mem_univ y⟩,by omega⟩
    exact Finset.mem_filter.mpr ⟨hy,yx.symm,codegree⟩
  have loss := Finset.card_le_card_sdiff_add_card
    (s := (eights H).erase x) (t := H.badPartners x)
  rw [Finset.card_erase_of_mem hx] at loss
  change (eights H).card-1 ≤ S.card+(H.badPartners x).card at loss
  have bound := Finset.card_le_card sub
  omega

/-- With at most two vertices outside L, an edge containing an L-pair must
contain a third L-vertex. A zero common-triple residue excludes codegree three. -/
theorem codegrees_at_most_two (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (L : Finset (Fin 21)) (large : 19 ≤ L.card)
    (upper : ∀ x ∈ L, ∀ y ∈ L, x ≠ y → H.codegree x y ≤ 3)
    (threeZero : ∀ x ∈ L, ∀ y ∈ L, ∀ z ∈ L,
      x ≠ y → x ≠ z → y ≠ z → H.codegree x y=3 → tripleCodegree H x y z=0) :
    ∀ x ∈ L, ∀ y ∈ L, x ≠ y → H.codegree x y ≤ 2 := by
  intro x hx y hy xy
  have bound := upper x hx y hy xy
  by_contra high
  have three : H.codegree x y=3 := by omega
  obtain ⟨e,he,xe,ye⟩ := cover x y xy
  have outsideSub : e \ L ⊆ Finset.univ \ L := by
    intro z hz
    exact Finset.mem_sdiff.mpr ⟨Finset.mem_univ z,(Finset.mem_sdiff.mp hz).2⟩
  have outside := Finset.card_le_card outsideSub
  have complement : (Finset.univ \ L).card ≤ 2 := by
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ L)]
    simp only [Finset.card_univ,Fintype.card_fin]
    omega
  have split := Finset.card_sdiff_add_card_inter e L
  rw [H.five_uniform e he] at split
  have interLarge : 3 ≤ (e ∩ L).card := by omega
  have pairSmall : ({x,y} : Finset (Fin 21)).card ≤ 2 := Finset.card_le_two
  obtain ⟨z,hz,apart⟩ := Finset.exists_mem_notMem_of_card_lt_card
    (s := {x,y}) (t := e ∩ L) (by omega)
  obtain ⟨ze,hz⟩ := Finset.mem_inter.mp hz
  have zx : z ≠ x := by intro eq; exact apart (by simp [eq])
  have zy : z ≠ y := by intro eq; exact apart (by simp [eq])
  have zero := threeZero x hx y hy z hz xy zx.symm zy.symm three
  have positive : 1 ≤ tripleCodegree H x y z := Finset.one_le_card.mpr
    ⟨e,Finset.mem_filter.mpr ⟨he,xe,ye,ze⟩⟩
  omega

end Aris4Math.ThirtyFour.TwentyOneEightGraph

#print axioms Aris4Math.ThirtyFour.TwentyOneEightGraph.contradiction
#print axioms Aris4Math.ThirtyFour.TwentyOneEightGraph.neighbors_at_least_six
#print axioms Aris4Math.ThirtyFour.TwentyOneEightGraph.codegrees_at_most_two
