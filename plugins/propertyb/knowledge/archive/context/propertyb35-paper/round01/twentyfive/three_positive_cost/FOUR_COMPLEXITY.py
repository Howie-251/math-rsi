"""Domain-size profile only; no probability/cover screen or classification theorem."""
from itertools import product,permutations
from collections import Counter
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
non=[m for m in range(1,16) if m.bit_count()>=2];counts=[]
def rec(j,left,occupied,cell):
 if j==len(non):
  if any(x>4 for x in occupied):return
  values={m:z for m,z in zip(non,cell)}
  for k,x in enumerate(occupied):values[1<<k]=4-x
  row=tuple(values.get(m,0) for m in range(1,16))
  counts.append(row);return
 mask=non[j];w=mask.bit_count()-1
 for z in range(min(left//w,*(4-occupied[k] for k in range(4) if mask>>k&1))+1):
  rec(j+1,left-w*z,[x+z*int(mask>>k&1) for k,x in enumerate(occupied)],cell+[z])
rec(0,5,[0]*4,[])
simple=[];qcounts=Counter()
for c in counts:
 A=[{m for m in range(1,16) if m>>k&1 and c[m-1]} for k in range(4)]
 # Equal supports across nonzero Venn cells are equivalent to equal actual sets.
 if len({frozenset(a) for a in A})<4:continue
 simple.append(c)
 nonempty=sum(z>0 for z in c);large=sum(z>=2 for z in c)
 qcounts[0]+=1;qcounts[1]+=nonempty;qcounts[2]+=nonempty*(nonempty-1)//2+large
summary=dict(scope=__doc__,labeled_count_families=len(counts),distinct_positive_families=len(simple),F_cell_markings_q0_1_2=dict(qcounts),elapsed_seconds=time.perf_counter()-st)
(P/'FOUR_COMPLEXITY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
