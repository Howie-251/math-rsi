from itertools import product
from pathlib import Path
import json
import time

start=time.process_time()
# H denotes original red x/h membership, Y the original blue y membership.
# All other points remain fixed. Enumerate exact five-edge color types.
risks=[]
for X,H,Y in product((0,1),repeat=3):
    remaining=5-X-H-Y
    for other_blue in range(remaining+1):
        before=Y+other_blue
        if not 1<=before<=4:continue
        after=X+H+other_blue
        if after==0:
            assert Y==1 and other_blue==0 and X==H==0
            risks.append(['new_red',X,H,Y,other_blue])
        elif after==5:
            assert Y==0 and X+H>=1
            red_before=5-before
            assert red_before==X+H
            risks.append(['new_blue',X,H,Y,other_blue])

compositions=[]
for p,B,U,V in product(range(2),range(5),range(6),range(11)):
    if p+B+U+V!=6:continue
    delta=p+2*(B+U)+3*V
    if delta==18:
        compositions.append([p,B,U,V,delta])
        assert (p,B,U,V)==(0,0,0,6) and 6+B<8
assert compositions
result={'status':'PASS','proper_edge_triple_flip_risks':risks,
        'b6_delta18_compositions':compositions,'cpu_seconds':time.process_time()-start,
        'scope':'Exact edge color types and one A1 blue-composition implication only'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
