#!/usr/bin/env python3
"""Saved root rescaling procedure; existing exact witness is not overwritten."""
import os
for key in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS']:
    os.environ[key] = '1'
import ctypes
import json
import resource
import time
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (8, 8))
start = time.process_time()
HERE = Path(__file__).resolve().parent
assert not (HERE / 'RESCALING_RESULT.json').exists(), 'Exact rescaling already completed.'
import numpy as np

prior = json.loads((HERE / 'RESULT.json').read_text())
data = json.loads((HERE / 'round_03.x.json').read_text())
last = json.loads((HERE / 'round_03.json').read_text())
info = json.loads((HERE / 'INPUT.json').read_text())
N, W, DEN = 94186, 57, 10**9
x = np.asarray(data['group_x'], dtype=np.float64)
caps = np.asarray(data['group_caps'], dtype=np.int64)
scale = (2 + 1e-8) / last['minimum_float_coverage']
numerators = np.ceil(scale * x * DEN).astype(np.int64)
assert np.all(numerators >= 0) and np.all(numerators <= caps * DEN)
assert int(numerators.sum()) <= 26 * DEN
r3 = np.fromfile(info['R3_file'], dtype='<u8')
r4 = np.fromfile(info['R4_file'], dtype='<u8')
assert r3.size == r4.size == N * W
lib = ctypes.CDLL(str(HERE / 'support_ops.so'))
u64 = np.ctypeslib.ndpointer(dtype=np.uint64, flags='C_CONTIGUOUS')
i64 = np.ctypeslib.ndpointer(dtype=np.int64, flags='C_CONTIGUOUS')
lib.evaluate_integer.argtypes = [u64, u64, i64, ctypes.c_int, ctypes.c_int, i64]
lib.evaluate_integer.restype = None
coverage = np.empty(N, dtype=np.int64)
lib.evaluate_integer(r3, r4, numerators, N, W, coverage)
assert int(coverage.min()) >= 2 * DEN
witness = dict(status='EXACT_GLOBAL_FRACTIONAL_WITNESS_VERIFIED', denominator=DEN,
    group_numerators=numerators.tolist(), group_caps=caps.tolist(),
    sum_numerator=int(numerators.sum()), sum=int(numerators.sum())/DEN,
    complete_target_count=N, minimum_integer_coverage=int(coverage.min()),
    minimum_target=int(coverage.argmin()), required_integer_coverage=2*DEN,
    positive_groups=int((numerators > 0).sum()), all_group_caps_exactly_pass=True,
    origin='Round3 vector scaled using complete-target minimum; no additional LP')
(HERE / 'EXACT_GLOBAL_WITNESS.json').write_text(json.dumps(witness, indent=2)+'\n')
result = {k:v for k,v in witness.items() if k not in ('group_numerators','group_caps')}
result.update(CPU_seconds=time.process_time()-start, additional_LP_calls=0,
    combined_whole_CPU_seconds=prior['whole_CPU_seconds']+time.process_time()-start,
    original_whole_budget=30, BFS_runs=0, SAT_calls=0, new_graphs=0, running=False)
assert result['combined_whole_CPU_seconds'] < 30
(HERE / 'RESCALING_RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
