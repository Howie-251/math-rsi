"""Independent single-sixth-point promotion from49 five8 representatives; exact certificate replay.
No original two-view intersection join, no DP, no SciPy, no layout search.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parents[1]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed,joint

def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
def main():
 start=time.time();src=HERE.parent/'five_join';old=json.loads((src/'DOMAIN.json').read_text());rs=json.loads((src/'FIVE_REMAINDERS.json').read_text())['cases'];ids={r['id'] for r in rs};allowed={key(r['counts'],5) for r in old['labelled'] if r['orbit'] in ids};assert len(allowed)==1505
 maps=[[sum(1<<p[i] for i in range(6) if t>>i&1) for t in range(64)] for p in permutations(range(6))];expected=set();nr=0;leaves=0;passes=0;states=0
 for r in rs:
  ns=key(r['counts'],5);ts=sorted((t for t in range(1,31) if ns[t]),key=lambda t:(-t.bit_count(),t));pp={31:0};lam=[0]*5
  def visit(j,used):
   nonlocal nr,leaves,passes,states
   states+=1
   if j<len(ts):
    t=ts[j];cap=min(ns[t],8-used,1 if t.bit_count()==4 else 3,*[3-lam[i] for i in range(5) if t>>i&1])
    for a in range(cap+1):
     pp[t]=a
     for i in range(5):lam[i]+=a*(t>>i&1)
     visit(j+1,used+a)
     for i in range(5):lam[i]-=a*(t>>i&1)
    pp.pop(t,None);return
   leaves+=1;p0=8-used
   if p0>ns[0] or min(lam)<1:return
   vv=[0]*64;vv[0]=ns[0]-p0;vv[32]=p0
   for t in range(1,32):a=pp.get(t,0);vv[t]=ns[t]-a;vv[t|32]=a
   for removed in range(5):
    order=[i for i in range(5) if i!=removed]+[5];proj=[0]*32
    for t,n in enumerate(vv):proj[sum(1<<j for j,i in enumerate(order) if t>>i&1)]+=n
    if tuple(proj) not in allowed:return
   passes+=1
   if tuple(vv) in expected:return
   nr+=1
   for m in maps:
    w=[0]*64
    for t,n in enumerate(vv):w[m[t]]=n
    expected.add(tuple(w))
  visit(0,0)
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert dom['complete'];assert nr==136 and len(expected)==35915 and expected=={key(r['counts'],6) for r in dom['labelled']}
 for r in dom['labelled']:
  ns=key(dom['orbits'][r['orbit']]['counts'],6);p=r['from_representative_permutation'];vv=[0]*64
  for t,n in enumerate(ns):vv[sum(1<<p[i] for i in range(6) if t>>i&1)]=n
  assert tuple(vv)==key(r['counts'],6)
 dp=json.loads((HERE/'SIX_DP.json').read_text());assert dp['complete'] and len(dp['cases'])==136;vals={r['id']:fixed(r) for r in dp['cases']};fixedn=sum(v<1 for v in vals.values());jn=0
 for z in json.loads((HERE/'SIX_JOINT.json').read_text())['results']:
  if Q(z.get('bound','2'))<1:vals[z['source_id']]=Q(joint.verify(z,v=20,s=6,expected_degrees=[8]*6)['bound']);jn+=1
 assert len(vals)==136 and max(vals.values())<1
 result=dict(status='PASS',scope=__doc__,source_five_representatives=len(rs),recursive_states=states,promotion_leaves=leaves,all_five_passes=passes,independent_true_S6_orbits=nr,independent_labelled_count=len(expected),transport_checks=len(expected),fixed_strict=fixedn,joint_strict=jn,remaining_count=0,max_accepted_bound=str(max(vals.values())),elapsed_seconds=time.time()-start)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
