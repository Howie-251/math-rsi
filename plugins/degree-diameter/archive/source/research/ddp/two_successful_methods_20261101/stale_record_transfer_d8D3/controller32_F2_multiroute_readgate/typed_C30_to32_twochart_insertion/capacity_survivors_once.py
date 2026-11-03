"""Recorded stage2 algorithm, preserved for review; original output already exists."""
import json,csv,time
from pathlib import Path
start=time.process_time();p=Path(__file__).resolve().parent
if(p/'CAPACITY_SURVIVOR_ATTEMPT.json').exists():raise RuntimeError('stage2 already attempted; do not restart')
(p/'CAPACITY_SURVIVOR_ATTEMPT.json').write_text(json.dumps({'status':'STARTED','newprep':.1,'priorcase':5.073725259})+'\n')
old=[list(map(int,l.split()))for l in(p/'INPUT_CONTROLLER.txt').read_text().splitlines()]
rows=list(csv.DictReader((p/'BASE_CAPACITY_SURVIVORS.tsv').open(),delimiter='\t'));out=[];surv=[]
for raw in rows:
 i,j,k,l=[int(raw[z])for z in ['i','j','k','l']]
 a=[r[0]for r in old]+[-1,-1];b=[r[2]for r in old]+[-1,-1]
 a[30],a[i]=a[i],30;a[31],a[j]=a[j],31;b[30],b[k]=b[k],30;b[31],b[l]=b[l],31
 ai=[0]*32;bi=[0]*32
 for u in range(32):ai[a[u]]=u;bi[b[u]]=u
 C=[[a[u],ai[u],b[u],bi[u]]for u in range(32)]
 bad=None;checked=0
 for root in [31]+list(range(30)):
  cur=[0]*32;total=[0]*32;cur[root]=total[root]=1
  for step in range(3):
   nxt=[0]*32
   for u,n in enumerate(cur):
    if n:
     for v in C[u]:nxt[v]+=2*n
   cur=nxt;total=[x+y for x,y in zip(total,cur)]
  checked+=1
  if min(total)<8:
   bad={'root':root,'first_bad_target':next(v for v,x in enumerate(total)if x<8),'first_bad_capacity':next(x for x in total if x<8),'minimum':min(total)};break
 item={'tails':[i,j,k,l],'additional_root_queries':checked,'root30_not_repeated':True,'first_bad':bad};out.append(item)
 if bad is None:surv.append(item)
r={'status':'COMPLETE_NO_ALL_INSERTION_CONTROLLERS_ANY_TWOCHOICE_FIBERRULE'if not surv else'COMPLETE_NECESSARY_CAPACITY_WITH_GLOBAL_SURVIVORS','saved_firststage_survivors':len(rows),'secondstage_all_processed':True,'global_capacity_survivors':surv,'entries':out,'new_matrix_field_pointimage_graph_BFS_Lean_ARIS':0,'new_native_CPU':time.process_time()-start,'prior_case_CPU':5.073725259,'newprep_CPU':.1,'case_CPU':5.173725259+time.process_time()-start,'case_cap':30,'scope':'all284310simplecontrollers in savedtypedC30to32insertionfamily; any8fiber/atmost2choicespertypedcontrollerdart, allstepsproject tothesecontrolleredges;notgeneralC32or8D3','new_graph_parameter_Lean':[0,0,0],'next':'STOP_CONTROLLERINSERTION_FAMILY;do not searchmorematricesonthem','terminal':True}
(p/'CAPACITY_SURVIVOR_RESULT.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(r,ensure_ascii=False))
