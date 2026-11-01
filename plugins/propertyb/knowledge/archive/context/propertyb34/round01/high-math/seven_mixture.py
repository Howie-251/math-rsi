"""Bounded new seven-low layout-mixture proposals; exact Fraction certificates only."""
from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
OLD=ROOT/'context/propertyb34-hour1-20261013/high-math'
sys.path[:0]=[str(OLD),str(ROOT/'computations')]
from mixed_layout_lp import solve_one
from fast_position_dp import Engine
from multilock import json_value

if __name__=='__main__':
 start=time.perf_counter();eng=Engine(24,7)
 source=json.loads((OLD/'SEVEN_LOW_CATALOGUE.json').read_text())
 layouts=[tuple(range(9,16)),tuple(range(10,17)),(9,10,11,12,13,23,24),(10,11,12,13,14,15,24)]
 out=[]
 for x in source['groups']:
  if x['group'] not in (5,6):continue
  z=solve_one(eng,x,layouts);out.append(z)
  print(x['group'],z['bound'],float(z['bound']),len(z['witnesses']),time.perf_counter()-start,flush=True)
  Path(__file__).with_name('SEVEN_MIXTURE.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
