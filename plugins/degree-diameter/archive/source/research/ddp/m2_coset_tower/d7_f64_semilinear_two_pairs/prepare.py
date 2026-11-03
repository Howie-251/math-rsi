"""Compare actual normalization lists and prepare one graph containing involutions."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();runs=[];limit=60.0
def run(args,log):
    remaining=max(1,math.ceil(limit-(cpu()-start)))
    def cap(): resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    before=cpu();wall=time.monotonic()
    with (HERE/log).open('w') as output:
        result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
    runs.append({'command':list(map(str,args)),'log':log,'returncode':result.returncode,
                 'cpu_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall})
    if result.returncode: raise RuntimeError(f'{log}: exit {result.returncode}')
run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],'compile.log')
run([str(HERE/'search'),'prepare',str(HERE)],'prepare.log')
actual=json.loads((HERE/'generated_scope.json').read_text())
independent=json.loads((HERE/'normalization_inputs.json').read_text())
assert actual['involution_codes']==independent['nonidentity_involution_codes']
assert len(actual['inverse_pair_representative_codes'])==1300
for ours,theirs in zip(actual['type_i'],independent['type_i']):
    assert ours['first_code']==theirs['first_involution_code']
    assert [row['representative_code'] for row in ours['orbits']]==theirs['second_representative_codes']
    assert [row['member_codes'] for row in ours['orbits']]==[row['member_codes'] for row in theirs['second_orbits']]
assert actual['type_ii_involution_codes']==independent['type_ii']['allowed_involution_codes']
count=independent['counts_not_search_completion']
assert actual['type_i_total']==count['type_i_valid']==33774000
assert actual['type_ii_total']==count['type_ii_valid']==7716060
assert actual['raw_total']==count['total_valid']==41490060
assert actual['HH_total']==count['total_hh_pass']==38982510
sample=json.loads((HERE/'preflight.json').read_text())
result={'status':'PREFLIGHT_D5_CANDIDATE' if sample['bad_unordered_pairs']==0 else 'READY_FOR_INDEPENDENT_SAMPLE_CHECK',
        'scope_lists_match':True,'all_87_involutions_match':True,
        'both_type_I_twenty_orbits_match_member_by_member':True,
        'type_II_forty_five_involutions_match':True,
        'range_counts_match':True,'candidate_ranges_not_enumerated':True,
        'profile_started':False,'sample_edges':'preflight.edges',
        'sample_parameters':'preflight.json','sample_bad_pairs':sample['bad_unordered_pairs'],
        'cumulative_cpu_seconds':cpu()-start,'cumulative_cpu_limit_seconds':limit,
        'runs':runs,'normalization_input_file':'normalization_inputs.json',
        'actual_scope_file':'generated_scope.json'}
(HERE/'prepare.terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='runs'},indent=2))
