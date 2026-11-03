"""One ordered batch: p17 mixed, p29 mixed, p29 both; cumulative 120 CPU seconds."""
from pathlib import Path
import json
import math
import os
import resource
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
SOURCE = PARENT / 'p13_mixed_search'
CPU_BUDGET = 120.0
CASES = [(17,24,2,'mixed'), (29,12,12,'mixed'), (29,12,12,'both')]


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    started_cpu, started_children = time.process_time(), child_cpu()
    def used_cpu():
        return time.process_time()-started_cpu+child_cpu()-started_children
    affinity = min(os.sched_getaffinity(0))
    os.sched_setaffinity(0, {affinity})
    shutil.copyfile(SOURCE / 'search_reflections.cpp', HERE / 'search_reflections.cpp')
    shutil.copy2(SOURCE / 'search_reflections', HERE / 'search_reflections')
    exe = HERE / 'search_reflections'
    metadata = json.loads((PARENT / 'profile_metadata.json').read_text())
    scope = []
    for p,m,r,kind in CASES:
        case = next(c for c in metadata['cases'] if (c['p'],c['m'],c['r'])==(p,m,r))
        branch = case['branches'][kind]
        skel = PARENT / branch['skeleton_file']
        lines = skel.read_text().splitlines()
        rows = [list(map(int,line.split())) for line in lines[1:]]
        assert int(lines[0]) == len(rows) == branch['summary']['affine_form_capacity_survivors']
        assert rows == branch['summary']['survivor_quotients']
        legal = 0
        for beta,s,t in rows:
            assert 0 <= s <= t < m and math.gcd(math.gcd(math.gcd(m,m//2),beta),math.gcd(s,t))==1
            assert (kind=='mixed' and 0 <= beta < m//2) or (kind=='both' and beta==m//2)
            cross = ((p-1)*(p-2) if s==t==0 else p*(p-1) if s==0 or s==t else p*p)
            internal = ((p-1 if beta==0 else p) if kind=='mixed' else p*(p-1))
            legal += cross*internal
        variables = 3 if kind=='mixed' else 4
        assert len(rows)*p**variables == branch['summary']['survivor_raw_translation_assignments']
        assert legal == branch['summary']['survivor_legal_translation_assignments']
        scope.append(dict(p=p,m=m,r=r,n=2*p*m,kind=kind,
            skeletons=len(rows),skeleton_file=str(skel),coordinate_order=metadata['coordinate_order'][kind],
            expected_raw=len(rows)*p**variables,expected_legal=legal,
            full_coordinate_domain=f'F_{p}^{variables}, including all zero coordinates',
            further_symmetry_reduction=False,compatible_quotient_units=case['compatible_quotient_units']))
    assert sum(c['expected_raw'] for c in scope)==3332186
    assert sum(c['expected_legal'] for c in scope)==3273316
    (HERE / 'scope.json').write_text(json.dumps(dict(cases=scope,
        cumulative_cpu_limit_seconds=CPU_BUDGET,workers=1,stop_on_first_D5=True,
        implementation='Unchanged executable and source from the completed p13 nonfaithful run; no recompile or repeated regression',
        prior_preflight='../p13_mixed_search/preflight.json'),indent=2)+'\n')
    terminal = dict(status='RUNNING',scope=scope,branches=[],cumulative_cpu_limit_seconds=CPU_BUDGET,
                    workers=1,cpu_used_seconds=used_cpu(),next_branch=0)
    def save_terminal():
        terminal['cpu_used_seconds']=used_cpu()
        (HERE / 'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
    save_terminal()
    for idx, case in enumerate(scope):
        remaining = CPU_BUDGET-used_cpu()
        if remaining <= 1.0:
            terminal['status']='CPU_BUDGET_EXHAUSTED'
            terminal['next_branch']=idx
            break
        p,m,r,kind = case['p'],case['m'],case['r'],case['kind']
        directory = HERE / f'p{p}_{kind}'
        directory.mkdir(exist_ok=True)
        prefix = directory / 'search'
        # Half a second covers the engine's <=1024-assignment timer interval.
        engine_limit = remaining-0.5
        command=[str(exe),kind,str(p),str(m),str(r),case['skeleton_file'],str(engine_limit),str(prefix),'0','1','0']
        def child_limits():
            os.sched_setaffinity(0,{affinity})
            resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(remaining),math.ceil(remaining)))
        before=child_cpu()
        wall=time.monotonic()
        print(json.dumps(dict(event='START',branch=idx,p=p,kind=kind,
                              expected_raw=case['expected_raw'],remaining_cpu_seconds=remaining)),flush=True)
        with (directory / 'run.log').open('w') as log:
            proc=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=child_limits)
        runtime=dict(command=command,returncode=proc.returncode,cpu_seconds=child_cpu()-before,
                     wall_seconds=time.monotonic()-wall,engine_cpu_limit_seconds=engine_limit)
        if proc.returncode:
            terminal['status']='EXECUTION_ERROR'
            terminal['branches'].append(dict(case=case,runtime=runtime))
            terminal['next_branch']=idx
            save_terminal()
            raise RuntimeError(f'branch {idx} returned {proc.returncode}; no restart')
        summary=json.loads(prefix.with_suffix('.summary.json').read_text())
        best=json.loads(prefix.with_suffix('.best.json').read_text())
        records=[json.loads(line) for line in prefix.with_suffix('.skeleton_results.jsonl').read_text().splitlines()]
        assert sum(row['raw_visited'] for row in records)==summary['raw_visited']
        assert sum(row['legal_fully_scored'] for row in records)==summary['legal_fully_scored']
        assert sum(summary['score_histogram'].values())==summary['legal_fully_scored']
        if summary['skeletons_completed']==case['skeletons']:
            assert summary['raw_visited']==case['expected_raw']
            assert summary['legal_fully_scored']==case['expected_legal']
            assert summary['illegal_rejected']==case['expected_raw']-case['expected_legal']
        branch_terminal=dict(case=case,runtime=runtime,summary=summary,best=best,
            best_edges='search.best.edges',independent_all_source_check='pending',
            cursor=dict(skeleton_id=summary['next_skeleton_id'],assignment_index=summary['next_assignment_index']))
        (directory / 'terminal.json').write_text(json.dumps(branch_terminal,indent=2)+'\n')
        terminal['branches'].append(dict(directory=directory.name,**branch_terminal))
        terminal['next_branch']=idx+1
        save_terminal()
        print(json.dumps(dict(event='DONE',p=p,kind=kind,status=summary['status'],
            raw=summary['raw_visited'],legal=summary['legal_fully_scored'],best=best,
            cpu_seconds=runtime['cpu_seconds'],cumulative_cpu_seconds=used_cpu())),flush=True)
        if summary['minimum_missing_seen']==0:
            terminal['status']='CANDIDATE_COVERED_STOPPED_REMAINING_BRANCHES'
            break
        if summary['skeletons_completed']!=case['skeletons']:
            terminal['status']='CPU_BUDGET_EXHAUSTED'
            terminal['next_branch']=idx
            break
    else:
        terminal['status']='COMPLETE_NO_SOLUTION'
    save_terminal()
    print(json.dumps(dict(event='TERMINAL',status=terminal['status'],cpu_seconds=used_cpu(),
                          branches_run=len(terminal['branches']),next_branch=terminal['next_branch'])),flush=True)


if __name__ == '__main__':
    main()
