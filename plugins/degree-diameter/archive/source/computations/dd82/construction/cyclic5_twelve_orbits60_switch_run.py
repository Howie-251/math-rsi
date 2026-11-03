"""Compile and execute one deterministic bounded C5 orbit-switch descent."""
from collections import Counter
from pathlib import Path
import json
import os
import resource
import subprocess
import time

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'computations/dd82/construction'
OUT=BASE/'cyclic5_twelve_orbits60_switch_run'
SEED=BASE/'cyclic5_twelve_orbits60_endpoint_run/seed50'


def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')


def children_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def main():
    start=time.monotonic();parent_cpu=time.process_time();child_start=children_cpu()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'launch.json').exists(),'Exactly one descent episode'
    palette=json.loads((SEED/'palette.json').read_text())['orbits']
    assert len(palette)==354 and sum(o['selected'] for o in palette)==48
    input_file=OUT/'input.txt'
    input_file.write_text('354 48\n'+''.join(f"{o['index']} {o['a']} {o['b']} {o['shift']} {int(o['selected'])}\n" for o in palette))
    dump(OUT/'launch.json',dict(source=str(SEED.relative_to(ROOT)),total_cpu_budget_seconds=30,
        search_episodes=1,random_restarts=0,neutral_moves=False,quotient_hard_filters=False))
    before=children_cpu()
    compiled=subprocess.run(['g++','-O3','-std=c++17',str(BASE/'cyclic5_twelve_orbits60_switch.cpp'),
                             '-o',str(BASE/'cyclic5_twelve_orbits60_switch.bin')],capture_output=True,text=True)
    compile_cpu=children_cpu()-before
    (OUT/'compile.log').write_text(compiled.stdout+compiled.stderr)
    assert compiled.returncode==0
    # Include compilation and reserve CPU for saving and the final independent BFS.
    search_budget=max(0.1,29.0-compile_cpu-(time.process_time()-parent_cpu))
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(search_budget)+1),max(2,int(search_budget)+2)))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    before=children_cpu()
    with (OUT/'search.log').open('w') as log:
        run=subprocess.run([str(BASE/'cyclic5_twelve_orbits60_switch.bin'),str(input_file),str(OUT),str(search_budget)],
                           stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
    process_cpu=children_cpu()-before
    assert run.returncode==0
    search=json.loads((OUT/'search.json').read_text())
    final=json.loads((OUT/'candidate.best.json').read_text())
    # Existing checker reads only the complete final graph and performs all-source BFS.
    before=children_cpu()
    checked=subprocess.run(['python',str(BASE/'verify_hs_candidate.py'),str(OUT/'candidate.best.json')],
                           capture_output=True,text=True)
    bfs_cpu=children_cpu()-before
    (OUT/'verification.log').write_text(checked.stdout+checked.stderr)
    assert checked.returncode==0
    verification=json.loads((OUT/'candidate.best.verification.json').read_text())
    assert verification['bad_pair_count']==final['bad_pairs_exact']==search['best_bad_pairs']
    assert verification['n']==60 and verification['edges']==240 and verification['degrees']==[8]*60
    # Record departure from the original six-fibre restrictions in old labels.
    permutation=json.loads((SEED/'automorphism.json').read_text())['old_to_new']
    inverse={new:old for old,new in enumerate(permutation)}
    old_edges={tuple(sorted((inverse[u],inverse[v]))) for u,v in final['edges']}
    original_path=BASE/'petersen_six_fibers.best.edges'
    original={tuple(map(int,line.split())) for line in original_path.read_text().splitlines()[1:]}
    adj=[set() for _ in range(60)]
    for u,v in old_edges:adj[u].add(v);adj[v].add(u)
    fibres=[]
    for f in range(6):
        inside=lambda edge:edge[0]//10==f and edge[1]//10==f
        before_edges={e for e in original if inside(e)};after_edges={e for e in old_edges if inside(e)}
        fibres.append(dict(fibre=f,internal_edge_count=len(after_edges),
            internal_degree_histogram=dict(Counter(sum(v//10==f for v in adj[u]) for u in range(10*f,10*f+10))),
            original_internal_edges_removed=sorted(before_edges-after_edges),
            new_internal_edges=sorted(after_edges-before_edges)))
    cross=[]
    for f in range(6):
        for g in range(f+1,6):
            left=[sum(v//10==g for v in adj[u]) for u in range(10*f,10*f+10)]
            right=[sum(v//10==f for v in adj[u]) for u in range(10*g,10*g+10)]
            if left!=[1]*10 or right!=[1]*10:cross.append(dict(fibres=[f,g],left_degrees=left,right_degrees=right))
    structure=dict(fibres=fibres,nonmatching_original_interfaces=cross,
        left_original_six_petersen_model=bool(cross or any(f['original_internal_edges_removed'] or f['new_internal_edges'] for f in fibres)),
        bad_pairs_by_cyclic_orbit_pair=dict(Counter(f"{item['pair'][0]//5},{item['pair'][1]//5}" for item in verification['bad_pairs'])),
        bad_pairs_by_original_fibre_pair=dict(Counter(','.join(map(str,sorted((inverse[item['pair'][0]]//10,inverse[item['pair'][1]]//10)))) for item in verification['bad_pairs'])))
    dump(OUT/'final.structure.json',structure)
    result=dict(compile_cpu_seconds=compile_cpu,search_process_cpu_seconds=process_cpu,
        independent_bfs_cpu_seconds=bfs_cpu,parent_cpu_seconds=time.process_time()-parent_cpu,
        total_cpu_seconds=children_cpu()-child_start+time.process_time()-parent_cpu,
        wall_seconds=time.monotonic()-start,total_cpu_budget_seconds=30,search=search,
        verification={k:verification[k] for k in ['n','edges','max_degree','bad_pair_count','diameter','valid_target']},
        left_original_six_petersen_model=structure['left_original_six_petersen_model'])
    dump(OUT/'resources.json',result);print(json.dumps(result),flush=True)


if __name__=='__main__':main()
