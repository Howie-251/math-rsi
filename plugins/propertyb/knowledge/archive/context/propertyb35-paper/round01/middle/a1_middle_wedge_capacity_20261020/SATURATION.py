"""One forced4lock inventory at equality in the16-middle bound for j3."""
from pathlib import Path
import sys,json,time,importlib.util
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(P.parent),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
# two points exclusive to each outer edge, with saturated K2,2 middle edges.
ns={0:17,3:1,12:1,5:4,9:4,6:4,10:4}
st=time.process_time();e=SubsetEngine(21,4,ns);z=e.verify(e.solve());r={'counts':ns,'positions':z['positions'],'bound':z['bound'],'strict':z['bound']<1}
out={'scope':__doc__,'certificate':r,'cpu_seconds':time.process_time()-st}
if z['bound']<1:
 q=importlib.util.spec_from_file_location('replay',P.parents[1]/'twentyone-delta5/replay.py');m=importlib.util.module_from_spec(q);q.loader.exec_module(m);assert m.verify(json_value(r))==z['bound'];out['independent35_replay']='PASS'
(P/'SATURATION.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(json_value(out))
