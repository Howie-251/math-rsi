import csv,itertools,json,time
from collections import Counter
from pathlib import Path
q=Path(__file__).resolve().parent;t=time.process_time()
rows=list(csv.DictReader((q.parent/'WALK_LINEAR_FORMS.tsv').open(),delimiter='\t'))
groups={}
for r in rows:
 k=(int(r['root_base']),int(r['target_base']))
 v=tuple(int(r[x]) for x in ['alpha0','alpha1','alpha2','sigma','tau'])+(int(r['half'])%2,)
 groups.setdefault(k,set()).add(v)
forms=sorted(groups[1,2]);assert len(forms)==36
out={}
for modulus in [2,3,4]:
 profiles=[]
 for a in itertools.product(range(modulus),repeat=5):
  hits=Counter((sum(x*y for x,y in zip(a,v[:5]))+18*v[5])%modulus for v in forms)
  if all(hits[r]==36//modulus for r in range(modulus)):profiles.append(a)
 out[str(modulus)]={'tested_profiles':modulus**5,'balanced_profiles':len(profiles),'profiles':profiles}
result={'status':'COMPLETE_SYMBOLIC_CAPACITY_AND_M36_NECESSARY_RESIDUE_GATE','base_pair_symbolic_type_counts':{str(k):len(v) for k,v in groups.items()},'unconditional_even_m_upper':36,'controller_order_upper':108,'m36_residue_gates':out,'m36_excluded_by_empty_necessary_domain':any(v['balanced_profiles']==0 for v in out.values()),'CPU_seconds':time.process_time()-t,'CPU_budget_seconds':1,'controller_fiber_BFS_solver_Lean_runs':0,'all_jobs_terminal':True}
assert result['CPU_seconds']<1
(q/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(q/'DISTINCT_1_TO_2_FORMS.tsv').write_text('alpha0\talpha1\talpha2\tsigma\ttau\thalf\n'+'\n'.join('\t'.join(map(str,v)) for v in forms)+'\n')
print({k:v for k,v in result.items() if k!='m36_residue_gates'})
print({k:{x:v[x] for x in ['tested_profiles','balanced_profiles']} for k,v in out.items()})
