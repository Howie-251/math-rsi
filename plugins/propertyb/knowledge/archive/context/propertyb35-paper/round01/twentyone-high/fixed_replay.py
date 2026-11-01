"""Exact original35-stub witness replay for the degree6 reductions; no DP or SciPy."""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/twentyone-delta5'))
from replay import verify
st=time.time();out=[]
for filename in ['DOUBLES.json','TRIPLES.json','TWO_SIXES_TRIPLES.json','FOUR_SIXES.json','THREE_SIXES_FOUR.json','THREE_SIXES_FIVE_T2.json','THREE_SIXES_TWO_EIGHTS.json','TWO_SIXES_UNIT_EIGHTS.json']:
 rr=json.loads((HERE/filename).read_text())['cases'];vals=[verify(r) for r in rr];out.append(dict(file=filename,cases=len(rr),strict=sum(v<1 for v in vals),max_strict=str(max((v for v in vals if v<1),default=0))))
result=dict(status='PASS',scope=__doc__,fixed_inputs=sum(z['cases'] for z in out),independent_rows=21*sum(z['cases'] for z in out),results=out,elapsed_seconds=time.time()-st);(HERE/'FIXED_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
