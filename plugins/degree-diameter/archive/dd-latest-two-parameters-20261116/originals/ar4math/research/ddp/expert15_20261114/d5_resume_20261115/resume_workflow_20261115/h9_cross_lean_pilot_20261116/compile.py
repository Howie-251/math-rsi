from pathlib import Path
import os,json,resource,subprocess,time,math
P=Path(__file__).resolve().parent;N=P.parent;AR=P.parents[5]
origin=(N/'H9_CROSS_LEAN_PILOT_TASK.txt').stat().st_mtime
prior=json.loads((P/'PREFLIGHT.json').read_text())['child_CPU']+json.loads((P/'GENERATION_RESULT.json').read_text())['CPU']
r0=resource.getrusage(resource.RUSAGE_CHILDREN);c0=time.process_time();wall=time.monotonic();result={}
cmd=[str(AR/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-M2048','DegreeDiameter/Portfolio/H9CrossRouting.lean','-o',str(P/'H9CrossRouting.olean')]
try:
 lp=json.loads((AR/'research/ddp/expert15_20261114/d5_resume_20261115/d12_n42403/formal/BUILD_ATTEMPT_2.json').read_text())['LEAN_PATH']
 remaining=180-(time.time()-origin)
 if remaining<=0:raise TimeoutError('original180wall elapsed before compile')
 def limits():
  z=max(1,math.floor(30-prior));resource.setrlimit(resource.RLIMIT_CPU,(z,z));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 (P/'RUN_HANDLE.json').write_text(json.dumps({'running':True,'pid':os.getpid(),'command':cmd})+'\n')
 with(P/'BUILD.log').open('w')as f:r=subprocess.run(cmd,cwd=AR/'formal',stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=remaining,env={**os.environ,'LEAN_PATH':lp})
 result={'status':'COMPILED_KERNEL_MODULE'if r.returncode==0 else'BUILD_FAILED','exit_code':r.returncode,'command':cmd,'LEAN_PATH':lp}
except Exception as e:result={'status':'UNKNOWN_OR_TOOL_ERROR','error':str(e),'command':cmd}
finally:
 r=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime+time.process_time()-c0
 result.update(compile_CPU=cpu,total_measured_CPU=prior+cpu,compile_wall=time.monotonic()-wall,wall_since_parent_task=time.time()-origin,CPU_cap=30,wall_cap=180,running=False,concrete_graph_Lean_closed=False,new_graphs=0)
 (P/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RUN_HANDLE.json').write_text(json.dumps({'running':False,'status':result['status']})+'\n');print(json.dumps(result),flush=True)
