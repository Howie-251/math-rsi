"""Replace costly recomputation in exact 9/10-lock completions by list checks."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4];S=ROOT/'context/propertyb34/round01/high-math';F=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(S));from unit_catalogue import fullblocks

def fs(xs):return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n):return fs([i for i in range(n) if t>>i&1])
def listed(ts,n):return '['+','.join(tr(t,n) for t in ts)+']'
q9=json.loads((S/'V25_NINE_Q9_CATALOGUE.json').read_text())['results']
tenth=[c for g in json.loads((S/'V25_TENTH_BOUNDS.json').read_text())['results'] for c in g['cases']]
for name,n,bigs in [('TwentyFiveNineLowInventory',9,[r['large_blocks'] for r in q9]),('TwentyFiveNineLowTenthInventory',10,[[int(t) for t,v in r['counts'].items() if v and int(t).bit_count()>=3] for r in tenth])]:
 p=F/(name+'.lean');s=p.read_text();start=s.index('theorem completion');end=s.index('theorem recovered0',start)
 t=''
 for i,big in enumerate(bigs):
  literal=listed(big,n);full=listed(fullblocks(big,n),n)
  t+=f'''theorem completion{i} : pairCompletion (big {i})=full {i} := by
  have same : big {i}=({literal} : List (Finset (Fin {n}))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check {literal} {full}=true
  decide +kernel
'''
 t+='theorem completion : ∀ c,pairCompletion (big c)=full c := by\n  intro c\n  fin_cases c\n'
 for i in range(len(bigs)):t+=f'  · exact completion{i}\n'
 s=s[:start]+t+s[end:]
 if 'import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion\n' not in s:s='import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion\n'+s
 p.write_text(s)
print('replaced 147 + 25 full completion checks')
