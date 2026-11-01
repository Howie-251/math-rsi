"""Actual r3/no-seven-K5 realization of nonstrict core15, low marks0,1,2.
Explicit common free-point witness for all three low-star partitions.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();lines=[]
for c in range(5):lines.append(tuple(5*c+y for y in range(5)))
for m in range(5):
 for c in range(5):lines.append(tuple(sorted(5*x+(m*x+c)%5 for x in range(5))))
extra=[(3,4,11,12,13),(5,4,14,15,16),(6,9,17,18,19),(7,9,10,20,21),(8,10,22,23,24)];H=sorted(set(lines+[tuple(sorted(e)) for e in extra]));I=[0,1,2,3,5,6,7,8];F=sorted(set(range(25))-set(I));R={1,2,3,4,5,6,10,14,15,19,20,21};assert len(H)==35
lam=lambda a,b:sum(a in e and b in e for e in H)
ds=[sum(v in e for e in H) for v in range(25)];assert [v for v,d in enumerate(ds) if d==6]==[0,1,2] and [v for v,d in enumerate(ds) if d==8]==[4,9,10]
assert all(lam(a,b)>=1 for a,b in combinations(range(25),2));assert all(lam(a,b)==1 for a in [0,1,2] for b in range(25) if a!=b);assert all(lam(a,b)==1 for a,b in combinations(I,2));assert all(0<len(R&set(e))<5 for e in H)
ns=Counter(sum(1<<j for j,v in enumerate(I) if v in e) for e in H);pilot=json.loads((P/'MIXED_THREE_SIX_UNIT8_PILOT.json').read_text());z=next(z for z in pilot['results'] if z['base']==15 and z['low']==[0,1,2]);assert dict(ns)=={int(t):n for t,n in z['counts'].items()}
seven=[v for v,d in enumerate(ds) if d==7];remain=set(seven);comps=[]
while remain:
 todo=[remain.pop()];cc=set(todo)
 while todo:
  a=todo.pop();nn={b for b in remain if lam(a,b)>1};cc|=nn;remain-=nn;todo.extend(nn)
 comps.append(sorted(cc))
assert sorted(map(len,comps))==[3,4,4,4,4] and all(all(lam(a,b)>1 for a,b in combinations(cc,2)) for cc in comps)
stars=[]
for low in [0,1,2]:
 ss=[]
 for idx,e in enumerate(H):
  if low in e:ss.append(dict(edge_index=idx,trace=sum(1<<j for j,v in enumerate(I) if v in e),free=sorted(set(e)&set(F))))
 assert len(ss)==6 and sorted(v for s in ss for v in s['free'])==F;stars.append(ss)
common=[];cells=Counter()
for v in F:
 entries=[next(s for s in ss if v in s['free']) for ss in stars];tt=tuple(s['trace'] for s in entries);cells[tt]+=1;common.append(dict(free_point=v,star_edge_indices=[s['edge_index'] for s in entries],star_traces=tt))
for j in range(3):assert Counter({s['trace']:len(s['free']) for s in stars[j]})==Counter({t:sum(n for tt,n in cells.items() if tt[j]==t) for t in {tt[j] for tt in cells}})
assert cells[(15,15,15)]==1 and sum(n for tt,n in cells.items() if 15 not in tt)==16
out=dict(scope=__doc__,passed=True,points=list(range(25)),edges=H,extra_edges=extra,degrees=ds,unit_locks=I,free_points=F,trace_counts=dict(ns),matches_core=15,low_labels=[0,1,2],seven_support_components=comps,no_seven_K5=True,proper_red=sorted(R),low_stars=stars,common_free_point_witness=common,common_cells=[dict(star_traces=tt,multiplicity=n) for tt,n in sorted(cells.items())],elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_THREE_SIX_UNIT8_REALIZATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','degrees','matches_core','no_seven_K5','common_cells','elapsed_seconds']},indent=2))
