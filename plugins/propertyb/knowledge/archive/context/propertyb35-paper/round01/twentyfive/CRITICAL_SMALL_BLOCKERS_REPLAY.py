"""Direct actual-H/initial-state replay and complete small signed-transversal
checks for the five G centers. No MILP or construction code is imported.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
P=Path(__file__).resolve().parent;d=json.loads((P/'CRITICAL_SMALL_BLOCKERS_PILOT.json').read_text());H=[frozenset(e) for e in d['actual_H']['edges']];G=frozenset(d['actual_H']['G']);red=frozenset(d['found']['initial_red']);L=frozenset(range(24))-red;assert len(set(H))==len(H)==35 and all(len(e)==5 for e in H);assert G in H
D=[sum(v in e for e in H) for v in range(24)];assert min(D)==7 and all(D[g]==7 for g in G);assert all(sum(a in e and b in e for e in H)>=1 for a,b in combinations(range(24),2));assert set(e for e in H if not e&red or not e&L)=={G};assert sum(D[g] for g in G)==35
records=[]
for g in sorted(G):
 pos=[e-{g} for e in H if e&G=={g} and e-{g}<=L];neg=[e&L for e in H if g not in e];assert all(neg);a=Counter(x for A in pos for x in A);assert len(pos)<=5 and sum(n-1 for n in a.values())<=5
 forbidden=set().union(*(B for B in neg if len(B)==1));available=[A-forbidden for A in pos];blocked=any(not A for A in available)
 # All minimal positive transversals are covered by selecting one point from
 # an uncovered positive set; a nonminimal solution contains a minimal one.
 seen=set();solutions=[]
 def visit(R):
  R=frozenset(R)
  if R in seen:return
  seen.add(R)
  if any(B<=R for B in neg):return
  todo=next((A for A in pos if not A&R),None)
  if todo is None:solutions.append(R);return
  for x in todo:visit(R|{x})
 visit(frozenset())
 record=dict(g=g,positive=[sorted(A) for A in pos],positive_multiplicity=dict(a),negative_size_counts=dict(Counter(map(len,neg))),forbidden_singleton_points=sorted(forbidden),positive_after_singleton_deletion=[sorted(A) for A in available],singleton_obstruction=blocked,complete_transversal_search_nodes=len(seen),repairable=bool(solutions),repair=sorted(min(solutions,key=lambda R:(len(R),sorted(R)))) if solutions else None)
 if solutions:
  rr=(red-{g})|set(record['repair']);assert all(0<len(e&rr)<5 for e in H);record['proper_red_after_repair']=sorted(rr)
 records.append(record)
# Explicit valid coloring is supplied by any repaired center, not solver claims.
assert records[0]['singleton_obstruction'] and not records[0]['repairable']
# If this particular initial state blocks every center, it is still only one
# state of a colorable H; a separate proper coloring can be found directly.
proper=next((z['proper_red_after_repair'] for z in records if z['repairable']),None)
out=dict(passed=True,scope=__doc__,n=24,M=35,degrees=D,G=sorted(G),initial_red=sorted(red),initial_only_bad_edge=sorted(G),G_degree_sum=35,edge_critical_or_nonB_claimed=False,centers=records,proper_red=proper)
(P/'CRITICAL_SMALL_BLOCKERS_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
