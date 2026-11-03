"""Bounded full order61 internal-double cases; one solve per prepared input."""
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
# Reuse the generic process limiter, without any historical action.
process.OUTPUT_BYTES = 512 * 1024**2
CASES = {'r0_h1_b0':1086, 'r1_h0_b0':870, 'r2_h0_b1':800}

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare','solve','check'))
    parser.add_argument('--case', choices=tuple(CASES), required=True)
    parser.add_argument('--cpu', type=int, required=True)
    args = parser.parse_args()
    out = HERE / args.case
    out.mkdir(exist_ok=True)
    def bounded(cmd, name, cpu, wall, cap=False):
        return process.bounded(cmd, out/name, cpu, wall, args.cpu, cap_files=cap)
    if args.action == 'prepare':
        assert not (out/'preparation_process.json').exists()
        r = bounded([sys.executable,str(HERE/'encode.py'),'prepare','--case',args.case],
                    'prepare.log',30,45)
        r.update(status='PREPARED_NOT_RUN' if r['exit_code']==0 else 'PREPARATION_FAILED',solver_calls=0)
        save(out/'preparation_process.json',r)
    elif args.action == 'solve':
        assert not any((out/name).exists() for name in ('launch.json','solver.log','proof.lrat'))
        enc = json.loads((out/'encoding.json').read_text())
        assert enc['status']=='PREPARED_NOT_RUN' and enc['n']==61
        assert enc['primary_edge_variables']==CASES[args.case]
        assert os.access(process.SOLVER,os.X_OK)
        cmd=[str(process.SOLVER),'--lrat','-t','58',str(out/'input.cnf'),str(out/'proof.lrat')]
        save(out/'launch.json',dict(status='LAUNCHED',command=cmd,scope=enc['scope'],solver_calls=1,
             cpu_affinity=[args.cpu],solver_os_cpu_limit_seconds=60,solver_soft_time_seconds=58,
             solver_wall_limit_seconds=90,memory_limit_bytes=process.MEMORY_BYTES,
             per_file_limit_bytes=process.OUTPUT_BYTES,retained_internal_solver_state=False,automatic_restarts=0))
        r=bounded(cmd,'solver.log',60,90,True)
        status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-signal.SIGXFSZ:'OUTPUT_LIMIT_UNKNOWN',
                -signal.SIGKILL:'KILLED_UNKNOWN',-signal.SIGXCPU:'CPU_LIMIT_UNKNOWN'}.get(r['exit_code'],'PROCESS_FAILURE_UNKNOWN')
        if r['wall_timeout']:
            status='WALL_LIMIT_UNKNOWN'
        r.update(status=status,scope=enc['scope'],case=args.case,n=61,variables=enc['variables'],clauses=enc['clauses'],
                 solver_calls=1,proof_checked=False,retained_internal_solver_state=False,
                 proof_bytes=(out/'proof.lrat').stat().st_size if (out/'proof.lrat').exists() else 0)
        save(out/'result.json',r)
        if status=='SAT_CANDIDATE':
            r['decode_process']=bounded([sys.executable,str(HERE/'encode.py'),'decode','--case',args.case],'decode.log',10,15)
            if r['decode_process']['exit_code']!=0:
                r['status']='SAT_DECODE_CHECK_FAILED'
            else:
                r['independent_bfs_process']=bounded([sys.executable,str(process.BFS),str(out/'candidate.json')],
                                                     'independent_bfs.log',10,15)
                if r['independent_bfs_process']['exit_code']!=0:
                    r['status']='SAT_BFS_CHECK_FAILED'
                else:
                    g=json.loads((out/'candidate.verification.json').read_text())
                    r['independent_graph_check']=g
                    valid=(g['valid_target'] and g['n']==61 and g['edges']==244 and g['degrees']==[8]*61
                           and g['bad_pair_count']==0 and g['diameter'] is not None and g['diameter']<=2)
                    r['status']='VERIFIED_TARGET' if valid else 'SAT_FAILED_TARGET_CHECK'
        r['mathematical_conclusion']=(
            'A complete independently verified order61 target graph was found.' if r['status']=='VERIFIED_TARGET'
            else 'No exclusion until exact-input certificate check and full three-case coverage review.' if r['status']=='RAW_UNSAT'
            else 'No accepted target or exclusion; incomplete runs leave this case open.')
        save(out/'result.json',r)
    else:
        assert not (out/'certificate_check.json').exists()
        r=json.loads((out/'result.json').read_text())
        assert r['status']=='RAW_UNSAT' and r['exit_code']==20
        assert (out/'proof.lrat').stat().st_size>0 and os.access(process.CHECKER,os.X_OK)
        c=bounded([str(process.CHECKER),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')],
                  'certificate_check.log',90,120)
        verified=(c['exit_code']==20 and not c['wall_timeout']
                  and any(line.strip()=='s VERIFIED' for line in (out/'certificate_check.log').open()))
        c.update(verified=verified,scope='Exact saved internal-double case input only.')
        save(out/'certificate_check.json',c)
        r.update(proof_checked=verified,certificate_check=c,status='CHECKED_UNSAT_CASE' if verified else 'RAW_UNSAT')
        r['mathematical_conclusion']=(
            'Exact saved case CNF has a checked contradiction; not whole-order61 exclusion.' if verified
            else 'No checked exclusion.')
        save(out/'result.json',r)
    print(json.dumps(r,indent=2),flush=True)

if __name__=='__main__':
    main()

