#!/usr/bin/env python3
"""Reuse every short source path; no main graph generation or source BFS."""
import json
from pathlib import Path
import resource
import subprocess
import time

resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
assert not (HERE / "MATCHING_RESULT.json").exists(), "fixed matching gate already finished"
START = time.process_time()
data = json.loads((HERE / "PUBLISHED_K64.json").read_text())
G = [set(row) for row in data["adjacency"]]
extras = [tuple(sorted(edge)) for edge in data["extra_edges"]]
extra_index = {edge:i for i,edge in enumerate(extras)}
assert len(G) == 64 and len(extras) == 96
assert all(len(row)==6 and u not in row for u,row in enumerate(G))
assert all(u in G[v] for u,row in enumerate(G) for v in row)
assert all((u ^ bit) in G[u] for u in range(64) for bit in (1,2,4))
paths = {(u,v):[] for u in range(64) for v in range(u+1,64)}
path_count = 0
for root in range(64):
    def visit(sequence, mask):
        global path_count
        u = sequence[-1]
        if u > root:
            paths[(root,u)].append(mask)
            path_count += 1
        if len(sequence) == 4:
            return
        for v in G[u]:
            if v in sequence:
                continue
            edge = tuple(sorted((u,v)))
            index = extra_index.get(edge)
            visit(sequence+[v], mask | (0 if index is None else 1 << index))
    visit([root],0)
assert all(paths.values()), "published source was not actually D3"
critical = {}
for pair, masks in paths.items():
    intersection = masks[0]
    for mask in masks[1:]:
        intersection &= mask
    for i,edge in enumerate(extras):
        if intersection >> i & 1:
            critical.setdefault(i,dict(edge=edge, pair=pair, all_path_extra_masks=[str(x) for x in masks]))
blocked = []
for u in range(64):
    incident = [i for i,edge in enumerate(extras) if u in edge]
    assert len(incident)==3
    if all(i in critical for i in incident):
        blocked.append(u)
(HERE / "CRITICAL_EXTRA_EDGES.json").write_text(json.dumps(list(critical.values()),indent=2)+'\n')
out = dict(status="CRITICAL_VERTEX_BLOCKS_PUBLISHED_MATCHING" if blocked else "CRITICAL_GATE_PASSED", source_n=64,
           source_m=192, source_degree=6, source_short_simple_paths=path_count,
           source_all_pairs_have_path_at_most3=True, source_main1088_BFS=0,
           removable_domain_extra_edges=96, D3_critical_extra_edges=len(critical),
           vertices_with_all_three_extra_edges_critical=blocked, solver_calls=0,
           auxiliary_positive_graphs=0, main1088_graphs=0)
if not blocked:
    clauses=[]
    variable=96
    for u in range(64):
        incident=[i+1 for i,e in enumerate(extras) if u in e]
        clauses.append(incident)
        for j in range(3):
            for k in range(j+1,3):
                clauses.append([-incident[j],-incident[k]])
    for i in critical:
        clauses.append([-i-1])
    for pair,masks in paths.items():
        if 0 in masks:
            continue
        survivors=[]
        for mask in set(masks):
            edge_vars=[i+1 for i in range(96) if mask>>i&1]
            if len(edge_vars)==1:
                survivors.append(-edge_vars[0])
            else:
                variable+=1
                q=variable
                survivors.append(q)
                for e in edge_vars:
                    clauses.append([-q,-e])
                clauses.append([q]+edge_vars)
        clauses.append(survivors)
    cnf=HERE/'matching.cnf'
    with cnf.open('w') as f:
        f.write(f'p cnf {variable} {len(clauses)}\n')
        for row in clauses:f.write(' '.join(map(str,row))+' 0\n')
    solver=PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(12,13))
    with (HERE/'matching_solver.stdout').open('w') as f:
        result=subprocess.run([str(solver),'-q','-t','10',str(cnf)],stdout=f,stderr=f,
                              preexec_fn=limits,timeout=15)
    out.update(solver_calls=1,solver_exit_code=result.returncode,
               status='RAW_MATCHING_UNSAT_UNCERTIFIED' if result.returncode==20 else 'MATCHING_UNKNOWN')
    if result.returncode==10:
        positive=set()
        for line in (HERE/'matching_solver.stdout').read_text().splitlines():
            if line.startswith('v '):positive.update(int(x) for x in line[2:].split() if int(x)>0)
        removed=[extras[i] for i in range(96) if i+1 in positive]
        assert len(removed)==32
        H=[set(row) for row in G]
        for u,v in removed:H[u].remove(v);H[v].remove(u)
        assert all(len(row)==5 for row in H)
        for root in range(64):
            reach={root}
            for _ in range(3):reach |= {v for u in list(reach) for v in H[u]}
            assert len(reach)==64
        (HERE/'HIT_K64.json').write_text(json.dumps(dict(adjacency=[sorted(row) for row in H],removed=removed),indent=2)+'\n')
        out.update(status='PUBLISHED_MATCHING_K64_D3_HIT',auxiliary_positive_graphs=1,main1088_graphs=0)
out['worker_CPU_seconds']=time.process_time()-START
(HERE/'MATCHING_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
(HERE/'MATCHING_TERMINAL.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
