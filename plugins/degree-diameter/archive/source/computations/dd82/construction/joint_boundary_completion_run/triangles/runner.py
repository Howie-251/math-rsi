"""Reuse the joint-boundary process limits for separate triangle outputs."""
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('joint_boundary_triangles_base_runner', BASE / 'runner.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
base.process.OUTPUT_BYTES = 2 * 1024**3
# Existing defaults: 300CPU/360wall, 4GiB address space. Project/tool paths
# remain anchored to the original runner. No old action executes on import.

if __name__ == '__main__':
    base.main()
