from pathlib import Path
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
from independent_structure_bounds import independent_rows
st=time.process_time();ns={30:3,1:2,0:2}
for i in range(1,5):ns[1<<i]=6;ns[1|(1<<i)]=1
assert sum(ns.values())==35
E=SubsetEngine(21,5,ns);original=E.inv.copy();E.inv={p:(0,0,[]) for p in original}
z=E.solve();mode='zero'
if z['bound']>=1:E.inv=original;z=E.verify(E.solve());mode='nested_total_pure'
out=dict(scope='Unique actual A3 four10 core residual, center6 unit to allfour',mode=mode,counts=ns,degrees=[6,10,10,10,10],positions=z['positions'],bound=z['bound'],strict=z['bound']<1,cpu_seconds=time.process_time()-st)
(P/'ACTUAL_A3_FIVE.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(json_value(out))
