#!/usr/bin/env python3
"""Exactly evaluate a candidate in the fixed six-block Q4 model; no optimization."""
import argparse
from fractions import Fraction
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / 'archive/source/certificate_final_q4'
DIMS = [240, 212, 190, 187, 170, 9]

def require(condition, message):
    if not condition:
        raise ValueError(message)

def rational(value):
    return dict(numerator=value.numerator, denominator=value.denominator, exact=str(value))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--certificate', type=Path, required=True)
    ap.add_argument('--work-dir', type=Path, required=True, help='New directory; never overwrite an earlier run')
    ap.add_argument('--n', type=int, help='Also derive the exact finite-dimension bound for n >= 4')
    ap.add_argument('--compiler', help='C++17 compiler; defaults to CXX or PATH')
    a = ap.parse_args()
    if a.n is not None and a.n < 4:
        ap.error('--n must be at least 4')
    out = a.work_dir.resolve()
    if out.is_relative_to((ROOT/'archive').resolve()):
        ap.error('--work-dir must be outside the frozen archive')
    raw = a.certificate.read_bytes()
    c = json.loads(raw)
    require(c['dimensions'] == DIMS and len(c['gram_factors']) == 6,
            'Expected exactly the fixed six Q4 Gram blocks')
    require(c['q5_cuts'] == [], 'Q5 cuts are forbidden in the six-block Q4 model')
    require(c['face_root_masks'] == [0, 1, 3, 6, 7], 'Wrong face-root masks')
    D = c['gram_denominator']
    require(type(D) is int and D > 0, 'Invalid Gram denominator')
    mats = []
    for n, L in zip(DIMS, c['gram_factors']):
        require(len(L) == n and len(L[0]) > 0 and all(len(row) == len(L[0]) for row in L),
                'Invalid rectangular Gram factor shape')
        require(all(type(x) is int for row in L for x in row), 'Gram factors must be integers')
        mats.append([[sum(x*y for x, y in zip(L[i], L[j])) for j in range(n)] for i in range(n)])
    safe = 192*(D*D + sum(max(abs(x) for row in Q for x in row) for Q in mats))
    require(safe < 2**63, '64-bit arithmetic safety failed')
    den = 192*D*D
    mf = max(Fraction(mats[b][i][i], D*D) for b in range(5) for i in range(DIMS[b]))
    mv = max(Fraction(mats[5][i][i], D*D) for i in range(9))
    compiler = a.compiler or os.environ.get('CXX') or shutil.which('g++') or shutil.which('clang++')
    require(bool(compiler), 'Need a C++17 compiler via --compiler, CXX or PATH')
    out.mkdir(parents=True, exist_ok=False)
    (out/'certificate.json').write_bytes(raw)
    with (out/'verification_matrices.txt').open('w', encoding='ascii') as f:
        f.write(f'{D} -1 {den}\n')  # Negative target: compute the true maximum, never trust bound metadata.
        for Q in mats:
            f.write(str(len(Q))+'\n'+'\n'.join(' '.join(map(str, row)) for row in Q)+'\n')
    shutil.copy2(FROZEN/'keys.bin', out/'keys.bin')
    exe = out/('verify_q4.exe' if os.name == 'nt' else 'verify_q4')
    commands = [[compiler, '-O3', '-std=c++17', '-UNDEBUG', str(FROZEN/'verify_local.cpp'), '-o', str(exe)],
                [str(exe), 'verification_matrices.txt']]
    runs = []
    for cmd in commands:
        start = time.monotonic()
        p = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
        runs.append(dict(command=cmd, cwd=str(out), returncode=p.returncode,
                         stdout=p.stdout, stderr=p.stderr, wall_seconds=time.monotonic()-start))
        (out/'PROCESS.json').write_text(json.dumps(runs, indent=2)+'\n')
        require(p.returncode == 0, f'Compiler/checker failed: {p.stderr}')
    native = runs[-1]['stdout']
    exact = re.search(r'^EXACT_MAX (-?\d+) / (\d+)$', native, re.MULTILINE)
    worst = re.search(r'^WORST_GRAPH (\d+)$', native, re.MULTILINE)
    require(exact is not None and worst is not None, 'Incomplete native maximum output')
    numerator, actual_den = map(int, exact.groups())
    require(actual_den == den, 'Native denominator differs from the candidate denominator')
    C = Fraction(numerator, den)
    result = dict(status='PASS', model='six fixed Q4 blocks; no Q5 cuts',
                  certificate=str(a.certificate.resolve()), dimensions=DIMS, gram_denominator=D,
                  exact_local_numerator=numerator, exact_local_denominator=den,
                  C=rational(C), M_F=rational(mf), M_v=rational(mv), worst_graph=int(worst.group(1)),
                  bound_source='exact full-domain maximum; certificate bound metadata not used',
                  psd_source='integer Gram factors LL^T / D^2', arithmetic_absolute_bound=safe)
    if a.n is not None:
        finite = C + mf/Fraction(a.n-3) + mv*Fraction(4*a.n-6, (a.n-2)*(a.n-3))
        result['finite_dimension'] = dict(n=a.n, density_upper_bound=rational(finite),
            formula='C + M_F/(n-3) + M_v*(4*n-6)/((n-2)*(n-3))')
    (out/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
