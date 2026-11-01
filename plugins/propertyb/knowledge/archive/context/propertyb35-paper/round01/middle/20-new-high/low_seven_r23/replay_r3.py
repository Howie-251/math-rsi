"""Independent exact reconstruction of actual r3 domains and fixed/dual certificate replay.
No DP, SciPy or position search is used. All promotions are over actual old trace slots.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations,combinations
import json,time,sys
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(HERE.parents[1]/'twenty_remaining'),str(ROOT/'context/propertyb34/round01/middle-math')]
from audit_core import verify as verify_fixed
import verify_joint_layout as joint

def check35(ns,s,v,expected_degrees=None):
 assert v==20 and sum(ns.values())==35 and all(n>=0 and t.bit_count()<=5 for t,n in ns.items())
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees))
 return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
joint.check_profile=check35

def load(f):return json.loads((HERE/f).read_text())
def key(ns,s):return tuple(int(ns.get(t,ns.get(str(t),0))) for t in range(1<<s))
def fixed(r):return verify_fixed(dict(r,quotas=r.get('certificates',r.get('quotas'))))
def main():
 start=time.time();up=json.loads((HERE.parent/'DIAGNOSIS.json').read_text());strong=[]
 for r in up['pairs']:
  a,b=r['degrees'];c=r['codegree']
  if a in (8,9) and b in (8,9) and c>=5:
   assert fixed(r)<1;strong.append((a,b,c))
 expectedstrong={(8,8,c) for c in range(5,9)}|{(8,9,c) for c in range(5,9)}|{(9,9,c) for c in range(5,10)}
 assert set(strong)==expectedstrong
 proj=load('PROJECTIONS.json')['cases'];lookup={};pjoint=0
 for r in proj:
  val=fixed(r);strict=val<1
  if r.get('joint') and Q(r['joint'].get('bound','2'))<1:
   joint.verify(r['joint'],v=20,s=3,expected_degrees=[7,7,r['degree']]);strict=True;pjoint+=1
  assert strict==r['strict'];lookup[(r['low_codegree'],r['degree'],*r['cross'],r['triple'])]=strict
 expectedproj=set()
 for c,d,a,b in product((1,2,3),(8,9),(1,2,3),(1,2,3)):
  for t in range(min(c,a,b)+1):
   ns={7:t,3:c-t,5:a-t,6:b-t,1:7-c-a+t,2:7-c-b+t,4:d-a-b+t};ns[0]=35-sum(ns.values())
   if min(ns.values())>=0:expectedproj.add((c,d,a,b,t))
 assert len(expectedproj)==126 and set(lookup)==expectedproj
 bases=set()
 for c12,c13,c23 in product((1,2),repeat=3):
  for t in range(min(c12,c13,c23)+1):
   ns={7:t,3:c12-t,5:c13-t,6:c23-t,1:7-c12-c13+t,2:7-c12-c23+t,4:7-c13-c23+t};ns[0]=35-sum(ns.values())
   if min(ns.values())>=0:bases.add(key(ns,3))
 assert len(bases)==17
 dom=load('R3_WEAK_ONE_DOMAIN.json');expected=set()
 for n in bases:
  cs=[sum(v for t,v in enumerate(n) if t&m==m) for m in (3,5,6)]
  for a in product(*(range(min(n[t],3)+1) for t in range(1,8))):
   p=(0,*a);lam=[sum(v for t,v in enumerate(p) if t>>i&1) for i in range(3)]
   if min(lam)<1 or max(lam)>3 or sum(lam)>6:continue
   tau=[sum(v for t,v in enumerate(p) if t&m==m) for m in (3,5,6)]
   for d in (8,9):
    if any(lookup[(c,d,lam[i],lam[j],t)] for (i,j),c,t in zip(combinations(range(3),2),cs,tau)):continue
    p0=d-sum(p)
    if not 0<=p0<=n[0]:continue
    ns={0:n[0]-p0,8:p0}
    for t in range(1,8):ns[t]=n[t]-p[t];ns[t|8]=p[t]
    expected.add(key(ns,4))
 assert len(expected)==1348 and expected=={key(r['counts'],4) for r in dom['labelled']}
 for r in dom['labelled']:
  ns={int(t):v for t,v in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_permutation'];move=lambda t:(t&8)|sum(1<<p[i] for i in range(3) if t>>i&1)
  assert key({move(t):v for t,v in ns.items()},4)==key(r['counts'],4)
 dp=load('R3_WEAK_ONE_DP.json')['cases'];strictone={r['id'] for r in dp if fixed(r)<1};jstrict=[]
 for z in load('R3_WEAK_ONE_JOINT.json')['results']:
  if Q(z.get('bound','2'))<1:
   r=dp[z['source_id']];joint.verify(z,v=20,s=4,expected_degrees=[7,7,7,r['degree']]);strictone.add(r['id']);jstrict.append(z['source_id'])
 residual=set(range(len(dp)))-strictone;assert len(dp)==344 and len(residual)==16
 groups={}
 for r in dom['labelled']:
  if r['orbit'] not in residual:continue
  ns=key(r['counts'],4);n=tuple(ns[t]+ns[t|8] for t in range(8));a=tuple(ns[t|8] for t in range(8));d=sum(a);groups.setdefault(n,set()).add((d,a))
 expectedtwo=set()
 for n,views in groups.items():
  for da,a in views:
   for db,b in views:
    if da>db:continue
    ranges=[range(max(0,a[t]+b[t]-n[t]),min(a[t],b[t],1 if t==7 else 35)+1) for t in range(8)]
    for q in product(*ranges):
     if not 1<=sum(q)<=4:continue
     ns={}
     for t in range(8):ns[t]=n[t]-a[t]-b[t]+q[t];ns[t|8]=a[t]-q[t];ns[t|16]=b[t]-q[t];ns[t|24]=q[t]
     expectedtwo.add((da,db,key(ns,5)))
 two=load('R3_TWO_DOMAIN.json');actual={(r['degrees'][3],r['degrees'][4],key(r['counts'],5)) for r in two['labelled']}
 assert len(expectedtwo)==2100 and expectedtwo==actual
 for r in two['labelled']:
  rep=two['orbits'][r['orbit']];ns={int(t):v for t,v in rep['counts'].items()};p=r['from_representative_low_permutation'];swap=r['from_representative_outside_swap'];assert not swap or r['degrees'][3]==r['degrees'][4]
  def move(t):return sum(1<<p[i] for i in range(3) if t>>i&1)|((((t&8)<<1)|((t&16)>>1)) if swap else (t&24))
  assert key({move(t):v for t,v in ns.items()},5)==key(r['counts'],5)
 dp2=load('R3_TWO_DP.json');assert dp2['complete'] and len(dp2['cases'])==500
 vals={r['id']:fixed(r) for r in dp2['cases']};dpstrict=sum(v<1 for v in vals.values());jointvals=[]
 for z in load('R3_TWO_JOINT.json')['results']:
  r=dp2['cases'][z['source_id']];verified=joint.verify(z,v=20,s=5,expected_degrees=r['degrees']);v=Q(verified['bound']);assert v<1;vals[r['id']]=v;jointvals.append(v)
 assert all(v<1 for v in vals.values())
 result=dict(status='PASS',scope=__doc__,strong_high_pairs=len(strong),projections=126,projection_strict=sum(lookup.values()),projection_joint_strict=pjoint,low_bases=17,one_labelled=1348,one_orbits=344,one_fixed_strict=len(strictone)-len(jstrict),one_joint_strict=len(jstrict),one_residuals=sorted(residual),two_labelled=2100,two_orbits=500,two_fixed_strict=dpstrict,two_joint_strict=len(jointvals),two_all_strict=True,two_max=str(max(vals.values())),two_max_id=max(vals,key=vals.get),elapsed_seconds=time.time()-start)
 (HERE/'R3_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
