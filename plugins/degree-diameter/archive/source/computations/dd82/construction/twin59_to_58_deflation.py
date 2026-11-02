#!/usr/bin/env python3
"""One complete new deflation experiment and one bounded order-58 neutral BFS."""
from pathlib import Path
import json,os,resource,subprocess,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin59_to_58_deflation_run'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(12,13))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def run(command,prefix):
    start=time.monotonic()
    with prefix.with_suffix('.log').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    result={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-start,
      'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,'threads':1}
    prefix.with_suffix('.resources.json').write_text(json.dumps(result,indent=2)+'\n')
    assert p.returncode==0
    print(prefix.with_suffix('.log').read_text().strip())
    return result
def main():
    OUT.mkdir(exist_ok=True)
    source=HERE/'twin59_nonworsening_levels_run/expanded_states.json'
    data=json.loads(source.read_text());assert data['n']==59 and len(data['states'])==24
    inputfile=OUT/'source_states.txt'
    with inputfile.open('w') as out:
        out.write('24\n')
        for state in data['states']:
            assert len(state['edges'])==236
            out.write(f"{state['node']} 59 236\n")
            for u,v in state['edges']:out.write(f'{u} {v}\n')
    resources=[run([str(HERE/'twin59_to_58_deflation.bin'),str(inputfile),str(OUT/'deflation')],OUT/'deflation')]
    report=json.loads((OUT/'deflation.json').read_text())
    if report['minimum_bad_pairs']:
        resources.append(run([str(HERE/'twin58_deflated_neutral_component.bin'),str(OUT/'deflation.best.edges'),str(OUT/'component')],OUT/'component'))
    total=sum(r['user_cpu_seconds']+r['system_cpu_seconds'] for r in resources)
    assert total<30
    (OUT/'resources.json').write_text(json.dumps({'source':str(source),'whole_experiment_cpu_seconds':total,'runs':resources},indent=2)+'\n')
    print(f'total experiment CPU {total:.6f} seconds')
if __name__=='__main__':main()
