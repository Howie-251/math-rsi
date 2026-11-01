"""Bounded four-lock local probe; this is not a k13 full certificate."""
import json,time,itertools
from pathlib import Path
from layout_certified import LayoutCertificate,S
OUT=Path(__file__).resolve().parent
m=9564;v=972;k=13;positions=(v//2-1,v//2,v//2+1,v//2+2)
cal=LayoutCertificate(k,m,positions);start=time.process_time();wall=time.monotonic()
pairs=tuple(itertools.combinations(range(4),2))
patterns=[('six_pairs',pairs)]
for omit in range(4):
 tri=tuple(i for i in range(4) if i!=omit)
 patterns.append((f'triple_omit_{omit}',(tri,)+tuple((i,omit) for i in tri)))
patterns.append(('quadruple',(tuple(range(4)),)))
def counts(degrees,blocks):
 cnt=[0]*16
 for block in blocks:cnt[sum(1<<i for i in block)]+=1
 for i,d in enumerate(degrees):cnt[1<<i]=d-sum(i in b for b in blocks)
 cnt[0]=m-sum(cnt)
 assert min(cnt)>=0 and sum(cnt)==m
 assert all(sum(cnt[t] for t in range(16) if t&(1<<i))==degrees[i] for i in range(4))
 assert all(sum(cnt[t] for t in range(16) if t&(1<<i) and t&(1<<j))==1 for i,j in pairs)
 return cnt
# A permutation moves vertex i, its actual degree, and its trace incidences together.
def relabel(degrees,blocks,perm):
 ds=[0]*4
 for i,d in enumerate(degrees):ds[perm[i]]=d
 bs=[tuple(perm[i] for i in b) for b in blocks]
 return counts(ds,bs)
cache={};rows=[];failure=None;completed_f=[]
for f in range(81,129):
 degrees=(81,81,81,f);frows=[]
 for name,blocks in patterns:
  candidates={}
  for perm in itertools.permutations(range(4)):
   cnt=tuple(relabel(degrees,blocks,perm));candidates.setdefault(cnt,perm)
  tested=[];all_done=True
  for cnt,perm in candidates.items():
   if time.process_time()-start>42:all_done=False;break
   if cnt not in cache:cache[cnt]=cal.bound(v,list(cnt))
   z=cache[cnt];tested.append({'permutation':perm,'counts':cnt,'z':z,'margin':S-z})
  if not all_done:
   failure={'reason':'cpu_budget','f':f,'pattern':name};break
  best=min(tested,key=lambda r:r['z'])
  row={'f':f,'degrees':degrees,'pattern':name,'blocks':blocks,'distinct_relabelled_counts':len(candidates),'best':best,'all_layouts':tested,'all_relabellings_checked':True}
  frows.append(row);print('ROW',f,name,'best',best['z'],'margin',best['margin'],'distinct',len(candidates),'cpu',round(time.process_time()-start,3),flush=True)
  if best['z']>=S:
   failure={'reason':'fixed_position_certificate_failed_after_all_degree_trace_relabellings','f':f,'pattern':name,'best_z':best['z'],'margin':S-best['z']};break
 rows.extend(frows)
 if failure:break
 completed_f.append(f)
res={'k':k,'M':m,'v':v,'S':S,'positions':positions,'requested_f_range':[81,128],'completed_f':completed_f,'rows':rows,'failure':failure,'distinct_count_vectors_evaluated':len(cache),'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'full_k13_certificate':False,'arithmetic':'Python unbounded integers; original conditional probability formulas and outward rounding'}
(OUT/'FOUR_LOCK_PROBE.json').write_text(json.dumps(res,indent=2));print('DONE',failure,'cpu',res['cpu_seconds'],flush=True)
