"""T34 v22 delta>=7: strengthen the thirteen saved six-lock residuals.
Fixed saved positions first; new avoided-subfamily quota certificates, not a
repeat of the exhausted pure/total placement search. Exact replay is saved.
"""
from pathlib import Path
from fractions import Fraction
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,json_value
from avoided_lock_quotas import certificate
from independent_structure_bounds import independent_rows

def main():
 start=perf_counter();out=[]
 source=json.loads((ROOT/'context/propertyb34-hour1-20261013/MIDDLE_SIX_RESIDUE_RESULTS.json').read_text())
 for g in source['results']:
  for w in g['witnesses']:
   if Fraction(w['bound'])<1:continue
   counts={int(t):n for t,n in w['counts'].items()}
   p=Profile(22,5,tuple(w['positions']),counts)
   cs=[certificate(p,i) for i in range(6)]
   rs=rows(p,deductions={c['position']:c['loss'] for c in cs})
   b=total_bound(rs)
   stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in counts.items() for _ in range(n)]
   ir=independent_rows(22,p.positions,stubs)
   assert all(all(a[k]==c[k] for k in ['A','B','C']) for a,c in zip(rs,ir))
   assert sum(counts.values())==34
   assert all(sum(n for t,n in counts.items() if t&(1<<i))==7 for i in range(6))
   out.append(dict(graph=g['graph'],group=w['group'],old_bound=w['bound'],bound=b,positions=p.positions,counts=counts,certificates=cs,rows=rs,independent_ABC=True))
   print(g['graph'],w['group'],w['bound'],'->',b,b<1,flush=True)
   (HERE/'AVOIDED_THIRTEEN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==13,elapsed_seconds=perf_counter()-start,results=out)),indent=2)+'\n')
   if perf_counter()-start>90:break
 print('passed',sum(w['bound']<1 for w in out),'/',len(out),'seconds',perf_counter()-start,flush=True)

if __name__=='__main__':main()
