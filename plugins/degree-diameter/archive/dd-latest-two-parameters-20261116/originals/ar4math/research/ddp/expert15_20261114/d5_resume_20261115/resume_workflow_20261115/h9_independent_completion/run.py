"""Raw161-root verification; run only after inspecting the true-core binding.

The mathematical binding is read by the verifier agent, not inferred from an
artifact's mere existence. This driver preserves the cited original and reports
raw checks separately; it never declares the conditional core proof closed.
"""
import argparse
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--binding-artifact',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if not a.graph.is_file() or not a.binding_artifact.is_file():
        raise ValueError('actual graph and independently inspected binding original required')
    assert a.binding_artifact.stat().st_size>0
    c=json.loads(a.candidate.read_text());pins=c['pins']
    assert len(pins)==len(set(pins)) and len(pins)<=11
    out=a.output.resolve();out.mkdir(exist_ok=False,parents=True)
    start=time.process_time();wall=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    def used():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
    def run(cmd,log):
        rem=8-used();seconds=max(1,math.ceil(rem))
        if rem<=0:raise TimeoutError('whole independent8CPU budget exhausted')
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
            resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
            resource.setrlimit(resource.RLIMIT_CORE,(0,0))
        with(out/log).open('w') as f:
            subprocess.run(cmd,check=True,stdout=f,stderr=subprocess.STDOUT,
                           preexec_fn=limits,timeout=60)
    (out/'PINS.txt').write_text(str(len(pins))+'\n'+' '.join(map(str,pins))+'\n')
    metadata=dict(graph=str(a.graph.resolve()),candidate=str(a.candidate.resolve()),
                  binding_original=str(a.binding_artifact.resolve()),
                  binding_status='Must be independently read and connected by verifier; file presence is insufficient.',
                  source_Lean='Concrete sourceLean remains open; no Lean executed.',
                  CPU_cap=8,address_space_cap_bytes=512*1024**2)
    error=None
    try:
        binary=str(out/'check')
        run(['g++','-O2','-std=c++17',str(Path(__file__).with_name('check.cpp')),'-o',binary],'COMPILE.log')
        rem=8-used()-0.5
        if rem<=0:raise TimeoutError('compile used native budget')
        run([binary,str(a.graph.resolve()),str(out),str(out/'PINS.txt'),str(rem)],'CHECK.log')
        result=json.loads((out/'RAW_CHECK_RESULT.json').read_text())
    except (ValueError,OSError,TimeoutError,subprocess.SubprocessError) as exc:
        error=str(exc);result=dict(status='UNKNOWN_CHECK_PROCESS_OR_BUDGET',error=error)
    result.update(metadata,whole_CPU=used(),wall_seconds=time.monotonic()-wall,mathematical_acceptance='PENDING_VERIFIER_BINDING_REVIEW')
    (out/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if error:raise SystemExit(1)


if __name__=='__main__':main()
