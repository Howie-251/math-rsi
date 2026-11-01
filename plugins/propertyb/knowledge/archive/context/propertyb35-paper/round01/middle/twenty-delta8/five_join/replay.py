"""Independent fifth-point promotion from44 four8 representatives, full S5 closure, fixed/dual replay.
This does not reuse the original join of two four-views over three-point slots.
"""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parents[1]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed,joint

def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
def main():
 start=time.time();old=HERE.parent/'four_projection';dom4=json.loads((old/'DOMAIN.json').read_text());rs=json.loads((old/'FOUR_REMAINDERS.json').read_text())['cases'];ids={r['id'] for r in rs};allowed={key(r['counts'],4) for r in dom4['labelled'] if r['orbit'] in ids};assert len(allowed)==461
 core=tuple(15 if t==0 else 2 if t.bit_count()==2 else 0 for t in range(32));permmaps=[]
 for p in permutations(range(5)):
  m=[sum(1<<p[i] for i in range(5) if t>>i&1) for t in range(32)];permmaps.append(m)
 expected=set();independent_orbits=0;corehits=0;cartesian=0;promoted_pass=0
 for r in rs:
  oldns=key(r['counts'],4);ts=[t for t in range(1,16) if oldns[t]];ranges=[range(min(oldns[t],1 if t==15 else 3)+1) for t in ts]
  for values in product(*ranges):
   cartesian+=1;used=sum(values)
   if used>8:continue
   p0=8-used
   if not 0<=p0<=oldns[0]:continue
   pp=dict(zip(ts,values));lam=[sum(n for t,n in pp.items() if t>>i&1) for i in range(4)]
   if min(lam)<1 or max(lam)>3:continue
   ns=[0]*32;ns[0]=oldns[0]-p0;ns[16]=p0
   for t in range(1,16):p=pp.get(t,0);ns[t]=oldns[t]-p;ns[t|16]=p
   passed=True
   for removed in range(4):
    order=[i for i in range(4) if i!=removed]+[4];proj=[0]*16
    for t,n in enumerate(ns):proj[sum(1<<j for j,i in enumerate(order) if t>>i&1)]+=n
    if tuple(proj) not in allowed:passed=False;break
   if not passed:continue
   promoted_pass+=1;kk=tuple(ns)
   if kk==core:corehits+=1;continue
   if kk in expected:continue
   independent_orbits+=1
   for m in permmaps:
    vv=[0]*32
    for t,n in enumerate(ns):vv[m[t]]=n
    expected.add(tuple(vv))
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert independent_orbits==361 and len(expected)==23995 and expected=={key(r['counts'],5) for r in dom['labelled']}
 for r in dom['labelled']:
  ns={int(t):n for t,n in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_permutation'];move=lambda t:sum(1<<p[i] for i in range(5) if t>>i&1)
  assert key({move(t):n for t,n in ns.items()},5)==key(r['counts'],5)
 dp=json.loads((HERE/'FIVE_DP.json').read_text());assert dp['complete'] and len(dp['cases'])==361;vals={r['id']:fixed(r) for r in dp['cases']};pure={i for i,v in vals.items() if v<1};js=[]
 for z in json.loads((HERE/'FIVE_JOINT.json').read_text())['results']:
  if Q(z.get('bound','2'))>=1:continue
  verified=joint.verify(z,v=20,s=5,expected_degrees=[8]*5);vals[z['source_id']]=Q(verified['bound']);js.append(z['source_id'])
 rem={i for i,v in vals.items() if v>=1};assert len(rem)==49 and rem=={r['id'] for r in json.loads((HERE/'FIVE_REMAINDERS.json').read_text())['cases']}
 result=dict(status='PASS',scope=__doc__,old_four_seed_representatives=44,single_promotion_cartesian=cartesian,all_four_projection_pass=promoted_pass,core_excluded=corehits,independent_true_S5_orbits=361,independent_labelled_count=23995,transports=23995,fixed_strict=len(pure),joint_strict=len(js),remaining_count=49,remaining_ids=sorted(rem),max_accepted_bound=str(max(v for v in vals.values() if v<1)),elapsed_seconds=time.time()-start)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
