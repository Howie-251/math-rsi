"""One bounded run for each changed r1/r2 input; use the existing runner."""
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('internal_double_refined_bounded_runner', HERE.parent / 'runner.py')
runner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)
runner.HERE = HERE
runner.CASES = {case: runner.CASES[case] for case in ('r1_h0_b0', 'r2_h0_b1')}
# ROOT, tool paths and all process limits remain those of the base runner:
# 60 CPU / 90 wall seconds, 4 GiB address space, 512 MiB per output file.
if __name__ == '__main__':
    runner.main()
