import Aris4Math.General.RS.Bernoulli
open Aris4Math.General.RS
#print axioms bernoulli_harris
#print axioms bernoulli_rpow_jensen
#print axioms bernoulli_harris_events
#print axioms bernoulliProb_all_edges_hit
#check bernoulli_harris
#check bernoulli_rpow_jensen
#check bernoulliProb_all_edges_hit
#check bernoulliProb_hits
#check sum_bernoulliWeight

example {V : Type*} [Fintype V] {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (edges : Finset (Finset V)) :
    (∏ e ∈ edges, (1 - (1-p) ^ e.card)) ≤
      bernoulliProb p (fun b => ∀ e ∈ edges, ∃ v ∈ e, b v = true) :=
  bernoulliProb_all_edges_hit hp hp1 edges
