import Aris4Math.General.Growth.Seed
open Aris4Math.General.RS

example (k : ℕ) (hk : 17 ≤ k) : RSAccepts k (2 ^ k) := seed_rsAccepts hk
example (k : ℕ) (hk : 17 ≤ k) : AcceptedAt k (2 ^ k) (1 / (k : ℝ)) :=
  seed_acceptedAt hk
example (k M : ℕ) (hM : 1 ≤ M) (p : ℝ) (hA : AcceptedAt k M p) : 0 < p :=
  acceptedAt_p_pos hM hA

#print Aris4Math.General.RS.seed_rsAccepts
#print axioms Aris4Math.General.RS.seed_acceptedAt
#print axioms Aris4Math.General.RS.acceptedAt_p_pos
