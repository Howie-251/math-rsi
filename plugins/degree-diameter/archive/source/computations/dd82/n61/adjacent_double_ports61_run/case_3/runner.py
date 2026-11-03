"""Run/check this already prepared case with the existing bounded runner."""
import argparse
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('adjacent_ports_case_runner', PARENT / 'runner.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
# ROOT, SOLVER, CHECKER and BFS retain the correct project paths established
# when the parent runner was imported; only this case's output path changes.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--cpu', type=int, default=1)
    parser.add_argument('--solver-cpu', type=int, default=50)
    parser.add_argument('--solver-wall', type=int, default=70)
    args = parser.parse_args()
    if args.action == 'prepare':
        raise SystemExit('Cases are prepared only by parent prepare_cases.py; this wrapper does not regenerate CNF.')
    if args.action == 'solve':
        base.solve(args.cpu, args.solver_cpu, args.solver_wall)
    else:
        base.check(args.cpu)
