#!/usr/bin/env python3
"""Assemble exact certificate provenance and transport to all3107 actual markings."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as Q
from time import process_time
import json
P=Path(__file__).resolve().parent;B=P.parent;start=process_time()
D=json.loads((B/'DOMAIN.json').read_text())['records'];G=defaultdict(list)
def key(z):return (tuple(z['canonical_large']),z['canonical_lowmask'])
for i,z in enumerate(D):G[key(z)].append(i)
lookup={(z['base'],tuple(z['low'])):i for i,z in enumerate(D)}
cover={}
for k,ids in G.items():
 good=[i for i in ids if Q(D[i]['old_bound'])<1]
 if not good:continue
 i=min(good,key=lambda j:(Q(D[j]['old_bound']),j));z=D[i]
 cover[k]={'source':'old_affine_corrected','record':i,'positions':z['positions'],'bound':z['old_bound'],'raw':False}
assert len(cover)==325
PILOT=json.loads((B/'PROFILE.json').read_text())['records'];pc=0
for j,z in enumerate(PILOT):
 i=lookup[(z['base'],tuple(z['low']))];k=key(D[i])
 if k in cover:continue
 assert {int(t):n for t,n in z['counts'].items()}=={int(t):n for t,n in D[i]['counts'].items()}
 assert Q(z['raw_witness_bound'])<1
 assert sum((min(Q(row[n]) for n in ('A','B','C')) for row in z['rows']),Q())==Q(z['raw_witness_bound'])
 cover[k]={'source':'prior_pilot_raw','record':i,'source_record':j,'positions':z['positions'],'bound':z['raw_witness_bound'],'raw':True};pc+=1
assert pc==2
SC=json.loads((B/'diverse40/RESULT.json').read_text())['records'];fc=0
for j,z in enumerate(SC):
 i=z['domain_record'];k=key(z);assert k==key(D[i]) and k not in cover
 assert {int(t):n for t,n in z['counts'].items()}=={int(t):n for t,n in D[i]['counts'].items()}
 assert Q(z['raw_bound'])<1 and z['all_25_rows_independently_equal']
 assert sum((min(Q(row[n]) for n in ('A','B','C')) for row in z['raw_rows']),Q())==Q(z['raw_bound'])
 cover[k]={'source':'diverse40_raw','record':i,'source_record':j,'positions':z['positions'],'bound':z['raw_bound'],'raw':True};fc+=1
assert fc==40
N=[json.loads(line) for line in (P/'RECORDS.jsonl').read_text().splitlines() if line.strip()]
assert len(N)==1322
nc=0
for j,z in enumerate(N):
 i=z['domain_record'];k=key(z);assert k==key(D[i]) and k not in cover
 assert {int(t):n for t,n in z['counts'].items()}=={int(t):n for t,n in D[i]['counts'].items()}
 assert z['strict'] and Q(z['raw_bound'])<1 and z['all_25_rows_independently_equal']
 assert len(z['raw_rows'])==25
 assert sum((min(Q(row[n]) for n in ('A','B','C')) for row in z['raw_rows']),Q())==Q(z['raw_bound'])
 cover[k]={'source':'full_raw','record':i,'source_record':j,'positions':z['positions'],'bound':z['raw_bound'],'raw':True};nc+=1
assert set(cover)==set(G) and len(cover)==1689

def move(mask,p):return sum(1<<p[i] for i in range(9) if mask>>i&1)
callers=[];counts=Counter()
for i,tgt in enumerate(D):
 c=cover[key(tgt)];src=D[c['record']];ps=src['old_to_canonical'];pt=tgt['old_to_canonical'];assert sorted(ps)==sorted(pt)==list(range(9))
 canonical_src={move(int(m),ps):n for m,n in src['counts'].items()};canonical_tgt={move(int(m),pt):n for m,n in tgt['counts'].items()};assert canonical_src==canonical_tgt
 inverse={j:k for k,j in enumerate(ps)};positions=[c['positions'][inverse[pt[k]]] for k in range(9)]
 assert len(positions)==len(set(positions))==9 and all(1<=p<=25 for p in positions)
 assert {ps[j] for j in src['low']}=={pt[j] for j in tgt['low']}
 callers.append({'domain_record':i,'base':tgt['base'],'low':tgt['low'],'certificate':c,'transported_positions':positions});counts[c['source']]+=1
rawvals=[Q(z['raw_bound']) for z in SC+N]+[Q(z['raw_witness_bound']) for z in PILOT]
out={'status':'COMPLETE_ALL1689_ORBITS_ALL3107_MARKINGS','old_corrected_strict_orbits':325,'old_new_raw_pilot_orbits':2,'diverse40_raw_orbits':40,'full_raw_orbits':1322,'raw_orbits':1364,'colored_orbits':len(cover),'actual_markings':len(callers),'all_counts_transported_exactly':True,'new_full_rows_replayed':25*1322,'source_by_marking':dict(counts),'maximum_new_raw':str(max(rawvals)),'cpu_seconds':process_time()-start,'callers':callers}
(P/'COVERAGE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='callers'}))
