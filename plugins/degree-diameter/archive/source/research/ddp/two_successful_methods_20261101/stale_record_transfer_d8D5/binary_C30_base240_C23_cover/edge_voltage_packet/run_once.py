from pathlib import Path
import json,time,resource
B=Path(__file__).resolve().parent;P=B.parent
resource.setrlimit(resource.RLIMIT_CPU,(3,3));t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert not (B/'RESULT.json').exists()
a=load(P/'TYPED_BASE_ARCS.json');ps=load(P/'CRITICAL_PACKET_PATHS.json')['paths'];prior=load(P/'CRITICAL_PACKET_RESULT.json')
edges=sorted({tuple(sorted((u,v))) for u,v,_,_ in a['arcs_u_v_port_lambda']});assert len(edges)==960
ix={e:i for i,e in enumerate(edges)};forms=[];freq={}
for i,p in enumerate(ps):
 f={}
 for u,v in zip(p['vertices'],p['vertices'][1:]):
  e=ix[tuple(sorted((u,v)))];f[e]=f.get(e,0)+(1 if u<v else -1)
 f={e:c for e,c in f.items() if c};key=tuple(sorted(f.items()));forms.append(f);freq.setdefault(key,[]).append(i)
cols=sorted({e for f in forms for e in f});rows=[];base=forms[0]
for f in forms[1:]:rows.append([(f.get(e,0)-base.get(e,0))%23 for e in cols])
basis={};independent=[]
for j,row in enumerate(rows,1):
 v=row.copy()
 for c,b in sorted(basis.items()):
  z=v[c]
  if z:v=[(x-z*y)%23 for x,y in zip(v,b)]
 pivot=next((c for c,x in enumerate(v) if x),None)
 if pivot is not None:
  z=pow(v[pivot],-1,23);basis[pivot]=[(x*z)%23 for x in v];independent.append(j)
rank=len(basis);witness=False;theta=None;phases=None;selected=[]
if rank>=22:
 selected=independent[:22];m=[rows[j-1]+[i+1] for i,j in enumerate(selected)];pivots=[];rr=0
 for c in range(len(cols)):
  k=next((k for k in range(rr,len(m)) if m[k][c]),None)
  if k is None:continue
  m[rr],m[k]=m[k],m[rr];z=pow(m[rr][c],-1,23);m[rr]=[(x*z)%23 for x in m[rr]]
  for k in range(len(m)):
   if k==rr:continue
   z=m[k][c]
   if z:m[k]=[(x-z*y)%23 for x,y in zip(m[k],m[rr])]
  pivots.append(c);rr+=1
  if rr==22:break
 assert rr==22
 theta=[0]*960
 for i,c in enumerate(pivots):theta[cols[c]]=m[i][-1]
 phases=[sum(c*theta[e] for e,c in f.items())%23 for f in forms]
 assert len(set(phases))==23
 assert all((phases[j]-phases[0])%23==i+1 for i,j in enumerate(selected))
 witness=True
 save('VOLTAGE_WITNESS.json',{'field':23,'edge_orientation':'minlabel_to_maxlabel','edges':edges,'voltage':theta,'selected_paths':[0]+selected,'path_phases':phases,'critical_pair':[8,70],'phase_union':sorted(set(phases)),'whole_cover_status':'NOT_TESTED_NOT_A_DIAMETER_CERTIFICATE'})
save('SIGNED_EDGE_FLOWS.json',{'edges':edges,'path_flows':[sorted(f.items()) for f in forms],'equal_flow_classes':[{'flow':list(f),'path_indices':ids} for f,ids in freq.items()],'column_edges':cols,'independent_path_difference_indices':independent})
newcpu=time.process_time()-t0
r={'status':'CONSTRUCTED_ONE_PACKET_FULL23_EDGE_VOLTAGE_WITNESS' if witness else 'FLOW_INTERFACE_COMPLETE_NO_SINGLEPACKET_CONCLUSION','pair':[8,70],'saved_paths':len(ps),'distinct_signed_edge_flows':len(freq),'edge_support':len(cols),'flow_difference_rank_mod23':rank,'capacity_prediction_supported':len(freq)>=23,'rank_prediction_supported':rank>=22,'explicit_voltage_witness':witness,'witness_phase_coverage':len(set(phases)) if phases else None,'nonzero_edge_voltages':sum(x!=0 for x in theta) if theta else None,'new_CPU':newcpu,'new_prepare_CPU':.2,'prior_CPU':prior['samecase_CPU'],'samecase_CPU':prior['samecase_CPU']+.2+newcpu,'samecase_cap':10,'new_path_word_enumerations_BFS_solver_Lean_ARIS':0,'target5520_graph_generated':False,'allpair_D5_tested':False,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'singleactual8to70packet underindependentantisymmetricpoint-edgeF23voltages;no fullcoverexistenceclaim','terminal':True,'next':'REASSESS_SAVED_WITNESS_AND_DIAGONAL_OR_ALLPAIR_FLOW_NECESSARY_GATE_BEFORE_SEARCH'}
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))
