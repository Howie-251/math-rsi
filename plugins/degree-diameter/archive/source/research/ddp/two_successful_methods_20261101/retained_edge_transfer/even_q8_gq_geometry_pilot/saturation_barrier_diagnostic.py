import csv,json,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
start=time.process_time();wall=time.time();D=Path(__file__).resolve().parent
original=json.loads((D/'RESULT.json').read_text())
def rows(path):
 with (D/path).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def diagnostic(name,s,t,Ofile,Ocol,Sfile,Scol,Ifile,npoints,nlines):
 R=s*t+1;delta=(s+1)*(t+1)
 oo=sorted(rows(Ofile),key=lambda r:int(r['i']));O=[int(r[Ocol]) for r in oo]
 ss=sorted(rows(Sfile),key=lambda r:int(r['spread']));S=[int(r[Scol]) for r in ss]
 lines={}
 for row in rows(Ifile):lines.setdefault(int(row['line']),set()).add(int(row['point']))
 assert len(O)==len(S)==R and len(set(O))==R
 spreadpoints=[lines[l] for l in S]
 flags=[[int(p in L) for L in spreadpoints] for p in O]
 sigma=[]
 for i,f in enumerate(flags):
  owners=[j for j,a in enumerate(f) if a]
  assert len(owners)==1,(name,'ovoid_spread_owner',i,owners)
  sigma.append(owners[0])
 assert len(set(sigma))==R
 pointlines={p:set() for p in O}
 for l,points in lines.items():
  for p in O:
   if p in points:pointlines[p].add(l)
 commonO=[[len(pointlines[p]&pointlines[q]) for q in O] for p in O]
 commonS=[[len(a&b) for b in spreadpoints] for a in spreadpoints]
 with (D/('SATURATION_'+name+'_OFFDIAGONAL_TO_D.csv')).open('w') as f:
  w=csv.writer(f);w.writerow(['ovoid_index','spread_index','point','spread_line','diag_targets_tested','adjacent_targets','old_two_step_targets','fill_two_step_targets'])
  paircount=0;centercount=0;examples={}
  for i in range(R):
   for j in range(R):
    if j==sigma[i]:continue
    adjcount=old2count=fill2count=0
    assert flags[i][j]==0
    for r in range(R):
     direct=flags[r][j]*flags[i][sigma[r]]
     commonold=commonS[j][sigma[r]]*commonO[i][r]
     commonfill=0
     paircount+=1;adjcount+=bool(direct);old2count+=bool(commonold)
     if direct or commonold:
      raise AssertionError((name,'offdiag_to_D_counterexample',i,j,r,direct,commonold))
     kind='same_point' if i==r else ('same_spread' if j==sigma[r] else 'different_point_and_spread')
     if kind not in examples:examples[kind]=dict(i=i,j=j,r=r,center=[O[i],S[j]],diagonal=[O[r],S[sigma[r]]],adjacency=direct,common_old_neighbors=commonold,common_fill_neighbors=commonfill)
    centercount+=1;w.writerow([i,j,O[i],S[j],R,adjcount,old2count,fill2count])
 diagonalpairs=0
 for i in range(R):
  for r in range(i):
   direct=flags[r][sigma[i]]*flags[i][sigma[r]]
   commonold=commonS[sigma[i]][sigma[r]]*commonO[i][r]
   commonfill=int(sigma[i]==sigma[r])
   assert not(direct or commonold or commonfill),(name,'D_pair_counterexample',i,r)
   diagonalpairs+=1
 assert paircount==R*R*(R-1) and centercount==R*(R-1)
 assert delta*R*R==npoints*nlines
 matrices=dict(name=name,R=R,ovoid_points=O,spread_line_ids=S,ovoid_spread_owner=sigma,geometry_lines_through_O_pairs=commonO,spread_intersection_sizes=commonS)
 result=dict(name=name,status='PASS_SELECTED_SET_ZERO_ONE_TWO_ROUTE_DIAGNOSTIC',s=s,t=t,R=R,delta=delta,
  offdiagonal_centers_tested=centercount,offdiag_to_D_pairs_tested=paircount,offdiag_D_adjacencies=0,offdiag_D_common_old_neighbors=0,offdiag_D_common_fill_neighbors=0,
  distinct_D_pairs_tested=diagonalpairs,D_pair_adjacencies=0,D_pair_common_neighbors=0,
  selected_set_witnesses=examples,conditional_unfilled_source_order=npoints*nlines,conditional_filled_source_order=npoints*nlines+R,
  conditional_pin_union_size=delta*R*R,conditional_old_free_vertices=R,
  pin_union_binding='every filledsource vertex except D; proved by unique O-on-line and spreadowner, not by constructing source vertices',
  k_scope='positive integer; k full immutable-neighborhood copies per center',
  original_helper_degree_lower_bound=R*(R-1),stronger_helper_degree_lower_bound=R*R,
  singlehelper_impossible_when='delta+k<R^2',largest_integer_k_excluded_by_stronger_bound=R*R-delta-1,
  source_D3_instantiated_here=False,exact_distance_three_claim='conditional on source/fullNcopy D3; lower bound no short route does not need D3',
  large_source_vertices_generated=0,large_source_edges_generated=0)
 return result,matrices
try:
 a,am=diagnostic('BALANCED_Q8',8,8,'OVOID65.tsv','point','SPREAD65.tsv','original_line','ORIGINAL_INCIDENCE.tsv',585,585)
 b,bm=diagnostic('PAYNE_Q8',7,9,'OVOID64.tsv','derived_point','DERIVED_SPREAD64.tsv','derived_line','DERIVED_INCIDENCE.tsv',512,640)
 (D/'SATURATION_SELECTED_GEOMETRY_MATRICES.json').write_text(json.dumps([am,bm],indent=2)+'\n')
 result=dict(status='PASS_SELECTED_GEOMETRY_AND_CONDITIONAL_SINGLEHELPER_BARRIER',cases=[a,b],
  new_field_checks=0,new_sourcegraphs=0,new_BFS=0,new_Lean=0,new_solver=0,new_q=0,
  source_orders_are_conditional=True,no_new_graph_or_record_claimed=True,
  excluded_scope=['simultaneous helper batches with new mutual edges','changing existing edges','different initial center code','arbitrarily large k with cap at least R^2'],
  all_processes_terminal=True,CPU_budget_seconds=5,diagnostic_CPU_seconds=time.process_time()-start)
 (D/'SATURATION_BARRIER_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 terminal=dict(status='PASS',single_worker=True,all_processes_terminal=True,total_diagnostic_CPU_seconds=time.process_time()-start,wall_seconds=time.time()-wall,CPU_budget_seconds=5,result_file='SATURATION_BARRIER_RESULT.json',measurement_boundary='One Python paper/selected-incidence diagnostic and output aggregation; interactive authoring excluded.')
 (D/'SATURATION_BARRIER_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 print(json.dumps(dict(terminal=terminal,cases=[dict(name=c['name'],route_pairs=c['offdiag_to_D_pairs_tested'],D_pairs=c['distinct_D_pairs_tested'],helper_bound=c['stronger_helper_degree_lower_bound']) for c in [a,b]]),indent=2))
except Exception as e:
 result=dict(status='FAIL_COUNTEREXAMPLE',reason=str(e),CPU_seconds=time.process_time()-start)
 (D/'SATURATION_BARRIER_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 (D/'SATURATION_BARRIER_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
 raise
