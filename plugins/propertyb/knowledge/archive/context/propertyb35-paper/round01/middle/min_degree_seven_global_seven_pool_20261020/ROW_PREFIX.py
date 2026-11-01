from pathlib import Path
from math import comb,ceil
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();d=json.loads((P/'RESULT.json').read_text());rows=[]
for row in d['rows']:
 ds=row['high_degrees'];q=[]
 for mask in range(8):
  k=mask.bit_count();r=5-k;DF=7*r+sum(x for j,x in enumerate(ds) if mask>>j&1)
  q.append(max(4,ceil((DF-39-comb(r,2))/k)) if k else 4)
 vals=[]
 for z in row['domain']:
  weighted=sum(n*b for n,b in zip(z['high_trace_counts'],q))
  vals.append({'pair_codegrees':z['pair_codegrees'],'triple':z['triple'],'degree_sum_lower':weighted,'Gamma_edges_lower':ceil(weighted/2)})
 rows.append({'high_degrees':ds,'q_lower_by_high_trace_mask':q,'necessary_domain':len(vals),'min_Gamma_edges_lower':min(z['Gamma_edges_lower'] for z in vals),'max_Gamma_edges_lower':max(z['Gamma_edges_lower'] for z in vals),'best_possible_bound_witness':min(vals,key=lambda z:z['Gamma_edges_lower']),'all_bounds':vals})
res={'status':'COMPLETE_SHARED_SEVEN_PAIR_BUDGET_ROW_PREFIX','scope':'Assume actual nonB H21min7 =>Gamma min4 and at least3 sevenpoints =>lambda77<=2. Each edge F with k nonseven points and r=5-k sevenpoints has DF-39<=k qGamma(F)+C(r,2). No global e cap or paircap4.','rows':rows,'cpu_seconds':time.process_time()-start}
(P/'ROW_PREFIX_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print('CPU',res['cpu_seconds'])
for r in rows:print({k:v for k,v in r.items() if k!='all_bounds'})
