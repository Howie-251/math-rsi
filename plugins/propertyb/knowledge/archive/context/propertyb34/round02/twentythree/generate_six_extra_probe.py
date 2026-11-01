from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;SRC=ROOT/'formal/Aris4Math/ThirtyFour'
body=lambda path:'\n'.join(l for l in path.read_text().splitlines()if not l.startswith('import '))
ns={int(t):v for t,v in json.loads((ROOT/'context/propertyb34/round01/middle-math/EXTEND_LOW_23_6.json').read_text())['results'][2]['counts'].items()if v}
fs=lambda t:'{'+','.join(str(i)for i in range(6)if t>>i&1)+'}'if t else'∅'
mu='(fun T => '+''.join(f'if T={fs(t)} then {v} else 'for t,v in sorted(ns.items()))+'0)'
old='namespace Aris4Math.ThirtyFour.TwentyThreeSixLowClassified\nabbrev Residue := Fin 1\ndef residualCounts (r : Residue) : Finset (Fin 6) → ℕ := '+mu+'\nend Aris4Math.ThirtyFour.TwentyThreeSixLowClassified\n'
imports='import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase\nimport Aris4Math.ThirtyFour.TwentyFourPermutation\n'
actual=body(SRC/'TwentyThreeSixLowExtraCatalogue.lean')
actual=actual.replace('/-- The seven-lock input','variable (checkedCoverage : ∀ b values, values∈catalogue b → ∀ d, (b=none ∨ b=some 0) → ∃ w : Witness, Matched d b values w)\ninclude checkedCoverage\n\n/-- The seven-lock input')
actual=actual.replace(':= coverage b values member d',':= checkedCoverage b values member d')
actual=actual.replace('actual_normalized_extension H','actual_normalized_extension checkedCoverage H')
actual=actual.replace('theorem normalizer_', 'omit checkedCoverage in\ntheorem normalizer_')
result=imports+body(SRC/'TwentyThreeHighPromotion.lean')+'\n'+body(SRC/'TwentyThreeSparsePromotion.lean')+'\n'+old+'\n'+body(SRC/'TwentyThreeSixLowExtraCatalogueData.lean')+'\n'+actual
(HERE/'SixExtraActualProbe.lean').write_text(result)

# The complete actual chain is checked independently of the still-pending
# finite coverage and numerical certificates, with those exact APIs explicit.
complete=body(SRC/'TwentyThreeExactlySixLowComplete.lean')
variables="""variable
  (checkedCoverage : ∀ b values, values∈catalogue b → ∀ d, (b=none ∨ b=some 0) → ∃ w : Witness, Matched d b values w)
  (classify : ∀ (H : Simple5Hypergraph (Fin 23)), H.PairCovering → H.edges.card=34 →
    ∀ f : Fin 6↪Fin 23, (∀ i, H.degree (f i)=6) → ¬PropertyB H →
    ∃ r : TwentyThreeSixLowClassified.Residue, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeSixLowClassified.residualCounts r T)
  (closeProfile : ∀ (H : Simple5Hypergraph (Fin 23)) (f : Fin 7↪Fin 23)
    (d : Degree) (q : NewCase), (∀ T, count H f T=μ d q T) → PropertyB H)
include checkedCoverage classify closeProfile
"""
complete=complete.replace('/-- The exact-six branch',variables+'\n/-- The exact-six branch')
complete=complete.replace('TwentyThreeSixLowClassified.actual_residual H','classify H').replace('actual_extension H','actual_extension checkedCoverage H').replace('TwentyThreeSixLowExtraChecked.propertyB_of_counts H','closeProfile H')
(HERE/'SixExtraCompleteProbe.lean').write_text('import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection\n'+result+'\n'+complete)
