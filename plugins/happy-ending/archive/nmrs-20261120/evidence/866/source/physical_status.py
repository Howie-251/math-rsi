"""Read-only live pipeline/solver/checker state with bounded output."""
import json
from pathlib import Path
import platform
import time

assert platform.system()=='Linux'
HERE=Path(__file__).resolve().parent
OUT=HERE/'h13-physical-all02'


def command(pid):
    try:
        return Path(f'/proc/{pid}/cmdline').read_bytes().replace(b'\0',b' ').decode()
    except FileNotFoundError:
        return None


def tail(path):
    if not path.exists():
        return None
    with path.open('rb') as source:
        source.seek(max(0,path.stat().st_size-2000))
        return source.read().decode(errors='replace')[-1600:]


result={}
if (HERE/'physical-preparation.json').exists():
    result['preparation']=json.loads((HERE/'physical-preparation.json').read_text())
    result['preparation']['live_cmdline']=command(result['preparation']['pid'])
    if result['preparation']['steps']:
        step=result['preparation']['steps'][-1]
        step['live_cmdline']=command(step['pid'])
        result['phase_log_tail']=tail(HERE/step['script'].replace('.py','.log'))
if (OUT/'progress.json').exists():
    progress=json.loads((OUT/'progress.json').read_text())
    result['query']={k:v for k,v in progress.items() if k not in ['command']}
    result['query']['live_process_cmdline']=command(progress['process_pid'])
    result['query']['elapsed_seconds']=round(time.time()-progress['started_unix'],2)
    result['solver_log_tail']=tail(OUT/'solver.log')
    result['checker_log_tail']=tail(OUT/'checker.log')
if (OUT/'formula.cnf').exists():
    result['cnf_bytes_now']=(OUT/'formula.cnf').stat().st_size
if (OUT/'extension.cnf').exists():
    result['extension_bytes_now']=(OUT/'extension.cnf').stat().st_size
if (OUT/'proof.drat').exists():
    result['proof_bytes_now']=(OUT/'proof.drat').stat().st_size
print(json.dumps(result),flush=True)
