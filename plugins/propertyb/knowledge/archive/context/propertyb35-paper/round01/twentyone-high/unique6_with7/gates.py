"""M35/v21 center6: complete unit(7,d) gates for7<=d<=15, and complete677 triples after actual strong-pair exclusions."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,sys,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def recover(ds,cs,t):
 inc={0:35,1:ds[0],2:ds[1],4:ds[2],3:cs[0],5:cs[1],6:cs[2],7:t};ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(8)}
 return ns if min(ns.values())>=0 else None

def main():
 st=time.time();old=json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'];cached={(tuple(r['degrees']),tuple(r['codegrees']),r['triple']):r for r in old};out=[]
 for d in range(7,16):
  for c in range(1,8):
   for t in (0,1):
    ns=recover((6,7,d),(1,1,c),t)
    if ns is None:continue
    key=((6,7,d),(1,1,c),t)
    if key in cached:z=dict(cached[key]);z['bound']=Fraction(z['bound'])
    else:
     eng=SubsetEngine(21,3,ns);z=eng.verify(eng.solve());z.update(degrees=[6,7,d],codegrees=[1,1,c],triple=t,strict=z['bound']<1)
    z['id']=len(out);out.append(z)
  rr=[r for r in out if r['degrees'][2]==d];print('unit7',d,'count',len(rr),'res',[(r['codegrees'][2],r['triple']) for r in rr if not r['strict']],flush=True)
 (HERE/'UNIT7_GATES.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,degree_range=[7,15],cases=out)),indent=2)+'\n')
 cached={(tuple(r['degrees']),tuple(r['codegrees']),r['triple']):r for r in out};tri=[]
 for a in (1,2,3):
  for b in range(a,4):
   for c in (1,2,3):
    for t in range(min(a,b,c)+1):
     ns=recover((6,7,7),(a,b,c),t)
     if ns is None:continue
     key=((6,7,7),(a,b,c),t)
     if key in cached:z=dict(cached[key])
     else:
      eng=SubsetEngine(21,3,ns);z=eng.verify(eng.solve());z.update(degrees=[6,7,7],codegrees=[a,b,c],triple=t,strict=z['bound']<1)
     z['id']=len(tri);tri.append(z)
 print('677 domain',len(tri),'strict',sum(z['strict'] for z in tri),'nonunit residual',[(z['codegrees'],z['triple']) for z in tri if not z['strict'] and z['codegrees'][0]>=2],flush=True)
 (HERE/'ALL677_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=tri,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
