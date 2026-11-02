"""Forced-edge propagation on a saved deletion set; ignores all screen choices."""
import argparse
import importlib.util
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('baseline', HERE.parent / 'screen.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


def analyze(n):
    start = time.process_time()
    source = HERE / f'n{n}' / 'deletion_candidate.json'
    deleted = set(json.loads(source.read_text())['deleted'])
    data = baseline.geometry()
    vertices = set(range(73)) - deleted
    adj = {x: data['adj'][x] & vertices for x in vertices}
    steps, obstruction = [], None
    while True:
        deficit = {x: 8 - len(adj[x]) for x in vertices}
        assert all(d >= 0 for d in deficit.values())
        positive = {x for x in vertices if deficit[x] > 0}
        saturated = vertices - positive
        allowed = {x: positive - adj[x] - {x} if x in positive else set() for x in vertices}
        forced, reasons, unit_domains = set(), [], {}
        for x in sorted(positive):
            if len(allowed[x]) < deficit[x]:
                obstruction = dict(kind='INSUFFICIENT_AVAILABLE_NEIGHBORS', x=x,
                                   deficit=deficit[x], available=sorted(allowed[x]))
                break
            if len(allowed[x]) == deficit[x]:
                forced.update(tuple(sorted((x, y))) for y in allowed[x])
                reasons.append(dict(kind='DEGREE_TIGHT', x=x, targets=sorted(allowed[x])))
            if deficit[x] != 1:
                continue
            partners = sorted(s for s in saturated if s not in adj[x] and not (adj[x] & adj[s]))
            domain = set(allowed[x])
            for s in partners:
                domain &= adj[s]
            unit_domains[x] = dict(saturated_bad_partners=partners, domain=sorted(domain))
            if not domain:
                obstruction = dict(kind='EMPTY_UNIT_DOMAIN', x=x,
                                   saturated_bad_partners=partners,
                                   partner_neighborhoods={s: sorted(adj[s]) for s in partners},
                                   available=sorted(allowed[x]))
                break
            if len(domain) == 1:
                y = next(iter(domain))
                forced.add(tuple(sorted((x, y))))
                reasons.append(dict(kind='UNIT_SINGLETON', x=x, y=y,
                                    saturated_bad_partners=partners))
        if not obstruction:
            for x in sorted(vertices):
                incoming = [list(edge) for edge in sorted(forced) if x in edge]
                if len(incoming) > deficit[x]:
                    obstruction = dict(kind='FORCED_CAPACITY_OVERFLOW', x=x,
                                       deficit=deficit[x], forced_edges=incoming)
                    break
        steps.append(dict(step=len(steps), deficits=deficit, unit_domains=unit_domains,
                          forced_edges=sorted(forced), reasons=reasons, obstruction=obstruction))
        if obstruction or not forced:
            break
        for x, y in forced:
            assert y not in adj[x]
            adj[x].add(y)
            adj[y].add(x)
    result = dict(status='FIXED_DELETION_CONTRADICTION' if obstruction else 'FORCING_UNDECIDED',
                  n=n, deleted=sorted(deleted), source_candidate=str(source),
                  scope='All monotone completions of this saved deletion set only; arbitrary screen choices ignored',
                  screen_choices_used=False, solver_calls=0, steps=steps,
                  obstruction=obstruction, elapsed_cpu_seconds=time.process_time()-start,
                  justification='A saturated vertex keeps its neighborhood. Every deficit-one vertex must choose one available new neighbor lying in every saturated bad-partner neighborhood. Singleton domains force edges in every completion; degree-tight neighborhoods do likewise. Forced edges cannot exceed remaining degree capacity. Reapply after forced additions.')
    baseline.save(source.parent / 'forced_completion_analysis.json', result)
    print(json.dumps(dict(status=result['status'], n=n, obstruction=obstruction,
                         steps=len(steps), cpu_seconds=result['elapsed_cpu_seconds']), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, choices=(58, 59), required=True)
    analyze(parser.parse_args().n)
