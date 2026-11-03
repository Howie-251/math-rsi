"""Exact3276triple stage; consumesactualportballs withoutBFS."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import time

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parent/'source_and_single'
start=time.process_time()
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_computation']
balls=load(SOURCE/'PORT_BALLS.json');cells=load(SOURCE/'PORT_CLASSES.json')
assert (balls['source_n'],balls['source_m'])==(364,714)
ports=balls['ports'];assert len(ports)==28 and balls['rows_port_order']==ports
assert cells['R2_classes_partition_all364'] and cells['R2_class_sizes']==[13]*28
r4=[sum(int(x)<<(64*w) for w,x in enumerate(row)) for row in balls['R4_words_u64']]
interiors=[]
for p,cell in zip(ports,cells['R2_class_members']):
    assert p in cell
    interiors.append(sum(1<<v for v in cell if v!=p))
records=[];hist=Counter();maximum=-1;maxima=[]
for indices in combinations(range(28),3):
    mask=r4[indices[0]]|r4[indices[1]]|r4[indices[2]]
    good=[j for j in range(28) if j not in indices and interiors[j]&~mask==0]
    row=dict(triple=[ports[j] for j in indices],port_indices=list(indices),
        good_ports=[ports[j] for j in good],good_count=len(good),
        good_port_index_mask=sum(1<<j for j in good))
    records.append(row);hist[len(good)]+=1
    if len(good)>maximum:maximum=len(good);maxima=[row]
    elif len(good)==maximum:maxima.append(row)
assert len(records)==3276
status='UNIFORM_TOPOLOGY_OBSTRUCTION_MAX_GOOD_BELOW18' if maximum<18 else 'CAPACITY_PASSES_ASSIGNMENT_SEARCH_REQUIRED'
result=dict(status=status,source_n=364,source_m=714,ports=ports,triples_enumerated=3276,
    good_count_histogram=dict(sorted(hist.items())),maximum_good_count=maximum,
    necessary_good_count=18,maximum_attaining_triples=len(maxima),first_maximum_witness=maxima[0],
    prediction_supported=False if maximum<18 else None,
    max_good_stage_complete=True,assignment_search_run=False,graph_generated=False,
    hypothetical_n=377,actual_n=None,actual_D=None,
    scope='Fixed13-helper center+3branches+9leaves tree only;all28portsusedonce',
    all13_tree_shapes_excluded=False,source_BFS=0,portballs_recomputed=0,
    CPU_seconds=time.process_time()-start,
    evidence=['PREDICTION.json','capacity.py','triple_good_sets.json',
              '../source_and_single/PORT_BALLS.json','../source_and_single/PORT_CLASSES.json'],
    pending=[] if maximum<18 else ['Boundedfiniteassignmentsearchwithremaining30CPUbudget'])
(OUT/'triple_good_sets.json').write_text(json.dumps(records,indent=2)+'\n')
(OUT/'CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
if maximum<18:
    (OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
