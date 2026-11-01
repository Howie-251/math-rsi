"""Complete 65-family low<=2 filter. Reuse all prior r3 witnesses; no DP.
For r4..6 evaluate the frozen old THREE_SCREEN menu and inherited q2 layouts
on true new counts with original BareLayout raw ABC; no new layout search.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from math import comb
import sys,json,time
P=Path(__file__).resolve().parent
ROOT=P.parents[5]
S=ROOT/'context/propertyb34/round01/high-math'
OLD=ROOT/'context/propertyb35-paper/round01/twentyfive'
sys.dont_write_bytecode=True
sys.path.insert(0,str(S))
from unit_catalogue import fullblocks,canonical
from bare_layout import BareLayout
started=time.process_time()
src=json.loads((S/'UNIT_CATALOGUE_8.json').read_text())
assert src['complete'] and len(src['orbits'])==65
screen3=json.loads((OLD/'MIXED_THREE_SIX_UNIT8_SCREEN.json').read_text())
pilot3=json.loads((OLD/'MIXED_THREE_SIX_UNIT8_PILOT.json').read_text())
pilot2=json.loads((OLD/'MIXED_TWO_SIX_UNIT8_PILOT.json').read_text())
cert2=json.loads((OLD/'MIXED_TWO_SIX_UNIT8_CERTIFICATE.json').read_text())
menu=list(dict.fromkeys([tuple(range(a,a+8)) for a in range(1,19)]+
                        [tuple(z['positions']) for z in pilot2['results']]))
assert len(menu)==46

def jsonable(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,dict):return {str(k):jsonable(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [jsonable(v) for v in x]
 return x

def colored(big,low):
 k,m=canonical(big,8,extra=[int(i in low) for i in range(8)],with_perm=True)
 return (k,sum(1<<m[i] for i in low)),m

def canonical_positions(pos,m):
 cp=[0]*8
 for i,j in enumerate(m):cp[j]=pos[i]
 return tuple(cp)

# Only old complete two-low certificate tuples, transported as in THREE_SCREEN.
q2cache={}
for z in cert2['results']:
 big=[int(t) for t in z['counts'] if int(t).bit_count()>=3]
 key,m=colored(big,z['low'])
 q2cache.setdefault(key,set()).add(canonical_positions(z['positions'],m))
# Prior r3 DP output is imported as concrete witness, never rerun.
p3cache={}
for z in pilot3['results']:
 big=[int(t) for t in z['counts'] if int(t).bit_count()>=3]
 key,m=colored(big,z['low'])
 p3cache[key]=(canonical_positions(z['positions'],m),Fraction(z['raw_ABC_bound']),z)
s3lookup={(z['base'],tuple(z['low'])):z for z in screen3['results']}

records={r:[] for r in (3,4,5,6)}
groups={r:{} for r in (4,5,6)}
filters={}
for r in records:
 stat={'candidate_markings':65*comb(8,r),'excluded_low_intersection':0,'excluded_nonnegative_counts':0}
 for base,big in enumerate(src['orbits']):
  bs=fullblocks(big,8)
  h=[7-sum(bool(t&(1<<i)) for t in bs) for i in range(8)]
  for low in combinations(range(8),r):
   lm=sum(1<<i for i in low)
   if any((t&lm).bit_count()>2 for t in bs):stat['excluded_low_intersection']+=1;continue
   ss=[x-int(i in low) for i,x in enumerate(h)]
   empty=35+r-len(bs)-sum(h)
   if min(ss+[empty])<0:stat['excluded_nonnegative_counts']+=1;continue
   ns={t:1 for t in bs};ns.update({1<<i:n for i,n in enumerate(ss) if n})
   if empty:ns[0]=empty
   assert sum(ns.values())==35
   assert all(sum(n for t,n in ns.items() if t&(1<<i))==7-int(i in low) for i in range(8))
   assert all(sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))==1 for i,j in combinations(range(8),2))
   assert all((t&lm).bit_count()<=2 for t in ns)
   z={'base':base,'low':list(low),'counts':ns,'old_empty':empty-r,'empty':empty}
   key,m=colored(big,low)
   z['canonical_large']=key[0];z['canonical_lowmask']=key[1];z['old_to_canonical']=m
   if r==3:
    old=s3lookup[(base,low)]
    assert ns=={int(t):n for t,n in old['counts'].items() if n}
    v=Fraction(old['raw_ABC_bound']);pos=old['positions'];source='existing_r3_SCREEN_fixed_witness'
    status='strict' if v<1 else 'old_DP_unprocessed'
    if v>=1 and key in p3cache:
     cp,pv,pz=p3cache[key]
     if pv<v:pos=[cp[m[i]] for i in range(8)];v=pv
     source='existing_r3_PILOT_concrete_witness'
     status='strict' if v<1 else 'completed_DP_nonstrict_import'
     z['old_DP_representative']={'base':pz['base'],'low':pz['low'],'reported_optimum':pz['bound']}
    z.update(positions=pos,raw_ABC_bound=v,status=status,witness_source=source)
   else:
    groups[r].setdefault(key,[]).append(len(records[r]))
   records[r].append(z)
 stat['feasible_markings']=len(records[r]);stat['feasible_families']=len({z['base'] for z in records[r]})
 assert sum(stat[k] for k in ['excluded_low_intersection','excluded_nonnegative_counts','feasible_markings'])==stat['candidate_markings']
 filters[r]=stat

profile='profile' in sys.argv
engines={}
checked=[]
for r in (4,5,6):
 for no,(key,ids) in enumerate(groups[r].items()):
  if profile and no>=5:break
  z=records[r][ids[0]];ns=z['counts'];big=src['orbits'][z['base']]
  positions=list(menu)
  for L in combinations(z['low'],2):
   qkey,m=colored(big,L)
   assert qkey in q2cache
   for cp in sorted(q2cache[qkey]):positions.append(tuple(cp[m[i]] for i in range(8)))
  positions=list(dict.fromkeys(positions))
  best=None;bestpos=None
  for pos in positions:
   eng=engines.setdefault(pos,BareLayout(25,pos))
   value=eng.bound(ns)
   if best is None or value<best:best=value;bestpos=pos
  cp=canonical_positions(bestpos,z['old_to_canonical'])
  for j in ids:
   zz=records[r][j];zz.update(positions=[cp[zz['old_to_canonical'][i]] for i in range(8)],raw_ABC_bound=best,status='strict' if best<1 else 'fixed_menu_nonstrict',witness_source='old_THREE_SCREEN_menu_and_old_q2_transports',menu_size=len(positions))
  checked.append({'r':r,'base':z['base'],'low':z['low'],'orbit_size':len(ids),'menu_size':len(positions),'raw_ABC_bound':best,'positions':bestpos})

summary={}
for r,zs in records.items():
 done=[z for z in zs if 'raw_ABC_bound'in z]
 summary[r]={**filters[r],'colored_orbits':len({(tuple(z['canonical_large']),z['canonical_lowmask']) for z in zs}),
             'witnesses_available':len(done),'strict':sum(z['raw_ABC_bound']<1 for z in done),
             'nonstrict_witness':sum(z['raw_ABC_bound']>=1 for z in done),
             'maximum_available_raw_bound':max((z['raw_ABC_bound'] for z in done),default=None)}
 if r==3:
  summary[r]['completed_DP_nonstrict_labels']=sum(z['status']=='completed_DP_nonstrict_import' for z in zs)
  summary[r]['old_DP_unprocessed_labels']=sum(z['status']=='old_DP_unprocessed' for z in zs)
output={'complete':not profile,'mode':'profile_first_5_colored_orbits_per_new_r' if profile else 'full',
        'imports':['complete65-unit8-catalogue','original BareLayout integer raw ABC implementation','old r2 concrete fixed-layout certificates','old r3 SCREEN/PILOT concrete witnesses, not their optimum proof'],
        'fixed_menu_size':len(menu),'summary':summary,'new_checked_orbits':checked,
        'cpu_seconds':time.process_time()-started,
        'r3_raw_not_recomputed':True,'new_DP_or_layout_search':False}
if not profile:
 output['records']=records
 output['remaining']={r:[z for z in zs if z['raw_ABC_bound']>=1] for r,zs in records.items()}
 for r in records:assert summary[r]['witnesses_available']==len(records[r])
name='PROFILE.json' if profile else 'RESULT.json'
(P/name).write_text(json.dumps(jsonable(output),indent=2)+'\n')
print(json.dumps(jsonable({k:output[k] for k in ['complete','mode','summary','cpu_seconds']}),indent=2))
