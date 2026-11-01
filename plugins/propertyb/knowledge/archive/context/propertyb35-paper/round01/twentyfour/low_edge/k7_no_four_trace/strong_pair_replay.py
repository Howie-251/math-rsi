"""Independent n24/M35 35-stub injection replay for two8 locks of codegree6..8; no deduction used."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5]
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
def main():
 st=time.time();rr=json.loads((HERE/'STRONG_88_PAIR.json').read_text())['cases'];out=[]
 assert {r['codegree'] for r in rr}=={6,7,8}
 for r in rr:
  c=r['codegree'];expected={0:19+c,1:8-c,2:8-c,3:c};assert {int(t):n for t,n in r['counts'].items() if n}=={t:n for t,n in expected.items() if n}
  pos=tuple(r['positions']);assert pos==(11,24)
  types=[frozenset(i+1 for i in range(2) if t>>i&1) for t,n in expected.items() for _ in range(n)]
  rows=independent_rows(24,pos,types);value=sum((z['bound'] for z in rows),Q());assert value==Q(r['bound'])<1
  assert all(Q(cer['loss'])==0 for cer in r['certificates'])
  assert all((a['A'],a['B'],a['C'])==(Q(b['A']),Q(b['B']),Q(b['C'])) and Q(b['deduction'])==0 for a,b in zip(rows,r['rows']))
  out.append(dict(codegree=c,bound=str(value),positions=pos))
 result=dict(status='PASS',scope=__doc__,complete_codegree_domain=[6,7,8],fixed_profiles=3,independent_rows=72,stubs_per_profile=35,ordered_distinct_pairs=1190,results=out,elapsed_seconds=time.time()-st);(HERE/'STRONG_88_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
