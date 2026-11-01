from pathlib import Path
from fractions import Fraction
import sys,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01'),str(Path(__file__).parent)]
from multilock import Profile,rows,total_bound,json_value
from independent_structure_bounds import independent_rows
from pure_quota import certificate
from six_seven import profiles
src=json.loads(Path(__file__).with_name('SIX_SEVEN_V24.json').read_text());dp=json.loads(Path(__file__).with_name('POSITION_DP.json').read_text());out=[]
for x in src['results']:
 counts={int(t):n for t,n in x['counts'].items()};pos=x['positions']
 if Fraction(x['bound'])>=1:
  z=next(z for z in dp['results'] if z.get('bad')==[0,1]);assert counts=={int(t):n for t,n in z['counts'].items()};pos=z['positions']
 p=Profile(24,5,pos,counts);cs=[certificate(p,i) for i in range(6)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(6)});b=total_bound(rs)
 assert b<1
 stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in counts.items() for _ in range(n)]
 ir=independent_rows(24,pos,stubs)
 assert all(all(a[z]==c[z] for z in ('A','B','C')) for a,c in zip(rs,ir))
 assert sum(counts.values())==34
 assert all(sum(n for t,n in counts.items() if t&(1<<i))==7 for i in range(6))
 out.append(dict(group=x['group'],extra=x['extra'],blocks=x['blocks'],positions=pos,counts=counts,bound=b,certificates=cs,rows=rs,independent_ABC=True))
nums=[dict(extra=e,raw=profiles(e)[1],orbits=len(profiles(e)[0])) for e in (0,1)]
Path(__file__).with_name('V24_NO_SIX_CERTIFICATES.json').write_text(json.dumps(json_value(dict(scope='Complete 46 orbit input catalogue for six degree-seven locks whose pair codegrees are all one except at most one two. Exact 34-edge profiles. Selection and recursion coverage in DERIVATION_PACKAGE.md; not Lean.',catalogues=nums,passed=len(out),worst=max(z['bound'] for z in out),results=out)),indent=2)+'\n')
print(nums,'PASS',len(out),'worst',max(z['bound'] for z in out))
