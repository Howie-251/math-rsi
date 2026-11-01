"""Re-execute frozen local verifiers; redirect their writes into this audit."""
from pathlib import Path
import contextlib
import io
import json
import math
import resource
import runpy
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BASE = ROOT / "context/propertyb35-paper/round01/middle"
sys.dont_write_bytecode = True
original_read = Path.read_text
original_write = Path.write_text
records = []

def mapped(path):
    absolute = path.resolve()
    if absolute.is_relative_to(HERE):
        return absolute
    if not absolute.is_relative_to(ROOT):
        raise RuntimeError(f"Output outside permitted project: {absolute}")
    return HERE / "replay" / absolute.relative_to(ROOT)

def output(path, data, *args, **kwargs):
    destination = mapped(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    return original_write(destination, data, *args, **kwargs)

def input_text(path, *args, **kwargs):
    absolute = path.resolve()
    if absolute.is_relative_to(ROOT) and not absolute.is_relative_to(HERE):
        alternate = mapped(path)
        if alternate.exists():
            return original_read(alternate, *args, **kwargs)
    return original_read(path, *args, **kwargs)

Path.write_text = output
Path.read_text = input_text
start = time.process_time()
# This is an actual execution limit for this replay only. It does not hard-enforce
# the model's read-only/nonrecursive/eight-turn prompt conventions.
resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
scripts = [
    "min_degree_eight_singleton_star_20261020/SCOPE_CHECK.py",
    "min_degree_eight_singleton_star_20261020/INDEPENDENT_VERIFY.py",
    "min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_CHECK.py",
    "delta8_strong_pair_transfer_20261020/VERIFY.py",
    "delta8_c3_capacity_transfer_20261020/INDEPENDENT_VERIFY.py",
    "delta8_high_center_q4_20261020/audit/VERIFY.py",
    "c3_unique_high_pair_five_20261020/PILOT.py",
    "c3_unique_high_pair_five_20261020/VERIFY.py",
    "delta8_one_exception_scalar_20261020/CHECK.py",
    "delta8_one_exception_scalar_20261020/audit/CHECK.py",
]
for number, name in enumerate(scripts, 1):
    t = time.process_time()
    capture = io.StringIO()
    status = "PASS"
    try:
        with contextlib.redirect_stdout(capture):
            runpy.run_path(str(BASE / name), run_name="__main__")
    except BaseException as error:
        status = "FAIL"
        capture.write(f"\n{type(error).__name__}: {error}\n")
        raise
    finally:
        log = HERE / f"run-{number:02d}.log"
        original_write(log, capture.getvalue())
        records.append({"script": str((BASE/name).relative_to(ROOT)),
                        "status": status, "cpu_seconds": time.process_time()-t,
                        "log": log.name})
        original_write(HERE/"ACTUAL_RUN_RECEIPT.json",
                       json.dumps({"status": status, "runs": records,
                                   "total_cpu_seconds": time.process_time()-start,
                                   "write_redirect": "native/replay; frozen source unchanged",
                                   "imported_old_c14_catalogue_rerun": False}, indent=2)+"\n")
    print(number, status, name, records[-1]["cpu_seconds"], flush=True)
print("TOTAL_CPU", time.process_time()-start)
