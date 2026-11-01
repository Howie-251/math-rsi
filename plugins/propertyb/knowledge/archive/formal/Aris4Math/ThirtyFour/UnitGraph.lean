import Aris4Math.ThirtyFour.TwentySevenMany

/-! A general graph argument on an actual selected vertex set. No graph enumeration. -/
namespace Aris4Math.ThirtyFour.UnitGraph

variable (S : Finset (Fin 20)) (R : Fin 20 → Fin 20 → Prop) [DecidableRel R]
def neighbors (x : Fin 20) : Finset (Fin 20) := S.filter (R x)

structure Rules : Prop where
  symm : Symmetric R
  irrefl : Irreflexive R
  triangle : ∀ x ∈ S, ∀ a ∈ S, ∀ b ∈ S, R x a → R x b → ¬ R a b
  pathIsolate : ∀ x ∈ S, ∀ a ∈ S, ∀ b ∈ S, ∀ z ∈ S,
    a ≠ b → x ≠ z → a ≠ z → b ≠ z →
    R x a → R x b → ¬ R x z → ¬ R a b → ¬ R a z → ¬ R b z → False
  commonThree : ∀ x ∈ S, ∀ z ∈ S, ∀ a ∈ S, ∀ b ∈ S, ∀ c ∈ S,
    x ≠ z → a ≠ b → a ≠ c → b ≠ c →
    R x a → R x b → R x c → R z a → R z b → R z c → False

variable {S R}

theorem universal_of_three (rules : Rules S R) (x : Fin 20) (hx : x ∈ S)
    (large : 3 ≤ (neighbors S R x).card) : ∀ z ∈ S, x ≠ z → R x z := by
  obtain ⟨f,hf⟩ := TwentySevenMany.exists_indexed_subset (neighbors S R x) large
  let a := f 0
  let b := f 1
  let c := f 2
  have ha : a ∈ S := (Finset.mem_filter.mp (hf 0)).1
  have hb : b ∈ S := (Finset.mem_filter.mp (hf 1)).1
  have hc : c ∈ S := (Finset.mem_filter.mp (hf 2)).1
  have xa : R x a := (Finset.mem_filter.mp (hf 0)).2
  have xb : R x b := (Finset.mem_filter.mp (hf 1)).2
  have xc : R x c := (Finset.mem_filter.mp (hf 2)).2
  have ab : a ≠ b := f.injective.ne (by decide)
  have ac : a ≠ c := f.injective.ne (by decide)
  have bc : b ≠ c := f.injective.ne (by decide)
  have nab := rules.triangle x hx a ha b hb xa xb
  have nac := rules.triangle x hx a ha c hc xa xc
  have nbc := rules.triangle x hx b hb c hc xb xc
  intro z hz xz
  by_contra nxz
  have az : a ≠ z := by intro eq; exact nxz (eq ▸ xa)
  have bz : b ≠ z := by intro eq; exact nxz (eq ▸ xb)
  have cz : c ≠ z := by intro eq; exact nxz (eq ▸ xc)
  have miss (v : Fin 20) (h : ¬ R z v) : ¬ R v z := fun hv => h (rules.symm hv)
  by_cases za : R z a
  · by_cases zb : R z b
    · by_cases zc : R z c
      · exact rules.commonThree x hx z hz a ha b hb c hc xz ab ac bc xa xb xc za zb zc
      · exact rules.pathIsolate z hz a ha b hb c hc ab cz.symm ac bc za zb zc nab nac nbc
    · by_cases zc : R z c
      · exact rules.pathIsolate z hz a ha c hc b hb ac bz.symm ab bc.symm za zc zb nac nab (fun h => nbc (rules.symm h))
      · exact rules.pathIsolate x hx b hb c hc z hz bc xz bz cz xb xc nxz nbc (miss b zb) (miss c zc)
  · by_cases zb : R z b
    · by_cases zc : R z c
      · exact rules.pathIsolate z hz b hb c hc a ha bc az.symm ab.symm ac.symm zb zc za nbc
          (fun h => nab (rules.symm h)) (fun h => nac (rules.symm h))
      · exact rules.pathIsolate x hx a ha c hc z hz ac xz az cz xa xc nxz nac (miss a za) (miss c zc)
    · exact rules.pathIsolate x hx a ha b hb z hz ab xz az bz xa xb nxz nab (miss a za) (miss b zb)

/-- On at least six vertices these forbidden local configurations force a
universal vertex or unit degree at most one everywhere. -/
theorem dichotomy (rules : Rules S R) (large : 6 ≤ S.card) :
    (∃ x ∈ S, ∀ y ∈ S, x ≠ y → R x y) ∨
    (∀ x ∈ S, (neighbors S R x).card ≤ 1) := by
  classical
  by_cases universal : ∃ x ∈ S, ∀ y ∈ S, x ≠ y → R x y
  · exact Or.inl universal
  right
  have atMostTwo (x : Fin 20) (hx : x ∈ S) : (neighbors S R x).card ≤ 2 := by
    by_contra hn
    exact universal ⟨x,hx,universal_of_three rules x hx (by omega)⟩
  intro b hb
  by_contra hn
  have two : (neighbors S R b).card=2 := by have := atMostTwo b hb; omega
  obtain ⟨a,c,ac,Nb⟩ := Finset.card_eq_two.mp two
  have amem : a ∈ neighbors S R b := by simp [Nb]
  have cmem : c ∈ neighbors S R b := by simp [Nb]
  obtain ⟨ha,ba⟩ := Finset.mem_filter.mp amem
  obtain ⟨hc,bc⟩ := Finset.mem_filter.mp cmem
  have baNe : b ≠ a := by intro eq; subst a; exact rules.irrefl b ba
  have bcNe : b ≠ c := by intro eq; subst c; exact rules.irrefl b bc
  have nac := rules.triangle b hb a ha c hc ba bc
  let A := (neighbors S R a).erase b
  let C := (neighbors S R c).erase b
  have bA : b ∈ neighbors S R a := Finset.mem_filter.mpr ⟨hb,rules.symm ba⟩
  have bC : b ∈ neighbors S R c := Finset.mem_filter.mpr ⟨hb,rules.symm bc⟩
  have smallA : A.card ≤ 1 := by
    have bound := atMostTwo a ha
    simp only [A,Finset.card_erase_of_mem bA]
    omega
  have smallC : C.card ≤ 1 := by
    have bound := atMostTwo c hc
    simp only [C,Finset.card_erase_of_mem bC]
    omega
  have sub : S ⊆ {a,b,c} ∪ (A ∪ C) := by
    intro z hz
    by_cases za : z=a
    · simp [za]
    by_cases zb : z=b
    · simp [zb]
    by_cases zc : z=c
    · simp [zc]
    have nbz : ¬ R b z := by
      intro h
      have mem : z ∈ neighbors S R b := Finset.mem_filter.mpr ⟨hz,h⟩
      simp only [Nb,Finset.mem_insert,Finset.mem_singleton] at mem
      exact mem.elim za zc
    by_cases az : R a z
    · exact Finset.mem_union_right _ (Finset.mem_union_left _ (Finset.mem_erase.mpr ⟨zb,Finset.mem_filter.mpr ⟨hz,az⟩⟩))
    by_cases cz : R c z
    · exact Finset.mem_union_right _ (Finset.mem_union_right _ (Finset.mem_erase.mpr ⟨zb,Finset.mem_filter.mpr ⟨hz,cz⟩⟩))
    exact False.elim (rules.pathIsolate b hb a ha c hc z hz ac (Ne.symm zb) (Ne.symm za) (Ne.symm zc) ba bc nbz nac az cz)
  have bound := Finset.card_le_card sub
  have union1 := Finset.card_union_le ({a,b,c} : Finset (Fin 20)) (A ∪ C)
  have union2 := Finset.card_union_le A C
  have triple : ({a,b,c} : Finset (Fin 20)).card ≤ 3 := by
    have ins1 := Finset.card_insert_le a ({b,c} : Finset (Fin 20))
    have ins2 := Finset.card_insert_le b ({c} : Finset (Fin 20))
    simp only [Finset.card_singleton] at ins2
    omega
  omega
end Aris4Math.ThirtyFour.UnitGraph
