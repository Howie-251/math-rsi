import sys,json,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from scan import CEIL,C
OUT=Path(__file__).resolve().parent
allrows=[]
for m in (4647,4660):
 p=OUT/f'M{m}.json';x=json.loads(p.read_text())
 for r in x['rows']:
  v=r['v'];d0=CEIL(v-1,11);hi=12*m//v;r['d0']=d0;r['minimum_degree_upper']=hi
  if r['mode']=='one':r['degree_range']=[d0,hi]
  if r['mode']=='two':
   r['degree_ranges']=[{'d':d,'s_d':2*(v-1)-11*d,'e_min':d,'e_max':max(d,(12*m-v*d)//(2*(v-1)-11*d)+d)} for d in range(d0,hi+1)]
   assert sum(a['e_max']-a['e_min']+1 for a in r['degree_ranges'])==r['profiles']
  if r['mode']=='three':
   r['degree_range']=[d0,r['D']];r['types']=['separate','triple'];r['Z']=(r['D']+1)*v-12*m;r['existence_strict_difference']=22*r['Z']-(11*(r['D']+1)-v+2)**2
   n=r['D']-d0+1;assert r['profiles']==2*C(n+2,3) and r['existence_strict_difference']>0
 x['below_domain']={'v_min':23,'v_max':x['candidate_v'][0]-1,'all_balanced_strict':all(m*(C(v//2,12)+C(v-v//2,12))<C(v,12) for v in range(23,x['candidate_v'][0]))}
 x['above_domain']={'first_v':x['candidate_v'][-1]+1,'v_times_d0':(x['candidate_v'][-1]+1)*CEIL(x['candidate_v'][-1],11),'degree_budget':12*m}
 assert x['above_domain']['v_times_d0']>12*m
 phases=[]
 for mode,g in itertools.groupby(x['rows'],key=lambda r:r['mode']):
  rs=list(g);w=max(rs,key=lambda r:r['worst_z']);phases.append({'mode':mode,'v_min':rs[0]['v'],'v_max':rs[-1]['v'],'v_count':len(rs),'profiles':sum(r['profiles'] for r in rs),'worst':w})
 x['phase_summary']=phases;x['total_profiles']=sum(r['profiles'] for r in x['rows']);p.write_text(json.dumps(x,indent=2));allrows.append({'M':m,'conclusion_m12_ge':m+1,'complete':x['complete'],'total_profiles':x['total_profiles'],'wall_seconds':x['wall_seconds'],'maxrss_bytes':x['maxrss_bytes'],'phases':phases})
(OUT/'SUMMARY.json').write_text(json.dumps(allrows,indent=2))
