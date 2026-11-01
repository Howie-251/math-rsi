import Mathlib.Data.Finset.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.EquivFin

namespace Aris4Math.General.RS

universe u

def Uniform {V : Type u} (E : Finset (Finset V)) (k : ℕ) : Prop :=
  ∀ e ∈ E, e.card = k

def Mono {V : Type u} (e : Finset V) (c : V → Bool) (q : Bool) : Prop :=
  ∀ x ∈ e, c x = q

def Bichromatic {V : Type u} (E : Finset (Finset V)) (c : V → Bool) : Prop :=
  ∀ e ∈ E, (∃ x ∈ e, c x = true) ∧ (∃ x ∈ e, c x = false)

def PropertyB {V : Type u} (E : Finset (Finset V)) : Prop :=
  ∃ c : V → Bool, Bichromatic E c

noncomputable def singlePairs {V : Type u} (E : Finset (Finset V)) :
    Finset (Finset V × Finset V) := by
  classical
  exact (E ×ˢ E).filter (fun ef => ef.1 ≠ ef.2 ∧ (ef.1 ∩ ef.2).card = 1)

noncomputable def gamma {V : Type u} (E : Finset (Finset V)) : ℕ :=
  (singlePairs E).card

def PilotTarget : Prop :=
  ∀ (V : Type u) [Finite V] (E : Finset (Finset V)),
    Uniform E 17 → E.card ≤ 2 ^ 17 → PropertyB E

end Aris4Math.General.RS
