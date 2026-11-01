"""All selected degree7..12 pairs with combined high excess<=3, lambda>=5."""
from pathlib import Path
from fractions import Fraction
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
out=[]
for d1 in range(7,13):
 for d2 in range(d1,13):
  if max(d1-9,0)+max(d2-9,0)>3:continue
  for c in range(5,d1+1):
   ns={0:35-d1-d2+c,1:d1-c,2:d2-c,3:c}
   ts=[frozenset(v+1 for v in range(2) if m>>v&1) for m,n in ns.items() for _ in range(n)]
   assert len(ts)==35
   cert=[]
   for pos in ((10,21),(21,10)):
    rr=independent_rows(21,pos,ts);val=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
    cert.append((val,pos,rr))
   value,pos,rr=min(cert,key=lambda z:z[0])
   out.append(dict(degrees=[d1,d2],codegree=c,counts=ns,positions=pos,bound=str(value),strict=value<1,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]))
assert all(z['strict'] for z in out)
res=dict(status='PASS',scope=__doc__,cases=out,total=len(out),maximum=str(max(Fraction(z['bound']) for z in out)),original_stubs_per_case=35,ordered_distinct_pairs_per_case=1190,quota=0,cpu_seconds=time.process_time()-st)
(P/'PAIR_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k!='cases'})
