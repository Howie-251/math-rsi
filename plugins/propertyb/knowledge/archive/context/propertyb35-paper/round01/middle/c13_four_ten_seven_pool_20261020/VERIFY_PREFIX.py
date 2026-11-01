"""Independent470-domain count and only the actual five checked fixed certificates."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
dom=json.loads((P/'WORST_SOURCE_DOMAIN.json').read_text());checked=json.loads((P/'RESULT.json').read_text())
PP=(3,5,6,9,10,12);mu=dom['source_counts']
def weak(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for rest in weak(n-a,k-1):yield(a,)+rest
keys=set()
for c0 in range(8):
 for cp in weak(7-c0,6):
  if any(c>mu[p] for p,c in zip(PP,cp)):continue
  rows=tuple(sum(c for p,c in zip(PP,cp) if p>>v&1) for v in range(4))
  if any(not 1<=r<=4 for r in rows):continue
  keys.add((cp,c0))
expected={(tuple(z['c_pair']),z['c0']) for z in dom['cases']};assert keys==expected and len(keys)==470
cert=[]
for z in checked['cases']:
 ns={int(m):n for m,n in z['counts'].items()};masks=[m for m,n in ns.items() for _ in range(n)];assert len(masks)==35
 ts=[frozenset(v+1 for v in range(5) if m>>v&1) for m in masks]
 rows=independent_rows(21,tuple(z['positions']),ts);U=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
 assert U==Fraction(z['bound']) and (U<1)==z['strict']
 cert.append(dict(c_pair=z['c_pair'],c0=z['c0'],inclusive_z_to_K=z['inclusive_z_to_K'],counts=ns,expanded35_masks=masks,positions=z['positions'],bound=str(U),strict=U<1,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rows]))
out=dict(status='PASS_COMPLETE470_DOMAIN_AND_FIVE_CHECKED_PREFIX_BOUNDS',scope=__doc__,complete_domain=470,checked_prefix=5,strict_prefix=4,first_nonstrict=cert[-1],other465_not_evaluated=True,all_checked_bounds_equal=True,cases=cert,cpu_seconds=time.process_time()-st)
(P/'VERIFY_PREFIX.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('cases','first_nonstrict')})
