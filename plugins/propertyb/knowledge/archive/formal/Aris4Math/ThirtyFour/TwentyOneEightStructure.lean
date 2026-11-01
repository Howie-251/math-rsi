import Aris4Math.ThirtyFour.TwentyOneEightTriples
import Aris4Math.ThirtyFour.TwentyOneEightQuads
import Aris4Math.ThirtyFour.TwentyOneEightGraph
namespace Aris4Math.ThirtyFour.TwentyOneEightStructure
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree threeVertices)
open TwentyOneEightGraph (eights Unit)

theorem triple_residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (f : Fin 3↪Fin 21)
    (degrees : ∀j,H.degree (f j)=8) :
    TwentyOneEightTripleCoverage.Residue (H.codegree (f 0) (f 1)) (H.codegree (f 0) (f 2))
      (H.codegree (f 1) (f 2)) (tripleCodegree H (f 0) (f 1) (f 2)) := by
  apply TwentyOneEightTriples.residual H cover size noB f degrees
  intro i j ne
  exact TwentyOneEightTriples.pair_le_three H size noB (f i) (f j) (f.injective.ne ne) (degrees i) (degrees j)

theorem pair_le_two (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H) :
    ∀x∈eights H,∀y∈eights H,x≠y→H.codegree x y≤2 := by
  apply TwentyOneEightGraph.codegrees_at_most_two H cover (eights H)
    (TwentyOneEightGraph.eights_at_least_nineteen H size minimum)
  · intro x hx y hy xy
    exact TwentyOneEightTriples.pair_le_three H size noB x y xy (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
  · intro x hx y hy z hz xy xz yz three
    have dx:=(Finset.mem_filter.mp hx).2
    have dy:=(Finset.mem_filter.mp hy).2
    have dz:=(Finset.mem_filter.mp hz).2
    have res:=triple_residual H cover size noB (threeVertices x y z xy xz yz) (by
      intro i;fin_cases i <;> assumption)
    exact res.1 (Or.inl three)

theorem triangle_free (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) :
    ∀x∈eights H,∀a∈eights H,∀b∈eights H,Unit H x a→Unit H x b→¬Unit H a b := by
  intro x hx a ha b hb xa xb ab
  have res:=triple_residual H cover size noB (threeVertices x a b xa.1 xb.1 ab.1) (by
    intro i;fin_cases i
    · exact (Finset.mem_filter.mp hx).2
    · exact (Finset.mem_filter.mp ha).2
    · exact (Finset.mem_filter.mp hb).2)
  exact res.2 ⟨xa.2,xb.2,ab.2⟩

theorem quad_residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H)
    (f : Fin 4↪Fin 21) (degrees : ∀j,H.degree (f j)=8) :
    TwentyOneEightQuadCoverage.Residue
      (fun j=>H.codegree (f (ThirtyThree.QuadProfiles.first j)) (f (ThirtyThree.QuadProfiles.second j)))
      (fun j=>ThirtyThree.QuadProfiles.count H f (ThirtyThree.QuadProfiles.highLabels j)) := by
  have member (j) : f j∈eights H := Finset.mem_filter.mpr ⟨Finset.mem_univ _,degrees j⟩
  apply TwentyOneEightQuads.residual H cover size noB f degrees
  · intro i j ne
    exact pair_le_two H cover size minimum noB (f i) (member i) (f j) (member j) (f.injective.ne ne)
  · intro i j k ij ik jk triple
    exact triangle_free H cover size noB (f i) (member i) (f j) (member j) (f k) (member k)
      ⟨f.injective.ne ij,triple.1⟩ ⟨f.injective.ne ik,triple.2.1⟩ ⟨f.injective.ne jk,triple.2.2⟩
end Aris4Math.ThirtyFour.TwentyOneEightStructure
#print axioms Aris4Math.ThirtyFour.TwentyOneEightStructure.pair_le_two
#print axioms Aris4Math.ThirtyFour.TwentyOneEightStructure.quad_residual
