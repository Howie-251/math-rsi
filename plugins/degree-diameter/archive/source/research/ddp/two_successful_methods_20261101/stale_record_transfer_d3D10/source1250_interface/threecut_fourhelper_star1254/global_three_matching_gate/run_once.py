from pathlib import Path
import json,os,resource,subprocess,time
D=Path(__file__).resolve().parent;os.chdir(D)
source=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d3_D10_current1250_source/source1250.edges');assert source.is_file()
prior=1.916663729;prep=.5;cap=30.;start=time.process_time();wall=time.time()
def child(argv,log,limit):
 before=resource.getrusage(resource.RUSAGE_CHILDREN)
 def bound():
  resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(limit)),max(2,int(limit)+1)))
  resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
 with open(log,'w') as out:
  p=subprocess.Popen(argv,stdout=out,stderr=subprocess.STDOUT,preexec_fn=bound)
  (D/'DRIVER_HANDLE.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'start_UTC':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),'starline_CPU_cap':cap,'prior_fixed_CPU':prior,'new_prep_charge':prep},indent=2)+'\n')
  rc=p.wait()
 after=resource.getrusage(resource.RUSAGE_CHILDREN)
 return rc,after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
cc,ct=child(['g++','-O2','-std=c++17','run_once.cpp','-o','run_once'],'COMPILE.log',5)
rc=None;nt=0
if cc==0:
 remaining=cap-prior-prep-ct-(time.process_time()-start)-.5
 rc,nt=child([str(D/'run_once'),str(source),str(max(.1,remaining-1))],'RUN.log',remaining)
pt=time.process_time()-start;total=prior+prep+ct+nt+pt
r=json.loads((D/'NUMERIC_RESULT.json').read_text()) if (D/'NUMERIC_RESULT.json').exists() else {'status':'UNKNOWN_EXECUTION_FAILURE'}
r.update({'starline_CPU_cap':cap,'prior_fixed_CPU':prior,'new_prep_charge':prep,'compile_exit':cc,'compile_CPU':ct,'numeric_exit':rc,'native_actual_CPU':nt,'parent_actual_CPU':pt,'starline_cumulative_CPU':total,'new_graph_count':0,'new_parameter_count':0,'new_Lean_count':0})
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps({'terminal':True,'status':r['status'],'starline_CPU':total,'CPU_cap':cap,'compile_exit':cc,'native_exit':rc,'wall_seconds':time.time()-wall,'sourceD10validationBFS':0,'no_automatic_continuation':True},indent=2)+'\n')
print(json.dumps(r,indent=2),flush=True)
