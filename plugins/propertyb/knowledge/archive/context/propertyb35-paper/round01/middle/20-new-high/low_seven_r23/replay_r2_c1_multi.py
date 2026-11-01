"""Independent actual c1 and >=2 small-w Q domain and residual-structure audit, no optimizer/search.
Direct old two-low promotions, shared three-point inventory join, third four-view and exact triple projections.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE))
from replay_r2_c3 import fixed,joint,vec,project,canonical,newprojkey

def load(f):return json.loads((HERE/f).read_text())
def main():
 start=time.time();projs=load('PROJECTIONS.json')['cases'];lookup={};pj=0
 for r in projs:
  if r['low_codegree']!=1:continue
  val=fixed(r);strict=val<1
  if not strict and r.get('joint') and Q(r['joint'].get('bound','2'))<1:
   joint.verify(r['joint'],v=20,s=3,expected_degrees=[7,7,r['degree']]);strict=True;pj+=1
  assert strict==r['strict'];lookup[(r['degree'],*r['cross'],r['triple'])]=strict
 dp=load('R2_TWO_DP.json')['cases'];jm={r['source_id']:r for r in load('R2_TWO_JOINT.json')['results']};four={};four_joint=0;four_fixed=0
 for r in dp:
  if r['low_codegree']!=1:continue
  val=fixed(r);strict=val<1;four_fixed+=1
  if not strict and Q(jm[r['id']].get('bound','2'))<1:
   joint.verify(jm[r['id']],v=20,s=4,expected_degrees=r['degrees']);strict=True;four_joint+=1
  four[canonical(r['counts'],r['degrees'],((0,1),(2,3)))]=(r['id'],strict)
 n=(22,6,6,1);views={}
 for budget in (1,2):
  vv=[]
  for p1,p2,p3 in product(range(4),range(4),range(2)):
   la,lb=p1+p3,p2+p3
   if not(1<=la<=3 and 1<=lb<=3 and la+lb<=2+budget):continue
   for d in (8,9):
    if lookup[(d,la,lb,p3)]:continue
    p0=d-p1-p2-p3
    if 0<=p0<=n[0]:vv.append((d,(p0,p1,p2,p3)))
  views[budget]=vv
 pairraw=set();groups={}
 for (dy,a),(dz,b) in product(views[1],views[2]):
  ranges=[range(max(0,a[t]+b[t]-n[t]),min(a[t],b[t])+1) for t in range(4)]
  for q in product(*ranges):
   if not 1<=sum(q)<=4:continue
   ns={}
   for t in range(4):ns[t]=n[t]-a[t]-b[t]+q[t];ns[t|4]=a[t]-q[t];ns[t|8]=b[t]-q[t];ns[t|12]=q[t]
   pairraw.add((dy,dz,vec(ns,4)));idx,strict=four[canonical(ns,[7,7,dy,dz],((0,1),(2,3)))]
   if strict:continue
   old=tuple(ns[t]+ns[t|8] for t in range(8));prom=tuple(ns[t|8] for t in range(8));groups.setdefault((dy,old),set()).add((dz,prom))
 stored={(r['degrees'][2],r['degrees'][3],vec(r['counts'],4)) for r in load('R2_TWO_DOMAIN.json')['labelled'] if sum(v for t,v in r['counts'].items() if int(t)&3==3)==1};assert pairraw==stored
 triples={};triple_joint=0
 for r in load('R2_NEW_PROJECTIONS.json')['cases']:
  val=fixed(r);strict=val<1
  if not strict and r.get('joint') and Q(r['joint'].get('bound','2'))<1:
   joint.verify(r['joint'],v=20,s=3,expected_degrees=r['degrees']);strict=True;triple_joint+=1
  triples[(tuple(r['degrees']),vec(r['counts'],3))]=strict
 expected=set()
 for (dy,old),vv in groups.items():
  for (dz,a),(dw,b) in product(vv,repeat=2):
   if dz>dw:continue
   ranges=[range(max(0,a[t]+b[t]-old[t]),min(a[t],b[t],1 if t==7 else 35)+1) for t in range(8)]
   for q in product(*ranges):
    if not 1<=sum(q)<=4:continue
    ns={}
    for t in range(8):ns[t]=old[t]-a[t]-b[t]+q[t];ns[t|8]=a[t]-q[t];ns[t|16]=b[t]-q[t];ns[t|24]=q[t]
    deg=[7,7,dy,dz,dw];wz=sum(v*(t&3).bit_count() for t,v in ns.items() if t&8)-2;ww=sum(v*(t&3).bit_count() for t,v in ns.items() if t&16)-2
    if min(wz,ww)>1:continue
    if any(triples[newprojkey(ns,deg,(i,3,4))] for i in range(3)):continue
    ok=False
    for order,w0 in (((0,1,3,4),wz),((0,1,4,3),ww)):
     if w0>1:continue
     vv4=project(ns,order);deg4=[deg[i] for i in order];idx,strict=four[canonical(dict(enumerate(vv4)),deg4,((0,1),(2,3)))]
     if not strict:ok=True
    if not ok:continue
    expected.add(canonical(ns,deg,((0,1),(2,),(3,4))))
 selected=load('R2_C1_MULTIPLE_SMALL_DP.json')['cases'];actual={canonical(r['counts'],r['degrees'],((0,1),(2,),(3,4))) for r in selected};assert len(expected)==346 and expected==actual
 jm5={r['source_id']:r for r in load('R2_C1_MULTIPLE_SMALL_JOINT.json')['results']};res=[];strictvals=[];jf=0
 for r in selected:
  val=fixed(r)
  if val>=1 and Q(jm5[r['id']].get('bound','2'))<1:
   joint.verify(jm5[r['id']],v=20,s=5,expected_degrees=r['degrees']);val=Q(jm5[r['id']]['bound']);jf+=1
  if val<1:strictvals.append(val);continue
  ns={int(t):v for t,v in r['counts'].items()};ws=[sum(v*(t&3).bit_count() for t,v in ns.items() if t&b)-2 for b in (4,8,16)];assert sorted(ws) in ([0,1,1],[1,1,2])
  if sorted(ws)==[0,1,1]:assert all(r['degrees'][i+2]==9 for i,w in enumerate(ws) if w==1)
  else:assert r['degrees'][2:]==[9,9,9]
  res.append(dict(source_id=r['id'],degrees=r['degrees'],low_excesses=ws))
 assert len(res)==6
 result=dict(status='PASS',scope=__doc__,old_c1_projection_count=len(lookup),old_c1_projection_strict_joint=pj,c1_four_fixed_replayed=four_fixed,c1_four_strict_joint=four_joint,independent_raw_four_count=len(pairraw),new_triples_replayed=205,new_triple_strict_joint=triple_joint,independent_five_orbits=346,five_strict=len(strictvals),five_strict_joint=jf,five_strict_max=str(max(strictvals)),six_residual_structures=res,elapsed_seconds=time.time()-start)
 (HERE/'R2_C1_MULTIPLE_SMALL_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
