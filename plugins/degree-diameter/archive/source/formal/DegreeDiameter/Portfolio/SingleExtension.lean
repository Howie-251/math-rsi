import Mathlib.Combinatorics.SimpleGraph.Walk

/-!
A construction lemma for the new (12,5) candidate only.
This module does not import the paused D=2 development.
The diameter premise below is explicit and remains to be proved for the actual
42342-vertex source; no theorem about that source is postulated here.
-/
namespace DegreeDiameter.Portfolio

open SimpleGraph

/-- Every ordered vertex pair has a genuine graph walk of length at most `D`.
The zero-length walk covers equal vertices. -/
def DiameterAtMost {V : Type*} (G : SimpleGraph V) (D : Nat) : Prop :=
  ∀ u v, ∃ p : G.Walk u v, p.length ≤ D

/-- The actual single-vertex extension on `Option V`; `none` is the new vertex. -/
def singleVertexExtension {V : Type*} (G : SimpleGraph V) (pins : Set V) :
    SimpleGraph (Option V) where
  Adj
    | some u, some v => G.Adj u v
    | none, some v => v ∈ pins
    | some u, none => u ∈ pins
    | none, none => False
  symm := by
    intro a b h
    cases a with
    | none => cases b with
      | none => exact h
      | some v => exact h
    | some u => cases b with
      | none => exact h
      | some v => exact G.symm h
  loopless := by
    intro a h
    cases a with
    | none => exact h
    | some u => exact G.loopless u h

/-- All old edges are retained, with `some` as their vertex embedding. -/
def oldVertexHom {V : Type*} (G : SimpleGraph V) (pins : Set V) :
    G →g singleVertexExtension G pins where
  toFun := some
  map_rel' := by intro u v h; exact h

/-- The pins R4-cover every old vertex, using actual walks in the old graph. -/
def PinsCoverRadius {V : Type*} (G : SimpleGraph V) (pins : Set V) (r : Nat) : Prop :=
  ∀ v, ∃ u ∈ pins, ∃ p : G.Walk u v, p.length ≤ r

/-- Conditional construction theorem: old diameter D plus pin-radius r gives
extension diameter at most `max D (r+1)`. No bound on pin cardinality is needed
for this distance statement; the twelve-pin degree obligation is separate. -/
theorem singleVertexExtension_diameter {V : Type*} (G : SimpleGraph V)
    (pins : Set V) {D r : Nat}
    (hdiam : DiameterAtMost G D) (hcover : PinsCoverRadius G pins r) :
    DiameterAtMost (singleVertexExtension G pins) (max D (r + 1)) := by
  have hnew : ∀ v, ∃ p : (singleVertexExtension G pins).Walk none (some v),
      p.length ≤ r + 1 := by
    intro v
    obtain ⟨u, hu, p, hp⟩ := hcover v
    have hedge : (singleVertexExtension G pins).Adj none (some u) := hu
    refine ⟨Walk.cons hedge (p.map (oldVertexHom G pins)), ?_⟩
    simpa using Nat.succ_le_succ hp
  intro a b
  cases a with
  | none => cases b with
    | none => exact ⟨Walk.nil, Nat.zero_le _⟩
    | some v =>
      obtain ⟨p, hp⟩ := hnew v
      exact ⟨p, hp.trans (le_max_right _ _)⟩
  | some u => cases b with
    | none =>
      obtain ⟨p, hp⟩ := hnew u
      refine ⟨p.reverse, ?_⟩
      simpa using hp.trans (le_max_right D (r + 1))
    | some v =>
      obtain ⟨p, hp⟩ := hdiam u v
      refine ⟨p.map (oldVertexHom G pins), ?_⟩
      simpa using hp.trans (le_max_left D (r + 1))

/-- Explicitly conditional D5/R4 specialization for candidate42343.
The old graph's D5 property and the actual R4 pin certificate must be supplied. -/
theorem singleVertexExtension_diameterAtMostFive {V : Type*} (G : SimpleGraph V)
    (pins : Set V) (hdiam : DiameterAtMost G 5)
    (hcover : PinsCoverRadius G pins 4) :
    DiameterAtMost (singleVertexExtension G pins) 5 := by
  exact singleVertexExtension_diameter G pins hdiam hcover

/-- Local data needed to certify radius coverage. The fields are proof obligations,
not axioms and not an assertion that any actual source already satisfies them. -/
structure ParentDepthCertificate {V : Type*} (G : SimpleGraph V)
    (pins : Set V) (radius : Nat) where
  parent : V → V
  depth : V → Nat
  depth_le : ∀ v, depth v ≤ radius
  root_mem : ∀ v, depth v = 0 → v ∈ pins
  step : ∀ v, depth v ≠ 0 →
    G.Adj (parent v) v ∧ depth (parent v) + 1 = depth v

/-- A locally checked parent/depth certificate gives genuine bounded old walks. -/
theorem parentDepthCertificate_sound {V : Type*} {G : SimpleGraph V}
    {pins : Set V} {radius : Nat}
    (cert : ParentDepthCertificate G pins radius) : PinsCoverRadius G pins radius := by
  have reaches : ∀ n, ∀ v, cert.depth v = n →
      ∃ u ∈ pins, ∃ p : G.Walk u v, p.length ≤ n := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro v hv
      by_cases hzero : n = 0
      · have hroot : cert.depth v = 0 := hv.trans hzero
        exact ⟨v, cert.root_mem v hroot, Walk.nil, Nat.zero_le n⟩
      · have hdepth : cert.depth v ≠ 0 := by
          intro heq
          exact hzero (hv.symm.trans heq)
        obtain ⟨hadj, hstep⟩ := cert.step v hdepth
        have hsmall : cert.depth (cert.parent v) < n := by
          rw [← hv, ← hstep]
          exact Nat.lt_succ_self _
        obtain ⟨u, hu, p, hp⟩ := ih _ hsmall (cert.parent v) rfl
        refine ⟨u, hu, p.concat hadj, ?_⟩
        calc
          (p.concat hadj).length = p.length + 1 := by simp
          _ ≤ cert.depth (cert.parent v) + 1 := Nat.add_le_add_right hp 1
          _ = n := hstep.trans hv
  intro v
  obtain ⟨u, hu, p, hp⟩ := reaches (cert.depth v) v rfl
  exact ⟨u, hu, p, hp.trans (cert.depth_le v)⟩

/-- Conditional final caller for a source D5 theorem and a verified R4 certificate.
In particular, this does not manufacture a D5 theorem for the actual old graph. -/
theorem singleVertexExtension_diameterAtMostFive_of_parentDepth {V : Type*}
    (G : SimpleGraph V) (pins : Set V) (hdiam : DiameterAtMost G 5)
    (cert : ParentDepthCertificate G pins 4) :
    DiameterAtMost (singleVertexExtension G pins) 5 :=
  singleVertexExtension_diameterAtMostFive G pins hdiam (parentDepthCertificate_sound cert)

end DegreeDiameter.Portfolio
