"""Run only after the parent authorizes the single prepared4096 batch."""
from pathlib import Path
import subprocess,sys,time,resource,math
out=Path(__file__).resolve().parent

def cpu_children():
 c=resource.getrusage(resource.RUSAGE_CHILDREN);return c.ru_utime+c.ru_stime

def cap(n):
 def setcap():resource.setrlimit(resource.RLIMIT_CPU,(n,n))
 return setcap

def main():
 import json
 start=time.process_time();c0=cpu_children()
 with (out/'compile.log').open('w') as log:
  cp=subprocess.run(['g++','-O3','-std=c++17',str(out/'producer.cpp'),'-o',str(out/'producer')],stdout=log,stderr=subprocess.STDOUT,timeout=30,preexec_fn=cap(5))
 compileCPU=cpu_children()-c0;hard=math.floor(15-compileCPU-(time.process_time()-start)-.5)
 if cp.returncode!=0 or hard<1:
  result={'status':'COMPILE_ERROR_OR_NO_NATIVE_BUDGET','compile_exit_code':cp.returncode,'actual_global_D':None}
 else:
  with (out/'worker.log').open('w') as log:
   run=subprocess.run([str(out/'producer'),str(out),str(max(.05,hard-.2)),str(hard)],stdout=log,stderr=subprocess.STDOUT,timeout=60,preexec_fn=cap(hard))
  if run.returncode==0:result=json.loads((out/'NATIVE_RESULT.json').read_text())
  else:
   result={'status':'UNKNOWN_NATIVE_LIMIT_OR_ERROR','native_exit_code':run.returncode,'actual_global_D':None}
   if(out/'checkpoint.json').exists():result['last_checkpoint']=json.loads((out/'checkpoint.json').read_text())
 result['execution_receipt']={'aggregate_CPU_budget_seconds':15,'compiler_process_CPU_seconds':compileCPU,'child_process_CPU_seconds':cpu_children()-c0,'driver_CPU_seconds':time.process_time()-start,'workers':1,'live_handle':None}
 for name in ['RESULT.json','terminal.json']:(out/name).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
