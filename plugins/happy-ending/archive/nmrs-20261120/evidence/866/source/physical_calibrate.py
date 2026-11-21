"""Assign original36 true ranks, order, P, all color/DP and replay full CNF."""
import hashlib
import heapq
import itertools as it
import json
from pathlib import Path
import platform
import time

assert platform.system() == 'Linux'
HERE = Path(__file__).resolve().parent
OUT = HERE/'h13-physical-all02'
PRIOR = HERE/'h13-exact-wlog-third01'


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def main():
    began=time.monotonic()
    source=Path('<private-linux-workspace>/reports/n866-scalar-grid-20261119/calibration-C30/ambient36_witness.json')
    witness=json.loads(source.read_text())
    chi={tuple(map(int,k.split(','))):int(v=='R') for k,v in witness['chi_in_natural_order'].items()}
    swapped=bool(chi[0,1,2])
    if swapped:
        chi={k:1-v for k,v in chi.items()}
    meta=json.loads((PRIOR/'inputs/base-metadata.json').read_text())
    initial=json.loads((PRIOR/'structure.json').read_text())
    structure=json.loads((OUT/'structure.json').read_text())
    manifest=json.loads((OUT/'manifest.json').read_text())
    shapes=list(map(tuple,meta['universe']['column_heights']))
    index={shape:j for j,shape in enumerate(shapes)}
    ranks,states={},[0]
    for end in range(1,36):
        incoming=[]
        for start in range(end):
            rank=[1,1]
            for earlier in range(start):
                col=chi[earlier,start,end]
                rank[col]=max(rank[col],ranks[earlier,start][col]+1)
            ranks[start,end]=rank
            incoming.append(rank)
        states.append(index[tuple(max((red for blue,red in incoming if blue>=x),default=0) for x in range(1,5))])
    owners={state:owner for owner,state in enumerate(states)}
    assert len(owners)==36 and states[:3]==[0,1,5]
    values={j+1:j not in owners for j in range(70)}
    for record in meta['labels']:
        a,b=record['pair']
        selected=tuple(ranks[owners[a],owners[b]]) if a in owners and b in owners else tuple(record['choices'][0]['cell'])
        for choice in record['choices']:
            values[choice['variable']]=tuple(choice['cell'])==selected
    for record in meta['colors']:
        triple=record['triple']
        values[record['variable']]=bool(chi[tuple(owners[j] for j in triple)]) if all(j in owners for j in triple) else False
    actual4=set()
    for a,t,u,v in it.combinations(range(36),4):
        col=chi[a,t,u]
        if chi[t,u,v]==col:
            actual4.add((states[a],states[u],states[v],col))
    actual5=set()
    for a,t,u,col in actual4:
        for v in range(owners[u]+1,36):
            if chi[owners[t],owners[u],v]==col:
                actual5.add((a,states[v],col))
    assert all((a,b,1-c) not in actual5 for a,b,c in actual5)
    for record in meta['reach4']:
        values[record['variable']]=tuple(record['key']) in actual4
    for record in meta['reach5']:
        values[record['variable']]=tuple(record['key']) in actual5
    for record in meta['threshold']:
        i,j=record['key']
        values[record['variable']]=sum(values[t] for t in range(1,i+1))>=j
    for i in range(13,71):
        values[69209+i-13]=sum(values[t] for t in range(1,i+1))>=13
    for i,flag in initial['threshold14']:
        values[flag]=sum(values[t] for t in range(1,i+1))>=14
    mask=sum(chi[triple]<<bit for bit,triple in enumerate(it.combinations(range(6),3)))
    library=json.loads((PRIOR/'prefix6-library.json').read_text())
    for template in library['templates']:
        selected=template['mask']==mask
        values[template['selector']]=selected
        if selected:
            assert template['ordered_states']==states[:6]
    for link in initial['selection_chain']:
        values[link['variable']]=values[link['previous']] or values[link['selector']]
    cells=[{(x,y) for x in range(1,5) for y in range(1,s[x-1]+1)} for s in shapes]
    edges={a:{b for b in range(70) if cells[a]<cells[b]} for a in range(70)}
    for a,b in zip(states,states[1:]):
        edges[a].add(b)
    degree={a:sum(a in row for row in edges.values()) for a in range(70)}
    queue=[a for a in range(70) if degree[a]==0]
    heapq.heapify(queue)
    total=[]
    while queue:
        a=heapq.heappop(queue)
        total.append(a)
        for b in edges[a]:
            degree[b]-=1
            if degree[b]==0:
                heapq.heappush(queue,b)
    assert len(total)==70
    place={a:i for i,a in enumerate(total)}
    for (a,b),flag in structure['orders']:
        values[flag]=place[a]<place[b]
    for (a,b),choices in structure['labels']:
        selected=tuple(ranks[owners[a],owners[b]]) if a in owners and b in owners and owners[a]<owners[b] else None
        for cell,flag in choices:
            values[flag]=tuple(cell)==selected
    for triple,flag in structure['colors']:
        values[flag]=bool(chi[tuple(sorted(owners[a] for a in triple))]) if all(a in owners for a in triple) else False
    for (a,b,col,value),flag in structure['coordinates']:
        values[flag]=a in owners and b in owners and owners[a]<owners[b] and ranks[owners[a],owners[b]][col]==value
    for (a,b,c,col,value),flag in structure['witnesses']:
        values[flag]=(all(j in owners for j in (a,b,c)) and owners[a]<owners[b]<owners[c]
                      and ranks[owners[a],owners[b]][col]==value and chi[owners[a],owners[b],owners[c]]==col)
    for key,flag in structure['reach4']:
        values[flag]=tuple(key) in actual4
    for key,flag in structure['reach5']:
        values[flag]=tuple(key) in actual5
    assert len(values)==manifest['variables'] and max(values)==manifest['variables']
    checked=excluded=0
    failures=[]
    with (OUT/'formula.cnf').open() as stream:
        for line in stream:
            if line.startswith(('p','c')):
                continue
            clause=list(map(int,line.split()))[:-1]
            if clause==[-70229]:
                excluded+=1
                continue
            checked+=1
            if not any(values[abs(literal)]==(literal>0) for literal in clause):
                failures.append({'line':checked+excluded,'clause':clause})
                if len(failures)>=10:
                    break
    result={'status':'PASS_FULL_ORIGINAL36_PHYSICAL_CNF_EXCEPT_ONLY_H13_UPPER' if not failures else 'FAILED_PHYSICAL_CALIBRATION',
            'population':36,'holes':34,'source':str(source),'source_sha256':sha(source),
            'chosen_prefix_mask':mask,'color_swapped_to_WLOG':swapped,'full_order':total,
            'assigned_variables':len(values),'checked_clauses':checked,'excluded_only_upper_count':excluded,
            'failures':failures,'cnf_sha256':sha(OUT/'formula.cnf'),'seconds':time.monotonic()-began}
    (OUT/'calibration.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
    assert not failures and excluded==1 and checked+excluded==manifest['clauses']


if __name__=='__main__':
    main()
