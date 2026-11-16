from pathlib import Path
import array,json,math,os,resource,subprocess,time
P=Path(__file__).resolve().parent;R=P.parent;G=R/'d12_weighted_plane_cover'
def cc():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def limit(t):
 def apply():
  s=max(1,math.ceil(t));resource.setrlimit(resource.RLIMIT_CPU,(s,s));resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 return apply
def main():
 assert not(P/'RUN_HANDLE.json').exists(),'One finite continuation only'
 c0=cc();p0=time.process_time();w0=time.monotonic();used=lambda:cc()-c0+time.process_time()-p0
 # Reconstruct actual IDs from the earlier shared selector map once; native filters by current degrees each step.
 ids=array.array('I');ids.frombytes((G/'current_graph_data/FREE_IDS.u32le.bin').read_bytes())
 it=iter((G/'joint_cover/planes.txt').read_text().split());np=int(next(it));nf=int(next(it));assert np==754 and nf==len(ids)
 with(P/'RAW_PLANES_ACTUAL_IDS.txt').open('w')as f:
  f.write(str(np)+'\n')
  for _ in range(np):
   f.write(next(it)+'\n')
   for j in range(91):
    k=int(next(it));vs=[ids[int(next(it))-1]for _ in range(k)];f.write(str(k)+' '+' '.join(map(str,vs))+'\n')
 try:next(it);assert False
 except StopIteration:pass
 old=(G/'minimal_frontier_completion/frontier.cpp').read_text().split('int main(int argc,char**argv)')[0]
 (P/'continue.cpp').write_text(old+(P/'main.inc.cpp').read_text())
 def run(cmd,log,seconds,timeout=460):
  with(P/log).open('w')as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limit(seconds),timeout=timeout,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'})
  if r.returncode:raise RuntimeError(f'{log} exit {r.returncode}')
 run(['g++','-O3','-std=c++17',str(P/'continue.cpp'),'-o',str(P/'continue')],'COMPILE.log',20-used())
 run([str(P/'continue'),'--control'],'CONTROL.log',20-used())
 remaining=20-used()-0.5;assert remaining>0
 (P/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_SINGLE_FINITE_CONTINUATION','pid':os.getpid(),'whole_CPU_cap':20,'native_CPU_budget':remaining,'max_accepted':8,'no_followup':True})+'\n')
 run([str(P/'continue'),str(P),str(P/'RAW_PLANES_ACTUAL_IDS.txt'),str(R/'d12_n42403/graph_d12_D5_n42403.edges'),str(remaining)],'NATIVE.log',remaining+0.2,max(1,470-(time.monotonic()-w0)))
 result=json.loads((P/'NATIVE_RESULT.json').read_text());result.update(whole_CPU=used(),whole_wall=time.monotonic()-w0,whole_CPU_cap=20,control_log='CONTROL.log')
 assert result['whole_CPU']<=20
 (P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RUN_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','running':False,'result':'RESULT.json'})+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
