from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
source=json.loads((P.parent/'twentytwo_q3_global_compression_20261020/RESULT.json').read_text());rows=[]
for r in source['rows']:
 for z in r['actual_necessary_profiles']:
  if min(z['F_degrees'])<7:continue
  s=sum(r['sizes']);dirty=15-s;clean=s+2;outside=139-s
  ns=Counter({31:1});ns.update(r['traces'])
  for v,a in enumerate(z['attachments']):ns[1<<v]+=a
  assert sum(ns.values())==35 and all(4*z['attachments'][v]+sum(5-t.bit_count() for t in r['traces'] if t>>v&1)>=17 for v in range(5))
  rows.append({'traces':r['traces'],'attachments':z['attachments'],'F_degrees':z['F_degrees'],'s':s,'outside_total_degree':outside,'outside_excess_above7':20-s,'dirty_union_upper':dirty,'clean_lower':clean,'clean_degree_upper':(outside-7*dirty)//clean,'counts':dict(ns)})
assert len(rows)==277
out={'status':'COMPLETE22_MIN7_ANCHOR_NECESSARY_DOMAIN','scope':'Exact22 constants from complete3276/91 trace geometry, anchor tree residual546, min7 and17outside paircover filters. No21 probability certificate imported. Necessary profiles only.','source_trace_orbits':91,'source_labels':3276,'source_anchor_tail':546,'min7_profile_count':len(rows),'min7_trace_orbits':len({tuple(z['traces']) for z in rows}),'trace_size_sum_histogram':dict(Counter(z['s'] for z in rows)),'profiles':rows,'cpu_seconds':time.process_time()-st}
(P/'DOMAIN.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='profiles'})
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
old=json.loads((P.parent/'min_degree_seven_clean_star_20261020/FIVE_RESULT.json').read_text());menu=[tuple(x) for x in old['menu']];assert len(menu)==16
z=rows[0];e=SubsetEngine(22,5,z['counts']);e.inv={p:(0,0,[]) for p in e.inv};vals=[];pilotst=time.process_time()
for pos in menu:
 lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for k in range(1,23):bit=lock.get(k,0);U+=e.value(k,left,bit);left|=bit
 vals.append({'positions':pos,'bound':str(Fraction(U,e.D))})
best=min(vals,key=lambda x:Fraction(x['bound']))
pilot={'status':'COMPLETE_ONE_PROFILE_OLD16_AT22','N':22,'free_vertices':17,'source':z,'menu_count':16,'zero_quota':True,'best':best,'all_fixed':vals,'cpu_seconds':time.process_time()-pilotst}
(P/'PILOT_RESULT.json').write_text(json.dumps(pilot,indent=2)+'\n');print('PILOT',best,pilot['cpu_seconds'])
