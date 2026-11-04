"""Verify positive T44 paths and endpoint-set compatibility independently.

The perfect-endpoint exception universe is imported from its separate
finite proof package. Its mathematical exhaustiveness is not re-proved here.
No producer search function or existing checker is imported.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
V = frozenset(range(16))
ODD = frozenset(x for x in V if x.bit_count() % 2)
EVEN = V - ODD


def require(test, message):
    if not test:
        raise AssertionError(message)


def edge(a, b):
    return (min(a, b), max(a, b))


def rank_matching(mate, holes):
    remaining = sorted(V-set(holes))
    rank = 0
    while remaining:
        x = remaining.pop(0)
        i = remaining.index(mate[x])
        completions = 1
        for k in range(1, len(remaining)-1, 2):
            completions *= k
        rank += i*completions
        remaining.pop(i)
    return rank


def endpoint_triples():
    units = (1, 2, 4, 8)
    triples = {frozenset(c) for c in combinations(units, 3)}
    for a, b in combinations(units, 2):
        for c in units:
            if c not in (a,b):
                triples.add(frozenset((a,b,a^b^c)))
    require(len(triples) == 16, '16 coordinate-orbit endpoint hitting triples')
    return sorted(triples, key=lambda s: tuple(sorted(s)))


def main():
    triples = endpoint_triples()
    source = ROOT/'q4_perfect_endpoint_abundance_check.json'
    imported = json.loads(source.read_text(encoding='utf-8'))
    require(imported['status'] == 'PASS', 'perfect endpoint input status')
    exceptions = imported['all_exceptional_matchings']
    require(len(exceptions) == 4708, 'perfect endpoint exception count')
    seen_perfect = set()
    bad_sets = []
    for record in exceptions:
        matching = frozenset(edge(*e) for e in record['matching'])
        require(len(matching) == 8 and sorted(x for e in matching for x in e) == list(range(16)),
                'imported exception is perfect matching')
        require(matching not in seen_perfect, 'distinct imported exceptions')
        seen_perfect.add(matching)
        bad = frozenset(record['bad_odd_endpoints'])
        require(bad <= ODD and len(bad) <= 4, 'exceptional bad endpoint bound')
        require(all(not t <= bad for t in triples), 'universal endpoint hitting triples')
        bad_sets.append(bad)

    files = []
    histogram = Counter()
    low_sets = Counter()
    paths_total = 0
    low_records = 0
    for p in (3,15):
        for b,t in combinations(sorted(EVEN-{0,p}), 2):
            name = f'q4_t44_path_abundance_{p}_{b}_{t}.bin'
            data = (ROOT/name).read_bytes()
            offset = 0
            ranks = bytearray(10395)
            holes = {0,p,b,t}
            allowed = V-{0,p}
            rows = 0
            file_hist = Counter()
            while offset < len(data):
                require(offset+17 <= len(data), 'complete record header')
                mate = data[offset:offset+16]
                count = data[offset+16]
                offset += 17
                require({x for x,y in enumerate(mate) if y==255} == holes, 'exact holes')
                require(all(mate[x] in V-holes and mate[x] != x and mate[mate[x]] == x
                            for x in V-holes), 'matching involution')
                matching = frozenset(edge(x,mate[x]) for x in V-holes)
                require(len(matching) == 6, 'six required edges')
                rank = rank_matching(mate, holes)
                require(0 <= rank < 10395 and not ranks[rank], 'unique complete matching rank')
                ranks[rank] = 1
                endpoints = set()
                require(offset+14*count <= len(data), 'complete path records')
                for _ in range(count):
                    path = data[offset:offset+14]
                    offset += 14
                    require(len(set(path)) == 14 and set(path) == allowed, 'path exact support')
                    require(path[0] == b and path[-1] in ODD, 'path endpoints')
                    require(path[-1] not in endpoints, 'distinct witness endpoints')
                    endpoints.add(path[-1])
                    edges = frozenset(edge(a,c) for a,c in zip(path,path[1:]))
                    require(len(edges) == 13 and matching <= edges, 'required edges in path')
                    require(all((a^c).bit_count() == 1 for a,c in edges-matching), 'new edges short')
                require(len(endpoints) == count, 'endpoint count')
                relative = frozenset(x^b for x in endpoints)
                require(relative <= ODD, 'translated root0 endpoint parity')
                # This condition alone gives a small abstract gluing theorem.
                require(count >= 5 or any(q <= relative for q in triples),
                        'path endpoints hit every perfect-matching endpoint set')
                if count <= 4:
                    low_records += 1
                    low_sets[tuple(sorted(relative))] += 1
                    require(all(not relative <= bad for bad in bad_sets),
                            'direct low-set versus all perfect exceptions')
                histogram[count] += 1
                file_hist[count] += 1
                paths_total += count
                rows += 1
            require(offset == len(data) and rows == 10395 and all(ranks), 'full matching universe')
            files.append({'file': name, 'sha256': hashlib.sha256(data).hexdigest(),
                          'records': rows, 'positive_paths': sum(k*n for k,n in file_hist.items()),
                          'endpoint_count_histogram': dict(sorted(file_hist.items()))})
    require(len(files) == 30, 'complete normalized hole geometry cover')
    result = {
        'status': 'PASS',
        'scope': 'Q4 T44 positive path cover and compatibility; Q5 sameface c=0 gluing',
        'imported_perfect_endpoint_proof': 'Q4_PERFECT_ENDPOINT_ABUNDANCE.md',
        'imported_exception_json': source.name,
        'imported_exception_json_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'imported_exception_count': len(exceptions),
        'import_dependency': 'The separate perfect-endpoint proof establishes that nonexceptional matchings have at most one bad odd endpoint and that these 4708 exception bad sets are exact.',
        'hitting_triples': [sorted(t) for t in triples],
        'records': 30*10395,
        'positive_paths': paths_total,
        'endpoint_count_histogram': dict(sorted(histogram.items())),
        'low_records': low_records,
        'low_relative_endpoint_sets': [{'endpoints': list(s), 'records': n}
                                       for s,n in sorted(low_sets.items())],
        'files': files,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'full_T44_5_claimed': False,
        'full_T15_claimed': False,
    }
    (ROOT/'t44_sameface_path_gluing_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','records','positive_paths','low_records','endpoint_count_histogram','low_relative_endpoint_sets')},indent=2))


if __name__ == '__main__':
    main()
