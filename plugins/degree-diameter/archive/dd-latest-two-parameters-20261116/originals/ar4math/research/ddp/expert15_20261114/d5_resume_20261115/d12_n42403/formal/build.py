from pathlib import Path
import json,os,resource,subprocess,time
P=Path(__file__).resolve().parent
AR=next(x for x in P.parents if x.name=='ar4math');BIN=AR/'.tools/lean-4.24.0-linux/bin';ROOT=AR/'formal'
st=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
def limits():
 resource.setrlimit(resource.RLIMIT_CPU,(24,24));resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
if(P/'BUILD_RESULT.json').exists():
 i=1
 while(P/f'BUILD_ATTEMPT_{i}.json').exists():i+=1
 (P/'BUILD_RESULT.json').rename(P/f'BUILD_ATTEMPT_{i}.json')
 (P/'BUILD.log').rename(P/f'BUILD_ATTEMPT_{i}.log')
paths=[ROOT/'.lake/build/lib/lean',*sorted((ROOT/'.lake/packages').glob('*/.lake/build/lib/lean'))]
cmd=[str(BIN/'lean'),'-j1','-M2048',str(P/'D12N42403Increment.lean'),'-o',str(P/'D12N42403Increment.olean')]
env={**os.environ,'PATH':str(BIN)+':'+os.environ.get('PATH',''),'LEAN_PATH':':'.join(map(str,paths))}
with(P/'BUILD.log').open('w')as out:r=subprocess.run(cmd,cwd=P,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits,env=env)
after=resource.getrusage(resource.RUSAGE_CHILDREN);used=time.process_time()-st+after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
result={'status':'CONDITIONAL_INCREMENT_COMPILED'if r.returncode==0 else'BUILD_FAILED','exit_code':r.returncode,'CPU_seconds':used,'command':cmd,'LEAN_PATH':env['LEAN_PATH'],'source_D5_formal_instance_inherited':False,'actual_R4_Lean_certificate_closed':False,'complete_actual_graph_Lean_certification':False,'no_new_source_formalization':True}
(P/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
