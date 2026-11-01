"""Bind all 374 unit families and all 9 possible high vertices to saved q=8 cases.
Only exact label isomorphisms are recovered; no probability layouts are searched.
"""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math'
sys.path.insert(0,str(S));from unit_catalogue import canonical,fullblocks
old=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())['orbits'];new=json.loads((S/'V25_NINE_Q8_CATALOGUE.json').read_text())['results'];index={tuple(r['large_blocks']):r['id'] for r in new};assert len(index)==840
start=time.monotonic();rows=[];feasible=0
for c,big in enumerate(old):
 blocks=fullblocks(big,9);inc=[sum(bool(t>>i&1) for t in blocks) for i in range(9)]
 for high in range(9):
  degree=[7 if i==high else 6 for i in range(9)];bad=next((i for i in range(9) if inc[i]>degree[i]),None)
  if bad is not None:
   rows.append(dict(base=c,high=high,rejection={'vertex':bad,'incident':[t for t in blocks if t>>bad&1][:degree[bad]+1]}));continue
  assert len(blocks)+sum(degree[i]-inc[i] for i in range(9))<=34
  normal,perm=canonical(big,9,[int(i==high) for i in range(9)],True)
  assert perm[high]==8 and len(set(perm))==9
  target=index[normal];feasible+=1
  rows.append(dict(base=c,high=high,target=target,permutation=perm))
assert feasible==1397 and len(rows)==3366
result=dict(rows=rows,raw=len(rows),feasible=feasible,representatives=840,elapsed=time.monotonic()-start)
(HERE/'Q8_COLORED_CERTIFICATES.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
