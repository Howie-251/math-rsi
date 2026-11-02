from pathlib import Path
import datetime
import json
import resource
import subprocess
import time

base = Path(__file__).resolve().parent
started_cpu = time.process_time() + resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
source = base.parent / 'graph_d82_D3_n346516.edges'
output = base / 'graph_d83_D3_n350742.edges'
assert not output.exists(), 'This fixed producer is one-shot; inspect prior receipt instead of rerunning.'
attempts = []
commands = [
    ['g++', '-std=c++17', '-O2', '-o', str(base/'produce_once'), str(base/'produce_once.cpp')],
    [str(base/'produce_once'), str(source), str(output)],
]
for phase, command in zip(['compile', 'write_complete_graph'], commands):
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = subprocess.run(command, text=True, capture_output=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu = after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime
    (base/(phase+'.log')).write_text(result.stdout + result.stderr)
    attempts.append({'phase':phase, 'exit_code':result.returncode, 'CPU_seconds':cpu})
    assert result.returncode == 0, attempts
    if phase == 'write_complete_graph':
        report = json.loads(result.stdout)
total_cpu = time.process_time() + resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime - started_cpu
assert total_cpu < 30
report.update(CPU_seconds=total_cpu, CPU_budget_seconds=30, attempts=attempts,
    old_source_file=str(source), output=str(output), exact_diameter='PENDING_FRESH_PROOF_AND_BFS',
    root_counts_modified=False, old_geometry_field_Lean_solver_runs=0)
(base/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(base/'PARAMETERS.json').write_text(json.dumps({'source':str(source),'source_n':346516,'source_m':14204970,
    'original_H_n':342290,'original_U_n':342225,'first_clone_label':'342290+h','second_clone_label':'346516+h',
    'center_count':4225,'first_hub':346515,'second_hub':350741,'source_fillers':'342225+j,j0..64',
    'new_clone_neighbors':'actual first-clone original-U-neighbor list, frozen from one source stream',
    'all_old_edges_retained':True,'new_new_edges':0,'n':350742,'m':14547195,'Delta':83,'D_prediction':3,
    'public_gate':'../../../../../public_baseline_audit/DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.md',
    'priority':'UNKNOWN'},ensure_ascii=False,indent=2)+'\n')
(base/'TERMINAL.json').write_text(json.dumps({'status':'PRODUCER_TERMINAL_PASS_PENDING_FRESH_ACCEPTANCE',
    'running':False,'all_children_terminal':True,'CPU_seconds':total_cpu,'CPU_budget_seconds':30,
    'actual_complete_output':str(output),'BFS_runs':0,'no_automatic_next_parameter':True},indent=2)+'\n')
print(json.dumps({'status':report['status'],'n':350742,'m':14547195,'CPU_seconds':total_cpu}))
