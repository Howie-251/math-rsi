"""Cheap actual-cache necessary obstruction; no ball/BFS/pair generation."""
from pathlib import Path
from collections import Counter
import json
import struct
import time

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parent/'source_and_single'
ROOT=OUT.parents[4]
started=time.process_time()
binding=json.loads((SOURCE/'PORT_BINDING.json').read_text())
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_search']
assert (binding['source_n'],binding['source_m'])==(364,714)
ports=binding['eligible_ports']
assert len(ports)==28
degrees=[0]*364
with (ROOT/binding['source_file']).open() as f:
    assert tuple(map(int,f.readline().split()))==(364,714)
    edge_count=0
    for line in f:
        u,v=map(int,line.split());degrees[u]+=1;degrees[v]+=1;edge_count+=1
assert edge_count==714 and Counter(degrees)==Counter({3:28,4:336})
assert ports==[v for v,d in enumerate(degrees) if d==3]

def read_masks(filename):
    raw=(SOURCE/filename).read_bytes()
    assert len(raw)==28*6*8
    rows=struct.unpack('<168Q',raw)
    return [sum(rows[6*i+w]<<(64*w) for w in range(6)) for i in range(28)]

r3=read_masks(binding['R3_binary_file'])
r4=read_masks(binding['R4_binary_file'])
incidence3=[[q for q in ports if (row>>q)&1] for row in r3]
incidence4=[[q for q in ports if (row>>q)&1] for row in r4]
assert incidence3==[[p] for p in ports] and incidence4==[[p] for p in ports]
Na=ports[:3];Nb=ports[3:6]
u1=0;u2=0
for i in range(3):u1|=r4[i];u2|=r3[i]
for i in range(3,6):u1|=r3[i];u2|=r4[i]
covered1=[p for p in ports if (u1>>p)&1]
covered2=[p for p in ports if (u2>>p)&1]
assert covered1==covered2==ports[:6]
missing=[p for p in ports if not (u1>>p)&1]
result=dict(
    status='COMPLETE_UNIFORM_PORT_OBSTRUCTION',
    source_file=binding['source_file'],source_n=364,source_m=714,
    source_degree_histogram=dict(Counter(degrees)),ports=ports,
    R3_port_intersections=incidence3,R4_port_intersections=incidence4,
    prediction_supported=False,
    scope='Allunordereddisjointpairs of3-subsets ofthese28actualdegree3ports;twoadjacentnewroots;nootheredgechange',
    port_triples=3276,unordered_disjoint_pairs_excluded_by_uniform_proof=3767400,
    pairs_enumerated=0,profile1000_run=False,native_compiled=False,
    profile_not_run_reason='Everypairfailsauniformnecessaryportcoverageconditionbeforeenumeration',
    uniform_proof='Forallfreeportsp,R4_old(p)intersectP={p};thusR4(A)unionR3(B)andR3(A)unionR4(B)intersectP=AunionB,only6of28ports',
    uncovered_old_ports_per_new_root=22,
    first_lex_pair=dict(Na=Na,Nb=Nb,covered_ports_condition1=covered1,covered_ports_condition2=covered2,
        missing_old_ports=missing,first_witness=missing[0],hypothetical_newroot_distances_to_witness=[6,6]),
    inherited_source_D=5,
    forced_family_D=6,
    forced_family_D_proof='Distinctportsareatolddistance5byR4exclusionandsourceD5.Anyunselectedportlies5oldstepsfromthelastselectedportafteranewrootexit,soitsnewrootdistance>=6;anowntripleportgives<=6.',
    hypothetical_n=366,actual_n=None,actual_D=None,graph_generated=False,
    R3_R4_recomputed=0,source_allroot_BFS=0,pair_search_run=False,
    CPU_seconds=time.process_time()-started,
    evidence=['../source_and_single/PORT_BINDING.json','../source_and_single/PORT_BALLS.json',
              '../source_and_single/R3.u64le.bin','../source_and_single/R4.u64le.bin',
              '../source_and_single/PORT_CLASSES.json','PREDICTION.json','capacity_check.py'],
    pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps({k:v for k,v in result.items() if k not in ['R3_port_intersections','R4_port_intersections']},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','pairs_enumerated','unordered_disjoint_pairs_excluded_by_uniform_proof','forced_family_D','CPU_seconds']}))
