from pathlib import Path
import array,json,time
D=Path(__file__).resolve().parent;ROOT=D.parents[6];start=time.process_time()
cache=D.parents[1]/'OLD_LENGTH_LE3_ENDPOINT_SETS.json'
j=json.loads(cache.read_text());assert j['exact_lengths']==[0,1,2,3] and j['generated_once']
A=array.array('I',[0])*(4*36*36);orbits=[];translated=0
for i in range(36):
 tau=i//18;b=(i%18)//2;eps=i%2;power=pow(23,b,38)
 orbits.append({'r':i,'tau':tau,'b':b,'epsilon':eps,'representative_label':342*tau+9*eps+b,'vertices':[342*tau+9*(eps+2*k)+b for k in range(19)]})
 for row in j['rows']:
  if row['source_type']!=tau:continue
  a=row['length'];rho=row['target_type'];endpoints=row['endpoints_and_one_actual_word'];assert len(endpoints)==row['count']
  for endpoint in endpoints:
   u=endpoint['endpoint_group_label'];ua,ub=divmod(u,9);assert 0<=u<342
   aa=(eps+power*ua)%38;bb=(b+ub)%9;r=18*rho+2*bb+(aa%2);k=aa//2
   A[(a*36+i)*36+r]|=1<<k;translated+=1
assert len({v for o in orbits for v in o['vertices']})==684
for i in range(36):assert A[i*36+i]==1 and sum(A[i*36+j].bit_count() for j in range(36))==1
with (D/'A_EXACT_LENGTH0_3.u32').open('wb') as f:A.tofile(f)
(D/'ORBIT_MAPPING.json').write_text(json.dumps(orbits,indent=2)+'\n')
schema={'status':'CACHE_CONVERSION_ONLY_NO_DP','A_layout':'(length*36+i)*36+j','A_type':'uint32_little_endian_low19bits','A_entries':len(A),'old_cache_rows':len(j['rows']),'translated_stored_endpoints':translated,'action':'h_r*u (left), h_r=(epsilon,b)','label':'342*tau+9*(epsilon+2*k)+b','variable':'1+((r*36+s)*19+t)','original_variables':24624,'source_parse_count':0,'old_DP_BFS_field_runs':0,'converter_actual_CPU':time.process_time()-start}
(D/'CACHE_CONVERSION.json').write_text(json.dumps(schema,indent=2)+'\n');print(json.dumps(schema),flush=True)
