"""Reuse the bounded joint-boundary runner with separate sorted outputs."""
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('joint_boundary_sorted_base_runner', BASE / 'runner.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
base.process.OUTPUT_BYTES = 2 * 1024**3
# Keep base.ROOT and base.process paths/resource constants anchored to the
# original project; only the output cap changes from1GiB to2GiB here.
# This is local to this imported process and never edits the base runner.

if __name__ == '__main__':
    base.main()
