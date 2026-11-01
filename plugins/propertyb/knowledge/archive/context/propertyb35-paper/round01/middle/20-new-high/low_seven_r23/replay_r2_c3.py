"""Independent actual c3 r2 domain, certificate and global residual-structure audit.
Use arbitrary three real w=0 outsiders; no optimizer/DP/Scipy is run.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE))
from replay_r3 import fixed,joint

def load(f):return json.loads((HERE/f).read_text())
def vec(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
def project(ns,order):
 out=[0]*(1<<len(order))
 for t,n in ns.items():out[sum(1<<i for i,j in enumerate(order) if int(t)>>j&1)]+=n
 return tuple(out)
def canonical(ns,degrees,groups):
 vv=vec(ns,len(degrees));keys=[]
 for orders in product(*(permutations(g) for g in groups)):
  order=sum((tuple(p) for p in orders),())
  if tuple(degrees[j] for j in order)!=tuple(degrees):continue
  keys.append(project(dict(enumerate(vv)),order))
 return (tuple(degrees),min(keys))
def newprojkey(ns,degrees,order):
 dd=tuple(sorted(degrees[i] for i in order));vvs=[]
 for p in permutations(order):
  if tuple(degrees[i] for i in p)==dd:vvs.append(project(ns,p))
 return dd,min(vvs)
def main():
 start=time.time();w1=0;highpairs=0
 for r in load('PROJECTIONS.json')['cases']:
  if r['low_codegree']==3 and sum(r['cross'])==3:
   val=fixed(r)
   if val>=1:
    joint.verify(r['joint'],v=20,s=3,expected_degrees=[7,7,r['degree']]);val=Q(r['joint']['bound'])
   assert val<1;w1+=1
 assert w1==8
 for r in json.loads((HERE.parent/'DIAGNOSIS.json').read_text())['pairs']:
  if min(r['degrees'])>=8 and max(r['degrees'])<=9 and r['codegree']>=5:
   assert fixed(r)<1;highpairs+=1
 assert highpairs==13
 dp=load('R2_TWO_DP.json')['cases'];jmap={r['source_id']:r for r in load('R2_TWO_JOINT.json')['results']};four={};fixedcount=0;jcount=0
 for r in dp:
  if r['low_codegree']!=3:continue
  v=fixed(r);strict=v<1;fixedcount+=1
  if not strict and Q(jmap[r['id']].get('bound','2'))<1:
   joint.verify(jmap[r['id']],v=20,s=4,expected_degrees=r['degrees']);strict=True;jcount+=1
  four[canonical(r['counts'],r['degrees'],((0,1),(2,3)))]=(r['id'],strict)
 # Rebuild precisely all common-low c3 two-outsider inputs with both w0.
 n=(24,4,4,3);views=[(d,(d-1,0,0,1)) for d in (8,9)]+[(d,(d-2,1,1,0)) for d in (8,9)];pairraw=[];groups={}
 for (dy,a),(dz,b) in product(views,repeat=2):
  ranges=[range(max(0,a[t]+b[t]-n[t]),min(a[t],b[t])+1) for t in range(4)]
  for q in product(*ranges):
   if not 1<=sum(q)<=4:continue
   ns={}
   for t in range(4):ns[t]=n[t]-a[t]-b[t]+q[t];ns[t|4]=a[t]-q[t];ns[t|8]=b[t]-q[t];ns[t|12]=q[t]
   pairraw.append((dy,dz,vec(ns,4)));idx,strict=four[canonical(ns,[7,7,dy,dz],((0,1),(2,3)))]
   if strict:continue
   old=tuple(ns[t]+ns[t|8] for t in range(8));prom=tuple(ns[t|8] for t in range(8));groups.setdefault((dy,old),set()).add((dz,prom))
 # Independent comparison with stored raw pair domain at w0 on both outsiders.
 stored=set()
 for r in load('R2_TWO_DOMAIN.json')['labelled']:
  ns={int(t):v for t,v in r['counts'].items()}
  if sum(v for t,v in ns.items() if t&3==3)!=3:continue
  if any(sum(v*((t&3).bit_count()) for t,v in ns.items() if t&b)!=2 for b in (4,8)):continue
  stored.add((r['degrees'][2],r['degrees'][3],vec(ns,4)))
 assert set(pairraw)==stored
 # Exact new triple views and their fixed/joint certificates.
 triple={};triple_fixed=0;triple_joint=0
 for r in load('R2_NEW_PROJECTIONS.json')['cases']:
  v=fixed(r);strict=v<1;triple_fixed+=1
  if not strict and r.get('joint') and Q(r['joint'].get('bound','2'))<1:
   joint.verify(r['joint'],v=20,s=3,expected_degrees=r['degrees']);strict=True;triple_joint+=1
  triple[(tuple(r['degrees']),vec(r['counts'],3))]=strict
 expected=set()
 for (dy,old),vv in groups.items():
  for (dz,a),(dw,b) in product(vv,repeat=2):
   if dz>dw:continue
   ranges=[range(max(0,a[t]+b[t]-old[t]),min(a[t],b[t],1 if t==7 else 35)+1) for t in range(8)]
   for q in product(*ranges):
    if not 1<=sum(q)<=4:continue
    ns={}
    for t in range(8):ns[t]=old[t]-a[t]-b[t]+q[t];ns[t|8]=a[t]-q[t];ns[t|16]=b[t]-q[t];ns[t|24]=q[t]
    deg=[7,7,dy,dz,dw]
    if any(triple[newprojkey(ns,deg,(i,3,4))] for i in range(3)):continue
    # Third common-low four-view must share the same actual H and is also within the pair domain.
    view=project(ns,(0,1,3,4));idx,strict=four[canonical(dict(enumerate(view)),[7,7,dz,dw],((0,1),(2,3)))]
    if strict:continue
    expected.add(canonical(ns,deg,((0,1),(2,),(3,4))))
 selected=[r for r in load('R2_C23_DP.json')['cases'] if sum(v for t,v in r['counts'].items() if int(t)&3==3)==3];actual={canonical(r['counts'],r['degrees'],((0,1),(2,),(3,4))) for r in selected}
 assert len(expected)==18 and expected==actual
 j5={r['source_id']:r for r in load('R2_C23_JOINT.json')['results']};res=[];strictvals=[]
 for r in selected:
  v=fixed(r)
  if v>=1 and Q(j5[r['id']].get('bound','2'))<1:
   joint.verify(j5[r['id']],v=20,s=5,expected_degrees=r['degrees']);v=Q(j5[r['id']]['bound'])
  if v<1:strictvals.append(v);continue
  ns={int(t):n for t,n in r['counts'].items()};paired=[]
  for i in (2,3,4):
   assert sum(n*((t&3).bit_count()) for t,n in ns.items() if t>>i&1)==2
   tau=sum(n for t,n in ns.items() if t&3==3 and t>>i&1);assert tau in (0,1)
   if tau:paired.append(i);assert r['degrees'][i]==9
  assert len(paired)==2
  res.append(dict(source_id=r['id'],degrees=r['degrees'],paired_indices=paired,bound=str(v)))
 assert len(res)==4
 result=dict(status='PASS',scope=__doc__,w1_exclusions=w1,strong_high_pairs=highpairs,c3_four_fixed_replayed=fixedcount,c3_four_strict_joint=jcount,independent_raw_w0_pair_count=len(set(pairraw)),new_triples_replayed=triple_fixed,new_triple_strict_joint=triple_joint,independent_c3_five_orbits=18,five_strict=len(strictvals),five_strict_max=str(max(strictvals)),four_residual_structures=res,global_obligation='For every triple of Z=w0 Q vertices, exactly two are paired and have degree9. |Z|>=3; |Z|>=4 gives3P=8, while |Z|=3 gives Q=10 and at most one degree9 by total175.',elapsed_seconds=time.time()-start)
 (HERE/'R2_C3_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
