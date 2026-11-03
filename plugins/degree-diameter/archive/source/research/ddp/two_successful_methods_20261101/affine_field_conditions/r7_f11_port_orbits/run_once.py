import csv,itertools,json,resource,time
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parent;Q=11;POINTS=['inf']+list(range(11));FULL=(1<<12)-1
def inv(x):return pow(x%Q,-1,Q)
def normalize(v):
 s=inv(next(x for x in v if x%Q));return tuple(x*s%Q for x in v)
def mobius(c,x):
 a,b,c0,d=c
 if x==0:return 0 if c0==0 else 1+a*inv(c0)%Q
 t=x-1;den=(c0*t+d)%Q
 return 0 if den==0 else 1+(a*t+b)*inv(den)%Q
def mask(xs):return sum(1<<x for x in xs)
def elements(m):return tuple(i for i in range(12) if m>>i&1)
def image(m,p):return sum(1<<p[i] for i in elements(m))
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3))%Q for j in range(3)] for i in range(3)]
def mv(a,x):return tuple(sum(a[i][j]*x[j] for j in range(3))%Q for i in range(3))
def mi(m):
 a=[r[:]+[int(i==j) for j in range(3)] for i,r in enumerate(m)]
 for j in range(3):
  k=next(i for i in range(j,3) if a[i][j]%Q);a[j],a[k]=a[k],a[j];s=inv(a[j][j]);a[j]=[x*s%Q for x in a[j]]
  for i in range(3):
   if i!=j:
    f=a[i][j];a[i]=[(x-f*y)%Q for x,y in zip(a[i],a[j])]
 return [r[3:] for r in a]
def ell(i):return (0,0,1) if i==0 else (1,i-1,(i-1)**2%Q)
def H(i):
 if i==0:return [[0,0,1],[1,0,0],[0,1,0]]
 t=i-1;return [[1,0,0],[-t%Q,1,0],[0,-t%Q,1]]
def cross(x,y):return ((x[1]*y[2]-x[2]*y[1])%Q,(x[2]*y[0]-x[0]*y[2])%Q,(x[0]*y[1]-x[1]*y[0])%Q)
def detcols(x,y,z):return sum(a*b for a,b in zip(cross(x,y),z))%Q
def main():
 resource.setrlimit(resource.RLIMIT_CPU,(20,20));wall=time.monotonic();assert (D/'PRED.md').exists() and not (D/'RESULT.json').exists()
 coeffs=sorted({normalize(c) for c in itertools.product(range(Q),repeat=4) if (c[0]*c[3]-c[1]*c[2])%Q})
 perms=[tuple(mobius(c,x) for x in range(12)) for c in coeffs]
 assert len(coeffs)==len(set(perms))==1320 and all(len(set(p))==12 for p in perms)
 six=[mask(c) for c in itertools.combinations(range(12),6)];seven=list(itertools.combinations(range(12),7));unseen=set(six);orbits=[]
 for m in six:
  if m not in unseen:continue
  orbit={image(m,p) for p in perms};assert orbit<=unseen;orbits.append(orbit);unseen-=orbit
 assert not unseen and len(six)==924 and len(seven)==792
 orbits.sort(key=lambda o:(len(o),min(o)));oid={m:i for i,o in enumerate(orbits) for m in o};comps=[]
 for o in orbits:
  ids={oid[FULL^m] for m in o};assert len(ids)==1;comps.append(next(iter(ids)))
 orbitinfo=[dict(id=i,size=len(o),representative_ids=list(elements(min(o))),representative_points=[POINTS[x] for x in elements(min(o))],complement_orbit=comps[i],complement_invariant=comps[i]==i) for i,o in enumerate(orbits)]
 profiles=Counter();profile_rows=[];selected=None
 def compatible(a,b,sm):return oid[sm^(1<<a)]==comps[oid[sm^(1<<b)]]
 def assignment(s):
  sm=mask(s);special=[x for x in s if len(orbits[oid[sm^(1<<x)]])==264];ordinary=[x for x in s if len(orbits[oid[sm^(1<<x)]])==660]
  if len(special)==2 and len(ordinary)==5 and compatible(*special,sm) and all(compatible(x,x,sm) for x in ordinary):return special+ordinary
  for a,b in itertools.combinations(s,2):
   if not compatible(a,b,sm):continue
   rem=[x for x in s if x not in (a,b)]
   for c,d in itertools.combinations(rem,2):
    tail=[x for x in rem if x not in (c,d)]
    if compatible(c,d,sm) and all(compatible(x,x,sm) for x in tail):return [a,b,c,d]+tail
  return None
 for s in seven:
  sm=mask(s);types=[oid[sm^(1<<p)] for p in s];counts=tuple(Counter(types)[i] for i in range(len(orbits)));profiles[counts]+=1;order=assignment(s)
  profile_rows.append(dict(mask=sm,point_ids=' '.join(map(str,s)),points=json.dumps([POINTS[x] for x in s]),puncture_orbits=' '.join(map(str,types)),profile=json.dumps(counts),reverse_compatible=bool(order)))
  if selected is None and order is not None:selected=(s,order)
 with (D/'SIX_SUBSETS.csv').open('w') as f:
  w=csv.writer(f);w.writerow(['mask','point_ids','points','orbit_id','orbit_size','complement_orbit'])
  for m in six:w.writerow([m,' '.join(map(str,elements(m))),json.dumps([POINTS[x] for x in elements(m)]),oid[m],len(orbits[oid[m]]),comps[oid[m]]])
 with (D/'SEVEN_SUBSET_PROFILES.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(profile_rows[0]));w.writeheader();w.writerows(profile_rows)
 pred_orbits=sorted(map(len,orbits))==[264,660] and all(i==c for i,c in enumerate(comps))
 pred_profile=all(Counter(len(orbits[i]) for i in [oid[mask(s)^(1<<p)] for p in s])=={264:2,660:5} for s in seven)
 actual=dict(PGL_permutations=len(perms),six_subsets=924,seven_subsets=792,orbits=orbitinfo,profile_histogram=[dict(punctures_per_orbit=list(k),seven_sets=v) for k,v in sorted(profiles.items())],predicted_orbits_supported=pred_orbits,predicted_2plus5_profile_supported=pred_profile)
 if selected is None:
  result=dict(status='NO_REVERSE_COMPATIBLE_S_IN_THIS_FIXED_LOCAL_INTERFACE',actual=actual,CPU_seconds=time.process_time(),CPU_budget_seconds=20,controller_searches=0,complete_graphs_generated=0,BFS_runs=0,Lean_compilations=0,solver_calls=0)
  (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(D/'TERMINAL.json').write_text(json.dumps(dict(running=False,**result),indent=2)+'\n');print(json.dumps(result));return
 raw,ports=selected;sm=mask(raw);bp=[sm^(1<<p) for p in ports];porttypes=[oid[b] for b in bp];allowed=[]
 images=[[image(b,p) for p in perms] for b in bp]
 for a in range(7):
  for b in range(7):
   maps=[i for i,m in enumerate(images[a]) if m==(FULL^bp[b])]
   if maps:allowed.append(dict(source_port=a,target_port=b,PGL_maps=len(maps)))
 charts=[];I3=[[1,0,0],[0,1,0],[0,0,1]];pairs=[(0,1),(2,3),(4,4),(5,5),(6,6)]
 for a,b in pairs:
  choices=[i for i,m in enumerate(images[a]) if m==(FULL^bp[b])];assert choices
  idx=choices[0];aa,bb,cc,dd=coeffs[idx];block=[[1,0,0],[0,dd,cc],[0,bb,aa]];T=mm(mi(H(ports[b])),mm(block,H(ports[a])));Tr=mi(T)
  stem=f'cross_{a}_{b}' if a!=b else f'self_{a}'
  charts.append(dict(chart_id=stem+('_forward' if a!=b else '_plus'),source_port=a,target_port=b,matrix=T,literal_inverse=Tr,PGL_coefficients=list(coeffs[idx]),PGL_permutation=list(perms[idx]),compatible_PGL_maps=len(choices)))
  charts.append(dict(chart_id=stem+('_reverse' if a!=b else '_minus'),source_port=b,target_port=a,matrix=Tr,literal_inverse=T,reverse_is_actual_3x3_inverse=True,forward_chart=charts[-1]['chart_id']))
 checks=[];allpoints=set(itertools.product(range(Q),repeat=3))
 for chart in charts:
  a,b=chart['source_port'],chart['target_port'];T,Tr=chart['matrix'],chart['literal_inverse'];ea,eb=ell(ports[a]),ell(ports[b])
  assert mm(T,Tr)==mm(Tr,T)==I3 and mv(T,ea)==eb and mv(Tr,eb)==ea
  turns=[]
  for s in range(7):
   if s==a:continue
   for t in range(7):
    if t==b:continue
    det=detcols(eb,mv(T,ell(ports[s])),ell(ports[t]));assert det!=0;turns.append([s,t,det])
  planes=[];union=set()
  for before in [True,False]:
   for s in range(7):
    if s==(a if before else b):continue
    v=mv(T,ell(ports[s])) if before else ell(ports[s]);normal=normalize(cross(eb,v));points={tuple((x*eb[j]+y*v[j])%Q for j in range(3)) for x,y in itertools.product(range(Q),repeat=2)}
    assert len(points)==121;union|=points;planes.append(dict(family='transported_source' if before else 'target',other_port=s,normal=list(normal)))
  assert len(planes)==len({tuple(p['normal']) for p in planes})==12 and union==allpoints
  chart['checks']=dict(two_sided_literal_inverse=True,portline_exact_coefficient1=True,NBturns=36,all_NBturn_determinants_nonzero=True,adjacent_planes=12,adjacent_union=1331,noise_reverse='-t mod11')
  checks.append(dict(chart_id=chart['chart_id'],turn_determinants=turns,planes=planes,**chart['checks']))
 reverse=[1,0,3,2,4,5,6];assert all(any(x['source_port']==p and x['target_port']==reverse[p] for x in charts) for p in range(7))
 params=dict(field='Prime field F11; ordinary integer arithmetic modulo11',PG1_point_ids=POINTS,actual=actual,selected_raw_ids=list(raw),selected_raw_points=[POINTS[x] for x in raw],
  selected_role_order_ids=ports,selected_role_order_points=[POINTS[x] for x in ports],port_orbit_ids=porttypes,port_orbit_sizes=[len(orbits[i]) for i in porttypes],
  directions=[list(ell(p)) for p in ports],reverse_ports=reverse,H=[H(p) for p in ports],H_inverse=[mi(H(p)) for p in ports],
  puncture_B_ids=[list(elements(b)) for b in bp],allowed_source_target_pairs=allowed,actual_charts=charts,
  selection_rule='First lexicographic seven-set in PG1order[inf,0,...10]with complete reverse-compatible assignment;264special2before660ordinary5when profile holds.',
  matrix_transport='T=H_target^-1*diag(1,Qf)*H_source;Qf=[[d,c],[b,a]]',inverse_rule='Actual3x3matrix inverse; no projective rescaling',noise_reverse='-t mod11',scope='One r7/q11 local interface only; no controller or graph.')
 (D/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n');(D/'CHART_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
 result=dict(status='PASS_FIXED_R7_F11_TYPED_PORT_LOCAL_RANK_PENCIL_INTERFACE',**actual,selected_ports=params['selected_role_order_points'],port_orbit_sizes=params['port_orbit_sizes'],
  allowed_directed_port_pairs=len(allowed),actual_chart_records=10,unique_actual_matrices=len({tuple(sum(c['matrix'],[])) for c in charts}),
  literal_inverse_checks=10,exact_portline_checks=10,NBturn_determinants_checked=360,all_turns_rank3=True,adjacent_pencils_checked=10,planes_per_pencil=12,vectors_per_adjacent_union=1331,
  controller_searches=0,complete_graphs_generated=0,BFS_runs=0,Lean_compilations=0,solver_calls=0,other_fields_or_parameters_tested=0,CPU_seconds=time.process_time(),wall_seconds=time.monotonic()-wall,CPU_budget_seconds=20,workers=1,
  global_graph_or_general_q_claim=False,next='Return local interface and actualdata to root/complementary agent; no controller/graph/q ladder continuation.')
 assert result['CPU_seconds']<20
 (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(D/'TERMINAL.json').write_text(json.dumps(dict(status=result['status'],running=False,CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=20,next=result['next']),indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','PGL_permutations','predicted_orbits_supported','predicted_2plus5_profile_supported','selected_ports','port_orbit_sizes','allowed_directed_port_pairs','NBturn_determinants_checked','CPU_seconds']}))
if __name__=='__main__':main()
