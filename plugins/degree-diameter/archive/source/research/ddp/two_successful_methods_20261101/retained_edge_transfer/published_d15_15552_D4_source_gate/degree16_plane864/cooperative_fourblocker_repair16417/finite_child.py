#!/usr/bin/env python3
import time
START=time.process_time()
import array,collections,csv,itertools,json,os,resource,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent;PLANE=HERE.parent
ROOT=next(p for p in HERE.parents if(p/'research-wiki').is_dir())
LOCAL=PLANE.parent/'nonorbit_clone_interface/append_oneout_twoin_gate'
AVAILABLE=PLANE/'available_pin_extension16417'
N=16416;OLD=15552;Z=N;BYTES=2052;INF=99
resource.setrlimit(resource.RLIMIT_CPU,(80,80))
phase='INPUT';prefix={};counts=collections.Counter();hit=None
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2)+'\n')
def checkpoint(stage,**kw):
 save('CHECKPOINT.json',dict(stage=stage,pid=os.getpid(),CPU_sofar=time.process_time()-START,**kw))
def budget():
 if time.process_time()-START>74:raise TimeoutError('softCPUreturn74')
def ballunion(P,table):
 m=0
 for p in P:m|=table[p]
 return m
def firstbit(mask):return(mask&-mask).bit_length()-1
def main():
 global phase,prefix,hit
 assert(HERE/'COOPERATIVE_BLOCKER_REPAIR_PAPER.md').is_file()
 raw=(LOCAL/'ALL15552_CENTER_BLOCKING_PROFILES.tsv').read_text()
 if'\t'not in raw.splitlines()[0]:raw=raw.replace('\\t','\t')
 candidates=[r for r in csv.DictReader(raw.splitlines(),delimiter='\t')if int(r['selected_role_or_minus1'])<0 and int(r['distinct_blocking_clone_owners'])==4]
 assert len(candidates)==342
 params=json.loads((PLANE/'PARAMETERS.json').read_text());centers=params['source_center_labels']
 adj=[[]for _ in range(N)];edges=[]
 with(PLANE/'graph_d16_D4_n16416.edges').open()as f:
  assert tuple(map(int,next(f).split()))==(N,129240)
  for line in f:
   u,v=map(int,line.split());adj[u].append(v);adj[v].append(u);edges.append((u,v))
 degree=list(map(len,adj));assert len(edges)==129240 and collections.Counter(degree)=={14:126,15:3924,16:12366}
 source_adj=[tuple(w for w in adj[v]if w<OLD)for v in range(OLD)]
 # Current R1/R2 and oldsource R3 are a new immutable metric cache.
 phase='CLOSED_BALL_CACHE';checkpoint(phase)
 R1=[]
 for v in range(N):
  m=1<<v
  for w in adj[v]:m|=1<<w
  R1.append(m)
 R2=[]
 for v in range(N):
  m=R1[v]
  for w in adj[v]:m|=R1[w]
  R2.append(m)
 available=json.loads((AVAILABLE/'ALL_AVAILABLE_PINS.json').read_text())['available_actual_pin_labels']
 oldR3=[None]*OLD;reused=0
 with(AVAILABLE/'ALL4050_CLOSED_R3_SUPPORTS.bits').open('rb')as f:
  for v in available:
   b=f.read(BYTES);assert len(b)==BYTES
   if v<OLD:oldR3[v]=int.from_bytes(b,'little');reused+=1
  assert not f.read(1)
 assert reused==3186
 newR3=0
 for v in range(OLD):
  if v%512==0:budget()
  if oldR3[v]is None:
   m=R2[v]
   for w in adj[v]:m|=R2[w]
   oldR3[v]=m;newR3+=1
 assert newR3==12366
 for name,table in [('CURRENT_ALL16416_R1.bits',R1),('CURRENT_ALL16416_R2.bits',R2),('CURRENT_OLDSOURCE15552_R3.bits',oldR3)]:
  with(HERE/name).open('wb')as f:
   for m in table:f.write(m.to_bytes(BYTES,'little'))
 save('IMMUTABLE_BASE_DISTANCE_SCHEMA.json',dict(current_graph=str((PLANE/'graph_d16_D4_n16416.edges').relative_to(ROOT)),
  current_graph_parse_count=1,current_n=N,sourceoldlabels='0..15551',target_bit='actualcurrentlabel0..16415',
  row_bytes=BYTES,byte_order='little',R1_rows=N,R2_rows=N,oldsource_R3_rows=OLD,
  oldsource_R3_reused_from_available=3186,oldsource_R3_new_by_bitset_recurrence=12366,
  recurrence='R1=self|adj;R2=R1|ORneighborR1;R3=R2|ORneighborR2',
  base_rule='deletefourdonortargetbits;currentrestrictedmetric=basebydonor_to_oldcenterretraction',
  sourceD4_validity_BFS_field_Lean_ARIS=0,local_BFS_cache_roots=0))
 pair_edges=list(itertools.combinations(range(5),2));hdegrees=[]
 for mask in range(1024):
  ds=[0]*5
  for bit,(i,j)in enumerate(pair_edges):
   if mask>>bit&1:ds[i]+=1;ds[j]+=1
  hdegrees.append(ds)
 domains={};allfull=(1<<N)-1;case_records=[];phase='FINITE_342_MAXIMAL_H'
 failfile=(HERE/'ALL_FAILURE_ROUTE_DECOMPOSITIONS.jsonl').open('w')
 stagefile=(HERE/'ALL_MAXIMAL_H_STAGES.tsv').open('w',newline='');out=csv.writer(stagefile,delimiter='\t')
 out.writerow(['case_index','source_center_v','Hmask','Hedges','stage','first_helper','first_target','target_class'])
 ballsfile=(HERE/'ALL_VISITED_CASE_HELPER_B0_B3.bits').open('wb')
 for case_index,row in enumerate(candidates):
  budget();v=int(row['source_center']);prefix={'case_index':case_index,'source_center_v':v}
  roles=sorted(map(int,row['blocking_old_roles'].split(',')));donors=[OLD+r for r in roles]
  Nv=set(source_adj[v]);blocked=set(map(int,row['blocking_slot_labels'].split(',')))
  assert len(Nv)==int(row['source_degree']) and blocked=={w for w in Nv if degree[w]==16}
  removed_by=[[]for _ in range(4)];rolepos={r:i for i,r in enumerate(roles)}
  for w in sorted(blocked):
   own=[c for c in adj[w]if c>=OLD];assert len(own)==1 and own[0]-OLD in rolepos
   removed_by[rolepos[own[0]-OLD]].append(w)
  assert all(removed_by)
  originals=[set(adj[c])for c in donors]+[Nv]
  assert all(all(p<OLD for p in P)for P in originals)
  P=[originals[i]-set(removed_by[i])for i in range(4)]+[Nv]
  helpers=donors+[Z];removed_edges={tuple(sorted((donors[i],w)))for i in range(4)for w in removed_by[i]}
  removed_mask=sum(1<<c for c in donors);basefull=allfull^removed_mask
  caps=[16-len(P[i])for i in range(5)];ecap=tuple(min(c,4)for c in caps)
  assert all(c>=0 for c in caps)
  B=[]
  for group in P:
   pm=sum(1<<p for p in group)
   bs=[pm,ballunion(group,R1),ballunion(group,R2),ballunion(group,oldR3)]
   bs=[m&basefull for m in bs];B.append(bs)
   for m in bs:ballsfile.write(m.to_bytes(BYTES,'little'))
  assert B[4][3]==basefull # full-N newZ interface, a newhelper-input check
  initial=[[INF]*5 for _ in range(5)]
  for i in range(5):
   initial[i][i]=0
   for j in range(i):
    d=next((r+2 for r in range(3)if B[i][r]&B[j][0]),INF)
    initial[i][j]=initial[j][i]=d
  if ecap not in domains:
   legal=[];maximal=[]
   for mask,ds in enumerate(hdegrees):
    if any(ds[i]>ecap[i]for i in range(5)):continue
    legal.append(mask)
    if all((mask>>b&1)or ds[i]>=ecap[i]or ds[j]>=ecap[j]for b,(i,j)in enumerate(pair_edges)):maximal.append(mask)
   domains[ecap]=dict(effective_cap=list(ecap),legal_H_count=len(legal),all_inclusion_maximal_H_masks=maximal,
    maximal_H_edgecount_histogram=dict(collections.Counter(m.bit_count()for m in maximal)))
  record=dict(case_index=case_index,source_center_v=v,source_Nv=sorted(Nv),donor_old_roles=roles,
   donor_current_labels=donors,donor_oldsource_centers=[centers[r]for r in roles],
   original_fullN=[sorted(x)for x in originals],remaining_P=[sorted(x)for x in P],deleted_by_donor=removed_by,
   helper_labels=helpers,helper_capacity=caps,effective_capacity=list(ecap),initial_base_costs=initial,
   base_vertices=N-4,base_donor_exclusion_mask_hex=hex(removed_mask),
   helper_ball_byte_offset=case_index*5*4*BYTES,maximal_H_count=len(domains[ecap]['all_inclusion_maximal_H_masks']))
  case_records.append(record);counts['centers_started']+=1
  for hm in domains[ecap]['all_inclusion_maximal_H_masks']:
   budget();prefix={**prefix,'Hmask':hm};counts['H_evaluated']+=1
   D=[a.copy()for a in initial]
   for b,(i,j)in enumerate(pair_edges):
    if hm>>b&1:D[i][j]=D[j][i]=1
   before=[a.copy()for a in D]
   for k in range(5):
    for i in range(5):
     for j in range(5):D[i][j]=min(D[i][j],D[i][k]+D[k][j])
   badpair=next(((i,j)for i in range(5)for j in range(i+1,5)if D[i][j]>4),None)
   fail=None;covers=[]
   if badpair:
    i,j=badpair;fail=dict(type='HELPER_PAIR',first_helper_index=i,first_helper=helpers[i],target=helpers[j],
     target_class='newZ'if j==4 else'donor_helper',threshold='nohelperpairWalk<=4',
     truncated_weighted_distance=D[i][j],not_claiming_true_infinite_distance=True,
     original_fullN_i=sorted(originals[i]),original_fullN_j=sorted(originals[j]),
     deleted_attachments_i=removed_by[i]if i<4 else[],deleted_attachments_j=removed_by[j]if j<4 else[])
   else:
    for i in range(5):
     cover=0
     for g in range(5):
      if D[i][g]<=3:cover|=B[g][3-D[i][g]]
     covers.append(cover)
     missing=basefull&~cover
     if missing:
      target=firstbit(missing);options=[]
      for g in range(5):
       ell=D[i][g];radius=3-ell
       r=next((r for r in range(4)if B[g][r]>>target&1),None)
       options.append(dict(last_helper=helpers[g],weighted_helper_cost=ell,allowed_old_leg_radius=radius,
        old_leg_min_in_0to3=r,total_length_if_known=ell+1+r if r is not None else None,
        reaches_within4=bool(radius>=0 and(B[g][radius]>>target&1))))
      losses=[]
      if i<4:
       for w in removed_by[i]:
        r=next((r for r,tab in enumerate([None,R1,R2,oldR3])if((1<<w)if r==0 else tab[w])>>target&1),None)
        if r is not None:losses.append(dict(deleted_edge=[helpers[i],w],old_base_leg_length=r,old_total_length=1+r,
         route_form='donor--deleted_oldslot--stable_base_leg--target'))
      fail=dict(type='HELPER_TO_BASE',first_helper_index=i,first_helper=helpers[i],target=target,
       target_class='original15552'if target<OLD else'retained_clone',last_helper_route_decomposition=options,
       lost_direct_donor_attachment_routes=losses)
      break
   if fail:
    counts[fail['type']]+=1;counts['H_failed']+=1
    fail.update(case_index=case_index,source_center_v=v,Hmask=hm,Hedges=[pair_edges[b]for b in range(10)if hm>>b&1],
     helper_labels=helpers,initial_with_H_costs=before,Floyd_costs=D)
    failfile.write(json.dumps(fail)+'\n')
    out.writerow([case_index,v,hm,hm.bit_count(),fail['type'],fail['first_helper'],fail['target'],fail['target_class']])
    continue
   hit=dict(case=record,Hmask=hm,H_index_edges=[list(pair_edges[b])for b in range(10)if hm>>b&1],
    initial_with_H_costs=before,Floyd_costs=D,full_base_cover_hex=[hex(x)for x in covers],base_full_hex=hex(basefull),
    all5_helperpairs_within4=True,all5_helper_to_all16412_base_within4=True)
   out.writerow([case_index,v,hm,hm.bit_count(),'FULL_WEIGHTED_D4_PASS',-1,-1,'all'])
   break
  if hit:break
  counts['centers_complete']+=1
  if case_index%32==0:checkpoint('FINITE_MAXIMAL_H_ACTIVE',case_index=case_index,H_completed=counts['H_evaluated'])
 failfile.close();stagefile.close();ballsfile.close()
 save('ALL_VISITED_CENTER_HELPER_INTERFACES.json',case_records)
 save('ALL_CAPACITY_MAXIMAL_H_DOMAINS.json',list(domains.values()))
 save('HELPER_BALL_SCHEMA.json',dict(bytes_per_ball=BYTES,case_order='ALL_VISITED_CENTER_HELPER_INTERFACES.json',
  ordering='case then helper0..4 then radius0..3',target_bits='actualcurrentlabels0..16415;fourdonortargetsremoved',
  cases_saved=len(case_records),immutable_metric='currentrestrictedbasebyretraction'))
 result=dict(status='COMPLETE_NO_FIXED342_FOURBLOCKER_DONATION_ALL_MAXIMAL_HELPER_H',full_domain_complete=hit is None,
  candidate_center_domain=342,counts=dict(counts),source_current_graph_parses=1,
  existing_oldsource_R3_reused=3186,new_oldsource_R3_by_recurrence=12366,new_current_R2_rows=N,
  old_source_D4_BFS_field_Lean_ARIS_solver=0,new_graph_parameter_Lean_counts=[0,0,0],candidate_graphs_generated=0,
  scope='sameaccepted16416,342exactfourblockeroldcenters,deterministicblockededge donation,newZfullsourceNv,all5helperH',
  not_general16D4_NO=True,next='STOP noS5/seed/secondcase')
 if hit:
  phase='POSITIVE_ARTIFACTS';checkpoint(phase,source_center_v=hit['case']['source_center_v'])
  rc=hit['case'];donors=rc['donor_current_labels'];helpers=rc['helper_labels'];Nv=rc['source_Nv']
  removed={tuple(sorted((donors[i],w)))for i in range(4)for w in rc['deleted_by_donor'][i]}
  hedges=[tuple(sorted((helpers[i],helpers[j])))for i,j in hit['H_index_edges']]
  final_edges=[(u,v)for u,v in edges if tuple(sorted((u,v)))not in removed]
  assert len(final_edges)==129240-len(removed)
  final_edges += [(w,Z)for w in Nv]+hedges
  final_adj=[[]for _ in range(N+1)]
  for u,v in final_edges:final_adj[u].append(v);final_adj[v].append(u)
  fdeg=list(map(len,final_adj));assert max(fdeg)<=16
  assert sum(u<OLD and v<OLD for u,v in final_edges)==116316
  with(HERE/'graph_d16_D4_n16417.edges').open('w')as f:
   f.write(f'{N+1} {len(final_edges)}\n')
   for u,v in final_edges:f.write(f'{u} {v}\n')
  stats=[]
  for root in helpers:
   ds=[-1]*(N+1);ds[root]=0;q=[root]
   for x in q:
    for y in final_adj[x]:
     if ds[y]<0:ds[y]=ds[x]+1;q.append(y)
   assert len(q)==N+1 and max(ds)<=4
   stats.append(dict(root=root,rootscope='newcandidatehelper',reached=len(q),ecc=max(ds),distance_histogram=dict(collections.Counter(ds))))
  hit.update(removed_actual_oldedges=sorted(map(list,removed)),added_actual_Hedges=list(map(list,hedges)),
   newZ_actual_edges=[[w,Z]for w in Nv],candidate_helper_BFS=stats)
  save('WEIGHTED_BASE_COVER_CERTIFICATE.json',hit)
  save('RETAINED860_CLONE_ROLE_BINDINGS.json',[dict(old_role=j,actual_vertex=OLD+j,source_center=centers[j],frozen_N=adj[OLD+j])
   for j in range(864)if OLD+j not in donors])
  save('PARAMETERS.json',dict(n=N+1,m=len(final_edges),maxdegree=max(fdeg),degree_histogram=dict(collections.Counter(fdeg)),
   source_current_graph=str((PLANE/'graph_d16_D4_n16416.edges').relative_to(ROOT)),source_center_v=rc['source_center_v'],
   original_source_Nv=Nv,donor_roles=rc['donor_old_roles'],donor_labels=donors,removed_oldedges=hit['removed_actual_oldedges'],
   helper_Hedges=hit['added_actual_Hedges'],all15552_source_vertices_and116316_source_edges_preserved=True,
   all16416_current_vertices_preserved=True,all16416_current_edges_preserved=False,remaining_fullN_clones=860,
   base_vertices=16412,helper_vertices=5,final_newpoint_label=Z,proof='weightedhelperpairs+lasthelperbasecover+inheritedbaseD4',
   exactD4_lower='16417>(16+1)^3=4913',fresh_acceptance='PENDING_ROOT',new_graph_parameter_Lean_counts=[0,0,0]))
  result.update(status='FOUND_COOPERATIVE_FOURBLOCKER_16417_CANDIDATE_PENDING_FRESH_ACCEPTANCE',full_domain_complete=False,
   candidate_graphs_generated=1,selected_source_center=rc['source_center_v'],candidate_n=N+1,candidate_m=len(final_edges),
   candidate_degree_histogram=dict(collections.Counter(fdeg)),new_candidate_helper_BFS_roots=5,fresh_acceptance='PENDING_ROOT')
 save('CHILD_RESULT.json',result)
 checkpoint('CHILD_TERMINAL',status=result['status'],counts=dict(counts))
if __name__=='__main__':
 try:main()
 except Exception as exc:
  save('CHILD_RESULT.json',dict(status='UNKNOWN_COOPERATIVE_BUDGET_OR_INPUT_PROCESS_FAILURE',phase=phase,
   first_unfinished_prefix=prefix,error=str(exc),traceback=traceback.format_exc(),counts=dict(counts),
   full_domain_complete=False,candidate_graphs_generated=0,new_graph_parameter_Lean_counts=[0,0,0],
   next='STOP preservepartialdataandcost;noautomaticretry'))
  raise
