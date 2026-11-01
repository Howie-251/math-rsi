from pathlib import Path
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'computations'),str(Path(__file__).parent)]
from enumerate_pair_partitions import enumerate_partitions,canonical_large_blocks,exact_types
from multilock import json_value
from position_dp import solve
start=time.perf_counter();by={}
for part in enumerate_partitions(5):
 key=canonical_large_blocks(part,5)
 if key in by and by[key]['bound']<1:continue
 counts=exact_types(part,5,degree=6,edges=34)['counts_by_mask'];z=solve(25,counts,5)
 if key not in by or z['bound']<by[key]['bound']:by[key]=dict(large=key,blocks=part,**z);print(key,z['bound'],z['positions'],flush=True)
Path(__file__).with_name('V25_FIVE_DP.json').write_text(json.dumps(json_value(dict(scope='All five isomorphism types, exact position DP; search stops after first successful labeling.',elapsed=time.perf_counter()-start,results=list(by.values()))),indent=2)+'\n')
