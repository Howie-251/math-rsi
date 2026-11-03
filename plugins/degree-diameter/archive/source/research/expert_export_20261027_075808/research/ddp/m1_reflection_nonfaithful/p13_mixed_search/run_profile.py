"""Two explicit preflight assignments, then the one approved complete p13 batch."""
from pathlib import Path
import json
import os
import resource
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ORIGINAL = ROOT / 'research/ddp/m1_f41_reflections/search_reflections.cpp'
EXE = HERE / 'search_reflections'
VERIFY = ROOT / 'computations/ddp/verify_graph'
SKELS = HERE.parent / 'p13_m28_r5_mixed_skeletons.txt'


def run(args, log, hard_limit=30):
    def single_worker():
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
        resource.setrlimit(resource.RLIMIT_CPU, (hard_limit, hard_limit))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    proc = subprocess.run(list(map(str, args)), capture_output=True, text=True,
                          preexec_fn=single_worker)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    Path(log).write_text(proc.stdout + proc.stderr)
    return proc, dict(command=list(map(str, args)), returncode=proc.returncode,
                      cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                      wall_seconds=time.monotonic()-started)


def mul(a, b):
    ax, ai = divmod(a, 28)
    bx, bi = divmod(b, 28)
    return ((ax + pow(5, ai, 13)*bx) % 13)*28 + (ai+bi) % 28


def inverse(a):
    ax, ai = divmod(a, 28)
    return (-pow(5, -ai, 13)*ax % 13)*28 + (-ai) % 28


def independent_edges(g):
    edges = set()
    for x in range(364):
        for gen in g[:2]:
            edges.add(tuple(sorted((x, mul(x, gen)))))
        for gen in g[2:4]:
            edges.add(tuple(sorted((364+x, 364+mul(x, gen)))))
        for gen in (0, g[4], g[5]):
            edges.add((x, 364+mul(x, gen)))
    return edges


def main():
    shutil.copyfile(ORIGINAL, HERE / 'search_reflections.cpp')
    proc, compilation = run(['g++', '-O3', '-std=c++17', HERE / 'search_reflections.cpp', '-o', EXE],
                            HERE / 'compile.log')
    assert proc.returncode == 0
    checks = []
    for idx, values in enumerate(((0, 0, 0), (4, 7, 12))):
        bx, sx, tx = values
        b = bx*28+1
        generators = [14, 42, b, inverse(b), sx*28+1, tx*28+6]
        prefix = HERE / f'preflight_{idx}'
        proc, check_run = run([EXE, 'check', 13, 28, 5, *generators, prefix],
                              prefix.with_suffix('.log'))
        assert proc.returncode == 0
        saved = json.loads(prefix.with_suffix('.json').read_text())
        tokens = list(map(int, prefix.with_suffix('.edges').read_text().split()))
        assert tokens[:2] == [728, 1820]
        edges = {tuple(tokens[i:i+2]) for i in range(2, len(tokens), 2)}
        assert len(edges) == 1820 and edges == independent_edges(generators)
        proc, verify_run = run([VERIFY, prefix.with_suffix('.edges'), 5, 5],
                               prefix.with_suffix('.generic_verify.json'))
        assert proc.returncode in (0, 1)
        verified = json.loads(proc.stdout)
        assert verified['roots_checked'] == 728
        assert verified['min_degree'] == verified['max_degree'] == 5
        assert verified['bad_unordered_pairs'] == saved['bad_unordered_pairs']
        assert verified['unreachable_unordered_pairs'] == 0
        assert (verified['bad_unordered_pairs'] == 0) == (saved['missing_sum'] == 0)
        assert f"diameter {verified['diameter']}" in prefix.with_suffix('.log').read_text()
        checks.append(dict(quotient=[1,1,6], values=list(values), generators=generators,
            exact_edge_set_match=True, root_missing=saved['root_missing'],
            bad_unordered_pairs=verified['bad_unordered_pairs'], diameter=verified['diameter'],
            checker_semantics='all unordered pairs at distance >5 or unreachable',
            check_run=check_run, independent_verify_run=verify_run))
    (HERE / 'preflight.json').write_text(json.dumps(dict(status='PASSED', compilation=compilation,
        parameterization_changes='None: copied the already parameterized and regressed F41 source unchanged',
        array_review='q=364, n=728; vectors sized from parameters; unsigned-short vertex bound 65535; stamp under 2^32',
        action_review='Only r^m=1 and r^(m/2)=-1 required; no faithful-action test', checks=checks), indent=2)+'\n')
    skeleton_lines = SKELS.read_text().splitlines()
    assert int(skeleton_lines[0]) == len(skeleton_lines)-1 == 48
    prefix = HERE / 'complete_mixed'
    proc, production = run([EXE, 'mixed', 13, 28, 5, SKELS, 29.5, prefix, 0, 0, 0],
                           HERE / 'production.log', hard_limit=30)
    assert proc.returncode == 0
    summary = json.loads(prefix.with_suffix('.summary.json').read_text())
    rows = [json.loads(line) for line in prefix.with_suffix('.skeleton_results.jsonl').read_text().splitlines()]
    assert sum(row['raw_visited'] for row in rows) == summary['raw_visited']
    assert sum(map(int, summary['score_histogram'].values())) == summary['legal_fully_scored']
    if summary['skeletons_completed'] == 48:
        assert summary['raw_visited'] == summary['legal_fully_scored'] == 105456
        assert summary['illegal_rejected'] == 0
        assert all(row['status']=='COMPLETE' and row['raw_visited']==2197 for row in rows)
    terminal = dict(scope='Only (13,28,5) mixed; all 48 approved skeletons; full F13^3 variables including zero',
        search_cpu_limit_seconds=30, worker_count=1, search_run=production, summary=summary,
        preflight='preflight.json', best_parameters='complete_mixed.best.json',
        best_complete_edgelist='complete_mixed.best.edges',
        independent_all_root_best_verification='pending separate checker')
    (HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2)+'\n')
    print(json.dumps(dict(status=summary['status'], raw_visited=summary['raw_visited'],
        legal=summary['legal_fully_scored'], minimum_missing=summary['minimum_missing_seen'],
        search_cpu_seconds=production['cpu_seconds'], best=json.loads(prefix.with_suffix('.best.json').read_text())),indent=2))


if __name__ == '__main__':
    main()
