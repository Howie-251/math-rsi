"""Exactly three degree6 points, no degree7; complete joint five-point domain with two actual degree8 common unit points, low triple0/1."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();out=[];lowpairs=list(itertools.combinations(range(3),2));defects=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
for T in (0,1):
 choices=defects if T==0 else [(0,0,0)]
 for az,bz in itertools.product(choices,repeat=2):
  for c in range(1,5):
   for gs in itertools.product((0,1),repeat=3):
    opts=[range(min(a,b,gs[i],gs[j])+1) for (i,j),a,b in zip(lowpairs,az,bz)]
    for hs in itertools.product(*opts):
     inc={m:0 for m in range(32)};inc[0]=35
     for i,d in enumerate([6,6,6,8,8]):inc[1<<i]=d
     for i,j in itertools.combinations(range(5),2):inc[(1<<i)|(1<<j)]=2 if j<3 else c if i==3 else 1
     inc[7]=T
     for (i,j),a,b,h in zip(lowpairs,az,bz,hs):inc[(1<<i)|(1<<j)|8]=a;inc[(1<<i)|(1<<j)|16]=b;inc[(1<<i)|(1<<j)|24]=h
     for i,g in enumerate(gs):inc[(1<<i)|24]=g
     ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(32)}
     if min(ns.values())<0:continue
     eng=SubsetEngine(21,5,ns);z=eng.verify(eng.solve());z.update(degrees=[6,6,6,8,8],low_triple=T,low_pair_z=az,low_pair_w=bz,partner_codegree=c,single_low_triples=gs,low_pair_quads=hs,strict=z['bound']<1);out.append(z)
 rr=[z for z in out if z['low_triple']==T];print(T,'domain',len(rr),'strict',sum(z['strict'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
 for i,z in enumerate(rr):
  if not z['strict']:print('residual',i,z['low_pair_z'],z['low_pair_w'],z['partner_codegree'],z['single_low_triples'],z['low_pair_quads'],z['bound'])
(HERE/'THREE_SIXES_TWO_EIGHTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
