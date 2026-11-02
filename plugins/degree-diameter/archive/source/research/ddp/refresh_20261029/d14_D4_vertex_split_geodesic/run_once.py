#!/usr/bin/env python3
"""Run only the81-root geodesic split gate, reusing the executed recipe generator."""
from pathlib import Path
import json
import resource
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
previous = HERE.parent / 'd14_D4_seven_plain_hub'
start = time.process_time()
old_children = resource.getrusage(resource.RUSAGE_CHILDREN)
shutil.copy2(previous / 'INPUT.txt', HERE / 'INPUT.txt')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'check.cpp', '-o', 'check'],
                   cwd=HERE, stdout=log, stderr=log, check=True)

def child_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (8, 8))

with (HERE / 'native.log').open('w') as log:
    run = subprocess.run([str(HERE / 'check')], cwd=HERE, stdout=log, stderr=log,
                         preexec_fn=child_limit, timeout=20)
children = resource.getrusage(resource.RUSAGE_CHILDREN)
aggregate = time.process_time() - start + children.ru_utime - old_children.ru_utime + children.ru_stime - old_children.ru_stime
result_path = HERE / 'RESULT.json'
result = json.loads(result_path.read_text()) if result_path.exists() else dict(status='PARTIAL_UNKNOWN_NO_FINAL_NATIVE_RECEIPT')
terminal = dict(status='TERMINAL', native_status=result['status'], returncode=run.returncode,
    aggregate_preparation_compile_native_CPU_seconds=aggregate, batch_CPU_budget_seconds=10,
    running=False, pending=[], source_old_D4_revalidation=False, new_graphs=0,
    recipe_generator_reused_from='research/ddp/refresh_20261029/d14_D4_seven_plain_hub/check.cpp',
    source_adjacency_reconstructed_from_same_input=True, old_old_candidate_BFS=0,
    source_credit='Nishant Bhakar / f4t4nt published9720 route-chart source')
(HERE / 'TERMINAL.json').write_text(json.dumps(terminal, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(native_status=result['status'], aggregate_CPU_seconds=aggregate,
    result=str(result_path.relative_to(ROOT))), ensure_ascii=False))
