from pathlib import Path
import json,math,os,resource,shutil,subprocess,sys,time
P=Path(__file__).resolve().parent;G=P.parent;D=G/'current_graph_data';J=G/'joint_cover'
def cc():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def lim(seconds):
 def apply():
  s=max(1,math.ceil(seconds));resource.setrlimit(resource.RLIMIT_CPU,(s,s));resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 return apply
def main():
 assert not(P/'RUN_HANDLE.json').exists(),'Single authorized frontier probe only.'
 start=time.process_time();c0=cc();wall=time.monotonic();used=lambda:time.process_time()-start+cc()-c0
 def run(cmd,log,seconds):
  with(P/log).open('w')as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=lim(seconds),env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'})
  if r.returncode:raise RuntimeError(f'{log} exit{r.returncode}')
 run(['g++','-O3','-std=c++17',str(P/'frontier.cpp'),'-o',str(P/'frontier')],'COMPILE.log',20-used())
 run([str(P/'frontier'),'--control'],'CONTROL.log',20-used())
 shutil.copyfile(J/'verify.py',P/'verify.py')
 remaining=20-used()-1.5
 assert remaining>0 and time.monotonic()-wall<300
 with(P/'NATIVE.log').open('w')as f:
  proc=subprocess.Popen([str(P/'frontier'),str(P),str(J),str(D),str(remaining)],stdout=f,stderr=subprocess.STDOUT,preexec_fn=lim(remaining+0.4))
  (P/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_SINGLE_FRONTIER_PROBE','driver_pid':os.getpid(),'native_pid':proc.pid,'native_CPU_limit':remaining,'whole_CPU_limit':20,'no_followup_authorized':True})+'\n');proc.wait(timeout=max(1,350-(time.monotonic()-wall)))
 if proc.returncode:raise RuntimeError(f'native exit{proc.returncode}; retain logs')
 result=json.loads((P/'NATIVE_RESULT.json').read_text())
 if result['status']=='COMPLETE_PROVIDER_COVER_FOUND':
  run([sys.executable,str(P/'verify.py')],'VERIFY.log',20-used())
  verification=json.loads((P/'VERIFICATION.json').read_text());result['verification']=verification;result['actual_R4_checks']=1;result['status']=verification['status']
 result.update(whole_CPU=used(),whole_wall=time.monotonic()-wall,whole_CPU_limit=20,followup_authorized=False)
 assert result['whole_CPU']<=20,result['whole_CPU']
 (P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RUN_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','running':False,'result':'RESULT.json'})+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
