import DegreeDiameter.N63Defect
import DegreeDiameter.N63Compose

-- Checkpoint-only file; not part of the default audit and not run after the pause.

#print DegreeDiameter.n63Chebyshev
#print DegreeDiameter.n63Annihilator
#check @DegreeDiameter.n63_original_defect_local_factor
#check @DegreeDiameter.n63_original_defect_annihilator
#print axioms DegreeDiameter.n63_original_defect_local_factor
#print axioms DegreeDiameter.n63_original_defect_annihilator

#check @DegreeDiameter.n63_composition_irreducible
#print axioms DegreeDiameter.n63_composition_irreducible
