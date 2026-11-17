import Std
import Lean.Elab.Tactic.Omega

/-!
Primitive ordered-color interface for the balanced49 port.
The chain-closure proof implements the main-authored argument in
BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md, section 2.2.
No geometry, finite certificate, or capacity conclusion is assumed here.
-/
namespace Balanced49Abstract

/-- Exactly the four-bit patterns having at most one switch. -/
def Packet4 (a b c d : Bool) : Prop :=
  (a = b ∧ b = c) ∨ (a = b ∧ c = d) ∨ (b = c ∧ c = d)

def switches (a b c d : Bool) : Nat :=
  (if a = b then 0 else 1) + (if b = c then 0 else 1) + (if c = d then 0 else 1)

theorem packet_iff_switches (a b c d : Bool) : Packet4 a b c d ↔ switches a b c d ≤ 1 := by
  cases a <;> cases b <;> cases c <;> cases d <;> decide

/-- The eight forbidden source words, in ES7OrderedContract.packetBits order. -/
def packetBits : List (Bool × Bool × Bool × Bool) :=
  [(false, true, false, false), (false, true, false, true),
   (false, true, true, false), (true, false, false, true),
   (true, false, true, false), (true, false, true, true),
   (false, false, true, false), (true, true, false, true)]

/-- Each row is exactly the disjunction excluding its four-bit forbidden word. -/
def packetCnf (a b c d : Bool) : Bool := packetBits.all fun bad =>
  (!(a == bad.1)) || (!(b == bad.2.1)) || (!(c == bad.2.2.1)) || (!(d == bad.2.2.2))

theorem packet_cnf_iff (a b c d : Bool) : Packet4 a b c d ↔ packetCnf a b c d = true := by
  cases a <;> cases b <;> cases c <;> cases d <;> decide

theorem packet_endpoints {a b c d : Bool} (h : Packet4 a b c d)
    (ends : a = d) : b = a ∧ c = a := by
  cases h with
  | inl h => exact ⟨h.1.symm, h.2.symm.trans h.1.symm⟩
  | inr h =>
    cases h with
    | inl h => exact ⟨h.1.symm, h.2.trans ends.symm⟩
    | inr h => exact ⟨h.1.trans (h.2.trans ends.symm), h.2.trans ends.symm⟩

/-- Values outside increasing triples are irrelevant; no real-point fields. -/
structure Configuration (n : Nat) where
  cup : Nat → Nat → Nat → Bool
  packet : ∀ a b c d, a < b → b < c → c < d → d < n →
    Packet4 (cup a b c) (cup a b d) (cup a c d) (cup b c d)

theorem packet_source_sound {n : Nat} (c : Configuration n)
    (a b d e : Nat) (ab : a < b) (bd : b < d) (de : d < e) (en : e < n) :
    packetCnf (c.cup a b d) (c.cup a b e) (c.cup a d e) (c.cup b d e) = true :=
  (packet_cnf_iff _ _ _ _).mp (c.packet a b d e ab bd de en)

/-- Actual increasing vertices, with only consecutive triples constrained. -/
structure Path {n : Nat} (c : Configuration n) (color : Bool) (m : Nat) where
  vertex : Nat → Nat
  ordered : ∀ i j, i < j → j < m → vertex i < vertex j
  bounded : ∀ i, i < m → vertex i < n
  consecutive : ∀ i, i + 2 < m →
    c.cup (vertex i) (vertex (i + 1)) (vertex (i + 2)) = color

theorem chain_all {n : Nat} (c : Configuration n) (color : Bool)
    (m : Nat) (v : Nat → Nat)
    (ordered : ∀ i j, i < j → j < m → v i < v j)
    (bounded : ∀ i, i < m → v i < n)
    (steps : ∀ i, i + 2 < m → c.cup (v i) (v (i + 1)) (v (i + 2)) = color) :
    ∀ i j k, i < j → j < k → k < m → c.cup (v i) (v j) (v k) = color := by
  induction m with
  | zero => intro i j k ij jk km; omega
  | succ m ih =>
    have previous := ih
      (fun i j ij jm => ordered i j ij (by omega))
      (fun i im => bounded i (by omega))
      (fun i im => steps i (by omega))
    intro i j k ij jk km
    by_cases old : k < m
    · exact previous i j k ij jk old
    · have keq : k = m := by omega
      subst k
      have mlarge : 2 ≤ m := by omega
      have finalStep : c.cup (v (m - 2)) (v (m - 1)) (v m) = color := by
        have h := steps (m - 2) (by omega)
        have e1 : m - 2 + 1 = m - 1 := by omega
        have e2 : m - 2 + 2 = m := by omega
        simpa only [e1, e2] using h
      have penultimate : ∀ a, a < m - 1 →
          c.cup (v a) (v (m - 1)) (v m) = color := by
        intro a am
        by_cases last : a = m - 2
        · simpa only [last] using finalStep
        · have aearly : a < m - 2 := by omega
          have first := previous a (m - 2) (m - 1) aearly (by omega) (by omega)
          have packet := c.packet (v a) (v (m - 2)) (v (m - 1)) (v m)
            (ordered a (m - 2) aearly (by omega))
            (ordered (m - 2) (m - 1) (by omega) (by omega))
            (ordered (m - 1) m (by omega) (by omega)) (bounded m (by omega))
          exact (packet_endpoints packet (first.trans finalStep.symm)).2.trans first
      by_cases jlast : j = m - 1
      · subst j
        exact penultimate i ij
      · have jearly : j < m - 1 := by omega
        have first := previous i j (m - 1) ij jearly (by omega)
        have last := penultimate j jearly
        have packet := c.packet (v i) (v j) (v (m - 1)) (v m)
          (ordered i j ij (by omega))
          (ordered j (m - 1) jearly (by omega))
          (ordered (m - 1) m (by omega) (by omega)) (bounded m (by omega))
        exact (packet_endpoints packet (first.trans last.symm)).1.trans first

theorem Path.allTriples {n m : Nat} {c : Configuration n} {color : Bool}
    (p : Path c color m) :
    ∀ i j k, i < j → j < k → k < m →
      c.cup (p.vertex i) (p.vertex j) (p.vertex k) = color :=
  chain_all c color m p.vertex p.ordered p.bounded p.consecutive

/-- A selected subsequence retains its actual vertices and every triple color. -/
def Path.subsequence {n m : Nat} {c : Configuration n} {color : Bool}
    (p : Path c color m) (k : Nat) (index : Nat → Nat)
    (ordered : ∀ i j, i < j → j < k → index i < index j)
    (bounded : ∀ i, i < k → index i < m) : Path c color k where
  vertex i := p.vertex (index i)
  ordered i j ij jk := p.ordered _ _ (ordered i j ij jk) (bounded j jk)
  bounded i ik := p.bounded _ (bounded i ik)
  consecutive i ik := p.allTriples _ _ _
    (ordered i (i + 1) (by omega) (by omega))
    (ordered (i + 1) (i + 2) (by omega) ik) (bounded (i + 2) ik)

/-- Pullback along an actual increasing selection. Ambient colors are retained. -/
def Configuration.select {n : Nat} (c : Configuration n) (m : Nat) (f : Nat → Nat)
    (ordered : ∀ i j, i < j → j < m → f i < f j)
    (bounded : ∀ i, i < m → f i < n) : Configuration m where
  cup i j k := c.cup (f i) (f j) (f k)
  packet a b d e ab bd de em := c.packet _ _ _ _
    (ordered a b ab (by omega)) (ordered b d bd (by omega))
    (ordered d e de em) (bounded e em)

/-- Every selected path is an actual ambient path with the same endpoints. -/
def Path.toAmbient {n m k : Nat} {c : Configuration n} {color : Bool}
    (f : Nat → Nat)
    (ordered : ∀ i j, i < j → j < m → f i < f j)
    (bounded : ∀ i, i < m → f i < n)
    (p : Path (c.select m f ordered bounded) color k) : Path c color k where
  vertex i := f (p.vertex i)
  ordered i j ij jk := ordered _ _ (p.ordered i j ij jk) (p.bounded j jk)
  bounded i ik := bounded _ (p.bounded i ik)
  consecutive := p.consecutive

def NoSix {n : Nat} (c : Configuration n) : Prop :=
  ∀ color : Bool, ¬ Nonempty (Path c color 6)

/-- No interior-disjointness assumption: the two paths share actual endpoints. -/
def NoWeak7 {n : Nat} (c : Configuration n) : Prop :=
  ∀ a b, 2 ≤ a → 2 ≤ b → a + b = 9 →
    ∀ (red : Path c true a) (blue : Path c false b),
      red.vertex 0 = blue.vertex 0 →
      red.vertex (a - 1) = blue.vertex (b - 1) → False

/-- Prohibitions are explicit hypotheses on the same complete coloring. -/
structure BalancedInput (n : Nat) where
  configuration : Configuration n
  noSix : NoSix configuration
  noWeak7 : NoWeak7 configuration

def BalancedInput.select {n : Nat} (input : BalancedInput n) (m : Nat) (f : Nat → Nat)
    (ordered : ∀ i j, i < j → j < m → f i < f j)
    (bounded : ∀ i, i < m → f i < n) : BalancedInput m where
  configuration := input.configuration.select m f ordered bounded
  noSix := by
    intro color witness
    cases witness with
    | intro p => exact input.noSix color ⟨p.toAmbient f ordered bounded⟩
  noWeak7 := by
    intro a b ha hb total red blue sameStart sameEnd
    exact input.noWeak7 a b ha hb total
      (red.toAmbient f ordered bounded) (blue.toAmbient f ordered bounded)
      (congrArg f sameStart) (congrArg f sameEnd)

#print axioms packet_iff_switches
#print axioms packet_source_sound
#print axioms packet_endpoints
#print axioms chain_all
#print axioms Path.allTriples
#print axioms BalancedInput.select
end Balanced49Abstract
