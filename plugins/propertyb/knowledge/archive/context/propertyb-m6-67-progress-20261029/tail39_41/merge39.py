"""Merge successful bounded runs; no additional probability computation."""
import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent
j=json.loads((P/'WEAK_FOUR39.json').read_text());rep=json.loads((P/'WEAK_REPAIR39.json').read_text())
def key(r):return (tuple(r['degrees']),r['double'],tuple(r['blocks']))
lookup={key(r):r for r in rep['rows']};rows=[]
for row in j['rows']:
 r=lookup.get(key(row),row);assert r['strict'];ell={}
 for b in r['blocks']:ell[b]=ell.get(b,0)+1
 for i,d in enumerate(r['degrees']):ell[1<<i]=d-sum(n for b,n in ell.items() if b&(1<<i))
 ell[0]=66-sum(ell.values());assert sum(ell.values())==66 and min(ell.values())>=0
 rows.append(dict(r,ell=ell))
out=dict(v=39,M=66,patterns=j['patterns'],profiles=len(rows),strict=len(rows),maximum=str(max(Fraction(r['U']) for r in rows)),cpu_seconds=j['cpu_seconds']+rep['cpu_seconds'],rows=rows)
(P/'CERT39.json').write_text(json.dumps(out,indent=2));print(out['profiles'],out['strict'],out['maximum'])
