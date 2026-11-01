import Aris4Math.General.RS.PairProbability
open Aris4Math.General.RS

#check sampleProb_pairEvent
#check sampleProb_pairEvent_formula
#print axioms sampleProb_pairEvent
#print axioms sampleProb_pairEvent_formula
#print axioms pairEvent_iff_local
#print axioms permProb_pairLocal
#print axioms pairIntegrand_average

example {n k : ℕ} (f g : Finset (Fin n)) (x : Fin n)
    (hfg : f ∩ g = {x}) (hf : f.card = k) (hg : g.card = k)
    (hk : 2 ≤ k) (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => PairEvent f g c b σ q) =
      jk k p / (2 : ℝ)^(2*k-1) :=
  sampleProb_pairEvent_singleton f g x hfg hf hg (by omega) q p
