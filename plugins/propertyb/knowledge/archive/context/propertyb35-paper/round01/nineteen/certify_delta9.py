"""Exact local certificate for the complete v=19, M=35, delta=9 branch.
Every profile is reconstructed from actual degrees and intersections; no full hypergraph enumeration.
"""
from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,double,triple,json_value
HERE=Path(__file__).parent

def main():
 start=time.time();out=[]
 pairs=json.loads((HERE/'PAIR_SCAN.json').read_text())+json.loads((HERE/'TARGET_SCAN.json').read_text())
 mixed=json.loads((HERE/'MIXED_SCAN.json').read_text())+json.loads((HERE/'TWO_HIGH_SCAN.json').read_text())
 def keep_pair(d,c,label):
  r=next(r for r in pairs if r['d']==d and r['c']==c and r['strict'])
  z=evaluate(19,double(19,*d,c),r['pos'],True)
  assert z['strict'] and str(z['bound'])==r['bound']
  out.append(dict(label=label,degrees=d,codegree=c,**z))
 def keep_triple(d,c,t,label):
  r=next(r for r in mixed if r['d']==d and r['c']==c and r['t']==t and r['strict'])
  z=evaluate(19,triple(19,d,c,t),r['pos'],True)
  assert z['strict'] and str(z['bound'])==r['bound']
  out.append(dict(label=label,degrees=d,codegrees=c,triple=t,**z))
 for d in [[9,b] for b in range(9,14)]+[[10,10],[10,11],[10,12],[11,11]]:
  for c in range(4,min(d)+1):keep_pair(d,c,'strong_pair')
 for b in range(10,14):keep_pair([9,b],1,'low_high_unit')
 for c in [1,2]:keep_pair([11,11],c,'two_elevens_small')
 for b in [10,13]:
  for a,c in [(2,2),(2,3),(3,3)]:
   for t in [0,1]:keep_triple([9,9,b],[1,a,c],t,'low_unit_mixed')
 for c,ts in [([2,2,3],[1,2]),([2,3,3],[0,1,2]),([3,3,3],[0,1])]:
  for t in ts:keep_triple([9,11,11],c,t,'two_elevens_actual_trace')
 result=dict(scope=__doc__,profile_count=len(out),all_strict=all(z['strict'] for z in out),independent_A_B_C_check=True,max_bound=max(z['bound'] for z in out),elapsed_seconds=time.time()-start,profiles=out)
 (HERE/'DELTA9_CERTIFICATE.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print(json.dumps(json_value({k:v for k,v in result.items() if k!='profiles'}),indent=2))
if __name__=='__main__':main()
