"""One capped quotient profile; assign arbitrary legal voltages only afterward."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'computations/dd82/construction'
OUT=BASE/'cyclic5_four_orbit_quotient_run'
SEED=BASE/'cyclic5_twelve_orbits60_signature_lift_run/seed20'


def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')


def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime


def main():
    wall=time.monotonic();start=time.process_time();children=child_cpu()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'launch.json').exists(),'Only one quotient profile episode'
    palette=json.loads((SEED/'palette.json').read_text())['orbits']
    selected=[o for o in palette if o['selected']]
    assert len(selected)==48 and sum(o['a']==o['b'] for o in selected)==12
    input_file=OUT/'input.txt'
    input_file.write_text('48\n'+''.join(f"{o['index']} {o['a']} {o['b']} {o['shift']}\n" for o in selected))
    dump(OUT/'launch.json',dict(source=str(SEED.relative_to(ROOT)),total_cpu_budget_seconds=10,
        expected_deletion_sets=49995,expected_parameter_choices=5249475,
        voltage_search=False,solver_calls=0,profile_episodes=1))
    before=child_cpu()
    compiled=subprocess.run(['g++','-O3','-std=c++17',str(BASE/'cyclic5_four_orbit_quotient_profile.cpp'),
                             '-o',str(BASE/'cyclic5_four_orbit_quotient_profile.bin')],capture_output=True,text=True)
    compile_cpu=child_cpu()-before
    (OUT/'compile.log').write_text(compiled.stdout+compiled.stderr)
    assert compiled.returncode==0
    budget=max(0.1,9.0-compile_cpu-(time.process_time()-start))
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(budget)+1),max(2,int(budget)+2)))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    before=child_cpu()
    with (OUT/'profile.log').open('w') as log:
        run=subprocess.run([str(BASE/'cyclic5_four_orbit_quotient_profile.bin'),str(input_file),
                            str(OUT/'profile.json'),str(budget)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
    profile_process_cpu=child_cpu()-before
    assert run.returncode==0
    profile=json.loads((OUT/'profile.json').read_text())
    if profile['complete']:
        assert profile['deletion_sets_finished']==49995 and profile['raw_pairing_choices']==5249475
    by_pair={}
    for o in palette:by_pair.setdefault((o['a'],o['b']),[]).append(o)
    original_ids={o['index'] for o in selected}
    saved_graphs=[];bfs_cpu=0;verification=None
    for number,item in enumerate(profile['saved_distinct_matrices']):
        ids=original_ids-set(item['removed_orbit_ids']);added_ids=[]
        for a,b in item['added_quotient_edges']:
            choices=[o for o in by_pair[(a,b)] if o['index'] not in ids]
            assert choices
            choice=choices[0];ids.add(choice['index']);added_ids.append(choice['index'])
        assert len(ids)==48
        edges=set();matrix=[[0]*12 for _ in range(12)]
        for index in sorted(ids):
            o=palette[index];assert o['index']==index
            a,b,d=o['a'],o['b'],o['shift']
            matrix[a][b]+=1;matrix[b][a]+=1
            for t in range(5):edges.add(tuple(sorted((5*a+t,5*b+(t+d)%5))))
        assert matrix==item['matrix'] and len(edges)==240
        degree=[0]*60
        for u,v in edges:degree[u]+=1;degree[v]+=1
        assert degree==[8]*60
        graph_path=OUT/f'candidate{number:02d}.json'
        graph=dict(n=60,edges=sorted(edges),matrix=matrix,removed_orbit_ids=item['removed_orbit_ids'],
            added_orbit_ids=added_ids,selected_orbit_ids=sorted(ids),
            selected_parameters=[{k:palette[index][k] for k in ['index','a','b','shift']} for index in sorted(ids)],
            voltage_rule='First available shift on each added quotient pair; no voltage search')
        dump(graph_path,graph)
        graph_path.with_suffix('.edges').write_text('60 240\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
        saved_graphs.append(str(graph_path.relative_to(ROOT)))
        if number==0:
            before=child_cpu()
            check=subprocess.run(['python',str(BASE/'verify_hs_candidate.py'),str(graph_path)],capture_output=True,text=True)
            bfs_cpu=child_cpu()-before
            (OUT/'verification.log').write_text(check.stdout+check.stderr)
            assert check.returncode==0
            verification=json.loads(graph_path.with_suffix('.verification.json').read_text())
    result=dict(compile_cpu_seconds=compile_cpu,profile_process_cpu_seconds=profile_process_cpu,
        independent_bfs_cpu_seconds=bfs_cpu,parent_cpu_seconds=time.process_time()-start,
        total_cpu_seconds=child_cpu()-children+time.process_time()-start,wall_seconds=time.monotonic()-wall,
        total_cpu_budget_seconds=10,complete=profile['complete'],saved_full_graphs=saved_graphs,
        voltage_search=False,solver_calls=0,
        first_graph_verification=None if verification is None else {k:verification[k] for k in
            ['n','edges','max_degree','bad_pair_count','diameter','valid_target']})
    dump(OUT/'resources.json',result);print(json.dumps(dict(resources=result,profile=profile)),flush=True)


if __name__=='__main__':main()
