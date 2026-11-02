"""Reuse the original bounded full61 runner with this new output directory.

No old source or result is modified. No process is launched on import.
Solver limits remain at most 50 CPU/70 wall seconds, single core.
"""
import argparse
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'triple_full61_run'
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('triple61_grid_base_runner', BASE / 'runner.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--cpu', type=int, default=1)
    parser.add_argument('--solver-cpu', type=int, default=50)
    parser.add_argument('--solver-wall', type=int, default=70)
    args = parser.parse_args()
    if args.action == 'prepare':
        base.prepare(args.cpu)
    elif args.action == 'solve':
        base.solve(args.cpu, args.solver_cpu, args.solver_wall)
    else:
        base.check(args.cpu)
