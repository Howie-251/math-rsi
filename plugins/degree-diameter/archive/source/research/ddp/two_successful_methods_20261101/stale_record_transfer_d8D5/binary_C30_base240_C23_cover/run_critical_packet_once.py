from pathlib import Path
import itertools,json,resource,time
B=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
t0=time.process_time()
def load(n):return json.loads((B/n).read_text())
def save(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not (B/'CRITICAL_PACKET_RESULT.json').exists(), 'once only'
a=load('TYPED_BASE_ARCS.json'); prior=load('BASE_RESULT.json')
assert a['n']==240 and prior['native']['minimum_pair']==[8,70]
adj=[[] for _ in range(240)]
for u,v,p,l in a['arcs_u_v_port_lambda']:adj[u].append((v,p,l))
paths=[]
def dfs(u,prev,vertices,labels,coeff):
 if u==70:paths.append({'vertices':vertices.copy(),'labels_port_lambda':labels.copy(),'integer_coeff':list(coeff)})
 if len(labels)==5:return
 for v,p,l in adj[u]:
  if v==prev:continue
  c=list(coeff);j=0 if p<2 else 2;s=1 if p%2==0 else -1;c[j]+=s;c[j+1]+=s*l
  dfs(v,u,vertices+[v],labels+[[p,l]],tuple(c))
dfs(8,-1,[8],[],(0,0,0,0))
counts=[sum(len(p['labels_port_lambda'])==i for p in paths) for i in range(6)]
assert len(paths)==66 and counts==prior['native']['minimum_pair_steps0to5']
freq={}
for p in paths:
 f=tuple(x%23 for x in p['integer_coeff']);freq[f]=freq.get(f,0)+1
forms=sorted(freq)
save('CRITICAL_PACKET_PATHS.json',{'pair':[8,70],'steps0to5':counts,'paths':paths})
save('CRITICAL_PACKET_FORMS.json',{'modulus':23,'coeff_order':['cA','dA','cB','dB'],'forms':[{'f':list(f),'multiplicity':freq[f]} for f in forms],'distinct':len(forms)})
rows=[];survivors=[]
if len(forms)>=23:
 for i in range(4):
  for tail in itertools.product(range(23),repeat=3-i):
   theta=(0,)*i+(1,)+tail
   covered={sum(x*y for x,y in zip(f,theta))%23 for f in forms}
   rows.append((theta,len(covered)))
   if len(covered)==23:survivors.append(theta)
 assert len(rows)==12720
 with (B/'CRITICAL_PACKET_PHASE_COUNTS.tsv').open('w') as out:
  out.write('cA\tdA\tcB\tdB\tcovered_phases\n')
  for theta,n in rows:out.write('\t'.join(map(str,theta+(n,)))+'\n')
 save('CRITICAL_PACKET_SURVIVORS.json',{'pair':[8,70],'survivors':survivors})
newcpu=time.process_time()-t0
r={'status':'COMPLETE_NO_FIXED_BASE_FOUR_GLOBAL_COEFFICIENT_C23_FAMILY' if (len(forms)<23 or not survivors) else 'ONE_PACKET_PASS_NOT_A_COVER','pair':[8,70],'NB_paths':len(paths),'steps0to5':counts,'distinct_forms':len(forms),'forms_prediction_supported':len(forms)>=23,'parameter_representatives_tested':len(rows),'parameter_survivors':len(survivors),'maximum_phase_coverage':max((n for _,n in rows),default=None),'new_CPU':newcpu,'prior_CPU':prior['case_CPU'],'new_prep_CPU':.15,'samecase_CPU':prior['case_CPU']+.15+newcpu,'samecase_cap':5,'all_pairs_tested':False,'target5520_graph_generated':False,'new_accepted_target_graph_parameter_Lean':[0,0,0],'excluded_scope':'Only this fixedbinary240 base plus fourglobalcoeffordinaryC23 rule if terminalNO; not arbitrary23covers or general8D5','terminal':True,'next':'STOP_AND_REASSESS_NO_FIELD_FOLD_BASE_OR_PARAMETER_LADDER'}
assert r['samecase_CPU']<5
save('CRITICAL_PACKET_RESULT.json',r);save('CRITICAL_PACKET_TERMINAL.json',{'terminal':True,'result':'CRITICAL_PACKET_RESULT.json'})
print(json.dumps(r,ensure_ascii=False))
