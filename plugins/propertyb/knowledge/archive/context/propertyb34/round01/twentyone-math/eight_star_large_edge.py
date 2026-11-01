from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent;out=[];ds=(8,)*5;ls=(1,1,1,1,2,2,2,2,2,2)
for ns in profiles(5,ds,ls):
 if ns.get(15,0)!=1 or ns.get(14,0)+ns.get(30,0)!=1:continue
 z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];out.append(r);print({m:c for m,c in ns.items() if m.bit_count()>=3 and c},r['bound'])
(HERE/'EIGHT_STAR_LARGE_EDGE.json').write_text(json.dumps(json_value(dict(cases=out)),indent=2))
