from pathlib import Path
import json,subprocess,resource,time,shutil
B=Path(__file__).resolve().parent;R=B.parents[5];S=R/'research/ddp/more_graphs_20261027/d11_D4_current3645';t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert (S/'source3645.header.edges').exists();assert not (B/'RESULT.json').exists()
shutil.copyfile(S/'source3645.header.edges',B/'SOURCE.header.edges');holes=load(S/'absorbed_pair_probe/FREE_R3_CACHE.json')['missing'];assert len(holes)==743;(B/'HOLES.txt').write_text('743\n'+' '.join(map(str,holes))+'\n')
rows={};bindings=[]
for folder,meta,raw in [('absorbed_pair_probe','ENDPOINT_CACHE.json','endpoint_R3.u64le.bin'),('absorbed_switch_probe','NEW_R3_CACHE.json','new_R3.u64le.bin')]:
 d=load(S/folder/meta);roots=d['roots'] if folder=='absorbed_pair_probe' else d['new_roots'];data=(S/folder/raw).read_bytes();assert len(data)==len(roots)*57*8
 for i,r in enumerate(roots):
  row=data[i*456:(i+1)*456]
  if r in rows:assert rows[r]==row
  else:rows[r]=row
 bindings.append({'metadata':str((S/folder/meta).relative_to(R)),'raw':str((S/folder/raw).relative_to(R)),'roots':len(roots)})
(B/'CACHED_ROOTS.txt').write_text(f'{len(rows)} 57\n'+' '.join(map(str,sorted(rows)))+'\n')
with (B/'CACHED_R3.bin').open('wb') as out:
 for r in sorted(rows):out.write(rows[r])
save('CACHE_BINDING.json',{'source':str((S/'source3645.header.edges').relative_to(R)),'old_source_D4':'inherited,notrevalidated','old_holes_source':str((S/'absorbed_pair_probe/FREE_R3_CACHE.json').relative_to(R)),'holes':743,'input_caches':bindings,'unique_cached_roots':len(rows),'new_R3_queries_expected':3645-len(rows),'same_root_old_rows_equal':True})
c0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['g++','-O2','-std=c++17','run.cpp','-o','run'],cwd=B,capture_output=True,text=True);c1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'COMPILE.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
def limit():resource.setrlimit(resource.RLIMIT_CPU,(10,10))
r0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['./run'],cwd=B,capture_output=True,text=True,timeout=20,preexec_fn=limit);r1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'RUN.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
n=load(B/'NATIVE_RESULT.json');compilecpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime;childcpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime;parentcpu=time.process_time()-t0
r={'status':'COMPLETE_D4_CANDIDATE3646_PENDING_NEW_ACCEPTANCE' if n['full_D4_hit'] else 'COMPLETE_NO_ANY_SINGLE_SOURCE_CUT_ONLY_NEW_STAR_MAX11_D4','native':n,'prediction_inserted_layer_pass_supported':n['classes'].get('inserted_inserted',{}).get('newroot_pass',0)>0,'old_source_D4_revalidation_BFS':0,'old_free_R3_recomputed':False,'compile_CPU':compilecpu,'child_CPU':childcpu,'parent_CPU':parentcpu,'prior_read_CPU':1.0,'new_read_CPU_charge':.5,'prepare_CPU_charge':.25,'failed_input_preparation_CPU_charge':.1,'case_CPU':1.85+compilecpu+childcpu+parentcpu,'case_cap':15,'new_accepted_graph_parameter_Lean':[0,0,0],'new_Lean_ARIS_solver':0,'scope':'actual3645;deleteexactlyoneoriginaledge;addonevertexwithonlynewoldspokes;maximallegalP=all7freepluscutendsdominatesallsubsets;otheroldedgeskeep;noextraoldoldrepairs','terminal':True,'next':'newacceptanceifhit;elseSTOP_NO_AUTOMATIC_SECOND_CUT_OR_REPAIR_SEED'}
assert r['case_CPU']<15
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))
