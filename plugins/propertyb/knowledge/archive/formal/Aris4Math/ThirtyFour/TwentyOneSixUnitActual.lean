import Aris4Math.ThirtyFour.TwentyOneSixStructure
import Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneSixUnitSet

/-! Obtain the degree-six unit-neighbor structure directly from an actual
hypergraph. The pair bounds and every local residual premise are derived here
before applying the finite-set structure theorem. -/

namespace Aris4Math.ThirtyFour.TwentyOneSixUnitActual

open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyOneSixStructure (unit_eight_pair)
open Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
  (co6888 Residue6888 actual6888)
open Aris4Math.ThirtyFour.TwentyOneSixUnitSet (TripleResidue)

/-- The actual (6,8,8,8) classification supplies both finite-set obligations
for an arbitrary ordered triple of distinct unit neighbors of x. -/
theorem residual_on_three (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (noB : ¬ PropertyB H)
    (x a b c : Fin 21) (xa : x ≠ a) (xb : x ≠ b) (xc : x ≠ c)
    (ab : a ≠ b) (ac : a ≠ c) (bc : b ≠ c)
    (dx : H.degree x=6) (da : H.degree a=8)
    (db : H.degree b=8) (dc : H.degree c=8)
    (ua : H.codegree x a=1) (ub : H.codegree x b=1) (uc : H.codegree x c=1) :
    TripleResidue H x a b c ∧
    (∀ e ∈ H.edges, x ∈ e → a ∈ e → b ∈ e → c ∈ e → False) := by
  have ab1 := H.one_le_codegree cover ab
  have ac1 := H.one_le_codegree cover ac
  have bc1 := H.one_le_codegree cover bc
  have ab2 := unit_eight_pair H cover size noB x a b xa xb ab dx da db ua ub
  have ac2 := unit_eight_pair H cover size noB x a c xa xc ac dx da dc ua uc
  have bc2 := unit_eight_pair H cover size noB x b c xb xc bc dx db dc ub uc
  let i : Fin 2 := ⟨H.codegree a b-1,by omega⟩
  let j : Fin 2 := ⟨H.codegree a c-1,by omega⟩
  let k : Fin 2 := ⟨H.codegree b c-1,by omega⟩
  have hi : i.val+1=H.codegree a b := by dsimp [i]; omega
  have hj : j.val+1=H.codegree a c := by dsimp [j]; omega
  have hk : k.val+1=H.codegree b c := by dsimp [k]; omega
  let f := fourVertices x a b c xa xb xc ab ac bc
  have hd : ∀ t, H.degree (f t)=TwentyOneSixQuad6888Data.degree t := by
    intro t
    fin_cases t <;> simp [f,fourVertices,TwentyOneSixQuad6888Data.degree,dx,da,db,dc]
  have hc : ∀ t, H.codegree (f (first t)) (f (second t))=
      co6888 (i.val+1) (j.val+1) (k.val+1) t := by
    intro t
    fin_cases t <;> simp [f,fourVertices,first,second,co6888,ua,ub,uc,hi,hj,hk]
  have raw := actual6888 H size noB f i j k hd hc (by trivial)
  have result : count H f (highLabels 4)=0 ∧
      ((H.codegree a b=2 ∧ H.codegree a c=2 ∧ H.codegree b c=2) ∨
        (H.codegree a b+H.codegree a c+H.codegree b c=4 ∧
          ∀ t, count H f (highLabels t)=0)) := by
    simpa [Residue6888,co6888,hi,hj,hk] using raw
  constructor
  · rcases result.2 with allTwo | sumFour
    · exact Or.inl allTwo
    · refine Or.inr ⟨sumFour.1,?_⟩
      have triple := QuadIncidence.triple_count H f 0
      change tripleCodegree H x a b=count H f (highLabels 0)+count H f (highLabels 4)
        at triple
      rw [triple,sumFour.2 0,sumFour.2 4]
  · intro e he xe ae be ce
    have positive := TwentyOneFiveLocal.common_quad H f e he (by
      intro t; fin_cases t <;> simp [f,fourVertices,xe,ae,be,ce])
    have zero := result.1
    omega

/-- An actual large set of degree-eight unit neighbors of a six-degree vertex
has all pair codegrees two and capacity two on every edge through that vertex. -/
theorem unit_set_structure_of_not_propertyB (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (noB : ¬ PropertyB H)
    (x : Fin 21) (dx : H.degree x=6) (U : Finset (Fin 21)) (large : 7 ≤ U.card)
    (degrees : ∀ u ∈ U, H.degree u=8) (unit : ∀ u ∈ U, H.codegree x u=1) :
    (∀ a ∈ U, ∀ b ∈ U, a ≠ b → H.codegree a b=2) ∧
    (∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 2) := by
  have apart (u : Fin 21) (hu : u ∈ U) : x ≠ u := by
    intro eq
    have du := degrees u hu
    rw [eq] at dx
    omega
  have pairs : ∀ a ∈ U, ∀ b ∈ U, a ≠ b →
      H.codegree a b=1 ∨ H.codegree a b=2 := by
    intro a ha b hb ab
    have lower := H.one_le_codegree cover ab
    have upper := unit_eight_pair H cover size noB x a b (apart a ha) (apart b hb) ab
      dx (degrees a ha) (degrees b hb) (unit a ha) (unit b hb)
    omega
  have triple (a : Fin 21) (ha : a ∈ U) (b : Fin 21) (hb : b ∈ U)
      (c : Fin 21) (hc : c ∈ U) (ab : a ≠ b) (ac : a ≠ c) (bc : b ≠ c) :=
    residual_on_three H cover size noB x a b c (apart a ha) (apart b hb) (apart c hc)
      ab ac bc dx (degrees a ha) (degrees b hb) (degrees c hc)
      (unit a ha) (unit b hb) (unit c hc)
  exact TwentyOneSixUnitSet.unit_set_structure H x U dx large unit pairs
    (fun a ha b hb c hc ab ac bc => (triple a ha b hb c hc ab ac bc).1)
    (fun a ha b hb c hc ab ac bc => (triple a ha b hb c hc ab ac bc).2)

end Aris4Math.ThirtyFour.TwentyOneSixUnitActual

#print axioms Aris4Math.ThirtyFour.TwentyOneSixUnitActual.residual_on_three
#print axioms Aris4Math.ThirtyFour.TwentyOneSixUnitActual.unit_set_structure_of_not_propertyB
