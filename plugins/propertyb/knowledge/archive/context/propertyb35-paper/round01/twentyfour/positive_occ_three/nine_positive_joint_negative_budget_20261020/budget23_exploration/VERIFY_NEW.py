"""Stdlib exact checks of19 new23-budget certificates, complete981 difference, fulltarget columns."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
from fractions import Fraction as F
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
diff=json.loads((HERE/'DIFFERENCE.json').read_text());new=json.loads((HERE/'SOLVE_NEW.json').read_text())
old=json.loads((HERE.parent/'six_label_pilot/CENSUS_PROFILE.json').read_text())
source={tuple(r['vector']):r for r in old['rows']}
expected={tuple(r['graph']) for r in diff['newly_nongated_records']}
assert len(expected)==19 and {tuple(r['graph']) for r in new['rows']}==expected
# Recompute the complete23-budget delta from every old40-parameter row,
# including the old902 rows; no reliance on discovery's selected key list.
recomputed=set();raw=set();base_raw=set()
for key,r in source.items():
 assert len(r['maximal_b_parameter_rows'])==40
 fail20=any(p['C3_margin']<=0 and p['C4_margin']<=0 for p in r['maximal_b_parameter_rows'])
 fail23=any(p['C3_margin']<=0 and p['C4_margin']<=3 for p in r['maximal_b_parameter_rows'])
 if fail20:base_raw.add(key)
 if fail23:raw.add(key)
 if fail23 and not fail20:recomputed.add(key)
assert len(base_raw)==79 and len(raw)==98 and recomputed==expected
assert sum(r['orbit_size'] for r in source.values())==417328
# Every newcase uses the ordinary three jointbudgets plus pointprices only;
# the optional86-incidence row is deliberately absent.
assert new['budget_total']==23

EDGES=list(combinations(range(6),2));checked=0;bounds=[]
for r in new['rows']:
 g=r['graph'];s=source[tuple(g)];assert not s['nongated_maximal_b_rows']
 A=[set() for _ in range(6)];deg=[0]*6;n=0
 for (a,b),v in zip(EDGES,g):
  deg[a]+=v;deg[b]+=v
  for _ in range(v):A[a].add(n);A[b].add(n);n+=1
 for a in range(6):
  for _ in range(4-deg[a]):A[a].add(n);n+=1
 assert [sorted(a) for a in A]==r['sets']==s['sets']
 U=tuple(range(n));reds={frozenset(q) for k in (3,4) for q in combinations(U,k) if all(set(q)&a for a in A)}
 assert reds==set(map(frozenset,r['candidate_red_sets']))
 assert sum(len(a)==3 for a in reds)==r['C3'] and sum(len(a)==4 for a in reds)==r['C4']
 c=r['dual_certificate'];weights={frozenset(q['red_set']):F(q['weight']) for q in c['coverage_weights']}
 assert weights.keys()<=reds and all(w>=0 for w in weights.values()) and sum(weights.values())==1
 beta=list(map(F,c['budget_weights']));assert len(beta)==3+n and all(w>=0 for w in beta)
 gamma={(q['type'],frozenset(q['negative_set'])):F(q['weight']) for q in c['upper_bound_weights']}
 assert all(w>=0 for w in gamma.values())
 price={k:defaultdict(F) for k in (2,3,4)}
 for red,w in weights.items():
  for k in (2,3,4):
   for q in combinations(sorted(red),k):price[k][frozenset(q)]+=w
 for size,types in ((2,('N2',)),(3,('T3','Bx3')),(4,('N4',))):
  for q in combinations(U,size):
   Q=frozenset(q);pp=sum(beta[3+v] for v in q)
   for typ in types:
    rhs=beta[2]+pp+gamma.get((typ,Q),F(0))
    if typ in ('N2','T3'):rhs+=beta[0]
    if typ in ('N2','Bx3'):rhs+=beta[1]
    assert price[size][Q]<=rhs
    checked+=1
 B=[3,4,23]+[7-sum(v in a for a in A) for v in U]
 assert B==r['budgets']
 bound=sum(w*b for w,b in zip(beta,B))+sum(gamma.values())
 assert bound==F(c['coverage_upper_bound']) and bound<1
 bounds.append(str(bound))
# The old76 proof rows are unchanged; only their third RHS coefficient grows3.
oldcert=json.loads((HERE.parent/'six_label_pilot/joint_cover_lp/ALL77.json').read_text())
olddualkeys=set();integerkeys=set();b21=[]
for r in oldcert['rows']:
 if 'dual_certificate' in r:
  c=r['dual_certificate'];v=F(c['coverage_upper_bound'])+3*F(c['budget_weights'][2]);assert v<1;b21.append(v);olddualkeys.add(tuple(r['graph']))
 else:integerkeys.add(tuple(r['graph']))
assert len(b21)==76 and len(integerkeys)==1
old77=olddualkeys|integerkeys
isolate_extra=base_raw-old77
assert len(isolate_extra)==2 and all(source[k]['two_isolates_analytic_repair'] for k in isolate_extra)
classes={'raw_sum_strict':set(source)-raw,'two_isolates_extra':isolate_extra,
         'olddual':olddualkeys,'integer':integerkeys,'newdual':expected}
assert set.union(*classes.values())==set(source)
assert sum(map(len,classes.values()))==len(source)==981
partition={k:{'orbits':len(v),'labelled':sum(source[a]['orbit_size'] for a in v)} for k,v in classes.items()}
out={'status':'PASS','new_graph_keys_exactly_nineteen_delta_keys':True,'nineteen_old20_rows_were_sum_strict':True,
 'new_all_target_inequalities_checked':checked,'new_exact_bounds':bounds,'new_exact_max':str(max(map(F,bounds))),
 'old981_partition':partition,
 'all_new_upper_weights_empty':all(not r['dual_certificate']['upper_bound_weights'] for r in new['rows']),
 'global86_resource_row_used':False,
 'old76_newcost_all_strict':True,'old76_max_bound23':str(max(b21)),
 'no_scipy_or_solver_import':True,'cpu_seconds':time.process_time()-start}
(HERE/'VERIFY_NEW.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
