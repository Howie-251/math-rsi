import csv,json,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;GEOM=D.parents[2]/'even_q8_gq_geometry_pilot'
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
with (GEOM/'OVOID65.tsv').open() as f:O=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['i']))
with (GEOM/'SPREAD65.tsv').open() as f:S=sorted(csv.DictReader(f,delimiter='\t'),key=lambda r:int(r['spread']))
assert len(O)==len(S)==65
o=[int(r['point']) for r in O];owner=[int(r['spreadowner']) for r in O];s=[int(r['original_line']) for r in S]
assert len(set(o))==len(set(owner))==len(set(s))==65
(D/'center_input.h').write_text('constexpr int ovoid[65]={'+','.join(map(str,o))+'};\nconstexpr int ovoid_owner[65]={'+','.join(map(str,owner))+'};\nconstexpr int spread[65]={'+','.join(map(str,s))+'};\n')
(D/'INPUT_BINDING.json').write_text(json.dumps(dict(accepted_ovoid=str(GEOM/'OVOID65.tsv'),accepted_spread=str(GEOM/'SPREAD65.tsv'),ovoid_points=o,spread_lines=s,ovoid_owner=owner,label='center=o_i*585+S_j; h=65i+j; new342290+h',field_or_geometry_revalidation=False),indent=2)+'\n')
phases=[]
def call(args,name,limit):
 before=cpu()
 def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
 with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
  p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
  (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid,phase=name,single_worker=True,CPU_budget_seconds=120),indent=2)+'\n')
  rc=p.wait()
 phases.append(dict(phase=name,returncode=rc,CPU_seconds_including_driver=cpu()-before))
 return rc
rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:
 remaining=120-cpu()
 rc=call(['./verify','../../balanced/graph_d81_D3_n342290.edges','../graph_d82_D3_n346515.edges',str(min(110,remaining-3))],'validate',min(115,int(remaining-1)))
result=json.loads((D/'RESULT.json').read_text()) if (D/'RESULT.json').exists() else None
if rc==0:
 assert result['actual_newroot_R3_BFS_roots']==4225
 assert result['source_literal_parses']==result['candidate_literal_parses']==1
 (D/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
 (D/'RESULT.md').write_text('# Degree82 /346515: independent mathematical acceptance PASS\n\nComplete graph n346515/m14204970, degree81:4290/degree82:342225. Full sourcebody retained exactly; all4225 sourceN81/cloneN81 lists bound,342225disjointpins source minusD65 including65oldfills. All4225ordinarynewrootBFS match65diag(1,81,5249,341184) and4160off(1,81,5329,341104). Source old-only allpair/prefix genuineWalk and collapse nonD2 proof in PROOF.md. No oldrootBFS/sourceR2/field/projection/Lean/solver rerun; no rootcount or globalpriority claim.\n')
terminal=dict(status='PASS' if rc==0 else 'PARTIAL_OR_FAILED',returncode=rc,
 total_CPU_seconds_including_small_input_binding_compile_both_files_4225BFS_and_aggregation=cpu(),
 wall_seconds=time.time()-wall,CPU_budget_seconds=120,single_worker=True,all_children_terminal=True,phases=phases,result=result,
 measurement_boundary='One independent compile/validator batch; oneparse each acceptedsource andcompletecandidate, all4225literalN81bindings,degree/prefix andordinarynewrootBFS,aggregation. Interactive authoring excluded.')
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',returncode=rc,all_children_terminal=True),indent=2)+'\n')
print(json.dumps(terminal,indent=2));raise SystemExit(rc)
