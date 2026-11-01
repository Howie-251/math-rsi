"""Read-only certificate replay: standard library, no LP/generator imports."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as F
import json,time

HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(4),2))
SOURCES={'Tpair':(2,(1,0,1)),'Ttriple':(3,(1,0,0)),
         'Bpair':(2,(0,1,2)),'Btriple':(3,(0,1,1)),'B4':(4,(0,1,0))}

def main():
 started=time.process_time()
 profile=json.loads((HERE/'PROFILE.json').read_text())
 data=json.loads((HERE/'ALL_LP.json').read_text())
 key=lambda r:(r['n'],tuple(r['capacities']),tuple(r['graph']))
 domain={key(r):r for r in profile['representatives']}
 supplied={key(r):r for r in data['rows']}
 assert len(domain)==len(supplied)==len(data['rows'])==1333 and domain.keys()==supplied.keys()
 assert profile['labelled']==sum(r['orbit_size'] for r in domain.values())==5573
 reports=[];total_targets=0
 for k,row in supplied.items():
  n,cap,graph=k;assert n in (0,1,2) and all(4-n<=a<=4 for a in cap)
  assert sum(cap)>=(16,13,10)[n]
  A=[set() for _ in range(4)];point=0
  for i,m in enumerate(graph):
   for _ in range(m):
    for label in PAIRS[i]:A[label].add(point)
    point+=1
  for label in range(4):
   while len(A[label])<cap[label]:A[label].add(point);point+=1
   assert len(A[label])==cap[label]
  assert [sorted(a) for a in A]==row['sets']
  U=sorted(set().union(*A));assert U==list(range(len(U))) and len(U)<=16-n
  freq=Counter(v for a in A for v in a);assert max(freq.values())<=2
  budget=[2-n,18,8-2*n]+[7-freq[v] for v in U];assert budget==row['budgets']
  candidates={tuple(s) for size in range(1,5) for s in combinations(U,size) if all(set(s)&a for a in A)}
  assert len(candidates)==row['candidate_count']
  assert {str(s):v for s,v in Counter(map(len,candidates)).items()}==row['candidate_counts']
  active={size:{f for s in candidates for f in combinations(s,size)} for size in (2,3,4)}
  assert 2*len(active[2])+2*len(active[3])+len(active[4])==row['negative_variable_count']
  cert=row['dual_certificate'];beta=list(map(F,cert['budget_weights']))
  assert len(beta)==len(budget) and min(beta)>=0
  weights={}
  for item in cert['candidate_weights']:
   s=tuple(item['red_set']);w=F(item['weight'])
   assert s in candidates and s not in weights and w>=0;weights[s]=w
  assert sum(weights.values(),F())==1
  gamma={}
  for item in cert['upper_bound_weights']:
   typ=item['type'];s=tuple(item['negative_set']);g=F(item['weight'])
   assert typ in SOURCES and len(s)==SOURCES[typ][0] and s==tuple(sorted(set(s)))
   assert set(s)<=set(U) and g>=0 and (typ,s) not in gamma;gamma[typ,s]=g
  extensions={size:Counter() for size in (2,3,4)}
  for s,w in weights.items():
   for size in (2,3,4):
    for f in combinations(s,size):extensions[size][f]+=w
  checked=0
  for typ,(size,costs) in SOURCES.items():
   base=sum(beta[j]*costs[j] for j in range(3))
   for target in combinations(U,size):
    rhs=base+sum(beta[3+v] for v in target)+gamma.get((typ,target),F())
    assert extensions[size].get(target,F())<=rhs,(k,typ,target)
    checked+=1
  value=sum(b*v for b,v in zip(budget,beta))+sum(gamma.values(),F())
  assert value==F(cert['bound'])<1
  reports.append(dict(n=n,capacities=cap,graph=graph,exact_bound=str(value),targets_checked=checked,
                      upper_multiplier_count=len(gamma),upper_multiplier_sum=str(sum(gamma.values(),F()))))
  total_targets+=checked
 maximum=max(F(r['exact_bound']) for r in reports);assert maximum==F(10,11)
 result=dict(pass_all=True,full_profile_key_set_equal=True,representatives=1333,labelled_domain=5573,
             all_target_inequalities=total_targets,maximum_bound=str(maximum),rows=reports,
             all_upper_multiplier_count=sum(r['upper_multiplier_count'] for r in reports),
             process_seconds=time.process_time()-started,scope=__doc__)
 (HERE/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',len(reports),'targets',total_targets,'max',maximum,'CPU',result['process_seconds'])

if __name__=='__main__':main()
