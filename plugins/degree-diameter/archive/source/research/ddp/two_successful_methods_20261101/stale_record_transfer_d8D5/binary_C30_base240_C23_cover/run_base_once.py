import time
START=time.process_time()
from pathlib import Path
import json,subprocess,resource
HERE=Path(__file__).resolve().parent;BASE=next(p for p in HERE.parents if(p/'STAGE_STATE.json').is_file());PRIOR=.5

def save(n,x):(HERE/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
if(HERE/'BASE_ATTEMPT.json').exists():raise RuntimeError('one fixedbase NB gate already attempted')
save('BASE_ATTEMPT.json',{'status':'STARTED','prior_read_prep':PRIOR,'casecap':5})
old=BASE/'stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/EXISTING_C30_BINARY_CHART_INPUT.json'
C=json.loads(old.read_text())['typed_controller']['controller'];BAR=[1,0,3,2];M=[[2,1,4],[2,1,4],[1,2,7],[1,2,7]];V=[1,2,4,7]
def app(c,x):return(c[0]if x&1 else 0)^(c[1]if x&2 else 0)^(c[2]if x&4 else 0)
arcs=[];edges=set()
for u in range(30):
 for x in range(8):
  a=8*u+x
  for p in range(4):
   assert C[C[u][p]][BAR[p]]==u
   for lam in [0,1]:
    v=8*C[u][p]+(app(M[p],x)^(V[p]if lam else 0));assert v!=a
    assert app(M[BAR[p]],v%8)^(V[BAR[p]]if lam else 0)==x
    arcs.append([a,v,p,lam]);edges.add(tuple(sorted((a,v))))
assert len(arcs)==1920 and len(edges)==960
with(HERE/'BASE240.edges').open('w')as f:
 f.write('240 960\n')
 for u,v in sorted(edges):f.write(f'{u} {v}\n')
save('TYPED_BASE_ARCS.json',{'n':240,'degree':8,'controller':C,'maps_columns':M,'forwardnoise':V,'bar':BAR,'arcs_u_v_port_lambda':arcs,'reverse_lambda_is_same':True,'source':'existingC30plusARCbinarychart;notF5mod2','not_a_targetrecord_graph':True})
c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with(HERE/'BASE_COMPILE.log').open('w')as f:c=subprocess.run(['g++','-O3','-std=c++17','base_nb.cpp','-o','base_nb'],cwd=HERE,stdout=f,stderr=subprocess.STDOUT)
assert c.returncode==0
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
def limit():resource.setrlimit(resource.RLIMIT_CPU,(2,2))
p=subprocess.run([str(HERE/'base_nb')],cwd=HERE,capture_output=True,text=True,preexec_fn=limit);assert p.returncode==0
c2=resource.getrusage(resource.RUSAGE_CHILDREN);native=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r={'status':'BASE_COMPLETE_CAPACITY_PASS_NO_COVER_CONSTRUCTED'if native['capacity_pass']else'COMPLETE_NO_ALL_ORDINARY_RECORDSIZE_COVERS_OF_THIS_BASE','native':native,'compile_CPU':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'child_CPU':c2.ru_utime+c2.ru_stime-c1.ru_utime-c1.ru_stime,'parent_CPU':time.process_time()-START,'prior_read_prep_CPU':PRIOR,'case_CPU':PRIOR+c2.ru_utime+c2.ru_stime-c0.ru_utime-c0.ru_stime+time.process_time()-START,'case_cap':5,'base_graph_generated':True,'target5520_graph_generated':False,'oldsource_validation_solver_Lean_ARIS':0,'new_accepted_target_graph_parameter_Lean':[0,0,0],'intermediate_base_calibration_only':True,'next':'ifcapacitypass freezebase and testoneC23coefficientformpacket before parameters; otherwiseSTOPthisbaseforrecordsizeordinarycovers','terminal':True}
save('BASE_RESULT.json',r);save('BASE_TERMINAL.json',r)
print(p.stdout);print(json.dumps(r,ensure_ascii=False),flush=True)
