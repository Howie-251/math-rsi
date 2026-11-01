"""Connect the reused 50-type domain to the saved strict/residual split."""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as F
import re,json
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'formal/Aris4Math/ThirtyFour'
raw=json.loads((ROOT/'context/propertyb34/round01/middle-math/FOUR_LOW_23.json').read_text())
rows=raw['results']; perms=list(permutations(range(4)))
oldsrc=(ROOT/'formal/Aris4Math/ThirtyThree/TwentyThreeFourLowCatalog.lean').read_text()
oldtext=oldsrc.split('def counts :')[1].split('def permutationFn')[0]
oldrows=[]
for piece in oldtext.split('(fun T => ')[1:]:
 ns={}
 for literal,n in re.findall(r'if T = (∅|\{[0-9,]+\}) then ([0-9]+)',piece):
  mask=0 if literal=='∅' else sum(1<<int(x) for x in literal.strip('{}').split(','))
  ns[mask]=int(n)
 ns[0]+=1
 oldrows.append(ns)
assert len(oldrows)==50
counts=[{int(t):n for t,n in r['counts'].items() if n} for r in rows]
def image(t,p): return sum(1<<p[i] for i in range(4) if t>>i&1)
lookup=[]
for old in oldrows:
 found=[(j,k) for j,ns in enumerate(counts) for k,p in enumerate(perms)
        if all(old.get(image(t,p),0)==ns.get(t,0) for t in range(16))]
 assert found
 lookup.append(found[0])
vec=lambda xs:'!['+','.join(map(str,xs))+']'
fs=lambda t:'{'+','.join(str(i) for i in range(4) if t>>i&1)+'}' if t else '∅'
mu=lambda ns:'(fun T => '+''.join(f'if T={fs(t)} then {n} else ' for t,n in sorted(ns.items()))+'0)'
pure=[r['group'] for r in rows if F(r['bound'])<1]
joint=[r['group'] for r in rows if F(r['bound'])>=1 and F(r['joint']['bound'])<1]
res=[r['group'] for r in rows if F(r['bound'])>=1 and F(r['joint']['bound'])>=1]
s='import Aris4Math.ThirtyFour.LockRelabel\nimport Aris4Math.ThirtyFour.TwentyThreeFourLowCatalog\nimport Aris4Math.ThirtyFour.TwentyThreeFourLowStrict\n'
s+=''.join(f'import Aris4Math.ThirtyFour.TwentyThreeFourLowJoint{j}\n' for j in joint)
s+='''
namespace Aris4Math.ThirtyFour.TwentyThreeFourLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open Aris4Math.ThirtyThree.TwentyThreeFourLowCatalog (permutation)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def sourceCounts : Fin 50 → Finset (Fin 4) → ℕ := '+vec(mu(c) for c in counts)+'\n'
s+='def oldToSource : Fin 50 → Fin 50 × Fin 24 := '+vec(f'({a},{b})' for a,b in lookup)+'\n'
s+='''theorem old_binding : ∀ k T,
    TwentyThreeFourLowCatalog.counts k (T.image (permutation (oldToSource k).2)) =
      sourceCounts (oldToSource k).1 T := by decide +kernel
'''
s+=f'abbrev Residue := Fin {len(res)}\ndef residualSource : Residue → Fin 50 := '+vec(res)+'\n'
s+='def residualCounts (r : Residue) : Finset (Fin 4) → ℕ := sourceCounts (residualSource r)\n'
s+='def pureSource : TwentyThreeFourLowStrictData.Case → Fin 50 := '+vec(pure)+'\n'
s+='''theorem pure_binding : ∀ i T, sourceCounts (pureSource i) T =
    TwentyThreeFourLowStrictData.μ i T := by decide +kernel
'''
for j in joint:
 s+=f'''theorem joint_binding{j} : ∀ T, sourceCounts {j} T =
    TwentyThreeFourLowJoint{j}Data.μ T := by decide +kernel
'''
s+='''
/-- All 50 actual types are split into 42 strict types and precisely eight residues. -/
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23)) (f : Fin 4 ↪ Fin 23)
    (q : Fin 50) (notB : ¬ PropertyB H)
    (actual : ∀ T, count H f T=sourceCounts q T) :
    ∃ r : Residue, ∀ T, count H f T=residualCounts r T := by
  fin_cases q
'''
for j in range(50):
 if j in pure:
  p=pure.index(j)
  s+=f'''  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f {p}
      (fun T => (actual T).trans (pure_binding {p} T)))).elim
'''
 elif j in joint:
  s+=f'''  · exact (notB (TwentyThreeFourLowJoint{j}.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding{j} T)))).elim
'''
 else:
  s+=f'  · exact ⟨{res.index(j)}, actual⟩\n'
s+='''
/-- From any actual four low vertices, obtain a residue after a genuine
permutation of those same vertices. No external local-table premise remains. -/
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ r : Residue, ∃ σ : Equiv.Perm (Fin 4),
      ∀ T, count H (σ.toEmbedding.trans f) T=residualCounts r T := by
  obtain ⟨k, σ, actual⟩ := TwentyThreeFourLowCatalog.actual_representative_perm H cover edges f degrees
  change ∀ T, count H (σ.toEmbedding.trans f) T = TwentyThreeFourLowCatalog.counts k T at actual
  let τ := permutation (oldToSource k).2
  have mapped : ∀ T, count H ((τ.trans σ).toEmbedding.trans f) T =
      sourceCounts (oldToSource k).1 T := by
    intro T
    change count H (τ.toEmbedding.trans (σ.toEmbedding.trans f)) T = _
    rw [LockRelabel.count_comp_perm, actual]
    simpa only [Finset.map_eq_image] using old_binding k T
  obtain ⟨r, hr⟩ := residual_of_noB H ((τ.trans σ).toEmbedding.trans f)
    (oldToSource k).1 notB mapped
  exact ⟨r, τ.trans σ, hr⟩

end Aris4Math.ThirtyFour.TwentyThreeFourLowClassified
#print axioms Aris4Math.ThirtyFour.TwentyThreeFourLowClassified.actual_residual
'''
(OUT/'TwentyThreeFourLowClassified.lean').write_text(s)
print({'strict':len(pure)+len(joint),'residual':res,'binding_checked_python':50})
