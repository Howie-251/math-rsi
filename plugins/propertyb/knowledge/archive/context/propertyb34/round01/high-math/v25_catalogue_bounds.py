"""Bounded exact diagnosis of a complete colored nine-lock catalogue."""
from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from subset_position_dp import SubsetEngine
from multilock import json_value

if __name__=='__main__':
 q=int(sys.argv[1]);budget=float(sys.argv[2]) if len(sys.argv)>2 else 240
 source=json.loads((HERE/f'V25_NINE_Q{q}_CATALOGUE.json').read_text());out=[];start=time.perf_counter()
 for x in source['results']:
  ns={int(t):n for t,n in x['counts'].items()};eng=SubsetEngine(25,9,ns);z=eng.verify(eng.solve());z.update(id=x['id'],large_blocks=x['large_blocks'])
  # Counts and placements suffice to replay strict witnesses; keep full rows for residues.
  if z['bound']<1:z.pop('rows');z.pop('certificates')
  out.append(z)
  if len(out)%50==0:print(q,len(out),sum(z['bound']<1 for z in out),'elapsed',time.perf_counter()-start,flush=True)
  if len(out)%20==0 or len(out)==len(source['results']) or time.perf_counter()-start>budget:
   (HERE/f'V25_NINE_Q{q}_BOUNDS.json').write_text(json.dumps(json_value(dict(scope=__doc__,catalogue_size=len(source['results']),q=q,complete=len(out)==len(source['results']),elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>budget:print('BUDGET_STOP',flush=True);break
 print('FINAL',q,len(out),sum(z['bound']<1 for z in out),time.perf_counter()-start,flush=True)
