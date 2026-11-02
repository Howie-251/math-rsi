"""Read existing CSR once; no raw parse, radius balls, BFS or candidates."""
from array import array
from collections import Counter
from pathlib import Path
import json
import time

START=time.process_time()
OUT=Path(__file__).resolve().parent
data=array('I')
data.frombytes((OUT/'adjacency.csr.u32le.bin').read_bytes())
n,twom=data[0],data[1]
assert (n,twom)==(186033,2021634)
offsets=memoryview(data)[2:2+n+1]
neighbors=memoryview(data)[2+n+1:]
assert len(neighbors)==twom and offsets[-1]==twom
degree=(OUT/'degrees.u8.bin').read_bytes()
assert len(degree)==n

def N(u):
    return set(neighbors[offsets[u]:offsets[u+1]])

prototype=19161
deleted=78477
mandatory=[72425,85923,89934,95946,103392,107088,113094,120546,127006]
assert N(prototype)==set(mandatory+[deleted])
D=N(deleted)
assert len(D)==11
shared_count=Counter()
for u in D:
    for w in neighbors[offsets[u]:offsets[u+1]]:
        if degree[w]<11:
            shared_count[w]+=1
eligible=[w for w,d in enumerate(degree) if d<11 and w not in mandatory]
ranked=sorted(eligible,key=lambda w:(len(D)+degree[w]-2*shared_count[w],-shared_count[w],w))
most_shared=sorted(eligible,key=lambda w:(-shared_count[w],len(D)+degree[w]-2*shared_count[w],w))

def record(w):
    W=N(w)
    shared=sorted(D&W)
    return {'vertex':w,'degree':degree[w],'free_slots':11-degree[w],
            'shared_neighbors':shared,'shared_count':len(shared),
            'deleted_pin_private_neighbors':sorted(D-W),
            'guard_private_neighbors':sorted(W-D),
            'symmetric_difference_size':len(D^W),
            'neighbors':sorted(W),
            'shared_in_old182618_numeric_prefix':[u for u in shared if u<182618],
            'shared_in_later_numeric_suffix':[u for u in shared if u>=182618]}

result={'status':'COMPLETE_CSR_OPEN_NEIGHBORHOOD_PROXY_PROFILE_NO_BFS',
        'source_n':n,'source_m':twom//2,'source_CSR':str(OUT/'adjacency.csr.u32le.bin'),
        'prototype':prototype,'prototype_degree':degree[prototype],
        'deleted_saturated_pin':deleted,'deleted_pin_degree':degree[deleted],
        'deleted_pin_neighbors':sorted(D),'mandatory_free_pins':mandatory,
        'source_partition_caution':'SOURCE_PROFILE only labels old182618. It is not established as a geometric core; numeric-prefix/suffix classifications below make no geometric claim.',
        'eligible_guards_excluding_mandatory':len(eligible),
        'free_guard_shared_neighbor_histogram':dict(Counter(shared_count[w] for w in eligible)),
        'max_shared_neighbors':max(shared_count[w] for w in eligible),
        'minimum_open_neighborhood_symmetric_difference':len(D)+degree[ranked[0]]-2*shared_count[ranked[0]],
        'top_by_exact_symmetric_difference':[record(w) for w in ranked[:10]],
        'top_by_shared_neighbor_count':[record(w) for w in most_shared[:10]],
        'complete_full_neighborhood_free_proxy_exists':any(degree[w]==len(D) and shared_count[w]==len(D) for w in eligible),
        'enumeration_completeness':'Inverse index union over N(deleted) gives every positive-overlap free vertex exactly; all eligible zero-overlap vertices also ranked by their true degree, so symmetric-difference minimum is global.',
        'candidate_generation':0,'raw_source_parses':0,'BFS':0,'radius_balls':0,
        'CPU_seconds':time.process_time()-START,'pending':[]}
(OUT/'FREE_PIN_PROXY_ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if not k.startswith('top_')},indent=2))
print('TOP',json.dumps(result['top_by_exact_symmetric_difference'][:3]))
