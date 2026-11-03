"""Exact endpoint images for six embeddings at one fixed prime. No graph."""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
out=Path(__file__).resolve().parent
base=out.parents[1]
raw=json.loads((out.parent/'endpoint_polynomials/POLYNOMIAL_SETS.json').read_text())
sets={(r['root_base'],r['target_base'],r['phase']):r['polynomials'] for r in raw}
root4=json.loads((base/'root0_missing_by_slot.json').read_text())
assert root4['root_base']==0 and root4['radius']==9
roots=[r for r in range(1,109) if pow(r,18,109)==1 and all(pow(r,d,109)!=1 for d in [1,2,3,6,9])]
assert len(roots)==6 and 4 in roots
def image(polys,p,r):
    powers=[pow(r,j,p) for j in range(6)]
    return {sum(a*b for a,b in zip(poly,powers))%p for poly in polys}

records=[]
survivors=[]
for r in roots:
    if r==4:
        slots=[{'root_base':0,'target_base':x['end_base'],'phase':x['phase'],
                'actual_image_count':109-len(x['missing_field_elements']),
                'missing_field_elements':x['missing_field_elements']} for x in root4['slots']]
        assert sum(len(x['missing_field_elements']) for x in slots)==347
        records.append({'r':r,'A':(-r*r-r**3)%109,'B':(-1-r*r)%109,
                        'root4_actual_producer_reused':True,'base_roots_checked':[0],
                        'complete_D9_word_certificate':False,'root0_missing_total':347,'slots':slots})
        continue
    slots=[]
    checked=[]
    full=True
    for source in range(3):
        base_full=True
        for target in range(3):
            for j in range(36):
                points=image(sets[source,target,j],109,r)
                missing=sorted(set(range(109))-points)
                slots.append({'root_base':source,'target_base':target,'phase':j,
                              'actual_image_count':len(points),'missing_field_elements':missing})
                base_full &= not missing
        checked.append(source)
        if not base_full:
            full=False
            break
    if full:survivors.append({'N':109,'M':36,'r':r,'A':(-r*r-r**3)%109,'B':(-1-r*r)%109})
    records.append({'r':r,'A':(-r*r-r**3)%109,'B':(-1-r*r)%109,
                    'root4_actual_producer_reused':False,'base_roots_checked':checked,
                    'complete_D9_word_certificate':full,
                    'root0_missing_total':sum(len(x['missing_field_elements']) for x in slots if x['root_base']==0),
                    'slots':slots})

polys=sets[0,0,5]
buckets=defaultdict(list)
powers=[pow(4,j,109) for j in range(6)]
for p in polys:buckets[sum(a*b for a,b in zip(p,powers))%109].append(p)
best=None
for value,bucket in buckets.items():
    for a,b in combinations(bucket,2):
        diff=tuple(x-y for x,y in zip(a,b))
        degree=max(i for i,x in enumerate(diff) if x)
        key=(sum(map(abs,diff)),degree,diff)
        if best is None or key<best[0]:best=(key,{'field_value':value,'polynomial1':a,'polynomial2':b,'difference':diff,'difference_L1':key[0],'difference_degree':degree})
assert best is not None
missing=sorted(set(range(109))-set(buckets))
assert missing==[9,10,33,75,83,88,97]
control=image(polys,73,18)
thin={'root_base':0,'target_base':0,'phase':5,
      'formal_distinct_polynomials':len(polys),
      'actual_field':{'p':109,'r':4,'image_count':len(buckets),'missing':missing,
                      'formal_preimage_multiplicity_histogram':dict(Counter(map(len,buckets.values())))},
      'published_source_arithmetic_control_only':{'p':73,'r':18,'image_count':len(control),'missing':sorted(set(range(73))-control)},
      'smallest_L1_formal_kernel_pair_in_this_slot':best[1],
      'scope':'This checks just one publishedsource slot viacachedpolynomials, notitsgraph/BFS. Differentformal6tuples cancoincide in achosenfield.'}
result={'status':'COMPLETE_SIX_PRIMITIVE18_EMBEDDINGS',
        'prediction_disposition':'SUPPORTED' if not survivors else 'REFUTED',
        'p':109,'roots':roots,'embeddings_count':6,'complete_survivors':survivors,
        'embedding_summaries':[{k:v for k,v in r.items() if k!='slots'} for r in records],
        'all_embeddings_refuted_at_rootbase0':all(not r['complete_D9_word_certificate'] and r['base_roots_checked']==[0] for r in records),
        'certificate_scope':'EveryNBnamededgeword oflength<=9 is included. Immediatebacktrackreduction preserves endpoint, so these exactfieldimage sets equal the graphR9 foridentityroot at eachbase; enoughphase/formalcapacity alone is notthiscertificate.',
        'ordinary_bad_unordered_pairs':None,'actual_global_D':None,
        'CPU_seconds':time.process_time()-start,'new_graphs':0,'BFS':0,'other_primes_tested':0,
        'running':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'EMBEDDINGS.json').write_text(json.dumps(records,indent=2)+'\n')
(out/'THIN_PHASE5.json').write_text(json.dumps(thin,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('THIN',json.dumps(thin,indent=2))
