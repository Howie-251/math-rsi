from pathlib import Path
from fractions import Fraction
import json,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,json_value
from independent_structure_bounds import independent_rows
from pure_quota import certificate
out=[]
for suffix in ('3','3_12','3_12_48'):
 p=Path(__file__).with_name('MIXED_SIX_v24_low6_bad'+suffix+'.json');d=json.loads(p.read_text())
 for x in d['results']:
  ns={int(t):n for t,n in x['counts'].items()};pos=x['positions'];p=Profile(24,5,pos,ns);cs=[certificate(p,i) for i in range(6)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(6)});b=total_bound(rs);assert b==Fraction(x['bound'])<1
  stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in ns.items() for _ in range(n)];ir=independent_rows(24,pos,stubs);assert all(all(a[z]==c[z] for z in ('A','B','C')) for a,c in zip(rs,ir))
  out.append(dict(bad=suffix,group=x['group'],bound=b,independent_ABC=True))
Path(__file__).with_name('SIX_LOW_BAD_INDEPENDENT.json').write_text(json.dumps(json_value(dict(passed=len(out),worst=max(x['bound'] for x in out),results=out)),indent=2)+'\n')
print(len(out),'PASS worst',max(x['bound'] for x in out))
