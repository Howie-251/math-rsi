"""One bounded exact endpoint-relation and four-vertex-class lifting test."""
from pathlib import Path
from itertools import permutations
from collections import Counter, deque
from math import lcm
import json
import os
import resource
import signal
import time
import networkx as nx
import cyclic5_twelve_orbits60_endpoint_diagnose as helper

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
OUT = BASE/'cyclic5_twelve_orbits60_signature_lift_run'


class BudgetStop(Exception):
    pass


def stop(*_):
    raise BudgetStop


def dump(name, data):
    (OUT/name).write_text(json.dumps(data, indent=2)+'\n')


def cycle_type(mapping):
    todo = set(mapping)
    sizes = []
    while todo:
        first = min(todo)
        x, size = first, 0
        while x in todo:
            todo.remove(x); size += 1; x = mapping[x]
        assert x == first
        sizes.append(size)
    return sorted(sizes)


def main():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'result.json').exists(), 'One signature-lift episode only'
    data = json.loads((BASE/'cyclic5_twelve_orbits60_endpoint_run/endpoint_structure.json').read_text())
    source = ROOT/data['source']
    edges, adj = helper.read_edges(source)
    endpoints = set(data['bad_endpoints'])
    bad_pairs = {tuple(p) for p in data['bad_pairs']}
    assert {tuple(e) for e in data['induced_edges']} == {e for e in edges if set(e) <= endpoints}
    prior = json.loads(source.with_name('candidate.best.verification.json').read_text())
    assert bad_pairs == {tuple(x['pair']) for x in prior['bad_pairs']}
    classes = [c['vertices'] for c in data['signature_classes']]
    signatures = [tuple(c['endpoint_neighbors']) for c in data['signature_classes']]
    assert len(classes) == 10 and all(len(c) == 4 for c in classes)
    assert sorted(x for sig in signatures for x in sig) == sorted(endpoints)
    assert sorted(v for c in classes for v in c) == sorted(set(range(60))-endpoints)
    for c, sig in zip(classes, signatures):
        assert all(tuple(sorted(adj[v]&endpoints)) == sig for v in c)
    internal = [sorted(e for e in edges if set(e) <= set(c)) for c in classes]
    maps = {}
    interfaces = []
    quotient = nx.Graph()
    quotient.add_nodes_from(range(10))
    all_matching = True
    for a in range(10):
        for b in range(a+1, 10):
            rows = [[int(v in adj[u]) for v in classes[b]] for u in classes[a]]
            count = sum(map(sum, rows))
            if not count:
                continue
            matching = count == 4 and all(sum(r) == 1 for r in rows) and all(
                sum(rows[i][j] for i in range(4)) == 1 for j in range(4))
            interfaces.append(dict(a=a,b=b,matrix=rows,edges=count,perfect_matching=matching))
            quotient.add_edge(a,b)
            all_matching &= matching
            if matching:
                maps[a,b] = {u:next(v for v in classes[b] if v in adj[u]) for u in classes[a]}
                maps[b,a] = {v:u for u,v in maps[a,b].items()}
    connected = nx.is_connected(quotient)
    structure = dict(signature_classes=data['signature_classes'],internal_edges=internal,
        nonempty_interfaces=interfaces,quotient_edges=sorted(quotient.edges()),
        quotient_degrees=[quotient.degree(a) for a in range(10)],
        all_nonempty_interfaces_perfect_matching=all_matching,quotient_connected=connected)
    dump('interface_structure.json',structure)
    report = dict(source=data['source'],all_nonempty_interfaces_perfect_matching=all_matching,
        quotient_connected=connected,endpoint_automorphisms=0,endpoint_order5_candidates=0,
        class_order5_candidates=0,root_bijections_tested=0,successful_lifts=0,
        enumeration_complete=False,budget_stop=False,found_semiregular_order5=False,
        solver_calls=0,optimization_calls=0,full_bfs_reruns=0)
    if not all_matching or not connected:
        report['status'] = 'requires_general_class_CSP'
        report['CSP'] = 'Each class has 24 bijections to its prescribed image; retain exactly those pairs preserving every saved 4x4 interface and internal edges.'
    else:
        relation = nx.Graph()
        relation.add_nodes_from(sorted(endpoints))
        for bit, pairs in [(1,data['induced_edges']),(2,data['bad_pairs']),(4,signatures)]:
            for u,v in pairs:
                old = relation.get_edge_data(u,v,{}).get('kind',0)
                relation.add_edge(u,v,kind=old|bit)
        inverse_signature = {s:i for i,s in enumerate(signatures)}
        candidates = []
        found = None
        failure_counts = Counter()
        signal.signal(signal.SIGPROF,stop)
        signal.setitimer(signal.ITIMER_PROF,max(0.01,9.4-time.process_time()))
        try:
            iterator = nx.algorithms.isomorphism.GraphMatcher(relation,relation,
                edge_match=lambda a,b:a['kind']==b['kind']).isomorphisms_iter()
            for sigma in iterator:
                report['endpoint_automorphisms'] += 1
                if cycle_type(sigma) != [5]*4:
                    continue
                report['endpoint_order5_candidates'] += 1
                pi = {i:inverse_signature[tuple(sorted(sigma[x] for x in s))]
                      for i,s in enumerate(signatures)}
                if cycle_type(pi) != [5]*2:
                    continue
                report['class_order5_candidates'] += 1
                item = dict(endpoint_image=[sigma[x] for x in sorted(endpoints)],
                            class_image=[pi[i] for i in range(10)],failures=[])
                candidates.append(item)
                if any((pi[a],pi[b]) not in maps for a,b in quotient.edges()):
                    item['quotient_mismatch'] = True
                    failure_counts['quotient_mismatch'] += 1
                    continue
                for image in permutations(classes[pi[0]]):
                    report['root_bijections_tested'] += 1
                    lifted = {0:dict(zip(classes[0],image))}
                    queue = deque([0])
                    failure = None
                    while queue and failure is None:
                        a = queue.popleft()
                        for b in quotient.neighbors(a):
                            transported = {maps[a,b][u]:maps[pi[a],pi[b]][lifted[a][u]]
                                           for u in classes[a]}
                            if b in lifted:
                                if transported != lifted[b]:
                                    first = next(x for x in classes[b] if transported[x] != lifted[b][x])
                                    failure = dict(kind='propagation_conflict',a=a,b=b,vertex=first,
                                        previously=lifted[b][first],transported=transported[first])
                                    break
                            else:
                                lifted[b] = transported
                                queue.append(b)
                    if failure:
                        item['failures'].append(dict(root_image=image,**failure))
                        failure_counts[failure['kind']] += 1
                        continue
                    assert len(lifted) == 10
                    p = dict(sigma)
                    for mapping in lifted.values():
                        p.update(mapping)
                    assert sorted(p.values()) == list(range(60))
                    if {tuple(sorted((p[u],p[v]))) for u,v in edges} != edges:
                        item['failures'].append(dict(root_image=image,kind='full_edge_check'))
                        failure_counts['full_edge_check'] += 1
                        continue
                    report['successful_lifts'] += 1
                    lengths = cycle_type(p)
                    order = lcm(*lengths)
                    assert order % 5 == 0 and (order//5) % 5 != 0
                    found = []
                    for x in range(60):
                        for _ in range(order//5):
                            x = p[x]
                        found.append(x)
                    assert cycle_type(dict(enumerate(found))) == [5]*12
                    assert {tuple(sorted((found[u],found[v]))) for u,v in edges} == edges
                    item['success'] = dict(root_image=image,lift_cycle_type=lengths,
                                           power_used=order//5,original_lift=[p[x] for x in range(60)])
                    break
                if found is not None:
                    break
            else:
                report['enumeration_complete'] = True
        except BudgetStop:
            report['budget_stop'] = True
        finally:
            signal.setitimer(signal.ITIMER_PROF,0)
        dump('endpoint_candidates.json',candidates)
        report['failure_counts'] = dict(failure_counts)
        report['found_semiregular_order5'] = found is not None
        if found is not None:
            helper.OUT = OUT
            report['voltage_export'] = helper.export_voltage('seed20',source,edges,found,bad_pairs,
                source.with_name('candidate.best.verification.json'))
            report['status'] = 'verified_order5_and_full_voltage_export'
        else:
            report['status'] = 'complete_no_semiregular_order5' if report['enumeration_complete'] else 'unknown_budget'
    report.update(cpu_seconds=time.process_time()-start_cpu,
        wall_seconds=time.monotonic()-start_wall,cpu_budget_seconds=10,
        process_cpu_seconds=time.process_time())
    dump('result.json',report)
    print(json.dumps(report),flush=True)


if __name__ == '__main__':
    main()
