"""Independent edge-multiset/full-inclusive Mobius five-eight-core expansion and fixed replay.
No position DP, optimizer, or original ternary edge-vector generator is used.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
from collections import Counter
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE.parents[1]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(64))
def main():
 start=time.time();pairs=list(combinations(range(5),2));masks=[sum(1<<i for i in S) for S in pairs];expected={8:set(),9:set()}
 for r in (3,4):
  for mult in combinations_with_replacement(range(10),r):
   ctr=Counter(mult)
   if max(ctr.values())>2:continue
   lam=[sum(n for j,n in ctr.items() if i in pairs[j]) for i in range(5)]
   if min(lam)<1:continue
   pp={masks[j]:n for j,n in ctr.items()}
   for d in (8,9):
    I={}
    for T in range(1,64):
     low=T&31;yy=T&32
     if not yy:I[T]=8 if low.bit_count()==1 else 2 if low.bit_count()==2 else 0
     elif not low:I[T]=d
     elif low.bit_count()==1:I[T]=lam[low.bit_length()-1]
     elif low.bit_count()==2:I[T]=pp.get(low,0)
     else:I[T]=0
    ns={T:sum((-1)**(U.bit_count()-T.bit_count())*n for U,n in I.items() if U&T==T) for T in range(1,64)};ns[0]=35-sum(ns.values());assert min(ns.values())>=0
    expected[d].add(key(ns))
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert len(expected[9])==255 and expected[9]=={key(r['counts']) for r in dom['labelled']}
 for r in dom['labelled']:
  ns={int(t):n for t,n in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_low_permutation'];move=lambda t:(t&32)|sum(1<<p[i] for i in range(5) if t>>i&1)
  assert key({move(t):n for t,n in ns.items()})==key(r['counts'])
 expected8={tuple(n+1 if t==0 else n-1 if t==32 else n for t,n in enumerate(vv)) for vv in expected[9]};assert len(expected[8])==255 and expected[8]==expected8
 nine=json.loads((HERE/'DP.json').read_text());eight=json.loads((HERE/'DEGREE8_DP.json').read_text());assert nine['complete'] and eight['complete'] and len(nine['cases'])==len(eight['cases'])==7
 summary=[]
 for d,rs in ((9,nine['cases']),(8,eight['cases'])):
  vals=[]
  for r in rs:
   vv=key(dom['orbits'][r['id']]['counts']);vv=tuple(n+1 if t==0 else n-1 if t==32 else n for t,n in enumerate(vv)) if d==8 else vv
   assert key(r['counts'])==vv
   val=fixed(r);assert val==Q(r['bound'])<1;vals.append(val)
  summary.append(dict(external_degree=d,orbit_count=7,all_fixed_strict=True,max_bound=str(max(vals))))
 result=dict(status='PASS',scope=__doc__,independent_labelled_per_degree=255,true_S5_orbits_per_degree=7,transport_checks=255,certificate_count=14,all_strict=True,degree_cases=summary,elapsed_seconds=time.time()-start)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
