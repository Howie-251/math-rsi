"""Independent literal-schema and exhaustive coloring audit; imports no builder."""
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import platform
import time

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_cnf():
    lines = (ROOT / 'formula.cnf').read_text().splitlines()
    variables, declared = map(int, lines[0].split()[2:])
    clauses = []
    for line in lines[1:]:
        data = list(map(int, line.split()))
        assert data[-1] == 0 and all(0 < abs(v) <= variables for v in data[:-1])
        clauses.append(tuple(sorted(set(data[:-1]))))
    assert len(clauses) == declared and len(set(clauses)) == declared
    return variables, set(clauses)


def schema_audit():
    points = tuple(range(1, 20))
    triples = list(combinations(points, 3))
    number = {t: i + 1 for i, t in enumerate(triples)}
    pairs = list(combinations(points, 2))
    aux = {(k, e): len(triples) + 1 + index * len(pairs) + j
           for index, k in enumerate((4, 5, 6)) for j, e in enumerate(pairs)}
    expected = set()

    def require(literals):
        expected.add(tuple(sorted(set(literals))))

    def windows(path):
        return [number[tuple(path[i:i + 3])] for i in range(len(path) - 2)]

    for packet in combinations(points, 4):
        ids = [number[t] for t in combinations(packet, 3)]
        for pattern in product((False, True), repeat=4):
            if sum(pattern[i] != pattern[i + 1] for i in range(3)) >= 2:
                require([(-v if bit else v) for v, bit in zip(ids, pattern)])
    for size, red in ((7, True), (6, False)):
        for path in combinations(points, size):
            require([(-v if red else v) for v in windows(path)])
    for red_size, blue_size in ((4, 5), (5, 4), (6, 3)):
        for path in combinations(points, red_size):
            require([-x for x in windows(path)] + [aux[red_size, (path[0], path[-1])]])
        for path in combinations(points, blue_size):
            require([-aux[red_size, (path[0], path[-1])]] + windows(path))
    for size in (4, 5, 6):
        for path in combinations(points, size):
            reject_blue = size == 4 and (6 <= path[-1] <= 10 or 10 <= path[0] <= 14
                                                    or (6 <= path[0] <= path[-1] <= 14))
            reject_blue |= size == 5 and (6 <= path[0] <= 14 or 6 <= path[-1] <= 14)
            if reject_blue:
                require(windows(path))
            if size == 6 and ((path[-1] < 10 and 6 <= path[-2] <= 14)
                              or (path[0] > 10 and 6 <= path[1] <= 14)):
                require([-v for v in windows(path)])
    for path in ((1, 2, 3, 4, 5, 6), (14, 15, 16, 17, 18, 19),
                 (6, 7, 8, 9, 10), (10, 11, 12, 13, 14)):
        for v in windows(path):
            require([v])
    for triple in [(x, 5, 6) for x in range(1, 5)] + [(14, 15, y) for y in range(16, 20)]:
        require([number[triple]])
    variables, actual = read_cnf()
    assert variables == len(triples) + 3 * len(pairs)
    missing, extra = expected - actual, actual - expected
    assert not missing and not extra, (len(missing), len(extra))
    receipt = dict(check='independent_full_clause_set_reconstruction', passed=True,
                   variables=variables, clauses=len(actual), missing=0, extra=0,
                   cnf_sha256=sha(ROOT / 'formula.cnf'), verifier_sha256=sha(__file__))
    (ROOT / 'schema-audit.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))


def sat_audit():
    started = time.monotonic()
    points = tuple(range(1, 20))
    triples = tuple(combinations(points, 3))
    variables, clauses = read_cnf()
    model = set()
    for line in (ROOT / 'solve.stdout').read_text().splitlines():
        if line.startswith('v '):
            model.update(int(x) for x in line[2:].split() if int(x))
    assert all((v in model) != (-v in model) for v in range(1, variables + 1))
    assert all(any(v in model for v in clause) for clause in clauses)
    colors = {t: i + 1 in model for i, t in enumerate(triples)}
    catalogs = {'R': {}, 'B': {}}
    endpoint_lengths = {}
    tested = 0
    for size in range(2, 20):
        red_paths, blue_paths = [], []
        for path in combinations(points, size):
            tested += 1
            bits = [colors[path[i:i + 3]] for i in range(size - 2)]
            for red, bucket in ((True, red_paths), (False, blue_paths)):
                if all(x == red for x in bits):
                    bucket.append(path)
                    endpoint_lengths.setdefault((path[0], path[-1]), {True: set(), False: set()})[red].add(size)
        if red_paths:
            catalogs['R'][size] = red_paths
        if blue_paths:
            catalogs['B'][size] = blue_paths
    red6 = catalogs['R'].get(6, [])
    blue4, blue5 = catalogs['B'].get(4, []), catalogs['B'].get(5, [])
    frozen = ((1, 2, 3, 4, 5, 6), (14, 15, 16, 17, 18, 19),
              (6, 7, 8, 9, 10), (10, 11, 12, 13, 14))
    weak = [(edge, r, b) for edge, lengths in endpoint_lengths.items()
            for r in lengths[True] for b in lengths[False] if r + b >= 9]
    checks = dict(
        complete_DIMACS_assignment=True,
        packets=all(sum(bits[i] != bits[i + 1] for i in range(3)) <= 1
                    for four in combinations(points, 4)
                    for bits in [[colors[t] for t in combinations(four, 3)]]),
        no_R7=max(catalogs['R']) <= 6,
        no_B6=max(catalogs['B']) <= 5,
        no_weak7_all_exact_endpoint_lengths=not weak,
        frozen_R6_1_to_6=all(colors[t] for t in combinations(frozen[0], 3)),
        frozen_R6_14_to_19=all(colors[t] for t in combinations(frozen[1], 3)),
        frozen_R5_A=all(colors[t] for t in combinations(frozen[2], 3)),
        frozen_R5_B=all(colors[t] for t in combinations(frozen[3], 3)),
        A_no_in_B4=all(p[-1] not in range(6, 11) for p in blue4),
        B_no_out_B4=all(p[0] not in range(10, 15) for p in blue4),
        T_no_B5_start_or_end=all(p[0] not in range(6, 15) and p[-1] not in range(6, 15) for p in blue5),
        no_T_to_T_B4=all(not (p[0] in range(6, 15) and p[-1] in range(6, 15)) for p in blue4),
        early_R6_no_T_penultimate=all(not (p[-1] < 10 and p[-2] in range(6, 15)) for p in red6),
        late_R6_no_T_second=all(not (p[0] > 10 and p[1] in range(6, 15)) for p in red6),
        left_ambient_red_fan=all(colors[x, 5, 6] for x in range(1, 5)),
        right_ambient_red_fan=all(colors[14, 15, y] for y in range(16, 20)))
    assert all(checks.values()), checks
    with (ROOT / 'colors.tsv').open('w') as stream:
        stream.write('a\tb\tc\tcolor\n')
        for t in triples:
            stream.write('\t'.join(map(str, t)) + ('\tR\n' if colors[t] else '\tB\n'))
    witness = dict(n=19, roles=dict(A=list(range(6, 11)), B=list(range(10, 15)), T=list(range(6, 15)), pivot=10),
                   colors=[dict(vertices=t, color='R' if colors[t] else 'B') for t in triples],
                   frozen_red_paths=frozen, all_actual_paths=catalogs,
                   weak7_violations=weak, cnf_sha256=sha(ROOT / 'formula.cnf'))
    (ROOT / 'physical-witness.json').write_text(json.dumps(witness, indent=2) + '\n')
    receipt = dict(passed=True, checks=checks, tested_subsets_size_at_least_2=tested,
                   actual_path_counts={color: {k: len(v) for k, v in paths.items()}
                                       for color, paths in catalogs.items()},
                   seconds=time.monotonic() - started,
                   bindings={p.name: sha(p) for p in (ROOT / 'formula.cnf', ROOT / 'solve.stdout',
                             ROOT / 'colors.tsv', ROOT / 'physical-witness.json', Path(__file__))},
                   scope='A verified coloring of the requested necessary nineteen-point induced subdomain only; no ambient 75-point extension or geometric claim.')
    (ROOT / 'independent-verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    assert platform.system() == 'Linux'
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', action='store_true')
    parser.add_argument('--sat', action='store_true')
    args = parser.parse_args()
    assert args.schema != args.sat
    schema_audit() if args.schema else sat_audit()
