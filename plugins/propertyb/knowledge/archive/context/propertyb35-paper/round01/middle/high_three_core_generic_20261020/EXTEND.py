"""Same-H x6 star expansion of exactly the nine nonstrict 888 triple inventories."""
from pathlib import Path
from itertools import product
import json,time
from PILOT import stars,solve,json_value
HERE=Path(__file__).resolve().parent

def main():
 st=time.process_time();raw=json.loads((HERE/'PILOT.json').read_text());out=[];complete=True
 for sid in raw['nonstrict_ids']:
  ns={int(t):n for t,n in raw['cases'][sid]['counts'].items()}
  for margin in product((1,2),repeat=3):
   for hh in stars(ns,margin):
    if time.process_time()-st>8.8:
     complete=False;break
    nn={}
    for t,n in ns.items():
     if n-hh[t]:nn[t<<1]=n-hh[t]
     if hh[t]:nn[(t<<1)|1]=hh[t]
    assert sum(nn.values())==35
    assert all(sum(n for t,n in nn.items() if t>>i&1)==d for i,d in enumerate([6,8,8,8]))
    row=solve([6,8,8,8],nn,dict(source_id=sid,x_margins=margin,h=hh))
    out.append(row)
   if not complete:break
  print('source',sid,'processed',len(out),'nonstrict',sum(not r['strict'] for r in out),flush=True)
  if not complete:break
 bad=[i for i,r in enumerate(out) if not r['strict']]
 result=dict(scope=__doc__,complete=complete,expected_total=raw['total_star_candidates'],cases=out,
             nonstrict_ids=bad,cpu_seconds=time.process_time()-st)
 if complete:assert len(out)==raw['total_star_candidates']==298
 (HERE/'EXTENDED.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print('complete',complete,'count',len(out),'bad',len(bad),'max',max(r['bound'] for r in out),'CPU',result['cpu_seconds'])
if __name__=='__main__':main()
