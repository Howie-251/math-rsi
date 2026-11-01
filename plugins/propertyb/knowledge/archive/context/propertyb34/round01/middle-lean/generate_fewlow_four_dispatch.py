"""Connect all strict four-lock representatives to their original-H callers."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
out=P.parents[3]/'formal/Aris4Math/ThirtyFour/TwentyThreeFewLowFourClassified.lean'
d=json.loads((P/'FEW_LOW_FOUR_ALL_EXPORT.json').read_text())
mods=[r['module']for r in d['pure']+d['joint']]
s=['import Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage\n']+[f'import Aris4Math.ThirtyFour.{m}\n'for m in mods]
s+=['''namespace Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
''']
for k,name in enumerate(['OneLow','TwoLow']):
 pure=d['pure'][k];res=d['residual'][k]['groups'];prefix=pure['module'];N=73 if k==0 else 48
 joint=[r for r in d['joint']if r['module'].startswith(prefix)]
 s+=[f'namespace {name}\nopen TwentyThreeFewLowFourCoverage.{name} (NewCase μ)\n']
 s+=[f'def residual : Finset NewCase := '+ '{'+','.join(map(str,res))+'}\n']
 s+=[f'def pureIndex : {prefix}Data.Case → NewCase := !['+','.join(map(str,pure['groups']))+']\n']
 s+=[f'theorem pureMatch : ∀ c T, μ (pureIndex c) T={prefix}Data.μ c T := by decide +kernel\n']
 for r in joint:s+=[f'theorem jointMatch{r["group"]} : ∀ T, μ {r["group"]} T={r["module"]}Data.μ T := by decide +kernel\n']
 s+=[f'''theorem residual_of_noB (H : Simple5Hypergraph (Fin 23))
    (f : Fin 4 ↪ Fin 23) (c : NewCase)
    (counts : ∀ T, count H f T=μ c T) (noB : ¬PropertyB H) : c∈residual := by
  by_contra absent
  fin_cases c
''']
 for q in range(N):
  if q in res:s+=['  · exact absent (by decide)\n'];continue
  s+=['  · apply noB\n']
  if q in pure['groups']:
   idx=pure['groups'].index(q)
   s+=[f'    apply {prefix}.propertyB_of_counts H f {idx}\n    intro T\n    exact (counts T).trans (pureMatch {idx} T)\n']
  else:
   r=next(r for r in joint if r['group']==q)
   s+=[f'    apply {r["module"]}.propertyB_of_counts H f\n    intro T\n    exact (counts T).trans (jointMatch{q} T)\n']
 base='oneLow' if k==0 else 'twoLow'
 s+=[f'''/-- Actual old/new lock classification followed by all proved strict exclusions. -/
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (c : TwentyThreeFewLowBase.Case)
    (old : ∀ T, count H (LockExtension.restrict f) T=TwentyThreeFewLowBase.{base} c T)
    (degree : H.degree (f 3)=7)
    (pairs : ∀ i : Fin 3,
      H.codegree (f i.castSucc) (f 3)≤TwentyThreeFewLowFourCoverage.{name}.cap (some i))
    (noB : ¬PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<{k+1} ↔ i.val<{k+1}) ∧ q∈residual ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨q,σ,roles,counts⟩ :=
    TwentyThreeFewLowFourCoverage.{name}.actual H cover f c old degree pairs
  exact ⟨q,σ,roles,residual_of_noB H (σ.toEmbedding.trans f) q counts noB,counts⟩
end {name}
''']
s+=['end Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.OneLow.residual_of_noB\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.TwoLow.residual_of_noB\n']
s+=['#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.OneLow.actual_residual\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.TwoLow.actual_residual\n']
out.write_text(''.join(s));print(out)
