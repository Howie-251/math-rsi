"""Bounded two-return geometry check on the frozen 470 E16 residual rows."""

from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_DOUBLE_RETURN_BRIDGE_GEOMETRY import build_registry, donor_interface
from R7_E16_EVEN_HIGH_GAP_CHECK import receiver_plan
from R7_CONTROLLED_CYCLE_DONOR_PROBE import BITS


HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'R7_E16_DISTANCE2_SWITCH_CUT_CHECK.json'
OUTPUT = Path(__file__).with_suffix('.json')
CPU_LIMIT = 60
REPEATED_LIMIT = 8


def face(points, bit, side):
    return frozenset(v for v in points if bool(v & bit) == side)


def crosses(edge, bit):
    return edge is not None and bool((edge[0] ^ edge[1]) & bit)


def surviving(edge, outer, side, omitted):
    if face(edge, outer, side) == set(edge) and omitted.isdisjoint(edge):
        return edge
    return None


def prevents_exception(edge, bit, target_side, w):
    if edge is None:
        return False
    if crosses(edge, bit):
        return w not in face(edge, bit, target_side)
    return w in edge


def whole_interface(outer, minority, retained, marks, edge=None, allow_t15_odd=False):
    """Audited same-side Q6 gates, plus the corresponding exact exceptions."""
    majority = retained | marks
    s1 = []
    d3 = []
    for inner, bit in enumerate(BITS):
        if inner == outer:
            continue
        for side in (0, 1):
            sm, lg_set, u = (face(g, bit, side) for g in (minority, majority, marks))
            s, l = len(sm), len(lg_set)
            t, n = len(minority) - s, len(majority) - l
            record = dict(inner=inner, side=side, face_counts=[[s,l],[t,n]])
            if u == marks:
                if s in (0,1) and l == s + 5 and 1 <= t <= 16 and n == t - 1:
                    return dict(record, kind='Q6_same_side_majority_root')
                if (s,l) == (2,5) and 0 <= t <= 15 and n == t + 1:
                    return dict(record, kind='Q6_same_side_two_minority_roots')
                if (s,l,t,n) == (1,4,1,2):
                    a, = sm
                    w = a ^ bit
                    if prevents_exception(edge, bit, 1-side, w):
                        return dict(record, kind='Q6_T26_S1_forced_edge', root=a, mirror=w, edge=edge)
                    s1.append((inner, side, a, majority-lg_set))
                if allow_t15_odd and len(minority) == 1:
                    if s == 0 and l in (4,5):
                        return dict(record, kind=f'Q6_T15_D{l}')
                    if (s,l,t,n) == (1,4,0,1):
                        a, = sm
                        w = a ^ bit
                        if prevents_exception(edge, bit, 1-side, w):
                            return dict(record, kind='Q6_T15_D3_forced_edge', root=a, mirror=w, edge=edge)
                        d3.append((inner, side, next(iter(majority-lg_set))))
            if allow_t15_odd and (s,l,t,n,len(u)) == (1,2,0,3,1):
                a, = sm
                w = a ^ bit
                if w not in marks and prevents_exception(edge, bit, 1-side, w):
                    return dict(record, kind='Q6_T15_split_S2_forced_edge', root=a, mirror=w, edge=edge)
    for a,b in combinations(s1,2):
        if a[0] != b[0] and a[2] == b[2] and len(a[3] & b[3]) in (0,2):
            return dict(kind='Q6_T26_paired_S1', inner_sides=[a[:2],b[:2]], root=a[2])
    for a,b in combinations(d3,2):
        if a[0] != b[0] and a[2] == b[2]:
            return dict(kind='Q6_T15_shared_D3', inner_sides=[a[:2],b[:2]], outside_hole=a[2])
    return None


def make_search():
    lookup_t15, lookup_q5 = build_registry()

    @cache
    def donor(j, minority, retained, marks, edge):
        if len(minority) <= 1:
            plan = donor_interface(j, minority, retained, marks, lookup_t15)
            if plan:
                return plan
        return whole_interface(j, minority, retained, marks, edge, allow_t15_odd=True)

    @cache
    def receiver(j, minority, retained, marks, edge):
        if len(marks) == 2:
            plan = whole_interface(j, minority, retained, marks, edge)
            if plan:
                return dict(kind='whole_Q6', interface=plan), True
        counts = Counter()
        plan = receiver_plan(j, minority, retained, marks, lookup_q5, counts, 'E16')
        return (dict(kind='positive_split_Q5', **plan) if plan else None,
                bool(counts['E16_balanced_receiver_geometry']))

    def find(colors, edge, start):
        counts = Counter()
        for j, outer in enumerate(BITS):
            if process_time() - start >= CPU_LIMIT:
                raise TimeoutError
            for side in (0,1):
                for beta in (0,1):
                    a_minor = face(colors[1-beta], outer, side)
                    a_major = face(colors[beta], outer, side)
                    k = len(a_major)-len(a_minor)
                    if k < 4:
                        continue
                    counts[f'orientations_k{k}'] += 1
                    b_minor, b_major = colors[beta]-a_major, colors[1-beta]-a_minor
                    for X in combinations(sorted(a_major), k-2):
                        retained_a = a_major-frozenset(X)
                        Y = frozenset(v ^ outer for v in X)
                        b_edge = surviving(edge, outer, 1-side, Y)
                        for U in combinations(sorted(b_major), 2):
                            counts['source_choices'] += 1
                            V = frozenset(v ^ outer for v in U)
                            a_edge = surviving(edge, outer, side, V)
                            retained_b = b_major-frozenset(U)
                            rec, count_geometry = receiver(j, b_minor, retained_b, Y, b_edge)
                            counts['receiver_geometry'] += count_geometry
                            if rec is None:
                                continue
                            counts['receiver_supported'] += 1
                            supply = donor(j, a_minor, retained_a, V, a_edge)
                            if supply is not None:
                                return dict(k=k, outer=j, donor_side=side, donor_majority_parity=beta,
                                            X=X, U=U, donor_minority=sorted(a_minor),
                                            donor_retained=sorted(retained_a), donor_marks=sorted(V),
                                            receiver_minority=sorted(b_minor), receiver_retained=sorted(retained_b),
                                            receiver_marks=sorted(Y), donor=supply, receiver=rec), dict(counts)
        return None, dict(counts)

    return find


def run():
    start = process_time()
    source_bytes = SOURCE.read_bytes()
    source = json.loads(source_bytes)
    assert [len(t['uncovered']) for t in source['tables']] == [454,16]
    inputs = [(i, t, Z) for i, t in enumerate(source['tables']) for Z in t['uncovered']]
    find = make_search()
    completed = []
    status = 'complete'
    repeated = 0
    for i, table, Z in inputs:
        even = frozenset(Z) | frozenset(v ^ 64 for v in table['W'])
        odd = frozenset(table['Y']) | {64,67}
        edges = ((3,35),) if i == 0 else ((3,19),(3,35))
        branches = []
        try:
            for edge in edges:
                plan, counters = find((even, odd), edge, start)
                branches.append(dict(required_edge=edge, plan=plan, counters=counters))
        except TimeoutError:
            status = 'cpu_limit'
            break
        positive = all(row['plan'] for row in branches)
        completed.append(dict(table=i+1, Z=Z, positive=positive, branches=branches))
        no_geometry = all(not row['counters'].get('receiver_geometry') for row in branches)
        repeated = repeated + 1 if no_geometry else 0
        if repeated == REPEATED_LIMIT:
            status = 'repeated_no_receiver_geometry'
            break
    return dict(status=status, input_sha256=sha256(source_bytes).hexdigest(),
                completed=len(completed), positive=sum(r['positive'] for r in completed),
                uncovered=sum(not r['positive'] for r in completed), cpu_seconds=process_time()-start,
                input_limit=470, cpu_limit_seconds=CPU_LIMIT, repeated_limit=REPEATED_LIMIT,
                rows=completed, unvisited=[dict(table=i+1,Z=Z) for i,_,Z in inputs[len(completed):]])


if __name__ == '__main__':
    result = run()
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key:value for key,value in result.items() if key not in ('rows','unvisited')}))
