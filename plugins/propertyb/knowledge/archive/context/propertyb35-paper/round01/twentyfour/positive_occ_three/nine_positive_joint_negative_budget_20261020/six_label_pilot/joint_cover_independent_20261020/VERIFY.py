"""No scipy, no LP rerun, no generator imports: exact independent certificate check."""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
PAIRS=tuple(combinations(range(6),2))
TYPES={'N2':(2,(1,1,1)),'T3':(3,(1,0,1)),
       'Bx3':(3,(0,1,1)),'N4':(4,(0,0,1))}

def recover(graph):
 sets=[set() for _ in range(6)];pid=0
 for (a,b),n in zip(PAIRS,graph):
  for _ in range(n):sets[a].add(pid);sets[b].add(pid);pid+=1
 for s in sets:
  while len(s)<4:s.add(pid);pid+=1
  assert len(s)==4
 return sets

def main():
 started=time.process_time()
 source=json.loads((BASE/'CENSUS_SUMMARY.json').read_text())
 raw=json.loads((BASE/'joint_cover_lp'/'ALL77.json').read_text())
 expected={tuple(r['vector']):r for r in source['all_raw_bound_nongated_records']
           if not r['resolved_by_two_isolates']}
 actual={tuple(r['graph']):r for r in raw['rows']}
 assert len(expected)==len(actual)==len(raw['rows'])==77 and actual.keys()==expected.keys()
 reports=[];exceptions=[]
 for graph,row in actual.items():
  sets=recover(graph);assert [sorted(s) for s in sets]==row['sets']
  U=sorted(set().union(*sets));freq=Counter(v for s in sets for v in s)
  assert U==list(range(len(U))) and max(freq.values())<=2 and len(U)<=17
  caps=[7-freq[v] for v in U];budgets=[3,4,20]+caps
  assert row['budgets']==budgets
  candidates=[tuple(c) for k in (3,4) for c in combinations(U,k)
              if all(set(c)&s for s in sets)]
  c3=sum(len(s)==3 for s in candidates);c4=len(candidates)-c3
  assert (c3,c4)==(row['C3'],row['C4'])==(expected[graph]['C3'],expected[graph]['C4'])
  assert c3==row['M3'] and sum(graph)==row['E'] and len(candidates)==row['candidate_rows']
  cset=set(candidates)
  active={k:{tuple(f) for s in candidates for f in combinations(s,k)} for k in (2,3,4)}
  assert len(active[2])+2*len(active[3])+len(active[4])==row['negative_variables']
  cert=row.get('dual_certificate')
  if not cert:
   exceptions.append(dict(graph=graph,E=sum(graph),C3=c3,C4=c4,sets=row['sets']))
   continue
  beta=list(map(Q,cert['budget_weights']));assert len(beta)==len(budgets) and min(beta)>=0
  weights={}
  for item in cert['coverage_weights']:
   s=tuple(item['red_set']);value=Q(item['weight'])
   assert s in cset and s not in weights and value>=0
   weights[s]=value
  assert sum(weights.values(),Q())==1
  gamma={}
  for item in cert['upper_bound_weights']:
   typ=item['type'];f=tuple(item['negative_set']);value=Q(item['weight'])
   assert typ in TYPES and len(f)==TYPES[typ][0] and len(set(f))==len(f)
   assert f==tuple(sorted(f)) and set(f)<=set(U) and value>=0 and (typ,f) not in gamma
   gamma[typ,f]=value
  W={k:Counter() for k in (2,3,4)}
  for s,lam in weights.items():
   for k in (2,3,4):
    for f in combinations(s,k):W[k][f]+=lam
  checked=0;worst_slack=None
  # Check ALL U targets, including targets inactive on every candidate.
  # This independently verifies the four source types and all point prices.
  for typ,(size,coeff) in TYPES.items():
   base=sum(beta[j]*coeff[j] for j in range(3))
   for f in combinations(U,size):
    cost=base+sum(beta[3+v] for v in f)+gamma.get((typ,f),Q())
    lhs=W[size].get(f,Q());slack=cost-lhs
    assert slack>=0,(graph,typ,f,str(lhs),str(cost))
    worst_slack=slack if worst_slack is None else min(worst_slack,slack)
    checked+=1
  objective=sum(Q(b)*v for b,v in zip(budgets,beta))+sum(gamma.values(),Q())
  assert objective==Q(cert['coverage_upper_bound']) and objective<1
  reports.append(dict(graph=graph,C3=c3,C4=c4,targets_checked=checked,
                      candidate_weight_sum='1',upper_multiplier_count=len(gamma),
                      upper_multiplier_sum=str(sum(gamma.values(),Q())),
                      exact_bound=str(objective),strict_margin=str(1-objective),
                      minimum_target_slack=str(worst_slack)))
 assert len(reports)==76 and len(exceptions)==1
 assert exceptions[0]['graph']==(0,0,0,0,0,0,0,0,1,2,2,0,2,0,0)
 maximum=max(Q(r['exact_bound']) for r in reports);assert maximum==Q(10,11)
 # Verify the small integer inequalities in the exceptional proof.
 K=[set(range(0,2)),set(range(2,4)),set(range(4,6))]
 coreedges=[{a,b} for i in range(3) for j in range(i+1,3) for a in K[i] for b in K[j]]
 minima=[]
 for ell in range(4):
  left=min(sum(not e&set(deleted) for e in coreedges) for deleted in combinations(range(6),ell))
  assert left==(12,8,4,2)[ell];minima.append(left)
 coarse=[]
 for u0 in range(3):
  vals=[]
  for u1 in range(4-u0):
   for s0 in range(4-u0-u1):
    for s1 in range(4-u0-u1-s0):
     for v0 in range(5-u0-u1):
      for v1 in range(5-u0-u1-v0):
       q=5-u0-s0-v0
       if q>=0:vals.append(16*u0+4*u1+4*s0+s1+4*v0+v1+q)
  coarse.append(max(vals));assert coarse[-1]<48
 final=max(4*v0+v1+(2-v0) for v0 in range(2) for v1 in range(2-v0))
 assert final==5 and min((4-3+ell)*minima[ell] for ell in range(4))==8
 out=dict(pass_all=True,source_key_set_exactly_equal=True,source_residual_keys=77,
          verified_rational_certificates=76,maximum_exact_bound=str(maximum),
          all_target_inequalities=sum(r['targets_checked'] for r in reports),
          all_upper_multipliers_checked=True,exception=exceptions[0],
          exceptional_integer_checks=dict(core_edges_after_l_deletions=minima,
             coarse_maxima_u0_0_1_2=coarse,final_blocker_bound=final,minimum_remaining_candidates=8),
          rows=reports,process_seconds=time.process_time()-started,
          scope=__doc__)
 (HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',len(reports),'max',maximum,'targets',out['all_target_inequalities'],
       'exception',out['exceptional_integer_checks'],'CPU',out['process_seconds'])

if __name__=='__main__':main()
