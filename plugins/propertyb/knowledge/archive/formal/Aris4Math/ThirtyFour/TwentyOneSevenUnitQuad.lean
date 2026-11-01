import Aris4Math.ThirtyFour.TwentyOneSevenUnitQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneSevenTriples
namespace Aris4Math.ThirtyFour.TwentyOneSevenUnitQuad
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (threeVertices)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (high_inventory high_le_two)
set_option maxHeartbeats 0

theorem residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 4↪Fin 21)
    (degrees : ∀j,H.degree (f j)=(![7,8,8,8] : Fin 4→ℕ) j)
    (units : ∀j : Fin 4,j≠0→H.codegree (f 0) (f j)=1) :
    H.codegree (f 1) (f 2)=2 ∧ H.codegree (f 1) (f 3)=2 ∧
      H.codegree (f 2) (f 3)=2 ∧ count H f (highLabels 4)=0 := by
  have tail (i j : Fin 4) (i0 : i≠0) (j0 : j≠0) (ij : i≠j) : H.codegree (f i) (f j)≤2 := by
    let g:=threeVertices (f 0) (f i) (f j) (f.injective.ne i0.symm)
      (f.injective.ne j0.symm) (f.injective.ne ij)
    have di : H.degree (f i)=8 := by fin_cases i <;> simp +decide at i0 ⊢ <;> exact degrees _
    have dj : H.degree (f j)=8 := by fin_cases j <;> simp +decide at j0 ⊢ <;> exact degrees _
    exact TwentyOneSevenTriples.unit_neighbors_pair_le_two H size noB g
      (by intro k;fin_cases k <;> simp [g,threeVertices,degrees 0,di,dj])
      (units i i0) (units j j0)
  have ne (j) : first j≠second j := by fin_cases j <;> decide
  have hi (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    fin_cases j
    · change H.codegree (f 0) (f 1)≤2
      rw [units 1 (by decide)];decide
    · change H.codegree (f 0) (f 2)≤2
      rw [units 2 (by decide)];decide
    · change H.codegree (f 0) (f 3)≤2
      rw [units 3 (by decide)];decide
    · exact tail 1 2 (by decide) (by decide) (by decide)
    · exact tail 1 3 (by decide) (by decide) (by decide)
    · exact tail 2 3 (by decide) (by decide) (by decide)
  have lo (i j : Fin 4) (ij : i≠j):=H.one_le_codegree cover (f.injective.ne ij)
  have ua:=tail 1 2 (by decide) (by decide) (by decide)
  have ub:=tail 1 3 (by decide) (by decide) (by decide)
  have uc:=tail 2 3 (by decide) (by decide) (by decide)
  have la:=lo 1 2 (by decide)
  have lb:=lo 1 3 (by decide)
  have lc:=lo 2 3 (by decide)
  let a : Fin 2:=⟨H.codegree (f 1) (f 2)-1,by omega⟩
  let b : Fin 2:=⟨H.codegree (f 1) (f 3)-1,by omega⟩
  let c : Fin 2:=⟨H.codegree (f 2) (f 3)-1,by omega⟩
  have ae : a.val+1=H.codegree (f 1) (f 2) := by dsimp [a];omega
  have be : b.val+1=H.codegree (f 1) (f 3) := by dsimp [b];omega
  have ce : c.val+1=H.codegree (f 2) (f 3) := by dsimp [c];omega
  have cofun : TwentyOneSevenUnitQuadCoverage.co (a.val+1) (b.val+1) (c.val+1)=
      (fun j=>H.codegree (f (first j)) (f (second j))) := by
    funext j
    fin_cases j <;> simp +decide [TwentyOneSevenUnitQuadCoverage.co,first,second,units,ae,be,ce]
  have highs:=high_le_two H f hi
  let h : Fin 5→Fin 3:=fun j=>⟨count H f (highLabels j),by have:=highs j;omega⟩
  have inventory (j) : Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum
      (fun z=>(h z).val) j≤TwentyOneSevenUnitQuadCoverage.co (a.val+1) (b.val+1) (c.val+1) j := by
    rw [cofun]
    exact high_inventory H f j
  rcases TwentyOneSevenUnitQuadCoverage.coverage a b c h inventory with res | matched
  · simpa only [ae,be,ce] using res
  · apply False.elim
    apply noB
    let chosen:=TwentyOneSevenUnitQuadCoverage.choose (TwentyOneSevenUnitQuadCoverage.code a b c h)
    let σ:=TwentyOneSevenUnitQuadCoverage.perm chosen.2
    apply TwentyOneSevenQuad7888.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
    intro T
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,size,funext degrees]
    simpa only [cofun] using matched T
end Aris4Math.ThirtyFour.TwentyOneSevenUnitQuad
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenUnitQuad.residual
