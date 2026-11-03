"""Apply the proved quadratic-norm necessary condition to completed row survivors."""
from math import isqrt, prod
from pathlib import Path
import json
import os
import resource
import time


def square_or_five_square(sizes):
    value = prod(sizes)
    return isqrt(value)**2 == value or (
        value % 5 == 0 and isqrt(value // 5)**2 == value // 5)


def main():
    cpu0, wall0 = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {1})
    resource.setrlimit(resource.RLIMIT_CPU, (2, 3))
    source_path = Path(__file__).with_name('component_row_moment_screen.result.json')
    source = json.loads(source_path.read_text())
    assert source['full_input_complete']
    assert source['status'] == 'COMPLETE_NECESSARY_ROW_SCREEN'
    rows = []
    for row in source['rows']:
        survivors = [item for item in row['survivors']
                     if square_or_five_square(item['sizes'])]
        rows.append(dict(c=row['c'], input_sizes=len(row['survivors']),
                         surviving_sizes=len(survivors), survivors=survivors))
    result = dict(status='COMPLETE_NECESSARY_NORM_SCREEN', complete=True,
                  input_sizes=sum(r['input_sizes'] for r in rows),
                  surviving_sizes=sum(r['surviving_sizes'] for r in rows), rows=rows,
                  source=str(source_path),
                  scope='Size products square or five times square, a necessary norm condition only',
                  proof='proofs/dd82/n61/COMPONENT_QUOTIENT_GLOBAL_OBSTRUCTIONS.md',
                  not_checked=['shared interface compatibility',
                               'off-diagonal quotient polynomial', 'graph realization'],
                  cpu_seconds=time.process_time()-cpu0,
                  wall_seconds=time.monotonic()-wall0)
    Path(__file__).with_suffix('.result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
    print([(r['c'], r['input_sizes'], r['surviving_sizes']) for r in rows])


if __name__ == '__main__':
    main()
