"""Independent literal and exact physical-DP audit; never imports the builder."""
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import platform
import time

ROOT = Path(__file__).resolve().parent
POINTS = tuple(range(1, 24))
AA = frozenset((6, 7, 8, 9, 15))
BB = frozenset((15, 16, 17, 18))
TT = AA | BB
FROZEN = ((1, 2, 3, 4, 5, 6), (6, 7, 8, 9, 15), (9, 10, 11, 12, 13, 14),
          (15, 16, 17, 18), (18, 19, 20, 21, 22, 23))


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


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
    triples = tuple(combinations(POINTS, 3))
    number = {t: i + 1 for i, t in enumerate(triples)}
    pairs = tuple(combinations(POINTS, 2))
    aux = {(k, edge): len(triples) + 1 + index * len(pairs) + j
           for index, k in enumerate((4, 5, 6)) for j, edge in enumerate(pairs)}
    expected = set()

    def require(literals):
        expected.add(tuple(sorted(set(literals))))

    def windows(path):
        return [number[path[i:i + 3]] for i in range(len(path) - 2)]

    for packet in combinations(POINTS, 4):
        ids = [number[t] for t in combinations(packet, 3)]
        for pattern in product((False, True), repeat=4):
            if sum(pattern[i] != pattern[i + 1] for i in range(3)) >= 2:
                require([-v if bit else v for v, bit in zip(ids, pattern)])
    for size, red in ((7, True), (6, False)):
        for path in combinations(POINTS, size):
            require([-v if red else v for v in windows(path)])
    for red_size, blue_size in ((4, 5), (5, 4), (6, 3)):
        for path in combinations(POINTS, red_size):
            require([-v for v in windows(path)] + [aux[red_size, (path[0], path[-1])]])
        for path in combinations(POINTS, blue_size):
            require([-aux[red_size, (path[0], path[-1])]] + windows(path))
    for size in (4, 5, 6):
        for path in combinations(POINTS, size):
            if size == 4 and (path[-1] in AA or path[0] in BB or (path[0] in TT and path[-1] in TT)):
                require(windows(path))
            if size == 5 and (path[0] in TT or path[-1] in TT):
                require(windows(path))
            if size == 6 and (path[-1] < 6 or path[0] > 18 or (path[0] == 9 and path[-1] > 15)):
                require([-v for v in windows(path)])
    for path in FROZEN:
        for v in windows(path):
            require([v])
    for y in range(9, 15):
        for z in range(16, 24):
            require([-number[y, 15, z]])
    for y in range(10, 15):
        require([-number[8, 9, y]])
    variables, actual = read_cnf()
    assert variables == len(triples) + 3 * len(pairs)
    missing, extra = expected - actual, actual - expected
    assert not missing and not extra, (len(missing), len(extra))
    receipt = dict(passed=True, check='independent_complete_clause_set_reconstruction',
                   variables=variables, clauses=len(actual), missing=0, extra=0,
                   cnf_sha256=sha(ROOT / 'formula.cnf'), verifier_sha256=sha(__file__))
    (ROOT / 'schema-audit.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))


def physical_dp(colors, red):
    # Every state stores ALL exact achievable lengths and one actual witness
    # per length. Last-coordinate order makes the recurrence acyclic.
    reach = {(s, s, t): {2: (s, t)} for s, t in combinations(POINTS, 2)}
    for last in POINTS:
        states = [(key, table) for key, table in reach.items() if key[2] == last]
        for (first, previous, _), table in states:
            for new in POINTS[last:]:
                if colors[previous, last, new] == red:
                    target = reach.setdefault((first, last, new), {})
                    for length, path in table.items():
                        target.setdefault(length + 1, path + (new,))
    endpoints = {}
    for (first, _, last), table in reach.items():
        target = endpoints.setdefault((first, last), {})
        for length, path in table.items():
            target.setdefault(length, path)
    return endpoints, len(reach)


def sat_audit():
    began = time.monotonic()
    variables, clauses = read_cnf()
    model = set()
    for line in (ROOT / 'solve.stdout').read_text().splitlines():
        if line.startswith('v '):
            model.update(int(v) for v in line[2:].split() if int(v))
    assert all((v in model) != (-v in model) for v in range(1, variables + 1))
    assert all(any(v in model for v in clause) for clause in clauses)
    triples = tuple(combinations(POINTS, 3))
    colors = {triple: i + 1 in model for i, triple in enumerate(triples)}
    dynamic, state_counts = {}, {}
    for red in (False, True):
        dynamic[red], state_counts[red] = physical_dp(colors, red)

    def exists(red, length, first=None, last=None):
        return any(length in table for (s, t), table in dynamic[red].items()
                   if (first is None or s == first) and (last is None or t == last))

    # Independent explicit subsets through seven cross-check the DP at every
    # endpoint/length covered by any prohibition. Higher lengths are still
    # computed by the full DP, not inferred from a cap or path-shortening.
    brute = {red: {edge: set() for edge in combinations(POINTS, 2)} for red in (False, True)}
    red6, blue5 = [], []
    path_counts = {red: {} for red in (False, True)}
    tested = 0
    for size in range(2, 8):
        for path in combinations(POINTS, size):
            tested += 1
            bits = [colors[path[i:i + 3]] for i in range(size - 2)]
            for red in (False, True):
                if all(bit == red for bit in bits):
                    brute[red][path[0], path[-1]].add(size)
                    path_counts[red][size] = path_counts[red].get(size, 0) + 1
                    if red and size == 6:
                        red6.append(path)
                    if not red and size == 5:
                        blue5.append(path)
    assert all(brute[red][edge] == {k for k in table if k <= 7}
               for red in (False, True) for edge, table in dynamic[red].items())
    weak = [(edge, r, b) for edge in combinations(POINTS, 2)
            for r in dynamic[True][edge] for b in dynamic[False][edge] if r + b >= 9]
    max_red = max(k for table in dynamic[True].values() for k in table)
    max_blue = max(k for table in dynamic[False].values() for k in table)
    checks = dict(
        complete_literal_assignment=True,
        packets=all(sum(bits[i] != bits[i + 1] for i in range(3)) <= 1
                    for four in combinations(POINTS, 4)
                    for bits in [[colors[t] for t in combinations(four, 3)]]),
        no_R7=max_red <= 6,
        no_B6=max_blue <= 5,
        no_weak7_all_exact_endpoint_lengths=not weak,
        all_five_frozen_red_paths=all(all(colors[t] for t in combinations(path, 3)) for path in FROZEN),
        A_no_in_B4=all(not exists(False, 4, last=t) for t in AA),
        B_no_out_B4=all(not exists(False, 4, first=s) for s in BB),
        T_no_B5_start_or_end=all(not exists(False, 5, first=t) and not exists(False, 5, last=t) for t in TT),
        no_T_to_T_B4=all(not exists(False, 4, first=s, last=t) for s, t in combinations(sorted(TT), 2)),
        no_R6_ending_before_a1=all(not exists(True, 6, last=t) for t in range(1, 6)),
        no_R6_starting_after_b4=all(not exists(True, 6, first=s) for s in range(19, 24)),
        a4_R6_all_terminals_at_most_c=all(not exists(True, 6, first=9, last=t) for t in range(16, 24)),
        gap_pivot_blue_fan=all(not colors[y, 15, z] for y in range(9, 15) for z in range(16, 24)),
        a3_a4_gap_blue_fan=all(not colors[8, 9, y] for y in range(10, 15)),
        DP_matches_all_subsets_through_seven=True)
    assert all(checks.values()), checks
    with (ROOT / 'colors.tsv').open('w') as stream:
        stream.write('a\tb\tc\tcolor\n')
        for triple in triples:
            stream.write('\t'.join(map(str, triple)) + ('\tR\n' if colors[triple] else '\tB\n'))
    endpoint_data = []
    for edge in combinations(POINTS, 2):
        endpoint_data.append(dict(endpoints=edge, R_lengths=sorted(dynamic[True][edge]),
                                  B_lengths=sorted(dynamic[False][edge]),
                                  R_witnesses=dynamic[True][edge], B_witnesses=dynamic[False][edge]))
    witness = dict(n=23, A=sorted(AA), B=sorted(BB), T=sorted(TT), pivot=15,
                   private_gap=(9, 10, 11, 12, 13, 14), frozen_red_paths=FROZEN,
                   endpoints=endpoint_data, all_actual_R6=red6, all_actual_B5=blue5,
                   weak7_violations=weak)
    (ROOT / 'physical-witness.json').write_text(json.dumps(witness, indent=2) + '\n')
    receipt = dict(passed=True, checks=checks, DP_states={'R': state_counts[True], 'B': state_counts[False]},
                   endpoint_pairs=len(endpoint_data), tested_subsets_size_2_to_7=tested,
                   max_R=max_red, max_B=max_blue,
                   path_counts_through_seven={'R': path_counts[True], 'B': path_counts[False]},
                   seconds=time.monotonic() - began,
                   bindings={p.name: sha(p) for p in (ROOT / 'formula.cnf', ROOT / 'solve.stdout',
                             ROOT / 'colors.tsv', ROOT / 'physical-witness.json', Path(__file__))},
                   scope='Only the requested necessary private-gap subdomain; no 75-point extension or geometric realization is asserted.')
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
