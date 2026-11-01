#!/usr/bin/env python3
"""Run archived Property B checks in a separate, disposable work tree.

Source files are copied verbatim. No probability, domain, or path expression is
rewritten. The copied project hierarchy and its working directory supply paths.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
M6 = 'context/propertyb-m6-67-progress-20261029'
M7 = 'context/propertyb-m7-131-20261029'
M8 = 'context/propertyb-m8-267-20261029'
M9 = 'context/propertyb-m9-543-20261029'
M12 = 'context/propertyb-k12-4664-20261029'
OLD6 = 'context/propertyb-m6-66-20261029'
DIAG6 = 'context/propertyb-m6-67-diagnosis-20261029'
SMALL = 'propertyB_small_k'
FAST = 'context/collaborator-small-k-20261019/m10-m11'

CASES = {
    'm6': dict(dirs=[M6, OLD6, DIAG6, SMALL], scripts=[
        f'{M6}/root/base_domain_check.py',
        f'{M6}/independent31_33/check.py',
        f'{M6}/independent34_min10/check.py',
        f'{M6}/34_min9/check.py',
        f'{M6}/independent_new_branches/check.py',
        f'{M6}/independent_new_branches/whole35.py',
        f'{M6}/independent36_38/check.py',
        f'{M6}/independent39/check.py',
        f'{M6}/root/independent40_41.py',
        f'{DIAG6}/integer-lock/tail_independent.py'],
        scope='All used M66 local arithmetic branches; see proof for structural arguments.'),
    'm7': dict(dirs=[M7], scripts=[f'{M7}/independent/check.py'],
        scope='Full 424-type independent injection/Fraction replay and domain reconstruction.'),
    'm8': dict(dirs=[M8], scripts=[f'{M8}/independent/check.py'],
        scope='Full 2094-type independent injection/Fraction replay; component DP and domain.'),
    'm9': dict(dirs=[M9], scripts=[f'{M9}/independent/check.py'],
        scope='Full 3450-type independent injection/Fraction replay and decision tree.'),
    'm12': dict(dirs=[M12], scripts=[f'{M12}/independent/check.py'],
        scope='Independent full parameter/trace domain and 20 Fraction cases; NOT full probability replay.'),
    'm7-author': dict(dirs=[M7, SMALL], scripts=[f'{M7}/check_candidate.py'],
        scope='Author certificate generator; consumes archived pilot input where applicable.'),
    'm8-author': dict(dirs=[M8, SMALL], scripts=[f'{M8}/certificate.py'],
        scope='Author final certificate generator using archived initial/component/adaptive inputs.'),
    'm9-author': dict(dirs=[M9, SMALL], scripts=[f'{M9}/candidate.py', f'{M9}/coverage.py'],
        scope='Author candidate generator plus complete coverage reconstruction.'),
    'm12-author': dict(dirs=[M12, FAST], scripts=[
        f'{M12}/repro/conditional.py', f'{M12}/repro/tail.py',
        f'{M12}/repro/summarize.py', f'{M12}/repro/compare.py'],
        scope='Complete fixed-cut M4663 original implementation rerun (664355 types); requires NumPy.'),
}


def source_files(case):
    # Keep relative imports and archived mathematical inputs; exclude bytecode,
    # images, reviewer transcripts and nested archives. Every copy is verbatim.
    files = set()
    for directory in CASES[case]['dirs']:
        files.update(p for p in (ROOT / directory).rglob('*')
                     if p.is_file() and p.suffix in ('.py', '.json')
                     and '__pycache__' not in p.parts and 'reviews' not in p.parts)
    return sorted(files)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--list', action='store_true', help='list runnable cases and exact scope')
    ap.add_argument('--case', default='all', help='comma-separated case names; all=m6,m7,m8,m9,m12')
    ap.add_argument('--output', type=Path, help='new output directory (must not already exist)')
    args = ap.parse_args()
    if args.list:
        for name, spec in CASES.items():
            print(f'{name}: {spec["scope"]}')
        return
    if not __debug__:
        ap.error('Assertions are required; do not invoke Python with -O.')
    names = ['m6', 'm7', 'm8', 'm9', 'm12'] if args.case == 'all' else args.case.split(',')
    if any(n not in CASES for n in names):
        ap.error('Unknown case; use --list.')
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    out = (args.output or ROOT / 'reproduction-runs' / stamp).resolve()
    out.mkdir(parents=True, exist_ok=False)
    work = out / 'work'; work.mkdir()
    files = sorted({p for n in names for p in source_files(n)})
    for src in files:
        dest = work / src.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    env.pop('PYTHONPATH', None)
    records = []
    report = dict(source_root=str(ROOT), output_root=str(out), work_root=str(work),
                  copied_files=len(files), source_rewrites=[], second_machine=False,
                  python=sys.version, cases={n: CASES[n]['scope'] for n in names}, commands=records)
    for name in names:
        for script in CASES[name]['scripts']:
            logfile = out / (name + '-' + Path(script).parent.name + '-' + Path(script).stem + '.log')
            cmd = [sys.executable, '-B', str(work / script)]
            before = resource.getrusage(resource.RUSAGE_CHILDREN)
            start = time.monotonic()
            print(f'RUN {name}: {script}', flush=True)
            with logfile.open('w') as log:
                proc = subprocess.run(cmd, cwd=work, env=env, stdout=log, stderr=subprocess.STDOUT)
            after = resource.getrusage(resource.RUSAGE_CHILDREN)
            records.append(dict(case=name, script=script, exit_code=proc.returncode,
                                wall_seconds=time.monotonic()-start,
                                child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                                log=logfile.name))
            report['status'] = 'PASS' if proc.returncode == 0 else 'FAILED'
            (out / 'RUN_REPORT.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
            if proc.returncode:
                print(f'FAILED; see {logfile}', file=sys.stderr)
                raise SystemExit(proc.returncode)
    print(f'PASS; report: {out / "RUN_REPORT.json"}', flush=True)


if __name__ == '__main__':
    main()
