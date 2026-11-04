"""Exact sufficient-condition tests; no full-space claim."""
import json
from pathlib import Path
from collections import Counter
import networkx as nx
from verify_near_perfect import complete,cube_edges
from single_bridge_probe import solve
from four_hole_surgery import verify_path,edge,edges
ROOT=Path(__file__).resolve().parent

def certificate(m,u,v,n=6):
    for excluded in m:
        rest=[e for e in m if e!=excluded]
        used={a for e in rest for a in e}
        if u in used or v in used:continue
        free=set(range(1<<n))-used-{u,v}
        graph=nx.Graph();graph.add_nodes_from(free)
        graph.add_edges_from((a,b) for a,b in cube_edges(n) if a in free and b in free)
        extra=sorted(tuple(sorted(e)) for e in nx.max_weight_matching(graph,maxcardinality=True))
        if len(extra)*2==len(free):
            l=rest+extra
            assert len(l)==(1<<(n-1))-1 and {a for e in l for a in e}==set(range(1<<n))-{u,v}
            return {'removed_matching_edge':excluded,'completion':l}
    return None

def old_label(c):
    m,u,v=c['matching'],c['u'],c['v']
    if len({a^b for a,b in m})<=5:return 'known_five_directions'
    if not complete(m,u)[1]:return 'D2_perfect_completion'
    if len(complete(m,u,avoid_root=True)[1])==2:return 'N3_near_perfect_completion'
    for i in range(6):
        if not ((u^v)&(1<<i)):continue
        cross=[(a,b) if (a&(1<<i))==(u&(1<<i)) else (b,a)
               for a,b in m if (a^b)==1<<i]
        if len(cross)==1 and (cross[0][0].bit_count()-u.bit_count())%2:return 'D5_single_bridge'
    return 'remaining'

def main():
    data=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))['cases']
    counts=Counter();new=[]
    for c in data:
        if c['n']!=6:continue
        label=old_label(c)
        if label=='remaining':
            cert=certificate(c['matching'],c['u'],c['v'])
            if cert:
                label='F1_one_displaced_edge'
                new.append({**c,**cert})
        counts[label]+=1
    examples=[]
    for c in new[:12]:
        u,v=c['u'],c['v'];a,b=c['removed_matching_edge'];l=c['completion']
        assert len({a^b for a,b in l})>=4
        p=l+[(u,v)]
        result=solve(6,p,a,b,5,seconds=8,allowed_long=[(u,v)])
        example={'n':6,'u':u,'v':v,'matching':c['matching'],
                 'completion':l,'removed_matching_edge':[a,b],'status':result['status']}
        if result['status']=='FOUND':
            final=(edges(result['path'])|{edge(a,b)})-{edge(u,v)}
            path=verify_path(final,c['matching'],u,v)
            assert path is not None
            example.update({'intermediate_path':result['path'],'path':path})
        examples.append(example)
    result={'scope':'classification of original 1152 sampled Q6 cases only',
            'counts':dict(counts),'newly_closed_count':len(new),'certificates':new,
            'constructive_examples':examples}
    (ROOT/'one_displaced_edge_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps({'counts':dict(counts),'newly_closed_count':len(new),
                      'construction_counts':dict(Counter(c['status'] for c in examples))},indent=2))

if __name__=='__main__':main()
