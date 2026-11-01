import Aris4Math.ThirtyFour.TwentyEightGraph

namespace Aris4Math.ThirtyFour.TwentyEight
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles (first second count highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyStructure
open Aris4Math.ThirtyFour.TwentyEightGraph (Unit)

theorem propertyB_of_minimum_eight (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x, 8 ≤ H.degree x) : PropertyB H := by
  classical
  by_contra noB
  let L := eights H
  have large : 10 ≤ L.card := eights_at_least_ten H size minimum
  have degree (x : Fin 20) (hx : x ∈ L) : H.degree x=8 := (mem_eights H x).mp hx
  have rules : UnitGraph.Rules L (Unit H) := TwentyEightGraph.rules H cover size noB minimum
  rcases UnitGraph.dichotomy rules (by omega) with ⟨x,hx,universal⟩ | thin
  · obtain ⟨p,hp,px,_⟩ := exists_third L (by omega) x x
    have xp := universal p hp px.symm
    let S := (L.erase x).erase p
    have pLeaf : p ∈ L.erase x := Finset.mem_erase.mpr ⟨px,hp⟩
    have scard : 8 ≤ S.card := by
      simp only [S,Finset.card_erase_of_mem pLeaf,Finset.card_erase_of_mem hx]
      omega
    have member (z : Fin 20) (hz : z ∈ S) : z ≠ p ∧ z ≠ x ∧ z ∈ L := by
      obtain ⟨zp,hz⟩ := Finset.mem_erase.mp hz
      obtain ⟨zx,hz⟩ := Finset.mem_erase.mp hz
      exact ⟨zp,zx,hz⟩
    have leafPair (a b : Fin 20) (ha : a ∈ L) (hb : b ∈ L)
        (ax : a ≠ x) (bx : b ≠ x) (ab : a ≠ b) : H.codegree a b=2 :=
      TwentyEightGraph.pair_two H cover size noB minimum a b ha hb ab
        (TwentyEightGraph.triangle H cover size noB minimum x a b hx ha hb
          (universal a ha ax.symm) (universal b hb bx.symm))
    have capacity (e : Finset (Fin 20)) (he : e ∈ H.edges) (hpe : p ∈ e) : (S ∩ e).card ≤ 2 := by
      by_contra hn
      obtain ⟨f,hf⟩ := TwentySevenMany.exists_indexed_subset (S ∩ e) (show 3 ≤ (S ∩ e).card by omega)
      have mem (i : Fin 3) := Finset.mem_inter.mp (hf i)
      have info (i : Fin 3) := member (f i) (mem i).1
      let g := fourVertices p (f 0) (f 1) (f 2) (info 0).1.symm (info 1).1.symm (info 2).1.symm
        (f.injective.ne (by decide)) (f.injective.ne (by decide)) (f.injective.ne (by decide))
      have lows (i : Fin 4) : g i ∈ L := by
        fin_cases i
        · exact hp
        · exact (info 0).2.2
        · exact (info 1).2.2
        · exact (info 2).2.2
      have notCenter (i : Fin 4) : g i ≠ x := by
        fin_cases i
        · exact px
        · exact (info 0).2.1
        · exact (info 1).2.1
        · exact (info 2).2.1
      have pairs (j) : H.codegree (g (first j)) (g (second j))=2 :=
        leafPair _ _ (lows _) (lows _) (notCenter _) (notCenter _) (g.injective.ne (by fin_cases j <;> decide))
      have facts := TwentyEightLocal.graph_facts H cover size noB minimum g lows
      have zero : count H g (highLabels 4)=0 := facts.2.2.2.2.2.1 pairs
      have positive : 1 ≤ count H g (highLabels 4) := (TwentyEightLocal.common_quad_iff H g).mp
        ⟨e,he,by intro i; fin_cases i; exact hpe; exact (mem 0).2; exact (mem 1).2; exact (mem 2).2⟩
      omega
    have extra (e : Finset (Fin 20)) (he : e ∈ H.edges) (hpe : p ∈ e) (hxe : x ∈ e) :
        (S ∩ e).card+1 ≤ 2 := by
      have bound : (S ∩ e).card ≤ 1 := by
        apply Finset.card_le_one.mpr
        intro a ha b hb
        obtain ⟨ha,hae⟩ := Finset.mem_inter.mp ha
        obtain ⟨hb,hbe⟩ := Finset.mem_inter.mp hb
        have ia := member a ha
        have ib := member b hb
        by_contra ab
        let g := fourVertices x p a b px.symm ia.2.1.symm ib.2.1.symm ia.1.symm ib.1.symm ab
        have facts := TwentyEightGraph.four H cover size noB minimum x p a b hx hp ia.2.2 ib.2.2
          px.symm ia.2.1.symm ib.2.1.symm ia.1.symm ib.1.symm ab
        have xa := universal a ia.2.2 ia.2.1.symm
        have xb := universal b ib.2.2 ib.2.1.symm
        have zero : count H g (highLabels 4)=0 := facts.2.2.2.2.1 xp.2 xa.2 xb.2
        have positive : 1 ≤ count H g (highLabels 4) := (TwentyEightLocal.common_quad_iff H g).mp
          ⟨e,he,by intro i; fin_cases i; exact hxe; exact hpe; exact hae; exact hbe⟩
        omega
      omega
    have each (z : Fin 20) (hz : z ∈ S) : H.codegree p z=2 :=
      leafPair p z hp (member z hz).2.2 px (member z hz).2.1 (member z hz).1.symm
    have sum : (∑ z ∈ S, H.codegree p z)=2*S.card := by
      calc
        _ = ∑ _z ∈ S, 2 := Finset.sum_congr rfl each
        _ = _ := by simp [Nat.mul_comm]
    have cap := Incidence.extra_capacity H p x S 2 capacity extra
    have dp := degree p hp
    have px1 : H.codegree p x=1 := (TwentyEightGraph.unit_symm H xp).2
    rw [sum,dp,px1] at cap
    omega
  · obtain ⟨p,hp⟩ := Finset.one_le_card.mp (show 1 ≤ L.card by omega)
    let S := L.erase p
    have scard : 9 ≤ S.card := by simp only [S,Finset.card_erase_of_mem hp]; omega
    have capacity (e : Finset (Fin 20)) (he : e ∈ H.edges) (hpe : p ∈ e) : (S ∩ e).card ≤ 2 := by
      by_contra hn
      obtain ⟨f,hf⟩ := TwentySevenMany.exists_indexed_subset (S ∩ e) (show 3 ≤ (S ∩ e).card by omega)
      have mem (i : Fin 3) := Finset.mem_inter.mp (hf i)
      have info (i : Fin 3) := Finset.mem_erase.mp (mem i).1
      let g := fourVertices p (f 0) (f 1) (f 2) (info 0).1.symm (info 1).1.symm (info 2).1.symm
        (f.injective.ne (by decide)) (f.injective.ne (by decide)) (f.injective.ne (by decide))
      have lows (i : Fin 4) : g i ∈ L := by
        fin_cases i
        · exact hp
        · exact (info 0).2
        · exact (info 1).2
        · exact (info 2).2
      have facts := TwentyEightLocal.graph_facts H cover size noB minimum g lows
      have localThin : (Finset.univ.filter fun j : Fin 3 =>
          H.codegree (g (first (j.castLE (by decide : 3 ≤ 6)))) (g (second (j.castLE (by decide : 3 ≤ 6))))=1).card ≤ 1 := by
        apply Finset.card_le_one.mpr
        intro i hi j hj
        have eq (k : Fin 3) : H.codegree (g (first (k.castLE (by decide : 3 ≤ 6)))) (g (second (k.castLE (by decide : 3 ≤ 6))))=H.codegree p (g k.succ) := by
          fin_cases k <;> rfl
        have ni : g i.succ ∈ UnitGraph.neighbors L (Unit H) p := by
          apply Finset.mem_filter.mpr
          refine ⟨lows _,?_,?_⟩
          · change g 0 ≠ g i.succ
            exact g.injective.ne (Ne.symm (Fin.succ_ne_zero i))
          · rw [← eq]; exact (Finset.mem_filter.mp hi).2
        have nj : g j.succ ∈ UnitGraph.neighbors L (Unit H) p := by
          apply Finset.mem_filter.mpr
          refine ⟨lows _,?_,?_⟩
          · change g 0 ≠ g j.succ
            exact g.injective.ne (Ne.symm (Fin.succ_ne_zero j))
          · rw [← eq]; exact (Finset.mem_filter.mp hj).2
        have same := Finset.card_le_one.mp (thin p hp) _ ni _ nj
        exact (Fin.succ_injective 3) (g.injective same)
      have zero : count H g (highLabels 4)=0 := facts.2.2.2.2.2.2.2 localThin
      have positive : 1 ≤ count H g (highLabels 4) := (TwentyEightLocal.common_quad_iff H g).mp
        ⟨e,he,by intro i; fin_cases i; exact hpe; exact (mem 0).2; exact (mem 1).2; exact (mem 2).2⟩
      omega
    let A := S.filter (fun z => H.codegree p z=1)
    have smallA : A.card ≤ 1 := by
      apply (Finset.card_le_card (show A ⊆ UnitGraph.neighbors L (Unit H) p from ?_)).trans (thin p hp)
      intro z hz
      obtain ⟨hz,hunit⟩ := Finset.mem_filter.mp hz
      obtain ⟨zp,hz⟩ := Finset.mem_erase.mp hz
      exact Finset.mem_filter.mpr ⟨hz,zp.symm,hunit⟩
    have each (z : Fin 20) (hz : z ∈ S) :
        H.codegree p z+(if H.codegree p z=1 then 1 else 0)=2 := by
      obtain ⟨zp,hz⟩ := Finset.mem_erase.mp hz
      have lower := H.one_le_codegree cover zp.symm
      have upper := TwentyEightLocal.all_codegrees_le_two H cover size noB minimum p z hp hz zp.symm
      by_cases one : H.codegree p z=1
      · simp [one]
      · have two : H.codegree p z=2 := by omega
        simp [two]
    have sum : (∑ z ∈ S, H.codegree p z)+A.card=2*S.card := by
      have hs := Finset.sum_congr rfl (fun z hz => each z hz)
      simpa [Finset.sum_add_distrib,Finset.sum_boole,A,Nat.mul_comm] using hs
    have cap := Incidence.codegree_capacity H p S 2 capacity
    have dp := degree p hp
    rw [dp] at cap
    omega
end Aris4Math.ThirtyFour.TwentyEight
#print axioms Aris4Math.ThirtyFour.TwentyEight.propertyB_of_minimum_eight
