from pathlib import Path
from itertools import combinations
import json
P=Path(__file__).resolve().parent;pairs=list(combinations(range(6),2));out=[]
for nine in [0,4]:
 for center in [4,5]:
  other=9-center;edges=[tuple(sorted((i,center))) for i in range(4)]+[(4,5)]*2;mm=[edges.count(ij) for ij in pairs];s=[sum(m for ij,m in zip(pairs,mm) if v in ij) for v in range(6)];d=[8]*6;d[nine]=9;internal=[2]*4+[1]*2;single=[d[v]-internal[v]-s[v] for v in range(6)];p=next(v for v in range(4) if v!=nine);blue={p,center}
  pos3=sum(m for ij,m in zip(pairs,mm) if set(ij)<=blue);neg3=sum(m for ij,m in zip(pairs,mm) if not set(ij)&blue);pos4=sum(single[v] for v in blue)
  assert pos3==1 and neg3==0 and pos4 in [6,7]
  out.append(dict(nine=nine,star_center=center,P_degrees=d,P2degrees=s,P1counts=single,P2edge_multiset=edges,blue=sorted(blue),positive_four=pos4,positive_triple=pos3,negative_triple=neg3,negative_four=27-pos4,actual_H_realization_claimed=False))
(P/'STAR_RESIDUALS.json').write_text(json.dumps(dict(records=out),indent=2)+'\n');print(json.dumps(out,indent=2))
