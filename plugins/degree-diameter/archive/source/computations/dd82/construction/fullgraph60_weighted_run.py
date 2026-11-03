"""Prepare, then explicitly launch one full-graph weighted search; no auto-launch."""
from pathlib import Path
import argparse
import json
import os
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'computations/dd82/construction'
OUT = BASE / 'fullgraph60_weighted_run'
BINARY = OUT / 'search.bin'
TRACE = BASE / 'twin_seed_unrestricted_switch_run/twin60.json'
RUN_ID = 'dd82-v3-fullgraph-weighted60-20261013'


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + '\n')


def execute(command, log, cpu_limit, wall_limit):
    def limits():
        os.sched_setaffinity(0, {0})
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit + 1))
        resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with log.open('w') as output:
        try:
            code = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT,
                                  preexec_fn=limits, timeout=wall_limit).returncode
        except subprocess.TimeoutExpired:
            code = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=code, cpu_seconds=after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
                wall_seconds=time.monotonic() - start, pinned_cpu=0, threads=1,
                cpu_limit_seconds=cpu_limit, wall_limit_seconds=wall_limit, memory_limit_bytes=4 * 1024**3)


def prepare():
    OUT.mkdir(exist_ok=True)
    assert not (OUT / 'preparation.json').exists(), 'Preparation already recorded'
    provenance = json.loads(TRACE.read_text())
    source = Path(provenance['source'])
    assert source.is_file() and provenance['seed_bad_pairs'] == 20
    seed = source.read_text()
    rows = [list(map(int, line.split())) for line in seed.splitlines() if line.strip()]
    assert rows[0] == [60, 240] and len(rows) == 241
    degrees = [0] * 60
    es = set()
    for u, v in rows[1:]:
        assert 0 <= u < v < 60 and (u, v) not in es
        es.add((u, v)); degrees[u] += 1; degrees[v] += 1
    assert degrees == [8] * 60
    (OUT / 'seed.edges').write_text(seed)
    compiled = execute(['g++', '-O3', '-std=c++17', str(BASE / 'fullgraph60_weighted.cpp'), '-o', str(BINARY)], OUT / 'compile.log', 20, 30)
    assert compiled['exit_code'] == 0
    sanity = execute([str(BINARY), 'sanity', str(OUT / 'seed.edges'), str(OUT), '0', '0'], OUT / 'sanity.log', 5, 10)
    assert sanity['exit_code'] == 0
    checks = json.loads((OUT / 'sanity.json').read_text())
    assert checks['passed'] and checks['legal_proposals_checked'] == 1000
    result = dict(run_id=RUN_ID, status='PREPARED_NOT_RUN', seed_source=str(source), source_record=str(TRACE),
        source_edge_text_copied_exactly=(OUT / 'seed.edges').read_text() == source.read_text(),
        initial_n=60, initial_edges=240, initial_bad_pairs=20,
        old_neighborhood_reference=provenance['neighborhoods'][0],
        domain='All simple 8-regular labelled graphs on 60 vertices; unrestricted two-edge switches',
        score='sum of positive integer pair weights over uncovered pairs; all initial weights one',
        local_minimum_action='Increment every current uncovered pair weight by one; scan again',
        compile=compiled, sanity_process=sanity, sanity=checks, rng_used=False,
        planned_search_command=[sys.executable, str(Path(__file__).resolve()), 'run'],
        planned_process_cpu_limit=60, planned_process_wall_limit=90, planned_internal_cpu_limit=59,
        formal_search_started=False, independent_final_bfs_owner='root')
    save(OUT / 'preparation.json', result)
    print(json.dumps(result), flush=True)


def run():
    assert (OUT / 'preparation.json').exists()
    assert (OUT / 'changes.preparation.json').exists()
    assert not (OUT / 'launch.json').exists(), 'One authorized formal trajectory only'
    command = [str(BINARY), 'search', str(OUT / 'seed.edges'), str(OUT), '59', '88']
    save(OUT / 'launch.json', dict(run_id=RUN_ID, command=command, trajectories=1, chain_restarts=0,
                                 process_cpu_limit=60, process_wall_limit=90, rng_used=False))
    result = execute(command, OUT / 'search.log', 60, 90)
    result.update(run_id=RUN_ID, search_report_complete=(OUT / 'search.json').exists(),
                  independent_final_bfs_performed=False)
    if result['search_report_complete']:
        result['search'] = json.loads((OUT / 'search.json').read_text())
    save(OUT / 'resources.json', result)
    print(json.dumps(result), flush=True)


def prepare_changes():
    assert (OUT / 'preparation.json').exists()
    assert not (OUT / 'launch.json').exists()
    assert not (OUT / 'changes.preparation.json').exists()
    compiled = execute(['g++', '-O3', '-std=c++17', str(BASE / 'fullgraph60_weighted.cpp'), '-o', str(BINARY)], OUT / 'changes.compile.log', 20, 30)
    assert compiled['exit_code'] == 0
    sanity = execute([str(BINARY), 'change_sanity', str(OUT / 'seed.edges'), str(OUT), '0', '0'], OUT / 'changes.sanity.log', 5, 10)
    assert sanity['exit_code'] == 0
    checks = json.loads((OUT / 'change_sanity.json').read_text())
    assert checks['passed']
    previous = json.loads((OUT / 'preparation.json').read_text())
    result = dict(run_id=RUN_ID, previous_preparation_run_id=previous['run_id'],
        naming_correction_only=True, original_preparation_preserved=True, status='PREPARED_NOT_RUN',
        compile=compiled, change_sanity_process=sanity, change_sanity=checks,
        changes=['Ban the exact inverse of the most recent accepted switch, including across weight updates',
                 'Jump weights by the exact first strict-improvement threshold over all eligible moves',
                 'Direct graph equality against the last four accepted states; no hashes',
                 'Save first/best/final bad-pair lists and overlap, maximum weight and distinct incremented pairs'],
        formal_search_started=False)
    save(OUT / 'changes.preparation.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('action', choices=['prepare', 'prepare_changes', 'run'])
    args = p.parse_args()
    {'prepare': prepare, 'prepare_changes': prepare_changes, 'run': run}[args.action]()
