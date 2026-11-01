"""Bind the existing 374 uncolored families to the 147 feasible q=9 cases."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'context/propertyb34/round01/high-math'
FORMAL=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(SOURCE))
from unit_catalogue import fullblocks

def fs(xs): return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n=9): return fs([i for i in range(n) if t>>i&1])
def family(ts): return '∅' if not ts else '{'+','.join(tr(t) for t in ts)+'}'

rows=json.loads((SOURCE/'V25_NINE_Q9_CATALOGUE.json').read_text())['results']
uncolored=json.loads((SOURCE/'UNIT_CATALOGUE_9.json').read_text())['orbits']
assert len(rows)==147 and len(uncolored)==374
for r in rows: assert uncolored[r['base']]==r['large_blocks']
indices={r['base']:r['id'] for r in rows}
hdr='''namespace Aris4Math.ThirtyFour.TwentyFiveNineLowInventory
open TwentyFiveUnitCounts Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s='import Aris4Math.ThirtyFour.TwentyFiveInventorySupport\nimport Aris4Math.ThirtyFour.TwentyFiveUnitCounts\nimport Aris4Math.ThirtyFour.TwentyFiveNineLowData\n'+hdr
s+='def big : Fin 147 → Finset (Finset (Fin 9)) := !['+',\n'.join(family(r['large_blocks']) for r in rows)+']\n'
s+='def blockLabels : Fin 147 → List (Finset (Fin 9)) := !['+',\n'.join('['+','.join(tr(t) for t in fullblocks(r['large_blocks'],9))+']' for r in rows)+']\n'
s+='def full (c : Fin 147) : Finset (Finset (Fin 9)) := (blockLabels c).toFinset\n'
s+='theorem completion : ∀ c, pairCompletion (big c)=full c := by decide +kernel\n'
# Splitting the arithmetic recovery avoids a single giant proof whose error
# or recompilation would obscure the responsible finite input.
for r in rows:
 i=r['id']
 s+=f'''theorem recovered{i} : ∀ T : Finset (Fin 9),
+  inventory 34 (fun _ => 6) (full {i}) T=TwentyFiveNineLow.Case{i}.μ T := by
+  apply TwentyFiveInventorySupport.eq_of_support
+  · have included : (TwentyFiveNineLow.Case{i}.labels).all
+        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels {i})))=true := by decide +kernel
+    intro T pos
+    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLow.Case{i}.support T pos))
+  · decide +kernel
+'''.replace('\n+','\n')
s+='theorem recovered (c : Fin 147) (T : Finset (Fin 9)) :\n  inventory 34 (fun _ => 6) (pairCompletion (big c)) T=TwentyFiveNineLow.μ c T := by\n  rw [completion]\n  fin_cases c\n'
for r in rows:s+=f'  · exact recovered{r["id"]} T\n'
s+='end Aris4Math.ThirtyFour.TwentyFiveNineLowInventory\n'
(FORMAL/'TwentyFiveNineLowInventory.lean').write_text(s)

s='''import Aris4Math.ThirtyFour.TwentyFiveUnit9Actual
import Aris4Math.ThirtyFour.TwentyFiveNineLowInventory
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.K6Classification
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def selectedCase : Fin 374 → Fin 147 := !['+','.join(str(indices.get(c,0)) for c in range(374))+']\n'
s+='''theorem feasible_case : ∀ c, Feasible 34 (fun _ => 6) (pairCompletion (TwentyFiveUnit9Data.catalogue c)) →
  TwentyFiveUnit9Data.catalogue c=TwentyFiveNineLowInventory.big (selectedCase c) := by decide +kernel

/-- Every actual nine-low unit choice is represented, with all true counts. -/
theorem actual (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 9 ↪ Fin 25) (unit : Unit H f) (degrees : ∀ i, H.degree (f i)=6) :
    ∃ c : Fin 147, ∃ σ : Equiv.Perm (Fin 9),
      large H (σ.toEmbedding.trans f)=TwentyFiveNineLowInventory.big c ∧
      (∀ T, count H (σ.toEmbedding.trans f) T=TwentyFiveNineLow.μ c T) := by
  obtain ⟨c,σ,same⟩ := TwentyFiveUnit9Actual.actual H f unit
  let g := σ.toEmbedding.trans f
  have gUnit : Unit H g := unit_relabel H f unit σ
  obtain ⟨counts,feasible⟩ := actual_inventory H g gUnit (fun _ => 6) (fun i => degrees (σ i))
  rw [edges,show large H g=TwentyFiveUnit9Data.catalogue c from same] at counts feasible
  have normal := feasible_case c feasible
  refine ⟨selectedCase c,σ,same.trans normal,?_⟩
  intro T
  rw [counts T,normal]
  exact TwentyFiveNineLowInventory.recovered (selectedCase c) T
end Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
#print axioms Aris4Math.ThirtyFour.TwentyFiveNineLowClassified.actual
'''
(FORMAL/'TwentyFiveNineLowClassified.lean').write_text(s)
print('wrote q9 inventory and actual classified caller')
