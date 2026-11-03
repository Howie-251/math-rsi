import time
START=time.process_time()
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
import json,resource,subprocess
HERE=Path(__file__).resolve().parent;PARENT=HERE.parent
REPO=next(p for p in HERE.parents if(p/'AGENTS.md').is_file())
PRIOR=22.084731374+.25+.2

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one shot cachedpacket diagnostic already attempted')
save('ATTEMPT.json',{'status':'STARTED','prior_read_prep_CPU':PRIOR,'new_native_budget':10,'wholecasecap':45})
from scipy.sparse import load_npz
model=json.loads((PARENT/'FP_MODEL.json').read_text());matrix=load_npz(PARENT/'FP_MODEL_MATRIX.npz').tocsc()
structure=json.loads((REPO/'research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json').read_text())
F=structure['F_vertices'];P=structure['P_vertices'];twins=structure['port_twin_pairs'];pclass={p:c for c,pair in enumerate(twins)for p in pair};fi={f:k for k,f in enumerate(F)}
cover_rows={i:fi[label[1]]for i,label in enumerate(model['row_labels'])if label[0]=='F_target_R2_coverage'}
assert len(F)==520 and len(P)==130 and len(twins)==65 and len(cover_rows)==520
Cf={};Dp={};fp_donors={f:set()for f in F}
for col,label in enumerate(model['variable_labels']):
 mask=0
 for k in range(matrix.indptr[col],matrix.indptr[col+1]):
  row=int(matrix.indices[k])
  if row in cover_rows:
   assert matrix.data[k]==1;mask|=1<<cover_rows[row]
 if label[0]=='cut_FP':
  f,p=label[1:];fp_donors[f].add(p)
  if f in Cf:assert Cf[f]==mask
  else:Cf[f]=mask
 else:
  assert label[0]=='star_P';Dp[label[1]]=mask
fc={}
for f in F:
 donors=fp_donors[f];assert len(donors)==2
 c=pclass[next(iter(donors))];assert donors==set(twins[c]);fc[f]=c
assert sorted(sum(fc[f]==c for f in F)for c in range(65))==[8]*65
assert len(Cf)==520 and len(Dp)==130
with(HERE/'PACKETS_INPUT.txt').open('w')as out:
 out.write('520 130 65\n')
 for f in F:out.write(' '.join(map(str,[f,fc[f]]+[(Cf[f]>>(64*k))&((1<<64)-1)for k in range(9)]))+'\n')
 for p in P:out.write(' '.join(map(str,[p,pclass[p]]+[(Dp[p]>>(64*k))&((1<<64)-1)for k in range(9)]))+'\n')
save('COEFFICIENT_BINDING.json',{'source':'oldFP_MODEL_MATRIX520coverage rows only','F_labels':F,'P_labels':P,'twins':twins,'F_class':fc,'C_f_masks_decimal_strings':{f:str(Cf[f])for f in F},'D_p_masks_decimal_strings':{p:str(Dp[p])for p in P},'C_sizes':[min(m.bit_count()for m in Cf.values()),max(m.bit_count()for m in Cf.values())],'D_sizes':[min(m.bit_count()for m in Dp.values()),max(m.bit_count()for m in Dp.values())],'same_D_for_twin_pairs':sum(Dp[a]==Dp[b]for a,b in twins),'source_adj_A2_A3_BFS_reads':0})
c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with(HERE/'COMPILE.log').open('w')as out:c=subprocess.run(['g++','-O3','-march=native','-std=c++17','run.cpp','-o','run'],cwd=HERE,stdout=out,stderr=subprocess.STDOUT)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
assert c.returncode==0
compilecpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime
def limit():resource.setrlimit(resource.RLIMIT_CPU,(10,10))
with(HERE/'RUN.log').open('w')as out:
 job=subprocess.Popen([str(HERE/'run')],cwd=HERE,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
 save('HANDLE.json',{'PID':job.pid,'status':'RUNNING_CAPACITY_ONLY','compile_CPU':compilecpu,'parent_CPU_before_run':time.process_time()-START})
 code=job.wait()
c2=resource.getrusage(resource.RUSAGE_CHILDREN);nativecpu=c2.ru_utime+c2.ru_stime-c1.ru_utime-c1.ru_stime
native=json.loads((HERE/'NATIVE_RESULT.json').read_text())if(HERE/'NATIVE_RESULT.json').exists()else {'status':'UNKNOWN_CHILD_EXIT_NO_RESULT','returncode':code}
result={'status':native['status'],'native':native,'compile_CPU':compilecpu,'actual_child_CPU':nativecpu,'actual_parent_CPU':time.process_time()-START,'prior_read_prep_CPU':PRIOR,'wholecase_CPU':PRIOR+compilecpu+nativecpu+time.process_time()-START,'wholecasecap':45,'new_native_budget':10,'source_adj_A2_A3_BFS_solver_graph_Lean_ARIS':0,'new_graph_parameter_Lean':[0,0,0],'prediction_atleast_one_upper_pass_supported':native.get('upper_pass',0)>0,'scope':'saved650FPcovercoefficients,8F/2starP,twinclassquotas; upperpassnotactualcover or651graph','next':'STOP_REASSESS; actualFcoverobject iffound maytriggerconstruction, otherwise noautomaticsecondsolve/seed','terminal':True}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps(result,ensure_ascii=False),flush=True)
