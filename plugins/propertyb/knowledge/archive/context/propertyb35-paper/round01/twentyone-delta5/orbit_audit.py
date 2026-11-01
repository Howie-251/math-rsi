"""Independently replay one numeric witness per relabelling orbit and verify every original inventory/position map exactly."""
from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
from replay import verify
HERE=Path(__file__).parent

def arr(ns,width):return tuple(ns.get(m,ns.get(str(m),0)) for m in range(width))
def main():
 st=time.time();checks=[]
 for file,raw,ds,pattern_filter in [('GENERIC_8888_DP.json','GENERIC_FOUR_DOMAIN.json',(8,)*4,True),('GENERIC_78888_DP.json','GENERIC_78888_DOMAIN.json',(7,8,8,8,8),False),('GENERIC_88888_DP.json','GENERIC_88888_DOMAIN.json',(8,)*5,False)]:
  src=json.loads((HERE/file).read_text());assert src['complete'];rawcases=json.loads((HERE/raw).read_text())['cases'];expected={i:r for i,r in enumerate(rawcases) if not pattern_filter or tuple(r['neighbor_degrees'])==ds};cases=src['cases'];assert {r['source_id'] for r in cases}==set(expected);assert len(cases)==len(expected)
  n=len(ds);width=1<<(n+1);representatives={};metadata={z['orbit_id']:z for z in src.get('orbits',[])};seen_ids=set()
  perms=[p for p in itertools.permutations(range(n)) if all(ds[i]==ds[p[i]] for i in range(n))];moves=[[(m&1)|sum(1<<(p[i]+1) for i in range(n) if m>>(i+1)&1) for m in range(width)] for p in perms]
  for r in cases:
   assert tuple(r['neighbor_degrees'])==ds;aa=arr(r['counts'],width);assert aa==arr(expected[r['source_id']]['counts'],width)
   if metadata:
    oid=r['orbit_id'];rep=metadata[oid];seen_ids.add(oid);p=tuple(r['neighbor_permutation']);assert sorted(p)==list(range(n)) and all(ds[i]==ds[p[i]] for i in range(n));move=[(m&1)|sum(1<<(p[i]+1) for i in range(n) if m>>(i+1)&1) for m in range(width)];bb=[0]*width
    for m,x in enumerate(aa):bb[move[m]]=x
    key=tuple(bb);assert key==arr(rep['counts'],width)
   else:
    candidates=[]
    for p,move in zip(perms,moves):
     bb=[0]*width
     for m,x in enumerate(aa):bb[move[m]]=x
     candidates.append((tuple(bb),p))
    key,p=min(candidates);rep=None
   cp=[r['positions'][0]]+[0]*n
   for i,j in enumerate(p):cp[j+1]=r['positions'][i+1]
   bound=Q(r['bound']);assert r['strict']==(bound<1)
   if rep is not None:assert tuple(cp)==tuple(rep['positions']) and bound==Q(rep['bound'])
   if key not in representatives:
    one=dict(counts=dict(enumerate(key)),positions=cp,bound=bound);assert verify(one)==bound;representatives[key]=(tuple(cp),bound)
   else:assert representatives[key]==(tuple(cp),bound)
  if metadata:assert seen_ids==set(metadata)
  checks.append(dict(file=file,actual_inventory_cases=len(cases),exact_label_and_position_maps=len(cases),numeric_representatives=len(representatives),strict_actual_cases=sum(r['strict'] for r in cases)));print(checks[-1],flush=True)
 result=dict(status='PASS',scope=__doc__,checks=checks,total_actual_cases=sum(z['actual_inventory_cases'] for z in checks),total_numeric_representatives=sum(z['numeric_representatives'] for z in checks),elapsed_seconds=time.time()-st);(HERE/'ORBIT_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
