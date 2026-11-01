import Mathlib.Data.Finset.Max
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Lean.Elab.Tactic.Omega

/-! The analytic graph obstruction behind the one-low 23-point branch.
No graph is enumerated: a maximum independent set covers the vertex set by
closed neighborhoods, and absence of an induced three-vertex path makes each
of those neighborhoods a clique. The two four-point exclusions bound both
the number of representatives and each neighborhood by three. -/

namespace Aris4Math.ThirtyFour.FiveVertexClusterBound

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

def HasFour (P : V → V → Prop) : Prop :=
  ∃ f : Fin 4 → V, Function.Injective f ∧ ∀ i j, i ≠ j → P (f i) (f j)

def HasInducedP3 (R : V → V → Prop) : Prop :=
  ∃ a b c, a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ R a b ∧ R b c ∧ ¬ R a c

def Independent (R : V → V → Prop) (S : Finset V) : Prop :=
  ∀ a ∈ S, ∀ b ∈ S, a ≠ b → ¬ R a b

def cluster (R : V → V → Prop) [DecidableRel R] (a : V) : Finset V :=
  Finset.univ.filter fun x => x=a ∨ R a x

/-- Four distinct members of a pairwise-P set give an indexed four-point
pattern. This is just finite subset selection, with no enumeration of graphs. -/
theorem card_le_three_of_no_four (P : V → V → Prop) (forbidden : ¬ HasFour P)
    (S : Finset V) (pairs : ∀ a ∈ S, ∀ b ∈ S, a ≠ b → P a b) : S.card ≤ 3 := by
  classical
  by_contra high
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq (show 4 ≤ S.card by omega)
  let e : ↥T ≃ Fin 4 := Fintype.equivFinOfCardEq (by simpa using card)
  let f : Fin 4 → V := fun i => (e.symm i).val
  have inj : Function.Injective f := Subtype.val_injective.comp e.symm.injective
  apply forbidden
  refine ⟨f,inj,?_⟩
  intro i j ij
  exact pairs (f i) (sub (e.symm i).property) (f j) (sub (e.symm j).property) (inj.ne ij)

/-- In a simple graph with no induced P3, each closed neighborhood is a
clique. In particular a four-clique exclusion bounds its size by three. -/
theorem cluster_card_le_three (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ a b, R a b → R b a) (irreflexive : ∀ a, ¬ R a a)
    (noPath : ¬ HasInducedP3 R) (noClique : ¬ HasFour R) (a : V) :
    (cluster R a).card ≤ 3 := by
  have trans (x y z : V) (xy : R x y) (yz : R y z) (xz : x ≠ z) : R x z := by
    by_contra notRelated
    have xne : x ≠ y := by intro eq; subst y; exact irreflexive x xy
    have yne : y ≠ z := by intro eq; subst z; exact irreflexive y yz
    exact noPath ⟨x,y,z,xne,xz,yne,xy,yz,notRelated⟩
  apply card_le_three_of_no_four R noClique (cluster R a)
  intro x hx y hy xy
  obtain ⟨_,hx⟩ := Finset.mem_filter.mp hx
  obtain ⟨_,hy⟩ := Finset.mem_filter.mp hy
  rcases hx with hx | ax
  · subst x
    rcases hy with hy | ay
    · exact False.elim (xy hy.symm)
    · exact ay
  · rcases hy with hy | ay
    · subst y
      exact symmetric a x ax
    · exact trans x a y (symmetric a x ax) ay xy

/-- The absence of the three forbidden induced patterns bounds the whole
finite vertex domain, not merely one selected five-vertex graph. -/
theorem card_le_nine (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ a b, R a b → R b a) (irreflexive : ∀ a, ¬ R a a)
    (noPath : ¬ HasInducedP3 R) (noClique : ¬ HasFour R)
    (noIndependent : ¬ HasFour (fun a b => ¬ R a b)) : Fintype.card V ≤ 9 := by
  classical
  let candidates := (Finset.univ : Finset V).powerset.filter (Independent R)
  have empty : (∅ : Finset V) ∈ candidates := by
    simp [candidates,Independent]
  obtain ⟨I,hI,maximal⟩ := candidates.exists_max_image Finset.card ⟨∅,empty⟩
  have independent : Independent R I := (Finset.mem_filter.mp hI).2
  have ismall : I.card ≤ 3 :=
    card_le_three_of_no_four (fun a b => ¬ R a b) noIndependent I independent
  have covers : ∀ x : V, ∃ a ∈ I, x=a ∨ R a x := by
    intro x
    by_contra no
    have outside (a : V) (ha : a ∈ I) : x ≠ a ∧ ¬ R a x := by
      constructor
      · intro eq
        exact no ⟨a,ha,Or.inl eq⟩
      · intro related
        exact no ⟨a,ha,Or.inr related⟩
    have notMem : x ∉ I := by
      intro hx
      exact (outside x hx).1 rfl
    have enlarged : Independent R (insert x I) := by
      intro a ha b hb ab
      rcases Finset.mem_insert.mp ha with ha | ha
      · subst a
        rcases Finset.mem_insert.mp hb with hb | hb
        · exact False.elim (ab hb.symm)
        · intro related
          exact (outside b hb).2 (symmetric x b related)
      · rcases Finset.mem_insert.mp hb with hb | hb
        · subst b
          exact (outside a ha).2
        · exact independent a ha b hb ab
    have candidate : insert x I ∈ candidates := by
      apply Finset.mem_filter.mpr
      exact ⟨Finset.mem_powerset.mpr (Finset.subset_univ _),enlarged⟩
    have comparison := maximal (insert x I) candidate
    rw [Finset.card_insert_of_notMem notMem] at comparison
    omega
  have union : I.biUnion (cluster R) = Finset.univ := by
    ext x
    constructor
    · intro _
      exact Finset.mem_univ x
    · intro _
      obtain ⟨a,ha,related⟩ := covers x
      exact Finset.mem_biUnion.mpr ⟨a,ha,Finset.mem_filter.mpr ⟨Finset.mem_univ x,related⟩⟩
  have bound : Fintype.card V ≤ I.card*3 := by
    calc
      _ = (I.biUnion (cluster R)).card := by rw [union,Finset.card_univ]
      _ ≤ ∑ a ∈ I, (cluster R a).card := Finset.card_biUnion_le
      _ ≤ ∑ _a ∈ I, (3 : ℕ) := Finset.sum_le_sum
        (fun a _ => cluster_card_le_three R symmetric irreflexive noPath noClique a)
      _ = I.card*3 := by simp
  omega

/-- A domain of at least ten vertices supplies one of the three concrete
patterns excluded by the five-vertex residual graph classification. -/
theorem exists_forbidden_of_ten (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ a b, R a b → R b a) (irreflexive : ∀ a, ¬ R a a)
    (many : 10 ≤ Fintype.card V) :
    HasInducedP3 R ∨ HasFour R ∨ HasFour (fun a b => ¬ R a b) := by
  classical
  by_cases path : HasInducedP3 R
  · exact Or.inl path
  by_cases clique : HasFour R
  · exact Or.inr (Or.inl clique)
  by_cases independent : HasFour (fun a b => ¬ R a b)
  · exact Or.inr (Or.inr independent)
  have bound := card_le_nine R symmetric irreflexive path clique independent
  omega

end Aris4Math.ThirtyFour.FiveVertexClusterBound

#print axioms Aris4Math.ThirtyFour.FiveVertexClusterBound.card_le_nine
#print axioms Aris4Math.ThirtyFour.FiveVertexClusterBound.exists_forbidden_of_ten
