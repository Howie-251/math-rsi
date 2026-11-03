"""Bounded joint-boundary target actions; no automatic solve retries."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
prior = ROOT / 'computations/dd82/n61/adjacent_double_full61_run/runner.py'
spec = importlib.util.spec_from_file_location('prior_bounded_process', prior)
process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process)
# Reuse only the generic bounded subprocess function, not historical actions.
process.OUTPUT_BYTES = 1024**3

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--case', choices=('n58', 'n60'), required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--solver-cpu', type=int, default=300)
    parser.add_argument('--solver-wall', type=int, default=360)
    args = parser.parse_args()
    out = HERE / args.case
    out.mkdir(exist_ok=True)
    def bounded(cmd, name, cpu, wall, cap=False):
        return process.bounded(cmd, out / name, cpu, wall, args.cpu, cap_files=cap)
    if args.action == 'prepare':
        assert not (out / 'preparation_process.json').exists()
        r = bounded([sys.executable, str(HERE / 'encode.py'), 'prepare', '--case', args.case], 'prepare.log', 30, 45)
        r['status'] = 'PREPARED_NOT_RUN' if r['exit_code'] == 0 else 'PREPARATION_FAILED'
        r['solver_calls'] = 0
        save(out / 'preparation_process.json', r)
    elif args.action == 'solve':
        assert 3 <= args.solver_cpu <= 300 and 5 <= args.solver_wall <= 360
        assert not (out / 'launch.json').exists() and not (out / 'solver.log').exists()
        assert not (out / 'proof.lrat').exists()
        enc = json.loads((out / 'encoding.json').read_text())
        assert enc['status'] == 'PREPARED_NOT_RUN' and enc['n'] == int(args.case[1:])
        assert os.access(process.SOLVER, os.X_OK)
        cmd = [str(process.SOLVER), '--lrat', '-t', str(args.solver_cpu - 2), str(out / 'input.cnf'), str(out / 'proof.lrat')]
        save(out / 'launch.json', dict(status='LAUNCHED', command=cmd, scope=enc['scope'], solver_calls=1,
             cpu_affinity=[args.cpu], solver_os_cpu_limit_seconds=args.solver_cpu,
             solver_soft_time_seconds=args.solver_cpu-2, solver_wall_limit_seconds=args.solver_wall,
             memory_limit_bytes=process.MEMORY_BYTES, per_file_limit_bytes=process.OUTPUT_BYTES,
             retained_internal_solver_state=False, automatic_restarts=0))
        r = bounded(cmd, 'solver.log', args.solver_cpu, args.solver_wall, True)
        status = {10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-signal.SIGXFSZ:'OUTPUT_LIMIT_UNKNOWN',
                  -signal.SIGKILL:'KILLED_UNKNOWN',-signal.SIGXCPU:'CPU_LIMIT_UNKNOWN'}.get(r['exit_code'],'PROCESS_FAILURE_UNKNOWN')
        if r['wall_timeout']:status='WALL_LIMIT_UNKNOWN'
        r.update(status=status, scope=enc['scope'], n=enc['n'], variables=enc['variables'], clauses=enc['clauses'],
                 solver_calls=1, proof_checked=False, retained_internal_solver_state=False,
                 proof_bytes=(out/'proof.lrat').stat().st_size if (out/'proof.lrat').exists() else 0)
        save(out / 'result.json', r)
        if status == 'SAT_CANDIDATE':
            r['decode_process'] = bounded([sys.executable, str(HERE/'encode.py'),'decode','--case',args.case], 'decode.log', 10, 15)
            if r['decode_process']['exit_code'] != 0:
                r['status']='SAT_DECODE_CHECK_FAILED'
            else:
                r['independent_bfs_process']=bounded([sys.executable,str(process.BFS),str(out/'candidate.json')], 'independent_bfs.log',10,15)
                if r['independent_bfs_process']['exit_code'] != 0:
                    r['status']='SAT_BFS_CHECK_FAILED'
                else:
                    g=json.loads((out/'candidate.verification.json').read_text());n=enc['n']
                    r['independent_graph_check']=g
                    valid=(g['valid_target'] and g['n']==n and g['edges']==4*n and g['degrees']==[8]*n
                           and g['bad_pair_count']==0 and g['diameter'] is not None and g['diameter']<=2)
                    r['status']='VERIFIED_TARGET' if valid else 'SAT_FAILED_TARGET_CHECK'
        r['mathematical_conclusion'] = ('A complete independently verified target graph was found.' if r['status']=='VERIFIED_TARGET'
            else 'No exclusion until exact-input certificate check and domain coverage review.' if r['status']=='RAW_UNSAT'
            else 'No accepted target or exclusion; UNKNOWN does not exclude even this anchored domain.')
        save(out / 'result.json', r)
    else:
        assert not (out/'certificate_check.json').exists()
        r=json.loads((out/'result.json').read_text())
        assert r['status']=='RAW_UNSAT' and r['exit_code']==20
        assert (out/'proof.lrat').stat().st_size>0 and os.access(process.CHECKER,os.X_OK)
        c=bounded([str(process.CHECKER),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')], 'certificate_check.log',90,120)
        verified=c['exit_code']==20 and not c['wall_timeout'] and any(line.strip()=='s VERIFIED' for line in (out/'certificate_check.log').open())
        c.update(verified=verified,scope='Exact saved anchored input only.')
        save(out/'certificate_check.json',c)
        r.update(proof_checked=verified,certificate_check=c,status='CHECKED_UNSAT_ANCHORED_DOMAIN' if verified else 'RAW_UNSAT')
        r['mathematical_conclusion']=('Exact saved anchored CNF has a checked contradiction; whole-order exclusion is NOT implied.' if verified else 'No checked exclusion.')
        save(out/'result.json',r)
    print(json.dumps(r,indent=2),flush=True)

if __name__=='__main__':main()
