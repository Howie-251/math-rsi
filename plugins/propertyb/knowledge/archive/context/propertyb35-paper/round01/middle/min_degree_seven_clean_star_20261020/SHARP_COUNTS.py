"""Tiny exact count continuation; no old certificate or position calculation rerun."""
from pathlib import Path
from collections import Counter
from itertools import combinations,product
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def partitions(n,lo=1):
 if n==0:yield();return
 for a in range(lo,n+1):
  for rest in partitions(n-a,a):yield(a,)+rest
cases=[];spectra=set()
for clean in (11,12):
 dirty=16-clean
 for n7 in range(max(3,clean-8),5):
  nlarge=clean-n7;remaining=17-2*nlarge
  if remaining<0:continue
  # Clean non7 points are9 or>=11: extra above9 cannot equal1.
  for ce in range(remaining+1):
   for cp in partitions(ce,2):
    if len(cp)>nlarge:continue
    cdeg=[7]*n7+[9]*(nlarge-len(cp))+[9+x for x in cp]
    left=17-sum(d-7 for d in cdeg)
    for dp in partitions(left):
     if len(dp)>dirty:continue
     ddeg=[7]*(dirty-len(dp))+[7+x for x in dp]
     allD=tuple(sorted([7,10,10,10,9]+cdeg+ddeg))
     assert len(allD)==21 and sum(allD)==175 and sum(cdeg+ddeg)==129
     spectra.add(allD);cases.append(dict(clean=clean,dirty=dirty,clean7=n7,clean_degrees=cdeg,dirty_degrees=ddeg,whole_degree_counts=dict(Counter(allD))))
assert len(spectra)==5
old=json.loads((P/'STAR_RESULT.json').read_text())
B7=[z for z in old['nonstrict'] if z['source']==1 and z['r']==7]
B9=[z for z in old['nonstrict'] if z['source']==1 and z['r']==9]
assert len(B7)==3 and all(z['s'][0]==2 and z['s'][3]==1 and z['bound']=='718/715' for z in B7)
assert len(B9)==10 and all(z['s'][0]==1 and z['s'][3]==2 and z['bound']=='5072/5005' for z in B9)
two=[frozenset(c) for c in combinations(range(4),2)]
triples=set()
for A,B,C in product(two,repeat=3):
 triples.add((tuple(sorted((len(A&B),len(A&C),len(B&C)))),len(A&B&C)))
assert triples=={((2,2,2),2),((0,0,2),0),((1,1,2),1),((0,1,1),0),((1,1,1),0),((1,1,1),1)}
result=dict(common_F0_three_star_intersection_patterns=sorted(triples),status='PASS_SMALL_COUNT_REDUCTION',scope=__doc__,cases=cases,degree_spectra=[dict(Counter(ds)) for ds in sorted(spectra)],B7=[dict(s=z['s'],degrees=z['degrees'],bound=z['bound'],positions=z['positions']) for z in B7],B9=[dict(s=z['s'],bound=z['bound'],positions=z['positions']) for z in B9],cpu_seconds=time.process_time()-st)
(P/'SHARP_COUNTS.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(cases),'clean/dirty count cases',len(spectra),'whole spectra','CPU',result['cpu_seconds'])
