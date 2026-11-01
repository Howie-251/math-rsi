#!/usr/bin/env python3
"""Fourteen single-center pin types by red/blue event subset IE."""
from itertools import combinations
from pathlib import Path
from math import comb
from time import process_time
import json,sys
P=Path(__file__).resolve().parent

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def build(sizes,shared):
    blocks=[set() for _ in sizes];vertex=0
    for indices in shared:
        for i in indices:blocks[i].add(vertex)
        vertex+=1
    for i,size in enumerate(sizes):
        while len(blocks[i])<size:blocks[i].add(vertex);vertex+=1
    assert vertex==18
    return [sum(1<<v for v in block) for block in blocks]

def cases():
    for name,shared in [('triple',[(0,1,2)]),('same',[(0,1),(0,1)]),('adjacent',[(0,1),(1,2)]),('disjoint',[(0,1),(2,3)])]:
        yield 'w0_'+name,build([4]*5,shared),['']*5
    for shape,shared in [('3_4',[(0,1)]),('4_4',[(1,2)])]:
        for color in 'RB':yield 'w1_'+shape+'_'+color,build([3,4,4,4,4],shared),[color,'','','','']
    for colors in ['RR','BB','RB']:
        yield 'w2_double_pin_'+colors,build([2,4,4,4,4],[]),[colors,'','','','']
        yield 'w2_two_pins_'+colors,build([3,3,4,4,4],[]),[colors[0],colors[1],'','','']

def subsets(masks):
    for n in range(1,len(masks)+1):
        for indices in combinations(range(len(masks)),n):
            union=0
            for i in indices:union|=masks[i]
            yield union,(-1)**(n+1)

def evaluate(case):
    name,blocks,pins=case
    red=[block for block,pin in zip(blocks,pins) if 'B' not in pin]
    blue=[block for block,pin in zip(blocks,pins) if 'R' not in pin]
    result={}
    for q in (8,9):
        total=0
        for r,rc in subsets(red):
            for b,bc in subsets(blue):
                if not r&b:total+=rc*bc*choose(18-r.bit_count()-b.bit_count(),q-b.bit_count())
        assert 0<=total<=comb(18,q)
        result[str(q)]=total
    return {'name':name,'blocks':blocks,'pins':pins,'conflict_counts':result}

def main():
    started=process_time();domain=list(cases());assert len(domain)==14
    if '--profile' in sys.argv:
        row=evaluate(domain[4]);out={'status':'PROFILE_COMPLETE','one_new_type':row,
            'cpu_seconds':process_time()-started,'estimated_all14_cpu_seconds':(process_time()-started)*14}
        (P/'PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    records=[evaluate(case) for case in domain]
    assert [r['conflict_counts']['8'] for r in records[:4]]==[2557,3186,2967,2940]
    assert [r['conflict_counts']['9'] for r in records[:4]]==[3186,3996,3708,3672]
    out={'status':'PASS','single_center_pin_types':14,'quotas':[8,9],
         'method':'red/blue forcing block-subset IE; no literal coloring enumeration',
         'cpu_seconds':process_time()-started,'records':records}
    (P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','cpu_seconds':out['cpu_seconds'],
         'values':[(r['name'],r['conflict_counts']) for r in records]}))
if __name__=='__main__':main()
