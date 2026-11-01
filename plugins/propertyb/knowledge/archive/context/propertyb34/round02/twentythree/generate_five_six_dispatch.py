from pathlib import Path
from fractions import Fraction as F
import json
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'formal/Aris4Math/ThirtyFour'
vec=lambda xs:'!['+','.join(map(str,xs))+']'
for n,word in [(5,'Five'),(6,'Six')]:
 rows=json.loads((ROOT/f'context/propertyb34/round01/middle-math/EXTEND_LOW_23_{n}.json').read_text())['results']
 pure=[r['group']for r in rows if F(r['bound'])<1]
 joint=[r['group']for r in rows if F(r['bound'])>=1 and F(r['joint']['bound'])<1]
 res=[r['group']for r in rows if F(r['bound'])>=1 and F(r['joint']['bound'])>=1]
 prefix=f'TwentyThree{word}Low'
 s=f'import Aris4Math.ThirtyFour.{prefix}Promotion\n'
 if pure:s+=f'import Aris4Math.ThirtyFour.{prefix}Strict\n'
 for j in joint:s+=f'import Aris4Math.ThirtyFour.{prefix}StrictJoint{j}\n'
 s+=f'''namespace Aris4Math.ThirtyFour.{prefix}Classified
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open {prefix}Promotion (NewCase μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Residue := Fin {len(res)}
def residualSource : Residue → NewCase := {vec(res)}
def residualCounts (r : Residue) := μ (residualSource r)
'''
 if pure:
  s+=f'''def pureSource : {prefix}StrictData.Case → NewCase := {vec(pure)}
theorem pure_binding : ∀ i T, μ (pureSource i) T={prefix}StrictData.μ i T := by decide +kernel
'''
 for j in joint:s+=f'theorem joint_binding{j} : ∀ T, μ {j} T={prefix}StrictJoint{j}Data.μ T := by decide +kernel\n'
 s+=f'''theorem residual_of_noB (H : Simple5Hypergraph (Fin 23)) (f : Fin {n} ↪ Fin 23)
    (q : NewCase) (notB : ¬ PropertyB H) (actual : ∀ T, count H f T=μ q T) :
    ∃ r : Residue, ∀ T, count H f T=residualCounts r T := by
  fin_cases q
'''
 for j in range(len(rows)):
  if j in pure:
   p=pure.index(j);s+=f'''  · exact (notB ({prefix}Strict.propertyB_of_counts H f {p}
      (fun T => (actual T).trans (pure_binding {p} T)))).elim
'''
  elif j in joint:
   s+=f'''  · exact (notB ({prefix}StrictJoint{j}.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding{j} T)))).elim
'''
  else:s+=f'  · exact ⟨{res.index(j)},actual⟩\n'
 s+=f'''theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin {n} ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ r : Residue, ∃ σ : Equiv.Perm (Fin {n}),
      ∀ T, count H (σ.toEmbedding.trans f) T=residualCounts r T := by
  obtain ⟨q,σ,actual⟩ := {prefix}Promotion.actual H cover edges f degrees notB
  obtain ⟨r,hr⟩ := residual_of_noB H (σ.toEmbedding.trans f) q notB actual
  exact ⟨r,σ,hr⟩
end Aris4Math.ThirtyFour.{prefix}Classified
#print axioms Aris4Math.ThirtyFour.{prefix}Classified.actual_residual
'''
 (OUT/f'{prefix}Classified.lean').write_text(s)
