"""All64 endpoint-owner downclone subsets; deterministic, no solver."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import resource
import time
from semantic_check import analyze, transversals

HERE = Path(__file__).resolve().parent


def save(name, data):
    with (HERE / name).open('x') as out: json.dump(data, out, indent=2)


def main():
    assert platform.system() == 'Linux'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3,) * 2)
    start = time.monotonic()
    source = HERE / 'published_D26_colors.json'
    raw = json.loads(source.read_text())
    colors = {tuple(row['triple']): row['red'] for row in raw['colors']}
    analysis = analyze(colors, 26)
    ends = analysis.pop('_endpoints')
    owners = analysis['EndR5']
    assert owners == list(range(20, 26)) and analysis['D7_valid']
    srcb3 = {a for a, j in ends[False] if len(ends[False][a, j]) >= 3}
    srcb4 = set(analysis['SrcB4'])
    rows, owner_obstructions = [], {}
    for bits in range(64):
        selected = {owners[i] for i in range(6) if bits >> i & 1}
        bad = []
        for u, v in combinations(range(26), 2):
            red, blue = ends[True][u, v], ends[False][u, v]
            augmented = len(red) + len(blue) + (u in selected) + (v in selected)
            if augmented > 8:
                bad.append({'old_ends': [u, v], 'red': red, 'blue': blue,
                            'old_length_sum': len(red) + len(blue),
                            'selected_endpoint_count': (u in selected) + (v in selected),
                            'augmented_length_sum': augmented})
        badb4 = sorted(selected & srcb4)
        badb3 = sorted(selected & set(owners) & srcb3)
        allowed = not bad and not badb4 and not badb3
        row = {'S': sorted(selected), 'criterion_valid': allowed, 'weak_pair_obstruction_count': len(bad),
               'all_weak_pair_obstructions': bad, 'SrcB4_obstructions': badb4,
               'EndR5_SrcB3_obstructions': badb3}
        if len(selected) == 1:
            owner_obstructions[str(next(iter(selected)))] = row
        if allowed and len(selected) <= 4:
            named = [(v, sign) for v in range(26) for sign in (('-', '+') if v in selected else ('o',))]
            newcolors = {}
            for t in combinations(range(len(named)), 3):
                a, b, c = [named[i][0] for i in t]
                if a == b: value = False
                elif b == c: value = True
                else: value = colors[a, b, c]
                newcolors[t] = value
            actual = analyze(newcolors, len(named))
            actual.pop('_endpoints')
            actual['transversals'] = transversals(newcolors, len(named)) if actual['D7_valid'] else None
            stem = 'clone_S_' + ('_'.join(map(str, sorted(selected))) if selected else 'empty')
            save(stem + '_colors.json', {'n': len(named), 'owner_sign_labels': named,
                'colors': [{'triple': t, 'red': value} for t, value in newcolors.items()]})
            save(stem + '_semantics.json', actual)
            row['actual_semantic_check'] = {'D7_valid': actual['D7_valid'],
                'tau': actual['transversals'].get('tau') if actual['transversals'] else None,
                'red6_count': actual['transversals'].get('red6_count') if actual['transversals'] else None,
                'stem': stem}
            assert actual['D7_valid'], 'criterion-positive retained model failed semantic check'
            if actual['transversals'].get('tau') == 5:
                save('clone_tau5_counterexample.json', {'S': sorted(selected), 'stem': stem, 'actual': actual})
                print(json.dumps({'immediate_counterexample': True, 'S': sorted(selected), 'stem': stem}), flush=True)
                rows.append(row)
                break
        rows.append(row)
    report = {'schema': 'published_D26_all64_EndR5_downclone_calibration_v1',
              'status': 'COMPLETE' if len(rows) == 64 else 'TAU5_FOUND_STOPPED',
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256((HERE / 'semantic_check.py').read_bytes()).hexdigest(),
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'old_EndR5': owners, 'old_SrcB3': sorted(srcb3), 'old_SrcB4': sorted(srcb4),
              'subsets_tested': len(rows), 'criterion_valid_subsets': [r['S'] for r in rows if r['criterion_valid']],
              'singleton_owner_obstructions': owner_obstructions, 'all_subsets': rows,
              'solver_invocations': 0, 'elapsed_seconds': time.monotonic() - start,
              'scope': 'Exact supplied clone criterion classified all subsets; only criterion-valid order<=30 models generated and independently checked; no SAT search or acceptance'}
    save('endpoint_clone_result.json', report)
    print(json.dumps({'status': report['status'], 'subsets_tested': len(rows),
        'valid_subsets': report['criterion_valid_subsets'], 'old_SrcB3': sorted(srcb3),
        'singletons': {v: {'pair_count': r['weak_pair_obstruction_count'],
                          'first_witness': r['all_weak_pair_obstructions'][:1],
                          'SrcB3_obstructions': r['EndR5_SrcB3_obstructions']}
                       for v, r in owner_obstructions.items()},
        'elapsed_seconds': report['elapsed_seconds']}, indent=2))


if __name__ == '__main__': main()
