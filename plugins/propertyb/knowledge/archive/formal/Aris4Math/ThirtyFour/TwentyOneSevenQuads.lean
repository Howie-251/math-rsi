import Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneSevenTriples
namespace Aris4Math.ThirtyFour.TwentyOneSevenQuads
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (threeVertices)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (high_inventory high_le_two)
set_option maxHeartbeats 0

/-- The exact nine canonical residual trace tables are forced for every four
actual degree-seven vertices. The returned permutation is internal. -/
theorem residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 4↪Fin 21)
    (degrees : ∀j,H.degree (f j)=7) :
    ∃r : TwentyOneSevenQuadCoverage.Residue,∃p : TwentyOneSevenQuadCoverage.Perm,
      ∀T, count H ((TwentyOneSevenQuadCoverage.perm p).toEmbedding.trans f) T=
        TwentyOneSevenQuadCoverage.residueμ r T := by
  have third : ∀i j : Fin 4,i≠j→∃k,k≠i ∧ k≠j := by decide
  have pairs (i j : Fin 4) (ij : i≠j) : H.codegree (f i) (f j)≤2 := by
    obtain ⟨k,ki,kj⟩:=third i j ij
    let g:=threeVertices (f i) (f j) (f k) (f.injective.ne ij)
      (f.injective.ne ki.symm) (f.injective.ne kj.symm)
    have ds : ∀t,H.degree (g t)=(![7,7,7] : Fin 3→ℕ) t := by
      intro t;fin_cases t <;> simp [g,threeVertices,degrees]
    exact (TwentyOneSevenTriples.residual777 H cover size noB g ds).1
  have ne (j) : first j≠second j := by fin_cases j <;> decide
  have lo (j):=H.one_le_codegree cover (f.injective.ne (ne j))
  have hi (j):=pairs (first j) (second j) (ne j)
  let co : Fin 6→Fin 2:=fun j=>⟨H.codegree (f (first j)) (f (second j))-1,
    by have:=lo j;have:=hi j;omega⟩
  have coeq (j) : (co j).val+1=H.codegree (f (first j)) (f (second j)) := by
    have:=lo j;dsimp [co];omega
  have cofun:=funext coeq
  have highs:=high_le_two H f hi
  let h : Fin 5→Fin 3:=fun j=>⟨count H f (highLabels j),by have:=highs j;omega⟩
  have inventory (j) : Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum
      (fun z=>(h z).val) j≤(co j).val+1 := by
    rw [coeq]
    exact high_inventory H f j
  have matched:=TwentyOneSevenQuadCoverage.coverage co h inventory
  let chosen:=TwentyOneSevenQuadCoverage.choose (TwentyOneSevenQuadCoverage.code co h)
  let σ:=TwentyOneSevenQuadCoverage.perm chosen.2
  have counts (T) : count H (σ.toEmbedding.trans f) T=TwentyOneSevenQuadCoverage.μ chosen.1 T := by
    change ThirtyThree.MultiLockRecovery.count H (σ.toEmbedding.trans f) T=_
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,size,funext degrees]
    simpa only [cofun] using matched T
  have lower : 61≤chosen.1.val := by
    by_contra h
    exact noB (TwentyOneSevenQuadCoverage.propertyB_of_counts H (σ.toEmbedding.trans f)
      chosen.1 (by omega) counts)
  have upper:=chosen.1.isLt
  refine ⟨⟨chosen.1.val-61,by omega⟩,chosen.2,?_⟩
  intro T
  rw [counts,TwentyOneSevenQuadCoverage.residue_readback chosen.1 lower]
end Aris4Math.ThirtyFour.TwentyOneSevenQuads
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenQuads.residual
