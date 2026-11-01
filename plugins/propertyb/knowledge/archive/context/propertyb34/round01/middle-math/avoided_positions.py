"""New avoided-quota DP at the stored label order for the eleven residuals.
All increasing positions, fixed labels; no claim about all label permutations.
"""
from pathlib import Path
from fractions import Fraction
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'context/propertyb34-hour1-20261013/high-math'))
from position_dp import solve,json_value
start=perf_counter();out=[]
source=json.loads((HERE/'AVOIDED_THIRTEEN.json').read_text())
targets=[w for w in source['results'] if Fraction(w['bound'])>=1]
for w in targets:
 ns={int(t):n for t,n in w['counts'].items()}
 z=solve(22,ns,6,True)
 out.append(dict(graph=w['graph'],group=w['group'],old_bound=w['bound'],**z))
 print(w['graph'],w['group'],w['bound'],'->',z['bound'],z['bound']<1,'seconds',perf_counter()-start,flush=True)
 (HERE/'AVOIDED_POSITIONS.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(targets),elapsed_seconds=perf_counter()-start,results=out)),indent=2)+'\n')
 if perf_counter()-start>150:break
