from pathlib import Path
from collections import deque,Counter
import json,time,subprocess,resource,os
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
B=Path(__file__).resolve().parent;P=B.parent;R=B.parents[5];t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert not (B/'RESULT.json').exists()
solver=R/'.tools/lean-4.24.0-linux/bin/cadical';assert solver.is_file() and os.access(solver,os.X_OK)
sk=load(P/'SKELETON.json');edges=[tuple(e) for e in sk['edges']];eidx={e:i for i,e in enumerate(edges)};G=nx.Graph();G.add_nodes_from(range(10));G.add_edges_from(edges)
autos=list(GraphMatcher(G,G).isomorphisms_iter());assert len(autos)==120
edgeperms=[[eidx[tuple(sorted((a[u],a[v])))] for u,v in edges] for a in autos];ss=load(P/'SURVIVORS.json');orbits={}
for s in ss:
 sub=s['subdivided_edge_indices'];key=min(tuple(sorted(perm[e] for e in sub)) for perm in edgeperms);orbits.setdefault(key,[]).append(s)
keys=sorted(orbits);representatives=[min(orbits[k],key=lambda s:s['pattern']) for k in keys]
save('HELPER_ORBITS.json',{'automorphisms':120,'surviving_labelled_patterns':235,'orbits':len(orbits),'representatives':[{'pattern':s['pattern'],'member_patterns':[t['pattern'] for t in orbits[k]],'adjacency':s['adjacency'],'spokes':s['spokes_per_helper']} for k,s in zip(keys,representatives)]})
S=R/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single';a=load(S/'PORT_BALLS.json');cl=load(S/'PORT_CLASSES.json');q=load(R/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json');ports=a['ports'];assert len(ports)==28
balls=[]
for i,p in enumerate(ports):
 def mask(vertices):return sum(1<<v for v in set(vertices))
 row=[1<<p,mask(q['H3_graph'][p]+[p]),mask(cl['R2_class_members'][i])]
 for key in ['R3_words_u64','R4_words_u64']:row.append(sum(int(w)<<(64*j) for j,w in enumerate(a[key][i])))
 balls.append(row)
charges=[];cases=[];hit=None;source_edges=None
for ordinal,s in enumerate(representatives[:5]):
 C=B/f'orbit{ordinal}';C.mkdir(exist_ok=True);h=s['adjacency'];caps=s['spokes_per_helper'];assert sum(caps)==28;dh=[]
 for r in range(19):
  d=[-1]*19;d[r]=0;qq=deque([r])
  while qq:
   u=qq.popleft()
   for v in h[u]:
    if d[v]<0:d[v]=d[u]+1;qq.append(v)
  assert max(d)<=4;dh.append(d)
 clauses=[];nvar=532
 def x(p,j):return p*19+j+1
 def atmost(lits,k):
  nonlocal_dummy=None
  global nvar
  prev=None
  for lit in lits:
   cur=[]
   for _ in range(k):nvar+=1;cur.append(nvar)
   clauses.append([-lit,cur[0]])
   if prev is not None:
    for a1,b1 in zip(prev,cur):clauses.append([-a1,b1])
    for j in range(1,k):clauses.append([-lit,-prev[j-1],cur[j]])
    clauses.append([-lit,-prev[k-1]])
   prev=cur
 for p in range(28):
  ls=[x(p,j) for j in range(19)];clauses.append(ls);atmost(ls,1)
 for j,cap in enumerate(caps):atmost([x(p,j) for p in range(28)],cap)
 coverage=[]
 for hroot in range(19):
  for t in range(364):
   ls=[x(p,j) for p in range(28) for j in range(19) if (balls[p][4-dh[hroot][j]]>>t)&1]
   assert ls;coverage.append(ls)
 clauses+=coverage
 cnf=C/'MODEL.cnf'
 with cnf.open('w') as out:
  out.write(f'p cnf {nvar} {len(clauses)}\n')
  for ls in clauses:out.write(' '.join(map(str,ls))+' 0\n')
 meta={'pattern':s['pattern'],'variables':nvar,'assignment_variables':532,'clauses':len(clauses),'coverage_clauses':len(coverage),'ports':ports,'spokes':caps,'helper_adj':h,'source_BFS':0,'solver_seconds':5};(C/'MODEL.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 def limit():resource.setrlimit(resource.RLIMIT_CPU,(6,6))
 before=resource.getrusage(resource.RUSAGE_CHILDREN)
 with (C/'SOLVER.log').open('w') as out:
  proc=subprocess.Popen([str(solver),'-t','5',str(cnf)],stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
  save('LIVE_HANDLE.json',{'pid':proc.pid,'phase':f'orbit{ordinal}','argv':[str(solver),'-t','5',str(cnf)],'all_previous_cases':cases,'terminal':False})
  killed=False
  try:rc=proc.wait(timeout=10)
  except subprocess.TimeoutExpired:proc.kill();rc=proc.wait();killed=True
 after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime;charges.append(cpu);stdout=(C/'SOLVER.log').read_text();statuses=[l for l in stdout.splitlines() if l.startswith('s ')];status='SAT' if rc==10 and 's SATISFIABLE' in statuses else 'RAW_UNSAT_NOT_PROOFCHECKED' if rc==20 and 's UNSATISFIABLE' in statuses else 'UNKNOWN'
 result={'orbit':ordinal,'pattern':s['pattern'],'status':status,'returncode':rc,'solver_CPU':cpu,'wall_killed':killed,'proof_logged':False,'proof_checked':False}
 if status=='SAT':
  positives={int(z) for line in stdout.splitlines() if line.startswith('v ') for z in line[2:].split() if int(z)>0};owners=[]
  for p in range(28):
   js=[j for j in range(19) if x(p,j) in positives];assert len(js)==1;owners.append(js[0])
  assert [owners.count(j) for j in range(19)]==caps
  for hr in range(19):
   union=0
   for p,j in enumerate(owners):union|=balls[p][4-dh[hr][j]]
   assert union==(1<<364)-1
  # Full graph is only written after exact assignment and all19source-coverage checks.
  rows=(S/'source364.edges').read_text().splitlines();assert rows[0].split()==['364','714'];source_edges=[tuple(map(int,row.split())) for row in rows[1:] if row.strip()];assert len(source_edges)==714
  target=list(source_edges)+[(364+u,364+v) for u in range(19) for v in h[u] if u<v]+[(ports[p],364+j) for p,j in enumerate(owners)];assert len(target)==766
  with (B/'CANDIDATE383.edges').open('w') as out:
   out.write('383 766\n')
   for u,v in target:out.write(f'{u} {v}\n')
  save('PORT_ASSIGNMENT.json',{'orbit':ordinal,'helper_pattern':s['pattern'],'ports':ports,'owners':owners,'helper_adjacency':h,'source_coverage_all19':True,'whole_graph_candidate_n_m_degree_D':[383,766,4,5],'fresh_graph_BFS_Lean_ARIS':'PENDING'})
  hit=ordinal
 cases.append(result);(C/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 if hit is not None:break
parentcpu=time.process_time()-t0;prior=load(P/'RESULT.json')['case_CPU'];total=prior+.5+.25+parentcpu+sum(charges)
r={'status':'COMPLETE383_CANDIDATE_SAVED_PENDING_NEW_ACCEPTANCE' if hit is not None else 'NO_HIT_BOUNDED_HELPER_ORBIT_ASSIGNMENTS','helper_orbits':len(orbits),'orbits_tested':len(cases),'orbits_untested':len(orbits)-len(cases),'cases':cases,'prior_CPU':prior,'input_read_CPU_charge':.5,'prepare_CPU_charge':.25,'parent_CPU':parentcpu,'solver_CPU':sum(charges),'case_CPU':total,'case_cap':40,'candidate383_generated':hit is not None,'new_accepted_graph_parameter_Lean':[0,0,0],'source_or_target383_BFS_Lean_ARIS':0,'scope':'atmost5helperorbits of fixedPetersen9subdivision family;RAW_UNSATnotproofchecked andUNKNOWNpreserved;noallfamilyNO','terminal':True,'next':'freshbaseline_independentfull383BFS_Lean_ARISifhit;otherwiseSTOPnoparamseedtimerextensions'}
assert total<40
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});save('LIVE_HANDLE.json',{'terminal':True,'result':'RESULT.json','pid':None});print(json.dumps(r,ensure_ascii=False),flush=True)
