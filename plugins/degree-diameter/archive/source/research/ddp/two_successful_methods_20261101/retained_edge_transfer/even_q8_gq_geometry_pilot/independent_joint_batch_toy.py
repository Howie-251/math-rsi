import csv,itertools,json,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(15,16))
start=time.process_time();wall=time.time();D=Path(__file__).resolve().parent
results=[];total=validtotal=0
try:
 for M in [2,4,6]:
  for t in [2,3,4]:
   helperpairs=list(itertools.combinations(range(t),2));graphs=1<<len(helperpairs)
   tested=valid=unused_valid=0;mincap=None;capdist={}
   for mask in range(graphs):
    closed=[1<<h for h in range(t)];degree=[0]*t
    for b,(u,v) in enumerate(helperpairs):
     if mask>>b&1:
      closed[u]|=1<<v;closed[v]|=1<<u;degree[u]+=1;degree[v]+=1
    full=(1<<t)-1
    for own in itertools.product(range(-1,t),repeat=M):
     tested+=1
     good=True
     for c in range(M):
      a,b=own[c],own[c^1]
      cover=(closed[b] if b>=0 else 0)|(1<<a if a>=0 else 0)
      if cover!=full:good=False;break
     if not good:continue
     valid+=1
     if -1 in own:unused_valid+=1
     assert -1 not in own,('unused_owner_counterexample',M,t,mask,own)
     pins=[own.count(h) for h in range(t)]
     cap=max(pins[h]+degree[h] for h in range(t))
     for h,a in enumerate(pins):
      if a:assert degree[h]>=t-2,('active_degree_counterexample',M,t,mask,own,h)
     assert M<=t*(cap+2-t),('parabola_counterexample',M,t,mask,own,cap)
     assert M<=(cap+2)**2//4,('quadratic_counterexample',M,t,mask,own,cap)
     capdist[cap]=capdist.get(cap,0)+1
     mincap=cap if mincap is None else min(mincap,cap)
   total+=tested;validtotal+=valid
   results.append(dict(M=M,t=t,all_simple_helper_graphs=graphs,owner_choices_per_class=t+1,
    owner_graph_configurations=tested,valid_center_route_configurations=valid,
    valid_configurations_with_unused_class=unused_valid,minimum_helper_cap=mincap,
    valid_cap_distribution=capdist))
 # A sharp center-route witness only. Auxiliary edges realize exactly the short
 # route types; no assertion of full-graph diameter or saturated-source degrees.
 t=4;M=12;a=3;cap=5
 own=[c//3 for c in range(M)]
 partner=[3*((c//3)^1)+c%3 for c in range(M)]
 H={(0,2),(0,3),(1,2),(1,3)}
 edges=set()
 def edge(u,v):edges.add(tuple(sorted([u,v])))
 def adjacent(u,v):return tuple(sorted([u,v])) in edges
 for u,v in H:edge('h'+str(u),'h'+str(v))
 for c in range(M):
  edge('h'+str(own[c]),'x'+str(c))
  edge('x'+str(c),'p'+str(c))
  edge('p'+str(c),'c'+str(c))
  edge('x'+str(c),'c'+str(partner[c]))
  edge('c'+str(c),'c'+str(partner[c]))
 actual_helper_degree=[sum('h'+str(h) in e for e in edges) for h in range(t)]
 assert actual_helper_degree==[5]*4
 routecounts={};routes=[]
 for h in range(t):
  for c in range(M):
   d=partner[c]
   if own[c]==h:
    path=['h'+str(h),'x'+str(c),'p'+str(c),'c'+str(c)];kind='own_clone_shared_old_neighbor'
   elif own[d]==h:
    path=['h'+str(h),'x'+str(d),'c'+str(c)];kind='own_partner_clone'
   else:
    g=own[d];assert tuple(sorted([h,g])) in H
    path=['h'+str(h),'h'+str(g),'x'+str(d),'c'+str(c)];kind='neighbor_helper_partner_clone'
   assert len(path)-1<=3 and all(adjacent(u,v) for u,v in zip(path,path[1:]))
   routecounts[kind]=routecounts.get(kind,0)+1
   routes.append(dict(helper=h,center=c,partner=d,owner=own[c],partner_owner=own[d],route_type=kind,length=len(path)-1,path=path))
 assert M==t*(cap+2-t)==(cap+2)**2//4
 with (D/'INDEPENDENT_JOINT_BATCH_SHARP_TOY_ROUTES.csv').open('w') as f:
  w=csv.writer(f);w.writerow(['helper','center','partner','owner','partner_owner','route_type','length','path'])
  for r in routes:w.writerow([r[k] if k!='path' else ' -> '.join(r[k]) for k in ['helper','center','partner','owner','partner_owner','route_type','length','path']])
 toy=dict(t=t,M=M,pins_per_helper=a,Delta=cap,helper_graph_edges=sorted(H),
  matching_partner=partner,owner=own,actual_helper_degrees=actual_helper_degree,
  explicit_center_routes_checked=len(routes),route_types=routecounts,
  parabola_value=t*(cap+2-t),quadratic_value=(cap+2)**2//4,
  full_source_allpairs_D3_claimed=False,auxiliary_route_graph_is_q8_clonegraph=False)
 q8=[dict(case='balanced',R=65,delta=81,Delta=82,M=4160,quadratic_limit=(82+2)**2//4),
     dict(case='Payne',R=64,delta=80,Delta=81,M=4032,quadratic_limit=(81+2)**2//4)]
 for c in q8:c['conditional_batch_impossible']=c['M']>c['quadratic_limit']
 result=dict(status='PASS_BOUNDED_CENTER_ROUTE_EXHAUSTION_AND_SHARP_WITNESS',
  tested_owner_graph_configurations=total,valid_center_route_configurations=validtotal,
  counterexamples=0,cases=results,sharp_toy=toy,conditional_q8_consequences=q8,
  q8_onecopy_graphs_generated=0,new_field_checks=0,new_projection_checks=0,
  oldgraph_BFS=0,new_Lean=0,new_solver=0,new_q=0,all_processes_terminal=True,
  full_graph_D3_verified_in_toy=False,CPU_budget_seconds=15,test_CPU_seconds=time.process_time()-start)
 (D/'INDEPENDENT_JOINT_BATCH_ONE_COPY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 terminal=dict(status='PASS',single_worker=True,all_processes_terminal=True,
  total_CPU_seconds=time.process_time()-start,wall_seconds=time.time()-wall,
  CPU_budget_seconds=15,no_automatic_continuation=True,
  measurement_boundary='One exhaustive small abstract-owner/internal-graph test plus explicit sharp toy routes and aggregation; interactive paper/source authoring excluded.')
 (D/'INDEPENDENT_JOINT_BATCH_ONE_COPY_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 print(json.dumps(dict(terminal=terminal,tested=total,valid=validtotal,sharp_toy=toy,q8=q8),indent=2))
except Exception as e:
 result=dict(status='FAIL_COUNTEREXAMPLE',reason=str(e),CPU_seconds=time.process_time()-start)
 (D/'INDEPENDENT_JOINT_BATCH_ONE_COPY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 (D/'INDEPENDENT_JOINT_BATCH_ONE_COPY_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
 raise
