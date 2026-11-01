"""Independent structural generation of no-good-single-center P2 multigraphs:
a matching on C plus one attachment per remaining C point, plus45 edges.
No 15-slot six-edge enumeration or original profile source is imported.
"""
from itertools import combinations,product
from pathlib import Path
from collections import Counter
import json
P=Path(__file__).resolve().parent;C=range(4);pairs=list(combinations(range(6),2));source=json.loads((P/'PURE_P2_PROFILE.json').read_text());allrows=[];summary=[]
for nine in [0,4]:
 seen=set();hist=Counter();rows=[]
 for z in range(3):
  for matching in combinations(list(combinations(C,2)),z):
   used=[v for e in matching for v in e]
   if len(set(used))<2*z:continue
   available=[v for v in C if v not in used]
   for choices in product([None,4,5],repeat=len(available)):
    attach={v:q for v,q in zip(available,choices) if q is not None};ka=sum(q==4 for q in attach.values());kb=sum(q==5 for q in attach.values());x=6-z-ka-kb
    edges=list(matching)+list(attach.items())+[(4,5)]*x;mm=[edges.count(e)+edges.count((e[1],e[0])) for e in pairs];assert tuple(mm) not in seen;seen.add(tuple(mm))
    if z==2:
     q=next(v for v in [4,5] if v!=nine);p=next(v for v in C if v!=nine)
    elif z==1:
     if min(ka,kb)==0:q=4 if ka>=kb else 5;p=used[0]
     else:q=next(v for v in [4,5] if v!=nine);p=next(v for v in used if v!=nine)
    elif min(ka,kb)==0:
     q=4 if ka>=kb else 5
     if ka+kb==4:
      hist['star_residual']+=1;rows.append(dict(nine=nine,multiplicities=mm,star=q));continue
     p=next(v for v in C if v not in attach)
    elif min(ka,kb)==1:
     q=4 if kb==1 else 5;other=9-q;p=next(v for v in C if attach.get(v)==other)
    else:
     assert ka==kb==2;q=next(v for v in [4,5] if v!=nine);p=next(v for v in C if attach.get(v)==9-q and v!=nine)
    blue={p,q};s=[sum(m for e,m in zip(pairs,mm) if v in e) for v in range(6)];d=[8]*6;d[nine]=9;internal=[2]*4+[1]*2;single=[d[v]-internal[v]-s[v] for v in range(6)]
    pos3=sum(m for e,m in zip(pairs,mm) if set(e)<=blue);neg3=sum(m for e,m in zip(pairs,mm) if not set(e)&blue);pos4=sum(single[v] for v in blue)
    assert pos3==0
    if neg3==0:assert pos4<=8;kind='zeroT_eight_four_corollary'
    else:assert neg3==1 and pos4==8 and 27-pos4==19;kind='pending_oneT_eight_four_gate'
    hist[kind]+=1;rows.append(dict(nine=nine,multiplicities=mm,blue=sorted(blue),positive4=pos4,negative3=neg3,negative4=27-pos4,kind=kind))
 old=next(case for case in source['cases'] if case['summary']['nine']==nine);expected={tuple(r['multiplicities']) for r in old['records'] if max(r['P2degrees'][:4])<=1}
 assert seen==expected and len(seen)==138
 summary.append(dict(nine=nine,counts=dict(hist)));allrows.extend(rows)
out=dict(passed=True,scope=__doc__,summaries=summary,states=len(allrows),records=allrows)
(P/'SELECTOR_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
