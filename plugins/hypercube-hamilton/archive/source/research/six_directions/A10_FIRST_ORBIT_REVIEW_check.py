"""Independent small-domain audit. Never executes/mutates producer inputs."""
import hashlib
import itertools as it
import json
from pathlib import Path

R = Path(__file__).resolve().parent
NAMES = ['A10_FIRST_ORBIT_ANALYTIC_CLOSURE.md',
         'A10_first_orbit_geometry_check.py', 'A10_first_orbit_geometry_check.json',
         'Q4_GENERAL_AUGMENTATION.md', 'Q4_T15_CLASSIFICATION.md',
         'A8_BRIDGE_INPUTS_REVIEW.md', 'A8_BRIDGE_INPUTS_REVIEW.json',
         'Q4_T15_CLASSIFICATION_REVIEW.md', 'Q4_T15_CLASSIFICATION_REVIEW.json']
def hashes():
    return {n: hashlib.sha256((R/n).read_bytes()).hexdigest() for n in NAMES}
before = hashes()
record = json.loads((R/NAMES[2]).read_text())
assert before[NAMES[1]] == record['checker_sha256']
even = {0, 3, 5, 6, 15, 23}
odd = {8, 16, 25, 26}
holes = even | odd
assert all(bin(v).count('1') % 2 == 0 for v in even)
assert all(bin(v).count('1') % 2 == 1 for v in odd)
assert all(bin(v^w).count('1') != 1 for v in even-{0} for w in odd)
bits = [1, 2, 4, 8, 16]
cut_rows = []
for b, a in [(8, 15), (16, 23)]:
    A = {v for v in range(32) if v & b == 0}
    B = set(range(32))-A
    assert (len(even&A), len(odd&A), len(even&B), len(odd&B)) == (5, 1, 1, 3)
    M = {a^j for j in bits if j != b}
    assert M == {v^b for v in (even&A)-{0}}
    assert M.isdisjoint(holes)
    closed = B-M-holes
    assert len(closed) == 8
    producer = next(r for r in record['cuts'] if r['cut_bit'] == b)
    assert sorted(M) == producer['candidates']
    assert sorted(closed) == producer['closed_outside']
    assert sorted(even&A) == producer['A_majority_holes']
    assert sorted(odd&A) == producer['A_minority_holes']
    assert a == producer['singleton_majority_B']
    assert len(producer['choices']) == 6
    for pair in it.combinations(sorted(M), 2):
        row = next(r for r in producer['choices'] if r['selected_bridges'] == list(pair))
        assert row['T15_obstruction_edge'] == sorted(M-set(pair))
        assert row['selected_A_holes'] == sorted(x^b for x in pair)
    cut_rows.append(dict(bit=b, candidates=sorted(M), closed=sorted(closed)))
intersection = set(cut_rows[0]['closed']) & set(cut_rows[1]['closed'])
assert intersection == {24, 27, 28, 29, 30} and not intersection&holes
assert sorted(intersection) == record['odd_closed_intersection']

# Image construction by explicitly moving a vertex's set bits.
orbit = set()
for order in it.permutations(bits):
    image = {v: sum(order[i] for i in range(5) if v & bits[i]) for v in range(32)}
    orbit.add((tuple(sorted(image[v] for v in even-{0})),
               tuple(sorted(image[v] for v in odd))))
assert len(orbit) == 30 == record['orbit_size']

# Generate every partial matching independently by leave-unmatched/pair recursion.
def partial(vertices):
    if not vertices:
        yield ()
        return
    v, *rest = vertices
    yield from partial(rest)
    for w in rest:
        for tail in partial([x for x in rest if x != w]):
            yield ((v, w),)+tail
abstract = list(partial(list(range(4))))
assert len(abstract) == 10
counts = []
for fixed in abstract:
    good = [s for s in it.combinations(range(4), 2)
            if tuple(x for x in range(4) if x not in s) not in fixed]
    occurrences = [sum(v in s for s in good) for v in range(4)]
    assert len(good) >= 4 and min(occurrences) >= 2
    counts.append(dict(fixed_edges=[list(e) for e in fixed],
                       nonfixed_choices=len(good), minimum_selected_occurrences=min(occurrences)))
assert sorted(counts, key=str) == sorted(record['candidate_choice_cover'], key=str)

# c<=10 gives 1<=d<=6. All contracted alternating cycles are covered by
# fixing D canonically, then enumerating Q; labelled parallel edges count.
def perfect(vertices):
    if not vertices:
        yield ()
        return
    v, *rest = vertices
    for w in rest:
        for tail in perfect([x for x in rest if x != w]):
            yield ((v, w),)+tail
def forest(n, edges):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for v, w in edges:
        u, z = root(v), root(w)
        if u == z:
            return False
        parent[u] = z
    return True
cycle_rows = []
for d in range(1, 7):
    D = tuple((2*i, 2*i+1) for i in range(d))
    connected = checked = 0
    for Q in perfect(list(range(2*d))):
        # Two perfect matchings are a union of alternating cycles. Deleting
        # one D edge is a forest iff that union was a single cycle.
        if not forest(2*d, Q+D[:-1]):
            continue
        connected += 1
        for mask in range((1<<d)-1):
            J = tuple(D[i] for i in range(d) if mask>>i & 1)
            assert forest(2*d, Q+J)
            checked += 1
    cycle_rows.append(dict(d=d, alternating_cycles=connected, proper_subsets_checked=checked))
assert hashes() == before
out = dict(status='PASS', audited_input_hashes=before, cuts=cut_rows,
           odd_covered_intersection=sorted(intersection), orbit_size=len(orbit),
           abstract_four_candidate_matchings=10, choice_rows=counts,
           proper_subset_multigraph_checks=cycle_rows,
           original_Q5_matching_instances_enumerated=0,
           Hamilton_cycle_searches=0, production_inputs_unchanged=True)
(R/'A10_FIRST_ORBIT_REVIEW_check.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['audited_input_hashes','choice_rows']}))
