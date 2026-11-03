#!/usr/bin/env python3
import itertools
import json
import time
from collections import deque
from pathlib import Path

HERE=Path(__file__).resolve().parent
START=time.process_time()
INV=(1,0,3,2,4)

def controller(deck):
    n=3*deck
    out=[[None]*5 for _ in range(n)]
    perm=(0,2,1)
    volt=(6,3,12)
    for c in range(3):
        for g in range(deck):
            u=c*deck+g
            v=perm[c]*deck+(g+volt[c])%deck
            out[u][0]=v
            out[v][1]=u
            v=((c+1)%3)*deck+g
            out[u][2]=v
            out[v][3]=u
    for g in range(deck):
        u=g;v=deck+(g+1)%deck
        out[u][4]=v;out[v][4]=u
        out[2*deck+g][4]=2*deck+(g+deck//2)%deck
    assert all(len(set(row))==5 and u not in row for u,row in enumerate(out))
    assert all(out[v][INV[p]]==u for u,row in enumerate(out) for p,v in enumerate(row))
    return out

def end(C,u,word):
    for p in word:u=C[u][p]
    return u

def main():
    saved=json.loads((HERE.parent/'f4_c60_edge_projective/PARAMETERS.json').read_text())['controller']
    old=controller(20)
    assert old==saved,'Literal old controller formula mismatch: stop before candidate'
    C=controller(22)
    words=[w for k in range(4) for w in itertools.product(range(5),repeat=k)]
    roots=[]
    for c in range(3):
        u=c*22
        route={v:[] for v in range(66)}
        for w in words:route[end(C,u,w)].append(w)
        missing=[v for v,ws in route.items() if not ws]
        roots.append({'root':u,'reached':66-len(missing),'missing_vertices':missing,
                      'missing_base_deck':[[v//22,v%22] for v in missing],
                      'reachable_residues_by_base':[[g for g in range(22) if route[b*22+g]] for b in range(3)]})
    bad=[x for x in roots if x['missing_vertices']]
    result={'status':'CONTROLLER_NECESSARY_GATE_FAIL' if bad else 'CONTROLLER_NECESSARY_GATE_PASS_NOT_GRAPH',
            'source_controller_literal_binding':True,'source_controller_BFS_rerun':False,
            'candidate_vertices':66,'potential_fiber_vertices':4224,'potential_degree':20,
            'source_graph_generated':False,'candidate_fiber_graph_generated':False,'SAT_calls':0,
            'examined_root_classes':roots,'roots_cover_all_by_deck_translation':True,
            'first_counterexample':{'root':bad[0]['root'],'target':bad[0]['missing_vertices'][0]} if bad else None,
            'fixed_chart_certificate_controller_bound':68,
            'CPU_seconds':time.process_time()-START,
            'scope':'Only deck22, original a/b voltages, exact matching half-shift11. Does not exclude other66-vertex controllers or changed voltage rules.'}
    (HERE/'CONTROLLER66.json').write_text(json.dumps(C)+'\n')
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
