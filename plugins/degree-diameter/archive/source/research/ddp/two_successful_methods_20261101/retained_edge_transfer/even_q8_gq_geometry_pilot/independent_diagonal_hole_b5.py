import csv,json,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(15,16))
start=time.process_time();wall=time.time();D=Path(__file__).resolve().parent
def tsv(name):
 with (D/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def csvrows(name):
 with (D/name).open() as f:yield from csv.DictReader(f)
oldmat={a['name']:a for a in json.loads((D/'SATURATION_SELECTED_GEOMETRY_MATRICES.json').read_text())}
def run(name,s,t,Ofile,Ocol,Sfile,Scol,Ifile,Projfile,Intersectfile,Intersectcol,np,nl):
 R=s*t+1;delta=(s+1)*(t+1);Delta=delta+1;I=list(range(5));b=5
 O=[int(r[Ocol]) for r in sorted(tsv(Ofile),key=lambda r:int(r['i']))]
 S=[int(r[Scol]) for r in sorted(tsv(Sfile),key=lambda r:int(r['spread']))]
 lines={l:set() for l in range(nl)};plines={p:set() for p in range(np)}
 for r in tsv(Ifile):
  l,p=int(r['line']),int(r['point']);lines[l].add(p);plines[p].add(l)
 pointowner={}
 for j,l in enumerate(S):
  for p in lines[l]:pointowner[p]=j
 sigma=[pointowner[p] for p in O];holecols={sigma[h] for h in I}
 mat=oldmat[name];assert mat['ovoid_points']==O and mat['ovoid_spread_owner']==sigma and mat['spread_line_ids']==S
 outI=[i for i in range(R) if i not in I];outJ=[j for j in range(R) if j not in holecols]
 wanted={(O[i],S[sigma[h]]) for i in outI for h in I}|{(O[h],S[j]) for h in I for j in outJ}
 pred={}
 for r in csvrows(Projfile):
  key=int(r['point']),int(r['line'])
  if key in wanted:pred[key]=(int(r['projection_point']),int(r['connector_line']))
 assert set(pred)==wanted
 oi={p:i for i,p in enumerate(O)}
 lineO={int(r['line']):oi[int(r[Intersectcol])] for r in csvrows(Intersectfile)}
 freed={h:[(p,l) for p in sorted(lines[S[sigma[h]]]) for l in sorted(plines[O[h]]) if (p,l)!=(O[h],S[sigma[h]])] for h in I}
 for h,pins in freed.items():
  assert len(pins)==delta-1
  for p,l in pins:assert pointowner[p]==sigma[h] and lineO[l]==h
 pc={(p,i):len(plines[p]&plines[O[i]]) for h in I for p,l in freed[h] for i in outI}
 lc={(l,j):len(lines[l]&lines[S[j]]) for h in I for p,l in freed[h] for j in outJ}
 targetcount=pinchecks=positives=fillchecks=Dchecks=0
 routefile=D/('INDEPENDENT_DIAGONAL_HOLE_'+name+'_B5_ROUTE_PINS.tsv')
 targetfile=D/('INDEPENDENT_DIAGONAL_HOLE_'+name+'_B5_TARGETS.csv')
 with routefile.open('w') as rf,targetfile.open('w') as tf:
  rw=csv.writer(rf,delimiter='\t');rw.writerow(['target_i','target_j','target_oldlabel','hole_i','hole_spread_col','pin_point','pin_line','pin_oldlabel','middle_point','middle_line','middle_oldlabel','source_route_length'])
  tw=csv.writer(tf);tw.writerow(['target_i','target_j','old_pin_routes','one_per_hole','freed_fill_shortcuts','D_shortcuts','remaining_clone_shortcuts'])
  for i in outI:
   for j in outJ:
    if j==sigma[i]:continue
    targetcount+=1;selected=[]
    for h in I:
     hit=[]
     for p,l in freed[h]:
      pinchecks+=1
      assert not(O[i] in lines[l] and p in lines[S[j]])
      common=pc[p,i]*lc[l,j]
      if common:assert common==1;hit.append((p,l))
     assert len(hit)==1,(name,'oldpin_count',i,j,h,hit)
     p,l=hit[0];pstar,Mstar=pred[O[i],S[sigma[h]]];qstar,Lstar=pred[O[h],S[j]]
     assert (p,l)==(pstar,Lstar)
     assert p!=O[h] and l!=S[sigma[h]] and p not in lines[l]
     assert qstar in lines[l] and p in lines[Mstar] and qstar in lines[S[j]] and O[i] in lines[Mstar]
     v=p*nl+l;w=qstar*nl+Mstar;c=O[i]*nl+S[j]
     assert v!=w and w!=c and v!=c
     rw.writerow([i,j,c,h,sigma[h],p,l,v,qstar,Mstar,w,2])
     selected.append(v);positives+=1
     # Fill f_sigma(h) can have a length-two route to c only through a flag
     # whose point is on both spread lines; this intersection is empty.
     assert not(lines[S[sigma[h]]]&lines[S[j]])
     assert O[i] not in lines[S[j]]
     fillchecks+=1
    assert len(set(selected))==5
    for r in range(R):
     direct=int(O[r] in lines[S[j]])*int(O[i] in lines[S[sigma[r]]])
     commonold=mat['spread_intersection_sizes'][j][sigma[r]]*mat['geometry_lines_through_O_pairs'][i][r]
     assert direct==commonold==0
     Dchecks+=1
    tw.writerow([i,j,5,True,0,0,0])
 assert targetcount==(R-5)*(R-6) and positives==5*targetcount
 scalars=[]
 for k in range(1,6):
  lhs=(R-k)*(R-k-1);rhs=(k+1)*(k+2)*Delta
  assert lhs>rhs
  scalars.append(dict(holes=k,helpers=k+1,outside_targets=lhs,clone_cover_upper=rhs,gap=lhs-rhs))
 return dict(name=name,status='PASS_ONE_SELECTED_B5_ROUTE_TABLE',R=R,delta=delta,Delta=Delta,
  selected_hole_ovoid_indices=I,actual_hole_point_IDs=[O[h] for h in I],actual_hole_spread_columns=sorted(holecols),
  inherited_projection_rows=len(pred),new_GQ_projection_revalidation=0,
  outside_targets_tested=targetcount,freed_oldpair_pin_candidates_tested=pinchecks,positive_oldpin_routes=positives,
  each_target_exactly_five_distinct_oldpins=True,each_hole_exactly_one=True,
  freed_fill_shortcut_checks=fillchecks,freed_fill_shortcuts=0,
  inherited_D_matrix_route_lookups=Dchecks,D_shortcuts=0,
  unique_freedpin_center_owner_checked=True,remaining_clone_shortcuts=0,
  b1_to_b5_scalar_necessary_conditions=scalars,arbitrary_subset_result_requires_paper_proof=True)
try:
 a=run('BALANCED_Q8',8,8,'OVOID65.tsv','point','SPREAD65.tsv','original_line','ORIGINAL_INCIDENCE.tsv','ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv','OVOID65_LINE_INTERSECTIONS.csv','ovoid_point',585,585)
 b=run('PAYNE_Q8',7,9,'OVOID64.tsv','derived_point','DERIVED_SPREAD64.tsv','derived_line','DERIVED_INCIDENCE.tsv','DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv','OVOID64_DERIVED_LINE_INTERSECTIONS.csv','derived_ovoid_point',512,640)
 result=dict(status='PASS_SELECTED_B5_DIAGNOSTIC_SUPPORTS_DIAGONAL_HOLE_BOUND',cases=[a,b],
  new_field_checks=0,new_GQ_projection_revalidation=0,large_graph_reads_or_generation=0,BFS_runs=0,Lean_runs=0,solver_runs=0,
  original_owner_toy_repeated=False,b6_run=False,all_processes_terminal=True,CPU_budget_seconds=15,
  diagnostic_CPU_seconds=time.process_time()-start)
 (D/'INDEPENDENT_DIAGONAL_HOLE_REPAIR_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 terminal=dict(status='PASS',single_worker=True,all_processes_terminal=True,total_CPU_seconds=time.process_time()-start,
  wall_seconds=time.time()-wall,CPU_budget_seconds=15,
  measurement_boundary='One b5 selected subset per geometry in one Python run; reads accepted Inc and selected prior projection/matrix receipts, new freedpin route enumeration and aggregation only. Interactive authoring excluded.')
 (D/'INDEPENDENT_DIAGONAL_HOLE_REPAIR_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 print(json.dumps(dict(terminal=terminal,cases=[dict(name=c['name'],holecols=c['actual_hole_spread_columns'],targets=c['outside_targets_tested'],pins=c['positive_oldpin_routes'],candidate_checks=c['freed_oldpair_pin_candidates_tested']) for c in [a,b]]),indent=2))
except Exception as e:
 r=dict(status='FAIL_COUNTEREXAMPLE',reason=str(e),CPU_seconds=time.process_time()-start)
 (D/'INDEPENDENT_DIAGONAL_HOLE_REPAIR_RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
 (D/'INDEPENDENT_DIAGONAL_HOLE_REPAIR_COUNTEREXAMPLE.json').write_text(json.dumps(r,indent=2)+'\n')
 raise
