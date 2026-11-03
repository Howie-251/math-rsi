#!/usr/bin/env python3
"""Run the single frozen seven-edge hub candidate; no source diameter revalidation."""
from pathlib import Path
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
start = time.process_time()
old_children = resource.getrusage(resource.RUSAGE_CHILDREN)
source = ROOT / 'research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json'
data = json.loads(source.read_text())['construction']
charts = {row['symbol']: row for row in data['charts']}
generators = [(0, 1, 2, 2, 1), (2, 2, 1, 0, 4), (0, 1, 2, 1, 2), (1, 2, 1, 0, 3)]
lines = []
for name, gen in zip(['a', 'a^-1', 'b', 'b^-1'], generators):
    c = charts[name]
    lines.append(' '.join(map(str, [*gen, *sum(c['M'], []), *c['d']])))
lines.append(' '.join(map(str, [*sum(charts['p']['M'], []), *charts['p']['d']])))
(HERE / 'INPUT.txt').write_text('\n'.join(lines) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'check.cpp', '-o', 'check'], cwd=HERE, stdout=log, stderr=log, check=True)

def child_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))

with (HERE / 'native.log').open('w') as log:
    run = subprocess.run([str(HERE / 'check')], cwd=HERE, stdout=log, stderr=log,
                         preexec_fn=child_limit, timeout=45)
children = resource.getrusage(resource.RUSAGE_CHILDREN)
aggregate = time.process_time() - start + children.ru_utime - old_children.ru_utime + children.ru_stime - old_children.ru_stime
result_path = HERE / 'RESULT.json'
result = json.loads(result_path.read_text()) if result_path.exists() else dict(status='PARTIAL_UNKNOWN_NO_FINAL_NATIVE_RECEIPT')
terminal = dict(status='TERMINAL', native_status=result['status'], returncode=run.returncode,
                aggregate_preparation_compile_native_CPU_seconds=aggregate, batch_CPU_budget_seconds=30,
                one_literal_combination=True, running=False, pending=[], source_D4_BFS_repeated=0,
                source_credit='Nishant Bhakar / f4t4nt degree-diameter-graphs route-chart9720',
                source_recipe=str(source.relative_to(ROOT)), no_other_matching_or_coordinate=True)
(HERE / 'TERMINAL.json').write_text(json.dumps(terminal, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(native_status=result['status'], aggregate_CPU_seconds=aggregate,
                     result=str(result_path.relative_to(ROOT))), ensure_ascii=False))
