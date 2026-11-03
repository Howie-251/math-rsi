from pathlib import Path
import json, resource, subprocess
HERE=Path(__file__).resolve().parent
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();assert not (HERE/'prepare.terminal.json').exists()
scope=json.loads((HERE/'STRUCTURE_SCOPE.json').read_text())
Q=sorted({pow(4,i,61) for i in range(30)});NON=sorted(set(range(1,61))-set(Q));phase=[[i,j] for i in range(16) for j in range(30) if i%5 and (i+j)%5==0]
assert Q==scope['Q'] and NON==scope['N'] and phase==scope['filtered_full_index_pairs']
assert len(phase)==72 and len(Q)==len(NON)==30 and len(phase)*30**3==1944000
expected={'raw_HH_generating_sets':729000000,'after_unique_Q_cross_scaling':24300000,'after_safe_first_index_sign_restriction':12960000,'after_formal_word_necessary_bound':1944000};assert scope['counts']==expected
with (HERE/'scope_tables.hpp').open('w') as f:
 f.write('static const int SQ[30]={'+','.join(map(str,Q))+'};\n')
 f.write('static const int NON[30]={'+','.join(map(str,NON))+'};\n')
 f.write('static const int PHASE[72][2]={'+','.join('{'+','.join(map(str,z))+'}' for z in phase)+'};\n')
metadata={'parameters':scope['parameters'],'source_scope':'STRUCTURE_SCOPE.md','necessary_formal_filter':'WORD_PATTERNS.tsv',
 'scope_chain':expected,'actual_original_BB_inputs':1944000,'other_parent_inputs_not_BFS_scored':True,
 'safe_sign_layers':'0..15 first, complete fixed layers before the separate necessary word filter',
 'word_filter':'b=-a nonzero modulo5','retained_phase_pairs':phase,
 'order':'phase pairs in lexicographic i,j order, y ascending N, u ascending Q, v ascending N',
 'Q':Q,'N':NON,'parameters_each':'A=(1,1,i), B=(y,1,j), I=(u,0,15), J=(v,0,15); include the two true cross inverses',
 'actual_action_multiplier':4,'faithful_previous_multiplier3_not_reused':True,
 'group_product':'(x,w,i)(y,v,j)=(x+4^i*y mod61,w+v mod3,i+j mod30)',
 'inverse':'(-4^-i*x mod61,-w mod3,-i mod30)',
 'group_encoding':'x+61*w+183*i','leaf_parent':'5490+(g mod183)+183*((g div183) mod5)',
 'block_parent':'6405+(block-5490) mod183','head_triangles':61,'head_triangle_edges':183,
 'BB_mask_storage':'5 uint64 masks; all33 bits retained; zero-bit indices0,11,22 have weight1 and are always covered, other bits weight6',
 'preflight_then_complete_range':True,'preflight_cached_as_cursor0_no_duplicate_BFS':True,
 'population_for_root_statistics':'actual BB survivors only; minBB fallback separate if zero survivors',
 'CPU_limit_seconds':90,'worker_count':1,'independent_final_parent_owned':True}
(HERE/'production.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'production.cpp'),'-o',str(HERE/'production')],check=True);compile_cpu=cpu()-before
subprocess.run([str(HERE/'production'),'preflight',str(HERE),'3'],check=True)
check=json.loads((HERE/'preflight.check.json').read_text());assert check['all_915_BB_targets_match']
out={'status':'PREPARED_AND_PREFLIGHT_MATCHED','CPU_seconds':cpu()-start,'compile_CPU_seconds':compile_cpu,
 'preflight_CPU_seconds':check['CPU_seconds'],'actual_original_BB_scope':1944000,'actual_phase_pairs':72,
 'original_BB_targets_matched':915,'preflight_expanded_graphs':1,'preflight_complete_roots':3}
(HERE/'prepare.terminal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
