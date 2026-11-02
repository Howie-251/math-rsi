"""One bounded complete CRT-phase batch following the actual capacity gate."""
import json
from pathlib import Path
import resource
import subprocess
from time import process_time,perf_counter

root=Path(__file__).resolve().parent
assert not (root/'RESULT.json').exists(),'This one-shot batch already completed.'
capacity=json.loads((root/'CAPACITY_RESULT.json').read_text())
start=process_time();wall=perf_counter();receipts=[]
# Reuse the literal step/export functions, without the former random generator.
source=(root.parent/'m33_global_batch/search.cpp').read_text()
prefix=source[:source.index('int main(')].replace('#include <random>\n','')
prefix=prefix.replace('constexpr uint64_t SEED=2026110107ULL, MAXIMUM=2000000;\n','')
(root/'phase_cube.cpp').write_text(prefix+'\n'+(root/'phase_main.inc').read_text())
with (root/'PROFILES.tsv').open('w')as f:
    f.write('profile\tcapacity_pass\ta0\ta1\ta2\ta3\tsigma01\tsigma23\ttau02\ttau13\trho03\trho12\n')
    for p in capacity['profiles']:
        f.write('\t'.join(map(str,[p['profile'],int(p['capacity_pass']),*p['fixed_parameters_mod11']]))+'\n')
def child_run(name,args,limit=None):
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=perf_counter()
    def cap():
        seconds=max(1,int(limit));resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    with (root/(name+'.stdout')).open('w')as out,(root/(name+'.stderr')).open('w')as err:
        try:r=subprocess.run(args,cwd=root,stdout=out,stderr=err,preexec_fn=cap if limit else None,timeout=40);code=r.returncode
        except subprocess.TimeoutExpired:code='wall_timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    receipts.append({'stage':name,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':perf_counter()-t})
    return code
code=child_run('compile',['g++','-O3','-std=c++17','phase_cube.cpp','-o','phase_cube'])
if code==0:
    used=capacity['CPU_seconds']+sum(r['CPU_seconds']for r in receipts)+process_time()-start
    remaining=20-used
    assert remaining>1
    code=child_run('phase_cube',['./phase_cube',str(remaining-0.5)],remaining)
    if code==0:result=json.loads((root/'phase_cube.stdout').read_text())
    else:result={'status':'UNKNOWN_PROCESS_STOP','found':False,'whole_family_excluded':False,'three_fixed_profiles_complete':False}
else:result={'status':'COMPILE_FAILED','found':False,'whole_family_excluded':False,'three_fixed_profiles_complete':False}
result.update({'capacity_CPU_seconds':capacity['CPU_seconds'],'receipts':receipts,
               'wrapper_CPU_seconds':process_time()-start,
               'accounted_CPU_seconds':capacity['CPU_seconds']+sum(r['CPU_seconds']for r in receipts)+process_time()-start,
               'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':20,'workers':1,
               'running':False,'active_processes':[]})
if (root/'PHASE_ATTEMPTS.bin').exists():
    actual=(root/'PHASE_ATTEMPTS.bin').stat().st_size;result['actual_attempt_file_bytes']=actual
    if code==0:assert actual==result['recorded_attempt_bytes']
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
