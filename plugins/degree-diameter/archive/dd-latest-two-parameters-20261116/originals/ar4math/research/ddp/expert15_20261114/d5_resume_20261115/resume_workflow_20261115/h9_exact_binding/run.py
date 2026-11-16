from pathlib import Path
from array import array
import json,lzma,math,os,resource,subprocess,time
P=Path(__file__).resolve().parent
AR=P.parents[5]
R=AR/'research/ddp'
start=time.monotonic(); c0=time.process_time();old=resource.getrusage(resource.RUSAGE_CHILDREN)
previous=0
if (P/'RESULT.json').exists():
 previous=json.loads((P/'RESULT.json').read_text())['whole_CPU']
 if not (P/'ATTEMPT1_RESULT.json').exists():(P/'ATTEMPT1_RESULT.json').write_text((P/'RESULT.json').read_text())
 with (P/'ATTEMPT_HISTORY.jsonl').open('a') as h:h.write((P/'RESULT.json').read_text().replace('\n','')+'\n')
def used():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return previous+time.process_time()-c0+r.ru_utime+r.ru_stime-old.ru_utime-old.ru_stime
result={'status':'STARTED','running':True}
def run(cmd,name):
 remain=30-used();wall=300-(time.time()-json.loads((P/'TASK_START.json').read_text())['wall_start'])
 if remain<1 or wall<=0:raise TimeoutError('whole task limit')
 def limit():
  t=max(1,math.ceil(remain));resource.setrlimit(resource.RLIMIT_CPU,(t,t));resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 with(P/name).open('w')as f:subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,check=True,timeout=wall,preexec_fn=limit)
try:
 source=R/'more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges'
 coords=R/'global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin'
 mapping=R/'more_graphs_20261027/h9_other_degrees/point_to_core11.u16.bin'
 for src,name in [(source,'source.edges'),(coords,'point_coords.u8.bin'),(mapping,'pi.u16.bin')]:
  if not(P/name).exists():os.link(src,P/name)
 classes=json.loads((R/'more_graphs_20261027/h9_other_degrees/fold11_classes.json').read_text())
 candidate=json.loads((P.parent/'h9_joint_gate/batch202/CANDIDATE.json').read_text())
 with lzma.open(R/'breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/tau.txt.xz','rt')as f:tau=list(map(int,f.read().split()))
 (P/'tau.i32.bin').write_bytes(array('i',tau).tobytes())
 eps=bytearray(66430);split=set(classes['split_fold_ids'])
 for fold in split:
  p=classes['point_representatives'][fold];q=tau[tau[p]];eps[p]=eps[q]=candidate['colors'][str(fold)]
 (P/'eps.u8.bin').write_bytes(eps)
 (P/'pins.txt').write_text('\n'.join(map(str,candidate['pins']))+'\n')
 (P/'RUN_HANDLE.json').write_text(json.dumps({'pid':os.getpid(),'running':True,'whole_CPU_cap':30})+'\n')
 run(['g++','-O3','-std=c++17',str(P/'build.cpp'),'-o',str(P/'build')],'COMPILE.log')
 remain=30-used()-0.7
 run([str(P/'build'),str(P),str(remain)],'NATIVE.log')
 result=json.loads((P/'NATIVE_RESULT.json').read_text())
except (Exception,)as e:
 result={'status':'UNKNOWN_OR_BUILD_ERROR','error':str(e),'running':False,'candidate_accepted':False}
finally:
 result.update(running=False,whole_CPU=used(),whole_wall=time.monotonic()-start,whole_CPU_cap=30,new_graph_accepted=False,peripheral_BFS_run=False)
 (P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RUN_HANDLE.json').write_text(json.dumps({'running':False,'status':result['status']})+'\n');print(json.dumps(result),flush=True)
