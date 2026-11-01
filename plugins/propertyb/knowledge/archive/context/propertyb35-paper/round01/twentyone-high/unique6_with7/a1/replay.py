"""Independent full-inclusive a1 gate/four-lock domain and exact diagnostic witness audit."""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import importlib.util,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];BASE=HERE.parents[1]
spec=importlib.util.spec_from_file_location('old_replay',ROOT/'context/propertyb35-paper/round01/twentyone-delta5/replay.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
def key(ns,s):return tuple(ns.get(str(i),ns.get(i,0)) for i in range(1<<s))
def recover(inc,s):
 ns={}
 for A in sorted(range(1<<s),key=int.bit_count,reverse=True):ns[A]=inc[A]-sum(v for B,v in ns.items() if B&A==A)
 return ns if min(ns.values())>=0 else None
def main():
 st=time.time();g=json.loads((HERE/'NONUNIT7_GATES.json').read_text())['cases'];found=set()
 for d in (8,9):
  for c in range(1,8):
   for t in (0,1):
    ns=recover({0:35,1:6,2:7,4:d,3:2,5:1,6:c,7:t},3)
    if ns is not None:found.add((d,c,t,key(ns,3)))
 assert found=={(r['degrees'][2],r['codegrees'][2],r['triple'],key(r['counts'],3)) for r in g}
 assert all(old.verify(r)==Q(r['bound']) for r in g)
 opts={}
 for r in g+json.loads((HERE.parent/'UNIT7_GATES.json').read_text())['cases']+json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases']:
  if not r['strict']:opts.setdefault((tuple(r['degrees']),tuple(r['codegrees'][:2])),set()).add((r['codegrees'][2],r['triple']))
 rows=json.loads((HERE/'FOUR_DP.json').read_text())['cases'];seen={};labels=[]
 for r in rows:
  ns={int(m):v for m,v in r['counts'].items()};seen[key(ns,4)]=(r['id'],False)
  if r['degrees'][2]==r['degrees'][3]:
   def swap(m):return (m&3)|((m&4)<<1)|((m&8)>>1)
   seen[key({swap(m):v for m,v in ns.items()},4)]=(r['id'],True)
 rebuilt=set()
 for a in (1,2):
  for b,c in ((8,8),(8,9),(9,9)):
   for (cpz,tpz),(cpw,tpw),(czw,tzw) in product(opts[((6,7,b),(a,1))],opts[((6,7,c),(a,1))],opts[((6,b,c),(1,1))]):
    for tpzw in range(min(cpz,cpw,czw)+1):
     for q in range(min(tpz,tpw,tzw,tpzw)+1):
      ns=recover({0:35,1:6,2:7,4:b,8:c,3:a,5:1,9:1,6:cpz,10:cpw,12:czw,7:tpz,11:tpw,13:tzw,14:tpzw,15:q},4)
      if ns is None:continue
      k=key(ns,4);rebuilt.add(k);oid,swap=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_unit_pair_swap=swap))
 assert rebuilt==set(seen) and len(labels)==len(rebuilt)
 results=[]
 for a in (1,2):
  for b,c in ((8,8),(8,9),(9,9)):
   rr=[r for r in rows if r['center_seven_codegree']==a and r['degrees'][2:]==[b,c]];vals=[old.verify(r) for r in rr]
   results.append(dict(center_seven_codegree=a,unit_degrees=[b,c],orbits=len(rr),fixed_strict=sum(v<1 for v in vals),residual=sum(v>=1 for v in vals)))
 (HERE/'FOUR_DOMAIN.json').write_text(json.dumps(dict(scope='complete necessary domain; diagnostic, not a whole-branch closure',labelled=labels,orbits=rows),indent=2)+'\n')
 result=dict(status='PASS',scope=__doc__,nonunit7_gate_profiles=len(g),full_four_labels=len(labels),four_fixed_profiles=len(rows),results=results,elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
