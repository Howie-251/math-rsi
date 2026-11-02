"""Filter the actual original scope by unique projected S keys, then preserve all lifts."""
from pathlib import Path
import json
import resource
import subprocess
HERE=Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
st=json.loads((HERE/'structure.json').read_text());internal=json.loads((HERE/'internal_options.json').read_text())
allowed=json.loads((HERE/'QUOTIENT_BB_ALLOWED.json').read_text())
keys={tuple(x) for x in allowed['allowed_unique_projected_S']};assert len(keys)==16
ACTION=st['K_action_table'];KI=st['K_inverse_table'];NEG=st['A_negative']
GI=[NEG[ACTION[KI[g//147]][g%147]]+147*KI[g//147] for g in range(6174)]
def project(g):
    x=g%147;return x//7%7+7*(x//49)+21*(g//147//7)
ca=[[project(50+147*7*j),project(GI[50+147*7*j])] for j in range(6)]
cb=[[project(56+147*7*j),project(GI[56+147*7*j])] for j in range(6)]
actual=[];branches=[];offset=0;blocks=0
for branch,options in enumerate(internal):
    passed=0
    for idx,S0 in enumerate(options):
        sp=[project(s) for s in S0]
        for ja in range(6):
            for jb in range(6):
                blocks+=1
                canonical=tuple(sorted(set(ca[ja]+cb[jb]+sp)))
                if canonical not in keys:continue
                scope_base=offset+((idx*6+ja)*6+jb)*49
                actual.append({'branch':branch,'internal_index':idx,'cross_a_index':ja,'cross_b_index':jb,
                               'original_scope_base':scope_base,'internal_S':S0})
                passed+=1
    raw=len(options)*36*49
    row={'branch':branch,'full_normalized_inputs':raw,'quotient_blocks':len(options)*36,
         'passing_quotient_blocks':passed,'original_BB_inputs':passed*49,
         'quotient_rejected_original_inputs':raw-passed*49,'original_cursor_start':offset,'original_cursor_end':offset+raw}
    assert passed==allowed['branches'][branch]['passing_quotient_keys']
    branches.append(row);offset+=raw
assert blocks==589680 and len(actual)==4704 and offset==28894320
expected=[json.loads(s) for s in (HERE/'quotient_lift_allowed_keys.jsonl').read_text().splitlines()]
key=lambda z:(z['branch'],z['internal_index'],z['cross_a_index'],z['cross_b_index'])
assert sorted(map(key,actual))==sorted(map(key,expected))
assert len(set(map(key,actual)))==4704
assert len(actual)*49==allowed['passing_full_normalized_inputs']==230496
with (HERE/'production.selected_keys.jsonl').open('w') as f:
    for row in actual:f.write(json.dumps(row)+'\n')
with (HERE/'production.inputs.txt').open('w') as f:
    f.write(str(len(actual))+'\n')
    for row in actual:f.write(' '.join(map(str,[row['branch'],row['internal_index'],row['cross_a_index'],row['cross_b_index'],row['original_scope_base'],*row['internal_S']]))+'\n')
meta={'full_normalized_scope':offset,'actual_internal_sets':sum(map(len,internal)),
 'completed_projected_blocks':blocks,'allowed_unique_projected_S':16,
 'passing_projected_blocks':4704,'original_BB_inputs':230496,
 'quotient_rejected_original_inputs':offset-230496,'branches':branches,
 'all_passing_keys_match_independent_actual_lift_file':True,
 'projected_key':'sorted distinct Q codes; Q code=v+7*w+21*j',
 'no_generation_by_the_24_overlapping_pattern_records':True,
 'order':'branch, internal option, cross ja, cross jb; accepted blocks each expand ba=0..6 then bb=0..6',
 'filtered_cursor_start':0,'random_profile_is_not_prefix':True,'profile_score_cache_used':False,
 'full_graph_BFS_population':'only original BB survivors, or one minimum-BB fallback if there are none',
 'prior_saved_profile':'1200 random sampled inputs; not a production prefix',
 'new_head_triangle_route_term':'two zero-field nonzero-w points in all six original BB masks',
 'scope_proof':'STRUCTURE_SCOPE.md','quotient_proof':'QUOTIENT_BB_CHECK.md',
 'worker_count':1,'cumulative_CPU_limit_seconds':180,'independent_math_CPU_accounted_separately':True}
(HERE/'production.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
engine=(HERE/'profile.cpp').read_text().split('int main(int argc,char**argv)')[0]
(HERE/'production_engine.hpp').write_text(engine)
(HERE/'production_extra.hpp').write_text('static const int GINV[6174]={'+','.join(map(str,GI))+'};\n')
rows=[json.loads(s) for s in (HERE/'profile.results.jsonl').read_text().splitlines()]
assert len(rows)==1200
(HERE/'production.expected_BB.txt').write_text('\n'.join(str(z['root_missing_by_target_layer'][1][1]) for z in rows)+'\n')
ind=json.loads((HERE/'preflight.independent_check.json').read_text())
with (HERE/'production.expected_sample_masks.txt').open('w') as f:
    for mask in ind['BB_masks']:f.write(' '.join(str(mask>>(64*i)&((1<<64)-1)) for i in range(3))+'\n')
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'production.cpp'),'-o',str(HERE/'production')],check=True)
compile_cpu=cpu()-before
subprocess.run([str(HERE/'production'),'calibrate','2',str(HERE)],check=True)
out={'status':'PRODUCTION_PREPARED','cpu_seconds':cpu()-start,'compile_cpu_seconds':compile_cpu,
 'projected_blocks_checked':589680,'matching_allowed_blocks':4704,'original_BB_inputs':230496,
 'actual_counts_match_independent_lift_file':True,'additional_graphs_or_BFS':0}
(HERE/'production.prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
