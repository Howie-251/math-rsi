"""Independent direct fifth-unit8 promotion from47 four-view representatives; exact330 fixed replay.
No original two-view join, no DP, LP, SciPy or position search.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from audit21 import verify as fixedraw

def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
def main():
 st=time.time();src=HERE.parent;old=json.loads((src/'FOUR_DOMAIN.json').read_text());rs=[r for r in json.loads((src/'FOUR_REMAINDERS.json').read_text())['cases'] if max(r['neighbor_codegrees'])<=2];ids={r['id'] for r in rs};allowed={key(r['counts'],5) for r in old['labelled'] if r['orbit'] in ids};assert len(rs)==47 and len(allowed)==434
 maps=[[(t&1)|sum(1<<(p[i]+1) for i in range(5) if t>>(i+1)&1) for t in range(64)] for p in permutations(range(5))];projs=[[sum(1<<j for j,i in enumerate([0]+[i for i in range(1,5) if i!=removed]+[5]) if t>>i&1) for t in range(64)] for removed in range(1,5)];expected=set();nr=0;states=0;leaves=0;passed=0
 for r in rs:
  ns=key(r['counts'],5);ts=sorted((t for t in range(2,32,2) if ns[t]),key=lambda t:(-t.bit_count(),t));centers=[t for t in range(1,32,2) if ns[t] and t.bit_count()<=4]
  for ct in centers:
   lam=[int(bool(ct>>(i+1)&1)) for i in range(4)];pp={ct:1}
   def visit(j,used):
    nonlocal states,leaves,passed,nr
    states+=1
    if j<len(ts):
     t=ts[j];cap=min(ns[t],7-used,1 if t.bit_count()==4 else 2,*[2-lam[i] for i in range(4) if t>>(i+1)&1])
     for a in range(cap+1):
      pp[t]=a
      for i in range(4):lam[i]+=a*(t>>(i+1)&1)
      visit(j+1,used+a)
      for i in range(4):lam[i]-=a*(t>>(i+1)&1)
     pp.pop(t,None);return
    leaves+=1;p0=7-used
    if p0>ns[0] or min(lam)<1:return
    vv=[0]*64;vv[0]=ns[0]-p0;vv[32]=p0
    for t in range(1,32):a=pp.get(t,0);vv[t]=ns[t]-a;vv[t|32]=a
    for mp in projs:
     v=[0]*32
     for t,n in enumerate(vv):v[mp[t]]+=n
     if tuple(v) not in allowed:return
    passed+=1
    if tuple(vv) in expected:return
    nr+=1
    for mp in maps:
     v=[0]*64
     for t,n in enumerate(vv):v[mp[t]]=n
     expected.add(tuple(v))
   visit(0,0)
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert dom['complete'] and nr==330 and len(expected)==21100 and expected=={key(r['counts'],6) for r in dom['labelled']}
 for r in dom['labelled']:
  ns=key(dom['orbits'][r['orbit']]['counts'],6);p=r['from_representative_neighbor_permutation'];v=[0]*64
  for t,n in enumerate(ns):v[(t&1)|sum(1<<(p[i]+1) for i in range(5) if t>>(i+1)&1)]=n
  assert tuple(v)==key(r['counts'],6)
 dp=json.loads((HERE/'DP.json').read_text());assert dp['complete'] and len(dp['cases'])==330 and {key(r['counts'],6) for r in dp['cases']}=={key(r['counts'],6) for r in dom['orbits']};vals={r['id']:fixedraw(dict(r,quotas=r.get('certificates',r.get('quotas')))) for r in dp['cases']};rem={i for i,v in vals.items() if v>=1};assert len(rem)==106 and rem=={r['id'] for r in json.loads((HERE/'REMAINDERS.json').read_text())['cases']}
 result=dict(status='PASS',scope=__doc__,source_four_orbits=47,source_four_labelled=434,direct_promotion_states=states,promotion_leaves=leaves,all_four_view_passes=passed,independent_true_S5_orbits=nr,independent_labelled_count=len(expected),transport_checks=21100,fixed_certificates=330,fixed_strict=224,remaining=106,max_accepted_bound=str(max(v for v in vals.values() if v<1)),elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
