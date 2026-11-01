"""Export the saved q=9 and tenth-lock bare certificates without searching."""
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'context/propertyb34/round01/high-math'
FORMAL = ROOT / 'formal/Aris4Math/ThirtyFour'

def fl(xs): return '['+','.join(map(str,xs))+']'
def fs(xs): return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def bits(mask,n): return [i for i in range(n) if mask>>i&1]
def tr(mask,n): return fs(bits(mask,n))

def data_case(c,row,n):
    counts = sorted((int(k),v) for k,v in row['counts'].items() if v)
    pos=row['positions']
    mu=''.join(f'if T={tr(t,n)} then {m} else ' for t,m in counts)+'0'
    labels='['+','.join(tr(t,n) for t,_ in counts)+']'
    computed='⟨25,'+fl(sorted(pos))+',['+','.join('⟨'+fl(sorted(pos[i] for i in bits(t,n)))+','+str(m)+'⟩' for t,m in counts)+'],none,[]⟩'
    return f'''namespace Case{c}
def positionFn : Fin {n} → Fin 25 := !{fl([x-1 for x in pos])}
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin {n} ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin {n})) := {labels}
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin {n})) : ℕ := if T ∈ labels then ({mu}) else 0
theorem support (T : Finset (Fin {n})) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := {computed}
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case{c}
'''

def numeric_case(c,row,n):
    value=Fraction(row['bound'])
    assert value<1
    return f'''namespace Case{c}
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = ({value.numerator}/{value.denominator} : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin {n} ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case{c}
'''

def generate(label,rows,n,bare_checked=False):
    if not bare_checked:
        assert all(all(Fraction(c['loss'])==0 for c in row['certificates']) for row in rows)
    ns=f'TwentyFive{label}'
    header=f'''namespace Aris4Math.ThirtyFour.{ns}
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
    tail=f'end Aris4Math.ThirtyFour.{ns}\n'
    data='import Aris4Math.ThirtyFour.CachedSparseApplication\n'+header
    data+='\n'.join(data_case(c,row,n) for c,row in enumerate(rows))
    data+=f'def μ : Fin {len(rows)} → Finset (Fin {n}) → ℕ := !['+','.join(f'Case{c}.μ' for c in range(len(rows)))+']\n'
    data+=tail
    (FORMAL/f'{ns}Data.lean').write_text(data)
    strict=[(c,row) for c,row in enumerate(rows) if Fraction(row['bound'])<1]
    modules=[]
    for start in range(0,len(strict),12):
        batch=start//12
        module=f'{ns}Numeric{batch}'
        s=f'import Aris4Math.ThirtyFour.{ns}Data\n'+header
        s+='\n'.join(numeric_case(c,row,n) for c,row in strict[start:start+12])+tail
        (FORMAL/f'{module}.lean').write_text(s)
        modules.append(module)
    out=dict(group=label,cases=len(rows),strict=len(strict),residuals=[c for c,row in enumerate(rows) if Fraction(row['bound'])>=1],
             data=f'{ns}Data',batches=modules)
    print(json.dumps(out))
    return out

if __name__=='__main__':
    q9=json.loads((SOURCE/'V25_NINE_Q9_BOUNDS.json').read_text())['results']
    tenth_source=json.loads((SOURCE/'V25_TENTH_BOUNDS.json').read_text())['results']
    tenth=[c for group in tenth_source for c in group['cases']]
    manifest=[generate('NineLow',q9,9),generate('NineLowTenth',tenth,10)]
    Path(__file__).with_name('Q9_NUMERIC_BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
