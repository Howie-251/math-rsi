import Aris4Math.ThirtyFour.TwentyOneEightTripleCoverage
import Aris4Math.ThirtyFour.TwentyOneEightPairs
import Aris4Math.ThirtyFour.LockRelabel
namespace Aris4Math.ThirtyFour.TwentyOneEightTriples
open Aris4Math.ThirtyThree.TripleProfiles
open TwentyOneEightTripleCoverage (Residue)

/-- Full triple consequences from actual degree-eight locks. -/
theorem residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀j,H.degree (f j)=8)
    (pairs : ∀i j,i≠j→H.codegree (f i) (f j)≤3) :
    Residue (H.codegree (f 0) (f 1)) (H.codegree (f 0) (f 2)) (H.codegree (f 1) (f 2))
      (tripleCodegree H (f 0) (f 1) (f 2)) := by
  have la:=H.one_le_codegree cover (f.injective.ne (by decide : (0:Fin 3)≠1))
  have lb:=H.one_le_codegree cover (f.injective.ne (by decide : (0:Fin 3)≠2))
  have lc:=H.one_le_codegree cover (f.injective.ne (by decide : (1:Fin 3)≠2))
  have ua:=pairs 0 1 (by decide)
  have ub:=pairs 0 2 (by decide)
  have uc:=pairs 1 2 (by decide)
  obtain ⟨ta,tb,tc⟩:=ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  let a : Fin 3:=⟨H.codegree (f 0) (f 1)-1,by omega⟩
  let b : Fin 3:=⟨H.codegree (f 0) (f 2)-1,by omega⟩
  let c : Fin 3:=⟨H.codegree (f 1) (f 2)-1,by omega⟩
  let t : Fin 4:=⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  have ae : a.val+1=H.codegree (f 0) (f 1) := by dsimp [a];omega
  have be : b.val+1=H.codegree (f 0) (f 2) := by dsimp [b];omega
  have ce : c.val+1=H.codegree (f 1) (f 2) := by dsimp [c];omega
  rcases TwentyOneEightTripleCoverage.coverage a b c t (by simpa only [ae] using ta)
      (by simpa only [be] using tb) (by simpa only [ce] using tc) with residue | matched
  · simpa only [ae,be,ce] using residue
  · apply False.elim
    apply noB
    let chosen:=TwentyOneEightTripleCoverage.choose (TwentyOneEightTripleCoverage.code a b c t)
    let σ:=TwentyOneEightTripleCoverage.perm chosen.2
    apply TwentyOneEightTripleCoverage.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
    intro T
    rw [LockRelabel.count_comp_perm]
    change count H f (T.map σ.toEmbedding)=_
    rw [actual_recovered,triple_count_eq,size,degrees 0,degrees 1,degrees 2]
    simpa only [ae,be,ce] using matched T

/-- Without Property B every pair of degree-eight vertices has codegree at most three. -/
theorem pair_le_three (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y : Fin 21) (xy : x≠y)
    (dx : H.degree x=8) (dy : H.degree y=8) : H.codegree x y≤3 := by
  by_contra high
  exact noB (TwentyOneEightPairs.propertyB_of_high H size x y xy dx dy (by omega))
end Aris4Math.ThirtyFour.TwentyOneEightTriples
#print axioms Aris4Math.ThirtyFour.TwentyOneEightTriples.residual
