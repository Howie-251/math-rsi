"""Producer preparation: exact final-PASS local registries, no new theorem acceptance."""
from pathlib import Path
from itertools import permutations
import hashlib,json,collections
P=Path(__file__).resolve().parent
def read(name):return json.loads((P/name).read_text(encoding='utf-8'))
def sha(name):return hashlib.sha256((P/name).read_bytes()).hexdigest()
def checked(name):
    j=read(name);assert j['verdict']=='PASS',name;return j
source_gate=checked('HIGHER_Q5_FULL_REVIEW.json')
reuse_gate=checked('HIGHER_Q5_FULL_REUSE_REVIEW.json')
gates=['HIGHER_Q5_FULL_REVIEW.json','HIGHER_Q5_FULL_REUSE_REVIEW.json',
 'HIGHER_FORCED_CHERRY_REVIEW.json','Q5_A10_FULL_REVIEW.json',
 'Q5_T26_RANK_BATCH_REVIEW.json','Q5_T15_RANK_BATCH_REVIEW.json',
 'Q5_T17_RANK_BATCH_REVIEW.json','Q5_T63_RANK_REVIEW.json',
 'Q5_T63_COMPLETE_SPLIT_REVIEW.json','TEN_HOLE_COVERED_PARTIAL_REVIEW.json',
 'T44_Q5_CLOSURE_REVIEW.json','Q5_T37_INDEPENDENT_REVIEW.json',
 'TWELVE_NEW_TYPES_LOCAL_REVIEW.json','TWELVE_EXTRA_TYPES_REVIEW.json',
 'TWELVE_NEW_FORCED_REVIEW.json','TWELVE_EXTRA_FORCED_REVIEW.json','TWELVE_STAR_B_REVIEW.json']
for name in gates:checked(name)
sources={};count=0
for v in (1,7,31):
 for status in ('covered','free'):
    name=f'HIGHER_Q5_FULL_residual_h14_v{v}_{status}.bin';actual=sha(name)
    assert source_gate['audited_input_hashes'][name].removeprefix('sha256:')==actual
    size=(P/name).stat().st_size;assert size%13==0
    sources[name]={'sha256':actual,'bytes':size,'records':size//13};count+=size//13
assert count==9484443
legacy=[]
for typ in ('T26','T15','T17','T63'):
 name=f'HIGHER_Q5_FULL_{typ}_lookup.txt'
 assert reuse_gate['audited_input_hashes'][name].removeprefix('sha256:')==sha(name)
 legacy.append(name)
rows=[]
def add(family,source,entries,forced=False):
 for g in entries:
    rows.append({'family':family,'source_gate':source,'local_id':g['index'],
      'minority':g['minority'],'majority':g['majority'],'omitted':g['omitted'],
      'forced_pair':g['forced_pair'] if forced else []})
add(10,'Q5_T37_INDEPENDENT_REVIEW.json',read('Q5_T37_INDEPENDENT_REVIEW.json')['accepted_marked_inputs'])
add(11,'TWELVE_NEW_TYPES_LOCAL_REVIEW.json',read('TWELVE_NEW_TYPES_LOCAL_REVIEW.json')['accepted_marked_inputs'])
add(12,'TWELVE_EXTRA_TYPES_REVIEW.json',read('TWELVE_EXTRA_TYPES_REVIEW.json')['details']['accepted_marked_local_rows'])
forced_old={5:[1,2,4,7,11,28,31],6:[1,2,4,11,13,22,31],9:[1,2,4,7,11,21,31],11:[1,2,4,11,19,25,26],12:[1,2,4,7,11,13,31],13:[1,2,4,11,13,14,31],17:[1,2,4,7,11,13,14]}
assert read('Q5_T17_RANK_BATCH_REVIEW.json')['details']['forced_local_orbits']==7
add(20,'Q5_T17_RANK_BATCH_REVIEW.json',[{'index':i,'minority':[0],'majority':J,'omitted':[1,2,4],'forced_pair':[8,16]} for i,J in forced_old.items()],True)
add(21,'TWELVE_NEW_FORCED_REVIEW.json',read('TWELVE_NEW_FORCED_REVIEW.json')['details']['accepted_marked_statements'],True)
add(22,'TWELVE_EXTRA_FORCED_REVIEW.json',read('TWELVE_EXTRA_FORCED_REVIEW.json')['details']['accepted_marked_local_rows'],True)
add(23,'TWELVE_STAR_B_REVIEW.json',read('TWELVE_STAR_B_REVIEW.json')['accepted_marked_inputs'],True)
assert len(rows)==55+111+11+7+27+15+10
mask=lambda xs:sum(1<<x for x in xs)
maps=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
lookup={};shapes=set()
for g in rows:
 M,J,U,R=[g[k] for k in ('minority','majority','omitted','forced_pair')]
 assert len(set(M+J))==len(M)+len(J) and set(U)<=set(J) and not set(R)&set(M+J)
 if R:assert len(R)==2 and len(U)>=3 and len({x.bit_count()%2 for x in U+R})==1
 shapes.add((len(M),len(J),len(U)))
 for a in (M or U):
  for tr in maps:
   key=tuple(mask(tr[x^a] for x in xs) for xs in (M,J,U))
   value=(mask(tr[x^a] for x in R),g['family'],g['local_id'])
   if key in lookup:
    assert lookup[key][0]==value[0],('inconsistent unconditional/forced input',key,lookup[key],value)
   else:lookup[key]=value
(P/'FOURTEEN_REUSE_registry.txt').write_text(''.join(' '.join(map(str,[*k,*v]))+'\n' for k,v in sorted(lookup.items())))
catalog={'status':'PRODUCER_PREPARED_PENDING_APPLICATION_REVIEW','holes':14,'input_records':count,
 'source_domain_gate':'HIGHER_Q5_FULL_REVIEW.json','source_reduction_conditional_on_full_twelve_hole':True,
 'sources':sources,'gate_hashes':{n:sha(n) for n in gates},'legacy_lookup_hashes':{n:sha(n) for n in legacy},
 'explicit_local_rows':rows,'explicit_local_family_counts':dict(collections.Counter(x['family'] for x in rows)),
 'normalized_registry_keys':len(lookup),'normalized_forced_keys':sum(bool(v[0]) for v in lookup.values()),
 'shapes':sorted(map(list,shapes)),
 'family_meaning':{'1':'T44 complete','2':'T63 accepted marked split','3':'old55 T26','4':'accepted old/new T15 registry','5':'T15 short augmentation to T44','6':'old10 unforced T17','7':'old7 T63 rank',
 '10':'T37 accepted55','11':'new111 unforced T28/T19/T84/T105','12':'EXTRA_TYPES accepted11','20':'old7 forcedT17','21':'new27 forcedT28/T19','22':'new15 forcedT17','23':'STAR_B10 forcedT17'},
 'registry_sha256':sha('FOURTEEN_REUSE_registry.txt'),'unreviewed_star_A_or_MAmax_used':False,
 'full_twelve_hole_proved':False,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(P/'FOURTEEN_REUSE_catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
print(json.dumps({k:catalog[k] for k in ('input_records','explicit_local_family_counts','normalized_registry_keys','normalized_forced_keys','shapes')},indent=2))
