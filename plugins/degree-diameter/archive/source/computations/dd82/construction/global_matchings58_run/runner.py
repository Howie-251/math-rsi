"""One 60-CPU/90-wall batch, including independent BFS, with no restart."""
import argparse
import importlib.util
import json
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / 'pilot'
spec = importlib.util.spec_from_file_location('matching_bounded_process',
    ROOT / 'computations/dd82/n61/adjacent_double_full61_run/runner.py')
process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process)


def save(path, data):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def worker():
    # runpy keeps generation and the independent checker in one resource-limited
    # process, so the CPU ceiling applies to their sum, not separately to each.
    sys.argv = [str(HERE / 'generate.py'), 'generate', '--seed-start', '0',
                '--seed-stop', '8', '--out-dir', str(OUT)]
    runpy.run_path(sys.argv[0], run_name='__main__')
    checked = []
    for seed in range(8):
        candidate = OUT / f'seed{seed}/candidate.json'
        data = json.loads(candidate.read_text())
        sys.argv = [str(ROOT / 'computations/dd82/construction/verify_hs_candidate.py'),
                    str(candidate)]
        runpy.run_path(sys.argv[0], run_name='__main__')
        verified = json.loads(candidate.with_suffix('.verification.json').read_text())
        assert verified['n'] == 58 and verified['edges'] == 232
        assert verified['degrees'] == [8] * 58
        assert verified['bad_pair_count'] == data['bad_pair_count']
        assert sorted(x['pair'] for x in verified['bad_pairs']) == data['bad_pairs']
        checked.append(dict(seed=seed, bad_pair_count=verified['bad_pair_count'],
                            diameter=verified['diameter'], valid_target=verified['valid_target']))
        save(OUT / 'independent_checks.json', dict(checked_seeds=checked,
             all_requested_seeds_checked=len(checked) == 8))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('launch', 'worker'))
    parser.add_argument('--cpu', type=int, default=1)
    args = parser.parse_args()
    if args.action == 'worker':
        worker()
        return
    assert not OUT.exists(), 'Preserve the existing pilot; no automatic repeat'
    OUT.mkdir()
    command = [sys.executable, str(HERE / 'runner.py'), 'worker']
    save(OUT / 'launch.json', dict(command=command, seed_start=0, seed_stop=8,
         cpu_budget_seconds=60, wall_budget_seconds=90, cpu_affinity=[args.cpu],
         memory_limit_bytes=process.MEMORY_BYTES, per_file_limit_bytes=process.OUTPUT_BYTES,
         automatic_restarts=0, includes_independent_bfs=True, local_switches=False))
    measured = process.bounded(command, OUT / 'process.log', 60, 90, args.cpu, cap_files=True)
    measured['generated_seeds'] = [seed for seed in range(8)
                                  if (OUT / f'seed{seed}/candidate.json').exists()]
    measured['checked_seeds'] = [seed for seed in range(8)
                                if (OUT / f'seed{seed}/candidate.verification.json').exists()]
    measured['status'] = ('COMPLETE_EIGHT_SEEDS_AND_BFS' if measured['exit_code'] == 0
                          and len(measured['checked_seeds']) == 8 else 'INCOMPLETE_BATCH')
    measured['scope'] = 'One eight-seed generation pilot, not an exhaustive family or order decision'
    save(OUT / 'process_result.json', measured)
    print(json.dumps(measured, indent=2), flush=True)


if __name__ == '__main__':
    main()
