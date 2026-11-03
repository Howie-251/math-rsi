"""Exact81900cachedmask pairs; no graph/BFS/assignment search."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import time
import resource

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parent/'source_and_single'
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
load=lambda p:json.loads(p.read_text())
assert load(OUT/'STAGE2_PREDICTION.json')['frozen_before_computation']
assert load(OUT/'CAPACITY.json')['maximum_good_count']==0
balls=load(SOURCE/'PORT_BALLS.json');classes=load(SOURCE/'PORT_CLASSES.json')
ports=balls['ports'];assert len(ports)==28
assert classes['R2_classes_partition_all364'] and classes['R2_class_sizes']==[13]*28
r3=[sum(int(x)<<(64*w) for w,x in enumerate(row)) for row in balls['R3_words_u64']]
r4=[sum(int(x)<<(64*w) for w,x in enumerate(row)) for row in balls['R4_words_u64']]
interiors=[sum(1<<v for v in cell if v!=p) for p,cell in zip(ports,classes['R2_class_members'])]
hist=Counter();counts=bytearray();maximum=-1;first=None;maxcount=0;profile=None
stop=False
for triple_index,T in enumerate(combinations(range(28),3)):
    union=r4[T[0]]|r4[T[1]]|r4[T[2]]
    for p in range(28):
        if p in T:continue
        if len(counts)%1024==0 and time.process_time()-start>4.4:stop=True;break
        absent=~(union|r3[p])
        good=[q for q in range(28) if q not in T and q!=p and interiors[q]&absent==0]
        count=len(good);counts.append(count);hist[count]+=1
        if count>maximum:
            maximum=count;maxcount=1
            first=dict(triple_index=triple_index,T=[ports[q] for q in T],parent_port=ports[p],
                good_ports=[ports[q] for q in good],good_count=count,mask_pair_ordinal=len(counts))
        elif count==maximum:maxcount+=1
        if len(counts)==1000:
            profile=dict(pairs=1000,CPU_seconds=time.process_time()-start,
                projected_all81900_CPU=(time.process_time()-start)*81.9,maximum_so_far=maximum)
            (OUT/'STAGE2_PROFILE1000.json').write_text(json.dumps(profile,indent=2)+'\n')
    if stop:break
complete=len(counts)==81900
excluded=complete and maximum<18
status=('COMPLETE_FIXED_HOST_K13_EXTENSION_CLASS_EXCLUDED' if excluded else
        'CAPACITY_MAX_AT_LEAST18_RETURN_WITHOUT_ASSIGNMENT' if complete else 'CPU_LIMIT_UNKNOWN')
(OUT/'parent_port_good_counts.u8.bin').write_bytes(counts)
result=dict(status=status,source_n=364,source_m=714,port_count=28,source_balls_reused=True,
    triples=3276,parent_choices_per_triple=25,scope_mask_pairs=81900,mask_pairs_evaluated=len(counts),
    complete_pair_scope=complete,good_count_histogram=dict(sorted(hist.items())),
    maximum_good_count=maximum,necessary_foreign_leaf_cells=18,first_maximum_witness=first,
    maximum_attaining_pairs=maxcount,stage1_maximum_good_count=0,
    stage2_prediction_supported=excluded if complete else None,
    original_existence_prediction_supported=False if excluded else None,
    prediction_file='STAGE2_PREDICTION.json',
    fixed_host_k13_extension_class_excluded=excluded,
    class_scope='Retainallnatural364/714hostedges;noaddedoldoldedges;degreecap4;13newvertices;oldports eachatmostoneedge',
    arbitrary377vertex_graphs_excluded=False,otherhosts_or_rewiring_excluded=False,k14_investigated=False,
    assignment_search_run=False,source_BFS=0,portballs_recomputed=0,graph_generated=False,
    hypothetical_n=377,actual_n=None,actual_D=None,CPU_seconds=time.process_time()-start,
    profile1000=profile,count_binary_layout='81900uint8,lexTthenascendingparentportoutsideT',
    evidence=['STAGE2_PREDICTION.json','parent_port_capacity.py','CAPACITY.json',
        'parent_port_good_counts.u8.bin','../MULTI_VERTEX_PORT_BARRIER.md',
        '../source_and_single/PORT_BALLS.json','../source_and_single/PORT_CLASSES.json'],
    pending=[] if complete else ['Unfinishedfixed81900maskpairremainder'])
(OUT/'PARENT_PORT_CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
