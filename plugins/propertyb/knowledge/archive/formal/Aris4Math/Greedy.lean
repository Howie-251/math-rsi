import Aris4Math
import Mathlib.Data.Finset.Max

/-!
# P1: the actual greedy algorithm and its critical-pair obstruction

Vertices are `Fin v`, scanned in their natural order. Blue sets start empty.
At step t, vertex t is inserted exactly when it is the last vertex of an edge
that is still entirely red. No critical-pair coverage hypothesis is assumed.
-/

namespace Aris4Math.Greedy

variable {v : ℕ}

/-- A concrete reason to flip the current vertex from red to blue. -/
def FlipWitness (E : Finset (Finset (Fin v))) (blue : Finset (Fin v))
    (x : Fin v) : Prop :=
  ∃ A ∈ E, x ∈ A ∧ (∀ y ∈ A, y ≤ x) ∧ ∀ y ∈ A, y ∉ blue

/-- The finite greedy scan, with blue membership recording the color.
After the last vertex, the state stays fixed. -/
noncomputable def blueAfter (E : Finset (Finset (Fin v))) : ℕ → Finset (Fin v)
  | 0 => ∅
  | t + 1 => by
      classical
      exact if ht : t < v then
        let x : Fin v := ⟨t, ht⟩
        if FlipWitness E (blueAfter E t) x then insert x (blueAfter E t)
        else blueAfter E t
      else blueAfter E t

/-- Every step either keeps the blue set or inserts just the current vertex. -/
theorem blueAfter_step_subset (E : Finset (Finset (Fin v))) (t : ℕ) :
    blueAfter E t ⊆ blueAfter E (t + 1) := by
  classical
  simp only [blueAfter]
  split_ifs <;> simp

/-- Colors only change from red to blue. -/
theorem blueAfter_mono (E : Finset (Finset (Fin v))) : Monotone (blueAfter E) := by
  exact monotone_nat_of_le_succ (blueAfter_step_subset E)

/-- Only vertices already scanned can be blue. -/
theorem blueAfter_mem_before (E : Finset (Finset (Fin v))) (t : ℕ)
    (x : Fin v) (hx : x ∈ blueAfter E t) : x.val < t := by
  classical
  induction t with
  | zero => simp [blueAfter] at hx
  | succ t ih =>
      simp only [blueAfter] at hx
      split_ifs at hx with ht hflip
      · rcases Finset.mem_insert.mp hx with hnew | hold
        · subst x
          simp
        · exact Nat.lt.step (ih hold)
      · exact Nat.lt.step (ih hx)
      · exact Nat.lt.step (ih hx)

/-- A flip really happens when the algorithm's condition is satisfied. -/
theorem blueAfter_of_flip (E : Finset (Finset (Fin v))) (x : Fin v)
    (hflip : FlipWitness E (blueAfter E x.val) x) :
    x ∈ blueAfter E (x.val + 1) := by
  classical
  simp only [blueAfter, dif_pos x.isLt]
  simp [hflip]

/-- Every blue vertex has the actual all-red witness from its own scan time. -/
theorem blueAfter_mem_witness (E : Finset (Finset (Fin v))) (t : ℕ)
    (x : Fin v) (hx : x ∈ blueAfter E t) :
    FlipWitness E (blueAfter E x.val) x := by
  classical
  induction t with
  | zero => simp [blueAfter] at hx
  | succ t ih =>
      simp only [blueAfter] at hx
      split_ifs at hx with ht hflip
      · rcases Finset.mem_insert.mp hx with hnew | hold
        · subst x
          exact hflip
        · exact ih hold
      · exact ih hx
      · exact ih hx

/-- Every nonempty edge contains a blue vertex after the scan: there is no
all-red output edge. This needs no uniformity assumption. -/
theorem no_all_red_edge (E : Finset (Finset (Fin v))) (e : Finset (Fin v))
    (he : e ∈ E) (hne : e.Nonempty) :
    ∃ x ∈ e, x ∈ blueAfter E v := by
  classical
  by_contra hred
  have all_red : ∀ x ∈ e, x ∉ blueAfter E v := by
    intro x hx hb
    exact hred ⟨x, hx, hb⟩
  let x := e.max' hne
  have hx : x ∈ e := Finset.max'_mem e hne
  have hflip : FlipWitness E (blueAfter E x.val) x := by
    refine ⟨e, he, hx, ?_, ?_⟩
    · intro y hy
      exact Finset.le_max' e y hy
    · intro y hy hblue
      exact all_red y hy (blueAfter_mono E (Nat.le_of_lt x.isLt) hblue)
  have hblue := blueAfter_of_flip E x hflip
  have hfinal : x ∈ blueAfter E v :=
    blueAfter_mono E (Nat.succ_le_of_lt x.isLt) hblue
  exact all_red x hx hfinal

/-- The endpoint and intersection data of the ordered critical pair. -/
structure CriticalPair (A B : Finset (Fin v)) (x : Fin v) : Prop where
  distinct : A ≠ B
  mem_left : x ∈ A
  mem_right : x ∈ B
  last_left : ∀ y ∈ A, y ≤ x
  first_right : ∀ y ∈ B, x ≤ y
  singleton_intersection : A ∩ B = {x}

/-- Any all-blue edge of size at least two produces a distinct ordered
critical pair. The witness edge is obtained from the actual flip history. -/
theorem all_blue_implies_critical_pair
    (E : Finset (Finset (Fin v))) (B : Finset (Fin v))
    (hsize : 2 ≤ B.card) (hblue : B ⊆ blueAfter E v) :
    ∃ A ∈ E, ∃ x : Fin v, CriticalPair A B x := by
  classical
  have hne : B.Nonempty := Finset.card_pos.mp (by omega)
  let x := B.min' hne
  have hxB : x ∈ B := Finset.min'_mem B hne
  have hxblue : x ∈ blueAfter E v := hblue hxB
  obtain ⟨A, hAE, hxA, hlast, hred⟩ := blueAfter_mem_witness E v x hxblue
  have hfirst : ∀ y ∈ B, x ≤ y := by
    intro y hy
    exact Finset.min'_le B y hy
  have hinter : A ∩ B = {x} := by
    ext y
    constructor
    · intro hy
      have hAB := Finset.mem_inter.mp hy
      exact Finset.mem_singleton.mpr (le_antisymm (hlast y hAB.1) (hfirst y hAB.2))
    · intro hy
      have hyx := Finset.mem_singleton.mp hy
      subst y
      exact Finset.mem_inter.mpr ⟨hxA, hxB⟩
  have hdistinct : A ≠ B := by
    intro heq
    have hsingle : B = {x} := by simpa [heq] using hinter
    have hcard : B.card = 1 := by simp [hsingle]
    omega
  exact ⟨A, hAE, x, ⟨hdistinct, hxA, hxB, hlast, hfirst, hinter⟩⟩

/-- The order predicates really say max A = x = min B. -/
theorem critical_pair_endpoints (A B : Finset (Fin v)) (x : Fin v)
    (h : CriticalPair A B x) :
    A.max' ⟨x, h.mem_left⟩ = x ∧ B.min' ⟨x, h.mem_right⟩ = x := by
  exact ⟨(Finset.max'_eq_iff _ _ _).mpr ⟨h.mem_left, h.last_left⟩,
    (Finset.min'_eq_iff _ _ _).mpr ⟨h.mem_right, h.first_right⟩⟩

/-- Failure means the actual output has a monochromatic edge. -/
def Failure (E : Finset (Finset (Fin v))) : Prop :=
  ∃ e ∈ E, (∀ x ∈ e, x ∉ blueAfter E v) ∨ e ⊆ blueAfter E v

/-- Full P1 on ordered vertices: for an n-uniform hypergraph with n ≥ 2,
algorithm failure produces two distinct edges meeting at their common endpoint.
The theorem quantifies over all such hypergraphs, without sampling. -/
theorem uniform_failure_covered (E : Finset (Finset (Fin v))) (n : ℕ)
    (hn : 2 ≤ n) (huniform : ∀ e ∈ E, e.card = n)
    (hfail : Failure E) :
    ∃ A ∈ E, ∃ B ∈ E, ∃ x : Fin v, CriticalPair A B x := by
  obtain ⟨B, hBE, hred | hblue⟩ := hfail
  · have hne : B.Nonempty := Finset.card_pos.mp (by rw [huniform B hBE]; omega)
    obtain ⟨x, hxB, hxblue⟩ := no_all_red_edge E B hBE hne
    exact False.elim (hred x hxB hxblue)
  · have hsize : 2 ≤ B.card := by rw [huniform B hBE]; exact hn
    obtain ⟨A, hAE, x, hp⟩ := all_blue_implies_critical_pair E B hsize hblue
    exact ⟨A, hAE, B, hBE, x, hp⟩

/-- A permutation is interpreted as vertex → position. Relabeling vertices
by their positions turns its greedy scan into the ordered scan already proved. -/
def orderedEdges (E : Finset (Finset (Fin v))) (σ : Equiv.Perm (Fin v)) :
    Finset (Finset (Fin v)) := E.image (fun e => e.map σ.toEmbedding)

theorem orderedEdges_uniform (E : Finset (Finset (Fin v))) (n : ℕ)
    (huniform : ∀ e ∈ E, e.card = n) (σ : Equiv.Perm (Fin v)) :
    ∀ e ∈ orderedEdges E σ, e.card = n := by
  intro e he
  obtain ⟨A, hAE, rfl⟩ := Finset.mem_image.mp he
  simpa using huniform A hAE

/-- Failure of the actual greedy scan in the order σ. -/
def FailureAt (E : Finset (Finset (Fin v))) (σ : Equiv.Perm (Fin v)) : Prop :=
  Failure (orderedEdges E σ)

/-- Position k has an ordered critical pair of original distinct edges. -/
def CriticalAt (E : Finset (Finset (Fin v))) (σ : Equiv.Perm (Fin v))
    (k : Fin v) : Prop :=
  ∃ A ∈ E, ∃ B ∈ E, A ≠ B ∧
    CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k

/-- P1 for an arbitrary permutation, retaining original edge identities. -/
theorem failureAt_covered (E : Finset (Finset (Fin v))) (n : ℕ)
    (hn : 2 ≤ n) (huniform : ∀ e ∈ E, e.card = n)
    (σ : Equiv.Perm (Fin v)) (hfail : FailureAt E σ) :
    ∃ k : Fin v, CriticalAt E σ k := by
  obtain ⟨A, hAE, B, hBE, k, hp⟩ := uniform_failure_covered (orderedEdges E σ) n hn
    (orderedEdges_uniform E n huniform σ) hfail
  obtain ⟨a, haE, rfl⟩ := Finset.mem_image.mp hAE
  obtain ⟨b, hbE, rfl⟩ := Finset.mem_image.mp hBE
  refine ⟨k, a, haE, b, hbE, ?_, hp⟩
  intro hab
  exact hp.distinct (congrArg (fun e => e.map σ.toEmbedding) hab)

/-- Bad outcomes in any finite permutation sample, including a sample formed
by locking prescribed vertices at prescribed positions. -/
noncomputable def badPermutations (E : Finset (Finset (Fin v)))
    (sample : Finset (Equiv.Perm (Fin v))) : Finset (Equiv.Perm (Fin v)) := by
  classical
  exact sample.filter (FailureAt E)

/-- The critical-pair event at one position in that same sample. -/
noncomputable def criticalPermutations (E : Finset (Finset (Fin v)))
    (sample : Finset (Equiv.Perm (Fin v))) (k : Fin v) :
    Finset (Equiv.Perm (Fin v)) := by
  classical
  exact sample.filter (fun σ => CriticalAt E σ k)

/-- The concrete P1 event inclusion required by the finite-event spine.
It holds for every sample, so conditioning on fixed permutation positions
requires no new greedy-algorithm argument. -/
theorem failure_event_cover (E : Finset (Finset (Fin v))) (n : ℕ)
    (hn : 2 ≤ n) (huniform : ∀ e ∈ E, e.card = n)
    (sample : Finset (Equiv.Perm (Fin v))) :
    badPermutations E sample ⊆
      (Finset.univ : Finset (Fin v)).biUnion (criticalPermutations E sample) := by
  classical
  intro σ hσ
  obtain ⟨hsample, hfail⟩ := Finset.mem_filter.mp hσ
  obtain ⟨k, hk⟩ := failureAt_covered E n hn huniform σ hfail
  exact Finset.mem_biUnion.mpr
    ⟨k, Finset.mem_univ k, Finset.mem_filter.mpr ⟨hsample, hk⟩⟩

/-- A successful permutation gives Property B in the original count-based
definition, with the positional coloring pulled back to the original vertices. -/
theorem propertyB_of_successful_permutation
    (H : Aris4Math.Simple5Hypergraph (Fin v)) (σ : Equiv.Perm (Fin v))
    (hsuccess : ¬ FailureAt H.edges σ) : Aris4Math.PropertyB H := by
  classical
  let blue := blueAfter (orderedEdges H.edges σ) v
  let c : Fin v → Bool := fun x => decide (σ x ∉ blue)
  refine ⟨c, ?_⟩
  intro e he
  have hemap : e.map σ.toEmbedding ∈ orderedEdges H.edges σ :=
    Finset.mem_image.mpr ⟨e, he, rfl⟩
  have hmapne : (e.map σ.toEmbedding).Nonempty := by
    apply Finset.card_pos.mp
    rw [Finset.card_map, H.five_uniform e he]
    decide
  have red_exists : ∃ p ∈ e.map σ.toEmbedding, p ∉ blue := by
    by_contra hnone
    apply hsuccess
    refine ⟨e.map σ.toEmbedding, hemap, Or.inr ?_⟩
    intro p hp
    by_contra hnotblue
    exact hnone ⟨p, hp, hnotblue⟩
  obtain ⟨rpos, hrpos, hrred⟩ := red_exists
  obtain ⟨r, hre, hrmap⟩ := Finset.mem_map.mp hrpos
  have hrcolor : c r = true := by
    have hrred' : σ r ∉ blue := by simpa [← hrmap] using hrred
    simp [c, hrred']
  have lower : 1 ≤ (e.filter (fun x => c x = true)).card :=
    Finset.card_pos.mpr ⟨r, Finset.mem_filter.mpr ⟨hre, hrcolor⟩⟩
  obtain ⟨bpos, hbpos, hbblue⟩ := no_all_red_edge (orderedEdges H.edges σ)
    (e.map σ.toEmbedding) hemap hmapne
  obtain ⟨b, hbe, hbmap⟩ := Finset.mem_map.mp hbpos
  have hbcolor : c b = false := by
    have hbblue' : σ b ∈ blue := by simpa [← hbmap] using hbblue
    simp [c, hbblue']
  have subset_erase : e.filter (fun x => c x = true) ⊆ e.erase b := by
    intro y hy
    obtain ⟨hye, hycolor⟩ := Finset.mem_filter.mp hy
    apply Finset.mem_erase.mpr
    refine ⟨?_, hye⟩
    intro hyb
    subst y
    simp [hbcolor] at hycolor
  have upper := Finset.card_le_card subset_erase
  rw [Finset.card_erase_of_mem hbe, H.five_uniform e he] at upper
  exact ⟨lower, upper⟩

end Aris4Math.Greedy

#print axioms Aris4Math.Greedy.blueAfter_mono
#print axioms Aris4Math.Greedy.blueAfter_mem_before
#print axioms Aris4Math.Greedy.blueAfter_mem_witness
#print axioms Aris4Math.Greedy.no_all_red_edge
#print axioms Aris4Math.Greedy.all_blue_implies_critical_pair
#print axioms Aris4Math.Greedy.critical_pair_endpoints
#print axioms Aris4Math.Greedy.uniform_failure_covered
#print axioms Aris4Math.Greedy.failureAt_covered
#print axioms Aris4Math.Greedy.failure_event_cover
#print axioms Aris4Math.Greedy.propertyB_of_successful_permutation
