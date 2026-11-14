"""Check the seven audited marked Q5 T63 ranks on the 53 remaining inputs."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
import re
from time import process_time


HERE = Path(__file__).parent
PRIOR = HERE / 'R7_MU3_COVERAGE_CIRCLE_T63_V2.json'
PROOF = Path('E:/新问题/research/six_directions/Q5_T63_RANK_PROOF.md')
REVIEW = PROOF.with_name('Q5_T63_RANK_REVIEW.json')


def marked_ranks():
    proof, review = PROOF.read_bytes(), REVIEW.read_bytes()
    audit = json.loads(review)
    proof_hash = sha256(proof).hexdigest()
    assert audit['verdict'] == 'PASS' and audit['audited_input_hashes'][PROOF.name] == proof_hash
    rows = re.findall(r'^\|(\d+)\|(\d+(?:,\d+){5})\|(\d+(?:,\d+){2})\|', proof.decode('utf-8'), re.M)
    assert [int(index) for index, _, _ in rows] == list(range(7))
    ranks = {}
    for rank, h, u in rows:
        h, u = (tuple(map(int, field.split(','))) for field in (h, u))
        assert len(h) == 6 and len(u) == 3 and set(u) <= set(h)
        for p in permutations(range(5)):
            def image(x):
                return sum(((x >> i) & 1) << j for i, j in enumerate(p))
            mapped = tuple(map(image, h)), tuple(map(image, u))
            for t in range(32):
                key = tuple(tuple(sorted(x ^ t for x in group)) for group in mapped)
                previous = ranks.setdefault(key, (int(rank), p, t))
                assert previous[0] == int(rank)
    return ranks, {'proof_sha256': proof_hash, 'review_sha256': sha256(review).hexdigest()}


def plans(row, ranks):
    L, V = set(row['L']), {127 ^ x for x in row['V']}
    for j in range(7):
        for donor_side in (0, 1):
            for same, other in ((L, V), (V, L)):
                in_donor = lambda x: ((x >> j) & 1) == donor_side
                W = {x for x in same if not in_donor(x)}
                minority = {x for x in other if not in_donor(x)}
                if (len(W), len(minority)) != (4, 1):
                    continue
                a, = minority
                source = sorted(x ^ (1 << j) for x in other if in_donor(x))
                for k in range(7):
                    if k == j:
                        continue
                    w = a ^ (1 << k)
                    W_Z = {x for x in W if not (((x ^ a) >> k) & 1)}
                    q = len(W_Z)
                    if q not in (1, 3):
                        continue
                    W_T = W - W_Z
                    coords = [i for i in range(7) if i not in (j, k)]
                    def project(x):
                        return sum(((x >> i) & 1) << d for d, i in enumerate(coords))
                    for Y in combinations(source, 3):
                        Y_Z = {x for x in Y if not (((x ^ a) >> k) & 1)}
                        if len(Y_Z) != q or w in Y:
                            continue
                        Y_T = set(Y) - Y_Z
                        U = Y_T | {w} if q == 1 else Y_Z
                        H = U | (W_T if q == 1 else W_Z)
                        assert len(H) == 6 and len(U) == 3 and len({x.bit_count() % 2 for x in H}) == 1
                        local = tuple(tuple(sorted(map(project, group))) for group in (H, U))
                        if local not in ranks:
                            continue
                        rank, p, t = ranks[local]
                        yield {'q': q, 'outer_j': j, 'donor_side': donor_side, 'inner_k': k,
                               'Z_side': (a >> k) & 1, 'a': a, 'w': w, 'W': sorted(W), 'W_Z': sorted(W_Z),
                               'W_T': sorted(W_T), 'Y': Y, 'Y_Z': sorted(Y_Z), 'Y_T': sorted(Y_T),
                               'H': sorted(H), 'U': sorted(U), 'Q5_axes': coords, 'Q5_H_U': local,
                               'rank': rank, 'rank_to_local_coordinate_permutation': p,
                               'rank_to_local_xor_after_permutation': t}


def main():
    start = process_time()
    prior = PRIOR.read_bytes()
    candidates = json.loads(prior)['no_plan']
    assert len(candidates) == 53
    ranks, bindings = marked_ranks()
    hits, misses, templates = [], [], defaultdict(Counter)
    for row in candidates:
        candidate = next(plans(row, ranks), None)
        if candidate is None:
            misses.append(row)
            templates[row['template']]['no_plan'] += 1
        else:
            hits.append(dict(row, plan=candidate))
            templates[row['template']][f'rank_q{candidate["q"]}'] += 1
    data = {'scope': 'Proposed q1/q3 receiver with an audited exact marked T63 rank. Geometry only, pending receiver theorem audit.',
            'input_sha256': sha256(prior).hexdigest(), **bindings, 'ordinary_matching_calls': 0, 'hamilton_calls': 0,
            'audited_rank_marked_images': len(ranks), 'cpu_seconds': round(process_time() - start, 3),
            'templates': dict(templates), 'rank_hits': hits, 'no_plan': misses}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data, separators=(',', ':')) + '\n', encoding='utf-8')
    print(len(hits), len(misses), len(ranks), dict(templates), data['cpu_seconds'])


if __name__ == '__main__':
    main()
