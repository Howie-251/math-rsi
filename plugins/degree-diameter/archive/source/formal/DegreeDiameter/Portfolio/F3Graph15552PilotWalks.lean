import DegreeDiameter.Portfolio.F3Graph15552PilotCertificate
namespace DegreeDiameter.Portfolio.F3Graph15552
namespace PilotLargestGroup
theorem all_walk_bound (x y : Fin 81) :
    ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4 :=
  coset_walk_bound a b reference word column choice alpha column_certificate cover_certificate
    controller_certificate length_certificate x y
#print axioms all_walk_bound
end PilotLargestGroup
namespace PilotFullrank
theorem all_walk_bound (x y : Fin 81) :
    ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4 :=
  inverse_walk_bound a b word inverseBasis basis_certificate controller_certificate length_certificate x y
#print axioms all_walk_bound
end PilotFullrank
end DegreeDiameter.Portfolio.F3Graph15552
