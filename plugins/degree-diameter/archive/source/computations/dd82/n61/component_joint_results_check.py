"""Independent matrix and input-coverage check of saved quotient enumerations.

Does not rerun searches or certify a search's exhaustion independently.
Completeness combines terminal per-size records with the reviewed search.
"""
from itertools import permutations, product
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent


def direct_check(sizes, domains, q):
    c = len(sizes)
    assert len(q) == c and all(len(row) == c for row in q)
    assert sum(sizes) == 61 and all(sum(row) == 8 for row in q)
    assert sum(q[i][i] for i in range(c)) == 8-(c-1)//2
    for i in range(c):
        assert q[i][i] in domains[i] and 0 <= q[i][i] < sizes[i]
        assert sizes[i]*q[i][i] % 2 == 0
        for j in range(c):
            assert type(q[i][j]) is int and 0 <= q[i][j] <= sizes[j]
            assert sizes[i]*q[i][j] == sizes[j]*q[j][i]
            assert sum(q[i][k]*q[k][j] for k in range(c))+q[i][j] == sizes[j]+11*(i == j)


def known_lifting_case(sizes, q):
    examples = [
        ((2, 5, 6, 18, 30), [[0,5,3,0,0],[2,0,0,0,6],[1,0,1,6,0],[0,0,2,1,5],[0,1,0,3,4]], 'matching-edge'),
        ((3, 3, 15, 15, 25), [[0,3,5,0,0],[3,0,0,5,0],[1,0,2,0,5],[0,1,0,2,5],[0,0,3,3,2]], 'periodic-column'),
    ]
    for ns, target, label in examples:
        if tuple(sizes) != ns:
            continue
        groups = [[i for i, n in enumerate(ns) if n == size] for size in sorted(set(ns))]
        for choices in product(*(permutations(g) for g in groups)):
            perm = list(range(len(ns)))
            for group, choice in zip(groups, choices):
                for i, j in zip(group, choice):
                    perm[i] = j
            if all(q[perm[i]][perm[j]] == target[i][j] for i in range(len(ns)) for j in range(len(ns))):
                return label
    return None


def main():
    start = time.process_time()
    domain = json.loads((HERE/'component_norm_screen.result.json').read_text())
    assert domain['complete'] and domain['surviving_sizes'] == 65
    expected = {tuple(item['sizes']): item['diagonal_domains']
                for row in domain['rows'] for item in row['survivors']}
    assert len(expected) == 65
    completed, checked_models, files = {}, [], []
    for suffix in ('profile', 'remaining', 'unresolved'):
        path = HERE/f'component_joint_quotient.{suffix}.json'
        if not path.exists():
            continue
        result = json.loads(path.read_text())
        files.append(path.name)
        for item in result['items']:
            sizes = tuple(item['sizes'])
            assert sizes in expected and item['diagonal_domains'] == expected[sizes]
            if item['enumeration_complete']:
                assert sizes not in completed, 'A completed domain was run again'
                assert item['status'] in ('MODEL', 'EXHAUSTED_NO_MODEL')
                assert bool(item['models']) == (item['status'] == 'MODEL')
                completed[sizes] = path.name
            for model in item['models']:
                direct_check(sizes, expected[sizes], model['Q'])
                checked_models.append(dict(sizes=sizes, source=path.name,
                                           lifting_case=known_lifting_case(sizes, model['Q'])))
    missing = [list(sizes) for sizes in expected if sizes not in completed]
    result = dict(status='SAVED_RESULTS_CHECKED',
                  expected_size_domains=65, completed_size_domains=len(completed),
                  all_size_domains_complete=not missing, unresolved_sizes=missing,
                  sources=files, independently_checked_models=checked_models,
                  all_saved_models_in_proved_lifting_cases=all(m['lifting_case'] for m in checked_models),
                  completed_by_c={str(c): sum(len(sizes) == c for sizes in completed)
                                  for c in (5,7,9,11,13,15,17)},
                  scope='Exact saved-model and terminal input coverage check; search exhaustiveness rests on the separately reviewed enumeration algorithm',
                  cpu_seconds=time.process_time()-start)
    Path(__file__).with_suffix('.result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
