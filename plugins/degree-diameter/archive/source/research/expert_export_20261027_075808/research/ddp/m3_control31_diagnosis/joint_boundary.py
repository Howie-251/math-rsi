"""Concrete next representation; constructs/checks a supplied boundary, never searches.

Eight ports, two attachments each, to eleven fixed external vertices. Target
multiplicities remain those of the saved graph, so all 31 degrees remain four.
"""
from pathlib import Path
from collections import Counter
import argparse,json

HERE=Path(__file__).resolve().parent


def make_spec():
    source=HERE.parent/'second_mechanism/control_unrestricted_n31.edges'
    rows=[tuple(map(int,l.split())) for l in source.read_text().splitlines()];n,m=rows[0]
    edges={tuple(sorted(e)) for e in rows[1:]};ports=[0,1,7,17,18,19,24,28]
    triangles=[{0,1,30},{11,18,19},{11,24,30},{7,17,28}]
    fixed_triangle_edges={tuple(sorted((u,v))) for t in triangles for u in t for v in t if u<v}
    variable={e for e in edges if (e[0] in ports or e[1] in ports) and e not in fixed_triangle_edges}
    assert len(variable)==16
    baseline={p:[] for p in ports};counts=Counter()
    for u,v in variable:
        if u in ports:p,t=u,v
        else:p,t=v,u
        assert t not in ports;baseline[p].append(t);counts[t]+=1
    assert all(len(v)==2 for v in baseline.values()) and len(counts)==11
    return dict(control_order=n,ports=ports,target_multiplicity=dict(sorted(counts.items())),
                fixed_edges=sorted(edges-variable),baseline_assignment={p:sorted(v) for p,v in baseline.items()},
                variable_edge_count=16,binary_entry_count=8*11,
                scope='only these 16 attachments change; all other 46 edges fixed; no existence claim')


def build(spec,assignment):
    assignment={int(p):list(map(int,ns)) for p,ns in assignment.items()}
    assert sorted(assignment)==spec['ports']
    targets={int(v):int(c) for v,c in spec['target_multiplicity'].items()}
    counts=Counter();edges={tuple(e) for e in spec['fixed_edges']}
    for p,ns in assignment.items():
        assert len(ns)==len(set(ns))==2 and all(t in targets for t in ns)
        for t in ns:
            edge=tuple(sorted((p,t)));assert edge not in edges;edges.add(edge);counts[t]+=1
    assert dict(counts)==targets
    n=spec['control_order'];adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert len(edges)==62 and all(len(a)==4 for a in adj)
    missing=[]
    for s in range(n):
        reached={t for a in adj[s] for b in adj[a] for t in adj[b]}
        missing.extend([s,t] for t in range(n) if t not in reached)
    return edges,missing


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--assignment',type=Path);p.add_argument('--output',type=Path)
    args=p.parse_args();spec=make_spec();(HERE/'joint_boundary_spec.json').write_text(json.dumps(spec,indent=2)+'\n')
    assignment=json.loads(args.assignment.read_text()) if args.assignment else spec['baseline_assignment']
    edges,missing=build(spec,assignment)
    if args.output:args.output.write_text('31 62\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
    print(json.dumps(dict(status='provided_assignment_checked_no_search',ports=spec['ports'],
                         targets=spec['target_multiplicity'],zero_count=len(missing),zero_pairs=missing)))
