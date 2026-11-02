"""Decode this case with the prepared parent encoder; no generation."""
import argparse
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('adjacent_ports_case_encode', PARENT / 'encode.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
# Keep base.ROOT and its generic helper path anchored to the parent project.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('decode',))
    parser.add_argument('--log', type=Path, default=HERE / 'solver.log')
    args = parser.parse_args()
    base.decode(args.log)
