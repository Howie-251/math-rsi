"""Finite literal source transfer; classify every endpoint by its C35 phase."""
from pathlib import Path
import json
import math
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (30, 35))
SPEC = next(s for s in json.loads((ROOT / 'context/DD_PORTFOLIO_START_20261026/baselines/generator_specs.json').read_text()) if s['id'] == 'd10_D4')
M = SPEC['m']
PHASES = [g[0] for g in SPEC['generators']]


def endpoints(n, r, m=M, positive=None):
    positive = SPEC['generators'] if positive is None else positive
    arcs = []
    for phase, x in positive:
        arcs.extend([(phase, x % n), ((-phase) % m, -x * pow(r, -phase, n) % n)])
    layers = [set() for _ in range(m)]
    raw = [0] * m
    counts = [0] * 5

    def walk(phase, x, depth, last):
        counts[depth] += 1
        layers[phase].add(x)
        raw[phase] += 1
        if depth == 4:
            return
        for k, (dp, b) in enumerate(arcs):
            if last is not None and k == (last ^ 1):
                continue
            walk((phase + dp) % m, (x * pow(r, dp, n) + b) % n, depth + 1, k)

    walk(0, 0, 0, None)
    assert counts == [1, 10, 90, 810, 7290]
    missing = [sorted(set(range(n)) - layer) for layer in layers]
    return dict(modulus=n, action=r,
                action_order=next(k for k in range(1, m + 1) if pow(r, k, n) == 1),
                hypothetical_order=m * n,
                raw_word_counts_by_length=counts, raw_words_by_phase=raw,
                distinct_endpoints_by_phase=[len(layer) for layer in layers],
                missing_by_phase=missing,
                representative_root_missing=sum(map(len, missing)),
                all_phases_full=not any(missing), graph_generated=False)


def main():
    # No candidate in this degree10/D4 group family can exceed Moore8201.
    moore = 1 + 10 * sum(9 ** j for j in range(4))
    candidates = [n for n in range(SPEC['n'] + 1, moore // M + 1)
                  if math.gcd(SPEC['a'], n) == 1 and pow(SPEC['a'], M, n) == 1]
    cases = [endpoints(n, SPEC['a']) for n in candidates]
    result = dict(status='COMPLETE_LITERAL_RULE', target_Delta=10, target_D=4,
                  saved_baseline=2485, source_parameters=SPEC,
                  frozen_rule='Same five integer translations, C35 phases and literal action2; no offset optimization.',
                  modulus_interval=[72, moore // M], complete_legal_moduli=candidates,
                  cases=cases, new_graphs=0, old_source_BFS=0,
                  actual_diameter=None, ordinary_bad_unordered_pairs=None,
                  CPU_seconds=time.process_time() - START)
    (OUT / 'LITERAL_RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(legal_moduli=candidates, cases=[{k: c[k] for k in ['modulus', 'action_order', 'hypothetical_order', 'representative_root_missing', 'distinct_endpoints_by_phase', 'all_phases_full']} for c in cases], CPU_seconds=result['CPU_seconds']), ensure_ascii=False))


if __name__ == '__main__':
    main()
