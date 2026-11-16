"""Sound arithmetic incidence bounds on saved provider tables; no search or BFS."""
from pathlib import Path
from collections import Counter
import json, math, resource, time
OUT=Path(__file__).resolve().parent
def main():
 t=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(2,3))
 data=json.loads((OUT/'LINE_PROVIDER_TABLES.json').read_text())
 rows=[];hist=Counter();allopen=0;ruledout=0
 for p in data['planes']:
  if p['status']!='NECESSARY_GATE_OPEN':continue
  allopen+=1;inc={}
  for ell,providers in enumerate(p['line_free_pin_providers']):
   for v in providers:inc[v]=inc.get(v,0)|(1<<ell)
  forced=p['forced_pin_ids'];covered=0
  for v in forced:covered|=inc[v]
  residual=((1<<91)-1)^covered
  contributions=sorted(((bits&residual).bit_count() for v,bits in inc.items() if v not in forced),reverse=True)
  target=residual.bit_count();total=0;k=0
  while total<target and k<len(contributions):total+=contributions[k];k+=1
  assert total>=target
  maxcover=max(bits.bit_count() for bits in inc.values())
  lb=max(math.ceil(91/maxcover),len(forced)+k)
  hist[lb]+=1;ruledout+=lb>12
  rows.append(dict(plane_global_id=p['plane_global_id'],available_pin_count=len(inc),forced_pin_ids=forced,
    maximum_lines_per_pin=maxcover,uncovered_lines_after_forced=target,
    residual_top_contributions=contributions,strict_pin_lower_bound=lb,
    excludes_budget12=lb>12))
 result=dict(status='COMPLETE_ARITHMETIC_NECESSARY_BOUND_ONLY',planes_previously_open=allopen,
   lower_bound_histogram=dict(hist),further_excluded_by_lower_bound=ruledout,
   still_not_excluded=allopen-ruledout,planes=rows,CPU_seconds=time.process_time()-t,
   BFS_calls=0,search_calls=0,solver_calls=0,
   proof='Forced singleton-provider pins must be selected. After their union, k other columns cover at most the sum of the k largest residual incidence counts. This ignores overlaps and so is a necessary lower bound, not feasibility.')
 (OUT/'INCIDENCE_RESOURCE_BOUNDS.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='planes'}))
 print('anchor635',next(r for r in rows if r['plane_global_id']==635))
if __name__=='__main__':main()
