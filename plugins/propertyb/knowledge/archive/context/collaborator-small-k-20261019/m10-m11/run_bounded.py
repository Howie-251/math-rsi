"""Bounded replay; never starts a second child after the 45-second budget."""
import os,sys,time,subprocess,resource,json
from pathlib import Path
base=Path(__file__).resolve().parent
start=time.monotonic();results=[]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
for k in (10,11):
    remain=45-(time.monotonic()-start)
    if remain<=0:break
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    t=time.monotonic()
    try:
        p=subprocess.run([sys.executable,str(base/'propertyB_k10_k11_verified.py'),str(k)],cwd=base,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=remain)
        out,status=p.stdout,str(p.returncode)
    except subprocess.TimeoutExpired as e:
        out=e.stdout or b''
        if isinstance(out,bytes):out=out.decode(errors='replace')
        status='timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    (base/f'LOCAL_REPLAY_K{k}.log').write_text(out)
    results.append(dict(k=k,status=status,wall_seconds=time.monotonic()-t,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime))
    if status!='0':break
summary=dict(results=results,total_wall_seconds=time.monotonic()-start,numpy_threads=1,budget_wall_seconds=45)
(base/'LOCAL_REPLAY_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
