from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();d=json.loads((P/'RESULT.json').read_text())
tables={tuple(z['types']):z for z in d['residual_types']}
def comps(n,k):
 if k==1:yield (n,);return
 for a in range(n+1):
  for tail in comps(n-a,k-1):yield (a,)+tail
out=[]
for r in d['remaining']:
 h=[sum(t>>v&1 for t in r['traces']) for v in range(5)];minimal_d=[1+a+b for a,b in zip(r['k_by_v'],h)];generic=[];actual=[]
 for delta in comps(31-r['sum_k'],5):
  a=[x+y for x,y in zip(r['k_by_v'],delta)]
  if not all(x in tables[tuple(t)]['failure_a'] for x,t in zip(a,r['types_by_v'])):continue
  deg=[1+x+y for x,y in zip(a,h)];ex=sum(max(x-9,0) for x in deg)
  z={'attachments':a,'original_F_degrees':deg,'F_high_excess':ex};generic.append(z)
  if min(deg)>=6 and sum(x==6 for x in deg)<=1 and ex<=4:actual.append(z)
 assert len(generic)==r['failed_attachment_compositions']
 out.append({**r,'h_by_v':h,'minimal_F_degrees':minimal_d,'minimal_F_high_excess':sum(max(x-9,0) for x in minimal_d),'generic_tail':generic,'A2_A3_local_necessary_tail':actual,'A2_at_most_two_sevens_count':sum(sum(x==7 for x in z['original_F_degrees'])<=2 for z in actual),'A3_at_most_three_sevens_count':sum(sum(x==7 for x in z['original_F_degrees'])<=3 for z in actual)})
res={'scope':'Exact small tail from the preceding complete91-orbit threshold domain; actual filter uses only min original degree6, at most one degree6, F high-excess above9 at most4. Separately counted at most2/3 degree7 vertices in F. No original-H realizability claim.','source_trace_orbits':91,'generic_tail_orbits':len(out),'generic_tail_attachment_count':sum(len(x['generic_tail']) for x in out),'actual_necessary_tail_orbits':sum(bool(x['A2_A3_local_necessary_tail']) for x in out),'actual_necessary_tail_attachment_count':sum(len(x['A2_A3_local_necessary_tail']) for x in out),'rows':out,'cpu_seconds':time.process_time()-st}
(P/'TAIL_RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
lines=['# q=3 threshold residuals','', 'All3276 labeled trace triples form91 actual S5 orbits. The primary red-tree bound closes68 orbits. The23 residuals have only'+str(res['generic_tail_attachment_count'])+' attachment compositions in total. The actual A2/A3 local degree/high-excess constraints leave'+str(res['actual_necessary_tail_orbits'])+' orbits / '+str(res['actual_necessary_tail_attachment_count'])+' compositions. This is a necessary domain, not a counterexample set.','', '|Trace masks|k by vertex|h by vertex|degrees at k|high excess at k|Generic tail|Actual necessary tail|A2/A3 counts|','|---|---|---|---|---:|---:|---:|---|']
for r in out:
 lines.append('|'+str(r['traces'])+'|'+str(r['k_by_v'])+'|'+str(r['h_by_v'])+'|'+str(r['minimal_F_degrees'])+'|'+str(r['minimal_F_high_excess'])+'|'+str(len(r['generic_tail']))+'|'+str(len(r['A2_A3_local_necessary_tail']))+'|'+str(r['A2_at_most_two_sevens_count'])+'/'+str(r['A3_at_most_three_sevens_count'])+'|')
lines+=['','An actual necessary tail example is listed in `TAIL_RESULT.json`; each has `d_v=1+a_v+h_v`, sum a31, all17 choices of r fail this bound at every v, and all stated local constraints. No claim q=3 implies B has been proved.']
(P/'TAIL_TABLE.md').write_text('\n'.join(lines)+'\n')
print({k:v for k,v in res.items() if k!='rows'})
for r in out:
 if r['A2_A3_local_necessary_tail']:print(r['traces'],'count',len(r['A2_A3_local_necessary_tail']),'example',r['A2_A3_local_necessary_tail'][0])
