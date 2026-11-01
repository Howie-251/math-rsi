"""Exact one-partition marked conflict formula, five occupancy types only."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
import time

t0=time.process_time()
patterns=[(1,1,1,1,0),(2,1,1,0,0),(2,2,0,0,0),(3,1,0,0,0),(4,0,0,0,0)]
values=[]
for pattern in patterns:
    ans=0
    for nr in (1,2):
        for R in combinations(range(5),nr):
            for nb in (1,2):
                for B in combinations([i for i in range(5) if i not in R],nb):
                    if any(pattern[i] for i in B):
                        continue
                    red=4+4*nr-sum(pattern[i] for i in R)
                    blue=4*nb
                    if red>10 or blue>10 or red+blue>20:
                        continue
                    ans+=(-1)**(nr+nb)*comb(20-red-blue,10-red)
    values.append(ans)
assert values==[330,752,1248,1596,3528]
result={'status':'PASS','occupancies':patterns,'counts':values,
        'formula':'one-partition red/blue-block inclusion-exclusion with T forced red',
        'original_Hs_enumerated':0,'cpu_seconds':time.process_time()-t0}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
