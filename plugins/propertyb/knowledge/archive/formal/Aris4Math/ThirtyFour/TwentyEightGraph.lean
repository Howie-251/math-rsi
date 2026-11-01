import Aris4Math.ThirtyFour.TwentyEightLocal
import Aris4Math.ThirtyFour.UnitGraph

namespace Aris4Math.ThirtyFour.TwentyEightGraph
open Aris4Math.ThirtyThree.QuadProfiles (first second count highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyStructure

def Unit (H : Simple5Hypergraph (Fin 20)) (x y : Fin 20) : Prop := x ≠ y ∧ H.codegree x y=1
instance (H : Simple5Hypergraph (Fin 20)) : DecidableRel (Unit H) := fun x y => by unfold Unit; infer_instance

theorem unit_symm (H : Simple5Hypergraph (Fin 20)) : Symmetric (Unit H) := by
  intro x y h
  exact ⟨h.1.symm,by rw [H.codegree_comm]; exact h.2⟩
theorem unit_irrefl (H : Simple5Hypergraph (Fin 20)) : Irreflexive (Unit H) := fun x h => h.1 rfl

variable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
  (size : H.edges.card=34) (noB : ¬ PropertyB H) (minimum : ∀ x, 8 ≤ H.degree x)
include cover size noB minimum

theorem four (x a b c : Fin 20) (hx : x ∈ eights H) (ha : a ∈ eights H)
    (hb : b ∈ eights H) (hc : c ∈ eights H)
    (xa : x ≠ a) (xb : x ≠ b) (xc : x ≠ c) (ab : a ≠ b) (ac : a ≠ c) (bc : b ≠ c) :
    TwentyEightFacts.GraphFacts
      (fun j => H.codegree (fourVertices x a b c xa xb xc ab ac bc (first j))
        (fourVertices x a b c xa xb xc ab ac bc (second j)))
      (count H (fourVertices x a b c xa xb xc ab ac bc) (highLabels 4)) := by
  apply TwentyEightLocal.graph_facts H cover size noB minimum
  intro j; fin_cases j <;> simp [fourVertices,hx,ha,hb,hc]

theorem triangle (x a b : Fin 20) (hx : x ∈ eights H) (ha : a ∈ eights H) (hb : b ∈ eights H)
    (xa : Unit H x a) (xb : Unit H x b) : ¬ Unit H a b := by
  intro ab
  have large := eights_at_least_ten H size minimum
  obtain ⟨c,hc,cx,ca,cb⟩ := exists_fourth (eights H) (by omega) x a b
  have facts := four H cover size noB minimum x a b c hx ha hb hc xa.1 xb.1 cx.symm ab.1 ca.symm cb.symm
  exact facts.1 xa.2 xb.2 ab.2

theorem pair_two (x y : Fin 20) (hx : x ∈ eights H) (hy : y ∈ eights H) (xy : x ≠ y)
    (notUnit : ¬ Unit H x y) : H.codegree x y=2 := by
  have lower := H.one_le_codegree cover xy
  have upper := TwentyEightLocal.all_codegrees_le_two H cover size noB minimum x y hx hy xy
  have notOne : H.codegree x y ≠ 1 := fun h => notUnit ⟨xy,h⟩
  omega

theorem cycle_edge (x a z b : Fin 20) (hx : x ∈ eights H) (ha : a ∈ eights H)
    (hz : z ∈ eights H) (hb : b ∈ eights H) (xz : x ≠ z) (ab : a ≠ b)
    (xa : Unit H x a) (xb : Unit H x b) (za : Unit H z a) (zb : Unit H z b) :
    ∃ e ∈ H.edges, x ∈ e ∧ a ∈ e ∧ z ∈ e ∧ b ∈ e := by
  have xz2 := pair_two H cover size noB minimum x z hx hz xz
    (triangle H cover size noB minimum a x z ha hx hz (unit_symm H xa) (unit_symm H za))
  have ab2 := pair_two H cover size noB minimum a b ha hb ab
    (triangle H cover size noB minimum x a b hx ha hb xa xb)
  let f := fourVertices x a z b xa.1 xz xb.1 za.1.symm ab zb.1
  have facts := four H cover size noB minimum x a z b hx ha hz hb xa.1 xz xb.1 za.1.symm ab zb.1
  have az1 : H.codegree a z=1 := (unit_symm H za).2
  have q1 : count H f (highLabels 4)=1 := facts.2.2.2.1 xa.2 xz2 xb.2 az1 ab2 zb.2
  obtain ⟨e,he,all⟩ := (TwentyEightLocal.common_quad_iff H f).mpr (by omega)
  exact ⟨e,he,all 0,all 1,all 2,all 3⟩

theorem rules : UnitGraph.Rules (eights H) (Unit H) := by
  refine ⟨unit_symm H,unit_irrefl H,?_,?_,?_⟩
  · intro x hx a ha b hb
    exact triangle H cover size noB minimum x a b hx ha hb
  · intro x hx a ha b hb z hz ab xz az bz xa xb nxz nab naz nbz
    have facts := four H cover size noB minimum x a b z hx ha hb hz xa.1 xb.1 xz ab az bz
    exact facts.2.2.1 xa.2 xb.2
      (pair_two H cover size noB minimum x z hx hz xz nxz)
      (pair_two H cover size noB minimum a b ha hb ab nab)
      (pair_two H cover size noB minimum a z ha hz az naz)
      (pair_two H cover size noB minimum b z hb hz bz nbz)
  · intro x hx z hz a ha b hb c hc xz ab ac bc xa xb xc za zb zc
    obtain ⟨e,he,hxe,hae,hze,hbe⟩ := cycle_edge H cover size noB minimum x a z b hx ha hz hb xz ab xa xb za zb
    obtain ⟨f,hf,hxf,haf,hzf,hcf⟩ := cycle_edge H cover size noB minimum x a z c hx ha hz hc xz ac xa xc za zc
    have same := TwentyEightLocal.edge_eq_of_unit H x a xa.2 e f he hf hxe hae hxf haf
    subst f
    let vertices := fourVertices x a b c xa.1 xb.1 xc.1 ab ac bc
    have facts := four H cover size noB minimum x a b c hx ha hb hc xa.1 xb.1 xc.1 ab ac bc
    have zero : count H vertices (highLabels 4)=0 := facts.2.2.2.2.1 xa.2 xb.2 xc.2
    have positive : 1 ≤ count H vertices (highLabels 4) :=
      (TwentyEightLocal.common_quad_iff H vertices).mp ⟨e,he,by intro j; fin_cases j <;> simp [vertices,fourVertices,hxe,hae,hbe,hcf]⟩
    omega
end Aris4Math.ThirtyFour.TwentyEightGraph
