import Aris4Math.ThirtyFour.TwentyOneEightQuadCoverage
import Aris4Math.ThirtyFour.LockRelabel
namespace Aris4Math.ThirtyFour.TwentyOneEightQuads
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (high_inventory high_le_two)
open TwentyOneEightQuadCoverage (Residue TriangleFree pair)
set_option maxHeartbeats 0

theorem pair_readback (H : Simple5Hypergraph (Fin 21)) (f : Fin 4↪Fin 21)
    (i j : Fin 4) (ne : i≠j) : H.codegree (f i) (f j)=
      pair (fun z=>H.codegree (f (first z)) (f (second z))) i j := by
  fin_cases i <;> fin_cases j <;> simp +decide [pair,first,second] at ne ⊢ <;>
    rw [H.codegree_comm]

/-- Permutation-complete actual quadruple classification. -/
theorem residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 4↪Fin 21)
    (degrees : ∀j,H.degree (f j)=8)
    (pairs : ∀i j,i≠j→H.codegree (f i) (f j)≤2)
    (triangle : ∀i j k : Fin 4,i≠j→i≠k→j≠k→
      ¬(H.codegree (f i) (f j)=1 ∧ H.codegree (f i) (f k)=1 ∧ H.codegree (f j) (f k)=1)) :
    Residue (fun j=>H.codegree (f (first j)) (f (second j)))
      (fun j=>count H f (highLabels j)) := by
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
  have tf : TriangleFree (fun j=>(co j).val+1) := by
    rw [cofun]
    intro i j k ij ik jk
    rw [←pair_readback H f i j ij,←pair_readback H f i k ik,←pair_readback H f j k jk]
    exact triangle i j k ij ik jk
  rcases TwentyOneEightQuadCoverage.coverage co h tf inventory with res | matched
  · simpa only [cofun] using res
  · apply False.elim
    apply noB
    let chosen:=TwentyOneEightQuadCoverage.choose (TwentyOneEightQuadCoverage.code co h)
    let σ:=TwentyOneEightQuadCoverage.perm chosen.2
    apply TwentyOneEightQuadCoverage.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
    intro T
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,size,show (fun j=>H.degree (f j))=(fun _=>8) from funext degrees]
    simpa only [cofun] using matched T
end Aris4Math.ThirtyFour.TwentyOneEightQuads
#print axioms Aris4Math.ThirtyFour.TwentyOneEightQuads.residual
