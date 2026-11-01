"""Two degree6 points have codegree1: complete small shared star views needed for a three-seven-neighbour test."""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/twentyone-delta5'))
from star_low import SubsetEngine,json_value
st=time.time();dom=json.loads((HERE/'STAR_THREE_DOMAIN.json').read_text())['cases'];pilot={r['source_id']:r for r in json.loads((HERE/'STAR_THREE_PILOT.json').read_text())['cases']};wanted=[(6,7,7),(6,8,8),(6,8,9),(6,9,9),(7,7,7)];out=[]
for ds in wanted:
 rr=[]
 for i,r in enumerate(dom):
  if r['center_degree']!=6 or tuple(r['neighbor_degrees'])!=ds:continue
  if i in pilot:z=pilot[i]
  else:
   eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i)
  out.append(z);rr.append(z)
 print(ds,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max(r['bound'] if not isinstance(r['bound'],str) else __import__('fractions').Fraction(r['bound']) for r in rr),flush=True)
(HERE/'BUDDY_STAR_THREE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
