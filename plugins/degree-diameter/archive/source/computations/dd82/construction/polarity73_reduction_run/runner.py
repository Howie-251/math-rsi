"""One bounded variable-deletion screen profile; never a complete graph solver."""
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
spec = importlib.util.spec_from_file_location('polarity73_bounded_process', prior)
process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process)
# Only use the generic resource limiter, never the historical entry points.
process.OUTPUT_BYTES = 256 * 1024**2

def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--n', type=int, choices=(58,59), required=True)
    parser.add_argument('--cpu', type=int, required=True)
    args = parser.parse_args()
    out = HERE / f'n{args.n}'
    out.mkdir(exist_ok=True)
    def bounded(command, logfile, cpu, wall, cap=False):
        return process.bounded(command, out/logfile, cpu, wall, args.cpu, cap_files=cap)
    if args.action == 'prepare':
        assert not (out/'preparation_process.json').exists()
        result = bounded([sys.executable, str(HERE/'screen.py'), 'prepare', '--n', str(args.n)],
                         'prepare.log', 20, 30)
        result.update(status='PREPARED_NOT_RUN' if result['exit_code']==0 else 'PREPARATION_FAILED',
                      solver_calls=0)
        save(out/'preparation_process.json', result)
    elif args.action == 'solve':
        assert not any((out/name).exists() for name in ('launch.json','solver.log','proof.lrat'))
        encoding = json.loads((out/'encoding.json').read_text())
        assert encoding['status']=='PREPARED_NOT_RUN' and encoding['n']==args.n
        assert os.access(process.SOLVER, os.X_OK)
        command = [str(process.SOLVER), '--lrat', '-t', '28',
                   str(out/'input.cnf'), str(out/'proof.lrat')]
        save(out/'launch.json',dict(status='LAUNCHED',command=command,scope=encoding['scope'],
             solver_calls=1,solver_os_cpu_limit_seconds=30,solver_soft_time_seconds=28,
             solver_wall_limit_seconds=45,cpu_affinity=[args.cpu],memory_limit_bytes=process.MEMORY_BYTES,
             per_file_limit_bytes=process.OUTPUT_BYTES,retained_internal_solver_state=False,
             automatic_restarts=0,complete_graph_solver=False))
        result = bounded(command,'solver.log',30,45,True)
        status = {10:'SCREEN_SAT_PENDING_DECODE',20:'RAW_UNSAT',0:'UNKNOWN',
                  -signal.SIGXFSZ:'OUTPUT_LIMIT_UNKNOWN',-signal.SIGXCPU:'CPU_LIMIT_UNKNOWN',
                  -signal.SIGKILL:'KILLED_UNKNOWN'}.get(result['exit_code'],'PROCESS_FAILURE_UNKNOWN')
        if result['wall_timeout']:
            status='WALL_LIMIT_UNKNOWN'
        result.update(status=status,n=args.n,scope=encoding['scope'],solver_calls=1,
                      variables=encoding['variables'],clauses=encoding['clauses'],proof_checked=False,
                      proof_bytes=(out/'proof.lrat').stat().st_size if (out/'proof.lrat').exists() else 0,
                      retained_internal_solver_state=False,complete_graph_constructed=False)
        save(out/'result.json',result)
        if status=='SCREEN_SAT_PENDING_DECODE':
            result['decode_process']=bounded(
                [sys.executable,str(HERE/'screen.py'),'decode','--n',str(args.n)],'decode.log',10,15)
            result['status']=('SCREEN_SAT_CHECKED' if result['decode_process']['exit_code']==0
                              else 'SCREEN_SAT_DECODE_CHECK_FAILED')
            if result['status']=='SCREEN_SAT_CHECKED':
                result['deletion_candidate_path']=str((out/'deletion_candidate.json').relative_to(ROOT))
        result['mathematical_conclusion']=(
            'Necessary deletion screen is satisfiable; a deletion pattern is not a completed target graph.'
            if result['status']=='SCREEN_SAT_CHECKED' else
            'No exclusion until exact-input certificate check and coverage justification.'
            if result['status']=='RAW_UNSAT' else
            'No completed target or checked exclusion; this screen remains undecided or needs correction.')
        save(out/'result.json',result)
    else:
        assert not (out/'certificate_check.json').exists()
        result=json.loads((out/'result.json').read_text())
        assert result['status']=='RAW_UNSAT' and result['exit_code']==20
        assert os.access(process.CHECKER,os.X_OK) and (out/'proof.lrat').stat().st_size>0
        checked=bounded([str(process.CHECKER),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')],
                        'certificate_check.log',90,120)
        valid=(checked['exit_code']==20 and not checked['wall_timeout'] and
               any(line.strip()=='s VERIFIED' for line in (out/'certificate_check.log').open()))
        checked.update(verified=valid,scope='Only the saved variable-deletion necessary-condition screen')
        save(out/'certificate_check.json',checked)
        result.update(status='CHECKED_UNSAT_SCREEN' if valid else 'RAW_UNSAT',
                      proof_checked=valid,certificate_check=checked)
        result['mathematical_conclusion']=(
            'The exact necessary deletion screen is contradictory; reduction/source completeness is needed '
            'to exclude this monotone polarity family, never the whole graph order.'
            if valid else 'No checked exclusion.')
        save(out/'result.json',result)
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    main()

