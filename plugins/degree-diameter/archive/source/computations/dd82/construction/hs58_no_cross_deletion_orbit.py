#!/usr/bin/env python3
"""Bounded explicit automorphisms and their orbit on induced two-edge matchings."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json
import signal
import sys
import time

import networkx as nx
from hs_augmentation import base


class CPUStop(Exception):
    pass


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=True)
    assert not (out/'result.json').exists(), 'One bounded attempt; no unchanged rerun'
    start_cpu, start_wall = time.process_time(), time.monotonic()
    edges, ns = base()
    edge_set = set(edges)
    edge_id = {e:i for i,e in enumerate(edges)}
    m = len(edges)
    seed_edges = ((0,1),(10,11))
    seed = tuple(sorted(edge_id[e] for e in seed_edges))
    domain = set()
    counts = Counter()
    for i,j in combinations(range(m),2):
        e,f = edges[i],edges[j]
        if set(e)&set(f):
            counts['adjacent_deletions'] += 1
        elif any(b in ns[a] for a in e for b in f):
            counts['disjoint_with_Q_cross_edge'] += 1
        else:
            counts['disjoint_without_Q_cross_edge'] += 1
            domain.add((i,j))
    assert seed in domain
    generators, edge_actions, searches = [], [], []
    states = [seed]
    index = {seed:0}
    tree = [dict(parent=None,generator=None)]
    closed = True

    def save(stop_reason):
        complete = set(states) == domain and closed
        (out/'generators.json').write_text(json.dumps(dict(
            n=50,HS_edges=edges,generators=generators),indent=2)+'\n')
        (out/'orbit.json').write_text(json.dumps(dict(
            seed_deletions=seed_edges,
            states=[dict(deletions=[edges[i],edges[j]],**tree[k])
                    for k,(i,j) in enumerate(states)]),indent=2)+'\n')
        report = dict(complete=complete,stop_reason=stop_reason,
            scope='All unordered pairs of disjoint HS edges with no Q cross-edge between their endpoints.',
            direct_domain_counts=dict(counts),direct_domain_size=len(domain),
            visited_orbit_size=len(states),missing_domain_size=len(domain-set(states)),
            every_orbit_member_in_domain=set(states)<=domain,
            orbit_closed_under_all_generators=closed,generator_count=len(generators),
            networkx_searches=searches,cpu_seconds=time.process_time()-start_cpu,
            wall_seconds=time.monotonic()-start_wall,
            full_automorphism_group_computed=False,external_orbit_classification_used=False)
        (out/'result.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2),flush=True)

    def install(name,p):
        nonlocal closed
        assert sorted(p)==list(range(50))
        images={tuple(sorted((p[u],p[v]))) for u,v in edges}
        assert images==edge_set
        gid=len(generators)
        generators.append(dict(name=name,permutation=p,bijection_verified=True,
            image_edge_set_equals_Q=True,checked_original_edges=len(edges)))
        action=[edge_id[tuple(sorted((p[u],p[v])))] for u,v in edges]
        edge_actions.append(action)
        closed=False

        def visit(parent,g):
            i,j=states[parent]
            image=tuple(sorted((edge_actions[g][i],edge_actions[g][j])))
            assert image in domain
            if image not in index:
                index[image]=len(states)
                states.append(image)
                tree.append(dict(parent=parent,generator=g))

        previous=len(states)
        for k in range(previous):
            visit(k,gid)
        cursor=previous
        while cursor<len(states):
            for g in range(len(generators)):
                visit(cursor,g)
            cursor+=1
        closed=True

    def coordinates(kind):
        p=[]
        for v in range(50):
            side=int(v>=25)
            i,j=divmod(v-25*side,5)
            if kind=='common_translation':
                p.append(25*side+5*i+(j+1)%5)
            elif kind=='U_track_translation':
                p.append(5*((i+1)%5)+j if side==0 else 25+5*i+(j+i)%5)
            elif kind=='V_track_translation':
                p.append(5*i+(j-i)%5 if side==0 else 25+5*((i+1)%5)+j)
            elif kind=='inverse_track_scaling':
                p.append(25*side+5*((2 if side==0 else 3)*i%5)+j)
            elif kind=='side_exchange':
                p.append(25+5*i+(2*j)%5 if side==0 else 5*((3*i)%5)+(2*j)%5)
            else:
                raise ValueError(kind)
        return p

    def pinned_graph(pins):
        graph=nx.Graph()
        order=list(pins)+[v for v in range(50) if v not in pins]
        for v in order:
            color=tuple(0 if v==w else (1 if w in ns[v] else 2) for w in pins)
            graph.add_node(v,color=color)
        graph.add_edges_from(edges)
        return graph

    def stop_signal(signum,frame):
        raise CPUStop()

    signal.signal(signal.SIGPROF,stop_signal)
    # Leave time inside the external ten-second CPU cap to save a partial orbit.
    signal.setitimer(signal.ITIMER_PROF,8.8)
    reason='not_started'
    try:
        for name in ['common_translation','U_track_translation','V_track_translation',
                     'inverse_track_scaling','side_exchange']:
            install(name,coordinates(name))
        source_pins=(0,1,10,11)
        source=pinned_graph(source_pins)
        while set(states)!=domain:
            target=min(domain-set(states))
            e,f=edges[target[0]],edges[target[1]]
            found=False
            for swap,flip0,flip1 in product(range(2),repeat=3):
                a,b=(f,e) if swap else (e,f)
                pins=tuple(a[::(-1 if flip0 else 1)]+b[::(-1 if flip1 else 1)])
                record=dict(target_deletions=[e,f],source_pins=source_pins,target_pins=pins,
                            found=False,finished=False)
                searches.append(record)
                call_start=time.process_time()
                matcher=nx.algorithms.isomorphism.GraphMatcher(
                    source,pinned_graph(pins),node_match=lambda a,b:a['color']==b['color'])
                mapping=next(matcher.isomorphisms_iter(),None)
                record.update(finished=True,found=mapping is not None,
                              cpu_seconds=time.process_time()-call_start)
                if mapping is not None:
                    p=[mapping[v] for v in range(50)]
                    assert all(p[u]==v for u,v in zip(source_pins,pins))
                    install('targeted_automorphism_'+str(len(searches)),p)
                    found=True
                    break
            if not found:
                reason='all_eight_endpoint_orientations_exhausted_for_uncovered_pair'
                break
        else:
            reason='entire_direct_domain_is_one_verified_generator_orbit'
    except CPUStop:
        reason='bounded_cpu_stop_partial_orbit'
    finally:
        signal.setitimer(signal.ITIMER_PROF,0)
    save(reason)


if __name__=='__main__':
    main()
