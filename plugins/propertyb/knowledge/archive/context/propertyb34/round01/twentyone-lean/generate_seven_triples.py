from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s='''import Aris4Math.ThirtyFour.TwentyOneSevenTriple777Coverage
import Aris4Math.ThirtyFour.TwentyOneSevenTriple778Coverage
import Aris4Math.ThirtyFour.TwentyOneSevenTriple788Coverage
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
import Aris4Math.ThirtyFour.TwentyOneSixPairs
import Aris4Math.ThirtyFour.LockRelabel
namespace Aris4Math.ThirtyFour.TwentyOneSevenTriples
open Aris4Math.ThirtyThree.TripleProfiles

theorem pair_le_four (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y : Fin 21) (xy : x≠y)
    (dx : H.degree x=7) (dy7 : 7≤H.degree y) (dy8 : H.degree y≤8) : H.codegree x y≤4 := by
  by_contra high
  apply noB
  exact TwentyOneSixPairs.propertyB_of_high H size x y xy (by omega) (by omega)
    (by omega) dy8 (by omega)
'''
for d in [7,8]:
 suffix='77'+str(d);cov='TwentyOneSevenTriple'+suffix+'Coverage';ordinary='TwentyOneSevenTriple'+suffix
 s+=f'''
theorem residual{suffix} (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀j,H.degree (f j)=(![7,7,{d}] : Fin 3→ℕ) j) :
    H.codegree (f 0) (f 1)≤2 ∧ H.codegree (f 0) (f 2)≤2 ∧ H.codegree (f 1) (f 2)≤2 := by
  have d0 : H.degree (f 0)=7:=degrees 0
  have d1 : H.degree (f 1)=7:=degrees 1
  have d2 : H.degree (f 2)={d}:=degrees 2
  have la:=H.one_le_codegree cover (f.injective.ne (by decide : (0:Fin 3)≠1))
  have lb:=H.one_le_codegree cover (f.injective.ne (by decide : (0:Fin 3)≠2))
  have lc:=H.one_le_codegree cover (f.injective.ne (by decide : (1:Fin 3)≠2))
  have ua:=pair_le_four H size noB (f 0) (f 1) (f.injective.ne (by decide)) d0 (by omega) (by omega)
  have ub:=pair_le_four H size noB (f 0) (f 2) (f.injective.ne (by decide)) d0 (by omega) (by omega)
  have uc:=pair_le_four H size noB (f 1) (f 2) (f.injective.ne (by decide)) d1 (by omega) (by omega)
  obtain ⟨ta,tb,tc⟩:=ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  obtain ⟨ia,ib,ic⟩:=TwentyOneSixIncidence.inventories H (f 0) (f 1) (f 2)
    (f.injective.ne (by decide)) (f.injective.ne (by decide)) (f.injective.ne (by decide))
  rw [d0] at ia
  rw [d1] at ib
  rw [d2] at ic
  let a : Fin 4:=⟨H.codegree (f 0) (f 1)-1,by omega⟩
  let b : Fin 4:=⟨H.codegree (f 0) (f 2)-1,by omega⟩
  let c : Fin 4:=⟨H.codegree (f 1) (f 2)-1,by omega⟩
  let t : Fin 5:=⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  have ae : a.val+1=H.codegree (f 0) (f 1) := by dsimp [a];omega
  have be : b.val+1=H.codegree (f 0) (f 2) := by dsimp [b];omega
  have ce : c.val+1=H.codegree (f 1) (f 2) := by dsimp [c];omega
  rcases {cov}.coverage a b c t (by simpa only [ae] using ta)
      (by simpa only [be] using tb) (by simpa only [ce] using tc)
      (by simpa only [ae,be] using ia) (by simpa only [ae,ce] using ib)
      (by simpa only [be,ce] using ic) with residue | matched
  · simpa only [ae,be,ce] using residue
  · apply False.elim
    apply noB
    let chosen:={cov}.choose ({cov}.code a b c t)
    let σ:={cov}.perm chosen.2
    apply {ordinary}.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
    intro T
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,triple_count_eq,size,d0,d1,d2]
    simpa only [ae,be,ce] using matched T
'''
s+='''
theorem unit_neighbors_pair_le_two (H : Simple5Hypergraph (Fin 21))
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀j,H.degree (f j)=(![7,8,8] : Fin 3→ℕ) j)
    (unit01 : H.codegree (f 0) (f 1)=1) (unit02 : H.codegree (f 0) (f 2)=1) :
    H.codegree (f 1) (f 2)≤2 := by
  have d0 : H.degree (f 0)=7:=degrees 0
  have d1 : H.degree (f 1)=8:=degrees 1
  have d2 : H.degree (f 2)=8:=degrees 2
  have upper:=ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H (f 1) (f 2)
  obtain ⟨ta,tb,tc⟩:=ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  obtain ⟨_,ib,_⟩:=TwentyOneSixIncidence.inventories H (f 0) (f 1) (f 2)
    (f.injective.ne (by decide)) (f.injective.ne (by decide)) (f.injective.ne (by decide))
  rw [unit01,d1] at ib
  let c : Fin 9:=⟨H.codegree (f 1) (f 2),by omega⟩
  let t : Fin 2:=⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  rcases TwentyOneSevenTriple788Coverage.coverage c t tc ib with low | matched
  · exact low
  · apply False.elim
    apply noB
    let chosen:=TwentyOneSevenTriple788Coverage.choose (TwentyOneSevenTriple788Coverage.code c t)
    let σ:=TwentyOneSevenTriple788Coverage.perm chosen.2
    apply TwentyOneSevenTriple788.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
    intro T
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,triple_count_eq,size,d0,d1,d2,unit01,unit02]
    exact matched T
end Aris4Math.ThirtyFour.TwentyOneSevenTriples
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenTriples.residual777
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenTriples.residual778
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenTriples.unit_neighbors_pair_le_two
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyOneSevenTriples.lean').write_text(s)
