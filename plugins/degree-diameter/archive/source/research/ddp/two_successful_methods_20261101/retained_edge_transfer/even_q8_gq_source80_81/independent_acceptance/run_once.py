import csv,json,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;G=D.parents[1]/'even_q8_gq_geometry_pilot'
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
def tsv(name):
 with (G/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
geom=[]
for name,pointfile,np,nl in [('derived','DERIVED_POINTS.tsv',512,640),('balanced','PG3_POINTS.tsv',585,585)]:
 rows=tsv(pointfile)
 assert len(rows)==np and [int(r['point']) for r in rows]==list(range(np))
 mapping=[dict(point=int(r['point']),original_point=int(r.get('original_point',r['point'])),coordinates=[int(r[k]) for k in ['x0','x1','x2','x3']]) for r in rows]
 geom.append(dict(case=name,points=np,lines=nl,old_label='p*nl+l',point_data=str(G/pointfile),ordered_point_mapping=mapping))
inputbinding=dict(status='BOUND_PRIOR_ACCEPTED_Q8_COORDINATE_AND_INDEX_DATA',cases=geom,
 prior_geometry_proof=str(G/'RESULT.json'),new_field_law_checks=0,new_small_projection_checks=0,
 new_graph_formula_checked_by='complete literal edges against corresponding accepted incidence matrices',
 actual_original_derivation_point_ID=2)
(D/'INPUT_DATA_BINDING.json').write_text(json.dumps(inputbinding,indent=2)+'\n')
phases=[]
def call(args,name,limit):
 before=cpu()
 def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
 with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
  p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
  (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid,phase=name,single_worker=True,CPU_budget_seconds=150),indent=2)+'\n')
  rc=p.wait()
 phases.append(dict(phase=name,returncode=rc,CPU_seconds_including_driver=cpu()-before))
 return rc
rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:
 remaining=150-cpu()
 rc=call(['./verify','..',str(G),str(min(140,remaining-3))],'validate',min(145,int(remaining-1)))
result=json.loads((D/'RESULT.json').read_text()) if (D/'RESULT.json').exists() else None
if rc==0:
 assert result['actual_helper_R3_BFS_roots']==129 and result['actual_old_R3_BFS_roots']==0
 assert result['source_graph_literal_parses']==4 and len(result['cases'])==2
 for c in result['cases']:
  case=D/c['case'];(case/'SUMMARY.json').write_text(json.dumps(c,indent=2)+'\n')
  text=(f"# {c['case']}: filled graph independent acceptance PASS\n\n"
        f"n={c['filled_n']}, m={c['filled_m']}, all vertices degree{c['degree_cap']}. "
        f"Entire unfilled oldbody of {c['old_edge_body_retained_exact']}edges retained exactly; all old/new edges and complete degrees match the accepted geometry formulas. "
        f"All {c['actual_helper_R3_BFS_roots']}new helper roots have measured histogram {c['actual_helper_histogram']}. "
        f"Actual no-distance<=2 witness is {c['actual_nonD2_witness']}. "
        "Old all-pairs projection routes, all-helper measurements and old-only-interior prefix proof give exactD3 for the endpoint and each actual helper prefix. "
        "No oldrootR3BFS, field laws, smallGQprojections or Lean were rerun. Unfilled source is a reproduction only.\n")
  (case/'RESULT.md').write_text(text);(case/'PROOF.md').write_text(text+'\nSee ../PROOF.md for explicit genuine-Walk, completeness and prefix arguments.\n')
 (D/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
 (D/'RESULT.md').write_text('# Both q8 filled source graphs: independent acceptance PASS\n\n'
   'Derived327744/80 and balanced342290/81 pass full graph-level binding, all129newhelper ordinaryBFS and all-pair/currentprefix proof. Classical unfilled sources are reproductions. See PROOF.md and per-case evidence. No newLean or globalpriority claim.\n')
terminal=dict(status='PASS' if rc==0 else 'PARTIAL_OR_FAILED',returncode=rc,
 total_CPU_seconds_including_geometry_data_binding_compile_four_files_129helper_BFS_and_aggregation=cpu(),
 wall_seconds=time.time()-wall,CPU_budget_seconds=150,single_worker=True,all_children_terminal=True,
 phases=phases,result=result,
 measurement_boundary='One recipe/index-data binding, compiler, validator and output aggregation batch. Four whole literal files, two actualfilled CSR graphs,129newhelperR3BFS, two actualshortpath witness checks. Zero prior field/smallGQprojection or oldrootR3 revalidation. Interactive authoring and read-only inspection excluded.')
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',returncode=rc,all_children_terminal=True),indent=2)+'\n')
print(json.dumps(terminal,indent=2));raise SystemExit(rc)
