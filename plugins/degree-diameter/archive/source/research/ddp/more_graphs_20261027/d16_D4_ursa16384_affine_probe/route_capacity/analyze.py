"""Exact small word-relation inventory; read cached interface, never source graph."""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json
import resource
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
OUT=Path(__file__).resolve().parent
interface=json.loads((OUT.parent/'INTERFACE.json').read_text())
types=interface['relation_types']
assert len(types)==4 and all(t['constant']==0 for t in types)
INV=[3,2,1,0]
# Reuse exactly the field encoding and multiplication tables of ../probe.py,
# without importing its source-parser side effects.
mul2=[sum(([0,2,3,1][x//4**j%4])*4**j for j in range(4)) for x in range(256)]
mul=[[0]*256,list(range(256)),mul2,[x^mul2[x] for x in range(256)]]
field_inv=[0,1,3,2]

def apply(columns,x):
    y=0
    for j,col in enumerate(columns):
        y^=mul[x//4**j%4][col]
    return y

def basis(vectors):
    rows=[]
    for x in vectors:
        for pivot,row in rows:
            x^=mul[x//4**pivot%4][row]
        if not x:
            continue
        p=next(j for j in range(4) if x//4**j%4)
        x=mul[field_inv[x//4**p%4]][x]
        rows=[(j,row^mul[row//4**p%4][x]) for j,row in rows]
        rows.append((p,x));rows.sort()
    return [row for _,row in rows]

def span(rows):
    values={0}
    for row in rows:
        values={v^mul[s][row] for v in values for s in range(4)}
    return values

def reduce(word):
    stack=[]
    for s in word:
        if stack and INV[s]==stack[-1]:stack.pop()
        else:stack.append(s)
    return tuple(stack)

def dot(x,y):
    z=0
    for j in range(4):
        z^=mul[x//4**j%4][y//4**j%4]
    return z

directions=[]
for t in types:
    d=next(v for v in t['D'] if v)
    assert span([d])==set(t['D'])
    directions.append(d)
states={():([1,4,16,64],[])}
images={():{0}}
words=[()]+[w for k in range(1,5) for w in product(range(4),repeat=k)]
records=[]
for word in words:
    if word:
        Mprev,Bprev=states[word[:-1]]
        t=types[word[-1]]
        M=t['canonical_columns']
        states[word]=([apply(M,col) for col in Mprev],
                      basis([apply(M,row) for row in Bprev]+[directions[word[-1]]]))
        images[word]=span(states[word][1])
    M,B=states[word]
    r=len(B)
    assert len(images[word])==4**r
    normals=basis([v for v in range(1,256) if all(dot(v,b)==0 for b in B)])
    assert len(normals)==4-r
    records.append({'word_types':list(word),'word':''.join(map(str,word)),
                    'length':len(word),'reduced_word_types':list(reduce(word)),
                    'is_reduced':reduce(word)==word,'rank':r,'image_size':len(images[word]),
                    'image_basis':B,'missing_direction_normals_basis':normals,
                    'linear_columns':M,'linear_rank':len(basis(M))})
assert len(words)==341

groups=defaultdict(set)
multiplicity=Counter()
for word in words:
    groups[reduce(word)].update(images[word]);multiplicity[reduce(word)]+=1
classes=[{'reduced_word_types':list(w),'word':''.join(map(str,w)),
          'route_word_count':multiplicity[w],'zero_source_union_size':len(points),
          'zero_source_union_fibers':sorted(points)} for w,points in sorted(groups.items(),key=lambda kv:(len(kv[0]),kv[0]))]
raw_capacity=sum(len(images[w]) for w in words)
class_capacity=sum(len(s) for s in groups.values())
zero_overlap_capacity=sum(len(s)-1 for s in groups.values())
by_length={str(k):{'all_words':sum(r['length']==k for r in records),
                  'all_rank_histogram':dict(Counter(r['rank'] for r in records if r['length']==k)),
                  'reduced_words':sum(r['length']==k and r['is_reduced'] for r in records),
                  'reduced_rank_histogram':dict(Counter(r['rank'] for r in records if r['length']==k and r['is_reduced']))}
           for k in range(5)}
summary={'status':'COMPLETE_EXACT_WORD_RELATION_CAPACITY','source_interface':str(OUT.parent/'INTERFACE.json'),
         'field_encoding':'F4 0,1,w,w+1;w^2=w+1; byte=x0+4*x1+16*x2+64*x3; addition XOR',
         'inverse_types':INV,'word_count':len(words),'reduced_word_count':sum(r['is_reduced'] for r in records),
         'rank_by_length':by_length,'canonical_M_ranks':[len(basis(t['canonical_columns'])) for t in types],
         'all_route_cardinality_sum':raw_capacity,'raw_controller_order_upper_bound':raw_capacity//256,
         'free_reduction_class_count':len(groups),'free_class_union_sum':class_capacity,
         'free_class_controller_order_upper_bound':class_capacity//256,
         'free_class_common_zero_adjusted_numerator':zero_overlap_capacity,
         'common_zero_controller_order_upper_bound':zero_overlap_capacity//255,
         'common_zero_bound_proof':'All zero-source route images contain0. Group all words by free reduction because inverse-consistent controller labels give a common endpoint within each class. At each of n covered controller fibers the union has size at most1+sum_class(|classunion|-1), so255*n <= total(|classunion|-1). Necessary only.',
         'reduced4_fullrank_words':[r['word'] for r in records if r['length']==4 and r['is_reduced'] and r['rank']==4],
         'reduced4_deficient_words':[{'word':r['word'],'rank':r['rank'],'image_basis':r['image_basis'],'missing_direction_normals_basis':r['missing_direction_normals_basis']} for r in records if r['length']==4 and r['is_reduced'] and r['rank']<4],
         'capacity_does_not_exclude_controller_gt64':zero_overlap_capacity//255>64,
         'prediction_disposition':'SUPPORTED' if zero_overlap_capacity//255>64 and any(r['length']==4 and r['is_reduced'] and r['rank']<4 for r in records) else 'REFUTED',
         'ordinary_bad_unordered_pairs':None,'actual_candidate_n':None,'actual_candidate_D':None,
         'source_edge_parses':0,'graph_BFS':0,'controller_search':False,'CPU_seconds':time.process_time()-START,
         'running':False,'pending':[]}
(OUT/'WORD_IMAGES.json').write_text(json.dumps({'inverse_types':INV,'source_fiber':0,'records':[{**r,'fibers':sorted(images[tuple(r['word_types'])])} for r in records]},indent=2)+'\n')
(OUT/'FREE_REDUCTION_CLASSES.json').write_text(json.dumps(classes,indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['reduced4_fullrank_words','reduced4_deficient_words']},indent=2))
