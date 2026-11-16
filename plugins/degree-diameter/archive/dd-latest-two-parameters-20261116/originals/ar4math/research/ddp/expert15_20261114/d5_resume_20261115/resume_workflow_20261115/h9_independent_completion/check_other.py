"""One cached-geometry binding plus existing raw161root checker, total4CPU."""
from array import array
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
RUN=HERE.parent
SOURCE=RUN/'h9_exact_binding'
AUTHOR=RUN/'h9_other_orientation'
OUT=HERE/'other37632'


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(4,4))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    start=time.process_time();wall=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    def used():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
    OUT.mkdir(exist_ok=False)
    def binary(path,kind):
        a=array(kind);a.frombytes(path.read_bytes());return a
    n=66430;tau=binary(SOURCE/'tau.i32.bin','i');pi=binary(SOURCE/'pi.u16.bin','H')
    lines=binary(SOURCE/'line_points.i32.bin','i');sigma=binary(AUTHOR/'sigma.i32.bin','i')
    eps=(AUTHOR/'eps.u8.bin').read_bytes();c=json.loads((AUTHOR/'CANDIDATE.json').read_text())
    assert len(tau)==2*n and len(pi)==len(sigma)==len(eps)==n and len(lines)==10*n
    tinv=[0]*(2*n)
    for u,v in enumerate(tau):tinv[v]=u
    assert len(set(sigma))==n and min(sigma)==n and max(sigma)==2*n-1
    assert all(eps[p]in(0,1) and eps[p]==eps[tau[tau[p]]]for p in range(n))
    assert all(sigma[p]==(tau[p]if eps[p]else tinv[p])for p in range(n))
    assert all(eps[p]==0 for p in range(n)if p!=tau[tau[p]] and pi[p]==pi[tau[tau[p]]])
    expected=set()
    for p in range(n):
        l=sigma[p]-n
        for q in lines[10*l:10*l+10]:
            u,v=pi[p],pi[q]
            if p!=q:assert u!=v,'forbidden mergedfiber edge'
            if u!=v:expected.add((min(u,v),max(u,v)))
    actual_core=set();outside=set();newpins=[]
    with(AUTHOR/'candidate37632.edges').open()as f:
        actual_n,actual_m=map(int,next(f).split());assert(actual_n,actual_m)==(37632,205365)
        for row in f:
            u,v=map(int,row.split());u,v=min(u,v),max(u,v)
            if v<37471:actual_core.add((u,v))
            elif v==37631:newpins.append(u)
            else:outside.add((u,v))
    assert expected==actual_core and len(expected)==203747
    oldoutside=set()
    with(SOURCE/'source.edges').open()as f:
        next(f)
        for row in f:
            u,v=map(int,row.split());u,v=min(u,v),max(u,v)
            if v>=37471:oldoutside.add((u,v))
    assert outside==oldoutside and len(outside)==1608
    assert sorted(newpins)==sorted(c['pins']) and len(newpins)==10
    binding=dict(status='INDEPENDENT_CACHED_TRUE_GEOMETRY_SIGMA_LITERAL_BINDING_PASS',
                 sigma_bijection=True,eps_phi_constant=True,merged_eps_zero=True,
                 actual_core_edges=len(actual_core),actual_core_exact_match=True,
                 actual_outside_edges=len(outside),outside_exact_old_match=True,new_pins_exact=True,
                 geometry_scope='Reused already Root-bound trueH9 incidence/tau/pi; no geometry rebuild.',
                 core_D5_scope='Same actual classicalH9 plus arbitrarysigma/partialfold theorem; sourceLean remains open.',
                 CPU_seconds=time.process_time()-start)
    (OUT/'BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
    (OUT/'PINS.txt').write_text(str(len(newpins))+'\n'+' '.join(map(str,sorted(newpins)))+'\n')
    # Release finite reconstruction sets before the distance child.
    del expected,actual_core,outside,oldoutside
    rem=4-used();assert rem>0.25
    def limits():
        sec=max(1,math.ceil(rem));resource.setrlimit(resource.RLIMIT_CPU,(sec,sec))
        resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
        resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    with(OUT/'CHECK.log').open('w')as log:
        subprocess.run([str(HERE/'canonical37632/check'),str(AUTHOR/'candidate37632.edges'),str(OUT),str(OUT/'PINS.txt'),str(rem-0.25)],
                       check=True,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=30)
    result=json.loads((OUT/'RAW_CHECK_RESULT.json').read_text())
    result.update(graph=str(AUTHOR/'candidate37632.edges'),binding=binding,
                  whole_CPU=used(),whole_wall=time.monotonic()-wall,whole_CPU_cap=4,
                  rebuilt_geometry=False,compiler_runs=0,source_Lean_closed=False)
    (OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
