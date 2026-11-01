"""Replay 83 winning five-lock layouts with the independent injection formula.
Load only four function definitions from the old independent checker; its main
body and all submitted probability modules are never imported or executed.
"""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
import ast
import json
import signal
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'context/propertyb-m6-66-20261029/independent/check.py'
INPUT = HERE.parent / 'pilot/TAIL_RESTRICTED.json'
OUTPUT = HERE / 'TAIL_ARITHMETIC.json'
START = time.process_time()
WALL_START = time.monotonic()


def deadline(signum, frame):
    raise TimeoutError('20 CPU-second or 100 wall-second limit reached')


signal.signal(signal.SIGPROF, deadline)
signal.signal(signal.SIGALRM, deadline)
signal.setitimer(signal.ITIMER_PROF, 20)
signal.alarm(100)

# AST definition extraction avoids running the source's old top-level replay.
names = {'ceildiv', 'fall', 'probs', 'full_delete'}
tree = ast.parse(SOURCE.read_text())
functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
assert {n.name for n in functions} == names
namespace = {'Q': Fraction, 'factorial': factorial, 'comb': comb, 'lru_cache': lru_cache}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), 'exec'), namespace)
prob = namespace['probs']
delete = namespace['full_delete']


def bound(v, slots, ell):
    # Identical summation structure to independent/check.py::bound, with only
    # the edge-budget assertion changed from 65 to 66. The injection kernel
    # already supports arbitrary len(slots), including five.
    slots = tuple(slots)
    ell = {int(t): n for t, n in ell.items() if n}
    assert len(set(slots)) == 5 and all(1 <= h <= v for h in slots)
    assert sum(ell.values()) == 66 and min(ell.values()) >= 0
    deletion = {h: delete(v, slots, ell, j) for j, h in enumerate(slots)}
    value = Fraction(0)
    for h in range(1, v + 1):
        end = sum(n * prob(v, slots, h, t)[0] for t, n in ell.items())
        begin = sum(n * prob(v, slots, h, t)[1] for t, n in ell.items())
        pair = sum(n * (m - (t == u)) * prob(v, slots, h, t, u)
                   for t, n in ell.items() for u, m in ell.items())
        assert pair >= deletion.get(h, 0)
        value += min(end, begin, pair - deletion.get(h, 0))
    return value


def main():
    source = json.loads(INPUT.read_text())
    rows = []
    for group in source['vertices']:
        v = group['v']
        for r in group['rows']:
            assert r['degrees'] == [9] * 5
            blocks = r['blocks']
            assert all(sum(bool(b & (1 << i) and b & (1 << j)) for b in blocks) == 1
                       for i in range(5) for j in range(i + 1, 5))
            ell = {b: 1 for b in blocks}
            for i in range(5):
                ell[1 << i] = 9 - sum(bool(b & (1 << i)) for b in blocks)
            ell[0] = 66 - sum(ell.values())
            value = bound(v, r['positions'], ell)
            assert value == Fraction(r['U']), (v, blocks, value, r['U'])
            assert value < 1, (v, blocks, value)
            rows.append(dict(v=v, degrees=r['degrees'], blocks=blocks,
                             positions=r['positions'], ell=ell, U=str(value),
                             matches_original=True, strict=True))
    assert len(rows) == 83
    summary = []
    for v, expected in [(42, 31), (43, 26), (44, 26)]:
        rr = [r for r in rows if r['v'] == v]
        assert len(rr) == expected
        summary.append(dict(v=v, profiles=len(rr), maximum=str(max(Fraction(r['U']) for r in rr))))
    result = dict(status='PASS', review_independence='same-family',
                  acceptance_status='provisional', profiles=len(rows),
                  method='Independent uniform injection / falling-factorial exact Fraction replay',
                  formula_source=str(SOURCE.relative_to(ROOT)),
                  loaded_functions=sorted(names), source_main_executed=False,
                  submitted_probability_module_loaded=False,
                  modifications='Driver uses M=66; injection kernel and full-delete formula unchanged; five slots already supported',
                  scope='All 83 structurally retained v42-v44 five-lock layouts, full-pool deletion; no v31-v41 or full m6>=67 claim',
                  cpu_seconds=time.process_time()-START,
                  wall_seconds=time.monotonic()-WALL_START,
                  summary=summary, rows=rows)
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
