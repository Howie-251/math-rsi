"""Independent trace-polynomial replay of the first necessary P inventory."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
HERE=Path(__file__).resolve().parent
j=json.loads((HERE/'RUN.json').read_text());f=j['first_nongated']
C=set(f['C']);T=list(map(set,f['higher_traces']));d=f['degrees'];s=f['J_degrees'];h=f['hi'];u=f['singleton_counts']
J={tuple(r['pair']):r['multiplicity'] for r in f['J']}
assert f['inventory']==[6,2,0] and f['nine_degree_point']==0
assert sum(J.values())==6 and sum(u)==26
assert all(u[v]+s[v]+h[v]+int(v in C)==d[v] for v in range(6))
assert all(s[v]+sum(len(t)-1 for t in T if v in t)<=4*d[v]-18-4*int(v in C) for v in range(6))
for p in combinations(range(6),2):
 assert set(p)<=C or any(set(p)<=t for t in T) or J.get(p,0)>0
expected_sigs={}
for k in (2,3):
 for blue in combinations(range(6),k):
  S=set(blue)
  if not S&C:continue
  pos=Counter({4:sum(u[v] for v in S)})
  neg=Counter({4:sum(u[v] for v in range(6) if v not in S)})
  for edge,v in J.items():
   if set(edge)<=S:pos[3]+=v
   elif set(edge).isdisjoint(S):neg[3]+=v
  for t in T:
   if t<=S:pos[5-len(t)]+=1
   elif t.isdisjoint(S):neg[5-len(t)]+=1
  expected_sigs[blue]=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4])
rows=f['all_proper_C_blue_pair_signatures']+f['all_proper_C_three_blue_signatures']
assert len(rows)==len(expected_sigs)==35
for r in rows:
 assert expected_sigs[tuple(r['blue'])]==tuple(r[q] for q in ('m4','m3','m2','m1','negative1','negative2','T','B'))
 assert r['gate'] is None
out={'status':'PASS','signed_choices_replayed':35,'pair_choices':15,'triple_choices':20,
     'small_negative_choices':sum(bool(r['negative1'] or r['negative2']) for r in rows),
     'all_blue_higher_three_trace_choices':sum(bool(r['m2']) for r in rows),
     'necessary_degree_capacity_and_P_pair_tests':True,
     'PL_realizability':'not determined; no exterior incidence construction asserted'}
(HERE/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
