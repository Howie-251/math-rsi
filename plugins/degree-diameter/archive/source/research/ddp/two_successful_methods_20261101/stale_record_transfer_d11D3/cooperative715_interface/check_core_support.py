#!/usr/bin/env python3
"""New actual715 class/core two-step premise binding; no sourceD3 or585 check."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json,resource,math
P=Path(__file__).resolve().parent;R=P.parents[4]
OLD=R/'research/ddp/more_graphs_20261027/d3d4_transfer'
old=json.loads((OLD/'RESULT.json').read_text())['source715'];classes=old['classes']
rows=[set(map(int,s.split())) for s in (OLD/'source715.implicit_adj.txt').read_text().splitlines() if s.strip()]
F={x for c in classes for x in c['members']};B=set(range(old['n']))-F
N={c['class']:set(c['common_saturated_neighbors']) for c in classes}
owner={x:a for a,ns in N.items() for x in ns}
T={}
for c in classes:
 a=c['class'];v=c['members'][0]
 r2=set(rows[v])
 for u in rows[v]:r2.update(rows[u])
 T[a]=r2&B
S={t:tuple(a for a in range(65) if t in T[a]) for t in sorted(B)}
one=Counter(a for block in S.values() for a in block)
two=Counter(pair for block in S.values() for pair in combinations(block,2))
three=Counter(triple for block in S.values() for triple in combinations(block,3))
intersection_hist=Counter();bad=[]
for a in range(65):
 for b in range(65):
  k=len(T[a]&N[b]);intersection_hist[(a==b,k)]+=1
  if k!=(8 if a==b else 1):bad.append([a,b,k])
checks={'class_count':len(classes)==65,'core_count':len(B)==520,'owner_covers_core':set(owner)==B,
 'own_class_8_other_class_1':not bad,
 'S_all_size9':all(len(s)==9 for s in S.values()),'S_distinct520':len(set(S.values()))==520,
 'each_single72':len(one)==65 and set(one.values())=={72},
 'each_pair9':len(two)==math.comb(65,2) and set(two.values())=={9},
 'each_triple1':len(three)==math.comb(65,3) and set(three.values())=={1}}
# Integer partitions of one class's8or9 total hits among8core targets.
def partitions(n,lo=1):
 if n==0:yield [];return
 for a in range(lo,n+1):
  for rest in partitions(n-a,a):yield[a]+rest
def f(k):return math.comb(k,2)-(math.comb(k,3) if k>=3 else 0)
part={}
for a in [8,9]:
 ps=[x for x in partitions(a) if len(x)<=8];values=[sum(f(k) for k in x) for x in ps];best=max(values)
 witness=next(x for x,val in zip(ps,values) if val==best)
 full=[sum(f(k) for k in x) for x in ps if len(x)==8]
 part[str(a)]={'partitions':len(ps),'maximum_moment':best,'maximizing_partition':witness,'full_covered_class_moments':sorted(set(full)),
 'outside_class_count':65-a,'outside_moment_lower_bound':7*math.comb(a,2)-math.comb(a,3)}
checks['partition8_max5_full0']=part['8']['maximum_moment']==5 and part['8']['full_covered_class_moments']==[0]
checks['partition9_max6_full1']=part['9']['maximum_moment']==6 and part['9']['full_covered_class_moments']==[1]
u=resource.getrusage(resource.RUSAGE_SELF);cpu=u.ru_utime+u.ru_stime
support=dict(date='2026-11-01',status='PASS_ACTUAL715_NEW_CORE_R2_AND_DESIGN_PREMISES' if all(checks.values()) else 'FAILED_NEW_PREMISES',checks=checks,source='research/ddp/more_graphs_20261027/d3d4_transfer/source715.implicit_adj.txt',source_adjacency_parses=1,canonical_class_core_R2_expansions=65,sourceD3_BFS_runs=0,eligibleR2_rechecks=0,old585_adjacency_parses=0,old585_R2_or_Steiner_rechecks=0,field_runs=0,helpergraph_or_solver_runs=0,old_source_check_reexecuted=False,
 T_size_histogram=dict(Counter(map(len,T.values()))),S_size_histogram=dict(Counter(map(len,S.values()))),intersection_histogram=[{'same_owner_class':same,'intersection':k,'ordered_class_pairs':v} for(same,k),v in sorted(intersection_hist.items())],single_multiplicity_histogram=dict(Counter(one.values())),pair_multiplicity_histogram=dict(Counter(two.values())),triple_multiplicity_histogram=dict(Counter(three.values())),first_failed_intersections=bad[:10],scalar_partition_bounds=part,CPU_seconds=cpu,prior_measured_metadata_CPU_seconds=0.035727,cumulative_measured_CPU_seconds=cpu+0.035727,CPU_budget_seconds=20)
(P/'CORE_SUPPORT_RESULT.json').write_text(json.dumps(support,indent=2)+'\n')
(P/'CORE_SUPPORT_DATA.json').write_text(json.dumps({'T_class_core_R2':{str(a):sorted(v) for a,v in T.items()},'S_core_class_blocks':{str(t):list(s) for t,s in S.items()},'core_owner_class':owner},indent=2)+'\n')
print(json.dumps(support,indent=2))
