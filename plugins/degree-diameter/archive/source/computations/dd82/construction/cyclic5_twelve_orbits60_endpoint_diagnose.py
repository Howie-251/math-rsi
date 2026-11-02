"""Exact bad-endpoint reduction, then export the distinct known C5 seed.

The 20-bad-pair graph is not replaced by the older 50-bad-pair graph.
If endpoint neighbourhoods repeat, stop the unique-lift route without
claiming that an order-five automorphism of the 20-bad graph is absent.
"""
from collections import Counter,defaultdict
from pathlib import Path
import json
import os
import resource
import signal
import time

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'computations/dd82/construction'
OUT=BASE/'cyclic5_twelve_orbits60_endpoint_run'
START_CPU=time.process_time()
START_WALL=time.monotonic()


class BudgetStop(Exception):pass


def alarm(*args):raise BudgetStop


def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')


def read_edges(path):
    rows=[tuple(map(int,line.split())) for line in path.read_text().splitlines() if line.strip()]
    assert rows[0]==(60,240)
    edges=set(rows[1:]);assert len(edges)==240
    adj=[set() for _ in range(60)]
    for u,v in edges:
        assert 0<=u<v<60
        adj[u].add(v);adj[v].add(u)
    assert all(len(row)==8 for row in adj)
    return edges,adj


def cycles(p):
    todo=set(range(60));answer=[]
    while todo:
        u=min(todo);cycle=[];v=u
        while v in todo:
            todo.remove(v);cycle.append(v);v=p[v]
        assert v==u
        answer.append(cycle)
    return answer


def export_voltage(name,path,edges,permutation,bad_pairs,old_check):
    target=OUT/name;target.mkdir(exist_ok=True)
    assert sorted(permutation)==list(range(60))
    assert {tuple(sorted((permutation[u],permutation[v]))) for u,v in edges}==edges
    orbit_vertices=cycles(permutation)
    assert len(orbit_vertices)==12 and all(len(c)==5 for c in orbit_vertices)
    relabel={v:5*a+t for a,c in enumerate(orbit_vertices) for t,v in enumerate(c)}
    selected=[];catalog=[];all_pairs=set()
    for a in range(12):
        for b in range(a,12):
            for d in ((1,2) if a==b else range(5)):
                orbital={tuple(sorted((orbit_vertices[a][t],orbit_vertices[b][(t+d)%5]))) for t in range(5)}
                assert len(orbital)==5 and not (orbital&all_pairs)
                all_pairs|=orbital
                assert not (orbital&edges) or orbital<=edges
                item=dict(index=len(catalog),a=a,b=b,shift=d,
                          kind='within' if a==b else 'between',selected=orbital<=edges,
                          original_edges=sorted(orbital))
                catalog.append(item)
                if item['selected']:selected.append(item)
    assert len(catalog)==354 and len(all_pairs)==1770 and len(selected)==48
    assert {tuple(e) for item in selected for e in item['original_edges']}==edges
    shifts=[[set() for _ in range(12)] for _ in range(12)]
    for item in selected:
        a,b,d=item['a'],item['b'],item['shift']
        shifts[a][b].add(d);shifts[b][a].add((-d)%5)
    assert [sum(map(len,row)) for row in shifts]==[8]*12
    new_edges=sorted(tuple(sorted((relabel[u],relabel[v]))) for u,v in edges)
    expected_bad=sorted(tuple(sorted((relabel[u],relabel[v]))) for u,v in bad_pairs)
    # Independent direct voltage coverage, not a repeat BFS of the old graph.
    voltage_bad=[];missing=[]
    for a in range(12):
        for b in range(a,12):
            covered=set(shifts[a][b])
            for c in range(12):
                covered|={(x+y)%5 for x in shifts[a][c] for y in shifts[c][b]}
            required=set(range(5)) if a!=b else {1,2,3,4}
            absent=sorted(required-covered)
            if absent:missing.append(dict(a=a,b=b,missing_shifts=absent))
            for d in absent:
                for t in range(5):
                    u,v=5*a+t,5*b+(t+d)%5
                    if u<v:voltage_bad.append((u,v))
    voltage_bad=sorted(set(voltage_bad))
    assert voltage_bad==expected_bad
    (target/'seed.edges').write_text('60 240\n'+''.join(f'{u} {v}\n' for u,v in new_edges))
    dump(target/'seed.json',dict(n=60,edges=new_edges,original_source=str(path.relative_to(ROOT)),
                               coordinates='vertex 5*a+t, a in 0..11, t in Z5'))
    dump(target/'automorphism.json',dict(permutation=permutation,cycles=orbit_vertices,
        old_to_new=[relabel[v] for v in range(60)],order=5,semiregular=True,
        checked_original_edge_images=240,exact_reconstruction=True))
    dump(target/'palette.json',dict(orbit_count=354,orbits=catalog))
    dump(target/'voltages.json',dict(source=str(path.relative_to(ROOT)),
        shifts=[[sorted(d) for d in row] for row in shifts],
        selected_orbit_indices=[item['index'] for item in selected],selected_orbits=48,
        quotient_weighted_degrees=[8]*12,missing_voltage_blocks=missing,
        bad_pairs=voltage_bad,bad_pair_count=len(voltage_bad),
        prior_independent_bfs=str(old_check.relative_to(ROOT)),
        voltage_bad_pairs_match_prior_independent_bfs=True))
    return dict(source=str(path.relative_to(ROOT)),automorphism_verified=True,cycle_type=[5]*12,
                palette_orbits=354,selected_orbits=48,bad_pairs=len(voltage_bad),
                missing_voltage_blocks=missing)


def main():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(10,11))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'diagnosis.json').exists(),'Single endpoint diagnostic only'
    path=BASE/'petersen_all_matchings_run/candidate.best.edges'
    old_check=path.with_name('candidate.best.verification.json')
    edges,adj=read_edges(path)
    checked=json.loads(old_check.read_text())
    bad_pairs={tuple(item['pair']) for item in checked['bad_pairs']}
    assert len(bad_pairs)==20
    endpoints=set(v for pair in bad_pairs for v in pair)
    assert len(endpoints)==20
    groups=defaultdict(list)
    for v in range(60):
        if v not in endpoints:groups[tuple(sorted(adj[v]&endpoints))].append(v)
    signature_sizes=Counter(len(s) for s in groups for v in groups[s])
    unique=len(groups)==40
    data=dict(source=str(path.relative_to(ROOT)),bad_endpoints=sorted(endpoints),
        bad_pairs=sorted(bad_pairs),induced_edges=sorted(e for e in edges if set(e)<=endpoints),
        remaining_vertices=40,signature_size_histogram=dict(signature_sizes),
        distinct_endpoint_neighbor_sets=len(groups),unique_lift_available=unique,
        signature_classes=[dict(endpoint_neighbors=s,vertices=vs) for s,vs in sorted(groups.items())],
        signature_multiplicity_histogram=dict(sorted(Counter(map(len,groups.values())).items())))
    dump(OUT/'endpoint_structure.json',data)
    found=None;enumerated=0;complete=False;budget_stop=False
    if unique:
        import networkx as nx
        graph=nx.Graph();graph.add_nodes_from(sorted(endpoints))
        for u,v in edges:
            if u in endpoints and v in endpoints:graph.add_edge(u,v,kind='adjacency')
        for u,v in bad_pairs:
            assert not graph.has_edge(u,v)
            graph.add_edge(u,v,kind='distance_greater_than_two')
        inverse={s:vs[0] for s,vs in groups.items()}
        signal.signal(signal.SIGPROF,alarm)
        signal.setitimer(signal.ITIMER_PROF,max(0.01,9-time.process_time()+START_CPU))
        try:
            for mapping in nx.algorithms.isomorphism.GraphMatcher(
                graph,graph,edge_match=lambda a,b:a['kind']==b['kind']).isomorphisms_iter():
                enumerated+=1;p=[-1]*60
                for v in endpoints:p[v]=mapping[v]
                for s,vs in groups.items():
                    image=tuple(sorted(mapping[v] for v in s))
                    if image not in inverse:break
                    p[vs[0]]=inverse[image]
                else:
                    if all(len(c)==5 for c in cycles(p)) and {
                        tuple(sorted((p[u],p[v]))) for u,v in edges}==edges:
                        found=p;break
            else:complete=True
        except BudgetStop:budget_stop=True
        finally:signal.setitimer(signal.ITIMER_PROF,0)
    report=dict(source20=str(path.relative_to(ROOT)),unique_lift_available=unique,
        signature_classes=len(groups),signature_multiplicities=data['signature_multiplicity_histogram'],
        colored_endpoint_automorphisms_enumerated=enumerated,enumeration_complete=complete,
        budget_stop=budget_stop,found_order5=found is not None,
        status20=('found' if found is not None else 'unique_lift_not_available' if not unique
                  else 'complete_no_order5' if complete else 'unknown_budget'),
        complete_fullgraph_nonexistence_claim=False)
    if found is not None:
        report['seed20_voltage']=export_voltage('seed20',path,edges,found,bad_pairs,old_check)

    # Read the different, previously verified 50-bad seed with its actual symmetry.
    fifty=BASE/'petersen_six_fibers.best.edges'
    fifty_check=fifty.with_suffix('.verification.json')
    fifty_edges,_=read_edges(fifty)
    old=json.loads(fifty_check.read_text())
    assert old['uncovered_pair_count']==50 and old['c5_automorphism_verified']
    sigma=[10*((u//10+1)%5)+u%10 if u<50 else
           50+(u%5+1)%5+5*(u%10//5) for u in range(60)]
    fifty_bad={(item['u'],item['v']) for item in old['uncovered_pairs']}
    report['seed50_voltage']=export_voltage('seed50',fifty,fifty_edges,sigma,fifty_bad,fifty_check)
    report.update(cpu_budget_seconds=10,cpu_seconds=time.process_time()-START_CPU,
        wall_seconds=time.monotonic()-START_WALL,solver_calls=0,optimization_calls=0,full_bfs_reruns=0)
    dump(OUT/'diagnosis.json',report)
    print(json.dumps(report),flush=True)


if __name__=='__main__':main()
