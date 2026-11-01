"""qGamma-degree3 flag budget plus fixed-count convex degree box, frozen5813 keys."""
from pathlib import Path
from math import comb
from itertools import combinations
from functools import lru_cache
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();base=P.parent/'a2_a3_joint_moment_frontier_20261020'
tail=json.loads((P.parent/'three_nonunit_direct_repair_20261020/TAIL_RESULT.json').read_text());source=[]
for row in tail['rows']:
 T=row['traces'];flag=sum(comb((a&b).bit_count(),2) for a,b in combinations(T,2));h=[sum(bool(t&(1<<i)) for t in T) for i in range(5)]
 for q in row['A2_A3_local_necessary_tail']:
  a=q['attachments'];ds=[1+a[i]+h[i] for i in range(5)];assert ds==q['original_F_degrees'] and sum(a)==31
  source.append({'traces':T,'attachments':a,'degrees':ds,'flag':flag})
assert len(source)==83 and len({tuple(s['traces']) for s in source})==16
zero=[s for s in source if s['flag']==0];assert zero==[{'traces':[3,13,22],'attachments':[6,6,7,6,6],'degrees':[9,9,10,8,8],'flag':0}]
assert all(sum(d==10 for d in q['degrees'])==1 and sum(d==8 for d in q['degrees'])==2 and sum(d==9 for d in q['degrees'])==2 for q in zero)
(P/'SOURCE_AUDIT.json').write_text(json.dumps({'status':'PASS','actual_tail_keys':83,'trace_orbits':16,'zero_flag_keys':zero,'all83_flag_keys':source},indent=2)+'\n')
old=json.loads((base/'CONDITIONAL_CRITICAL_SURVIVORS.json').read_text());assert len(old)==5813
jobs=json.loads((base/'RESULT.json').read_text())['jobs'];degree={j['unique_degree_key']:j['degrees'] for j in jobs}
def f(s):
 a,b=divmod(s,5)
 return (s*s-(5-b)*a*a-b*(a+1)**2)//2
@lru_cache(None)
def box(E,z):
 best=-1;witness=None
 for m in range(min(35,z)+1):
  k=35-m;X=2*E-3*m-4*k
  if not 0<=X<=25*k:continue
  a,b=divmod(X,25)
  value=m*f(31)+a*f(5)+(f(30-b)+(k-a-1)*f(30) if a<k else 0)
  if value>best:best=value;witness={'q3_count':m,'other_count':k,'X':X,'q29_count':a,'remainder':b}
 return best,witness
modes=[]
for mode in ('pair_resource_only','all_resources'):
 surviving=[]
 for row in old:
  ds=degree[row['unique_degree_key']];n=row['n'];tau=row['tau'];E=595-n[1]
  h10=ds.count(10);b8=ds.count(8);c9=ds.count(9)
  resources=[2*n[2],10*h10,4*b8,(9*c9)//2]
  zero_cap=resources[0] if mode=='pair_resource_only' else min(resources)
  z=3*tau+zero_cap;cap,w=box(E,z)
  if cap<0:continue
  budget=min(row['P'],cap);C=[0]*5;rem=budget
  for j in range(4,-1,-1):C[j]=min(rem,row['C_caps'][j]);rem-=C[j]
  L2=sum(x*y for x,y in zip(C,(36,120,330,792,1716)))+6864*n[1]
  if L2>=5445440:surviving.append({**row,'previous_P':row['P'],'q3_upper':z,'zero_flag_resources':resources,'q3_box_bound':cap,'q3_box_witness':w,'P':budget,'C':C,'twice_L':L2,'margin':(L2-5445440)//2})
 def summary(rr):
  d={'survivors':len(rr),'distinct_moment_keys':len({(tuple(s['n']),s['tau']) for s in rr})}
  if rr:d.update({'n4_range':[min(s['n'][4] for s in rr),max(s['n'][4] for s in rr)],'tau_range':[min(s['tau'] for s in rr),max(s['tau'] for s in rr)],'closest_witness':min(rr,key=lambda s:(s['margin'],s['tau'],s['n'][4])),'minimum_high_witness':min(rr,key=lambda s:(s['n'][3]+s['n'][4],s['tau'],s['n'][4]))})
  return d
 per=[]
 for job in jobs:
  rr=[s for s in surviving if s['unique_degree_key']==job['unique_degree_key']]
  per.append({'unique_degree_key':job['unique_degree_key'],'a':job['a'],'b':job['b'],'partition':job['partition'],**summary(rr)})
 out={'mode':mode,'jobs':per,**summary(surviving)};modes.append(out)
 (P/('SURVIVORS_'+mode+'.json')).write_text(json.dumps(surviving,indent=2)+'\n')
 print(mode,out['survivors'],out['distinct_moment_keys'],'margin',out.get('closest_witness',{}).get('margin'),flush=True)
 for job in per:print(' ',job['a'],job['b'],job['partition'],job['survivors'],flush=True)
assert modes[0]['survivors']==4534
out={'scope':__doc__,'source_keys':len(old),'actual_tail_source_keys':83,'unique_zero_flag_type':zero,'modes':modes,'box_cache_entries':box.cache_info().currsize,'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print('CPU',out['cpu_seconds'])
