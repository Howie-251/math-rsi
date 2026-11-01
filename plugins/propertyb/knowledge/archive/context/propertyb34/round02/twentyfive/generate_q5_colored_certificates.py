"""Recover exact color-preserving labels after proved degree pruning.
Uses saved q5 representatives only; does not search probability layouts.
"""
from pathlib import Path
from itertools import combinations
import sys,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math'
sys.path.insert(0,str(S));from unit_catalogue import canonical,fullblocks
old=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())['orbits'];new=json.loads((S/'V25_NINE_Q5_CATALOGUE.json').read_text())['results'];index={tuple(r['large_blocks']):r['id'] for r in new};assert len(index)==11692
start=time.monotonic();families=[];rows=[];feasible=0;rejected=0;budget=0
for c,big in enumerate(old):
 blocks=fullblocks(big,9);inc=[sum(bool(t>>i&1) for t in blocks) for i in range(9)]
 bad=next((i for i in range(9) if inc[i]>7),None)
 if bad is not None:
  families.append(dict(base=c,large_blocks=big,rejection={'vertex':bad,'incident':[t for t in blocks if t>>bad&1][:8]}));rejected+=1;continue
 eligible=[i for i in range(9) if inc[i]<=6];lows=[list(xs) for xs in combinations(eligible,5)]
 families.append(dict(base=c,large_blocks=big,full=blocks,eligible=eligible,lows=lows))
 for low in lows:
  degree=[6 if i in low else 7 for i in range(9)]
  assert all(inc[i]<=degree[i] for i in range(9))
  if len(blocks)+sum(degree[i]-inc[i] for i in range(9))>34:
   rows.append(dict(base=c,low=low,rejection={'full':blocks}));budget+=1;continue
  normal,perm=canonical(big,9,[int(i not in low) for i in range(9)],True)
  assert all((perm[i]<5)==(i in low) for i in range(9)) and len(set(perm))==9
  target=index[normal];feasible+=1
  rows.append(dict(base=c,low=low,target=target,permutation=perm))
assert (len(families),rejected,len(rows),feasible,budget)==(374,65,23759,23507,252)
assert set(r['target'] for r in rows if 'target' in r)==set(range(11692))
result=dict(families=families,rows=rows,raw=374*126,pruned=len(rows),feasible=feasible,family_rejects=rejected,budget_rejects=budget,representatives=11692,elapsed=time.monotonic()-start)
(HERE/'Q5_COLORED_CERTIFICATES.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('rows','families')}))
