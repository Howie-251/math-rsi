#!/usr/bin/env python3
"""Exact orbital-union domain and one bounded degree-eight enumeration."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import argparse
import json
import os
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'coset60_s5_c2_run'
FAMILIES = ('S5', 'A5_times_C2')


def dump(path, data):
    path.write_text(json.dumps(data, indent=2) + '\n')


def resources(start):
    r = resource.getrusage(resource.RUSAGE_SELF)
    return dict(user_cpu_seconds=r.ru_utime, system_cpu_seconds=r.ru_stime,
                total_process_cpu_seconds=r.ru_utime+r.ru_stime,
                wall_since_main_seconds=time.monotonic()-start, threads=1)


def make_domain(name):
    identity = tuple(range(5))
    involution = (1, 0, 3, 2, 4)
    perms = list(permutations(range(5)))
    even = [p for p in perms if sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
    elements = [(p, 0) for p in perms] if name == 'S5' else [(p, b) for p in even for b in range(2)]
    index = {g: i for i, g in enumerate(elements)}
    assert len(elements) == 120 and elements[0] == (identity, 0)

    def mul(i, j):
        p, a = elements[i]
        q, b = elements[j]
        return index[tuple(p[q[k]] for k in range(5)), a ^ b]

    inverses = []
    for i, (p, b) in enumerate(elements):
        q = [0]*5
        for k, x in enumerate(p):
            q[x] = k
        j = index[tuple(q), b]
        assert mul(i, j) == mul(j, i) == 0
        inverses.append(j)
    h = index[involution, 0]
    assert mul(h, h) == 0 and h != 0
    cosets = sorted({tuple(sorted((g, mul(g, h)))) for g in range(120)})
    assert len(cosets) == 60 and cosets[0] == tuple(sorted((0, h)))
    coset_of = {g: c for c, members in enumerate(cosets) for g in members}
    representatives = [c[0] for c in cosets]
    suborbits = []
    suborbit_of = {}
    for c in range(1, 60):
        if c in suborbit_of:
            continue
        orbit = sorted({c, coset_of[mul(h, representatives[c])]})
        oid = len(suborbits)
        for x in orbit:
            assert x != 0 and x not in suborbit_of
            suborbit_of[x] = oid
        suborbits.append(orbit)
    assert Counter(map(len, suborbits)) == Counter({1: 3, 2: 28})
    inverse_orbits = []
    for orbit in suborbits:
        targets = {suborbit_of[coset_of[inverses[representatives[c]]]] for c in orbit}
        assert len(targets) == 1
        inverse_orbits.append(targets.pop())
    assert all(inverse_orbits[inverse_orbits[i]] == i for i in range(len(suborbits)))
    used = set()
    blocks = []
    for i, orbit in enumerate(suborbits):
        if i in used:
            continue
        inverse = inverse_orbits[i]
        ids = sorted({i, inverse})
        used.update(ids)
        roots = sorted({c for j in ids for c in suborbits[j]})
        rows = []
        for c, g in enumerate(representatives):
            neighbors = {coset_of[mul(g, representatives[s])] for s in roots}
            other_rep = cosets[c][1]
            assert neighbors == {coset_of[mul(other_rep, representatives[s])] for s in roots}
            assert c not in neighbors and len(neighbors) == len(roots)
            rows.append(sum(1 << x for x in neighbors))
        assert all(bool(rows[x] & (1 << y)) == bool(rows[y] & (1 << x))
                   for x in range(60) for y in range(60))
        blocks.append(dict(block_id=len(blocks), directed_suborbit_ids=ids,
                          valency=len(roots), root_neighbors=roots, adjacency_rows=rows))
    for x in range(60):
        seen = 0
        for block in blocks:
            assert not (seen & block['adjacency_rows'][x])
            seen |= block['adjacency_rows'][x]
        assert seen == ((1 << 60)-1) ^ (1 << x)
    counts = [1] + [0]*8
    for block in blocks:
        d = block['valency']
        for k in range(8, d-1, -1):
            counts[k] += counts[k-d]
    # Direct products/permutation cycle orders also verify no element has order 15.
    orders = []
    for g in range(120):
        power, order = g, 1
        while power:
            power = mul(power, g)
            order += 1
        orders.append(order)
    assert 15 not in orders
    return dict(family=name, group_order=120, degree=60, stabilizer=[0, h],
                group_elements=[dict(permutation=p, factor=b) for p, b in elements],
                cosets_gH=cosets, coset_representatives=representatives,
                directed_suborbits=suborbits, inverse_suborbit_ids=inverse_orbits,
                orbital_blocks=blocks, valency_histogram=dict(Counter(b['valency'] for b in blocks)),
                degree_eight_unions=counts[8], group_element_order_histogram=dict(Counter(orders)),
                disjoint_complete_symmetric_orbital_partition_verified=True,
                representative_independence_verified=True)


def profile():
    start_cpu, start = time.process_time(), time.monotonic()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'profile.json').exists(), 'No unchanged profile repeat'
    reports = {}
    for name in FAMILIES:
        data = make_domain(name)
        dump(OUT/(name+'.domain.json'), data)
        reports[name] = {k: data[k] for k in ['degree_eight_unions', 'valency_histogram', 'group_element_order_histogram']}
    result = dict(complete=True, phase='finite_domain_only', families=reports,
                  cpu_seconds=time.process_time()-start_cpu, wall_seconds=time.monotonic()-start,
                  cpu_budget_seconds=5, resources=resources(start), graph_searches=0)
    dump(OUT/'profile.json', result)
    print(json.dumps(result), flush=True)


def search_one(name):
    data = json.loads((OUT/(name+'.domain.json')).read_text())
    blocks = data['orbital_blocks']
    rows = [b['adjacency_rows'] for b in blocks]
    weights = [b['valency'] for b in blocks]
    suffix = [0]*(len(blocks)+1)
    for i in range(len(blocks)-1, -1, -1):
        suffix[i] = suffix[i+1]+weights[i]
    histogram = Counter()
    combination_types = Counter()
    best_size, best_blocks = -1, None
    count = 0

    def visit(start, need, chosen, neighbors):
        nonlocal best_size, best_blocks, count
        if not need:
            assert neighbors.bit_count() == 8 and not (neighbors & 1)
            ball = neighbors | 1
            pending = neighbors
            while pending:
                bit = pending & -pending
                x = bit.bit_length()-1
                for b in chosen:
                    ball |= rows[b][x]
                pending ^= bit
            size = ball.bit_count()
            histogram[size] += 1
            combination_types[tuple(sorted(weights[b] for b in chosen))] += 1
            count += 1
            if size > best_size:
                best_size, best_blocks = size, chosen[:]
            return
        if suffix[start] < need:
            return
        for b in range(start, len(blocks)):
            if weights[b] <= need:
                visit(b+1, need-weights[b], chosen+[b], neighbors | rows[b][0])

    cpu, wall = time.process_time(), time.monotonic()
    visit(0, 8, [], 0)
    assert count == data['degree_eight_unions']
    adjacency = []
    for x in range(60):
        row = 0
        for b in best_blocks:
            row |= rows[b][x]
        assert row.bit_count() == 8
        adjacency.append(row)
    edges = [(x, y) for x in range(60) for y in range(x+1, 60) if adjacency[x] & (1 << y)]
    assert len(edges) == 240
    candidate = dict(n=60, edges=edges, family=name, selected_orbital_blocks=best_blocks,
                     root_radius_two_ball=best_size, coset_domain_file=name+'.domain.json')
    path = OUT/(name+'.best.json')
    dump(path, candidate)
    path.with_suffix('.edges').write_text('60 240\n'+''.join(f'{x} {y}\n' for x, y in edges))
    return dict(complete=True, family=name, expected_unions=data['degree_eight_unions'],
                tested_unions=count, root_ball_histogram=dict(sorted(histogram.items())),
                selected_valency_type_counts=[dict(valencies=list(k), count=v) for k, v in sorted(combination_types.items())],
                diameter_two_count=histogram[60], maximum_root_radius_two_ball=best_size,
                best_orbital_blocks=best_blocks, cpu_seconds=time.process_time()-cpu,
                wall_seconds=time.monotonic()-wall)


def enumerate_all():
    start_cpu, start = time.process_time(), time.monotonic()
    assert (OUT/'profile.json').exists()
    assert not (OUT/'result.json').exists(), 'One exhaustive run, no unchanged repeat'
    reports = {name: search_one(name) for name in FAMILIES}
    result = dict(complete=True, families=reports, cpu_budget_seconds=30,
                  cpu_seconds=time.process_time()-start_cpu, wall_seconds=time.monotonic()-start,
                  resources=resources(start), attempts=1)
    dump(OUT/'result.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['profile', 'enumerate'])
    args = parser.parse_args()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    limit = 5 if args.phase == 'profile' else 30
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit+1))
    (profile if args.phase == 'profile' else enumerate_all)()
