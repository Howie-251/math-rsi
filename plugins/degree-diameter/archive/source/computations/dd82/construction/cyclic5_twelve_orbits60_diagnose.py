"""One bounded C5-automorphism diagnosis of the actual 20-bad-pair seed.

First test automorphisms fixing each of the six original Petersen fibres,
then (only if necessary) enumerate graph automorphisms without fibre colors.
Any returned permutation is checked on the full original edge set.
No candidate optimization, SAT, or graph-distance search is performed.
"""
from pathlib import Path
import collections
import json
import os
import resource
import signal
import time

START_CPU=time.process_time()
START_WALL=time.monotonic()
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'computations/dd82/construction/cyclic5_twelve_orbits60_run'
SOURCE=ROOT/'computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges'
OLD_CHECK=SOURCE.with_name('candidate.best.verification.json')


class BudgetStop(Exception):
    pass


def alarm(*args):
    raise BudgetStop


def dump(path,obj):
    path.write_text(json.dumps(obj,indent=2)+'\n')


def cycle_decomposition(p):
    unseen=set(range(len(p)));cycles=[]
    while unseen:
        v=min(unseen);cycle=[];u=v
        while u in unseen:
            unseen.remove(u);cycle.append(u);u=p[u]
        assert u==v
        cycles.append(cycle)
    return cycles


def main():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(5,6))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'diagnosis.json').exists(),'Do not repeat this diagnostic'
    signal.signal(signal.SIGPROF,alarm)
    signal.setitimer(signal.ITIMER_PROF,4.6)
    import networkx as nx

    lines=SOURCE.read_text().splitlines()
    n,e=map(int,lines[0].split())
    edges={tuple(map(int,line.split())) for line in lines[1:]}
    assert n==60 and e==240 and len(edges)==240
    neighbors=[set() for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n
        neighbors[u].add(v);neighbors[v].add(u)
    assert all(len(row)==8 for row in neighbors)
    saved_check=json.loads(OLD_CHECK.read_text())
    assert saved_check['bad_pair_count']==20

    found=None;method=None;restricted_count=0;full_count=0
    restricted_complete=False;full_complete=False;budget_stop=False
    graph=nx.Graph();graph.add_nodes_from(range(n));graph.add_edges_from(edges)
    # Every fibre-preserving automorphism is determined by its first fibre:
    # each other fibre is transported through its unique matching to fibre 0.
    transports=[list(range(10))]
    for fibre in range(1,6):
        row=[]
        for u in range(10):
            targets=neighbors[u]&set(range(10*fibre,10*fibre+10))
            assert len(targets)==1
            row.append(next(iter(targets)))
        assert len(set(row))==10
        transports.append(row)
    try:
        first=graph.subgraph(range(10)).copy()
        for automorphism in nx.algorithms.isomorphism.GraphMatcher(first,first).isomorphisms_iter():
            restricted_count+=1
            p=[-1]*60
            for row in transports:
                for u in range(10):p[row[u]]=row[automorphism[u]]
            if any(len(c)!=5 for c in cycle_decomposition(p)):continue
            image={tuple(sorted((p[u],p[v]))) for u,v in edges}
            if image==edges:
                found=p;method='fibre_preserving_transport';break
        else:
            restricted_complete=True
        if found is None:
            # This coloring is a graph invariant, unlike the old fibre labels.
            bad_counts=collections.Counter(v for item in saved_check['bad_pairs'] for v in item['pair'])
            for v in graph:graph.nodes[v]['bad_count']=bad_counts[v]
            matcher=nx.algorithms.isomorphism.GraphMatcher(
                graph,graph,node_match=lambda a,b:a['bad_count']==b['bad_count'])
            for automorphism in matcher.isomorphisms_iter():
                full_count+=1
                p=[automorphism[v] for v in range(60)]
                if all(len(c)==5 for c in cycle_decomposition(p)):
                    found=p;method='unrestricted_graphmatcher';break
            else:
                full_complete=True
    except BudgetStop:
        budget_stop=True
    finally:
        signal.setitimer(signal.ITIMER_PROF,0)

    report=dict(source=str(SOURCE.relative_to(ROOT)),networkx_version=nx.__version__,
        restricted_tested=restricted_count,restricted_complete=restricted_complete,
        unrestricted_tested=full_count,unrestricted_complete=full_complete,
        budget_stop=budget_stop,found=found is not None,method=method,
        solver_calls=0,optimization_calls=0,full_bfs_reruns=0,cpu_budget_seconds=5)
    if found is not None:
        assert sorted(found)==list(range(60))
        assert {tuple(sorted((found[u],found[v]))) for u,v in edges}==edges
        cycles=cycle_decomposition(found)
        assert len(cycles)==12 and all(len(c)==5 for c in cycles)
        coordinates={v:(a,t) for a,c in enumerate(cycles) for t,v in enumerate(c)}
        labels={v:5*a+t for v,(a,t) in coordinates.items()}
        palette=[]
        for a in range(12):
            for b in range(a+1,12):
                for d in range(5):
                    orbital={tuple(sorted((cycles[a][t],cycles[b][(t+d)%5]))) for t in range(5)}
                    palette.append(dict(index=len(palette),kind='between',a=a,b=b,shift=d,
                                        edges=sorted(orbital),selected=orbital<=edges))
            for s in (1,2):
                orbital={tuple(sorted((cycles[a][t],cycles[a][(t+s)%5]))) for t in range(5)}
                palette.append(dict(index=len(palette),kind='within',a=a,b=a,shift=s,
                                    edges=sorted(orbital),selected=orbital<=edges))
        assert len(palette)==354
        assert sum(len(o['edges']) for o in palette)==1770
        assert len({tuple(edge) for o in palette for edge in o['edges']})==1770
        assert all(not (set(map(tuple,o['edges']))&edges) or o['selected'] for o in palette)
        selected=[o for o in palette if o['selected']]
        assert len(selected)==48
        assert {tuple(edge) for o in selected for edge in o['edges']}==edges
        voltages=[[[] for _ in range(12)] for _ in range(12)]
        for o in selected:
            a,b,d=o['a'],o['b'],o['shift']
            if a==b:voltages[a][a].extend([d,(-d)%5])
            else:voltages[a][b].append(d);voltages[b][a].append((-d)%5)
        voltages=[[sorted(x) for x in row] for row in voltages]
        assert [sum(map(len,row)) for row in voltages]==[8]*12
        relabelled=sorted(tuple(sorted((labels[u],labels[v]))) for u,v in edges)
        dump(OUT/'seed.relabelled.json',dict(n=60,edges=relabelled,
            coordinates='vertex 5*a+t for t in Z5',source=str(SOURCE.relative_to(ROOT))))
        (OUT/'seed.relabelled.edges').write_text('60 240\n'+''.join(f'{u} {v}\n' for u,v in relabelled))
        dump(OUT/'automorphism.json',dict(permutation=found,cycles=cycles,
            old_to_new=[labels[v] for v in range(60)],edge_images_checked=240,
            order=5,semiregular=True))
        dump(OUT/'palette.json',dict(orbit_count=354,edge_orbits=palette))
        dump(OUT/'voltages.json',dict(voltages=voltages,selected_orbit_indices=[o['index'] for o in selected],
            selected_orbit_count=48,weighted_quotient_degrees=[sum(map(len,row)) for row in voltages],
            bad_pairs_relabelled=sorted(tuple(sorted((labels[u],labels[v])))
                for item in saved_check['bad_pairs'] for u,v in [item['pair']]),
            inherited_verification=str(OLD_CHECK.relative_to(ROOT)),
            inherited_bad_pair_count=20,inherited_diameter=saved_check['diameter']))
        report.update(cycle_type=[5]*12,palette_orbits=354,selected_orbits=48,
                      all_edges_reconstructed=True,inherited_bad_pairs=20)
    report.update(cpu_seconds=time.process_time()-START_CPU,wall_seconds=time.monotonic()-START_WALL)
    dump(OUT/'diagnosis.json',report)
    print(json.dumps(report),flush=True)


if __name__=='__main__':main()
