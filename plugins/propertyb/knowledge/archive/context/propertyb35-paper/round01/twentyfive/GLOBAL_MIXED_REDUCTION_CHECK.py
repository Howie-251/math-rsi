"""Two explicit actualH counterexamples to universal q2 unit-lock reselection.
One small diagnostic of degree virtualization; no new q3 catalogue/table.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations')];sys.dont_write_bytecode=True
from unit_catalogue import canonical
from bare_layout import BareLayout
st=time.perf_counter();lines=[]
for c in range(5):lines.append(tuple(5*c+y for y in range(5)))
for m in range(5):
 for c in range(5):lines.append(tuple(sorted(5*x+(m*x+c)%5 for x in range(5))))
assert len(set(lines))==30 and all(sum(i in e and j in e for e in lines)==1 for i,j in combinations(range(25),2))
R={1,2,3,4,5,6,10,14,15,19,20,21}
extras=[[(0,2,3,4,5),(0,6,7,8,9),(0,10,11,12,13),(1,14,15,16,17),(1,18,19,20,21)],[(0,3,4,5,6),(0,7,8,9,10),(1,11,12,13,14),(1,2,15,16,17),(2,18,19,20,21)]]
units=[[22,23,24,2,6,10,14,18],[22,23,24,3,7,11,15,18]]
cert=json.loads((P/'MIXED_TWO_SIX_UNIT8_CERTIFICATE.json').read_text());cache={}
for z in cert['results']:
 ns={int(t):n for t,n in z['counts'].items()};big=[t for t in ns if t.bit_count()>=3];k,m=canonical(big,8,extra=[int(i in z['low']) for i in range(8)],with_perm=True);key=(k,sum(1<<m[i] for i in z['low']));v=Q(z['raw_ABC_bound']);cp=[0]*8
 for i,j in enumerate(m):cp[j]=z['positions'][i]
 if key not in cache or v<cache[key][1]:cache[key]=(cp,v)
catalogue=json.loads((root/'context/propertyb34/round01/high-math/UNIT_CATALOGUE_8.json').read_text());base_empty=[]
for big in catalogue['orbits']:
 used={tuple(sorted((i,j))) for t in big for i,j in combinations([i for i in range(8) if t>>i&1],2)};blocks=list(big)+[(1<<i)+(1<<j) for i,j in combinations(range(8),2) if (i,j) not in used];ss=[7-sum(t>>i&1 for t in blocks) for i in range(8)];base_empty.append(35-len(blocks)-sum(ss))
assert min(base_empty)==-2 and [i for i,b in enumerate(base_empty) if b==-2]==[11,12,14,27,58]
out=[]
for ex,I in zip(extras,units):
 H=sorted(set(lines+list(map(lambda e:tuple(sorted(e)),ex))));assert len(H)==35;ds=[sum(v in e for e in H) for v in range(25)];low=[v for v,d in enumerate(ds) if d==6];seven=[v for v,d in enumerate(ds) if d==7];high=[v for v,d in enumerate(ds) if d>7];assert low==[22,23,24]
 assert all(0<len(R&set(e))<5 for e in H)
 lam=lambda a,b:sum(a in e and b in e for e in H)
 assert all(lam(a,b)==1 for a in low for b in range(25) if a!=b)
 comps=[];remain=set(seven)
 while remain:
  todo=[remain.pop()];cc=set(todo)
  while todo:
   a=todo.pop();nn={b for b in remain if lam(a,b)>1};cc|=nn;remain-=nn;todo.extend(nn)
  comps.append(sorted(cc))
 assert sorted(map(len,comps)) in [[4]*5,[3]+[4]*4]
 assert all(all(lam(a,b)>1 for a,b in combinations(cc,2)) for cc in comps)
 assert len(comps)==5 and all(len(cc)<=4 for cc in comps)
 assert all(lam(a,b)==1 for a,b in combinations(I,2))
 ns=Counter(sum(1<<i for i,v in enumerate(I) if v in e) for e in H);assert sum(ns.values())==35
 diagnostics=[]
 for j in range(3):
  virtual=Counter(ns);virtual[0]-=1;virtual[1<<j]+=1;assert min(virtual.values())>=0;virtual={t:n for t,n in virtual.items() if n};L=[i for i in range(3) if i!=j];k,m=canonical([t for t in virtual if t.bit_count()>=3],8,extra=[int(i in L) for i in range(8)],with_perm=True);cp,v=cache[(k,sum(1<<m[i] for i in L))];pos=[cp[m[i]] for i in range(8)];assert BareLayout(25,pos).bound(virtual)==v;a=BareLayout(25,pos).bound(ns)
  pp=list(range(9,17));av=BareLayout(25,pp).bound(virtual);aa=BareLayout(25,pp).bound(ns)
  diagnostics.append(dict(raised_low_index=j,virtual_q2_bound=str(v),same_witness_on_actual_q3=str(a),positions=pos,central_layout=pp,central_virtual=str(av),central_actual=str(aa),central_actual_minus_virtual=str(aa-av)))
 out.append(dict(points=list(range(25)),edges=H,extra_edges=ex,degrees=ds,low=low,seven=seven,high=high,seven_support_components=comps,seven_independence_number=5,no_seven_K5=True,no_eight_unit_with_exactly_two_low=True,proper_red=sorted(R),eight_unit_three_low=I,actual_trace_counts=dict(ns),virtualization_diagnostics=diagnostics))
result=dict(scope=__doc__,passed=True,unit8_base_empty_minimum=min(base_empty),unit8_base_empty_minus_two_families=[i for i,b in enumerate(base_empty) if b==-2],actual_hypergraphs=out,elapsed_seconds=time.perf_counter()-st)
(P/'GLOBAL_MIXED_REDUCTION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(passed=True,spectra=[dict(Counter(z['degrees'])) for z in out],diagnostics=[z['virtualization_diagnostics'] for z in out],elapsed_seconds=result['elapsed_seconds']),indent=2))
