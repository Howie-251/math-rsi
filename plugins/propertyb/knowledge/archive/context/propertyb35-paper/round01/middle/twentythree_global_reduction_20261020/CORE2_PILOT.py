"""Five actual core2 inventories for23/min7/max8, conditional all six corepair codegrees2. Old3 fixedpositions only; no grid."""
from pathlib import Path
from itertools import combinations_with_replacement
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));from subset_position_dp import SubsetEngine
st=time.process_time();menu=((9,10,22,23),(10,11,22,23),(10,22,11,23));result=[]
for ds in combinations_with_replacement((7,8),4):
 ns={15:2,**{1<<i:d-2 for i,d in enumerate(ds)}};ns[0]=35-sum(ns.values());e=SubsetEngine(23,4,ns);e.inv={p:(0,0,[]) for p in e.inv};vals=[]
 for pos in menu:
  locks={k:1<<i for i,k in enumerate(pos)};left=0;u=0
  for k in range(1,24):pivot=locks.get(k,0);u+=e.value(k,left,pivot);left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(u,e.D)),'strict':u<e.D})
 best=min(vals,key=lambda x:Fraction(x['bound']));result.append({'degrees':ds,'counts':ns,'menu':vals,'best':best});print(ds,best)
out={'status':'COMPLETE_FIVE_CORE2_FIXED_MENU_PILOT','scope':__doc__,'Nfree':19,'cases':result,'strict':sum(z['best']['strict'] for z in result),'cpu_seconds':time.process_time()-st};(P/'CORE2_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print('CPU',out['cpu_seconds'])
