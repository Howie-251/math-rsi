from pathlib import Path
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from position_dp import solve
from multilock import json_value
out=[]
for degree in range(6,18):
 ns={0:30-degree,1:4,2:degree-2,3:2};z=solve(24,ns,2);out.append(dict(degree=degree,**z));print(degree,z['bound'],z['positions'],flush=True)
Path(__file__).with_name('LOW_PARTNER_PROBE.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
