"""Exact source-potential identities and a same-edge flat source rotation.
No full-H search, no claim that the partial family extends to 35 edges.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json, time
start=time.process_time()
x=0
G=frozenset([1,2,3,4]); F=frozenset([5,11,6,7])
links=[G,F,frozenset([13,11,17,18]),frozenset([9,10,12,19]),
       frozenset([9,14,16,20]),frozenset([10,15,12,8])]
Q=[frozenset([g,6,7,8,20]) for g in G]
P=[frozenset([f,13,10,14,15]) for f in [5,6,7]]
P += [frozenset([11,9,10,14,15])]
N=[frozenset([5,b,9,14,16]) for b in [17,18]]
bar=Q+P+N
edges=[L|{x} for L in links]+bar
R0=frozenset([1,2,3,4,9,10,13,14,15,16])
R1=(R0-{13})|{5}
Brole=frozenset([9,10,11,12]); U=frozenset([1,2,3,5,13]); p=16
V=frozenset(range(1,21))-Brole-U-{p}
target={x:6,p:7,**{v:8 for v in Brole|U},**{v:9 for v in V}}
assert len(V)==10 and len(edges)==len(set(edges))==16
assert all(len(e)==5 for e in edges)
assert Counter(v for L in links for v in L)==Counter({v:2 if v in Brole else 1 for v in range(1,21)})
assert len(U)==5
D=Counter(v for e in edges for v in e)
assert all(D[v]<=target[v] for v in range(21))
co=Counter(tuple(sorted(ij)) for e in edges for ij in combinations(e,2))
repeat={v:sum(max(co[tuple(sorted((v,w)))]-1,0) for w in range(21) if w!=v) for v in range(21)}
assert all(repeat[v]<=4*target[v]-20 for v in range(21))

def state(R):
 B=set(range(1,21))-R
 assert len(R)==len(B)==10
 assert all(0<len(e&R)<5 for e in bar)
 red=[i for i,L in enumerate(links) if L<=R]
 blue=[i for i,L in enumerate(links) if L<=B]
 assert len(red)==len(blue)==1
 private=[i for i,e in enumerate(bar) if len(e&R) in [1,4]]
 owner={i:next(iter(e&R if len(e&R)==1 else e&B)) for i,e in enumerate(bar) if i in private}
 core=links[red[0]]|links[blue[0]]
 assert set(owner.values())==core and len(private)==8
 safeR={v for v in links[red[0]] if all(v not in L or L<=R or len(L&R)>=2 for L in links)}
 safeB={v for v in links[blue[0]] if all(v not in L or L<=B or len(L&B)>=2 for L in links)}
 assert len(safeR)==len(safeB)==4
 failures=[]
 for g in safeR:
  for y in safeB:
   Rp=(R-{g})|{y}
   bad=[i for i,e in enumerate(bar) if len(e&Rp) in [0,5]]
   assert bad
   failures.append([g,y,bad])
 return {'red_link':red[0], 'blue_link':blue[0], 'private_indices':private,
         'owners':owner,'private_count':len(private),'safe_sizes':[len(safeR),len(safeB)],
         'core_degree_class':sorted(target[v] for v in core),
         'core_role_class':sorted(('B' if v in Brole else 'U' if v in U else 'p' if v==p else 'V') for v in core),
         'mixed_blue_histogram':sorted(len(L&B) for L in links if not L<=R and not L<=B),
         'blue_role_counts':[len(B&Brole),len(B&U),int(p in B),len(B&V)],
         'safe_swap_failures':failures}
s0,s1=state(R0),state(R1)
for key in ['private_count','core_degree_class','core_role_class','mixed_blue_histogram','blue_role_counts','safe_sizes']:
 assert s0[key]==s1[key],key
# Check the derivative for every balanced exterior swap, conditional on bar proper.
def E(R): return sum(len(e&R) in [1,4] for e in bar)
checks=0
for R in [R0,R1]:
 B=set(range(1,21))-R
 for s in R:
  for y in B:
   Rp=(R-{s})|{y}
   if any(len(e&Rp) in [0,5] for e in bar): continue
   gain2=[i for i,e in enumerate(bar) if y in e and s not in e and len(e&B)==2]
   gain3=[i for i,e in enumerate(bar) if s in e and y not in e and len(e&B)==3]
   loss1=[i for i,e in enumerate(bar) if s in e and y not in e and len(e&B)==1]
   loss4=[i for i,e in enumerate(bar) if y in e and s not in e and len(e&B)==4]
   assert E(Rp)-E(R)==len(gain2)+len(gain3)-len(loss1)-len(loss4)
   checks+=1
# Forward rotation: blue y=5 exchanges with red s=13; one blue star changes.
y,s=5,13
assert R1==(R0-{s})|{y}
gain=[i for i in s1['private_indices'] if i not in s0['private_indices']]
loss=[i for i in s0['private_indices'] if i not in s1['private_indices']]
transfer=[i for i in set(s0['private_indices'])&set(s1['private_indices']) if s0['owners'][i]!=s1['owners'][i]]
assert gain==[8,9] and loss==[5,6] and transfer==[4]
result={'status':'PASS','scope':'16-edge A1-role partial family only; no extension or full-H counterexample claim',
 'edges':[sorted(e) for e in edges], 'bar_edges':[sorted(e) for e in bar], 'red0':sorted(R0),'red1':sorted(R1),
 'roles':{'x':x,'p':p,'B':sorted(Brole),'U':sorted(U),'V':sorted(V)},
 'states':[s0,s1],'rotation':{'old_blue':y,'old_red':s,'gain_indices':gain,'loss_indices':loss,'owner_transfer_indices':transfer},
 'all_legal_swap_derivative_checks':checks,'partial_degrees':dict(D),'target_degrees':target,
 'row_repeat':repeat,'cpu_seconds':time.process_time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','partial_edges':len(edges),'derivative_checks':checks,'gain':gain,'loss':loss,'transfer':transfer,'cpu_seconds':result['cpu_seconds']}))
