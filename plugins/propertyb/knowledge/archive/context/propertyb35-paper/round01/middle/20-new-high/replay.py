"""Independent fixed-position exact replay of the delta7/8 small diagnosis.
Expanded35-stub injection counts and exact nested/avoided losses; no search.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE.parent/'twenty_remaining'))
from audit_core import verify
start=time.time();data=json.loads((HERE/'DIAGNOSIS.json').read_text());out=[]
for family in ('pairs','triples'):
 vals=[verify(r) for r in data[family]]
 out.append(dict(family=family,cases=len(vals),strict=sum(v<1 for v in vals),max_strict=str(max(v for v in vals if v<1))))
answer=dict(status='PASS',scope=__doc__,results=out,elapsed_seconds=time.time()-start)
(HERE/'DIAGNOSIS_REPLAY.json').write_text(json.dumps(answer,indent=2)+'\n');print(json.dumps(answer,indent=2))
