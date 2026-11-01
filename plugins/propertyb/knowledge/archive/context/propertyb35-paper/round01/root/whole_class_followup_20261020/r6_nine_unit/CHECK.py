"""Complete374-family (six low + three seven) nine-unit domain, low trace <=2.
Bind/evaluate frozen old q6 affine models; no probability rerun in domain mode.
Profile only three still-nonstrict colored orbits using existing exact DP.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5]
S=ROOT/'context/propertyb34/round01/high-math';OLD=ROOT/'context/propertyb35-paper/round01/twentyfive'
sys.dont_write_bytecode=True;sys.path.insert(0,str(S))
from unit_catalogue import fullblocks,canonical
start=time.process_time()
src=json.loads((S/'UNIT_CATALOGUE_9.json').read_text());assert src['complete'] and len(src['orbits'])==374 and src['parents_processed']==65
old=json.loads((OLD/'UNIT9_MIXED_AFFINE.json').read_text());assert old['complete'] and old['catalogue_families']==374
oldfamilies={z['base']:z for z in old['families']}
rows=[];groups={};filters={'candidate_markings':374*84,'excluded_low_intersection':0,'excluded_negative_multiplicity':0}
for base,big in enumerate(src['orbits']):
 bs=fullblocks(big,9);h=[7-sum(bool(t&(1<<i)) for t in bs) for i in range(9)]
 for low in combinations(range(9),6):
  mask=sum(1<<i for i in low)
  if any((t&mask).bit_count()>2 for t in bs):filters['excluded_low_intersection']+=1;continue
  singles=[a-int(i in low) for i,a in enumerate(h)];empty=41-len(bs)-sum(h)
  if min(singles+[empty])<0:filters['excluded_negative_multiplicity']+=1;continue
  ns={t:1 for t in bs};ns.update({1<<i:a for i,a in enumerate(singles) if a})
  if empty:ns[0]=empty
  assert sum(ns.values())==35
  assert all(sum(n for t,n in ns.items() if t&(1<<i))==7-int(i in low) for i in range(9))
  assert all(sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))==1 for i,j in combinations(range(9),2))
  assert all((t&mask).bit_count()<=2 for t in ns)
  f=oldfamilies[base];assert f['feasible']
  c=next(z for z in f['cases'] if z['q']==6)
  oldns={t:1 for t in f['full']};oldns.update({1<<i:a-int(i in low) for i,a in enumerate(f['single_high']) if a-int(i in low)})
  if c['empty']:oldns[0]=c['empty']
  assert ns==oldns
  values=[Fraction(a)+sum(Fraction(lay['slopes'][i]) for i in low) for a,lay in zip(c['layout_constants'],f['layouts'])]
  value=min(values);j=values.index(value);pos=f['layouts'][j]['positions']
  key,m=canonical(big,9,extra=[int(i in low) for i in range(9)],with_perm=True)
  colored=(key,sum(1<<m[i] for i in low))
  z={'base':base,'low':list(low),'low_mask':mask,'counts':ns,'empty':empty,'canonical_large':key,'canonical_lowmask':colored[1],
     'old_to_canonical':m,'old_17_layout_bound':value,'old_positions':pos,'all_counts_match_old_q6_model':True}
  groups.setdefault(colored,[]).append(len(rows));rows.append(z)
assert len(rows)==140 and len(groups)==105
filters['feasible_markings']=len(rows);filters['feasible_families']=len({z['base'] for z in rows});filters['colored_orbits']=len(groups)
def convert(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,dict):return {str(k):convert(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [convert(v) for v in x]
 return x
summary={**filters,'strict_old_labels':sum(z['old_17_layout_bound']<1 for z in rows),'residual_old_labels':sum(z['old_17_layout_bound']>=1 for z in rows),
         'strict_old_orbits':sum(all(rows[j]['old_17_layout_bound']<1 for j in ids) for ids in groups.values()),
         'old_maximum':max(z['old_17_layout_bound'] for z in rows),'domain_and_old_affine_cpu_seconds':time.process_time()-start}
(P/'DOMAIN.json').write_text(json.dumps(convert({'complete_domain':True,'source_families':374,'source_metadata':{k:v for k,v in src.items() if k!='orbits'},'summary':summary,'records':rows}),indent=2)+'\n')
print(json.dumps(convert(summary),indent=2),flush=True)
if 'profile' not in sys.argv:raise SystemExit
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
profile=[]
for key,ids in groups.items():
 if all(rows[j]['old_17_layout_bound']<1 for j in ids):continue
 z=rows[ids[0]];tm=time.process_time();eng=SubsetEngine(25,9,z['counts']);w=eng.verify(eng.solve())
 raw=BareLayout(25,w['positions']).bound(z['counts'])
 rec={'base':z['base'],'low':z['low'],'colored_orbit_labels':[rows[j]['low'] for j in ids],
      'old_bound':z['old_17_layout_bound'],'dp_cpu_seconds':time.process_time()-tm,'raw_witness_bound':raw,**w}
 profile.append(rec);print('profile',len(profile),z['base'],z['low'],'corrected',w['bound'],'raw',raw,'CPU',rec['dp_cpu_seconds'],flush=True)
 if len(profile)>=3:break
out={'scope':'Only first three old-nonstrict colored-orbit exact DP pilots; not full105 DP or full r6 closure.',
     'domain_summary':summary,'profile_cases':len(profile),'strict':sum(z['bound']<1 for z in profile),
     'profile_cpu_seconds':sum(z['dp_cpu_seconds'] for z in profile),'records':profile}
(P/'PROFILE.json').write_text(json.dumps(convert(out),indent=2)+'\n')
