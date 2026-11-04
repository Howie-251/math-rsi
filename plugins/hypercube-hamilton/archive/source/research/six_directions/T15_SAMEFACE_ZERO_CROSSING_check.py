"""Independent finite certificate audit; imports no producer or prior checker.

Only writes the dedicated T15_SAMEFACE_ZERO_CROSSING_check.json result.
Positive witnesses suffice: no completeness claim for the listed path endpoints.
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parent
V = frozenset(range(16))
ODD = frozenset(x for x in V if x.bit_count() % 2)
N = frozenset((1, 2, 4, 8))
D3 = ODD - N
REPS = ((1, 2), (2, 4), (1, 14), (2, 14))


def need(value, message):
    if not value:
        raise RuntimeError(message)


def edge(x, y):
    return tuple(sorted((x, y)))


def all_matchings(vertices):
    if not vertices:
        yield ()
        return
    x, *rest = sorted(vertices)
    for y in rest:
        for tail in all_matchings(set(rest) - {y}):
            yield tuple(sorted(((x, y),) + tail))


def decode(mate, holes):
    need(len(mate) == 16 and {i for i, j in enumerate(mate) if j == 255} == set(holes),
         'mate holes')
    support = V - set(holes)
    need(all(mate[x] in support and mate[x] != x and mate[mate[x]] == x for x in support),
         'mate fixed-point-free involution')
    return tuple((x, mate[x]) for x in sorted(support) if x < mate[x])


def check_walk(walk, matching, support, cycle=False):
    need(len(walk) == len(support) and set(walk) == set(support), 'walk exact support')
    pairs = list(zip(walk, walk[1:]))
    if cycle:
        pairs.append((walk[-1], walk[0]))
    es = {edge(x, y) for x, y in pairs}
    need(len(es) == len(pairs) and set(matching) <= es, 'walk preserves matching')
    need(all((x ^ y).bit_count() == 1 for x, y in es - set(matching)), 'new edges short')


def transform(x, p):
    return sum(((x >> i) & 1) << p[i] for i in range(4))


def path_tables():
    summaries = []
    generation = json.loads((ROOT / 'q4_t15_path_abundance_generation.json').read_text())
    expected_generation = {tuple(r['avoid']): r for r in generation}
    need(len(generation) == 4 and set(expected_generation) == set(REPS), 'generation four families')
    for v, w in REPS:
        name = f'q4_t15_path_abundance_{v}_{w}.bin'
        data = (ROOT / name).read_bytes()
        holes = {0, 7, 11, 13, v, w}
        todo = set(all_matchings(V - holes))
        need(len(todo) == 945, 'independent 9!! count')
        cursor = count = paths = triangular = 0
        histogram = Counter()
        triangle_sets = Counter()
        while cursor < len(data):
            need(cursor + 17 <= len(data), 'complete row header')
            mate = data[cursor:cursor + 16]
            k = data[cursor + 16]
            cursor += 17
            matching = decode(mate, holes)
            need(matching in todo, 'unique matching in independently generated universe')
            todo.remove(matching)
            need(0 <= k <= 6 and cursor + 14 * k <= len(data), 'complete positive payload')
            ends = set()
            for _ in range(k):
                walk = data[cursor:cursor + 14]
                cursor += 14
                check_walk(walk, matching, V - {v, w})
                need(walk[0] == 0 and walk[-1] in ODD - {v, w}, 'path endpoint/root')
                need(walk[-1] not in ends, 'distinct listed endpoints')
                ends.add(walk[-1])
                paths += 1
            pqs = N - {v, w}
            triangle = {v, w} <= N and len(pqs) == 2 and tuple(sorted(pqs)) in matching
            if triangle:
                need(D3 <= ends, 'triangle has all four distance-three endpoints')
                triangular += 1
                triangle_sets[tuple(sorted(ends))] += 1
            else:
                need(ends == ODD - {v, w}, 'nontriangle has all six allowed odd endpoints')
            histogram[k] += 1
            count += 1
        need(cursor == len(data) and not todo and count == 945, 'full exact coverage')
        g = expected_generation[(v, w)]
        need(g['records'] == count and g['minimum'] == min(histogram)
             and g['hist'] == [histogram[i] for i in range(9)], 'generation census agreement')
        summaries.append(dict(file=name, records=count, paths=paths,
                              histogram=dict(sorted(histogram.items())),
                              triangular_records=triangular,
                              triangle_endpoint_sets=[dict(endpoints=list(s), count=c)
                                                      for s, c in sorted(triangle_sets.items())]))
    return summaries


def geometry():
    # All 560 marked geometries at root zero, without using old orbit counts.
    p4 = tuple(permutations(range(4)))
    orbit = {}
    for rep in REPS:
        orbit[rep] = {(frozenset(transform(x, p) for x in (7, 11, 13)),
                       frozenset(transform(x, p) for x in rep)) for p in p4}
    counter = Counter()
    for holes in combinations(sorted(ODD), 5):
        for avoid in combinations(holes, 2):
            available = frozenset(holes) - set(avoid)
            if available & N:
                counter['adjacent'] += 1
            else:
                hits = [rep for rep, states in orbit.items()
                        if (available, frozenset(avoid)) in states]
                need(len(hits) == 1, 'exactly one residual orbit')
                counter[str(hits[0])] += 1
    need(sum(counter.values()) == 560 and counter['adjacent'] == 520, 'geometry partition')
    return dict(at_root_zero=dict(counter),
                orbit_sizes={str(r): len(o) for r, o in orbit.items()},
                any_minority_root='translate root to 0; same coordinate permutation on both faces')


def certify_negative(matching, support):
    # Every required cycle is the union of its fixed matching and one disjoint
    # short perfect matching. Enumerate the latter, counting components directly.
    matching = set(matching)
    hist = Counter()

    def recurse(left, extra):
        if left:
            x = min(left)
            for y in sorted(left - {x}):
                if (x ^ y).bit_count() == 1 and edge(x, y) not in matching:
                    recurse(left - {x, y}, extra + [edge(x, y)])
            return
        graph = {x: set() for x in support}
        for x, y in list(matching) + extra:
            graph[x].add(y)
            graph[y].add(x)
        need(all(len(graph[x]) == 2 for x in support), 'negative complementary degree')
        unseen = set(support)
        components = 0
        while unseen:
            stack = [unseen.pop()]
            components += 1
            while stack:
                for y in graph[stack.pop()]:
                    if y in unseen:
                        unseen.remove(y)
                        stack.append(y)
        need(components != 1, 'claimed negative has Hamilton cycle')
        hist[components] += 1

    recurse(set(support), [])
    return dict(sorted(hist.items()))


def perfect_endpoint_census():
    negatives = {}
    tables = []
    for h in (1, 7):
        name = f'q4_distance{h.bit_count()}_avoided_table.bin'
        data = (ROOT / name).read_bytes()
        need(len(data) == 135135 * 30, 'perfect reduction table length')
        seen = set()
        bad = set()
        proofs = []
        for pos in range(0, len(data), 30):
            matching = decode(data[pos:pos + 16], {0, h})
            need(matching not in seen, 'base table distinct valid matching')
            seen.add(matching)
            cycle = data[pos + 16:pos + 30]
            if cycle == bytes([255]) * 14:
                bad.add(matching)
                proofs.append(dict(matching=matching,
                                   completion_components=certify_negative(matching, V - {0, h})))
            else:
                check_walk(cycle, matching, V - {0, h}, cycle=True)
        need(len(seen) == 135135, 'all 13!! valid matchings covered by cardinality')
        need(len(bad) == (51 if h == 1 else 53), 'negative count')
        negatives[h] = bad
        tables.append(dict(file=name, records=len(seen), positives=len(seen) - len(bad),
                           negatives=len(bad), negative_proofs=proofs))
    transported = {}
    transport = {}
    for y in ODD:
        source = 1 if y in N else 7
        p = next(p for p in permutations(range(4)) if transform(source, p) == y)
        transported[y] = {tuple(sorted(edge(transform(a, p), transform(b, p)) for a, b in m))
                          for m in negatives[source]}
        transport[y] = p
    candidates = defaultdict(set)
    inverse_instances = 0
    for y, bad in transported.items():
        for m in bad:
            for a, b in m:
                for u, z in ((a, b), (b, a)):
                    p = tuple(sorted((set(m) - {(a, b)}) | {edge(0, u), edge(y, z)}))
                    need(len(p) == 8 and sorted(x for e in p for x in e) == list(range(16)),
                         'inverse image perfect matching')
                    candidates[p].add(y)
                    inverse_instances += 1
    saved = json.loads((ROOT / 'q4_perfect_endpoint_abundance_check.json').read_text())
    saved_rows = {tuple(map(tuple, r['matching'])): set(r['bad_odd_endpoints'])
                  for r in saved['all_exceptional_matchings']}
    need(len(saved_rows) == len(saved['all_exceptional_matchings']), 'saved census has no duplicate rows')
    need(set(candidates) == set(saved_rows), 'saved census candidate universe agrees')
    hist = Counter()
    d3hist = Counter()
    minsets = Counter()
    for p, invbad in candidates.items():
        mate = {x: y for a, b in p for x, y in ((a, b), (b, a))}
        bad = set()
        for y in ODD:
            if mate[0] == y:
                bad.add(y)
            else:
                a, b = mate[0], mate[y]
                reduced = tuple(sorted(set(p) - {edge(0, a), edge(y, b)} | {edge(a, b)}))
                if reduced in transported[y]:
                    bad.add(y)
        need(bad == invbad | ({mate[0]} & ODD), 'forward inverse equivalence')
        need(bad == saved_rows[p], 'saved exact endpoint row agrees')
        good = ODD - bad
        need(len(good) >= 4 and good & D3, 'perfect endpoint bounds')
        hist[len(bad)] += 1
        d3hist[len(good & D3)] += 1
        if len(good) == 4:
            minsets[tuple(sorted(good))] += 1
    need(len(candidates) == 4708 and inverse_instances == 5824, 'inverse coverage count')
    need(saved['max_bad_odd_endpoints'] == max(hist)
         and saved['minimum_good_distance_three_endpoints'] == min(d3hist), 'saved bounds agree')
    return dict(tables=tables, inverse_instances=inverse_instances,
                exceptional_perfect_matchings=len(candidates),
                exceptional_bad_endpoint_histogram=dict(sorted(hist.items())),
                exceptional_good_distance_three_histogram=dict(sorted(d3hist.items())),
                minimum_endpoint_sets=[dict(endpoints=s, count=c) for s, c in sorted(minsets.items())],
                outside_candidate_universe='At most root partner is bad; hence >=7 good odd and >=3 good distance-three endpoints',
                saved_all_4708_rows_agree=True, transport=transport)


def main():
    names = ['q4_t15_path_abundance.cpp', 'q4_t15_path_abundance_generation.json',
             'Q4_T15_CLASSIFICATION.md', 'Q4_PERFECT_ENDPOINT_ABUNDANCE.md',
             'q4_perfect_endpoint_abundance_check.py', 'q4_perfect_endpoint_abundance_check.json',
             'T44_Q5_CLOSURE_DRAFT.md', 'T44_Q5_CLOSURE_REVIEW.json',
             'q4_distance1_avoided_table.bin', 'q4_distance3_avoided_table.bin']
    names += [f'q4_t15_path_abundance_{v}_{w}.bin' for v, w in REPS]
    hashes = {n: 'sha256:' + hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in names}
    t44 = json.loads((ROOT / 'T44_Q5_CLOSURE_REVIEW.json').read_text())
    need(t44['verdict'] == 'PASS' and t44['audited_input_hashes']['T44_Q5_CLOSURE_DRAFT.md']
         == hashes['T44_Q5_CLOSURE_DRAFT.md'], 'T44 theorem import current PASS provenance')
    result = dict(status='PASS', generated_at=datetime.now(timezone.utc).isoformat(),
                  audit_skill='proof-checker', review_independence='same-family',
                  acceptance_status='provisional', input_hashes=hashes,
                  paths=path_tables(), geometry=geometry(), perfect=perfect_endpoint_census(),
                  import_scope='T44_5 used only for adjacent available hole; full T44 proof not rerun',
                  full_Q5_T15_proved=False, full_P6_proved=False,
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    target = ROOT / 'T15_SAMEFACE_ZERO_CROSSING_check.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(status=result['status'], records=sum(t['records'] for t in result['paths']),
                         paths=sum(t['paths'] for t in result['paths']),
                         triangular=sum(t['triangular_records'] for t in result['paths']),
                         perfect_exceptions=result['perfect']['exceptional_perfect_matchings']), indent=2))


if __name__ == '__main__':
    main()
