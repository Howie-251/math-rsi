import Aris4Math.ThirtyFour.TwentyOneEightStructure
import Aris4Math.ThirtyFour.TwentyOneEightStarLocal

/-! A real common edge on a unit-codegree claw gives one of the two
five-lock star profiles. The two real edges exhaust each old leaf pair. -/

namespace Aris4Math.ThirtyFour.TwentyOneEightClaw

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open TwentyOneEightGraph (eights Unit neighbors)

theorem pair_exhausted (H : Simple5Hypergraph (Fin 21))
    {a b : Fin 21} {e g : Finset (Fin 21)} (two : H.codegree a b=2)
    (he : e∈H.edges) (hg : g∈H.edges) (eg : e≠g)
    (ae : a∈e) (be : b∈e) (ag : a∈g) (bg : b∈g) :
    ∀h∈H.edges,a∈h→b∈h→h=e ∨ h=g := by
  have sub : ({e,g} : Finset (Finset (Fin 21))) ⊆
      H.edges.filter (fun h => a∈h ∧ b∈h) := by
    intro h hh
    simp only [Finset.mem_insert,Finset.mem_singleton] at hh
    rcases hh with rfl | rfl
    · exact Finset.mem_filter.mpr ⟨he,ae,be⟩
    · exact Finset.mem_filter.mpr ⟨hg,ag,bg⟩
  have eq := Finset.eq_of_subset_of_card_le sub (show
      (H.edges.filter (fun h => a∈h ∧ b∈h)).card ≤ ({e,g} : Finset _).card by
    change H.codegree a b ≤ _
    simp [two,eg])
  intro h hh ah bh
  have mem : h∈H.edges.filter (fun h => a∈h ∧ b∈h) :=
    Finset.mem_filter.mpr ⟨hh,ah,bh⟩
  rw [←eq] at mem
  simpa using mem

theorem high_count_of_two_edges (H : Simple5Hypergraph (Fin 21))
    (f : Fin 5↪Fin 21) (e g : Finset (Fin 21)) (he : e∈H.edges)
    (hg : g∈H.edges) (eg : e≠g)
    (only : ∀h∈H.edges,3≤(lockSignature f h).card→h=e ∨ h=g)
    (T : Finset (Fin 5)) (large : 3≤T.card) :
    count H f T=(if lockSignature f e=T then 1 else 0)+
      (if lockSignature f g=T then 1 else 0) := by
  have eq : H.edges.filter (fun h => lockSignature f h=T) =
      ({e,g} : Finset _).filter (fun h => lockSignature f h=T) := by
    ext h
    simp only [Finset.mem_filter,Finset.mem_insert,Finset.mem_singleton]
    constructor
    · rintro ⟨hh,sig⟩
      exact ⟨only h hh (sig.symm ▸ large),sig⟩
    · rintro ⟨rfl | rfl,sig⟩
      · exact ⟨he,sig⟩
      · exact ⟨hg,sig⟩
  change (H.edges.filter (fun h => lockSignature f h=T)).card=_
  rw [eq]
  by_cases se : lockSignature f e=T <;> by_cases sg : lockSignature f g=T <;>
    simp [Finset.filter_insert,Finset.filter_singleton,se,sg,eg]

theorem large_contains_old_pair : ∀T : Finset (Fin 5),3≤T.card→
    (0∈T ∧ 1∈T) ∨ (0∈T ∧ 2∈T) ∨ (0∈T ∧ 3∈T) ∨
    (1∈T ∧ 2∈T) ∨ (1∈T ∧ 3∈T) ∨ (2∈T ∧ 3∈T) := by decide +kernel

theorem star_high_identity : ∀q : Fin 2,∀T : Finset (Fin 5),
    (if ({0,1,2,3} : Finset (Fin 5))=T then 1 else 0)+
      (if (if q=0 then ({1,2,3} : Finset (Fin 5)) else {1,2,3,4})=T then 1 else 0)=
      TwentyOneEightStarLocal.high q T := by decide +kernel

/-- The actual claw field needed by the global unit graph contradiction. -/
theorem no_common_edge (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H) :
    ∀x∈eights H,∀a∈eights H,∀b∈eights H,∀c∈eights H,
      a≠b→a≠c→b≠c→Unit H x a→Unit H x b→Unit H x c→
      ¬Unit H a b→¬Unit H a c→¬Unit H b c→
      ∀e∈H.edges,x∈e→a∈e→b∈e→c∈e→False := by
  intro x hx a ha b hb c hc ab ac bc xa xb xc nab nac nbc e he xe ae be ce
  have nonunit_two (u v : Fin 21) (hu : u∈eights H) (hv : v∈eights H)
      (uv : u≠v) (nu : ¬Unit H u v) : H.codegree u v=2 := by
    have lo := H.one_le_codegree cover uv
    have hi := TwentyOneEightStructure.pair_le_two H cover size minimum noB u hu v hv uv
    have ne : H.codegree u v≠1 := fun h => nu ⟨uv,h⟩
    omega
  have ab2 := nonunit_two a b ha hb ab nab
  have ac2 := nonunit_two a c ha hc ac nac
  have bc2 := nonunit_two b c hb hc bc nbc
  have dx := (Finset.mem_filter.mp hx).2
  have da := (Finset.mem_filter.mp ha).2
  have db := (Finset.mem_filter.mp hb).2
  have dc := (Finset.mem_filter.mp hc).2
  let p := fourVertices x a b c xa.1 xb.1 xc.1 ab ac bc
  have degrees : ∀j,H.degree (p j)=8 := by intro j;fin_cases j <;> assumption
  have co : (fun j => H.codegree (p (ThirtyThree.QuadProfiles.first j))
      (p (ThirtyThree.QuadProfiles.second j)))=![1,1,1,2,2,2] := by
    funext j
    fin_cases j <;> simp [p,fourVertices,ThirtyThree.QuadProfiles.first,
      ThirtyThree.QuadProfiles.second,xa.2,xb.2,xc.2,ab2,ac2,bc2]
  have res := (TwentyOneEightStructure.quad_residual H cover size minimum noB p degrees).2.2 co
  have sigE : lockSignature p e=ThirtyThree.QuadProfiles.highLabels 4 := by
    ext j
    fin_cases j <;> simp [p,fourVertices,ThirtyThree.QuadProfiles.highLabels,xe,ae,be,ce]
  have positive : 1≤ThirtyThree.QuadProfiles.count H p (ThirtyThree.QuadProfiles.highLabels 4) :=
    Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,sigE⟩⟩
  have leaf : ThirtyThree.QuadProfiles.count H p (ThirtyThree.QuadProfiles.highLabels 3)=1 := by
    rcases res with zero | ⟨_,leaf⟩
    · change ThirtyThree.QuadProfiles.count H p (ThirtyThree.QuadProfiles.highLabels 4)=0 at zero
      omega
    · exact leaf
  obtain ⟨g,hg⟩ := Finset.one_le_card.mp (show 1≤
      (H.edges.filter (fun g => lockSignature p g=ThirtyThree.QuadProfiles.highLabels 3)).card by
    change 1≤ThirtyThree.QuadProfiles.count H p (ThirtyThree.QuadProfiles.highLabels 3)
    omega)
  obtain ⟨hg,sigG⟩ := Finset.mem_filter.mp hg
  have memG (i : Fin 4) : p i∈g ↔ i∈ThirtyThree.QuadProfiles.highLabels 3 := by
    rw [←mem_lockSignature,sigG]
  have xg : x∉g := by simpa [p,fourVertices,ThirtyThree.QuadProfiles.highLabels] using memG 0
  have ag : a∈g := by simpa [p,fourVertices,ThirtyThree.QuadProfiles.highLabels] using memG 1
  have bg : b∈g := by simpa [p,fourVertices,ThirtyThree.QuadProfiles.highLabels] using memG 2
  have cg : c∈g := by simpa [p,fourVertices,ThirtyThree.QuadProfiles.highLabels] using memG 3
  have eg : e≠g := fun eq => xg (eq ▸ xe)
  have many := TwentyOneEightGraph.neighbors_at_least_six H cover size minimum x hx
  obtain ⟨w,hw,we⟩ := Finset.exists_mem_notMem_of_card_lt_card (show
      e.card<(neighbors H (eights H) x).card by rw [H.five_uniform e he];omega)
  obtain ⟨hw,xw⟩ := Finset.mem_filter.mp hw
  have aw : a≠w := by intro eq;exact we (eq ▸ ae)
  have bw : b≠w := by intro eq;exact we (eq ▸ be)
  have cw : c≠w := by intro eq;exact we (eq ▸ ce)
  have aw2 := nonunit_two a w ha hw aw
    (TwentyOneEightStructure.triangle_free H cover size noB x hx a ha w hw xa xw)
  have bw2 := nonunit_two b w hb hw bw
    (TwentyOneEightStructure.triangle_free H cover size noB x hx b hb w hw xb xw)
  have cw2 := nonunit_two c w hc hw cw
    (TwentyOneEightStructure.triangle_free H cover size noB x hx c hc w hw xc xw)
  have dw := (Finset.mem_filter.mp hw).2
  let f : Fin 5↪Fin 21 := ⟨![x,a,b,c,w],by
    intro i j eq
    fin_cases i <;> fin_cases j <;>
      simp [xa.1,xb.1,xc.1,xw.1,ab,ac,aw,bc,bw,cw,
        Ne.symm xa.1,Ne.symm xb.1,Ne.symm xc.1,Ne.symm xw.1,
        Ne.symm ab,Ne.symm ac,Ne.symm aw,Ne.symm bc,Ne.symm bw,Ne.symm cw] at eq ⊢⟩
  have fdeg : ∀i,H.degree (f i)=8 := by intro i;fin_cases i <;> assumption
  have fpair : ∀i j,i≠j→H.codegree (f i) (f j)=TwentyOneEightStarLocal.pair i j := by
    have xa1 := xa.2
    have xb1 := xb.2
    have xc1 := xc.2
    have xw1 := xw.2
    have ax := H.codegree_comm a x
    have bx := H.codegree_comm b x
    have cx := H.codegree_comm c x
    have wx := H.codegree_comm w x
    have ba := H.codegree_comm b a
    have ca := H.codegree_comm c a
    have wa := H.codegree_comm w a
    have cb := H.codegree_comm c b
    have wb := H.codegree_comm w b
    have wc := H.codegree_comm w c
    intro i j ne
    fin_cases i <;> fin_cases j <;>
      simp +decide [f,TwentyOneEightStarLocal.pair] at ne ⊢ <;> omega
  have fE : lockSignature f e=({0,1,2,3} : Finset (Fin 5)) := by
    ext i;fin_cases i <;> simp [f,xe,ae,be,ce,we]
  obtain ⟨q,fG⟩ : ∃q : Fin 2,lockSignature f g=
      (if q=0 then ({1,2,3} : Finset (Fin 5)) else {1,2,3,4}) := by
    by_cases wg : w∈g
    · refine ⟨1,?_⟩
      ext i;fin_cases i <;> simp [f,xg,ag,bg,cg,wg]
    · refine ⟨0,?_⟩
      ext i;fin_cases i <;> simp [f,xg,ag,bg,cg,wg]
  have only : ∀h∈H.edges,3≤(lockSignature f h).card→h=e ∨ h=g := by
    intro h hh large
    have cases := large_contains_old_pair (lockSignature f h) large
    simp only [mem_lockSignature] at cases
    change (x∈h ∧ a∈h) ∨ (x∈h ∧ b∈h) ∨ (x∈h ∧ c∈h) ∨
      (a∈h ∧ b∈h) ∨ (a∈h ∧ c∈h) ∨ (b∈h ∧ c∈h) at cases
    rcases cases with xaH | xbH | xcH | abH | acH | bcH
    · exact Or.inl (H.edge_unique_of_codegree_one xa.2 hh he xaH.1 xaH.2 xe ae)
    · exact Or.inl (H.edge_unique_of_codegree_one xb.2 hh he xbH.1 xbH.2 xe be)
    · exact Or.inl (H.edge_unique_of_codegree_one xc.2 hh he xcH.1 xcH.2 xe ce)
    · exact pair_exhausted H ab2 he hg eg ae be ag bg h hh abH.1 abH.2
    · exact pair_exhausted H ac2 he hg eg ae ce ag cg h hh acH.1 acH.2
    · exact pair_exhausted H bc2 he hg eg be ce bg cg h hh bcH.1 bcH.2
  apply noB (TwentyOneEightStarLocal.propertyB_of_high H size f fdeg fpair q ?_)
  intro T large
  rw [high_count_of_two_edges H f e g he hg eg only T large,fE,fG]
  exact star_high_identity q T

end Aris4Math.ThirtyFour.TwentyOneEightClaw

#print axioms Aris4Math.ThirtyFour.TwentyOneEightClaw.no_common_edge
