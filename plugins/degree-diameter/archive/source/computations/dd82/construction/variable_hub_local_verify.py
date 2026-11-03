#!/usr/bin/env python3
"""Independent fixed-order set recursion from the original ten triple tables.

This checks the decisive local negative result once. It does not use the C++
prepared input, bit masks, variable ordering, or connectivity filter.
"""
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'variable_hub_local_run'
POINTS=set(range(10))

def matchings(remaining,leave):
    if not remaining:
        yield []
        return
    u=min(remaining)
    for v in sorted(leave[u]&remaining):
        yield from ([{u,v}]+tail for tail in matchings(remaining-{u,v},leave))

def search(blocks,edges,mate):
    domains=[]
    for v in range(10):
        forbidden={v,mate[v]}
        domains.append([(b,e,POINTS-forbidden-block-edge)
            for b,block in enumerate(blocks) for e,edge in enumerate(edges)
            if not (forbidden&block or forbidden&edge or block&edge)])
    nodes=0
    def visit(chosen,usedb,usede):
        nonlocal nodes
        nodes+=1
        v=len(chosen)
        if v==10:return chosen
        for b,e,neighbors in domains[v]:
            if b in usedb or e in usede:continue
            if any((u in neighbors)!=(v in chosen[u][2]) for u in range(v)):continue
            found=visit(chosen+[(b,e,neighbors)],usedb|{b},usede|{e})
            if found is not None:return found
        return None
    found=visit([],set(),set())
    return dict(nodes=nodes,domain_sizes=list(map(len,domains)),witness=found)

def main():
    start=time.process_time()
    source=json.loads((HERE/'d1_10_3_catalog/10_3_grunbaum.json').read_text())
    results=[]
    for config in source['configurations']:
        blocks=[set(b) for b in config['blocks']]
        assert len(blocks)==10 and all(len(b)==3 for b in blocks)
        common=[[sum(u in b and v in b for b in blocks) for v in range(10)] for u in range(10)]
        assert all(common[u][u]==3 for u in range(10))
        assert all(common[u][v]<=1 for u in range(10) for v in range(u))
        leave=[{v for v in range(10) if v!=u and common[u][v]==0} for u in range(10)]
        assert all(len(row)==3 for row in leave)
        for matching in matchings(POINTS,leave):
            mate=[next(iter(pair-{u})) for u in range(10) for pair in matching if u in pair]
            edges=[{u,v} for u in range(10) for v in sorted(leave[u]-{mate[u]}) if u<v]
            assert len(edges)==10
            r=search(blocks,edges,mate)
            assert r['witness'] is None,'Counterexample to the C++ zero found; inspect before claiming closure.'
            results.append(dict(configuration=config['grunbaum_number'],mate=mate,**r))
    assert len(results)==71
    old=[json.loads(line) for line in (OUT/'states.results.jsonl').read_text().splitlines()]
    assert len(old)==71 and all(r['status']=='complete_no_witness' for r in old)
    result=dict(scope='Independent local feasibility enumeration from original triple tables; no connectivity or spectral pruning',
        source='d1_10_3_catalog/10_3_grunbaum.json',complete=True,states=71,witness_states=0,
        nodes=sum(r['nodes'] for r in results),cpu_seconds=time.process_time()-start,results=results)
    (OUT/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))

if __name__=='__main__':main()
