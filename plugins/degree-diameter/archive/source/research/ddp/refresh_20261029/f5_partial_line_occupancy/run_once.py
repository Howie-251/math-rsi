import itertools,json,pathlib,resource,subprocess,time
D=pathlib.Path(__file__).resolve().parent
ROOT=D.parents[3]
start=time.process_time()
child0=resource.getrusage(resource.RUSAGE_CHILDREN)
if (D/'RESULT.json').exists():raise SystemExit('one bounded experiment already completed')
def cpu_children():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-child0.ru_utime-child0.ru_stime
def limit():resource.setrlimit(resource.RLIMIT_CPU,(10,10))
subprocess.run(['g++','-O3','-std=c++17',str(D/'quotient.cpp'),'-o',str(D/'quotient')],check=True)
r=subprocess.run([str(D/'quotient')],capture_output=True,text=True,check=True,preexec_fn=limit)
(D/'quotient.log').write_text(r.stdout)
qres=json.loads(r.stdout)
rowstates=0
for a in range(32):
  for b in range(32):
    for c in range(2):
      direct=all(not ((b>>j&1) and (a&~(1<<j))) or ((a>>j&1) and c) for j in range(5))
      formula=(not a or not b or ((b&~a)==0 and (a.bit_count()==1 or c)))
      assert direct==formula
      rowstates+=1
P=json.loads((ROOT/'research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json').read_text())
ell=[tuple(x) for x in P['directions']];T=P['matrices'];inv=P['inverse_ports'];C=P['controller']
pts=list(itertools.product(range(5),repeat=3))
def add(x,y):return tuple((a+b)%5 for a,b in zip(x,y))
def scale(k,x):return tuple(k*a%5 for a in x)
def mat(m,x):return tuple(sum(a*b for a,b in zip(row,x))%5 for row in m)
def line(x,e):return {add(x,scale(k,e)) for k in range(5)}
def N(p,x):return line(mat(T[p],x),ell[inv[p]])
def paircheck(A,B,p):
  violations=[]
  for X,Y,port,side in [(A,B,p,'u'),(B,A,inv[p],'v')]:
    for w in pts:
      if not (N(port,w)&Y):continue
      for other in range(4):
        if other!=port and (line(w,ell[other])-{w})&X and w not in X:violations.append([side,list(w),other])
  return violations
p=1
pre={(k,0) for k in range(1,5)}|{(0,k) for k in range(1,5)}|{(k,k) for k in range(1,5)}
outer={(i,j) for i in range(5) for j in range(5)}-pre-{(0,0)}
U=outer|{(0,0)}
A={x for x in pts if (x[0],x[2]) in outer or ((x[0],x[2])==(0,0) and x[1]!=0)}
Bprime={x for x in pts if (x[0],x[2]) in U}
B={mat(T[p],x) for x in Bprime}
viol=paircheck(A,B,p)
assert len(A)==64 and len(B)==65 and not viol
low={tuple([0,0,0])};singleB={mat(T[p],next(iter(low)))}
assert not paircheck(low,singleB,p)
def code(x):return x[0]+5*x[1]+25*x[2]
witness={'port':p,'source_controller_dart':[0,20],'A_size':len(A),'B_size':len(B),'A_local_labels':sorted(map(code,A)),'B_local_labels':sorted(map(code,B)),'A_edge_line_sizes':[4]+[5]*12,'B_transformed_quotient':sorted([list(x) for x in U]),'bidirectional_keep_middle_violations':viol,'provider_flags':'All true; relaxed local two-fiber system, not a maxdegree16 global graph'}
(D/'BOUNDARY_COUNTEREXAMPLE.json').write_text(json.dumps(witness,ensure_ascii=False,indent=2)+'\n')
def triangleports(a):return [p for p,b in enumerate(C[a]) if set(C[a])&set(C[b])]
ext0=[p for p in range(4) if p not in triangleports(0)]
ext20=[p for p in range(4) if p not in triangleports(20)]
def plane(v,w):return {add(scale(i,v),scale(j,w)) for i in range(5) for j in range(5)}
E0=plane(*(ell[t] for t in ext0));E20=plane(*(ell[t] for t in ext20));transport={mat(T[1],x) for x in E0}
assert len(E0)==len(E20)==25 and transport!=E20
direction_witness=next(x for x in ell if x in E0 and mat(T[1],x) not in E20)
wholecpu=time.process_time()-start+cpu_children()
result={'status':'LOCAL_H65_SUPPORTED_WITH_FINITE_QUOTIENT_CERTIFICATE','row_truth_table_states':rowstates,'quotient':qres,'boundary_counterexample_file':'BOUNDARY_COUNTEREXAMPLE.json','unqualified_full_or_zero_prediction':'REFUTED by adjacent singleton pair','H65_threshold_note':'ceil65/5=13; if common support has13 lines both sizes>=65 already force full lines. At>=14 lines use connectivity plus a nonzero-holonomy triangle.','all_high_source_obstruction':{'dart':[0,20],'port':1,'external_ports_u':ext0,'external_ports_v':ext20,'E_u_not_transporting_to_E_v':True,'direction_witness':list(direction_witness),'image':list(mat(T[1],direction_witness))},'aggregate_CPU_seconds':wholecpu,'CPU_budget_seconds':15,'workers':1,'source_graph_reads':0,'source_graph_BFS':0,'SAT_calls':0,'new_graphs':0,'scope':'Local pair closure with provider flags relaxed; actual source consequence conditional on all30 fibers>=65. No exclusion of nonuniform general target.'}
assert wholecpu<15
(D/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps({'running':False,'status':'COMPLETE','aggregate_CPU_seconds':wholecpu,'new_graphs':0,'no_followup_started':True},indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
