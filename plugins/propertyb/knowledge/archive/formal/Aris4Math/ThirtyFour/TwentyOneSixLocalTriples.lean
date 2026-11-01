import Aris4Math.ThirtyFour.TwentyOneSixTriple666
import Aris4Math.ThirtyFour.TwentyOneSixTriple667
import Aris4Math.ThirtyFour.TwentyOneSixTriple668
import Aris4Math.ThirtyFour.TwentyOneSixTriple677
import Aris4Math.ThirtyFour.TwentyOneSixTriple678
import Aris4Math.ThirtyFour.TwentyOneSixTriple688
import Aris4Math.ThirtyFour.TwentyOneSixPairs
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
namespace Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxHeartbeats 0
set_option maxRecDepth 100000

def Suitable666 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple666Data.Case,
  a=TwentyOneSixTriple666Data.co i 0 ∧ b=TwentyOneSixTriple666Data.co i 1 ∧ c=TwentyOneSixTriple666Data.co i 2 ∧ t=TwentyOneSixTriple666Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable666 a b c t) := by unfold Suitable666;infer_instance

theorem apply666 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=6)
    (h : Suitable666 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple666.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

def Suitable667 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple667Data.Case,
  a=TwentyOneSixTriple667Data.co i 0 ∧ b=TwentyOneSixTriple667Data.co i 1 ∧ c=TwentyOneSixTriple667Data.co i 2 ∧ t=TwentyOneSixTriple667Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable667 a b c t) := by unfold Suitable667;infer_instance

theorem apply667 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=7)
    (h : Suitable667 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple667.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

def Suitable668 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple668Data.Case,
  a=TwentyOneSixTriple668Data.co i 0 ∧ b=TwentyOneSixTriple668Data.co i 1 ∧ c=TwentyOneSixTriple668Data.co i 2 ∧ t=TwentyOneSixTriple668Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable668 a b c t) := by unfold Suitable668;infer_instance

theorem apply668 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=8)
    (h : Suitable668 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple668.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

def Suitable677 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple677Data.Case,
  a=TwentyOneSixTriple677Data.co i 0 ∧ b=TwentyOneSixTriple677Data.co i 1 ∧ c=TwentyOneSixTriple677Data.co i 2 ∧ t=TwentyOneSixTriple677Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable677 a b c t) := by unfold Suitable677;infer_instance

theorem apply677 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=7)
    (h : Suitable677 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple677.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

def Suitable678 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple678Data.Case,
  a=TwentyOneSixTriple678Data.co i 0 ∧ b=TwentyOneSixTriple678Data.co i 1 ∧ c=TwentyOneSixTriple678Data.co i 2 ∧ t=TwentyOneSixTriple678Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable678 a b c t) := by unfold Suitable678;infer_instance

theorem apply678 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=8)
    (h : Suitable678 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple678.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

def Suitable688 (a b c t : ℕ) : Prop := ∃ i : TwentyOneSixTriple688Data.Case,
  a=TwentyOneSixTriple688Data.co i 0 ∧ b=TwentyOneSixTriple688Data.co i 1 ∧ c=TwentyOneSixTriple688Data.co i 2 ∧ t=TwentyOneSixTriple688Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable688 a b c t) := by unfold Suitable688;infer_instance

theorem apply688 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=8) (dz : H.degree z=8)
    (h : Suitable688 (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply TwentyOneSixTriple688.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

theorem coverage666 : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤6 → Suitable666 a.val b.val c.val t.val := by decide +kernel

theorem coverage667 : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤7+t.val → Suitable667 a.val b.val c.val t.val := by decide +kernel

theorem coverage668 : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤8+t.val →
    (a.val=1 ∧ b.val=1 ∧ c.val=1 ∧ t.val=0) ∨
    (a.val=2 ∧ ((b.val=1 ∧ c.val=1 ∧ t.val=0) ∨ (b.val=1 ∧ c.val=2 ∧ t.val=1) ∨ (b.val=2 ∧ c.val=1 ∧ t.val=1))) ∨
    Suitable668 a.val b.val c.val t.val := by decide +kernel

theorem coverage677 : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤6 → a.val+c.val≤7+t.val → b.val+c.val≤7+t.val →
    (a.val=1 ∧ b.val=1 ∧ c.val=2 ∧ t.val=1) ∨
    (a.val=2 ∧ b.val=2 ∧ c.val=1 ∧ t.val=0) ∨ Suitable677 a.val b.val c.val t.val := by decide +kernel

theorem coverage678 : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤6 → a.val+c.val≤7+t.val → b.val+c.val≤8+t.val →
    (a.val≤2 ∧ b.val≤2 ∧ c.val≤2) ∨ Suitable678 a.val b.val c.val t.val := by decide +kernel

theorem coverage688 : ∀ c : Fin 9, ∀ t : Fin 2,
    3≤c.val → 1+c.val≤8+t.val → Suitable688 1 1 c.val t.val := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
