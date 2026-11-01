"""Independent labelled-stub / falling-injection verification, all positive layouts and slots."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
from multilock import json_value
here=Path(__file__).parent

def verify(x,s,v):
 ns={int(t):n for t,n in x['counts'].items()};N=v-s
 assert sum(ns.values())==34
 assert all(sum(n for t,n in ns.items() if t&(1<<i))==6 for i in range(s))
 assert all(sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))==1 for i in range(s) for j in range(i))
 stubs=[frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in ns.items() for _ in range(n)]
 free=Fraction();av=[[Fraction() for _ in c['slots']] for c in x['centers']];mass=Fraction()
 for z in x['witnesses']:
  p=Fraction(z['probability']);pos=z['positions'];assert p>=0;mass+=p
  assert len(pos)==len(set(pos))==s and min(pos)>=1 and max(pos)<=v
  rs=independent_rows(v,pos,stubs)
  free+=p*sum((r['bound'] for r in rs if r['k'] not in pos),Fraction())
  def w(t,u,i):
   bit=1<<i;k=pos[i];left=sum(1<<j for j in range(s) if pos[j]<k);right=sum(1<<j for j in range(s) if pos[j]>k)
   if t&u!=bit or (t^bit)&~left or (u^bit)&~right:return Fraction()
   a=k-1-left.bit_count();b=v-k-right.bit_count()
   return injection_probability(N,a,b,5-t.bit_count(),5-u.bit_count(),False)
  for i,c in enumerate(x['centers']):
   r=rs[pos[i]-1]
   for j,(t,u) in enumerate(c['slots']):
    loss=w(t,u,i)+w(u,t,i);assert loss<=r['C']
    av[i][j]+=p*min(r['A'],r['B'],r['C']-loss)
 assert mass==1 and free==Fraction(x['free_average'])
 for c,a in zip(x['centers'],av):
  assert a==[Fraction(v) for v in c['averages']]
  assert max(a)==Fraction(c['maximum'])
 b=free+sum(max(a) for a in av);assert b==Fraction(x['bound'])<1
 return dict(group=x['group'],bound=b,layouts=len(x['witnesses']),independent_injection=True)

if __name__=='__main__':
 start=time.perf_counter();source=Path(sys.argv[1]);s=int(sys.argv[2]);out=[]
 for x in json.loads(source.read_text())['results']:
  if Fraction(x['bound'])>=1:continue
  out.append(verify(x,s,24));print(out[-1],flush=True)
 source.with_name(source.stem+'_INDEPENDENT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
