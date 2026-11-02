#!/usr/bin/env python3
"""Generate every two-sided Y incidence alignment for the supplied ten Z types."""
from pathlib import Path
from itertools import permutations,product
from collections import Counter
from math import factorial,prod
import json,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'d1_homogeneous_configuration_run'
def cycles(edges):
    adj=[[] for _ in range(10)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    assert all(len(a)==2 for a in adj)
    unseen=set(range(10));answer=[]
    while unseen:
        start=min(unseen);cycle=[start];previous=start;current=min(adj[start])
        while current!=start:
            cycle.append(current);previous,current=current,next(v for v in adj[current] if v!=previous)
        unseen-=set(cycle);answer.append(cycle)
    return answer
def mate(choice):
    result=[-1]*10
    for u,v in choice['matching']:result[u]=v;result[v]=u
    assert min(result)>=0
    return result
def transpose(rows):return [sum(1<<u for u in range(10) if rows[u]>>v&1) for v in range(10)]
def alignments(left,right):
    lc=cycles(left['factor_edges']);rc=cycles(right['factor_edges'])
    for pairing in permutations(range(len(rc))):
        if any(len(lc[k])!=len(rc[pairing[k]]) for k in range(len(lc))):continue
        choices=[[(shift,sign) for shift in range(len(c)) for sign in (1,-1)] for c in lc]
        for parameters in product(*choices):
            rows=[0]*10
            for k,((shift,sign),a) in enumerate(zip(parameters,lc)):
                b=rc[pairing[k]];length=len(a)
                for j,column in enumerate(b):
                    index=(shift+sign*j)%length
                    rows[a[index]]|=1<<column;rows[a[(index+1)%length]]|=1<<column
            yield rows
def main():
    start=time.process_time();OUT.mkdir(exist_ok=True)
    source=HERE/'d1_10_3_catalog/local_interfaces.json';catalog=json.loads(source.read_text())
    records=[];counts=[]
    for c in catalog['configurations']:
        number=c['grunbaum_number'];z=[sum(1<<v for v in row) for row in c['primal']['Z_row_supports']];zt=transpose(z)
        before=len(records);expected=0
        for li,left in enumerate(c['primal']['choices']):
            sl=mate(left)
            for ri,right in enumerate(c['dual']['choices']):
                if left['factor_cycle_type']!=right['factor_cycle_type']:continue
                sr=mate(right);typ=left['factor_cycle_type'];expected+=prod(2*n for n in typ)*prod(factorial(v) for v in Counter(typ).values())
                seen=[]
                for y in alignments(left,right):
                    yt=transpose(y)
                    assert all(w.bit_count()==2 for w in y+yt)
                    assert all((sl[i]==j)+(y[i]&y[j]).bit_count()+(z[i]&z[j]).bit_count()==1+4*(i==j) for i in range(10) for j in range(10))
                    assert all((sr[i]==j)+(yt[i]&yt[j]).bit_count()+(zt[i]&zt[j]).bit_count()==1+4*(i==j) for i in range(10) for j in range(10))
                    key=tuple(y);assert key not in seen;seen.append(key)
                    records.append((number,li,ri,sl,sr,z,y))
        count=len(records)-before;assert count==expected;counts.append({'configuration':number,'Y_alignments':count})
    assert [c['Y_alignments'] for c in counts]==[7200,720,720,7200,968,936,936,1584,1296,3100]
    assert len(records)==24660
    with (OUT/'inputs.txt').open('w') as out:
        out.write(str(len(records))+'\n')
        for number,li,ri,sl,sr,z,y in records:
            out.write(' '.join(map(str,[number,li,ri]+sl+sr+z+y))+'\n')
    metadata={'source':str(source),'input_count':len(records),'counts':counts,
      'all_two_sided_same_fiber_equations_verified':True,
      'generation':'All length-preserving cycle pairings, rotations and reflections from right factor vertices to left factor edges',
      'cpu_seconds':time.process_time()-start}
    (OUT/'preparation.json').write_text(json.dumps(metadata,indent=2)+'\n');print(json.dumps(metadata,indent=2))
if __name__=='__main__':main()
